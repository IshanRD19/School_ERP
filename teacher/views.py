from django.shortcuts import render, redirect
from principal.models import Personal_Info, AssignmentParameters, Subjects
from teacher.models import SubjectAllotment, Teachers, Assigments, Classes
from student.models import AssignmentGrades, Students, TimeTable
# Create your views here.


def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    #find the id for teacher corresponding to the personal info id
    teacher_id = Teachers.objects.get(Index=user)
    subject_teacher = SubjectAllotment.objects.filter(Teacher=teacher_id)
    timetable = []
    for i in subject_teacher:
        timetable.append(TimeTable.objects.filter(Subject=i.Subject, Class=i.Class))
    return render(request, 'teacherhome/teacherhome.html', {'context': user, 'classes': subject_teacher, "subjects": timetable})


def view_profile(request, index):
    user = Personal_Info.objects.get(Index=index)
    teacher_id = Teachers.objects.get(Index=user)
    return render(request, 'teacherhome/viewprofile.html', {'context': user})


def messages(request, index):
    return render(request, 'teacherhome/messageinbox.html')


def view_timetable(request, index):
    return render(request, 'teacherhome/viewtimetable.html')


def assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    teacher_id = Teachers.objects.get(Index=user)
    subjAllot = SubjectAllotment.objects.get(pk=sub)
    assignments = Assigments.objects.filter(Teacher=teacher_id,ClassSection=subjAllot.Class)
    return render(request, 'teacherhome/assignmenthome.html', {'context': assignments, 'user':user, 'sub':sub})


def add_assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    context = AssignmentParameters.objects.all()
    return render(request, 'teacherhome/addassignment.html', {'context': context, 'user': user, 'sub': sub})


def push_data_assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    teacher_id = Teachers.objects.get(Index=user)
    subjAllot = SubjectAllotment.objects.get(pk=sub)
    desc = request.POST['desc']
    assignment1 = Assigments()
    assignment1.Description = desc
    assignment1.Teacher = teacher_id
    assignment1.Subject = subjAllot.Subject
    assignment1.ClassSection = subjAllot.Class
    assignment1.save()
    all_students = Students.objects.filter(ClassSection=subjAllot.Class)
    try:
        for j in range(5):
            param1 = request.POST[str(j+1)]
            for i in all_students:
                a = AssignmentGrades()
                a.Assignment = assignment1
                a.Student = i
                a.GradingParameter = AssignmentParameters.objects.get(pk=param1)
                a.save()

    except:
        pass

    return redirect('/teacher/assignment/'+str(index)+"/"+str(sub))


def grade_assignment(request, id, index):
    assignment1 = Assigments.objects.get(pk=id)
    students = AssignmentGrades.objects.filter(Assigment=assignment1).values_list('Student').distinct()
    # param = AssignmentGrades.objects.filter(Assignment=assignment1).distinct()

    done = False
    student = {}
    params = []
    # for i in param:
    #     params.append(i.GradingParameter.GradingParameter)
    # params = list(set(params))
    for ar in students:
        for i in ar:
            stu = Students.objects.get(RegistrationNo=i)
            student[i] = [stu.Index.FirstName, AssignmentGrades.objects.filter(Student=i, Assigment=assignment1)]
            if not done:
                stud = AssignmentGrades.objects.filter(Student=i, Assigment=assignment1)
                done = True
    for i in stud:
        params.append(i.GradingParameter.GradingParameter)

    return render(request, 'teacherhome/gradeassignment.html', {'context': student, 'params': params, 'index': index, 'id': id})


def update_grade(request, index, id):
    assignment1 = Assigments.objects.get(pk=id)
    assignment_grades = AssignmentGrades.objects.filter(Assigment=assignment1)
    for i in assignment_grades:
        grade = request.POST[str(i.pk)]
        i.Grade = grade
        i.save()

    assignment1 = AssignmentGrades.objects.get(pk=id)
    class_section = SubjectAllotment.objects.get(Class=assignment1.Assigment.ClassSection, Teacher=assignment1.Assigment.Teacher, Subject=assignment1.Assigment.Subject)
    # return HttpResponse(class_section)
    return redirect('/teacher/assignment/'+str(index)+"/"+str(class_section.pk))


def view_class(request, index, classid):
    students = Students.objects.filter(ClassSection=Classes.objects.filter(ClassSection=classid))
    return render(request, 'teacherhome/viewclasses.html', {'context': students})


def view_student(request, studentreg):
    student = Students.objects.get(RegistrationNo=studentreg)
    return render(request, 'teacherhome/viewstudent.html', {'context': student.Index})

