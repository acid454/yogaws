#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  views.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import traceback
from django.shortcuts import render, redirect
try:
    from django.http import HttpResponse, JsonResponse
    from django.template import loader
    from django.utils import timezone
    from django.contrib.auth import get_user
    from .forms import UserLoginForm, NewUserForm, UserInfoForm
    from .models import User, UserWorkoutProps
    from django.contrib.auth import authenticate, login, logout
    import uuid
    import json
    import jsons
    from .resmanager import ResourcesManager
    from .audiocore.soundgen import SoundGenerator
    import_exception = None
except:
    import_exception = traceback.format_exc()

#import random
import hashlib


SCR_VERSION = "1.0.2"
WORKOUTS = None
SOUND_STREAMS = {}


def do_index(request):
    show_registration_form = False
    snack_text = None

    if request.method == "POST":
        if "password" in request.POST.keys():
            # Processing login form
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username =username, password = password)

                if user is not None:
                    login(request,user)
            else:
                show_registration_form = True
        elif 'submit_user_info' in request.POST.keys():
            # Processing user info form
            form = UserInfoForm(request.POST)
            if form.is_valid():
                request.user.kegel_timer = form.cleaned_data['kegel_timer']
                request.user.voice_acting = form.cleaned_data['voice_acting']
                request.user.shavasana_acting = form.cleaned_data['shavasana_acting']
                request.user.metronome = form.cleaned_data['metronome']
                request.user.save()
            else:
                snack_text = form.errors.as_text()
        else:
            # Processing registration form
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
            else:
                snack_text = form.errors.as_text()
    
    # Check, if this is completed workout
    active_wuid = request.GET.get('wuid')
    session_wuid = request.session.get('active_wuid', None)
    request.session['active_wuid'] = None
    workout_complete = (active_wuid is not None) and (active_wuid == session_wuid)
    if workout_complete and request.user.is_authenticated:
        request.user.complete_workouts += 1
        request.user.last_workout_id = request.session['workout_id']
        request.user.last_workout_date = timezone.now()
        request.user.save()

    return render(request, 'ywsapp/index.html', {
        "form_login":UserLoginForm(),
        "form_register": NewUserForm(),
        "form_user_info": UserInfoForm(instance= request.user if request.user.is_authenticated else None),
        "show_registration_form": show_registration_form,
        "main_bg_image":ResourcesManager().active_bg_image(),
        "workout_complete":workout_complete,
        "snack_text": snack_text,
        "scr_version": SCR_VERSION
    })

# Create your views here.
def index(request):
    if import_exception is not None:
        return HttpResponse(f"<pre>{import_exception}</pre>")
    
    try:
        return do_index(request)
    except:
        return HttpResponse(f"<pre>{str(traceback.format_exc())}</pre>")


def active(request):
    # Request active page -- so, start a new workout. Cache WS's id here, to check it in index page when done
    import uuid
    request.session['active_wuid'] = uuid.uuid4().hex
    request.session['workout_id'] = request.GET.get('id')

    return render(request, 'ywsapp/active.html', {
        "workout_id": request.GET.get('id'),
        "active_wuid": request.session['active_wuid'],
        "active_bg_image":ResourcesManager().active_bg_image(),
        "scr_version": SCR_VERSION
    })

def logout_view(request):
    logout(request)
    return redirect('/')


# --------========= WORKOUTS MANAGE ==========-------------------------
def _update_workouts():
    global WORKOUTS
    
    #-------------------------------------------------------------------
   
    WORKOUTS = {}
    for f in ResourcesManager().workout_files():
        #if f != "01_test.py": continue
        workouts = __import__(f[:-3]).do_load_workouts()
        for w in workouts:
            wid = hashlib.md5((f + ':' + w.__name__).encode()).hexdigest()
            WORKOUTS[wid] = { 'class':w, 'filenm':f, 'wid':wid }

def list_workouts(request):
    if WORKOUTS is None:
        _update_workouts()
    wrks = sorted( WORKOUTS.values(), key = lambda v: v['filenm'] )
    wrks = map(lambda x: jsons.dump(x['class']().build(None, x['wid']) ), wrks)
    
    result = {}
    for w in wrks:
        if w['group'] in result.keys():
            result[w['group']].append(w)
        else:
            result[w['group']] = [w]
    
    
    #result = list(map(lambda k: ( WORKOUTS[k]['class']().build(k), WORKOUTS.keys()))
    #result = sorted( result, key = lambda k: k.FILENAME )
    #result = list(map(lambda x: jsons.dump(x), result))

    #import pprint
    #pprint.PrettyPrinter(indent=4).pprint(result)
    return JsonResponse(result, safe = False, status = 200)


def view_workout(request):
    workout_id = request.GET.get('id')
    no_sounds = request.GET.get('no_sounds', False)

    # ToDo: this as decorator?
    if WORKOUTS is None:
        _update_workouts()

    if workout_id in WORKOUTS.keys():
        from speech_manager import SpeechManager

        this_user =  get_user(request) if request.user.is_authenticated else None
        result = WORKOUTS[workout_id]['class']().build(this_user, workout_id)

        if this_user:
            recs = UserWorkoutProps.objects.filter(user = this_user)
            for r in recs:
                result.apply_prop(r.prop_id, r.value)

        try:
            voice_acting = User.objects.filter(username=this_user).values()[0]['voice_acting']
        except:
            voice_acting = 0

        if not no_sounds:
            SpeechManager().generate_sounds(result, voice_acting)
        result = jsons.dump(result)
        
        #if not no_sounds:
        #    import pprint
        #    pprint.PrettyPrinter(indent=4).pprint(result)
        return JsonResponse(result, safe = False, status = 200)
    return JsonResponse({}, safe = False, status = 200)  # Not 200 here


def get_workout(request):
    workout_id = request.GET.get('id')

    # ToDo: this as decorator?
    if WORKOUTS is None:
        _update_workouts()
    
    if workout_id not in WORKOUTS.keys():
        return JsonResponse({}, safe = False, status = 404)

    from speech_manager import SpeechManager  #ToDo: remove to imports
    this_user =  get_user(request) if request.user.is_authenticated else None
    result = WORKOUTS[workout_id]['class']().build(this_user, workout_id)

    if this_user:
        recs = UserWorkoutProps.objects.filter(user = this_user)
        for r in recs:
            result.apply_prop(r.prop_id, r.value)

    try:
        voice_acting = User.objects.filter(username=this_user).values()[0]['voice_acting']
    except:
        voice_acting = 0

    #import pprint
    #pprint.PrettyPrinter(indent=4).pprint(result)
    SpeechManager().generate_sounds(result, voice_acting)

    # Generate sound, store id
    sound_id = str(uuid.uuid4())
    result.sound_id = sound_id

    print('-'*80, ' sound generation starts...')
    SOUND_STREAMS[sound_id] = SoundGenerator().generate(result)
    print(type(SOUND_STREAMS[sound_id]))
    print('-'*80, ' sound generation complete')
    

    
    del result.sets   # ToDo: maybe this inside build() of workout class?
    
    #import pprint
    #pprint.PrettyPrinter(indent=4).pprint(result)
    result = jsons.dump(result)
    return JsonResponse(result, safe = False, status = 200)



# ToDo: cache requests
def modify_workout_params(request):
    if (request.method != "POST") or (not request.user.is_authenticated):
        return JsonResponse({}, safe = False, status = 200)
    
    try:
        params = json.loads(request.body.decode('utf-8'))
    except:
        return JsonResponse({}, safe = False, status = 400)
    
    #print(params)
    try:
        for workout_id in WORKOUTS.keys():
            w = WORKOUTS[workout_id]['class'] #().build(workout_id)
            p = w.find_property_by_id(params['property_id'])
            if p is not None:
                break
        
        if p is None:
            return JsonResponse({}, safe = False, status = 404)
        
        #print(dir(request.user.id), request.user.is_authenticated)
        #print(get_user(request))
        try:
            v = int(params['value'])
            if (v < p.value_min) or (v > p.value_max):
                raise Exception()
        except:
            return JsonResponse({}, safe = False, status = 406)
        
        try:
            rec = UserWorkoutProps.objects.get(user = get_user(request), prop_id = params['property_id'])
        except:
            rec = UserWorkoutProps(user = get_user(request), prop_id = params['property_id'])
        
        rec.value = v
        rec.save()
        return JsonResponse({}, safe = False, status = 200)
    except:
        pass

    return JsonResponse({}, safe = False, status = 200) # Not 200 here

def sound(request):
    sound_id = request.GET.get('id')
    print(f"Search and returns sound id {sound_id}")

    chunk_size = 8192
    from io import BytesIO
    from wsgiref.util import FileWrapper
    from django.http import StreamingHttpResponse


    response = StreamingHttpResponse(
       FileWrapper(BytesIO(SOUND_STREAMS[sound_id]), chunk_size),
       content_type="audio/mp3"
   )

    response['Accept-Ranges'] = 'bytes' # Enable range requests
    response['Content-Length'] = len(SOUND_STREAMS[sound_id])
    print(f"Return sound stream, length {response['Content-Length']} bytes")
    return response
