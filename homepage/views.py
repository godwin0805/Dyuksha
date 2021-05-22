from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import EventData, Notifications
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django. contrib. auth import authenticate,login

def homepage(request):
    event = EventData.objects.all()
    notif = Notifications.objects.all()
    return render(request,'home.html',{'notif':notif,'events':event})
def signup(request):
    event = EventData.objects.all()
    notif = Notifications.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username = first_name).exists():
                messages.info(request,"Username Taken")
                return render(request,'signin.html')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request," Email Taken")
                return render(request,'signin.html')
                
                
            else:
                user = User.objects.create_user(username=first_name,password=password1,email=email)
                user.save();
                return render(request,'signin.html')
    else:
        messages.info(request,"Password not matching")
        return render(request,'signin.html')
        


def signin(request):
    event = EventData.objects.all()
    notif = Notifications.objects.all()
    if request.method == 'POST':
        Email = request.POST["email"]
        Password = request.POST["password"]
        user = authenticate(username= Email,password=Password)
        print(user)
        if user is not None:
            login(request,user)
            return render(request,'profile.html',{'notif':notif,'events':event})
        else:
            messages.info(request,"invalid credentials")
            return render(request,'signin.html')
            
    else:
        return render(request,'signin.html')

def createevent(request):
    return render(request,'createevent.html')