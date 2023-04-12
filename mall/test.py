import re

import requests
import time
import uuid
from requests_toolbelt import MultipartEncoder
import jsonpath
import json
import pymysql

time_t=int(time.time()*1000)
sessionUUID=str(uuid.uuid4())


def login():
    data={
        "t":time_t,
        "principal":"student",
        "credentials":"123456a",
        "sessionUUID":sessionUUID,
        "imageCode":"lemon"
    }

    url="http://mall.lemonban.com:8108/adminLogin"

    res=requests.post(url=url,json=data)
    print(res.json())
    return jsonpath.jsonpath(res.json(),"$..'access_token'")

def upload_img():
    token=login()[0]
    print(token)
    url="http://mall.lemonban.com:8108/admin/file/upload/img"
    with open(file="/Users/xuqin/Desktop/test.jpg",mode="rb") as file:
        image=file.read()
        data=MultipartEncoder(fields={
            "file":("test.jpg",image,"image/png")
        })
        head={"locale":"zh_CN"}
        head["Authorization"]=f"bearer{token}"
        head["Content_Type"]=data.content_type
        res=requests.post(url=url,data=data,headers=head)
        print(res.text)
    file.close()



def sqlconnect():
    db = pymysql.connect(host="localhost", user="root", password="xuqin1998", database="test")
    cursor = db.cursor()
    cursor.execute("select * from user where phone='18358349453'")
    data = cursor.fetchone()
    print(data)
    # 关闭数据库连接
    cursor.close()
    db.close()


sqlconnect()

def test():
    sql1='''{
        "t":"#time#",
        "principal":"student",
        "credentials":"123456a",
        "sessionUUID":"#sessionUUID#",
        "imageCode":"lemon"
    }'''
    sql='''select * from #user# where phone="#phone#"'''
    print(type(sql))
    test=re.findall("#(.*?)#",sql)
    for key in test:
        print(key)


