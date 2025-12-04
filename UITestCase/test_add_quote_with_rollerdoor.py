# Author:Yi Sun(Tim) 2024-8-29

'''Test Add a Quote with a Roller door function'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_quote_with_rollerdoor import *
from CommonModule.read_config import *

class AddQuoteWithRollerDoor_UI_Test(unittest.TestCase,Add_Quote_With_RollerDoor):
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
        cls.addquote_with_roller_door = Add_Quote_With_RollerDoor(cls.driver)
        cls.addquote_with_roller_door.add_door_fun()
        cls.addquote_with_roller_door.get_proposal_number
        cls.addquote_with_roller_door.search_new_quote()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_addquote_withrollerdoor_fun_001(self):
        '''Verify  Add a Quote with a standard door function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door 1(A1)','Quote'),self.verify_new_quote)


if __name__ == '__main__':
    unittest.main(verbosity=2)