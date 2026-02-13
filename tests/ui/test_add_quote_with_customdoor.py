# Author:Yi Sun(Tim) 2025-5-01

'''Test Add a Quote with a Custom door function'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_quote_with_custom_door import *
from utils.read_config import *

class AddQuoteWithCustomDoor_UI_Test(unittest.TestCase,Add_Quote_With_CustomDoor):
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
        cls.addquote_with_custom_door = Add_Quote_With_CustomDoor(cls.driver)
        cls.addquote_with_custom_door.add_custom_door_fun()
        cls.addquote_with_custom_door.get_proposal_number
        cls.addquote_with_custom_door.search_new_quote()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_addquote_withcustomdoor_fun_001(self):
        '''Verify  Add a Quote with a Custom door function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door 1(A1)','Quote'),self.verify_new_quote)


if __name__ == '__main__':
    unittest.main(verbosity=2)