from telnetlib import AUTHENTICATION
from django.shortcuts import render
from .models import *

# Create your views here.
def Business_view(request):
    business = Business.objects.all()
    
    context = {
        'business': business
    }
    
    return render(request, 'hoodapp/business.html',context)


def Neighbourhood_view(request):
    
    neighbourhood = Neighbourhood.objects.all()
    
    context = {
        'neighbourhood': neighbourhood
    }
    
    
    return render(request, 'hoodapp/neighbourhood.html',context)


def Profile_view(request):
    
    
    
    return render(request,'hoodapp/profile.html')





# AUTHENTICATION SECTION

def Register_user(request):
    
    
    return render(request,'accounts/register.html')
