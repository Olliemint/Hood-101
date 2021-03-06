from time import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        
        return self.name
    
    
    def save_location(self):
        self.save()
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=80,null=False,blank=False)
    def __str__(self):
    
        return self.category_name
    
    def save_category(self):
        self.save()


class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True)
    occupants_count = models.IntegerField(default=0,blank=True,null=True)
    police_num = models.CharField(max_length=255,null=True,blank=True)
    hospital_num = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        
        return self.name
    
    def create_neigbourhood(self):
        self.save()

    @classmethod
    def delete_neigbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def find_neigbourhood(cls, searchterm):
        search_results = cls.objects.filter(Q(name__icontains=searchterm))
        return search_results

    @classmethod
    def update_neighbourhood(cls, id, name):
        cls.objects.filter(id=id).update(name=name)
    
    
class Business(models.Model):
    
    name = models.CharField(max_length=255)    
    email_address = models.EmailField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(default='business.jpg',upload_to='bizimages', blank=True)
    posted = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        
        return self.name
    
    def save_business(self):
        self.save()

    @classmethod
    def delete_business(cls, id): 
        cls.objects.filter(id=id).delete()

    @classmethod
    def searchbusiness(cls, searchterm):
        search_results = cls.objects.filter(Q(name__icontains = searchterm))
        return search_results
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=1500,null=True,blank=True)
    avatar = models.ImageField(default='avatar.jpg',upload_to='profiles')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True,null=True) 
    def __str__(self):
        return f'{self.user.username} Profile'  
    
    

        
class Hood_update(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=False, blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)
    image = models.ImageField(default='business.jpg',upload_to='bizimages', blank=True)
    
    def __str__(self):
        
        return self.title
    
    def save_update(self):
        self.save()

    @classmethod
    def delete_update(cls, id):
        cls.objects.filter(id=id).delete()
  
            
    
    
    

    



