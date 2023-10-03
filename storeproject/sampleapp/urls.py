from . import views
from django.urls import path



urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('login/register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('second',views.second,name='second'),
    path('form/',views.form,name='form'),
    path('form/third/',views.third,name='third'),
    path('form/logout/',views.logout,name='logout'),
    path('form/third/logout/',views.logout,name='logout'),
    path('form/register/',views.register,name='register'),
    
    
   
    
]
