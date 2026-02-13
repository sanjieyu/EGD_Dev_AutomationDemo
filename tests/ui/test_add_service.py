# Author:Yi Sun(Tim) 2023-11-13

'''Test Add Serivce Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_service import *
from utils.read_config import *

class AddService_UI_Test(unittest.TestCase,Add_Service):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.goaddservice = Add_Service(cls.driver)
        cls.goaddservice.go_addservice()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_addservice_ui_001(self):
        '''Verify the url for Add Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Service/Create?QuoteId=0',self.check_add_service_url)

    def test_addservice_ui_002(self):
        '''Verify each section in Add Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Doors','Service Details  ','Site Contact Details','Service Items',
                          'Service Documents'),self.check_sections)

    def test_addservice_ui_003(self):
            '''Verify each section in Add Service page'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Back to Services'),self.check_buttons)
    def test_addservice_ui_004(self):
            '''Verify each elements in "Doors" section'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Door Type','Please Select\nCustom Door\nInsulated Sectional\nPanel Lift-Safe\n'
                                          'Roller Door\nSingle Skin Sectional','Additional Door Information'),
                             self.check_doors_section)

    def test_addservice_ui_005(self):
            '''Verify he Additional Door Infomation box in "Doors" section'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True,self.check_addition_box)

    def test_addservice_ui_006(self):
        '''Verify  each elements in "Service Details" section'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Service Type','Service Area','Service Status','Invoice No.',
                          'Account Type','Account Customer','Order Date','Service Date','Customer PO',
                          'User','Service Tech','Service Tech Name','Description'),self.check_service_details)

if __name__ == '__main__':
    unittest.main(verbosity=2)