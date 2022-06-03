"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from project url you are directed here 
urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    # do not put /register won't work
    path('register', views.register, name="register"),
    path('logout',views.logout, name='logout'),
    path('extra',views.extra, name='extra'),
    path('careerchoice',views.careerchoice, name='careerchoice'),
    path('student',views.student, name='student'),
    path('register',views.register, name='register'),
    path('test',views.test, name='test'),
    path('adminlogin',views.adminlogin, name='adminlogin'),
    path('base',views.base, name='base'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('timer',views.timer, name='timer'),
    path('feedback',views.feedback, name='feedback'),
    path('job',views.job, name='job'),
    path('job_listing',views.job_listing, name='job_listing'),
    path('jobcategory',views.jobcategory, name='jobcategory'),
    path('addstream',views.addstream, name='addstream'),
    path('adminfeedback',views.adminfeedback, name='adminfeedback'),
    path('report',views.report, name='report'),
    path('adminapply',views.adminapply, name='adminapply'),
    path('arts',views.arts, name='arts'),
    path('updatestream',views.updatestream, name='updatestream'),
    path('deletestream',views.deletestream, name='deletestream'),
    path('science',views.science, name='science'),
    path('Graduates',views.Graduates, name='Graduates'),
    path('commerse',views.commerse, name='commerse'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)