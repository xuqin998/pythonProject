import json
from jsonpath import jsonpath
from tools.params_handler import ParamsHandler



class ExtractdataHandler:
    def extract_data(self,extract:str,respnse:dict):
        if extract:
            extract=extract if isinstance(extract,dict) else json.loads(extract)
            for key,val in extract.items():
                vals=jsonpath(respnse,val)[0]
                setattr(ParamsHandler,key,vals)
        else:
            print("不需提取前置参数")