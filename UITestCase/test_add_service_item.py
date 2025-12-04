# Author:Yi Sun(Tim) 2023-11-27

'''Test Add Serivce Item Page'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_service_item import *
from CommonModule.read_config import *

class AddServiceItem_UI_Test(unittest.TestCase,Add_Service_Item):
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
        cls.goadditem = Add_Service_Item(cls.driver)
        cls.goadditem.go_service_item()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_additem_ui_001(self):
        '''Verify the title for Add Service Item page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Select Service Items',self.check_add_item_title)

    def test_additem_ui_002(self):
        '''Verify each section in Add Service Item page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('View more','Service Type'),self.check_item_sections)
    def test_additem_ui_003(self):
        '''Verify Item Select button in Add Service Item page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_item_select_btn)

    def test_additem_ui_004(self):
            '''Verify Close button in Add Service Item page'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.check_item_close_btn)

    def test_additem_ui_005(self):
        '''Verify Search button in Add Service Item page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_search_item_box)
    def test_additem_ui_006(self):
        '''Verify new addes service itme in Add Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('S-Res-ST', self.add_item_success)

if __name__ == '__main__':
    unittest.main(verbosity=2)