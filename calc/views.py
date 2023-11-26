from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Hello World !! ")

def htmlhome(request):    
    return render(request,'home.html', {"name":'Awi'})

def htmlhomewithbase(request):    
    return render(request,'homewithbase.html', {"name":'Awi'})    

def add(request):    
     val1 = int(request.GET['num1'])
     val2 = int(request.GET['num2'])
     res = val1 + val2
     return render(request, "result.html", {'result': res}) 

def addpost(request):    
     val1 = int(request.POST['num1'])
     val2 = int(request.POST['num2'])
     res = val1 + val2
     return render(request, "result.html", {'result': res})      