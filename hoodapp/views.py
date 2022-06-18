from .forms import *
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Business_view(request):
    business = Business.objects.all()
    
    context = {
        'business': business
    }
    
    return render(request, 'hood/home.html',context)


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
    form = Register_Form()
    
    if request.method == 'POST':
        form = Register_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hood:home')
    
    context={
        'form': form,
    }
    return render(request,'accounts/register.html',context)
