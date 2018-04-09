from django.db import models
from principal.models import Rooms, Personal_Info, AssignmentParameters
from teacher.models import Teachers, Classes, Subjects, Assigments

# Create your models here.


class Students(models.Model):
    RegistrationNo = models.CharField(primary_key=True, max_length=20)
    Index = models.ForeignKey(Personal_Info, limit_choices_to={'FirstName__in':Personal_Info.objects.filter(Role='Student').values('FirstName')})
    ClassSection = models.ForeignKey(Classes)             # 07B
    RollNo = models.CharField(max_length=3, default='NA')
    #From = models.DateField(auto_now=False)                                 # active from date
    #Till = models.DateField(auto_now=False)                                 # active till date
    NoOfSubjects = models.IntegerField(default=0)                           # total subjects
    AcademicScore = models.IntegerField(default=0)                          # aggregate %
    ClassRank = models.IntegerField(default=0)                              # current rank in class
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
    Sibling1DOB = models.DateField(blank=True, null=True)
    Sibling2DOB = models.DateField(blank=True, null=True)
    def __str__(self):
        return str(self.ClassSection)+"-"+str(self.RollNo)


class TimeTableLookUp(models.Model):
    TTID = models.CharField(primary_key=True, max_length=3)                 # Numerals 1,2,3,...
    WeekDay = models.CharField(max_length=9)                                # Monday,Tuesday,...
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    def __str__(self):
        return str(self.TTID)


class TimeTable(models.Model):
    TTID = models.ForeignKey(TimeTableLookUp)
    Class = models.ForeignKey(Classes)
    Subject = models.ForeignKey(Subjects)
    SessionYear = models.CharField(max_length=9)
    def __str__(self):
        return str(self.TTID)+"-"+str(self.Class)+"-"+str(self.Subject)

#class Attendance_2018(models.Model):
 #   RegistrationNo = models.ForeignKey(Students_2018)
  #  TTID = models.ForeignKey(TimeTableLookUp, max_length=12)
   # ClassDate = models.DateField(auto_now=False, null=True, blank=True)         # MM/DD/YYYY
    #Attendance = models.CharField(max_length=8)                            # present or absent


class Student_login_info(models.Model):
    username = models.ForeignKey(Personal_Info, limit_choices_to={'EMail__in':Personal_Info.objects.filter(Role='Student').values('EMail')})
    password = models.CharField(max_length=16)
    def __str__(self):
        return str(self.username)


class AssignmentGrades(models.Model):
    Assigment = models.ForeignKey(Assigments)
    Student = models.ForeignKey(Students)
    GradingParameter = models.ForeignKey(AssignmentParameters)
    Grade = models.IntegerField(default=3)



