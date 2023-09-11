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

def list_workouts(request):
    global WORKOUTS

    #return JsonResponse({"valid":False}, status = 200)   -- work fine
    if WORKOUTS is None:
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
        #print(result)
        return JsonResponse(result, safe = False, status = 200)
