# Author:Yi Sun(Tim) 2023-09-01

'''Test Search Doors Page'''
import time
import unittest
from selenium import webdriver
from time import *
from pages.search_door import *
from utils.read_config import *

class SearchDoors_UI_Test(unittest.TestCase,Search_Door):
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
        cls.gosearchdoors = Search_Door(cls.driver)
        cls.gosearchdoors.go_searchquotes()
        cls.gosearchdoors.go_searchdoors()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_searchdoors_ui_001(self):
        '''Verify the url for Search Doors page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Quote/List',self.check_searchurl)

    def test_searchdoors_ui_002(self):
        '''Verify the title for Search Doors page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Search Quotes',self.check_title)

    def test_searchdoors_ui_003(self):
        '''Verify each section of Doors filter table in Search Doors page''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door Status','Other Parameters'),self.check_section_doors)

    def test_searchdoors_ui_004(self):
        '''Verify each filter in "Door Status changed between" in Doors filter table, should have "Filter Date"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Filter Date'),self.check_door_status)

    def test_searchdoors_ui_005(self):
        '''Verify each filter in "Other Parameters" in Doors filter table, should have "Door Status" and "User" filters'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door Status','User'),self.check_other_para)

    def test_searchdoors_ui_006(self):
        '''Verify the default user name in "User" filter in Doors filter table, should be the current login user'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Yi Sun'),self.check_default_user)


if __name__ == '__main__':
    unittest.main(verbosity=2)