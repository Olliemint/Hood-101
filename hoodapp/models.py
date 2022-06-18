from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=80,null=False,blank=False)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    locattion = models.ForeignKey(Location,on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0,blank=True,null=True)
    police_num = models.IntegerField()
    hospital_num = models.IntegerField()
    
    
class Business(models.Model):
    
    name = models.CharField(max_length=255)    
    email_address = models.EmailField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=1500,null=True,blank=True)
    email_address = models.EmailField(max_length=255,null=True, blank=True) 
    avatar = models.ImageField(default='avatar.jpg',upload_to='profiles')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)   
    
    

    
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=False, blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)
  
            
    
    
    

    



