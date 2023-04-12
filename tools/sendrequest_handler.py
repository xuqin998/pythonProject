import requests
from tools.path_handler import upload_img
from requests_toolbelt import MultipartEncoder
from tools.params_handler import ParamsHandler
from tools.assert_handler import AssertHandler

class SendRequestHandler:
    def __init__(self):
        self.headers={"locale":"zh_CN"}
        self.response=AssertHandler()

    def upload_img(self,url,method):
        try:
            with open(file=upload_img, mode='rb') as file:
                print(upload_img)
                img = file.read()
                data = MultipartEncoder(fields={
                    "file": ("uploadimg.jpg", img, "image/png")
                })
                self.headers["Content-Type"] = data.content_type
                self.headers["Authorization"]=f"bearer{getattr(ParamsHandler,'access_token')}"
                print("=======",self.headers["Content-Type"])
                res = requests.request(url=url, method=method, data=data, headers=self.headers,verify=False)
                print(res.text)
                print(res)
                return res
        except Exception as e:
            print("图片上传错误",e)
            return {}
        finally:
            self.headers["Content-Type"]="application/json;charset=utf-8"

    def send_request(self,url,method,data,is_upload):
        if is_upload==1:
            res=self.upload_img(url=url,method=method)
        else:
            res=requests.request(url=url,method=method,json=data,headers=self.headers)    # post请求
            # res = requests.request(url=url, method=method, params=data, headers=self.headers)   get请求
        res=self.response.resultchange(response=res)
        return res

