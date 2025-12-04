# Author:Yi Sun(Tim) 2023-11-16

'''Test Panel Lift Safe Page'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.panel_left_safe import *
from CommonModule.read_config import *
from selenium.webdriver.support.ui import WebDriverWait

class PanelLiftSafe_UI_Test(unittest.TestCase,Panel_lift_Safe):
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
        cls.gopanellift = Panel_lift_Safe(cls.driver)
        cls.gopanellift.go_panel_lift_safe()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_panellift_ui_001(self):
        '''Verify each section in Panel Lift Safe page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Order','Rollforming','Assembly','Modifications',
                          'Extras Orders','Paint','Painted','QC'),self.check_panel_lift_section)

    def test_panellift_ui_002(self):
        '''Verify each column in Order table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:','Proposal No','Client Name','Supply Type','Door No',
                          'Status','    Extras Orders & Documents'),self.check_order_table)

    def test_panellift_ui_003(self):
            '''Verify each elements in Rollforming table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Number of Doors:', 'Reschedule from:'),self.check_rollforming_table)

    def test_panellift_ui_004(self):
        '''Verify Date Filter fun in Rollforming table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_rollforming_date_filter)

    def test_panellift_ui_005(self):
        '''Verify Save Changes button in Rollforming table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_rollforming_save)
    def test_panellift_ui_006(self):
        '''Verify Table display in Rollforming screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_rollforming_tableframe)

    def test_panellift_ui_007(self):
            '''Verify each elements in Assembly table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Number of Doors:', 'Prop. No','Door No','Status'), self.check_assembly_table)

    def test_panellift_ui_008(self):
        '''Verify each elements in Modification table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:', 'Prop. No', 'Door Colour', '    Extras Orders & Documents'),
                         self.check_modification_table)

    def test_panellift_ui_009(self):
        '''Verify each elements in Extra Order table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:', 'Prop. No', 'Colour Category', '    Extras Orders & Documents'),
                         self.check_extraorder_table)

    def test_panellift_ui_010(self):
            '''Verify each elements in Paint table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Number of Doors:', 'Proposal No', 'Actual Height', 'Status'),self.check_paint_table)

    def test_panellift_ui_011(self):
        '''Verify each elements in Painted table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:', 'Proposal No', 'Number of Panels', 'Status'), self.check_painted_table)

    def test_panellift_ui_012(self):
            '''Verify each elements in QC table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Number of Doors:', 'Proposal No', 'Actual Width', 'Status'),
                             self.check_qc_table)

    def test_panellift_ui_013(self):
            '''Verify qc pass and qc fail radio box in QC table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('QC Fail', 'QC Pass',),self.check_qc_table_new)

    def test_panellift_ui_014(self):
            '''Verify qc fail radio box status'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.check_qc_fail)

    def test_panellift_ui_015(self):
            '''Verify qc fail radio box status'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.check_qc_pass)

if __name__ == '__main__':
    unittest.main(verbosity=2)