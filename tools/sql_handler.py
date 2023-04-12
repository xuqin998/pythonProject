import pymysql
import re
from tools.params_handler import ParamsHandler

class SqlHandler:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="xuqin1998", database="test")
        self.cursor = self.db.cursor()


    def sql_excute(self,sql:str):
        try:
            if sql is not None:
                sql=self.sql_replace(sql)
                self.cursor.execute(sql)
                data = self.cursor.fetchone()
                print(data)
            else:
                print('无需sqlcheck')
        except Exception as e:
            print(e)
        finally:
            self.close_db()

    def sql_replace(self,sql):
        replace_param=re.findall(r'#(.*?)#',sql)
        if len(replace_param) > 0:
            for key in replace_param:
                get_data=getattr(ParamsHandler,key)
                sql=sql.replace(f'#{key}#',get_data)
        else:
            print('无需替换')
        return sql

    def close_db(self):
        self.cursor.close()
        self.db.close()




