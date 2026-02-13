# Author:Yi Sun(Tim) 2025-1-24

'''Test Add a Dealer Panellift Door Functian'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_dealer_panellift_door import *
from utils.read_config import *

class Add_Dealer_PanelDoor_Fun_Test(unittest.TestCase,Add_DP_PanelLift):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read =ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.dealer_username = cls.config_read.dealer_username()
        cls.dealer_password = cls.config_read.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_username,cls.dealer_password)
        cls.driver.implicitly_wait(5)
        cls.goaddquote = Add_Dealer_Quote(cls.driver)
        cls.goaddquote.creat_quote()
        cls.gopaneldoor = Dealer_Panel_Door(cls.driver)
        cls.gopaneldoor.go_panel_door()
        cls.addpaneldoor = Add_DP_PanelLift(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_dealer_panellift_door_fun_001(self):
        '''Verify the input validation when add a new door'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Errors\nDoor design is required\nDoor finish is required\nDoor color is required'),
                         self.validation_input)

    def test_add_dealer_panellift_door_fun_002(self):
        '''Verify the add door function'''
        self.driver.implicitly_wait(2)
        self.addpaneldoor.add_dealer_panel_door()
        self.addpaneldoor.new_added_door
        self.assertEqual(('Panel Lift-Safe, Classic panel, Woodgrain Texture, Monument (2200 x 3000)'),
                         self.new_added_door)

    def test_add_dealer_panellift_door_fun_003(self):
        '''Verify the duplicate button for the new added door'''
        self.driver.implicitly_wait(2)
        # self.addpaneldoor.add_dealer_panel_door
        # self.addpaneldoor.new_added_door
        self.assertEqual(True, self.duplicate_btn)

    def test_add_dealer_panellift_door_fun_004(self):
            '''Verify the delete button for the new added door'''
            self.driver.implicitly_wait(2)
            # self.addpaneldoor.add_dealer_panel_door
            # self.addpaneldoor.new_added_door
            self.assertEqual(True, self.delete_btn)


if __name__ == '__main__':
    unittest.main(verbosity=2)