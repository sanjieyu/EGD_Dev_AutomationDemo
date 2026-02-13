# Author:Yi Sun(Tim) 2023-8-20

'''API Testing for Sales Module'''

import requests
import json
import unittest
from utils.read_excel_title import *
from requests.sessions import Session


class TestSalesAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.excel_reader = ExcelData()
        cls.data = cls.excel_reader.read_excel()
        cls.session = Session()

        cls.base_header = {
            "User-Agent": "Mozilla/5.0...",
            "Host": "test"
        }

        login_url = cls.data[0]['Endpoint']
        login_payload = {
            "Email": "test_user",
            "Password": "test_password",
            "RememberMe": "false"
        }

        response = cls.session.post(
            url=login_url,
            headers=cls.base_header,
            data=login_payload
        )

        if response.status_code != 200:
            raise Exception(f"Login failed! Status code: {response.status_code}")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    def test_sales001(self):
        '''Verify the status code for the specified quote'''
        row_data = self.data[1]
        response = self.session.request(
            method=row_data['method'],
            url=row_data['Endpoint']
        )
        self.assertEqual(int(row_data['return code']), response.status_code)

    def test_sales002(self):
        '''Returns an array of doors data for the specified quote'''
        row_data = self.data[2]
        response = self.session.request(
            method=row_data['method'],
            url=row_data['Endpoint']
        )
        self.assertIn(row_data['response'], response.text)

    def test_sales003(self):
        '''verify the status code for Returns data for one specified door'''
        row_data = self.data[3]
        response = self.session.request(
            method=row_data['method'],
            url=row_data['Endpoint']
        )
        self.assertEqual(int(row_data['return code']), response.status_code)

    def test_sales004(self):
        '''verify the Returns data for one specified door'''
        row_data = self.data[4]
        response = self.session.request(
            method=row_data['method'],
            url=row_data['Endpoint'],
            data=row_data['payload']
        )
        self.assertIn(row_data['response'], response.text)

    def test_sales005(self):
        '''verify the status code for Updates Height of one specific door'''
        row_data = self.data[5]
        response = self.session.request(
            method=row_data['method'],
            url=row_data['Endpoint'],
            data=row_data['payload']
        )
        self.assertEqual(int(row_data['return code']), response.status_code)

    def test_sales006(self):
        '''verify the sUpdates Height of one specific door'''
        row_data = self.data[6]
        response = self.session.request(
            method=row_data['method'],
            url=row_data['Endpoint'],
            data=row_data['payload']
        )
        self.assertIn(row_data['response'], response.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)