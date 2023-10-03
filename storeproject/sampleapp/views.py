from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .form import detailform


# Create your views here.

def first(request):
    return render(request,'first.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['confirm-password']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('second')
        else:
            messages.info(request,"Invalid Username or password")
            return redirect('login')
        
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def second(request):
    return render(request,'second.html')






def third(request):
    return render(request,'third.html')





def form(request):
    

    if request.method == 'POST':
        form = detailform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"successfully submited your form")
            return redirect('form')  #Redirect to a success page after form submission
        
    else:
        form = detailform()
        
    
    return render(request, 'form.html', {'form': form})




