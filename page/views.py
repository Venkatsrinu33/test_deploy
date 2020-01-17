
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render
from .models import userdata
import datetime

# Create your views here.


def home(request):
    return render(request,'home.html')


def reg(request):
    return render(request, 'reg.html')


def Register(request):
    username = request.POST['t1']
    try:
        sr = userdata.objects.filter(username=username)
    except Exception as e:
        return HttpResponse(str(e))
    for item in sr:
        print(item.username)
        return HttpResponse('username exits')
    try:
        name = request.POST['t2']
        phoneno = int(request.POST['t3'])
        email = request.POST['t4']
        password1 = request.POST['t5']
        repassword = request.POST['t6']
        createddate = datetime.datetime.now()
        if password1==repassword:
            my = userdata(username=username,name=name,phoneno=phoneno,email=email,password=password1,createddate=createddate)
            my.save()
            return render(request,'success.html')
        else:
            return HttpResponse('enter valid data')
    except:
        data = {'message': 'please provide correct data'}
        print(data)
        return render(request, 'error.html', context=data)


def login(request):
    username = request.POST['t7']
    password = request.POST['t8']
    try:
        if userdata.objects.filter(username=username,password=password):
            return render(request,'post.html')
        else:
            return render(request,'loginfail.html')
    except:
        data={'message':'enter username/password'}
        print(data)
        return render(request,'error.html',context=data)

def logo(request):
    logout(request)
    return HttpResponse('logout success')



