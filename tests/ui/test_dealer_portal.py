# Author:Yi Sun(Tim) 2024-03-13

'''Test the Dealer Portal Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.dealer_portal import *
from utils.read_config import *

class DealerPortal_UI_Test(unittest.TestCase,Deal_Portal):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.dealer_username = cls.config_read.dealer_username()
        cls.dealer_password = cls.config_read.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_username,cls.dealer_password)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_dealer_portal_ui_001(self):
        self.driver.implicitly_wait(2)
        self.assertEqual("http://aabb/Dealer",self.check_dealer_url)

    def test_dealer_portal_ui_002(self):
        self.driver.implicitly_wait(2)
        self.assertEqual(("Create Quote","Search Quotes","ACCOUNT"),self.check_default_values)

    def test_dealer_portal_ui_003(self):
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_find_dealer_quote)

    def test_dealer_portal_ui_004(self):
        self.driver.implicitly_wait(2)
        self.assertEqual(("aabb","Log off"),self.check_account_menu)


if __name__ == '__main__':
    unittest.main(verbosity=2)
