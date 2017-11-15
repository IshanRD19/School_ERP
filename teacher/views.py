from django.shortcuts import render
from principal.models import Personal_Info, AssignmentParameters
from teacher.models import SubjectAllotment_2018, Teachers_2018, Assigments_2018, Classes_2018
# Create your views here.


def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    #find the id for teacher corresponding to the personal info id
    teacher_id = Teachers_2018.objects.get(Index=user)
    subject_teacher = SubjectAllotment_2018.objects.filter(Teacher=teacher_id)
    return render(request, 'teacherhome/teacherhome.html', {'context': user, 'classes': subject_teacher})


def assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    teacher_id = Teachers_2018.objects.get(Index=user)
    subjAllot = SubjectAllotment_2018.objects.get(pk=sub)
    assignments = Assigments_2018.objects.filter(Teacher=teacher_id,ClassSection=subjAllot.Class)
    return render(request, 'teacherhome/assignmenthome.html', {'context': assignments, 'user':user, 'sub':sub})

def add_assignment(request, index, sub):
    context = AssignmentParameters.objects.all()
    return render(request, 'teacherhome/addassignment.html',{'context':context})