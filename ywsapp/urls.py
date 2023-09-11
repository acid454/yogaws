from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list_workouts', views.list_workouts, name="list_workouts")
]
