from django.db import models

# Create your models here.

class Personal_Info(models.Model):
    Index = models.IntegerField(primary_key=True)
    Role = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    MiddleName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    DOB = models.DateField(auto_now=False)
    Sex = models.CharField(max_length=12)
    Contact = models.CharField(max_length=12)
    EMail = models.CharField(max_length=25)
    BloodGroup = models.CharField(max_length=3)
    AddressLine1 = models.TextField(max_length=50)
    AddressLine2 = models.CharField(max_length=50)
    AddressLine3 = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=6)
    CommuteDistance = models.IntegerField()             # XX.X kms
    CommuteTime = models.IntegerField()                 # minutes
    CommuteBy = models.CharField(max_length=10)


class Rooms_2018(models.Model):
    RoomID = models.CharField(primary_key=True, max_length=8)
    Capacity = models.IntegerField(default=0)
    Floor = models.IntegerField(default=0)
    Fans = models.IntegerField(default=0)
    Lights = models.IntegerField(default=0)
    AC = models.IntegerField(default=0)
    Windows = models.IntegerField(default=0)
    Doors = models.IntegerField(default=0)


class Subjects(models.Model):
    SubjectCode = models.CharField(primary_key=True, max_length=5)          # 07GEO, 12MAT
    SubjectName = models.CharField(max_length=20)                           # GEO, MAT
    TaughtSince = models.DateField(auto_now=True)
    TaughtTill = models.DateField(auto_now=True)
    NoOfTeachers = models.IntegerField(default=0)                        # total in all classes and sections


class Feedback(models.Model):
    FeedbackID = models.CharField(primary_key=True, max_length=10)
    GivenBy = models.CharField(max_length=20)
    GivenFor = models.CharField(max_length=20)
    SubjectCode = models.ForeignKey(Subjects, max_length=5)
    SubjectDifficulty = models.IntegerField(default=0)                   # rating of 1 to 5
    CreateInterest = models.IntegerField(default=0)
    HomeWorkLoad = models.IntegerField(default=0)
    OverallPerformance = models.IntegerField(default=0)
    Suggestions = models.TextField(max_length=50, default='NA')
