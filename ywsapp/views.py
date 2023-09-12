from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


WORKOUTS = None
GLOBAL_PATHS = [
    ["yoga", "workouts"],
    ["yoga", "asanas"],
    ["yoga", "sets"],
    ["yoga", "common"]
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

    result = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for path in GLOBAL_PATHS:
        sys.path.append(os.path.join(base_dir, *path))

    workout_files = os.listdir(os.path.join(base_dir, *(GLOBAL_PATHS[0])))
    workout_files = list(filter(lambda x: x.endswith(".py"), workout_files))
    
    for w in workout_files:
        local_workouts = __import__(w[:-3]).do_load_workouts()
        result += list(map(lambda x: x().view(), local_workouts))
        
    import pprint
    pprint.PrettyPrinter(indent=4).pprint(result)
    WORKOUTS = result

def list_workouts(request):
    if WORKOUTS is None: _update_workouts()
    return JsonResponse(WORKOUTS, safe = False, status = 200)

def view_workout(request):
    workout_name = request.GET.get('workout_name')

    if WORKOUTS is None: _update_workouts()
    for w in WORKOUTS:
        if w['name'] == workout_name:
            return JsonResponse(w, safe = False, status = 200)
    return JsonResponse({}, safe = False, status = 200)  # Not 200 here