# Author:Yi Sun(Tim) 2025-9-9

'''Test Change Quote Status to Invoiced for roller doors'''

import unittest
from selenium import webdriver
from utils.read_config import *
from pages.changeto_invoiced_roller import *

class ChangeTo_Invoiced_Roller_Test(unittest.TestCase,Change_Invoiced_Roller):

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
        cls.change_status_roller = Change_Invoiced_Roller(cls.driver)
        cls.change_status_roller.change_status_myobready()
        cls.change_status_roller.change_status_invoiced()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_invoiced_roller_ui_001(self):
        '''Verify the status change function, change a Roller door status to "Invoiced"'''
        self.driver.implicitly_wait(2)
        result = self.change_status_roller.check_invoiced_status()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main(verbosity=2)

