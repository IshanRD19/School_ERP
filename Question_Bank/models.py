from django.db import models
from teacher.models import Teachers, Classes
from principal.models import Personal_Info
# from Student.models import *
# Create your models here.


class Questions(models.Model):
    statement = models.TextField(max_length=200)
    correctOption = models.CharField(max_length=2)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to = 'pic_folder/', default = None)
    image2 = models.ImageField(upload_to = 'pic_folder/', default = None)
    maxMarks = models.IntegerField()
    subject = models.CharField(max_length=20, default='NA')
    subCategory = models.CharField(max_length=20)
    difficultyLevel = models.IntegerField(default=2)        # 1 to 5 for increasing toughness
    timeLimit = models.IntegerField()
    createdby = models.ForeignKey(Personal_Info)
    def __str__(self):
        return self.statement


class Question_Papers(models.Model):
    qpName = models.CharField(max_length=30)
    # timeDuration = models.DecimalField(max_digits=8, decimal_places=3)
    createdOn = models.DateField(auto_now=True)
    activeFlag = models.BooleanField(default=False)
    questions = models.ManyToManyField(Questions, related_name="question")
    # createdby = models.ForeignKey(Teachers)
    for_class = models.ForeignKey(Classes)

    def __str__(self):
        return self.qpName

# class Records(models.Model):
#
#     recordID = models.CharField(primary_key=True, max_length=10)
#     fromTime = models.TimeField(auto_now=True)
#     tillTime = models.TimeField(auto_now=True)
#     studentID = models.ForeignKey(Students)
#     questionID = models.ForeignKey(Questions)
#     response = models.CharField(max_length=2)


# class UploadLog(models.Model):
#     # time = models.DateField(auto=now)
#     file = models.FileField(upload_to='fileLog/')

class Session(models.Model):
    start = models.DateTimeField()
    questionpaper = models.ForeignKey(Question_Papers)
    end = models.DateTimeField(null=True)
    student = models.ForeignKey(Personal_Info)
    def __str__(self):
        return str(self.id)


class Log(models.Model):
    time = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Questions)
    session = models.ForeignKey(Session)

    def __str__(self):
        return str(self.time)+" "+str(self.session.id)


class Responses(models.Model):
    session = models.ForeignKey(Session)
    question = models.ForeignKey(Questions, null=True)
    response = models.CharField(max_length=1)
