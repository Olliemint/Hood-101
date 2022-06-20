from django.urls import path
from . import views

app_name ='hood'
urlpatterns =[
    path('',views.home,name='home'),
    path('register/',views.Register_user,name='register'),
    path('login/',views.Login_view,name='login'),
    path('logout/',views.Logout_view,name='logout'),
    path('profile/',views.Profile,name='profile'),
    path('business/',views.Business_view,name='business'),
    path('updates/',views.Updates_view,name='updates'),
    path('search/',views.Search_data,name='search'),
    
       
]