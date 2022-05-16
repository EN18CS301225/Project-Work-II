from django.shortcuts import render,redirect

from .models import Videos

# Create your views here.

def meditation(request):   
    return render(request,'video_content/meditation.html')

def index(request):
    return render(request,'video_content/index.html')

def display(request):
    
    videos = Videos.objects.all()
    title=Videos.objects.all()
    thumbnail=Videos.objects.all()
    context ={
        'videos':videos,
        'title':title,
        'thumbnail':thumbnail,
    }
    
    return render(request,'video_content/videos.html',context)