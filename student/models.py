from django.db import models
from principal.models import Personal_Info, Subjects

# Create your models here.

class Students_2018(models.Model):
    RegistrationNo = models.CharField(primary_key=True, max_length=20)
    Index = models.ForeignKey(Personal_Info)
    ClassSection = models.CharField(max_length=3, default='NA')             # 07B
    RollNo = models.CharField(max_length=3, default='NA')
    From = models.DateField(auto_now=False)                                 # active from date
    Till = models.DateField(auto_now=False)                                 # active till date
    NoOfSubjects = models.IntegerField(default=0)                           # total subjects
    AcademicScore = models.IntegerField(default=0)                          # aggregate %
    ClassRank = models.IntegerField(default=0)                              # current rank in class


class TimeTableLookUp(model.Model):
    TTID = models.CharField(primary_key=True, max_length=3)                 # Numerals 1,2,3,...
    WeekDay = models.CharField(max_length=9)                                # Monday,Tuesday,...
    StartTime = models.TimeField()
    EndTime = models.TimeField()


class TimeTable_2018(models.Model):
    TTID = models.ForeignKey(TimeTableLookUp, primary_key=True)
    ClassSection = models.CharField(primary_key=True, max_length=3)
    SubjectCode = models.ForeignKey(Subjects)
    #TeacherID = models.ForeignKey(Teachers_2018)


class Attendance_2018(models.Model):
    RegistrationNo = models.ForeignKey(Students_2018, primary_key=True)
    TTID = models.ForeignKey(TimeTableLookUp, primary_key=True, max_length=12)
    ClassDate = models.DateField(primary_key=True, auto_now=False)         # DD/MM/YYYY
    Attendance = models.CharField(max_length=8)                            # present or absent