# Author:Yi Sun(Tim) 2023-8-29

'''Test Admin Page'''

import unittest
from selenium import webdriver
from time import *
from UIModule.admin_portal import *
from CommonModule.read_config import *

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
        self.assertEqual('http://aabb',self.getURL)

    def test_adminportal_ui_002(self):
        '''Verify the default Sections in Admin login Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('ADD','LIST','ACCOUNT'),self.check_defaultmenu)

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
        self.assertEqual(('Quote','Lead','Account Customer','Installer'),self.add_menu)
    def test_adminportal_ui_007(self):
        '''Verify the List Menu'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quotes','Services                    »','Account Customers','Reports','Installers',
                          'MYOB','Job Accepted Doors','On-Hold Doors','New Order','Production','Production – WA',
                          'Schedule','Pipeline','Active Pipeline'),self.list_menu)

    def test_adminportal_ui_008(self):
        '''Verify the Account Menu'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Change my password','Update my profile','Update my email settings',
                          'Users Management','Travel Area Management','Rolling Cycle Management     »',
                          'SMS Notifications','Log off'),self.account_menu)

    def test_adminportal_ui_009(self):
        '''Verify the Copyright and Terms'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('© 2025 - EcoGarageDoors','Terms and Policies'),self.check_copyright)

if __name__ == '__main__':
    unittest.main(verbosity=2)