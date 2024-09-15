from django.shortcuts import render
from .models import *
# Create your views here.


def Home(request):
    imageslider = Imageslider.objects.all().order_by('-id')

    return render(request,'index.html', {'imageslider':imageslider})