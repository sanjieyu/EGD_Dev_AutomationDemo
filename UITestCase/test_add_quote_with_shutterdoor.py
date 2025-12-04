# Author:Yi Sun(Tim) 2025-3-27

'''Test Add a Quote with a Shutter door function'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_quote_with_shutterdoor import *
from CommonModule.read_config import *

class AddQuoteWithShutterDoor_UI_Test(unittest.TestCase,Add_Quote_With_ShutterDoor):
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
        cls.addquote_with_shutter_door = Add_Quote_With_ShutterDoor(cls.driver)
        cls.addquote_with_shutter_door.add_shutter_door_fun()
        cls.addquote_with_shutter_door.get_proposal_number
        cls.addquote_with_shutter_door.search_new_quote()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_addquote_withshutterdoor_fun_001(self):
        '''Verify  Add a Quote with a Shutter door function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door 1(A1)','Quote'),self.verify_new_quote)


if __name__ == '__main__':
    unittest.main(verbosity=2)