# Author:Yi Sun(Tim) 2025-04-09

'''Test the wall button logic function'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.wall_button import *
from utils.read_config import *

class WallButton_UI_Test(unittest.TestCase,Wall_Button):
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
        cls.wallbutton = Wall_Button(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_wall_button_fun_001(self):
        '''Verify the default wall button amount for cash sale'''
        self.driver.implicitly_wait(2)
        self.assertEqual('0',self.wallbutton.default_wallbutton_amount)

    def test_wall_button_fun_002(self):
        '''Verify the wall button amount for a Customer which got the 1st wall button free on customer card'''
        self.driver.implicitly_wait(2)
        self.assertEqual('1',self.wallbutton.customer_wallbutton_amount)


if __name__ == '__main__':
    unittest.main(verbosity=2)