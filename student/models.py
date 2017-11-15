from django.db import models
from principal.models import *
from teacher.models import *
from student.models import *

# Create your models here.


class Students_2018(models.Model):
    RegistrationNo = models.CharField(primary_key=True, max_length=20)
    Index = models.ForeignKey(Personal_Info, limit_choices_to={'FirstName__in':Personal_Info.objects.filter(Role='Student').values('FirstName')})
    ClassSection = models.CharField(max_length=3, default='NA')             # 07B
    RollNo = models.CharField(max_length=3, default='NA')
    #From = models.DateField(auto_now=False)                                 # active from date
    #Till = models.DateField(auto_now=False)                                 # active till date
    NoOfSubjects = models.IntegerField(default=0)                           # total subjects
    AcademicScore = models.IntegerField(default=0)                          # aggregate %
    ClassRank = models.IntegerField(default=0)                              # current rank in class
    def __str__(self):
        return str(self.ClassSection)+"-"+str(self.RollNo)


class TimeTableLookUp(models.Model):
    TTID = models.CharField(primary_key=True, max_length=3)                 # Numerals 1,2,3,...
    WeekDay = models.CharField(max_length=9)                                # Monday,Tuesday,...
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    def __str__(self):
        return str(self.TTID)


class TimeTable_2018(models.Model):
    TTID = models.ForeignKey(TimeTableLookUp)
    Class = models.ForeignKey(Classes_2018)
    Subject = models.ForeignKey(Subjects)
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