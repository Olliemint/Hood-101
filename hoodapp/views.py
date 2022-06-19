from multiprocessing import context
import re
from .forms import *
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User





# Create your views here.
def home(request):
    
    return render(request, 'hood/home.html')

def Updates_view(request):
    
    stories = Hood_update.objects.filter(category__category_name='Announcements',
        neighbourhood=request.user.profile.neighbourhood)
    
    alerts = Hood_update.objects.filter(category__category_name='Alerts',
        neighbourhood=request.user.profile.neighbourhood)
    
    context = {
        'stories': stories,
        'alerts': alerts
        }
    
    return render(request, 'hood/updates.html',context)

@login_required(login_url='hood:login') 
def Business_view(request):
    if request.user.profile.neighbourhood is None:
        messages.success(request, 'Please fillout you Neighbourhood')
        return redirect('hood:profile')
    else:
        
        business = Business.objects.filter(
            neighbourhood=request.user.profile.neighbourhood)
    neibdetails = Neighbourhood.objects.get(
            name=request.user.profile.neighbourhood)
    category = Category.objects.all()    
    context = {
        'business': business,
        'category': category,
        'neibdetails': neibdetails
    }
    return render(request, 'hood/business.html',context)


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
            return redirect('hood:home')
            
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, 'Username or password is incorrect')
        
        

    return render(request,'accounts/login.html')


def Logout_view(request):
    logout(request)
    return redirect('hood:home')
    # Redirect to a success page.
    
    
    
@login_required(login_url='hood:login')  
def Profile(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated!')
            return redirect('hood:home')

    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        # current_profile = Profile.objects.get(user_id = request.user)
        # current_post = Post.user_post(request.user) 
    
    
    context = {
       'u_form': u_form,
       'p_form': p_form,
       
        
    }
    
    return render(request, 'accounts/profile.html',context)

        
            
    
        
        
