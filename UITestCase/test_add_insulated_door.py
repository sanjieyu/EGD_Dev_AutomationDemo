# Author:Yi Sun(Tim) 2025-3-31

'''Test Add a Insulated Door Functian'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_insulated_door import *
from CommonModule.read_config import *

class Add_InsulatedDoor_Fun_Test(unittest.TestCase,Add_Insulated_Door):
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
        cls.addinsulateddoor = Add_Insulated_Door(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_insulateddoor_fun_001(self):
        '''Verify the add insulate door function'''
        self.driver.implicitly_wait(2)
        self.addinsulateddoor.add_insulated_door()
        # self.addinsulateddoor.new_added_door
        self.assertEqual(('1   Insulated Sectional, Ribline, Woodgrain Texture, Monument (2010 x 2560)'), self.new_added_door)

    def test_add_insulateddoor_fun_002(self):
        '''Verify the duplicate button for the new added insulate door'''
        self.driver.implicitly_wait(2)
        # self.addstandarddoor.add_door
        # self.addstandarddoor.new_added_door
        self.assertEqual(True, self.duplicate_btn)

    def test_add_insulateddoor_fun_003(self):
            '''Verify the delete button for the new added insulate door'''
            self.driver.implicitly_wait(2)
            # self.addstandarddoor.add_door
            # self.addstandarddoor.new_added_door
            self.assertEqual(True, self.delete_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)