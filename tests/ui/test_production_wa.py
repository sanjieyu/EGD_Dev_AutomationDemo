# Author:Yi Sun(Tim) 2025-10-14

'''Test Production WA Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.production_wa import *
from utils.read_config import *

class Production_WA_UI_Test(unittest.TestCase,Production_WA):
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
        cls.goproduction_wa = Production_WA(cls.driver)
        cls.goproduction_wa.go_production_wa()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_production_wa_ui_001(self):
        '''Verify the url for Production WA page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Production/WA',self.check_production_wa_url)

    def test_production_wa_ui_002(self):
        '''Verify the title for Production WA page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Production Details – WA',self.check_production_wa_title)

    def test_production_wa_ui_003(self):
        '''Verify each section in Production WA page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('OptiRoll','OptiLift'),self.check_production_wa_section)


if __name__ == '__main__':
    unittest.main(verbosity=2)