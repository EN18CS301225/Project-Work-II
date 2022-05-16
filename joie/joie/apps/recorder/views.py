from django.shortcuts import render
from django.http import HttpResponse
from .models import Record

# Create your views here.
def recorder(request):
    return render(request, "recorder/index.html")

def audionotes(request):
     return render(request, "recorder/audionotes.html")

