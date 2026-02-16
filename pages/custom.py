# Author:Yi Sun(Tim) 2023-11-02

'''Add Custom Door Details Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.add_quote import *

class Custom_Door(Add_Quote):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    add_door_menu = (By.ID,'test_sample')
    add_custom_btn = (By.NAME,'test_sample')
    add_btn_loc = (By.CSS_SELECTOR, "[aria-label='test_sample']")

    # [Remaining 50+ locators redacted for confidentiality]
    '''loc for each element for install details'''
    '''loc for each element for SIZE details'''
    '''loc for each element for Panels details'''
    '''loc for each element for checkboxes details'''
    '''loc for Opener details'''
    '''loc for other elements details '''
    '''loc for additional infomation details '''
    '''loc for Extra and Site Pictures'''
    '''loc for each element in Extra'''

    def go_addcustomdoor(self):
        '''Open the Add Custom Door from Quote Page'''
        self.driver.find_element(*self.add_door_menu).click()
        self.driver.find_element(*self.add_custom_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @property
    def check_customdoor_page(self):
        '''check the main elements in the page'''
        form_element = self.driver.find_element(*self.door_main_page)
        standarddoor_title = self.driver.find_element(*self.title_loc).text
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        print(standarddoor_title)
        return standarddoor_title

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.driver.find_element(*self.install_type_loc).text
        design = self.driver.find_element(*self.design_loc).text
        colour_category = self.driver.find_element(*self.colour_category_loc).text
        door_colour = self.driver.find_element(*self.door_colour_loc).text
        frame_colour = self.driver.find_element(*self.frame_colour_loc).text
        timber_profile = self.driver.find_element(*self.timber_profile_loc).text
        insert_material = self.driver.find_element(*self.insert_material_loc).text
        insert_location = self.driver.find_element(*self.insert_location_loc).text
        insert_type = self.driver.find_element(*self.insert_type_loc).text
        insert_colour = self.driver.find_element(*self.insert_colour_loc).text
        insert_other = self.driver.find_element(*self.insert_other_loc).text
        custom_colour = self.driver.find_element(*self.custom_colour_loc).text
        return  (install_type,design,colour_category,door_colour,frame_colour,timber_profile,insert_material,
                 insert_location,insert_type,insert_colour,insert_other,custom_colour)

    @property
    def check_frame_colour(self):
        '''check the Frame Colour dropdown list'''
        self.driver.find_element(*self.frame_colour_select).click()
        frame_colour_list = self.driver.find_element(*self.frame_colour_select).text
        return frame_colour_list

    @property
    def check_colour_custom(self):
        '''check the Door Colour dropdown for Custom Category'''
        custom = colour_category.select_by_visible_text('test_sample')
        custom_colour = self.driver.find_element(*self.door_colour_select)
        if custom_colour.is_enabled():
            return  False
        else:
            return True

    @property
    def check_colour_portabella(self):
        '''check the Door Colour dropdown for Portabella Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        portabella = colour_category.select_by_visible_text('test_sample')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_customcolour_box(self):
        '''check the Custom Colour input box should be disable by default'''
        custom_colour_box = self.driver.find_element(*self.custom_colour_inputbox)
        if custom_colour_box.is_enabled():
            return  False
        else:
            return True

    @property
    def check_srleft_default(self):
        '''check the default value for SR Left'''
        srleft_default = self.driver.find_element(*self.sr_left_select).get_attribute('value')
        print(srleft_default)
        return  srleft_default

    @property
    def lh_jamb_type(self):
        '''check the list for LH JAMB Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_jamb_select).click()
        lh_jambtype_list = self.driver.find_element(*self.lh_jamb_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_jambtype_list)
        return  lh_jambtype_list


if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://test_sample ")
        driver.implicitly_wait(10)

        login = Custom_Door(driver)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clickLogin()
        login.go_addquote()
        login.go_addcustomdoor()
        login.check_customdoor_page
        # login.check_install_details
        # login.check_install_type
        # login.check_design
        # login.check_colour_category
        # login.check_door_colour_custom
        # login.check_door_colour_oilcolour
        # login.check_door_colour_painted
        # login.check_door_colour_raw
        # login.check_door_colour_sealedcolour
        # login.check_frame_colour
        # login.check_timber_profile
        # login.check_insert_material
        # login.check_insert_location
        # login.check_insert_type_default
        # login.check_insert_type_cat1
        # login.check_insert_type_acrylic
        # login.check_insert_type_aluminium
        # login.check_colour_flexigraphic
        # login.check_colour_metalfx
        # login.check_colour_paintedfinish
        # login.check_colour_portabella
        # login.check_colour_timberfx
        # login.check_customcolour_box
        # login.check_customcolourbox_custom
        # login.check_size_details
        # login.check_openinglh_default
        # login.check_lhrk_list
        # login.check_timber_details
        # login.check_checkboxes_details
        # login.check_opener_details
        # login.check_other_details
        # login.check_additional_details
        # login.check_extra_picture
        # login.check_jamb_extras
        # login.check_cover_type
        # login.lh_jamb_type
        # login.lh_width_size
        # login.lh_depth_size
        # login.rh_jamb_type
        # login.rh_width_size
        # login.rh_depth_size
        # # login.check_cover_type
        # login.lh_cover_type
        # login.lh_cover_width_size
        # login.lh_cover_depth_size














































