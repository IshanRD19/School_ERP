from django.db import models

# Create your models here.

class Personal_Info(models.Model):
    Index = models.IntegerField(primary_key=True)
    Role = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    MiddleName = models.CharField(max_length=20, null=True, blank=True)
    LastName = models.CharField(max_length=20)
    #ProfilePicture = models.ImageField(upload_to='profile_image', blank=True)
    DOB = models.DateField(auto_now=False)
    Sex = models.CharField(max_length=12)
    Contact = models.CharField(max_length=12)
    SecondaryContact = models.CharField(max_length=12,default='')
    EMail = models.CharField(max_length=40)
    SecondaryEMail =models.CharField(max_length=40,default='')
    BloodGroup = models.CharField(max_length=3)
    AddressLine1 = models.TextField(max_length=60)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=6)
    CommuteDistance = models.FloatField()             # XX.X kms
    CommuteTime = models.IntegerField()                 # minutes
    CommuteBy = models.CharField(max_length=10)
    JoiningDate = models.DateField(default='')
    def __str__(self):
        return str(self.FirstName)+'-'+str(self.Index)


class Rooms(models.Model):
    RoomID = models.CharField(primary_key=True, max_length=8)
    Capacity = models.IntegerField(default=0)
    #RoomImage = models.ImageField(upload_to='room_image', blank=True)
    Floor = models.IntegerField(default=0)
    Fans = models.IntegerField(default=0)
    Lights = models.IntegerField(default=0)
    AC = models.IntegerField(default=0)
    Windows = models.IntegerField(default=0)
    Doors = models.IntegerField(default=0)
    def __str__(self):
        return str(self.RoomID)


class Subjects(models.Model):
    SubjectCode = models.CharField(primary_key=True, max_length=5)       # 07GEO, 12MAT
    SubjectName = models.CharField(max_length=20)                        # GEO, MAT
    Description = models.TextField(max_length=200)
    #SubjectImage = models.ImageField(upload_to='subject_image', blank=True)
    Books = models.TextField(max_length=150)
    Prerequisites = models.TextField(max_length=150)
    NoOfTeachers = models.IntegerField(default=0)                        # total in all classes and sections
    BaseSubject = models.CharField(max_length=20)
    Category = models.CharField(max_length=10)                           # importance level
    DifficultyLevel = models.IntegerField(default=2)                     # 1 (easy) to 5 (hard)
    AvgScore = models.DecimalField(max_digits=4, decimal_places=2)

    #TaughtSince = models.DateField(auto_now=False )
    #TaughtTill = models.DateField(auto_now=False)
    def __str__(self):
        return str(self.SubjectCode)


#class Feedback(models.Model):
 #   FeedbackID = models.CharField(primary_key=True, max_length=10)
  #  GivenBy = models.CharField(max_length=20)
   # GivenFor = models.CharField(max_length=20)
    #SubjectCode = models.ForeignKey(Subjects, max_length=5)
    #SubjectDifficulty = models.IntegerField(default=0)                   # rating of 1 to 5
    #CreateInterest = models.IntegerField(default=0)
    #HomeWorkLoad = models.IntegerField(default=0)
    #OverallPerformance = models.IntegerField(default=0)
    #Suggestions = models.TextField(max_length=50, default='NA')


class login_info(models.Model):
    username = models.ForeignKey(Personal_Info)
    password = models.CharField(max_length=16)


class AssignmentParameters(models.Model):
    GradingParameter = models.CharField(max_length=20)
    def __str__(self):
        return str(self.id)+":"+str(self.GradingParameter)


class School_Details(models.Model):
    #SchoolPicture = models.ImageField(upload_to='school_image', blank=True)
    Address = models.CharField(max_length=60)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Pincode = models.CharField(max_length=6)
    Contact1 = models.CharField(max_length=12)
    Contact2 = models.CharField(max_length=12)
    Contact3 = models.CharField(max_length=12)


class Messages(models.Model):
    Sender = models.ForeignKey(Personal_Info, related_name='messages_sent')
    Receiver = models.ForeignKey(Personal_Info, related_name='messages_received')
    DateTime = models.DateTimeField(auto_now=True)
    Text = models.TextField(max_length=600)
    #Image = models.ImageField()
    Status = models.CharField(max_length=10, default='Unread')          # Read or Unread