#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  views.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  


SCR_VERSION = "1.0.5"

import logging
from io import StringIO
main_log_stream = StringIO()
logger = logging.getLogger("ywsapp")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(main_log_stream))
logger.handlers[-1].setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger.info(f"--- starting app, SCR version is {SCR_VERSION} ---")


from django.shortcuts import render, redirect
try:
    from django.http import HttpResponse, JsonResponse
    from django.utils import timezone
    from django.contrib.auth import get_user
    from .forms import UserLoginForm, NewUserForm, UserInfoForm
    from .models import User
    from django.contrib.auth import authenticate, login, logout
    import uuid
    import json
    import jsons
    from .resmanager import ResourcesManager
    from .audiocore.soundgen import SoundGenerator
    from speech_manager import SpeechManager
    from .workout_manager import WorkoutManager
except:
    logger.exception("Exception while loading main view modules:")

# GLOBAL VARIABLES still here...
SOUND_STREAMS = {}


def wm_id(request):
    #return request.session.session_key if request.user.id is None else request.user.id
    if request.user.id is None:
        return request.session.session_key
    return get_user(request).id

def do_index(request):
    show_registration_form = False
    snack_text = "Some erors occured. Please, check logs" if 'Traceback (most recent call last)' in main_log_stream.getvalue() else None

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
        "main_bg_image":ResourcesManager().main_bg_image(),
        "workout_complete":workout_complete,
        "snack_text": snack_text,
        "scr_version": SCR_VERSION
    })

# Create your views here.
def index(request):
    try:
        return do_index(request)
    except:
        logger.exception("exception while rendering main view:")
        return logs(request)

def logs(request):
    return HttpResponse(f"<pre>{main_log_stream.getvalue()}</pre>")

def active(request):
    # Request active page -- so, start a new workout. Cache WS's id here, to check it in index page when done
    import uuid
    request.session['active_wuid'] = uuid.uuid4().hex
    request.session['workout_id'] = request.GET.get('id')

    return render(request, 'ywsapp/active.html', {
        "workout_id": request.GET.get('id'),
        "active_wuid": request.session['active_wuid'],
        "active_bg_image":ResourcesManager().active_bg_image(),
        "scr_version": SCR_VERSION,
        "debug": False
    })


def logout_view(request):
    logout(request)
    return redirect('/')


def list_workouts(request):
    this_user = get_user(request) if request.user.is_authenticated else None
    wrks = WorkoutManager().list_workouts(wm_id(request))
    wrks = map(lambda x: jsons.dump(x.build(this_user, x.id)), wrks)


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
    logger.info(f"get workout: {workout_id}, no_sounds: {no_sounds}")

    workout = WorkoutManager().load_workout(wm_id(request), workout_id)
    if workout is None:
        return JsonResponse({}, safe = False, status = 404)

    this_user = get_user(request) if request.user.is_authenticated else None
    result = workout

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


def get_workout(request):
    workout_id = request.GET.get('id')
    logger.info(f"get workout: {workout_id}")

    result = WorkoutManager().load_workout(wm_id(request), workout_id)
    if result is None:
        return JsonResponse({}, safe = False, status = 404)

    this_user = get_user(request) if request.user.is_authenticated else None
    #result = workout['default'].build(this_user, workout_id)

    #if this_user:
    #    recs = UserWorkoutProps.objects.filter(user = this_user)
    #    for r in recs:
    #        result.apply_prop(r.prop_id, r.value)

    try:
        voice_acting = User.objects.filter(username=this_user).values()[0]['voice_acting']
    except:
        voice_acting = 0

    #import pprint
    #pprint.PrettyPrinter(indent=4).pprint(result)
    SpeechManager().generate_sounds(result, voice_acting)

    del result.sets   # ToDo: maybe this inside build() of workout class?

    # Generate sound, store id
    sound_id = str(uuid.uuid4())
    result.sound_id = sound_id
    result = jsons.dump(result)
    SOUND_STREAMS[sound_id] = SoundGenerator().generate(result)
    
    #import pprint
    #pprint.PrettyPrinter(indent=4).pprint(result)
    return JsonResponse(result, safe = False, status = 200)



# ToDo: cache requests
def modify_workout_params(request):
    if request.method != "POST":
        return JsonResponse({}, safe = False, status = 200)
    
    try:
        params = json.loads(request.body.decode('utf-8'))
    except:
        return JsonResponse({}, safe = False, status = 400)
    

    logger.debug(f"modify_workout_params: '{params}' by user {get_user(request)}")
    try:
        WorkoutManager().edit_property(wm_id(request), params['property_id'], params['value'])
    except ValueError:
        return JsonResponse({}, safe = False, status = 406)
    except:
        logger.exception("Exception while modify workout params")
        return JsonResponse({}, safe = False, status = 400)
    
    # ToDo: alert user if he is anon, that parameters not saved in DB
    return JsonResponse({}, safe = False, status = 200) # Not 200 here


def sound(request):
    sound_id = request.GET.get('id')
    sound_check = request.GET.get('check', None)

    logger.debug(f"Sound id is {sound_id}, check is: {(sound_check)}")

    if sound_id not in SOUND_STREAMS.keys():
        logger.error(f"Sound id {sound_id} not in SOUND_STREAMS")
        return JsonResponse({}, safe = False, status = 404)
    
    result = SOUND_STREAMS[sound_id]
    if not result.sound_ready():
        return JsonResponse({}, safe = False, status = 503)
    
    if sound_check == 'true':
        return JsonResponse({}, safe = False, status = 200)
    
    logger.debug("Sound task done, result requested")
    result = result.get_result()

    chunk_size = 8192
    from io import BytesIO
    from wsgiref.util import FileWrapper
    from django.http import StreamingHttpResponse

    response = StreamingHttpResponse(
       FileWrapper(BytesIO(result), chunk_size),
       content_type="audio/mp3"
   )

    response['Accept-Ranges'] = 'bytes' # Enable range requests
    response['Content-Length'] = len(result)
    logger.debug(f"return sound stream, length {response['Content-Length']} bytes")
    return response
