import json
import unittest

from jsonpath import jsonpath
from unittest import TestCase

class AssertHandler(unittest.TestCase):
    def resultchange(self,response):
            try:
                if isinstance(response.json(),dict):
                    return {"response":response.json()}
            except Exception as e:
                return {"response": response.text}



    def assert_result(self,expect_result,response):
        if expect_result:
            expect_result=expect_result if isinstance(expect_result,dict) else json.loads(expect_result)
            actual_result={}
            for key in expect_result:
                actual_result[key]=jsonpath(response,f"$..{key}")[0]

            self.assertEqual(actual_result,expect_result)









