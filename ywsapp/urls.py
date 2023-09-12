from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('active', views.active, name="active"),
    path('list_workouts', views.list_workouts, name="list_workouts"),
    path('view_workout', views.view_workout, name="view_workout")
]
