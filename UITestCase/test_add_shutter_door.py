# Author:Yi Sun(Tim) 2025-3-26

'''Test Add a Shutter Door Functian'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_shutter_door import *
from CommonModule.read_config import *

class Add_ShutterDoor_Fun_Test(unittest.TestCase,Add_Shutter_Door):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read =ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.goaddquote = Add_Quote(cls.driver)
        cls.goaddquote.go_addquote()
        cls.goshutterdoor = Shutter_Door(cls.driver)
        cls.goshutterdoor.go_add_shutter_door()
        cls.addshutterdoor = Add_Shutter_Door(cls.driver)
        # cls.addstandarddoor.add_door
        # cls.addstandarddoor.new_added_door

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_shutterdoor_fun_001(self):
        '''Verify the input validation when add a new door'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Errors\nInstall Type is required\nPlease select windlock Track\nMotors field is required'),
                         self.validation_input)

    def test_add_shutterdoor_fun_002(self):
        '''Verify the add door function'''
        self.driver.implicitly_wait(2)
        self.addshutterdoor.add_shutter_detail()
        self.addshutterdoor.new_added_shutterdoor
        self.assertEqual(('Shutter Door (4010 x 5176)'), self.new_added_shutterdoor)

    def test_add_shutterdoor_fun_003(self):
        '''Verify the duplicate button for the new added door'''
        self.driver.implicitly_wait(2)
        # self.addshutterdoor.add_shutter_detail
        # self.addshutterdoor.new_added_door
        self.assertEqual(True, self.duplicate_btn)

    def test_add_shutterdoor_fun_004(self):
            '''Verify the delete button for the new added door'''
            self.driver.implicitly_wait(2)
            # self.addshutterdoor.add_shutter_detail
            # self.addshutterdoor.new_added_door
            self.assertEqual(True, self.delete_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)