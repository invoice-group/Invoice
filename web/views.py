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
        user = request.POST.get('user_id')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        check1 = User.objects.filter(user_id=user)
        check2 = User.objects.filter(user_phone=phone)
        if check1:
            result = {"success":False, "mes":"user_id"}
            JsonResponse(result)
        elif check2:
            result = {"success": False, "mes": "phone"}
            JsonResponse(result)
        else:
            user = User(
                user_id=user,
                user_password=password,
                user_phone=phone
            )
            user.save()
            result = {"success": True, "mes": "注册成功"}
            JsonResponse(result)

#登陆（id登陆成功的时候将user写入浏览器cookie）
def loginid(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        password = request.POST.get('password')
        #与数据库内比较
        check = User.objects.filter(user_id=user, user_password=password)
        if check:
            a = User.objects.get(user_id=user).user_img
            result = {"success" : True , "user_img" : a}
            result.set_cookie('user', user)
            JsonResponse(result)
        else:
            result = {"success": False}
            JsonResponse(result)

#登陆（phone）
def loginphone(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        #与数据库内比较
        check = User.objects.filter(user_phone=phone, user_password=password)
        if check:
            a = User.objects.get(user_phone=phone).user_img
            b = User.objects.get(user_phone=phone).user_id
            result = {"success" : True , "user_img" : a}
            result.set_cookie('user', b)
            JsonResponse(result)
        else:
            result = False
            JsonResponse(result)

#判断登陆
def iflogged(request):
    username = request.COOKIES.get('user')
    if not username:
        result = {"success" : False}
        return JsonResponse(result)
    else:
        result = {"success": True}
        return JsonResponse(result)

#上传头像
def upload_avatar(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        a = User.objects.get(user_id=user)
        a.user_img = request.FILES.get('user_img')
        a.save()
        result = {"success": True}
        JsonResponse(result)

#退出登陆
def logout(request):
    if request.method == 'POST':
        result = "logout"
        result.delete_cookie('user')
        return JsonResponse(result)

#获取用户统计信息
def getSta(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        num = Statistics.objects.get(user).sta_num
        total = Statistics.objects.get(user).sta_total_money
        average = Statistics.objects.get(user).sta_average_money
        result = {"number":num , "total": total, "average" : average}
        JsonResponse(result)

# 6.上传发票图片
def uploadInvoicePic(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        judge = Invoice.objects.filter(user_id=user_id)
        if (judge):
            img_invoice = Invoice(inv_img=request.FILES.get('invoice_img'))
            img_invoice.save()
        result = jsonResponse(judge, 0)
        return JsonResponse(result)

# 7.修改发票代码
def modifyInvoiceCode(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        inv_numh = request.POST.get('inv_numh')
        judge = Invoice.objects.filter(user_id=user_id).update(inv_numh=inv_numh)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 8.修改发票类别
def modifyInvoiceType(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        inv_class = request.POST.get('inv_class')
        judge = Invoice.objects.filter(user_id=user_id).update(inv_class=inv_class)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 9. 修改发票金额
def modifyInvoiceNum(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        inv_money = request.POST.get('inv_money')
        judge = Invoice.objects.filter(user_id=user_id).update(inv_money=inv_money)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 10. 修改发票日期
def modifyInvoiceDate(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        inv_date = request.POST.get('inv_date')
        judge = Invoice.objects.filter(user_id=user_id).update(inv_date=inv_date)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 11.查看用户所有上传发票图片
def retrieveInvoicePic(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        judge = Invoice.objects.filter(user_id=user_id)
        if (judge):
            imgs = Invoice.objects.all()  # 从数据库中取出所有的图片路径
            result = jsonResponse(judge, 3)
            result.update({'invoice_img': imgs})
            return JsonResponse(result)

# 12. 删除某位用户上传的发票图片
def deleteInvoicePic(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        judge = Invoice.objects.filter(user_id=user_id)
        if (judge):
            result = Invoice.inv_img.delete()
            result = jsonResponse(result)
        return JsonResponse(result, 1)

# 13.删除发票(删除某一指定发票代码的发票信息)
def deleteInvoice(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        inv_numh = request.POST.get('inv_numh')
        judge = Invoice.objects.filter(user_id=user_id, inv_numh=inv_numh).delete()
        result = jsonResponse(judge, 1)
        return JsonResponse(result)

# 返回JSON数据，num = {0,1,2,3} == CRUD
def jsonResponse(judge, num):
    if (num == 0):
        if(judge):
            result = {"success": judge, "mes": "添加成功！"}
        else:
            result = {"success": judge, "mes": "添加失败！"}
    elif (num == 1):
        if(judge):
            result = {"success": judge, "mes": "删除成功！"}
        else:
            result = {"success": judge, "mes": "删除失败！"}
    elif (num == 2):
        if(judge):
            result = {"success": judge, "mes": "修改成功！"}
        else:
            result = {"success": judge, "mes": "修改失败！"}
    elif (num == 3):
        if(judge):
            result = {"success": judge, "mes": "查询成功！"}
        else:
            result = {"success": judge, "mes": "查询失败！"}
    else:
        result = {"mes": "CRUD_num error!"}
    return result


