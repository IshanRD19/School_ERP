from django.shortcuts import render, redirect
from django.http import HttpResponse
from principal.models import login_info, Personal_Info
# Create your views here.

def home(request):
    return render(request, 'index.html', {})


def login_attempt(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        login_info.objects.get(username=Personal_Info.objects.get(Index=username), password=password)
        return HttpResponse('Welcome')
    except:
        return render(request, 'index.html', {'message':'Invalid Credentials!'})