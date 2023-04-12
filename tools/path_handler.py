import os

base_path=os.path.dirname(os.path.dirname(__file__))
#用例路径
test_datapath=os.path.join(base_path,"test_datas","test_data.xlsx")

#上传图片路径
upload_img=os.path.join(base_path,"test_datas","uploadimg.jpg")

report_url=os.path.join(base_path,"reports")