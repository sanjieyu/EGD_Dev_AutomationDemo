# Author:Yi Sun(Tim) 2023-11-02

'''Test Add Custom Door Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.custom_door import *
from utils.read_config import *

class Add_CustomDoor_UI_Test(unittest.TestCase,Custom_Door):
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
        cls.goaddquote = Add_Quote(cls.driver)
        cls.goaddquote.go_addquote()
        cls.gocustomdoor = Custom_Door(cls.driver)
        cls.gocustomdoor.go_addcustomdoor()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_customdoor_ui_001(self):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample'),self.check_customdoor_page)

    def test_add_customdoor_ui_002(self):
        '''Verify each element for install details '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test_sample','test_sample','test_sample','test_sample','test_sample','test_sample',
                          'test_sample','test_sample','test_sample','test_sample','test_sample',
                          'test_sample'),self.check_install_details)
    #
    def test_add_customdoor_ui_003(self):
        '''Verify the Install Type dropdown list '''
        self.driver.implicitly_wait(2)
        self.assertIn(('test_sample\ntest_sample\ntest_sample\ntest_sample\ntest_sample'),
                      self.check_install_type)
    #
    def test_add_customdoor_ui_004(self):
            '''Verify the Design dropdown list'''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'),self.check_design)
    #
    def test_add_customdoor_ui_005(self):
            '''Verify the Colour Category dropdown list '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'),self.check_colour_category)

    def test_add_customdoor_ui_006(self):
            '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category '''
            self.driver.implicitly_wait(2)
            self.assertEqual(False,self.check_door_colour_custom)
    #
    def test_add_customdoor_ui_007(self):
        '''Verify the Door Colour dropdown if select "OliColour" in Colour Category '''
        self.driver.implicitly_wait(2)
        self.assertIn(('test_sample\ntest_sample'), self.check_door_colour_oilcolour)
    #
    def test_add_customdoor_ui_008(self):
            '''Verify the Door Colour dropdown if select "Painted" in Colour Category '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_door_colour_painted)

    def test_add_customdoor_ui_009(self):
            '''Verify the Door Colour dropdown if select "Raw" in Colour Category '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_door_colour_raw)

    def test_add_customdoor_ui_010(self):
            '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'),self.check_door_colour_sealedcolour)

    def test_add_customdoor_ui_011(self):
            '''Verify the Frame Colour dropdown list '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_frame_colour)

    def test_add_customdoor_ui_012(self):
            '''Verify the Timber Profile dropdown list '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample\ntest_sample\ntest_sample\ntest_sample'), self.check_timber_profile)

    def test_add_customdoor_ui_013(self):
            '''Verify the Insert Material dropdown list'''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_insert_material)

    def test_add_customdoor_ui_014(self):
            '''Verify the Insert Location dropdown list,should includes "Face Fixed","Inserted into Frame" and "TBA" '''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_insert_location)

    def test_add_customdoor_ui_015(self):
            '''Verify Insert Type dropdown list, the default value should be empty '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('test_sample'), self.check_insert_type_default)

    def test_add_customdoor_ui_016(self):
            '''Verify the Insert Type dropdown if select "ACPS Cat1" in Insert Material category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_insert_type_cat1)

    def test_add_customdoor_ui_017(self):
            '''Verify the Insert Type dropdown if select "ACPS Cat2" in Insert Material category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_insert_type_cat2)

    def test_add_customdoor_ui_018(self):
            '''Verify the Insert Type dropdown if select "Acrylic" in Insert Material category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('3mm Acrylic\n4.5mm Acrylic\n6mm Acrylic'), self.check_insert_type_acrylic)

    def test_add_customdoor_ui_019(self):
            '''Verify the Insert Type dropdown if select "Aluminium" in Insert Material category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('test_sample'), self.check_insert_type_aluminium)


if __name__ == '__main__':
    unittest.main(verbosity=2)