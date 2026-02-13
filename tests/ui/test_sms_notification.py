# Author:Yi Sun(Tim) 2024-5-21

'''Test SMS Notification Page'''

import unittest
from selenium import webdriver
from utils.read_config import *
from pages.sms_notification import *

class SMS_Notification_Test(unittest.TestCase, SMS_Notification):
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
        cls.go_sms = SMS_Notification(cls.driver)
        cls.go_sms.go_sms_notification()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_sms_ui_001(self):
        '''Verify the URL'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Manage/SMSNotificationsSetting',self.check_sms_url)

    def test_sms_ui_002(self):
        '''Verify the Title'''
        self.driver.implicitly_wait(2)
        self.assertEqual('SMS Notification',self.check_sms_title)
    def test_sms_ui_003(self):
        '''Verify the default values'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('ECO_API_KEY','Eco2023!','+61437167001'),self.check_default_value)

    def test_sms_ui_004(self):
            '''Verify the apikey box status'''
            self.driver.implicitly_wait(2)
            self.assertEqual( False,self.check_apikey_disable)

    def test_sms_ui_005(self):
            '''Verify the password box status'''
            self.driver.implicitly_wait(2)
            self.assertEqual( False,self.check_pwd_disable)

    def test_sms_ui_006(self):
            '''Verify the From box status'''
            self.driver.implicitly_wait(2)
            self.assertEqual( False,self.check_from_disable)

    def test_sms_ui_007(self):
        '''Verify the tab screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('MLB-Install','SYD-Install'),self.check_tab)

    def test_sms_ui_008(self):
        '''Verify the Production Enter in MLB-Install tab screen'''
        self.driver.implicitly_wait(2)
        self.assertIn('MLB Install - In Production Entered',self.check_mlb_enter)
    def test_sms_ui_009(self):
        '''Verify the Production Rollforming in MLB-Install tab screen'''
        self.driver.implicitly_wait(2)
        self.assertIn('MLB Install - In Production Roll Forming',self.check_mlb_rollforming)

    def test_sms_ui_010(self):
            '''Verify the Production QC Pass in MLB-Install tab screen'''
            self.driver.implicitly_wait(2)
            self.assertIn( 'MLB Install - In Production QC Pass',self.check_mlb_qcpass)

if __name__ == '__main__':
    unittest.main(verbosity=2)