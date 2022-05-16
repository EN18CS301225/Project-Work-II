from django.urls import path
from . import views

app_name = "affirmation_reading"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("reading/", views.reading, name="reading"),
    
]