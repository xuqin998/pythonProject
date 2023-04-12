import json
from builtins import str

import jsonpath
import re
import time
import uuid
from tools.params_handler import ParamsHandler

class ReplcaeHandler:

    def replace_data(self,data:str):
        if data is not None:
            list_key=re.findall("#(\w.+)#",data)
            print(f'---------{list_key}',list_key)
            if len(list_key)>0:
                for key in list_key:
                    if key=="time":
                        times=str(int(time.time()*1000))
                        setattr(ParamsHandler,key,times)
                    elif key=="sessionUUID":
                        sessionUUID=str(uuid.uuid4())
                        setattr(ParamsHandler,key,sessionUUID)


                for key in list_key:
                    data=data.replace(f"#{key}#",getattr(ParamsHandler,key))
                return json.loads(data)
            else:
                print("入参无需替换")
                return {}
        else:
            print("接口没有入参，不需替换")
            return {}



if __name__ == '__main__':
    str="#123#569483"
    c=str.replace("#123#","#000#")
    print(c)



