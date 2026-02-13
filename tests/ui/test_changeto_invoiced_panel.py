# Author:Yi Sun(Tim) 2025-9-9

'''Test Change Quote Status to Invoiced for Panel lift doors'''

import unittest
from selenium import webdriver
from utils.read_config import *
from pages.changeto_invoiced_panel import *

class ChangeTo_Invoiced_Panel_Test(unittest.TestCase,Change_Invoiced_Panellift):

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
        cls.login.login(cls.admin_username, cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.change_status = Change_Invoiced_Panellift(cls.driver)
        cls.change_status.change_status_myobready()
        cls.change_status.change_status_invoiced()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_invoiced_panellift_ui_001(self):
        '''Verify the status change function, change a Panel Lift door status to "Invoiced"'''
        self.driver.implicitly_wait(2)
        result = self.change_status.check_invoiced_status()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main(verbosity=2)

