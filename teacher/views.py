from django.shortcuts import render
from principal.models import Personal_Info
from teacher.models import SubjectAllotment_2018,Teachers_2018
# Create your views here.


def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    #find the id for teacher corresponding to the personal info id
    teacher_id = Teachers_2018.objects.get(Index=user)
    subject_teacher = SubjectAllotment_2018.objects.filter(Teacher=teacher_id)
    return render(request, 'teacherhome/teacherhome.html', {'context': user, 'classes': subject_teacher})