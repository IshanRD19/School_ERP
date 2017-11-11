from django.shortcuts import render

# Create your views here.

def studentlogin(request):
    return render(request, 'studentlogin.html')