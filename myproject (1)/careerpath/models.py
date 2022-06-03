from django.db import models
from django.db.models.fields import IntegerField

class feedback(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    email = models.EmailField()
    Mobileno = models.CharField(max_length=10)
    msg = models.TextField()
    class Meta:
        db_table='feedback'

class Register(models.Model):
    id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Emailid=models.CharField(max_length=30)
    DOB=models.DateField(auto_now=False, auto_now_add=False)
    Category=models.CharField(max_length=30)
    
    Address=models.CharField(max_length=30)
    Mobile =models.CharField(max_length=30)
    Altmobile=models.CharField(max_length=30)
    FatherName=models.CharField(max_length=30)
    
    Foccupation=models.CharField(max_length=30)
    Mothersname=models.CharField(max_length=30)
    Moccupation=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    
    State=models.CharField(max_length=30)
    Zip=models.CharField(max_length=20)
    Password=models.CharField(max_length=30)
    confirmPassword=models.CharField(max_length=30)
    Image=models.ImageField(upload_to="media/photos")
    Branch=models.CharField(max_length=30)
    
    Resume=models.FileField(upload_to="media/files")
    SSCName=models.CharField(max_length=30)
    BoardName1=models.CharField(max_length=30)
    Branch1=models.CharField(max_length=30)
    
    Percentage1=models.CharField(max_length=30)
    YOP1=models.CharField(max_length=30)
    HSCName=models.CharField(max_length=30)
    BoardName2=models.CharField(max_length=30)
    
    Branch2=models.CharField(max_length=30)
    Percentage2=models.CharField(max_length=30)
    YOP2=models.CharField(max_length=30)
    CollegeName1=models.CharField(max_length=30)
    
    UniversityName1=models.CharField(max_length=30)
    DegreeName1=models.CharField(max_length=30)
    Percentage3=models.CharField(max_length=30)
    YOP3=models.CharField(max_length=30)
    
    CollegeName2=models.CharField(max_length=30)
    UniversityName2=models.CharField(max_length=30)
    DegreeName2=models.CharField(max_length=30)
    percentage4=models.CharField(max_length=30)
    YOP4=models.CharField(max_length=30)
    
    AOI=models.CharField(max_length=30)
    AOS=models.CharField(max_length=30)
    Cert=models.CharField(max_length=30)
    
    Hobbies=models.CharField(max_length=30)
    SpecialA=models.CharField(max_length=30)
    ECA=models.CharField(max_length=30)
    UpdateTime=models.DateField( )
    DOB=models.DateField(auto_now=False, auto_now_add=False)
#class Login_user(models.Model):
    #id=models.AutoField(primary_key=True)
   # Name = models.CharField(max_length=30)
    #Email=models.CharField(max_length=30)
    #Password=models.CharField(max_length=30)
    