#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.mail import send_mail
from web.models import Dreamreal
from web.forms import LoginForm
from web.forms import ProfileForm
from web.forms import AddForm
from web.models import Profile
import json
import datetime
from web.forms import DreamrealForm

def Login(request):
    if request.method == "GET":
        result = {} # 先指定一个字典
        username = request.GET.get('username')
        mobile = request.GET.get('mobile')
        date = request.GET.get('date')
        result['user'] = username
        result['mobileNum'] = mobile
        result['date'] = date
        result = json.dumps(result)
        # 指定返回数据类型为json且编码为utf-8
        return HttpResponse(result, content_type='application/json;charset=utf-8')


def hello(request):
    today = datetime.datetime.now()

    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})


def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)


def viewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)


def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)


def login(request):
   username = "not logged in"

   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()

   return render(request, 'loggedin.html', {"username" : username})

def SaveProfile(request):
   saved = False

   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)

      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = ProfileForm()

   return render(request, 'saved.html', locals())


def index(request):
    return render(request, 'index.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))

def index(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
