import time
import unittest

import requests
from ddt import ddt,data
from tools.excel_handler import HandlerExcel
from tools.path_handler import test_datapath,report_url,base_path
from tools.replace_handler import ReplcaeHandler
from tools.assert_handler import AssertHandler
from tools.extractdata_handler import ExtractdataHandler
from tools.params_handler import ParamsHandler
from tools.sendrequest_handler import SendRequestHandler
from tools.sql_handler import SqlHandler
from BeautifulReport import BeautifulReport
case_list=HandlerExcel(filename=test_datapath,sheetname="Sheet1").get_data()


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.replace=ReplcaeHandler()
        cls.heanders={"locale":"zh_CN"}
        cls.assert_result=AssertHandler()
        cls.extract=ExtractdataHandler()
        cls.send_request=SendRequestHandler()
        cls.sql_assert=SqlHandler()


    @data(*case_list)
    def test_login(self,case):
        data=self.replace.replace_data(case["data"])
        res=self.send_request.send_request(url=case["url"],method=case["method"],data=data,is_upload=case["is_upload"])
        self.assert_result.assert_result(case["expect_result"],res)
        print(case["sql_check"])
        if case["sql_check"] is not None:
            self.sql_assert.sql_excute(case["sql_check"])

        self.extract.extract_data(case["extract_data"],res)
        print("结束一次")


if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(base_path, pattern='test_*.py')
    now = time.strftime('%Y%m%d%H%M%S')
    BeautifulReport(discover).report(description='用例执行情况', filename='测试报告_' + str(now),
                                     report_dir=report_url)




