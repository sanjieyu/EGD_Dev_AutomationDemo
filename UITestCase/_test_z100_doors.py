# Author:Yi Sun(Tim) 2025-5-28

'''Test Change Quote Status'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.z100_doors import *

class z100_Doors_Test(unittest.TestCase,Move_100_Doors):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.read_config = ReadConfig()
        cls.url = cls.read_config.get_url()
        cls.admin_username = cls.read_config.admin_username()
        cls.admin_password = cls.read_config.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.move_100doors = Move_100_Doors(cls.driver)
        cls.move_100doors.find_copy_job()
        cls.move_100doors.goto_new_job()
        cls.move_100doors.get_job_number
        cls.move_100doors.goto_status()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_move_100doors_ui_001(self):
        '''Check if it's moved to MYOB screen'''
        self.assertTrue(self.move_100doors.check_myob_screen)

    def test_move_100doors_ui_002(self):
        '''Check if it's moved to Order screen'''
        self.assertTrue(self.move_100doors.move_check_order)

if __name__ == "__main__":
    unittest.main(verbosity=2)