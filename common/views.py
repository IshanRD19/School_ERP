from django.shortcuts import render, redirect
from django.http import HttpResponse
from principal.models import login_info, Personal_Info
from student.models import Student_login_info
# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def login_attempt(request):
    username = request.POST['username']
    password = request.POST['password']
    usertype = 1 # 1:student, 2:teacher, 3:principal
    try:
        user = Personal_Info.objects.get(EMail=username)
        if user.Role == 'principal':
            try:
                login_info.objects.get(username=user, password=password)
                return HttpResponse('Welcome')
            except:
                return render(request, 'index.html', {'message':'Invalid Password!'})

        elif user.Role == 'student':
            try:
                Student_login_info.objects.get(username=user, password=password)
                return HttpResponse('Welcome')
            except:
                return render(request, 'index.html', {'message':'Invalid Password!'})
    except:
        return render(request, 'index.html', {'message':'Invalid email!'})