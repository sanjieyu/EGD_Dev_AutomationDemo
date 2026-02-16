# Author:Yi Sun(Tim) 2023-8-29

'''Test Admin Page'''

import unittest
from selenium import webdriver
from time import *
from pages.admin_portal import *
from utils.read_config import *

class Admin_UI_Test(unittest.TestCase,Admin_Page):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip
    def test_adminportal_ui_001(self):
        '''Verify the url of Admin login Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://test_sample',self.getURL)

    def test_adminportal_ui_002(self):
        '''Verify the default Sections in Admin login Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample','test_sample','test_sample'),self.check_defaultmenu)

    def test_adminportal_ui_003(self):
        '''Verify the Find Quote in Admin Login page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_findquote)

    def test_adminportal_ui_004(self):
        '''Verify the Find Address in Admin Login page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_findaddress)

    def test_adminportal_ui_005(self):
        '''Verify the Find Client in Admin Login page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_findclient)

    def test_adminportal_ui_006(self):
        '''Verify the Add Menu'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample','test_sample','test_sample','test_sample'),self.add_menu)
    def test_adminportal_ui_007(self):
        '''Verify the List Menu'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample'),self.list_menu)

    def test_adminportal_ui_008(self):
        '''Verify the Account Menu'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample'),self.account_menu)

    def test_adminportal_ui_009(self):
        '''Verify the Copyright and Terms'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample'),self.check_copyright)

if __name__ == '__main__':
    unittest.main(verbosity=2)