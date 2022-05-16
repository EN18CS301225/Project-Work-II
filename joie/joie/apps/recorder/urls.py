from django.urls import path
from django.conf import  settings
from django.conf.urls import url
from . import views

app_name = "recorder"


urlpatterns = [
    path('', views.audionotes, name="audionotes"),
    path("recorder/", views.recorder, name="recorder"),
    
]