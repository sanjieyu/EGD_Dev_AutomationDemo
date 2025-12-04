# Author:Yi Sun(Tim) 2025-4-14

'''Test the Discount function'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.discount_check import *

class Discount_Check_Test(unittest.TestCase,Discount):
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
        cls.discount = Discount(cls.driver)
        cls.discount.add_panellift_door()
        cls.proposal_num = cls.discount.proposal_number


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_discount_ui_001(self):
        '''Verify the door price discount"'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Total Discount Amount: $35.70',self.discount.discount_panellift)

if __name__ == "__main__":
    unittest.main(verbosity=2)