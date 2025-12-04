# Author:Yi Sun(Tim) 2024-7-25

'''Test Rolling Cycle Management Page for Roller Doors'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.rolling_cycle_management_roller_door import *

class Rolling_RollerDoor_UI_Test(unittest.TestCase,Rolling_Cycle_Management_Roller_Door):
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
        cls.go_rolling_management_roller = Rolling_Cycle_Management_Roller_Door(cls.driver)
        cls.go_rolling_management_roller.go_rolling()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_rolling_management_roller_ui_001(self):
        '''Verify the url of Rolling Cycle Management Roller Door Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual( 'http://aabb/Manage/Rollforming/RollerDoors',self.check_rolling_url)

    def test_rolling_management_roller_ui_002(self):
        '''Verify the title of Rolling Cycle Management Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual( 'Rolling Cycle Management - ExoRoll Doors  ',self.check_rolling_title)

    def test_rolling_management_roller_ui_003(self):
        '''Verify the tab of Rolling Cycle Management Page'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('General Settings','Colour Cycles Settings','Temporary Closed','History'),self.check_tab)

    def test_rolling_management_roller_ui_004(self):
        '''Verify the General Settings screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Split Doors','Lockout Settings','Individual Shift Settings'),self.check_general_settings)

    def test_rolling_management_roller_ui_005(self):
        '''Verify the Colour Cycle Settings screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Coil Settings','Save Coil Settings'),self.check_colour_cycle_settings)

    def test_rolling_management_roller_ui_006(self):
        '''Verify the Temp Closed screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Temporary Closed Colour Cycles','Update Cycles'),self.check_temp_closed)

if __name__ == '__main__':
    unittest.main(verbosity=2)