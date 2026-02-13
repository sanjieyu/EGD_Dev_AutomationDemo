# Author:Yi Sun(Tim) 2025-3-18

'''Test Add Custom Door Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.shutter_door import *
from utils.read_config import *

class Add_ShutterDoor_UI_Test(unittest.TestCase,Shutter_Door):
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
        cls.goshutterdoor = Shutter_Door(cls.driver)
        cls.goshutterdoor.go_add_shutter_door()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_shutterdoor_ui_001(self):
        '''Verify the main elements in the page '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Roller Shutter Details'),self.check_shutterdoor_page)

    def test_add_shutterdoor_ui_002(self):
        '''Verify the unit and packaging type '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door / Unit Number','Packaging Type'),self.check_unit_packaging)

    def test_add_shutterdoor_ui_003(self):
        '''Verify the install section '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Install Type','Door Duty Cycle','Slat Type','Slat Design','Slat Ventilation',
                          'Slat Material','Slat Finish','Slat Finish Custom','Technician Measure','Measure Required'),
                         self.check_install_details)

    def test_add_shutterdoor_ui_004(self):
        '''Verify the install type '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nCommercial / Car Park\nDistribution Centre\nFactory / Warehouse\nResidential\n'
                          'Supply Only (Parts)\nSupply Only (Whole Door)'),self.check_install_type)

    def test_add_shutterdoor_ui_005(self):
        '''Verify the Door duty cycle '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\n10% Low\n30% High Duty\n60% Extra High'),self.check_door_duty_cycle)

    def test_add_shutterdoor_ui_006(self):
        '''Verify the Slat type'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\n100 x 0.8mm\n100 x 1.0mm\n75 x 0.8mm'),self.check_slat_type)

    def test_add_shutterdoor_ui_007(self):
        '''Verify the Slat design'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nSolid\nVentilation Perforated\nVentilation Slotted'),self.check_slat_design)

    def test_add_shutterdoor_ui_008(self):
        '''Verify the Slat ventilation'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nEvery Slat\nEvery 2nd Slat\nEvery 4th Slat\nBottom 1/3\nMiddle 1/3\nTop 1/3'),
                         self.check_slat_ventilation)

    def test_add_shutterdoor_ui_009(self):
        '''Verify the Slat material'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nGalvabond by Bluescope\nPowdercoat Custom - 1 Side\nPowdercoat Custom - 2 Side\n'
                          'Powdercoat Duralloy - 2 Side'),self.check_slat_material)

    def test_add_shutterdoor_ui_010(self):
        '''Verify the Slat finish'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nAnodic Bronze\nAnodic Dark Grey\nAnodic Off White\nAnodic Silver Grey\nAPO Grey\nBasalt\n'
                 'BASALT®\nBlack Gloss\nBlack Matt\nBlack Satin\nBlue Ridge\nBushland\nCharcoal\nClassic Cream\n'
                 'CLASSIC CREAM™\nCottage Green\nCOTTAGE GREEN®\nCove\nCOVE®\nDeep Ocean\nDEEP OCEAN®\nDomain\nDune\n'
                 'DUNE®\nEstate\nEvening Haze\nEVENING HAZE®\nGULLY®\nHamersley Brown\nHeadland\nHeritage Green\n'
                 'Ironstone\nIRONSTONE®\nJasper\nJASPER®\nLoft\nMangrove\nMANGROVE®\nManor Red\nMANOR RED®\nMonument\n'
                 'MONUMENT®\nNIGHT SKY®\nNotre Dame\nOff White\nOlde Pewter\nPale Eucalypt\nPALE EUCALYPT®\nPaperbark\n'
                 'PAPERBARK®\nPearl White Gloss\nPrimose Gloss\nRaw\nRiversand\nSandbank\nShale Grey\nSHALE GREY™\n'
                 'Shoji White\nStone Beige\nSurfmist\nSURFMIST®\nTBC\nTerrain\nTERRAIN®\nWallaby\nWALLABY®\nWhite Birch\n'
                 'Wilderness\nWindspray\nWINDSPRAY®\nWoodland Grey\nWOODLAND GREY®'), self.check_slat_finish)

    def test_add_shutterdoor_ui_011(self):
        '''Verify the status for technician_measure checkbox'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_technician_measure)

    def test_add_shutterdoor_ui_011(self):
        '''Verify the status for  Measure Required checkbox'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_measure_required)

    def test_add_shutterdoor_ui_012(self):
        '''Verify each element for size details'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Opening Size LH', 'Opening Size RH', 'Opening Size Width', 'SR Left', 'HR', 'SR Right'),
                         self.check_size_details)

    def test_add_shutterdoor_ui_013(self):
        '''Verify the default value for Opening Size LH, should be "0"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('0'), self.check_openinglh_default)

    def test_add_shutterdoor_ui_014(self):
            '''Verify the default value for Opening Size RH, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_openingrh_default)
    def test_add_shutterdoor_ui_015(self):
            '''Verify the default value for Opening Width, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_openingwidth_default)

    def test_add_shutterdoor_ui_016(self):
            '''Verify the default value for SR Left, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_srleft_default)
    def test_add_shutterdoor_ui_017(self):
            '''Verify the default value for SR Left, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_hr_default)

    def test_add_shutterdoor_ui_018(self):
        '''Verify the default value for SR Left, should be "0"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('0'), self.check_srright_default)

    def test_add_shutterdoor_ui_019(self):
            '''Verify each element for additional_fabrication details'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Additional Fabrication', 'Additional Fabrication Required', 'Shop Drawings',
                              'Lifting/Access Equipment'),self.check_additional_fabrication)

    def test_add_shutterdoor_ui_020(self):
        '''Verify the list for additional_fabrication dropdown'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nLevel 1\nLevel 2\nLevel 3\nLevel 4\nLevel 5\nLevel 6\nLevel 7\nLevel 8'),
                         self.check_additional_fabrication_list)

    def test_add_shutterdoor_ui_021(self):
            '''Verify the list for shop drawings dropdown'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nStandard\nMedium\nHigh\nComplex'),self.check_shop_drawings_list)

    def test_add_shutterdoor_ui_022(self):
            '''Verify the list for lifting_equipment dropdown'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nPlease Select\nForklift\nPlatform Ladder\nScissor Lift'),
                             self.check_lifting_equipment_list)

    def test_add_shutterdoor_ui_023(self):
            '''Verify each checkbox option'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Induction Loop', 'Reverse Roll - Roller Door', 'Eco Smart WiFi','Taper',
                              'Reverse Roll Colour'),self.check_checkbox_option)

    def test_add_shutterdoor_ui_024(self):
        '''Verify the status for Eco wifi checkbox'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_eco_wifi_checkbox)

    def test_add_shutterdoor_ui_025(self):
            '''Verify operation_details'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Operation Side', 'Operation Type', 'Battery Backup'), self.check_operation_details)

    def test_add_shutterdoor_ui_026(self):
            '''Verify operation_details'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Opener', 'No of Handsets', 'Wall Button', 'Opener Details', 'Digital Keypad',
                              'Internal Push Button','PE Beam','No. of PE Beam Sets'), self.check_opener_details)

    def test_add_shutterdoor_ui_027(self):
            '''Verify the list for Opener dropdown'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\n1PH - 25m2 ECO HDS-2501\n1PH - 40m2 ECO HDS-4001\n3PH - 25m2 ECO HDS-2503\n'
                              '3PH - 45m2 ECO HDS-4503\nManual Hoist - Extra Heavy Duty 25m2\nManual Hoist - Heavy Duty 22m2\n'
                              'Other\nReuse Existing Motor Only'),self.check_opener_list)

    def test_add_shutterdoor_ui_028(self):
            '''Verify the default value for Handsets, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_handsets_default)

    def test_add_shutterdoor_ui_029(self):
            '''Verify the default value for Wall button, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_wallbtn_default)

    def test_add_shutterdoor_ui_030(self):
        '''Verify the default value for Digital Keypad, should be "0"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('0'), self.check_digital_keypad_default)

    def test_add_shutterdoor_ui_031(self):
            '''Verify the default value for Internal Push, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_pushbtn_default)

    def test_add_shutterdoor_ui_032(self):
            '''Verify the default value for PE Beam Sets, should be "0"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_beam_set_default)

    def test_add_shutterdoor_ui_033(self):
        '''Verify the list for PE Beam dropdown'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nInfrared Sensor <15m\nInfrared Sensor IP54 >12m\nReflective <12m\n'
                          'Reflective <7m'), self.check_pe_beam_list)

    def test_add_shutterdoor_ui_034(self):
            '''Verify Other details'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Windlock', 'Track', 'Remove and Dispose','Seals','Hang Door From','Lintel Type',
                              'Fixing Type','Door Area (m2)','Door Status','Expected Delivery Date'),
                             self.check_other_details)

    def test_add_shutterdoor_ui_035(self):
            '''Verify Other Extras, Value'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Other Extras', 'Value $', 'Additional Door Information','Production Notes   (0 / 50)'),
                             self.check_other_extras_value)

    def test_add_shutterdoor_ui_036(self):
        '''Verify each element for jamb and pelmet of extras section'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('LH Jamb Type', 'Size', 'RH Jamb Type', 'Size','Pelmet Type','Size','Pelmet Colour'),
                         self.check_extras_jamb)

    def test_add_shutterdoor_ui_037(self):
            '''Verify list for LH JAMB Type'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nRHS\nRHS – Internal'), self.lh_jamb_type)

    def test_add_shutterdoor_ui_038(self):
            '''Verify list for LH JAMB Width'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('50\n100\n125\n150\n180'), self.lh_jamb_width)

    def test_add_shutterdoor_ui_039(self):
        '''Verify list for LH JAMB Width'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('50\n70'), self.lh_jamb_depth)

    def test_add_shutterdoor_ui_040(self):
            '''Verify list for RH JAMB Type'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nRHS\nRHS – Internal'), self.rh_jamb_type)

    def test_add_shutterdoor_ui_041(self):
        '''Verify list for RH JAMB Width'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('50\n100\n125\n150\n180'), self.rh_jamb_width)

    def test_add_shutterdoor_ui_042(self):
        '''Verify list for RH JAMB Width'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('50\n70'), self.rh_jamb_depth)

    def test_add_shutterdoor_ui_043(self):
            '''Verify list for Pelmet Type'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nColourbond\nCustom\nHeadpanel to match door\nSoffit – Colourbond\nSoffit – Custom'),
                             self.pelmet_type)

    def test_add_shutterdoor_ui_044(self):
        '''Verify list for Pelmet Height'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('100\n160\n200\n250\n300\n350'), self.pelmet_height)

    def test_add_shutterdoor_ui_045(self):
        '''Verify list for Pelmet Depth'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('50\n70'), self.pelmet_depth)

    def test_add_shutterdoor_ui_046(self):
            '''Verify list for Pelmet Colour'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nBasalt\nBlue Gum\nCedar\nClassic Cream\nCottage Green\nCove\nDeep Bronze\n'
                              'Deep Ocean\nDover White\nDune\nEvening Haze\nGully\nIronstone\nJarrah\nJasper\nMangrove\nManor Red\nMonument\n'
                              'New Copper\nNight Sky\nPale Eucalypt\nPaperbark\nPrecious Silver Pearl\nSame as Door\nShale Grey\n'
                              'Southerly\nSurfmist\nTBA\nTerrain\nWallaby\nWalnut\nWindspray\nWoodland Grey'),self.pelmet_colour)

    def test_add_shutterdoor_ui_047(self):
            '''Verify list for Hardware Colour Category'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nPowderCoatStandard'), self.hardware_colour_category)

    def test_add_shutterdoor_ui_048(self):
            '''Verify list for Track Colour Category'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nPowderCoatStandard\nPowderCoatUpgrade'), self.track_colour_category)

if __name__ == '__main__':
    unittest.main(verbosity=2)