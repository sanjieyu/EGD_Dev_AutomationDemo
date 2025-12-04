# Author:Yi Sun(Tim) 2025-05-27

'''Test the Track Option function'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.track_option import *
from CommonModule.read_config import *

class TrackOption_UI_Test(unittest.TestCase,Track_Option):
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
        cls.track_option  = Track_Option(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_track_option_fun_001(self):
        '''Verify the T35'''
        self.driver.implicitly_wait(2)
        self.assertEqual('T35',self.track_option.check_track_t35)
    #
    def test_track_option_fun_002(self):
        '''Verify the T50_Std'''
        self.driver.implicitly_wait(2)
        self.assertEqual('T50',self.track_option.check_track_t50)


if __name__ == '__main__':
    unittest.main(verbosity=2)