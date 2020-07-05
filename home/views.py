from django.shortcuts import render,HttpResponse
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        print("This is POST")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        instance=Contact(name=name,email=email,phone=phone,desc=desc)
        instance.save()
        print("Data Have been written to DB")
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')