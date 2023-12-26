from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.utils import timezone
from .forms import UserLoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
import jsons
import random
import os


WORKOUTS = None
SPEECH_MANAGER = None
GLOBAL_PATHS = [
    ["yoga", "workouts"],       # Note: workouts must be [0]
    ["yoga", "sets"],
    ["yoga", "common"],
    ["yoga", "containers"],
    ["yoga"]
]

BACKGROUND_IMAGES = os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                            'static', 'ywsapp', 'res', 'mainbg'))


# Create your views here.
def index(request):
    show_registration_form = False
    snack_text = None

    # Handle background image
    background_image = (BACKGROUND_IMAGES[random.randrange(len(BACKGROUND_IMAGES))])
    
    #print(dir(request))
    #print(dir(request.user), request.user.is_authenticated)
    #print(dir(request.session))

    if request.method == "POST":
        if "password" in request.POST.keys():
            # Processing login form
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                print("Login valid: " + str(request))
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username =username, password = password)

                if user is not None:
                    login(request,user)
            else:
                show_registration_form = True
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
        "show_registration_form": show_registration_form,
        "main_bg_image":background_image,
        "workout_complete":workout_complete,
        "snack_text": snack_text
    })

def active(request):
    # Request active page -- so, start a new workout. Cache WS's id here, to check it in index page when done
    import uuid
    request.session['active_wuid'] = uuid.uuid4().hex
    request.session['workout_id'] = request.GET.get('id')
    return render(request, 'ywsapp/active.html', {
        "workout_id": request.GET.get('id'),
        "active_wuid": request.session['active_wuid']
    })

def logout_view(request):
    logout(request)
    return redirect('/')


# --------========= WORKOUTS MANAGE ==========-------------------------
def _update_workouts():
    global WORKOUTS

    import os
    import sys

    #-------------------------------------------------------------------
    # Some preparations, that must be called once. Must be refactor    
    import random
    random.seed()
    import hashlib
    #-------------------------------------------------------------------


    WORKOUTS = {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for path in GLOBAL_PATHS:
        sys.path.append(os.path.join(base_dir, *path))

    

    workout_files = os.listdir(os.path.join(base_dir, *(GLOBAL_PATHS[0])))
    workout_files = list(filter(lambda x: x.endswith(".py"), workout_files))
    
    for f in workout_files:
        #if f != "01_test.py": continue
        workouts = __import__(f[:-3]).do_load_workouts()
        for w in workouts:
            WORKOUTS[hashlib.md5((f + ':' + w.__name__).encode()).hexdigest()] = w

def list_workouts(request):
    if WORKOUTS is None:
        _update_workouts()
    result = list(map(lambda k: jsons.dump(WORKOUTS[k]().build(k)), WORKOUTS.keys()))

    #import pprint
    #pprint.PrettyPrinter(indent=4).pprint(result)
    return JsonResponse(result, safe = False, status = 200)


def view_workout(request):
    workout_id = request.GET.get('id')

    if WORKOUTS is None:
        _update_workouts()

    if workout_id in WORKOUTS.keys():
        from speech_manager import SpeechManager
        result = WORKOUTS[workout_id]().build(workout_id)
        #print(result)
        SpeechManager().generate_sounds(result)
        result = jsons.dump(result)

        
        #import pprint
        #pprint.PrettyPrinter(indent=4).pprint(result)
        return JsonResponse( result, safe = False, status = 200)
    return JsonResponse({}, safe = False, status = 200)  # Not 200 here