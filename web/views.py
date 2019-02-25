#-*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.getcwd() + '/chinese_ocr')
import urllib.request
import urllib.parse
import json
import time
from web.invoice_tool import invoice_rec
import chinese_ocr
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from web.models import User, Invoice, Statistics
from django.core import serializers

# with open('1.jpg', 'rb') as f:  # 以二进制读取本地图片
#     data = f.read()
#     encodestr = str(base64.b64encode(data),'utf-8')

#请求头
headers = {
         'Authorization': '367503ca0d38462c93ad694cf9ef9162',
         'Content-Type': 'application/json; charset=UTF-8'
    }

def posturl(url,data={}):
  try:
    params = json.dumps(dict).encode(encoding='UTF8')
    req = urllib.request.Request(url, params, headers)
    r = urllib.request.urlopen(req)
    html = r.read()
    r.close()
    return html.decode("utf8")
  except urllib.error.HTTPError as e:
      print(e.code)
      print(e.read().decode("utf8"))
  time.sleep(1)

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
        # json_data = json.load(request)
        # user = json_data['user_id']
        # password = json_data['password']
        # phone = json_data['phone']
        user = request.POST.get('user_id')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        check1 = User.objects.filter(user_id=user)
        check2 = User.objects.filter(user_phone=phone)
        if check1:
            result = {"success": False, "mes":"该用户名已被注册"}
            return JsonResponse(result)
        elif check2:
            result = {"success": False, "mes": "该手机号已被注册"}
            return JsonResponse(result)
        else:
            new_user = User(
                user_id=user,
                user_password=password,
                user_phone=phone
            )
            new_user.save()
            result = {"success": True, "mes": "注册成功"}
            return JsonResponse(result)
    return render(request, "index.html")

#登陆（id登陆成功的时候将user写入浏览器cookie）
def loginid(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        password = request.POST.get('password')
        #与数据库内比较
        check = User.objects.filter(user_id=user, user_password=password)
        if check:
            img = User.objects.get(user_id=user).user_img
            id = User.objects.get(user_id=user).user_id
            result = {"success": True, "user_img": "lch"}
            response = JsonResponse(result)
            response.set_cookie("user", id, 604800)
            return response
        else:
            result = {"success": False}
            return JsonResponse(result)

#登陆（phone）
def loginphone(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        #与数据库内比较
        check = User.objects.filter(user_phone=phone, user_password=password)
        if check:
            img = User.objects.get(user_phone=phone).user_img
            id = User.objects.get(user_phone=phone).user_id
            print(str(img))
            result = {"success": True, "user_img": str(img)}
            response = JsonResponse(result, safe=False)
            response.set_cookie("user", id, 604800)
            return response

        else:
            check2 = User.objects.filter(user_phone=phone)
            if check2:
                result = {"success": False, "mes": "密码错误"}
                return JsonResponse(result)
            else:
                result = {"success": False, "mes": "不存在该账号"}
                return JsonResponse(result)

#判断登陆
def iflogged(request):
    cookies = request.COOKIES.get('user')
    check = User.objects.filter(user_id=cookies)
    if check:
        result = {"success": True, "user_id": cookies, "img_path": str(User.objects.get(user_id=cookies).user_img),
                  "number": Statistics.objects.get(sta_user_id=cookies).sta_num}
        return JsonResponse(result)
    else:
        result = {"success": False}
        return JsonResponse(result)

#上传头像
def upload_avatar(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        a = User.objects.filter(user_id=user)
        a.user_img = request.FILES.get('user_img')
        a.save()
        result = {"success": True}
        return JsonResponse(result)

#退出登陆
def logout(request):
    if request.method == 'POST':
        cookies = request.COOKIES.get('user')
        check = User.objects.filter(user_id=cookies)
        if check:
            result = {"flag" : 1,"mes": "退出成功"}
            response = JsonResponse(result)
            response.delete_cookie('user')
            return response
        else:
            result = {"flag" : 2,"mes": "请先登陆再退出"}
            return JsonResponse(result)

#获取用户统计信息
def getSta(request):
    if request.method == 'POST':
        user = request.POST.get('user_id')
        check = Statistics.objects.filter(sta_user_id=user)
        if check:
            num = Statistics.objects.get(sta_user_id=user).sta_num
            total = Statistics.objects.get(sta_user_id=user).sta_total_money
            average = Statistics.objects.get(sta_user_id=user).sta_average_money
            result = {"flag": 1, "number": num, "total": total, "average": average}
            return JsonResponse(result)
        else:
            result = {"flag": 2, "mes": "你还没有上传过任何发票"}
            return JsonResponse(result)

# 二维码识别
def QRCodeRecognise(id, inv_img):
    os.system('/root/lrl/main' + ' /root/yk/static/media/' + str(inv_img) + ' /root/lrl/result.txt')
    f = open('/root/lrl/result.txt')
    line = f.readline()
    list = []
    while line:
        print(line, end='')
        list.append(line.strip('\n'))
        line = f.readline()
    f.close()
    print(list)
    if len(list) == 4:
        Invoice.objects.filter(id=id).update(
            inv_numd=list[0],
            inv_numh=list[1],
            inv_money=list[2],
            inv_date=list[3]
        )
        print("二维码识别成功！")
        return True
    else:
        Invoice.objects.filter(id=id).delete()
        print("二维码识别失败！")
        return False

# 发票识别
def InvoiceRecognize(id, inv_img):
    dict = invoice_rec('/root/yk/static/media/' + str(inv_img))
    print(dict)
    if len(dict) == 16:
        Invoice.objects.filter(id=id).update(
            inv_numd=dict['发票代码'],
            inv_numh=dict['发票号码'],
            inv_money=dict['发票金额'],
            inv_date=dict['开票日期']
        )
        print('发票识别成功！')
        return True
    else:
        Invoice.objects.filter(id=id).delete()
        print('发票识别失败！')
        return False

# 6.上传发票图片(并进行识别)
def uploadInvoicePic(request):
    if request.method == 'POST':
        cookies = request.COOKIES.get('user')
        check = User.objects.filter(user_id=cookies)
        if True:
            user_id = request.POST.get('user_id')
            inv_img = request.FILES.get('inv_img')
            new_Invoice = Invoice(
                user_id=user_id,
                inv_img=inv_img,
                inv_money=0
            )
            new_Invoice.save()

            # 二维码识别
            flag = QRCodeRecognise(new_Invoice.id, new_Invoice.inv_img)
            if flag == False:
                # 发票识别
                flag = InvoiceRecognize(new_Invoice.id, new_Invoice.inv_img)

            Sta_check = Statistics.objects.filter(sta_user_id=user_id)
            if Sta_check:
                num = Statistics.objects.get(sta_user_id=user_id).sta_num + 1
                total_money = Statistics.objects.get(sta_user_id=user_id).sta_total_money
                Statistics.objects.filter(sta_user_id=user_id).update(sta_num= num)
                # 修改total_money
                money = Invoice.objects.get(id=new_Invoice.id).inv_money # 新上传发票的金额
                new_total_money = total_money + money  # 新的总额
                Statistics.objects.filter(sta_user_id=user_id).update(sta_total_money=new_total_money)
                Statistics.objects.filter(sta_user_id=user_id).update(sta_average_money=new_total_money/num)

                # Sta_check.num += 1
                # Sta_check.sta_total_money += new_Invoice.inv_money
                # Sta_check.sta_average_money = Sta_check.sta_total_money/Sta_check.num
            else:
                new_Sta = Statistics(
                    sta_user_id=user_id,
                    sta_num=1,
                    sta_total_money=Invoice.objects.get(id=new_Invoice.id).inv_money,
                    sta_average_money=Invoice.objects.get(id=new_Invoice.id).inv_money
                )
                new_Sta.save()
            if flag:
                result = {"success": True, "mes": "添加成功！", "inv_img": str(new_Invoice.inv_img),
                          "id": str(new_Invoice.id)}
                return JsonResponse(result)
            else:
                result = {"success": False, "mes": "无法读取文件！"}
                return JsonResponse(result)
        else:
            result = {"flag": 2, "mes": "cookie失效"}
            return JsonResponse(result)

# 7.修改发票代码
def modifyInvoiceCode(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        inv_numd = request.POST.get('inv_numd')
        judge = Invoice.objects.filter(id=id).update(inv_numd=inv_numd)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 8.修改发票号码
def modifyInvoiceType(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        inv_numh = request.POST.get('inv_numh')
        judge = Invoice.objects.filter(id=id).update(inv_numh=inv_numh)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 9. 修改发票金额
def modifyInvoiceNum(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        inv_money = request.POST.get('inv_money')
        old_money = Invoice.objects.get(id=id).inv_money
        judge = Invoice.objects.filter(id=id).update(inv_money=inv_money)
        if judge:
            user_id = Invoice.objects.get(id=id).user_id
            total_money = Statistics.objects.get(sta_user_id=user_id).sta_total_money
            result = total_money - old_money + Invoice.objects.get(id=id).inv_money
            Statistics.objects.filter(sta_user_id=user_id).update(sta_total_money = result)
            new_total_money = Statistics.objects.get(sta_user_id=user_id).sta_total_money
            num = Statistics.objects.get(sta_user_id=user_id).sta_num
            Statistics.objects.filter(sta_user_id=user_id).update(sta_average_money = new_total_money/num)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 10. 修改发票日期
def modifyInvoiceDate(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        inv_date = request.POST.get('inv_date')
        judge = Invoice.objects.filter(id=id).update(inv_date=inv_date)
        result = jsonResponse(judge, 2)
        return JsonResponse(result)

# 11.查看用户所有上传发票图片(信息)
def retrieveInvoicePic(request):
    if request.method == 'POST':
        cookies = request.COOKIES.get('user')
        check = User.objects.filter(user_id=cookies)
        if check:
            new_imgs = serializers.serialize("json", Invoice.objects.filter(user_id=cookies).order_by("id"))  # 从数据库中取出所有的图片路径
            result = jsonResponse(True, 3)
            result.update({'new_imgs': new_imgs})
            return JsonResponse(result)
        else:
            result = {"flag": 2, "mes": "cookie失效"}
            return JsonResponse(result)

# 12.删除发票(删除某一指定发票代码的发票信息)
def deleteInvoice(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        inv_money = Invoice.objects.get(id=id).inv_money
        # 更新statistics
        user_id = Invoice.objects.get(id=id).user_id
        total_money = Statistics.objects.get(sta_user_id=user_id).sta_total_money
        Statistics.objects.filter(sta_user_id=user_id).update(sta_total_money=total_money - inv_money)
        new_total_money = Statistics.objects.get(sta_user_id=user_id).sta_total_money
        num = Statistics.objects.get(sta_user_id=user_id).sta_num - 1
        if num!=0:
            Statistics.objects.filter(sta_user_id=user_id).update(sta_average_money=new_total_money / num)
        else:
            Statistics.objects.filter(sta_user_id=user_id).update(sta_average_money=0)
        Statistics.objects.filter(sta_user_id=user_id).update(sta_num= num)

        judge = Invoice.objects.filter(id=id).delete()
        if judge:
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


