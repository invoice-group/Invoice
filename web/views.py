#-*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, "index.html")

def test(request):
    if(request.method=="POST"):
        dict = {}
        username = request.POST.get('user')
        print(username)
        result = {"success" : "1" , "mes" : "测试成功！!!"}
        return JsonResponse(result)
        #return HttpResponse(json.dump(result))