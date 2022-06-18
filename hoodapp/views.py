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
    
    
    return render(request, 'hoodapp/neighbourhood.html',)
