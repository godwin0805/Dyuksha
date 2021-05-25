from django.shortcuts import render
from .models import EventData, Notifications,RegistrationModel
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django. contrib. auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def homepage(request):
    event = EventData.objects.all()
    notif = Notifications.objects.all()
    return render(request,'home.html',{'notif':notif,'events':event})


def createevent(request):
    return render(request,'createevent.html')

def event_create(request):
    event_title=request.POST["event_title"]
    event_description=request.POST["event_description"]
    event_date=request.POST["event_date"]
    event_time=request.POST["event_time"]
    event_location=request.POST["event_location"]
    event_banner=request.POST["event_banner"]
    event_participants =request.POST["event_participants"]
    eventdata = EventData(image=event_banner,event=event_title,date=event_date,time=event_time,location=event_location,description=event_description,No_of_participants=event_participants)
    eventdata.save()
    xx=RegistrationModel.objects.all()
    return render(request,'profile.html',{'reg':xx})


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
            messages.info(request,"password not match")
            return render(request,'signin.html')
    else:
        return render(request,'signin.html')
        
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt


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



@login_required
def register(request):
    
    event = EventData.objects.all()
    return render(request,'register.html',{'events':event})


def registerdone(request):
    if request.method == "POST" and not request.POST.get('edit') == 'edit':
        event_name =  request.POST['event_name']
        Team_Name =  request.POST['Team_Name']
        no_of_participants =  request.POST['no_of_participants']
        College_Email_ID =  request.POST['College_Email_ID']
        Mob_No =  request.POST['Mob_No']

        x = RegistrationModel(user=request.user, event_name=event_name, Team_Name=Team_Name, no_of_participants=no_of_participants, College_Email_ID=College_Email_ID, Mob_No=Mob_No)
        x.save()
        edit = False
    try:
        obj = RegistrationModel.objects.get(user=request.user)
        if request.POST.get('edit') == 'edit':
            edit = True
    except ObjectDoesNotExist:
        obj = None
    
    xx=RegistrationModel.objects.get(user=request.user)
    return render(request,'profile.html',{'reg':xx})