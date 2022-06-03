from django.http.request import host_validation_re
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime
from .models import Register
from . import models


# from .models import Student
def index(request):
    return render(request,"home.html")  #ithe home pahije krn apn home thevl fist page index nhi

def extra(request):
    # return HttpResponse("This is my aboutpage(/)")
     return render(request,'extra.html')
def careerchoice(request):
    # return HttpResponse("This is my projectpage(/)")
     return render(request,'careerchoice.html')
def student(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'student.html')
def register(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'register.html')
def login_request(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'login.html')
def logout_user(request):
    return render(request,'home.html')
def test(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'test.html')

def timer(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'timer.html')
 
def feedback(request):
    if request.method=="POST": 
        name=request.POST['name']
        branch=request.POST['branch']
        email=request.POST['email']
        Mobileno=request.POST['Mobileno']
        msg=request.POST['msg']
        ins=models.feedback(name=name,branch=branch,email=email,Mobileno=Mobileno,msg=msg)
        ins.save()
        # print("Data has been writeen to be db")
        messages.success(request,'Record successfully')
        return render(request,'feedback.html')
    else:
        return render(request,'feedback.html')



def job_listing(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'job_listing.html')
def jobcategory(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'jobcategory.html')
def job(request):
    # return HttpResponse("This is my contactpage(/)")
    return render(request,'job.html') 
def adminlogin(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'adminlogin.html')
def base(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'base.html')
def addstream(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'addstream.html')
def adminfeedback(request):
    # return HttpResponse("This is my contactpage(/)")
    resultdisplay=models.feedback.objects.all()
    
    return render(request,'adminfeedback.html',{'feedback':resultdisplay}) 
    # return render(request,'adminfeedback.html')
def report(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'report.html')
def adminapply(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'adminapply.html')
def arts(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'arts.html')
def deletestream(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'deletestream.html')
def updatestream(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'updatestream.html')
 
def science(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'science.html')
def Graduates(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'Graduates.html')
def commerse(request):
    # return HttpResponse("This is my contactpage(/)")
     return render(request,'commerse.html')
 

def dashboard(request):
    if not request.session.get('user_email'):
        messages.add_message(request, messages.ERROR,"Please login  ")
        return redirect("login")

    if request.method=='GET':
        data=request.session.get("user_name")
        user={}
        print(request.session.get("u_name"))
        user['user_name']=data
        return render(request, 'home.html', user)   #ithe pn home yeil krn apn dashboard asa page create nhi kely kahi  home page ha aplya  project first page ahe ok klal
    
def register(request):
    if request.method=="GET":
        return render(request, "register.html")
    else:
        print(request.POST)
        # keep model attribute name same every where 
        data={}
        
        data={
           "Emailid": request.POST['Emailid'],
            "Name": request.POST['Name'],
            "DOB": request.POST['DOB'],
            "Category": request.POST['Category'],
            "Mobile": request.POST['Mobile'],
            "Altmobile": request.POST['Altmobile'],
            "Address": request.POST['Address'],
            "FatherName": request.POST['FatherName'],
            "Foccupation": request.POST['Foccupation'],
            "Mothersname": request.POST['Mothersname'],
            "Moccupation": request.POST['Moccupation'],
            "City": request.POST['City'],
            "State": request.POST['State'],
            "Password": request.POST['Password'],
            "ConfirmPassword": request.POST['ConfirmPassword'],
            "Branch": request.POST['Branch'],
            "Zip": request.POST['Zip'],
            "SSCName": request.POST['SSCName'],
            "BoardName1": request.POST['BoardName1'],
            "Branch1": request.POST['Branch1'],
            "Percentage1": request.POST['Percentage1'],
            "YOP1": request.POST['YOP1'],
            "HSCName": request.POST['HSCName'],
            "BoardName2": request.POST['BoardName2'],
            "Branch2": request.POST['Branch2'],
            "Percentage2": request.POST['Percentage2'],
            "YOP2": request.POST['YOP2'],
            "CollegeName1": request.POST['CollegeName1'],
            "UniversityName1": request.POST['UniversityName1'],
            "DegreeName1": request.POST['DegreeName1'],
        
            "Percentage3": request.POST['Percentage3'],
            "YOP3": request.POST['YOP3'],
            "DegreeName2": request.POST['DegreeName2'],
            "UniversityName2":request.POST['UniversityName2'],
            "CollegeName2": request.POST['CollegeName2'],
            "Percentage4": request.POST['Percentage4'],
            "YOP4": request.POST['YOP4'],
            "AOI": request.POST['AOI'],
            "AOS": request.POST['AOS'],
            "Cert":request.POST['Cert'],
            "Hobbies": request.POST['Hobbies'],
            "SpecialA": request.POST['SpecialA'],
            "ECA": request.POST['ECA'],
        
        }
        
        
        
        r=Register(Name=data["Name"],
            Emailid=data["Emailid"],
            DOB=data["DOB"],
            Category=data["Category"],
            Mobile =data["Mobile"],
            Altmobile=data["Altmobile"],
            Address =data["Address"],
            FatherName =data["FatherName"],
            Foccupation =data["Foccupation"],
            Mothersname=data["Mothersname"],
            Moccupation=data["Moccupation"],
            City=data["City"],
            State=data["State"],
            Password=data["Password"],
            confirmPassword=data["ConfirmPassword"],
            Image=request.FILES.get("Image"),
            Branch=data["Branch"],
            Resume=request.FILES.get("Resume"),
            Zip=data["Zip"],
            SSCName=data["SSCName"],
            BoardName1=data["BoardName1"],
            Branch1=data["Branch1"],
            Percentage1=data["Percentage1"],
            YOP1=data["YOP1"],
            HSCName=data["HSCName"],
            BoardName2=data["BoardName2"],
            Branch2=data["Branch2"],
            Percentage2=data["Percentage2"],
            YOP2=data["YOP2"],
            CollegeName1=data["CollegeName1"],
            UniversityName1=data["UniversityName1"],
            DegreeName1=data["DegreeName1"],
            Percentage3=data["Percentage3"],
            YOP3=data["YOP3"],
            DegreeName2=data["DegreeName2"],
            UniversityName2=data["UniversityName2"],
            CollegeName2=data["CollegeName2"],
            percentage4=data["Percentage4"],
            YOP4=data["YOP4"],
            AOI=data["AOI"],
            AOS=data["AOS"],
            Cert=data["Cert"],
            Hobbies=data["Hobbies"],
            SpecialA=data["SpecialA"],
            ECA=data["ECA"],
            UpdateTime=datetime.now()
            ) 
        r.save()
        flag=True
        try:
            flag=True
            # r.save()
        except Exception as e:
            flag=False
            print(e)
        
        if flag:
            # registration successful zala
            # put some message like congrats wagere as u like 
            return redirect("login")
        else:
            return redirect("register")
            # or 
            # return render(request, "register.html")
    
def login(request):
    if request.method=="POST":
        u=None
        eml=request.POST['email']
        pas=request.POST['password']
        u=Register.objects.filter(Emailid=eml, Password=pas).first()
        if u:
            request.session['user_name']=u.Name
            print(u.Name)
            request.session['user_email']=u.Emailid
            messages.add_message(request, messages.SUCCESS,"")
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR,"Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")

def logout(request):
    if request.method=="GET":
        request.session.clear()
    return redirect("/")