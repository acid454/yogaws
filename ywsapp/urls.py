from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('active', views.active, name="active"),
    path('list_workouts', views.list_workouts, name="list_workouts"),
    path('view_workout', views.view_workout, name="view_workout"),
    path('get_workout', views.get_workout, name="get_workout"),
    path('logout', views.logout_view, name="logout"),
    path('modify_workout_params', views.modify_workout_params, name="modify_workout_params"),
    path('sound', views.sound, name="sound")
    #path('accounts/', include('django.contrib.auth.urls')),
    #path("register/", views.register, name="register"),
]
