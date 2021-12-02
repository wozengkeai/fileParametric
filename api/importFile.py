# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/2 20:48
@Auth ： zengxiaoyan
@File ：importFile.py
"""

import os
import random
import string
import requests
dir = 'F:\\testerZ\\fileParametric\\files'
def rename_file() -> str:
    '''
    重命名某个文件
    :return:
    '''
    # 获取现有文件名
    file = os.listdir(dir)
    filename = file[0]
    # 重命名
    tag = ''.join(random.sample(string.digits,3))
    newname = 'A01-CCC-H211202-' + tag + '.xlsx'
    os.rename(dir + '\\'+filename,dir + '\\'+newname)
    # 获取新的文件名
    newfile = os.listdir(dir)
    newfilename = newfile[0]
    print(newfilename)
    return newfilename

def import_file():
    # 上传文件，获取返回的临时文件存储地址
    filename = rename_file()
    fileurl = 'http://sg-storage-dev.fjmaimaimai.com/v1/upload/file'
    fileheader = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Authorization": "Bearer Gu-UaeV5I8JOe_ZOOpT5OWm2p9hCRMPU"
    }
    files = {
        "file": (filename,open(dir+'\\'+filename,'rb'),"form-data")
    }
    response = requests.post(url=fileurl,headers=fileheader,files=files)
    content = response.json()
    path = content['data']['file']['path']
    # 保存上传
    no = filename.split('.',-1)[0]
    print(no)
    importurl = 'http://sg-storage-dev.fjmaimaimai.com/v1/work-orders'
    data = {
        "warehouseNo":"A01",
        "ignoreRow":[],
        "workOrderNo": no,
        "file": path
    }
    import_res = requests.post(url=importurl,headers=fileheader,json=data)
    print(import_res.text)




if __name__ == "__main__":
    for i in range(2):
    #通过循环快速大量上传文件
        import_file()
