# Author:Yi Sun(Tim) 2024-8-29

'''Test Add a Roller Door Functian'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_roller_door import *
from utils.read_config import *

class Add_RollerDoor_Fun_Test(unittest.TestCase,Add_Roller_Door):
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
        cls.addrollerdoor = Add_Roller_Door(cls.driver)
        # cls.addstandarddoor.add_door
        # cls.addstandarddoor.new_added_door

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_rollerdoor_fun_001(self):
        '''Verify the add roller door function'''
        self.driver.implicitly_wait(2)
        self.addrollerdoor.add_roller_door()
        self.addrollerdoor.new_added_door
        self.assertEqual(('1   ExoRoll, ExoRoll eC, Smooth Texture, Monument (3100 x 2570)'), self.new_added_door)

    def test_add_rollerdoor_fun_002(self):
        '''Verify the duplicate button for the new added roller door'''
        self.driver.implicitly_wait(2)
        # self.addstandarddoor.add_door
        # self.addstandarddoor.new_added_door
        self.assertEqual(True, self.duplicate_btn)

    def test_add_rollerdoor_fun_003(self):
            '''Verify the delete button for the new added roller door'''
            self.driver.implicitly_wait(2)
            # self.addstandarddoor.add_door
            # self.addstandarddoor.new_added_door
            self.assertEqual(True, self.delete_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)