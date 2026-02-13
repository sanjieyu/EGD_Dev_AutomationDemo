# Author:Yi Sun(Tim) 2025-08-12

'''Test Add Standard Door Page, Extra section'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.standard_door_extra import *
from utils.read_config import *


class Add_StandardDoorExtra_UI_Test(unittest.TestCase,Standard_Door_Extra):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.config_read = ReadConfig()
        self.url = self.config_read.get_url()
        self.admin_username = self.config_read.admin_username()
        self.admin_password = self.config_read.admin_password()
        self.login = Admin_Portal(self.driver)
        self.driver.get(self.url)
        self.login.login(self.admin_username, self.admin_password)
        self.driver.implicitly_wait(5)
        self.goaddquote = Standard_Door(self.driver)
        self.goaddquote.go_addquote()
        self.gostandarddoor = Standard_Door_Extra(self.driver)
        self.gostandarddoor.go_addstandarddoor()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_standarddoor_extra_ui_001(self):
        '''Verify the Extras and Site Picture, should including "Extras" and "Site Picture" '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Extras', 'Site Pictures'), self.check_extra_picture)

    def test_add_standarddoor_extra_ui_002(self):
            '''Verify the details for Jamb in Extras section '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('LH Jamb Type', 'Size','RH Jamb Type','Size'), self.check_jamb_extras)

    def test_add_standarddoor_extra_ui_003(self):
            '''Verify the list for LH JAMB Type '''
            self.driver.implicitly_wait(2)
            self.assertIn(('Custom Fabrication\nHot Dip\nInternal – RHS\nInternal – Standard\nRHS\nStandard'),
                          self.lh_jamb_type)

    def test_add_standarddoor_extra_ui_004(self):
            '''Verify the list for LH Width Size'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('50\n100\n125\n150\n180'), self.lh_width_size)

    def test_add_standarddoor_extra_ui_005(self):
        '''Verify the list for LH Depth Size, should including "50" and "70" '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('50\n70'), self.lh_depth_size)

    def test_add_standarddoor_extra_ui_006(self):
            '''Verify the list for RH JAMB Type'''
            self.driver.implicitly_wait(2)
            self.assertIn(('Custom Fabrication\nHot Dip\nInternal – RHS\nInternal – Standard\nRHS\nStandard'),
                          self.rh_jamb_type)

    def test_add_standarddoor_extra_ui_007(self):
            '''Verify the list for RH Width Size, should including "50","100","125S","150" and "180" '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('50\n100\n125\n150\n180'), self.rh_width_size)

    def test_add_standarddoor_extra_ui_008(self):
        '''Verify the list for RH Depth Size, should including "50" and "70" '''
        self.driver.implicitly_wait(3)
        self.assertEqual(('50\n70'), self.rh_depth_size)

    def test_add_standarddoor_extra_ui_009(self):
            '''Verify the details for Cover Type in Extras section '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('LH Cover Type', 'Size', 'LH Cover Colour', 'RH Cover Type', 'Size',
            'RH Cover Colour'),self.check_cover_type)

    def test_add_standarddoor_extra_ui_010(self):
        '''Verify the list for LH Cover Width Size '''
        self.driver.implicitly_wait(3)
        self.assertEqual(('102\n127\n152\n182'), self.lh_cover_width_size)

    def test_add_standarddoor_extra_ui_011(self):
        '''Verify the list for LH Cover Depth Size'''
        self.driver.implicitly_wait(3)
        self.assertEqual(('52\n72'), self.lh_cover_depth_size)

    def test_add_standarddoor_extra_ui_012(self):
            '''Verify the list for LH Cover Type '''
            self.driver.implicitly_wait(3)
            self.assertIn(('Colourbond\nCustom'),self.lh_cover_type)

    def test_add_standarddoor_extra_ui_013(self):
            '''Verify the list for Pelmet Type '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nColourbond\nCustom\nHeadpanel to match door\nSoffit – Colourbond\n'
                              'Soffit – Custom'),self.pelmet_type)

    def test_add_standarddoor_extra_ui_014(self):
            '''Verify the Height for Pelmet Height '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('100\n160\n200\n250\n300\n350'),self.pelmet_height)

    def test_add_standarddoor_extra_ui_015(self):
            '''Verify the Height for Pelmet Depth '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('50\n70'),self.pelmet_depth)

    def test_add_standarddoor_extra_ui_016(self):
            '''Verify the Height for Pelmet Colour '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nBasalt\nBlue Gum\nCedar\nClassic Cream\nCottage Green\nCove\nDeep Bronze\n'
                              'Deep Ocean\nDover White\nDune\nEvening Haze\nGully\nIronstone\nJarrah\nJasper\nMangrove\nManor Red\n'
                              'Monument\nNew Copper\nNight Sky\nPale Eucalypt\nPaperbark\nPrecious Silver Pearl\n'
                              'Same as Door\nShale Grey\nSoutherly\nSurfmist\nTBA\nTerrain\nWallaby\nWalnut\nWindspray\n'
                              'Woodland Grey'),self.pelmet_colour)

    def test_add_standarddoor_extra_ui_017(self):
            '''Verify the Elements in Windows Section '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Window Type','No. of Windows','Window Colour','Window Position',
                              'Window Position Custom'),self.windows_section)

    @unittest.skip
    def test_add_standarddoor_extra_ui_018(self):
            '''Verify the list for Windows Type'''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nColonial\nColonial / Classic\nColonial / Lincoln\nCustom - Aluminium\n'
                              'Plain - Stanford\nPlain / Classic\nPlain / Lincoln\nPort Hole\nSunrise\nSunset'),
                             self.windows_type)

    def test_add_standarddoor_extra_ui_019(self):
            '''Verify the default value for No. of windows '''
            self.driver.implicitly_wait(3)
            self.assertEqual('0',self.default_no_windows)

    @unittest.skip
    def test_add_standarddoor_extra_ui_020(self):
            '''Verify the list for Windows Position '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nBottom\nLHS (Inside looking out)\nOther / Custom\nRHS (Inside looking out)\n'
                              'Top'),self.windows_position)

    def test_add_standarddoor_extra_ui_021(self):
            '''Verify the Elements in Hardware Colour Section '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Hardware Colour Category','Hardware Colour','Window Frame Colour','Hang Door Other',
                              'Fixing Type Other','Noggins Other'),self.hardware_colour_section)

    @unittest.skip
    def test_add_standarddoor_extra_ui_022(self):
            '''Verify the list for Windows Type'''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\n2 Lite Hampton Classic\n4 Lite Hampton Classic\n4 Lite Hampton Lincoln\n'
                              '6 Lite Colonial Lincoln\nCustom - Aluminium\nPlain / Classic\nPlain / Lincoln'),
                             self.windows_type_panellift)

    def test_add_standarddoor_extra_ui_023(self):
            '''Verify the Windows Position for Custom-Aluminium '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nOther / Custom'),self.windows_position_custom)

if __name__ == "__main__":
    unittest.main(verbosity=2)

