from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import  settings

app_name="video_content"

urlpatterns = [
   
    path('videos/',views.display,name='videos'),
    path('index/',views.index,name='index'),
    path("",views.meditation,name='meditation'),

]

    
