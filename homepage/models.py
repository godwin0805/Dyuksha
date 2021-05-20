from django.db import models
from django.db.models.fields import CharField, IntegerField

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