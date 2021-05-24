from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User

class EventData(models.Model):
    image = models.ImageField(upload_to='pics')
    event = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    No_of_participants = IntegerField()
    description = models.CharField(max_length=200)

class Notifications(models.Model):
    noti = models.CharField(max_length=256)


class RegistrationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    event_name = models.CharField(max_length=300)
    Team_Name = models.CharField(max_length=30)
    no_of_participants = models.CharField(max_length=3)
    College_Email_ID = models.EmailField(max_length=30)
    Mob_No = models.BigIntegerField()