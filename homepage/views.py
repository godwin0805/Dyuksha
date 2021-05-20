from django.shortcuts import render
from django.http import HttpResponse
from .models import EventData, Notifications

# Create your views here.
def homepage(request):
    event = EventData.objects.all()
    notif = Notifications.objects.all()
    return render(request,'home.html',{'notif':notif,'events':event})
def signin(request):
    return render(request,'signin.html')

