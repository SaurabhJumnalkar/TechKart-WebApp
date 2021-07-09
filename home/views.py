from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse('This is a response')
    context={
        'variable':"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Thank You For Your Response!')
    return render(request,'contact.html')
def services(request):
   
    return render(request,'services.html')