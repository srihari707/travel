from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        usrr=auth.authenticate(username=username,password=password)

        if usrr is not None:
            auth.login(request,usrr)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login/')

    return render(request,'login,html.html')

def registr(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        passsword1 = request.POST['password1']
        if password==passsword1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('registr')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('registr')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password is not matching')
            return redirect('registr')
        return redirect('/')
    return render(request,'registr.html')

def logout(request):
    auth.logout(request)
    return redirect('demo')
