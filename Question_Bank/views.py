from django.shortcuts import render, redirect
from Question_Bank.models import *
from teacher.models import Teachers, SubjectAllotment, Classes
from principal.models import Personal_Info
import pandas as pd
from django.http import HttpResponse
import datetime
# Create your views here.


def index(request, index):
    return render(request, 'questionpaper/home.html', {'index': index})


def createtest(request, index):
    return render(request, 'questionpaper/createtest.html', {'index': index})


def uploadquestions(request, index):
    return render(request, 'questionpaper/uploadquestions.html', {'index': index})


def submitquestions(request, index):
    if request.method == 'POST':
        csv_file = request.FILES['ques']
        dataFrame = pd.read_csv(csv_file)
        for i in range(dataFrame.shape[0]):
            question = Questions()
            question.subject = dataFrame[dataFrame.columns[0]][i]
            question.subCategory = dataFrame[dataFrame.columns[1]][i]
            question.timeLimit = dataFrame[dataFrame.columns[2]][i]
            question.maxMarks = dataFrame[dataFrame.columns[3]][i]
            question.statement = dataFrame[dataFrame.columns[4]][i]
            question.correctOption = dataFrame[dataFrame.columns[5]][i]
            question.option1 = dataFrame[dataFrame.columns[6]][i]
            question.option2 = dataFrame[dataFrame.columns[7]][i]
            question.option3 = dataFrame[dataFrame.columns[8]][i]
            question.option4 = dataFrame[dataFrame.columns[9]][i]
            question.createdby = Personal_Info.objects.get(Index=index)
            question.save()
        return redirect('/teacher/multiplechoice/'+str(index)+'/')


def createquestionpaper(request, index):
    questions = Questions.objects.all()
    person = Personal_Info.objects.get(Index=index)
    teacher = Teachers.objects.get(Index=person)
    subjects = SubjectAllotment.objects.filter(Teacher=teacher)
    return render(request, 'questionpaper/createquestionpaper.html', {'context': questions, 'index': index, 'subjects': subjects})


def submitquestionpaper(request, index):
    if request.method == 'POST':
        question_paper = Question_Papers()
        question_paper.qpName = request.POST['qname']
        question_paper.for_class = SubjectAllotment.objects.get(id=request.POST['class']).Class
        all_questions = Questions.objects.all()
        # s = []
        question_paper.save()
        for i in all_questions:
            try:
                if request.POST[str(i.id)]:
                # s.append(i.statement)
                    question_paper.questions.add(i)
            except:
                pass
        question_paper.save()
        return HttpResponse('<h1>Created Successfully</h1><br><a href="/teacher/multiplechoice/'+str(index)+'/">GO BACK</a>')
    return redirect('/teacher/multiplechoice/'+str(index)+'/')


def editquestions(request, index):
    all_questions = Questions.objects.all()
    return render(request, 'questionpaper/allquestionsforedit.html', {'context': all_questions, 'index': index})


def editquestionid(request, question_id, index):
    question = Questions.objects.get(id=question_id)
    return render(request, 'questionpaper/editquestion.html', {'context': question, 'index': index})


def questionedit(request, question_id, index):
    if request.method == 'POST':
        question = Questions.objects.get(id=question_id)
        question.statement = str(request.POST['statement'])
        question.correctOption = str(request.POST['correct'])
        question.option1 = str(request.POST['option1'])
        question.option2 = str(request.POST['option2'])
        question.option3 = str(request.POST['option3'])
        question.option4 = str(request.POST['option4'])
        question.maxMarks = str(request.POST['marks'])
        question.subject = str(request.POST['subject'])
        question.subCategory = str(request.POST['subcategory'])
        question.difficultyLevel = str(request.POST['difficulty'])
        question.timeLimit = str(request.POST['time'])
        question.save()
        return HttpResponse('<h1>Created Successfully</h1><br><a href="/teacher/multiplechoice/'+str(index)+'/">GO BACK</a>')

    return redirect('/teacher/multiplechoice/'+str(index)+'/')


def editquestionpaper(request, index):
    all_question_papers = Question_Papers.objects.all()
    return render(request, 'questionpaper/questionpapersforedit.html', {'context': all_question_papers, 'index':index})


def questionpaperid(request, questionpaper_id, index):
    question_paper = Question_Papers.objects.get(id=questionpaper_id)
    all_questions = Questions.objects.all()
    return render(request, 'questionpaper/editquestionpaper.html', {'question_paper': question_paper, 'questions': all_questions, 'index': index})


def questionpaperedit(request, questionpaper_id, index):
    if request.method == 'POST':
        question_paper = Question_Papers.objects.get(id=questionpaper_id)
        question_paper.qpName = request.POST['qpname']
        all_questions = Questions.objects.all()
        try:
            if request.POST['active']:
                question_paper.activeFlag = True
        except:
            question_paper.activeFlag = False
            # s = []
        question_paper.save()
        for i in all_questions:
            try:
                if request.POST[str(i.id)]:
                # s.append(i.statement)
                    question_paper.questions.add(i)
            except:
                question_paper.questions.remove(i)
        question_paper.save()
        return HttpResponse('<h1>Created Successfully</h1><br><a href="/teacher/multiplechoice/'+str(index)+'/">GO BACK</a>')
    return redirect('/teacher/multiplechoice/'+str(index)+'/')


def taketest(request, index):
    all_question_papers = Question_Papers.objects.filter(activeFlag=True)
    return render(request, 'questionpaper/taketesthome.html', {'context': all_question_papers, 'index': index})


def attempttest(request, questionpaper_id, index):
    question_paper = Question_Papers.objects.get(id=questionpaper_id)
    #all_test_questions = question_paper.questions.all()
    iterations = [i for i in range(1, len(question_paper.questions.all())+1)]
    current_session = Session()
    current_session.start = datetime.datetime.now()
    current_session.questionpaper = question_paper
    current_session.student = Personal_Info.objects.get(Index=index)
    current_session.save()
    return render(request, 'questionpaper/attempttest.html', {'context': question_paper, 'index': index, 'session':current_session, 'iterations':zip(iterations, question_paper.questions.all())})


def testresult(request, questionpaper_id, session_id, index):
    session = Session.objects.get(id=session_id)
    session.end = datetime.datetime.now()
    session.save()

    question_paper = Question_Papers.objects.get(id=questionpaper_id)
    totalquestions = question_paper.questions.count()
    correct = 0
    marks = 0
    attempted = totalquestions

    if request.method == "POST":
        for i in question_paper.questions.all():
            res = Responses()
            res.session = session
            res.question = i
            try:
                response = request.POST[str(i.id)]
                res.response = response
                if str(response) == str(i.correctOption):
                    correct += 1
                    marks += i.maxMarks
            except:
                attempted -= 1
            res.save()

    return render (request, 'questionpaper/testresults.html', {'question_paper': question_paper, 'totalquestions': totalquestions, 'correct': correct,'attempted': attempted, 'marks': marks, 'incorrect': attempted - correct, 'index': index})


def logs(request, index): #vaginatarian
    records = Records.objects.all()
    return render(request, 'questionpaper/logs.html', { 'context': records})


def createlog(request, questionpaper_id, index):
    if request.method == 'GET':

        id = request.GET['id']
        session_id = request.GET['session']
        session = Session.objects.get(id=session_id)
        question = Question_Papers.objects.get(id=questionpaper_id).questions.all()[int(id)-1]

        log = Log()
        log.session = session
        log.question = question
        log.save()

        return HttpResponse(question.statement)