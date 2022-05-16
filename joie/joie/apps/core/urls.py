
from django.urls import path
from django.conf import  settings
from . import views

app_name = "core"

urlpatterns = [
    path('', views.audionotes, name="audionotes"),
    path("core/", views.core, name="core"),
    path("record/", views.record, name="record"),
    path("record_detail/<uuid:id>/", views.record_detail, name="record_detail"),
]

