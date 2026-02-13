# Author:Yi Sun(Tim) 2024-5-22

'''Test User Management Page'''

import unittest
from selenium import webdriver
from utils.read_config import *
from pages.user_management import *

class User_Management_Test(unittest.TestCase,User_Management):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.read_config = ReadConfig()
        cls.url = cls.read_config.get_url()
        cls.admin_username = cls.read_config.admin_username()
        cls.admin_password = cls.read_config.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.go_user = User_Management(cls.driver)
        cls.go_user.go_user_management()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    def test_usermanagement_ui_001(self):
        '''Verify the URL'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Manage/UserManagementPanel',self.check_user_url)

    def test_usermanagement_ui_002(self):
        '''Verify the Title'''
        self.driver.implicitly_wait(2)
        self.assertEqual('User Management',self.check_user_title)

    def test_usermanagement_ui_003(self):
        '''Verify the Sections'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Roles Assigned','Registered Users'),self.check_section)

    def test_usermanagement_ui_004(self):
        '''Verify the New button'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_new_button)

    def test_usermanagement_ui_005(self):
        '''Verify the New Add User Screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Add New User','First Name:','Last Name:','Email:'),self.check_add_user)

    @unittest.skip
    def test_usermanagement_ui_006(self):
        '''Verify the validation for adding the duplicate user'''
        self.driver.implicitly_wait(2)
        self.assertIn( "User does not exists in the system.",self.validate_duplicate_user)

if __name__ == '__main__':
    unittest.main(verbosity=2)