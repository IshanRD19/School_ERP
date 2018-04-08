from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings
from principal.models import Personal_Info, AssignmentParameters, Subjects
from teacher.models import SubjectAllotment, Teachers, Assigments, Classes
from student.models import AssignmentGrades, Students, TimeTable


# Create your views here.

def createtest(request, index):
    user = Personal_Info.objects.get(Index=index)
    # find the id for teacher corresponding to the personal info id
    teacher_id = Teachers.objects.get(Index=user)
    subject_teacher = SubjectAllotment.objects.filter(Teacher=teacher_id)
    timetable = []
    for i in subject_teacher:
        timetable.append(TimeTable.objects.get(Subject=i.Subject, Class=i.Class))
    return render(request, 'subjectivequestions/createtest.html', {'context': timetable, 'index': index})


def home(request, index):
    return render(request, 'subjectivequestions/home.html', {'index': index})


def createtestclass(request, class_section, index):
    return render(request, 'subjectivequestions/createtestpage.html', {'context': class_section, 'index': index})


def registerpaper(request, class_section, index):
    # return HttpResponse('<h1><a href = "/teacher/subjective/' + str(index) + "/" + '>go back</a></h1>')
    questionPaperObject = QuestionPaper()
    questionPaperObject.of_class = Classes.objects.get(ClassSection=class_section)
    questionPaperObject.save()
    i = 1
    try:
        while True:
            question_text = request.POST['Q' + str(i)]
            question_marks = request.POST['M' + str(i)]
            question_number = request.POST['N' + str(i)]
            question_object = Question()
            question_object.statement = question_text
            question_object.total_marks = question_marks
            question_object.question_paper = questionPaperObject
            question_object.question_number = question_number
            question_object.save()
            i += 1
    except:
        pass
         # return HttpResponse('<h1><a href = "/teacher/subjective/' + str(index) + "/" + '>go back</a></h1>')

    return HttpResponse('<h1><a href = "/teacher/subjective/'+str(index)+"/"+'">go back</a></h1>')


def viewtest(request, index):
    user = Personal_Info.objects.get(Index=index)
    # find the id for teacher corresponding to the personal info id
    teacher_id = Teachers.objects.get(Index=user)
    subject_teacher = SubjectAllotment.objects.filter(Teacher=teacher_id)
    timetable = []
    for i in subject_teacher:
        timetable.append(TimeTable.objects.get(Subject=i.Subject, Class=i.Class))
    return render(request, 'subjectivequestions/viewtest.html', {'context': timetable, 'index':index})


def classtests(request, class_section, index):
    this_class = Classes.objects.get(ClassSection=class_section)
    all_tests = QuestionPaper.objects.filter(of_class=this_class)
    return render(request, 'subjectivequestions/viewalltest.html', {'context': all_tests, 'class_section': class_section, 'index': index})


class Questionparam:
    def __init__(self):
        self.parameters = []
        self.marks = []
        self.isEmpty = True

def viewpaper(request, class_section, paper_id, index):
    questionPaperObject = QuestionPaper.objects.get(id=paper_id)
    questions = Question.objects.filter(question_paper=questionPaperObject)
    question_parameters = []
    for i in questions:
        q = Questionparam()
        param = Parameters.objects.filter(of_question=i)
        for j in param:
            q.isEmpty = False
            q.parameters.append(j.name)
            q.marks.append(j.marks)
        q.param_marks = zip(q.parameters, q.marks)
        question_parameters.append(q)

    return render(request, 'subjectivequestions/testpaper.html', {'index': index, 'context': zip(questions, question_parameters), 'class_section': class_section, 'paper_id': paper_id})


def uploadpaper(request, class_section, paper_id, index):
    all_students = Students.objects.filter(ClassSection=class_section)
    all_answers = AnswerSheet.objects.filter(of_paper=paper_id)
    all_students_submitted = []
    for i in all_answers:
        all_students_submitted.append(i.of_student.RegistrationNo)
    submitted = []
    for i in all_students:
        if i.RegistrationNo in all_students_submitted:
            submitted.append(True)
        else:
            submitted.append(False)
    return render(request, 'subjectivequestions/uploadpaper.html',
                  {'context': zip(all_students, submitted), 'class_section': class_section, 'paperid': paper_id, 'index': index})


def submitpaper(request, class_section, paper_id, stu_id, index):
    if request.method == 'POST':
        myfile = request.FILES[stu_id]
        answersheet = AnswerSheet()
        answersheet.of_paper = QuestionPaper.objects.get(id=paper_id)
        answersheet.of_student = Students.objects.get(RegistrationNo=stu_id)
        answersheet.sheet = myfile
        answersheet.save()
        classSection = Classes.objects.get(ClassSection=class_section)
        all_students = Students.objects.filter(ClassSection=classSection)
        all_answers = AnswerSheet.objects.filter(of_paper=paper_id)
        all_students_submitted = []
        for i in all_answers:
            all_students_submitted.append(i.of_student.RegistrationNo)
        submitted = []
        for i in all_students:
            if i.RegistrationNo in all_students_submitted:
                submitted.append(True)
            else:
                submitted.append(False)
        return render(request, 'subjectivequestions/uploadpaper.html',
                      {'context': zip(all_students, submitted), 'index': index, 'class_section': class_section, 'paperid': paper_id})


def viewupload(request, class_section, paper_id, stu_id, index):
    student = Students.objects.get(RegistrationNo=stu_id)
    paper = QuestionPaper.objects.get(id=paper_id)
    answersheet = AnswerSheet.objects.get(of_student=student, of_paper=paper)
    return HttpResponse(
        '<object data="' + answersheet.sheet.url + '" type="application/pdf" width="100%" height="100%"><p><b>Example fallback content</b>: This browser does not support PDFs. Please download the PDF to view it: <a href="' + answersheet.sheet.url + '">Download PDF</a>.</p></object>')


def checkupload(request, class_section, paper_id, stu_id, index):
    student = Students.objects.get(RegistrationNo=stu_id)
    paper = QuestionPaper.objects.get(id=paper_id)
    answersheet = AnswerSheet.objects.get(of_student=student, of_paper=paper)
    # classsection = Class.objects.get(class_section=class_section)
    questions = Question.objects.filter(question_paper=paper)
    return render(request, 'subjectivequestions/checkpaper.html',
                  {'answersheet': answersheet, 'questions': questions, 'class_section': class_section,
                   'paperid': paper_id, 'studentid': stu_id, 'index': index})
    # return HttpResponse('<object data="'+answersheet.sheet.url+'" type="application/pdf" width="50%" height="100%"<p><b>Example fallback content</b>: This browser does not support PDFs. Please download the PDF to view it: <a href="'+answersheet.sheet.url+'">Download PDF</a>.</p></object>')


def submitmarks(request, class_section, paper_id, stu_id, index):
    student = Students.objects.get(RegistrationNo=stu_id)
    paper = QuestionPaper.objects.get(id=paper_id)
    questions = Question.objects.filter(question_paper=paper)
    if request.method == 'POST':
        for i in questions:
            try:
                marking = Marks()
                marks = request.POST[str(i.id)]
                marking.number = int(marks)
                marking.of_student = student
                marking.of_question = i
                marking.save()
            except:
                pass

    return HttpResponse('<h1>Sumbmitted Successfully!<br><a href="/teacher/subjective/'+str(index)+"/"+'">GO BACK</a>')


def classesviewmarks(request, index):
    all_classes = Classes.objects.all()
    return render(request, 'subjectivequestions/classesviewmarks.html', {'context': all_classes, 'index': index})


def testsviewmarks(request, class_section, index):
    this_class = Classes.objects.get(ClassSection=class_section)
    all_tests = QuestionPaper.objects.filter(of_class=this_class)
    return render(request, 'subjectivequestions/testsviewmarks.html', {'index':index, 'context': all_tests, 'class_section': class_section})


def studentsviewmarks(request, class_section, paper_id, index):
    classSection = Classes.objects.get(ClassSection=class_section)
    all_students = Students.objects.filter(ClassSection=classSection)
    all_answers = AnswerSheet.objects.filter(of_paper=paper_id)
    all_students_submitted = []
    for i in all_answers:
        all_students_submitted.append(i.of_student.RegistrationNo)
    submitted = []
    for i in all_students:
        if i.RegistrationNo in all_students_submitted:
            submitted.append(True)
        else:
            submitted.append(False)
    return render(request, 'subjectivequestions/studentsviewmarks.html',
                  {'index': index, 'context': zip(all_students, submitted), 'class_section': class_section, 'paperid': paper_id})


def viewmarks(request, class_section, paper_id, stu_id, index):
    questionPaperObject = QuestionPaper.objects.get(id=paper_id)
    questions = Question.objects.filter(question_paper=questionPaperObject)
    marks = Marks.objects.filter(of_question__in=questions)
    return render(request, 'subjectivequestions/viewmarks.html', {'context': marks, 'index': index})


def addparameter(request, class_section, paper_id, ques_id, index):
    if request.method == 'POST':
        question = Question.objects.get(id=ques_id)
        try:
            i = 1
            while True:
                param = request.POST['P'+str(i)]
                number = request.POST['M' + str(i)]
                i += 1
                newparam = Parameters()
                newparam.marks = int(number)
                newparam.of_question = question
                newparam.name = param
                newparam.save()
        except:
            pass

        return redirect('/teacher/subjective/'+str(index)+'/viewtest/'+str(class_section)+'/'+str(paper_id))
