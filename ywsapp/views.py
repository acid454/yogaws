from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


WORKOUTS = None
SPEECH_MANAGER = None
GLOBAL_PATHS = [
    ["yoga", "workouts"],       # Note: workouts must be [0]
    ["yoga", "sets"],
    ["yoga", "common"],
    ["yoga", "containers"],
    ["yoga"]
]


# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #template = loader.get_template("index.html")
    return render(request, 'ywsapp/index.html', {})

def active(request):
    return render(request, 'ywsapp/active.html', {})

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
        workouts = __import__(f[:-3]).do_load_workouts()
        for w in workouts:
            WORKOUTS[hashlib.md5((f + ':' + w.__name__).encode()).hexdigest()] = w
        #WORKOUTS += list(map(lambda x: {'id': w, 'class': x}, workouts))
        #print(WORKOUTS)
        #result += list(map(lambda x: x().build(), local_workouts))

    #-------------------------------------------------------------------
    # Some preparations, that must be called once. Must be refactor 
    
    
    #-------------------------------------------------------------------


def list_workouts(request):
    if WORKOUTS is None:
        _update_workouts()
    result = list(map(lambda k: WORKOUTS[k]().build(k), WORKOUTS.keys()))

    import pprint
    pprint.PrettyPrinter(indent=4).pprint(result)
    return JsonResponse(result, safe = False, status = 200)


def view_workout(request):
    workout_id = request.GET.get('id')

    if WORKOUTS is None:
        _update_workouts()

    if workout_id in WORKOUTS.keys():
        from speech_manager import SpeechManager
        result = WORKOUTS[workout_id]()
        SpeechManager().generate_sounds(result)
        result = result.build(workout_id)
        
        #import pprint
        #pprint.PrettyPrinter(indent=4).pprint(result)
        return JsonResponse( result, safe = False, status = 200)
    return JsonResponse({}, safe = False, status = 200)  # Not 200 here