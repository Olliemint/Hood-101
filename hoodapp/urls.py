from django.urls import path
from . import views

app_name ='hood'
urlpatterns =[
    path('register/',views.Register_user,name='register'),
    
]