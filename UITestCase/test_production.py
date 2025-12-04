# Author:Yi Sun(Tim) 2023-11-16

'''Test Production Page'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.production import *
from CommonModule.read_config import *

class Production_UI_Test(unittest.TestCase,Production):
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
        cls.goproduction = Production(cls.driver)
        cls.goproduction.go_production()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_production_ui_001(self):
        '''Verify the url for Production page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Production',self.check_production_url)

    def test_production_ui_002(self):
        '''Verify the title for Production page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Production Details',self.check_production_title)

    def test_production_ui_003(self):
        '''Verify each section in Production page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('ExoRoll Doors','Panel Lift Safe','Insulated Doors','Custom Doors',
                          'Roller Shutters','[OBSOLETE] All Doors'),self.check_production_section)


if __name__ == '__main__':
    unittest.main(verbosity=2)