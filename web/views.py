#-*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from web.models import User, Invoice, Statistics


def test(request):
    if(request.method=="POST"):
        dict = {}
        user = request.POST.get('user')
        print(user)
        result = {"success" : True , "mes" : "测试成功！"}
        return JsonResponse(result)

    return render(request, "index.html")


#注册
def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        admin = request.POST.get('admin')

        user = User(
            user_id=  user,
            user_password= password,
            user_phone= phone,
            user_admin= admin
        )
        user.save()
        return JsonResponse("注册成功")
#登陆（登陆成功的时候将user写入浏览器cookie）
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        #与数据库内比较
        check = User.objects.filter(user_id=user, user_password=password)
        if check:
            response = True
            response.set_cookie('user', user)
        else:
            response = False


#判断登陆
def iflogged(request):
    username = request.COOKIES.get('user')
    if not username:
        result = {"iflogged" : False}
        return JsonResponse(result)
    else:
        result = {"iflogged": True}
        return JsonResponse(result)

#上传头像
def upload_avatar(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        a = User.objects.get(user_id=user)
        a.user_img = request.FILES.get('img')
        a.save()

#退出登陆
def logout(request):
    response = "logout"
    response.delete_cookie('user')
    return JsonResponse(response)
