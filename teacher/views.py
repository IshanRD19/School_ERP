from django.shortcuts import render
from principal.models import Personal_Info
# Create your views here.


def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    return render(request, 'teacherhome/teacherhome.html', {'context': user})