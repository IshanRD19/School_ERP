from django.shortcuts import render
from principal.models import Personal_Info
from teacher.models import SubjectAllotment_2018, Classes_2018, Assigments_2018
from student.models import Students_2018
# Create your views here.

def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    # find the id for student corresponding to the personal info id
    student_class = Students_2018.objects.get(Index=user).ClassSection
    subject_list = SubjectAllotment_2018.objects.filter(Class=student_class)
    return render(request, 'studenthome.html', {'context':user, 'class': student_class, 'subjects': subject_list})


def view_subject_info(request, index, subcode):
    assignments = Assigments_2018.objects.filter(Subject=subcode)
    return render(request, 'subjectinfo.html', {'context':assignments})