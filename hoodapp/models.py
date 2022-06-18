from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)

class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    locattion = models.ForeignKey(Location,on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0,blank=True,null=True)
    police_num = models.IntegerField()
    hospital_num = models.IntegerField()

    



