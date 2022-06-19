from .forms import *
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User





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
            return redirect('hood:profile')
    
    context={
        'form': form,
    }
    return render(request,'accounts/register.html',context)



def Login_view(request):
    if request.method == 'POST':
    
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('hood:profile')
            
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, 'Username or password is incorrect')
        
        

    return render(request,'accounts/login.html')


def Logout_view(request):
    logout(request)
    return redirect('hood:login')
    # Redirect to a success page.
    
    
    
@login_required(login_url='hood:login')  
def Profile(request):
  
    
    return render(request, 'accounts/profile.html')
        
            
    
        
        
