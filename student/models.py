from django.db import models
from principal.models import Personal_Info, Subjects

# Create your models here.


class Students_2018(models.Model):
    RegistrationNo = models.CharField(primary_key=True, max_length=20, default='NA')
    Index = models.ForeignKey(Personal_Info, limit_choices_to={'FirstName__in':Personal_Info.objects.filter(Role='student').values('FirstName')})
    ClassSection = models.CharField(max_length=3, default='NA')             # 07B
    RollNo = models.CharField(max_length=3, default='NA')
    From = models.DateField(auto_now=False)                                 # active from date
    Till = models.DateField(auto_now=False)                                 # active till date
    NoOfSubjects = models.IntegerField(default=0)                           # total subjects
    AcademicScore = models.IntegerField(default=0)                          # aggregate %
    ClassRank = models.IntegerField(default=0)                              # current rank in class


class TimeTableLookUp(models.Model):
    TTID = models.CharField(primary_key=True, max_length=3)                 # Numerals 1,2,3,...
    WeekDay = models.CharField(max_length=9)                                # Monday,Tuesday,...
    StartTime = models.TimeField()
    EndTime = models.TimeField()


class TimeTable_2018(models.Model):
    TTID = models.ForeignKey(TimeTableLookUp)
    ClassSection = models.CharField(max_length=3)
    SubjectCode = models.ForeignKey(Subjects)


class Attendance_2018(models.Model):
    RegistrationNo = models.ForeignKey(Students_2018)
    TTID = models.ForeignKey(TimeTableLookUp, max_length=12)
    ClassDate = models.DateField(auto_now=False, null=True, blank=True)         # MM/DD/YYYY
    Attendance = models.CharField(max_length=8)                            # present or absent


class Student_login_info(models.Model):
    username = models.ForeignKey(Personal_Info, limit_choices_to={'EMail__in':Personal_Info.objects.filter(Role='student').values('EMail')})
    password = models.CharField(max_length=16)