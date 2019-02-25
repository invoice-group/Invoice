#-*- coding:utf-8 -*-
import os
import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob
image_files = glob('./test_images/*.*')

def is_check_dnum(msg):
    msg = msg.replace(' ', '')
    cnt = 0
    
    for c in msg:
        if c >= '0' and c <= '9':
            cnt += 1
        else:
            cnt = 0
    return cnt == 10 or cnt == 12

def get_check_dnum(msg):
    msg = msg.replace(' ', '')
    res = ''
    for c in msg:
        if c >= '0' and c <= '9':
            res += c
    return res


def is_check_num(msg):
    msg = msg.replace(' ', '')
    cnt = 0
    for c in msg:
        if c >= '0' and c <= '9':
            cnt += 1
        else:
            cnt = 0
    return cnt == 8


def get_check_num(msg):
    msg = msg.replace(' ', '')
    res = ''
    for c in msg:
        if c >= '0' and c <= '9':
            res += c
    return res


def is_date(msg):
    msg = msg.replace(' ', '')
    if '年' in msg and '月' in msg and '日' in msg:
        return True
    return False

def get_date(msg):
    msg = msg.replace(' ', '')
    nums = ''
    for c in msg:
        if c >= '0' and c <= '9':
            nums += c
    year = nums[0:4]
    month = nums[4:6]
    day = nums[6:8]
    return year + '年' + month + '月' + day + '日'


def is_money(msg):
    msg = msg.replace(' ', '')
    if '小' in msg and '写' in msg:
        return True
    return False


def get_money(msg):
    res = ''
    flag = 0
    msg = msg.replace(' ', '')
    msg = msg.replace('．', '.')

    for c in msg:
        if (c >= '0' and c <= '9') or c == '.':
            res += c
    return res


def rec_invoice(path, is_tmp=False):
    if is_tmp == True:      # is_temp
        result_dir = './test_result'
        if os.path.exists(result_dir):
            shutil.rmtree(result_dir)
        os.mkdir(result_dir)

    image = np.array(Image.open(path).convert('RGB'))   # read file
    t = time.time()   # time
    result, image_framed = ocr.model(image)  # rec

    if is_tmp == True:      # is_tmp
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        Image.fromarray(image_framed).save(output_file)

    res_dict = {}
    print("Mission complete, it took {:.3f}s".format(time.time() - t))
    # print("\nRecognition Result:\n")
    for key in result:
        # print(result[key][1])
        res_msg = result[key][1]
        if is_check_dnum(res_msg):
            if '发票代码' not in res_dict:
                res_dict['发票代码'] = get_check_dnum(res_msg)
        if is_check_num(res_msg):
            if '发票号码' not in res_dict:
                res_dict['发票号码'] = get_check_num(res_msg)
        if is_date(res_msg):
            if '开票日期' not in res_dict:
                res_dict['开票日期'] = get_date(res_msg)
        if is_money(res_msg):
            if '金额' not in res_dict:
                res_dict['金额'] = get_money(res_msg)
    return res_dict


if __name__ == '__main__':
    print(rec_invoice('/Users/Rubik/Desktop/样本/fp1.png'))



# if __name__ == '__main__':
#     result_dir = './test_result'
#     if os.path.exists(result_dir):
#         shutil.rmtree(result_dir)
#     os.mkdir(result_dir)
#     res_dict = {}
#     for image_file in sorted(image_files):
#         image = np.array(Image.open(image_file).convert('RGB'))
#         t = time.time()
#         result, image_framed = ocr.model(image)
#         output_file = os.path.join(result_dir, image_file.split('/')[-1])
#         Image.fromarray(image_framed).save(output_file)
#         print("Mission complete, it took {:.3f}s".format(time.time() - t))
#         print("\nRecognition Result:\n")
#         for key in result:
#             print(result[key][1])
#             res_msg = result[key][1]
#             if is_check_dnum(res_msg):
#                 if '发票代码' not in res_dict:
#                     res_dict['发票代码'] = get_check_dnum(res_msg)
#             if is_check_num(res_msg):
#                 if '发票号码' not in res_dict:
#                     res_dict['发票号码'] = get_check_num(res_msg)
#             if is_date(res_msg):
#                 if '开票日期' not in res_dict:
#                     res_dict['开票日期'] = get_date(res_msg)
#             if is_money(res_msg):
#                 if '金额' not in res_dict:
#                     res_dict['金额'] = get_money(res_msg)
#     print(res_dict)

