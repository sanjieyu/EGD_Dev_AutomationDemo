# Author:Yi Sun(Tim) 2023-11-30

'''Test Add a Service with service items function'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_service_with_item import *
from utils.read_config import *

class AddServiceWithItem_Fun_Test(unittest.TestCase,Add_Service_With_Items):
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
        cls.addservice_with_item = Add_Service_With_Items(cls.driver)
        cls.addservice_with_item.add_service_fun()
        cls.addservice_with_item.get_invoice_no


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_addservice_with_item_fun_001(self):
        '''Verify generate the Service Quote Document function'''
        self.driver.implicitly_wait(2)
        self.assertIn('api_EGD_Dev.xlsx',self.get_service_upload_doc)

    def test_addservice_with_item_fun_002(self):
        '''Verify generate the Service Quote Document function'''
        self.driver.implicitly_wait(2)
        self.assertIn('Service Quote Document',self.get_service_quote_doc)

    def test_addservice_with_item_fun_003(self):
        '''Verify the Quantity amount for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('1',self.check_quantity)

    def test_addservice_with_item_fun_004(self):
        '''Verify the Service Type for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Service Charges',self.check_service_type)

    def test_addservice_with_item_fun_005(self):
        '''Verify the Item name for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('S-Res-ST',self.check_item_name)

    def test_addservice_with_item_fun_006(self):
        '''Verify the Original Price for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('290',self.check_original_price)

    def test_addservice_with_item_fun_007(self):
        '''Verify the Discount for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('90',self.check_discount)

    def test_addservice_with_item_fun_008(self):
        '''Verify the Final Price for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('200',self.check_final_price)

    def test_addservice_with_item_fun_009(self):
        '''Verify the Total Price for the new added item'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Total Price : 200',self.check_total_price)

    def test_addservice_with_item_fun_010(self):
        '''Verify  Add a Service with a service item function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Add_by_Automation'),self.search_new_service)



if __name__ == '__main__':
    unittest.main(verbosity=2)