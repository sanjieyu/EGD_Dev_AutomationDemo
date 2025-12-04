# Author:Yi Sun(Tim) 2023-10-26

'''Test Add a Standard Door Functian'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_standar_door import *
from CommonModule.read_config import *

class Add_StandardDoor_Fun_Test(unittest.TestCase,Add_Standard_Door):
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
        cls.gostandarddoor = Standard_Door(cls.driver)
        cls.gostandarddoor.go_addstandarddoor()
        cls.addstandarddoor = Add_Standard_Door(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_standarddoor_fun_001(self):
        '''Verify the input validation when add a new door'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Errors\nDoor type is required\nDoor design is required\nDoor finish is required\n'
                          'Door color is required\nPackaging Type must be selected.\nIf SR (left) is less than 89mm, '
                          'LH Jamb should be minimum 90mm.\nIf SR (right) is less than 89mm, RH Jamb should be minimum '
                          '90mm.'), self.validation_input)

    def test_add_standarddoor_fun_002(self):
        '''Verify the add door function'''
        self.driver.implicitly_wait(2)
        self.addstandarddoor.add_door()
        self.addstandarddoor.new_added_door
        self.assertEqual(('1   Panel Lift-Safe, Classic panel, Woodgrain Texture, Monument (2010 x 2560)'),
                         self.new_added_door)

    def test_add_standarddoor_fun_003(self):
        '''Verify the duplicate button for the new added door'''
        self.driver.implicitly_wait(2)
        # self.addstandarddoor.add_door
        # self.addstandarddoor.new_added_door
        self.assertEqual(True, self.duplicate_btn)

    def test_add_standarddoor_fun_004(self):
            '''Verify the delete button for the new added door'''
            self.driver.implicitly_wait(2)
            # self.addstandarddoor.add_door
            # self.addstandarddoor.new_added_door
            self.assertEqual(True, self.delete_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)