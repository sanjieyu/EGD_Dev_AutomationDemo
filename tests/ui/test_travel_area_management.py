# Author:Yi Sun(Tim) 2024-5-20

'''Test Travel Area Management Page'''

import unittest
from selenium import webdriver
from utils.read_config import *
from pages.travel_area_management import *

class TravelArea_UI_Test(unittest.TestCase,Travel_Area_Management):
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
        cls.go_travel_management = Travel_Area_Management(cls.driver)
        cls.go_travel_management.go_travel_area_management()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_travel_management_ui_001(self):
        '''Verify the url of Travel Area Management Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual( 'http://aabb/Manage/TravelAreaManagement',self.check_travel_area_url)

    def test_travel_management_ui_002(self):
        '''Verify the title of Travel Area Management Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual( 'Travel Areas - Postal Codes',self.check_travel_area_title)

    def test_travel_management_ui_003(self):
        '''Verify the New button'''
        self.driver.implicitly_wait(2)
        self.assertEqual( True,self.check_new_button)

    def test_travel_management_ui_004(self):
        '''Verify the Search Box'''
        self.driver.implicitly_wait(2)
        self.assertEqual( True,self.check_search_box)
    def test_travel_management_ui_005(self):
        '''Verify the Search Box Function'''
        self.driver.implicitly_wait(2)
        self.assertEqual( 'Nanjing',self.check_search_result)

    def test_travel_management_ui_006(self):
            '''Verify the New screen'''
            self.driver.implicitly_wait(2)
            self.assertEqual( 'Add New Area',self.check_new_screen)

    def test_travel_management_ui_007(self):
            '''Verify each input in the Add New Area screen'''
            self.driver.implicitly_wait(2)
            self.assertEqual( ('Postcode :','Suburb:','State :','Comment :','Category :','Delivery Category :'),
                              self.check_new_screen_input)

    def test_travel_management_ui_008(self):
        '''Verify Save in the Add New Area screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual( True,self.check_new_save_btn)

    def test_travel_management_ui_009(self):
        '''Verify Close in the Add New Area screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual( True,self.check_new_close_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)