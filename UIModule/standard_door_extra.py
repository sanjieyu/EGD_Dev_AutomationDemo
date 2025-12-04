# Author:Yi Sun(Tim) 2025-08-12

'''Add Standard Door Details Page, Extra Section'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
# from UIModule.add_quote import *
from UIModule.standard_door import *

class Standard_Door_Extra(Standard_Door):
    '''loc for Extra and Site Pictures'''
    extras_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[1]/button/span')
    site_picture_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[10]/div/div/div[1]/'
                                 'button/span')

    '''loc for each element in Extra'''
    lh_jamb_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/div/'
                            'div[1]/div[1]/label[1]')
    lh_jamb_select = (By.ID,'LH_JambTypeStandard')
    lh_size_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/div/'
                            'div[1]/div[1]/label[2]')
    lh_size_width_btn = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                  'div/div[1]/div[2]/div[2]/span[1]/a')
    lh_size_depth_btn = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                  'div/div[1]/div[2]/div[3]/span[1]/a/span[1]')
    lh_size_width_select = (By.XPATH,'//*[@id="ui-id-5"]')
    lh_size_depth_select = (By.ID, 'ui-id-6')
    rh_jamb_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/div/'
                            'div[2]/div[1]/label[1]')
    rh_jamb_select = (By.ID,'RH_JambTypeStandard')
    rh_size_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/div/'
                            'div[2]/div[1]/label[2]')
    rh_size_width_btn = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                  'div/div[2]/div[2]/div[2]/span[1]/a/span[1]')
    rh_size_depth_btn = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                  'div/div[2]/div[2]/div[3]/span[1]/a/span[1]')
    rh_size_width_select = (By.ID,'ui-id-7')
    rh_size_depth_select = (By.ID,'ui-id-8')

    lh_cover_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[7]/div/div/div[2]/div/'
                                  'div/div[3]/div[1]/label[1]')
    lh_cover_select = (By.ID,'LH_CoverTypeStandard')
    lh_cover_width_size_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[7]/div/div/div[2]/'
                                        'div/div/div[3]/div[1]/label[2]')

    lh_cover_width_btn = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                   'div/div[3]/div[2]/div[2]/span[1]/a')
    lh_cover_depth_btn = (By.XPATH,
                          '/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/div/div[3]/'
                          'div[2]/div[3]/span[1]/a')
    lh_cover_width_select = (By.ID,'ui-id-9')
    lh_cover_depth_select = (By.ID, 'ui-id-10')
    lh_cover_colour_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                    'div/div[3]/div[1]/label[3]')
    lh_cover_colour_select = (By.ID,'LHCoverColour')
    rh_cover_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                  'div/div[4]/div[1]/label[1]')
    rh_cover_select = (By.ID,'RH_CoverTypeStandard')
    rh_cover_width_size_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                        'div/div/div[4]/div[1]/label[2]')
    rh_cover_width_btn = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                   'div/div[4]/div[2]/div[2]/span[1]/a')
    rh_cover_width_select = (By.ID,'ui-id-11')
    rh_cover_depth_select = (By.ID, 'ui-id-12')
    rh_cover_colour_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                    'div/div[4]/div[1]/label[3]')
    rh_cover_colour_select = (By.ID,'RHCoverColour')

    '''new added at 12th Dec 2024'''
    pelmet_type_select_loc = (By.ID,'PelmetTypeStandard')
    pelmet_height_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                      'div/div/div[5]/div[2]/div[2]/span[1]/a')
    pelmet_height_select_loc = (By.ID,'ui-id-13')
    pelmet_depth_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                     'div/div/div[5]/div[2]/div[3]/span[1]/a/span[1]')
    pelmet_depth_select_loc = (By.ID,'ui-id-14')
    pelmet_colour_select_loc = (By.ID,'Pelmet')

    windows_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                 'div/div[7]/fieldset/div/div[1]/label')
    windows_type_select_loc = (By.ID,'WindowType')
    no_windoes_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/div/'
                               'div[7]/fieldset/div/div[2]/label')
    no_windows_box_loc = (By.ID,'Windows')
    windows_colour_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                   'div/div[7]/fieldset/div/div[3]/label')
    windows_colour_select_loc = (By.ID,'window_color_standard_part')
    windows_position_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                     'div/div/div[8]/fieldset/div/div[1]/label')
    windows_position_select_loc = (By.ID,'WindowPosition')
    windows_custom_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                   'div/div[8]/fieldset/div/div[2]/label')
    windows_custom_box_loc = (By.ID,'WindowPositionCustom')

    hardware_colour_cate_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                         'div/div/div[9]/fieldset/div/div[1]/label')
    hardware_colour_cate_select_loc = (By.ID,'HardwareColourCategoryStandard')
    hardware_colour_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                    'div/div[9]/fieldset/div/div[2]/label')
    hardware_colour_select_loc = (By.ID,'HardwareColourStandard')
    window_frame_colour_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                        'div/div/div[9]/fieldset/div/div[3]/label')
    window_frame_colour_select_loc = (By.ID,'WindowFrameColour')
    hang_door_other_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                    'div/div[10]/fieldset/label')
    hang_door_other_box_loc = (By.ID,'HangDoorOther')
    fixing_type_other_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/'
                                      'div/div/div[11]/fieldset/label')
    fixing_type_other_box_loc = (By.ID,'FixingTypeOther')
    noggins_other_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[9]/div/div/div[2]/div/'
                                  'div/div[12]/fieldset/label')
    noggins_other_box_loc = (By.ID,'NogginsOther')

    @property
    def check_extra_picture(self):
        '''check the details for Jamb in Extras section'''
        extra = self.driver.find_element(*self.extras_loc).text
        site_pciture = self.driver.find_element(*self.site_picture_loc).text
        print(extra,site_pciture)
        return  extra,site_pciture

    @property
    def check_jamb_extras(self):
        '''check the details for Jamb in Extras section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        lh_jamb = self.driver.find_element(*self.lh_jamb_loc).text
        lh_size = self.driver.find_element(*self.lh_size_loc).text
        rh_jamb = self.driver.find_element(*self.rh_jamb_loc).text
        rh_size = self.driver.find_element(*self.rh_size_loc).text
        self.driver.find_element(*self.extras_loc).click()
        # print(lh_jamb,lh_size,rh_jamb,rh_size)
        return  lh_jamb,lh_size,rh_jamb,rh_size

    @property
    def lh_jamb_type(self):
        '''check the list for LH JAMB Type'''
        sleep(1)
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_jamb_select).click()
        lh_jambtype_list = self.driver.find_element(*self.lh_jamb_select).text
        self.driver.find_element(*self.lh_jamb_select).click()
        self.driver.find_element(*self.extras_loc).click()
        print(lh_jambtype_list)
        return  lh_jambtype_list

    @property
    def lh_jamb_type(self):
        '''check the list for LH JAMB Type'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_jamb_select).click()
        lh_jambtype_list = self.driver.find_element(*self.lh_jamb_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_jambtype_list)
        return  lh_jambtype_list

    @property
    def lh_width_size(self):
        '''check the list for LH JAMB Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_size_width_btn).click()
        lh_width_size = self.driver.find_element(*self.lh_size_width_select).text
        self.driver.find_element(*self.lh_size_width_btn).click()
        self.driver.find_element(*self.extras_loc).click()
        print(lh_width_size)
        return  lh_width_size

    @property
    def lh_depth_size(self):
        '''check the list for LH JAMB Depth Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_size_depth_btn).click()
        lh_depth_size = self.driver.find_element(*self.lh_size_depth_select).text
        self.driver.find_element(*self.lh_size_depth_btn).click()
        self.driver.find_element(*self.extras_loc).click()
        print(lh_depth_size)
        return  lh_depth_size

    @property
    def rh_jamb_type(self):
        '''check the list for RH JAMB Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_jamb_select).click()
        rh_jambtype_list = self.driver.find_element(*self.rh_jamb_select).text
        self.driver.find_element(*self.rh_jamb_select).click()
        self.driver.find_element(*self.extras_loc).click()
        print(rh_jambtype_list)
        return  rh_jambtype_list

    @property
    def rh_width_size(self):
        '''check the list for RH JAMB Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_size_width_btn).click()
        rh_width_size = self.driver.find_element(*self.rh_size_width_select).text
        self.driver.find_element(*self.rh_size_width_btn).click()
        self.driver.find_element(*self.extras_loc).click()
        print(rh_width_size)
        return  rh_width_size

    @property
    def rh_depth_size(self):
        '''check the list for RH JAMB Depth Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_size_depth_btn).click()
        rh_depth_size = self.driver.find_element(*self.rh_size_depth_select).text
        self.driver.find_element(*self.rh_size_depth_btn).click()
        self.driver.find_element(*self.extras_loc).click()
        print(rh_depth_size)
        return  rh_depth_size

    @property
    def check_cover_type(self):
        '''check the details for Cover Type in Extras section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        lh_cover_type = self.driver.find_element(*self.lh_cover_type_loc).text
        lh_cover_width_size = self.driver.find_element(*self.lh_cover_width_size_loc).text
        lh_cover_coloure = self.driver.find_element(*self.lh_cover_colour_loc).text
        rh_cover_type = self.driver.find_element(*self.rh_cover_type_loc).text
        rh_cover_width_size = self.driver.find_element(*self.rh_cover_width_size_loc).text
        rh_cover_coloure = self.driver.find_element(*self.rh_cover_colour_loc).text
        self.driver.find_element(*self.extras_loc).click()
        # print(lh_cover_type,lh_cover_width_size,lh_cover_coloure,rh_cover_type,rh_cover_width_size,rh_cover_coloure)
        return  lh_cover_type,lh_cover_width_size,lh_cover_coloure,rh_cover_type,rh_cover_width_size,rh_cover_coloure

    @property
    def lh_cover_width_size(self):
        '''check the list for LH Cover Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_width_btn).click()
        lh_cover_width_select = self.driver.find_element(*self.lh_cover_width_select).text
        self.driver.find_element(*self.lh_cover_width_btn).click()
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_width_select)
        return  lh_cover_width_select

    @property
    def lh_cover_depth_size(self):
        '''check the list for LH Cover Depth Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_depth_btn).click()
        lh_cover_depth_select = self.driver.find_element(*self.lh_cover_depth_select).text
        self.driver.find_element(*self.lh_cover_depth_btn).click()
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_depth_select)
        return   lh_cover_depth_select

    @property
    def lh_cover_type(self):
        '''check the list for LH Cover Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_select).click()
        lh_cover_list = self.driver.find_element(*self.lh_cover_select).text
        self.driver.find_element(*self.lh_cover_select).click()
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_list)
        return  lh_cover_list

    @property
    def pelmet_type(self):
        '''Check the list for Pelmet Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.pelmet_type_select_loc).click()
        pelmet_type_list = self.driver.find_element(*self.pelmet_type_select_loc).text
        self.driver.find_element(*self.pelmet_type_select_loc).click()
        self.driver.find_element(*self.extras_loc).click()
        print(pelmet_type_list)
        return  pelmet_type_list

    @property
    def pelmet_height(self):
        '''Check the Height for Pelmet Height'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.pelmet_height_btn_loc).click()
        pelmet_size_height = self.driver.find_element(*self.pelmet_height_select_loc).text
        self.driver.find_element(*self.pelmet_height_btn_loc).click()
        self.driver.find_element(*self.extras_loc).click()
        print(pelmet_size_height)
        return  pelmet_size_height

    @property
    def pelmet_depth(self):
        '''Check the Depth for Pelmet Height'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.pelmet_depth_btn_loc).click()
        pelmet_size_depth = self.driver.find_element(*self.pelmet_depth_select_loc).text
        self.driver.find_element(*self.pelmet_depth_btn_loc).click()
        self.driver.find_element(*self.extras_loc).click()
        print(pelmet_size_depth)
        return  pelmet_size_depth

    @property
    def pelmet_colour(self):
        '''Check the list for Pelmet Colour'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.pelmet_colour_select_loc).click()
        pelmet_colour_list = self.driver.find_element(*self.pelmet_colour_select_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(pelmet_colour_list)
        return  pelmet_colour_list

    @property
    def windows_section(self):
        '''Check the elements in Windows Section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        windows_type = self.driver.find_element(*self.windows_type_loc).text
        no_windows = self.driver.find_element(*self.no_windoes_loc).text
        windows_colour = self.driver.find_element(*self.windows_colour_loc).text
        windows_position = self.driver.find_element(*self.windows_position_loc).text
        windows_custom = self.driver.find_element(*self.windows_custom_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(windows_type,no_windows,windows_colour,windows_position,windows_custom)
        return  windows_type,no_windows,windows_colour,windows_position,windows_custom

    @property
    def windows_type(self):
        '''Check the list for Windows Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.find_element(*self.windows_type_select_loc).click()
        windows_type_list = self.driver.find_element(*self.windows_type_select_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(windows_type_list)
        return  windows_type_list

    @property
    def default_no_windows(self):
        '''Check the default value for No. of Windows'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        default_no_windows = self.driver.find_element(*self.no_windows_box_loc).get_attribute('value')
        self.driver.find_element(*self.extras_loc).click()
        print(default_no_windows)
        return  default_no_windows

    @property
    def windows_position(self):
        '''Check the list for Windows Position'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.find_element(*self.windows_position_select_loc).click()
        windows_position_list = self.driver.find_element(*self.windows_position_select_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(windows_position_list)
        return  windows_position_list

    @property
    def hardware_colour_section(self):
        '''Check the elements in Hardware Colour Section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        hardware_colour_cate = self.driver.find_element(*self.hardware_colour_cate_loc).text
        hardware_colour = self.driver.find_element(*self.hardware_colour_loc).text
        window_frame_colour = self.driver.find_element(*self.window_frame_colour_loc).text
        hang_door_other = self.driver.find_element(*self.hang_door_other_loc).text
        fixing_type_other = self.driver.find_element(*self.fixing_type_other_loc).text
        noggins_other = self.driver.find_element(*self.noggins_other_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(hardware_colour_cate,hardware_colour,window_frame_colour,hang_door_other,fixing_type_other,noggins_other)
        return  hardware_colour_cate,hardware_colour,window_frame_colour,hang_door_other,fixing_type_other,noggins_other

    @property
    def windows_type_panellift(self):
        '''Check the Windows Type for Panel Lift door'''
        Select(self.driver.find_element(*self.door_type_select)).select_by_visible_text('Panel Lift-Safe')
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        windows_type_list_panel = self.driver.find_element(*self.windows_type_select_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(windows_type_list_panel)
        return  windows_type_list_panel

    @property
    def windows_position_custom(self):
        '''Check the Windows Position list for Custom-Aluminium'''
        Select(self.driver.find_element(*self.door_type_select)).select_by_visible_text('Panel Lift-Safe')
        self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.windows_type_select_loc).click()
        Select(self.driver.find_element(*self.windows_type_select_loc)).select_by_visible_text('Custom - Aluminium')
        # self.driver.find_element(*self.windows_position_select_loc).click()
        windows_position_custom= self.driver.find_element(*self.windows_position_select_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(windows_position_custom)
        return  windows_position_custom

if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Standard_Door_Extra(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_addstandarddoor()
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
        # login.pelmet_type
        # login.pelmet_height
        # login.pelmet_depth
        # login.pelmet_colour
        # login.windows_section
        # login.windows_type
        # login.default_no_windows
        # login.windows_position
        # login.hardware_colour_section
        # login.windows_type_panellift
        # login.windows_position_custom