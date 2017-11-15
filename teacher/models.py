from django.db import models
from principal.models import  Personal_Info, Rooms_2018, Subjects

# Create your models here.

class Teachers_2018(models.Model):
    TeacherID = models.CharField(primary_key=True, max_length=12)
    Index = models.ForeignKey(Personal_Info, limit_choices_to={'FirstName__in':Personal_Info.objects.filter(Role='Teacher').values('FirstName')})
    ClassesPerWeek = models.IntegerField(default=0)
    Qualification = models.TextField(max_length=50, default='NA')
    Experience = models.IntegerField(default=0)                             # no. of months
    Salary = models.IntegerField(default=0)                                 # without commas
    def __str__(self):
        return str(self.TeacherID)


class Classes_2018(models.Model):
    ClassSection = models.CharField(primary_key=True, max_length=3)         # 09C
    RoomID = models.ForeignKey(Rooms_2018)
    ClassTeacherID = models.ForeignKey(Teachers_2018)
    Students = models.IntegerField(default=0)
    Subjects = models.IntegerField(default=0)
    #From = models.DateField(auto_now=False)
    #Till = models.DateField(auto_now=False)
    def __str__(self):
        return str(self.ClassSection)


class SubjectAllotment_2018 (models.Model):
    Class = models.ForeignKey(Classes_2018)
    Subject = models.ForeignKey(Subjects)
    Teacher = models.ForeignKey(Teachers_2018)
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
