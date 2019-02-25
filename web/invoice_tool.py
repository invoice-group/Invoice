#python3
#!/usr/bin/
import urllib.request
import urllib.parse
import json
import time
import os
import base64

headers = {
    'Authorization': 'APPCODE 9e488ba37c55408a8e3db9c6603b48ca',
    'Content-Type': 'application/json; charset=UTF-8'
}

def posturl(url,data={}):
  try:
    # params=json.dumps(dict).encode(encoding='UTF8')
    params = json.dumps(data)
    params = params.encode(encoding='UTF8')
    req = urllib.request.Request(url, params, headers)
    r = urllib.request.urlopen(req)
    html =r.read()
    r.close()
    return html.decode("utf8")
  except urllib.error.HTTPError as e:
      print(e.code)
      print(e.read().decode("utf8"))


def invoice_rec(path):
    with open(path, 'rb') as f:  # 以二进制读取本地图片
        data = f.read()
        encodestr = str(base64.b64encode(data), 'utf-8')


    url_request="https://ocrapi-invoice.taobao.com/ocrservice/invoice"
    dict = {'img': encodestr}

    html = posturl(url_request, data=dict)
    dict_all = eval(html)
    dict_res = dict_all['data']
    return dict_res


if __name__ == '__main__':
    # list = os.listdir(r'/root/yk/static/media/inv_img/')
    # print(list)
    print(invoice_rec(r'/root/yk/static/media/inv_img/20190225114139_98.jpg'))