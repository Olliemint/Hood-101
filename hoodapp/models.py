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
    
    
class Business(models.Model):
    
    name = models.CharField(max_length=255)    
    email_address = models.EmailField(max_length=255)
    locattion = models.ForeignKey(Location,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(max_length=50,null=True, blank=True)
    bio = models.TextField(max_length=1500,null=True,blank=True)
    email_address = models.EmailField(max_length=255,null=True, blank=True) 
    avatar = models.ImageField(default='avatar.jpg',upload_to='profiles')   
    
    
    

    



