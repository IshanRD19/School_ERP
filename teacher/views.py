from django.shortcuts import render, redirect
from principal.models import Personal_Info, AssignmentParameters, Subjects
from teacher.models import SubjectAllotment_2018, Teachers_2018, Assigments_2018, Classes_2018
from student.models import AssignmentGrades_2018, Students_2018, TimeTable_2018
# Create your views here.


def home(request, index):
    user = Personal_Info.objects.get(Index=index)
    #find the id for teacher corresponding to the personal info id
    teacher_id = Teachers_2018.objects.get(Index=user)
    subject_teacher = SubjectAllotment_2018.objects.filter(Teacher=teacher_id)
    TimeTable = []
    for i in subject_teacher:
        TimeTable.append(TimeTable_2018.objects.get(Subject=i.Subject, Class=i.Class))
    return render(request, 'teacherhome/teacherhome.html', {'context': user, 'classes': subject_teacher, "subjects": TimeTable})


def assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    teacher_id = Teachers_2018.objects.get(Index=user)
    subjAllot = SubjectAllotment_2018.objects.get(pk=sub)
    assignments = Assigments_2018.objects.filter(Teacher=teacher_id,ClassSection=subjAllot.Class)
    return render(request, 'teacherhome/assignmenthome.html', {'context': assignments, 'user':user, 'sub':sub})


def add_assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    context = AssignmentParameters.objects.all()
    return render(request, 'teacherhome/addassignment.html', {'context': context, 'user': user, 'sub': sub})


def push_data_assignment(request, index, sub):
    user = Personal_Info.objects.get(Index=index)
    teacher_id = Teachers_2018.objects.get(Index=user)
    subjAllot = SubjectAllotment_2018.objects.get(pk=sub)
    desc = request.POST['desc']
    assignment1 = Assigments_2018()
    assignment1.Description = desc
    assignment1.Teacher = teacher_id
    assignment1.Subject = subjAllot.Subject
    assignment1.ClassSection = subjAllot.Class
    assignment1.save()
    all_students = Students_2018.objects.filter(ClassSection=subjAllot.Class)
    try:
        for j in range(5):
            param1 = request.POST[str(j+1)]
            for i in all_students:
                a = AssignmentGrades_2018()
                a.Assigment = assignment1
                a.Student = i
                a.GradingParameter = AssignmentParameters.objects.get(pk=param1)
                a.save()

    except:
        pass

    return redirect('/teacher/assignment/'+str(index)+"/"+str(sub))


def grade_assignment(request, id, index):
    assignment1 = Assigments_2018.objects.get(pk=id)
    students = AssignmentGrades_2018.objects.filter(Assigment=assignment1).values_list('Student').distinct()
    # param = AssignmentGrades_2018.objects.filter(Assigment=assignment1).distinct()

    done = False
    student = {}
    params = []
    # for i in param:
    #     params.append(i.GradingParameter.GradingParameter)
    # params = list(set(params))
    for ar in students:
        for i in ar:
            stu = Students_2018.objects.get(RegistrationNo=i)
            student[i] = [stu.Index.FirstName, AssignmentGrades_2018.objects.filter(Student=i, Assigment=assignment1)]
            if not done:
                stud = AssignmentGrades_2018.objects.filter(Student=i, Assigment=assignment1)
                done = True
    for i in stud:
        params.append(i.GradingParameter.GradingParameter)

    return render(request, 'teacherhome/gradeassignment.html', {'context': student, 'params': params, 'index': index, 'id': id})


def update_grade(request, index, id):
    assignment1 = Assigments_2018.objects.get(pk=id)
    assignment_grades = AssignmentGrades_2018.objects.filter(Assigment=assignment1)
    for i in assignment_grades:
        grade = request.POST[str(i.pk)]
        i.Grade = grade
        i.save()

    assignment1 = AssignmentGrades_2018.objects.get(pk=id)
    class_section = SubjectAllotment_2018.objects.get(Class=assignment1.Assigment.ClassSection, Teacher=assignment1.Assigment.Teacher, Subject=assignment1.Assigment.Subject)
    # return HttpResponse(class_section)
    return redirect('/teacher/assignment/'+str(index)+"/"+str(class_section.pk))


def view_class(request, index, classid):
    students = Students_2018.objects.filter(ClassSection=Classes_2018.objects.filter(ClassSection=classid))
    return render(request, 'teacherhome/viewclasses.html', {'context': students})

def view_student(request, studentreg):
    student = Students_2018.objects.get(RegistrationNo=studentreg)
    return render(request, 'teacherhome/viewstudent.html', {'context': student.Index})

