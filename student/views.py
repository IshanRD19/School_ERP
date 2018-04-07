from django.shortcuts import render
from principal.models import Personal_Info, Subjects
from teacher.models import SubjectAllotment, Classes, Assigments
from student.models import Students
# Create your views here.

def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    # find the id for student corresponding to the personal info id
    student_class = Students.objects.get(Index=user).ClassSection
    subject_list = SubjectAllotment.objects.filter(Class=student_class)
    return render(request, 'studenthome.html', {'context':user, 'class': student_class, 'subjects': subject_list})


def view_subject_info(request, index, subcode):
    subject_name = Subjects.objects.get(SubjectCode=subcode).SubjectName
    student_class = Students.objects.get(Index=index).ClassSection
    assignments = Assigments.objects.filter(Subject=subcode, ClassSection=student_class)
    teacher = SubjectAllotment.objects.get(Class=student_class, Subject=subcode)
    return render(request, 'subjectinfo.html', {'context':assignments, 'teacher':teacher, 'subject':subject_name})