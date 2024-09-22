from django.shortcuts import render
from .models import *
# Create your views here.


def Home(request):
    imageslider = Imageslider.objects.all().order_by('-id')
    about1 = About1.objects.all().order_by('-id')[:1]
    about2 = About2.objects.all().order_by('-id')
    about3 = About3.objects.all().order_by('-id')[:3]
    project = Project.objects.all().order_by('-id')[:1]
    menu = Menu.objects.all().order_by('-id')

    return render(request,'index.html', {'imageslider':imageslider, 'about1':about1, 'about2':about2, 'about3':about3, 'project':project, 'menu':menu})