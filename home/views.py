from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from home import models
# Create your views here.
def home(request):
    context = {'name':'Sid','page':'portfolio'}
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        ins = models.Contact(name=name, email=email,phone=phone,comment=comment)
        ins.save()
        print("data written to db")
    return render(request, 'contact.html')
