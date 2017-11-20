from django.shortcuts import render

# Create your views here.

def studentlogin(request):
    return render(request, 'studentlogin.html')

def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    # find the id for teacher corresponding to the personal info id
    student_id = Teachers_2018.objects.get(Index=user)
    subjects = SubjectAllotment_2018.objects.filter(Teacher=teacher_id)
    return render(request, 'teacherhome/teacherhome.html', {'context': user, 'classes': subject_teacher})