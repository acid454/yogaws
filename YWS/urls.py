"""YWS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.conf import settings
import os

def serve_favicon(request):
    file_path = os.path.join(settings.BASE_DIR, 'ywsapp/static/ywsapp/res/favicon.ico')
    with open(file_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/x-icon")

def serve_apple_touch_icon(request):
    file_path = os.path.join(settings.BASE_DIR, 'ywsapp/static/ywsapp/res/apple-touch-icon.png')
    with open(file_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/png")

urlpatterns = [
    path('', include("ywsapp.urls")),
    path('admin/', admin.site.urls),
    path('favicon.ico', serve_favicon, name='favicon'),
    path('apple-touch-icon.png', serve_apple_touch_icon, name='apple_touch_icon'),
]
