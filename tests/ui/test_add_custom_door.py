# Author:Yi Sun(Tim) 2025-4-16

'''Test Add a Custom Door Functian'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_custom_door import *
from utils.read_config import *

class Add_CustomDoor_Fun_Test(unittest.TestCase,Add_Custom_Door):
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
        cls.gocustomdoor = Custom_Door(cls.driver)
        cls.gocustomdoor.go_addcustomdoor()
        cls.addcustomdoor = Add_Custom_Door(cls.driver)
        # cls.addstandarddoor.add_door
        # cls.addstandarddoor.new_added_door

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_customdoor_fun_001(self):
        '''Verify the input validation when add a new door'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Errors\nFor current Headroom height, pelmet is required\nPanels Wide should be selected\n'
                          'If SR (left) is less than 89mm, LH Jamb should be minimum 90mm.\n'
                          'If SR (right) is less than 89mm, RH Jamb should be minimum 90mm.\nMotors field is required'),
                         self.validation_input)

    def test_add_customdoor_fun_002(self):
        '''Verify the add door function'''
        self.driver.implicitly_wait(2)
        self.addcustomdoor.add_custom_detail()
        self.assertEqual(('Custom Door, Residential, OilColour (10 x 60)'), self.new_added_custom_door)
    def test_add_customdoor_fun_003(self):
        '''Verify the duplicate button for the new added door'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.duplicate_btn)

    def test_add_customdoor_fun_004(self):
            '''Verify the delete button for the new added door'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.delete_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)