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
