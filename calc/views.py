from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Hello World !! ")

def htmlhome(request):    
    return render(request,'home.html', {"name":'Awi'})

def htmlhomewithbase(request):    
    return render(request,'homewithbase.html', {"name":'Awi'})    