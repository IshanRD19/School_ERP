from django.db import models
from principal.models import *

# Create your models here.

class Teachers(models.Model):
    TeacherID = models.CharField(primary_key=True, max_length=12)
    Index = models.ForeignKey(Personal_Info, limit_choices_to={'FirstName__in':Personal_Info.objects.filter(Role='Teacher').values('FirstName')})
    ClassesPerWeek = models.IntegerField(default=0)
    Qualification1 = models.TextField(max_length=50, default='NA')
    Qualification2 = models.TextField(max_length=50, default='NA')
    PreviousExperience = models.TextField(max_length=250)
    ExperienceOfMonths = models.IntegerField(default=0)                     # no. of months
    Salary = models.IntegerField(default=0)                                 # without commas
    SessionYear = models.CharField(max_length=9)                            # 2017-2018
    Attribute1 = models.CharField(max_length=20)
    Attribute2 = models.CharField(max_length=20)
    Attribute3 = models.CharField(max_length=20)
    Attribute4 = models.CharField(max_length=20)
    Attribute5 = models.CharField(max_length=20)
    Attribute1Rating = models.IntegerField(default=0)
    Attribute2Rating = models.IntegerField(default=0)
    Attribute3Rating = models.IntegerField(default=0)
    Attribute4Rating = models.IntegerField(default=0)
    Attribute5Rating = models.IntegerField(default=0)
    Subject1 = models.CharField(max_length=25, default='')
    Subject2 = models.CharField(max_length=25, default='')
    Subject3 = models.CharField(max_length=25, default='')
    Skill1 = models.CharField(max_length=25, default=0)
    Skill2 = models.CharField(max_length=25, default=0)
    Skill3 = models.CharField(max_length=25, default=0)
    def __str__(self):
        return str(self.TeacherID)


class Classes(models.Model):
    ClassSection = models.CharField(primary_key=True, max_length=3)         # 09C
    RoomID = models.ForeignKey(Rooms)
    ClassTeacherID = models.ForeignKey(Teachers)
    Students = models.IntegerField(default=0)
    Subjects = models.IntegerField(default=0)
    #ClassPicture = models.ImageField(upload_to='class_picture', blank=True)
    SessionYear = models.CharField(max_length=9)
    #From = models.DateField(auto_now=False)
    #Till = models.DateField(auto_now=False)
    def __str__(self):
        return str(self.ClassSection)


class SubjectAllotment (models.Model):
    Class = models.ForeignKey(Classes)
    Subject = models.ForeignKey(Subjects)
    Teacher = models.ForeignKey(Teachers)
    SessionYear = models.CharField(max_length=9)
    def __str__(self):
        return str(self.Class)+"-"+str(self.Subject)+"-"+str(self.Teacher.Index.FirstName)


#class Q_Papers(models.Model):
 #   QPaperID = models.CharField(primary_key=True, max_length=15)            # DDMMYYYY-09C-GEO-2
 #  SubjectCode = models.ForeignKey(Subjects)
   # MadeBy = models.ForeignKey(Teachers_2018)
    #Topic = models.TextField(max_length=25)                                 # test of which unit or topic
    #MaxMarks = models.IntegerField(default=0)
    #StartTime = models.TimeField()
    #EndTime = models.TimeField()
    #Appeared = models.IntegerField(default=0)                               # total students who took test
    #AvgMarks = models.IntegerField(default=0)


class Teacher_Login_info(models.Model):
    username = models.ForeignKey(Personal_Info, limit_choices_to={'FirstName__in':Personal_Info.objects.filter(Role='Teacher').values('FirstName')})
    password = models.CharField(max_length=16)
    def __str__(self):
        return str(self.username)


class Assigments(models.Model):
    CreationDate = models.DateField(auto_now=True)
    BeginFrom = models.DateField(auto_now=True)
    Deadline = models.DateField(auto_now=True)
    Teacher = models.ForeignKey(Teachers)
    ClassSection = models.ForeignKey(Classes)
    Subject = models.ForeignKey(Subjects)
    Topic = models.CharField(max_length=40)
    Description = models.TextField(max_length=500)
    SessionYear = models.CharField(max_length=9)
    def __str__(self):
        return str(self.id)+"-"+str(self.Subject)


class Task_List(models.Model):
    CreatedOn = models.DateTimeField(auto_now=True)
    DeadLine = models.DateTimeField(blank=True, null=True)
    Task_Detail = models.CharField(max_length=100)
    Priority = models.IntegerField(default=2)         # 1-2-3
    Completed = models.BooleanField(default=False)





