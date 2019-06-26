from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    images = Images.objects.all()
    context = {
        'images':images,
    }
    return render(request,'index.html',context)
