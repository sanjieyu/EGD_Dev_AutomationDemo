# Author:Yi Sun(Tim) 2025-10-15

'''OptiLift Doors Production Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.production_wa import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class OptiLift_Production(Production_WA):

    '''loc for each section in this page'''
    order_tab_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/a')
    rollforming_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]/a')
    assembly_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/ul/li[3]/a')
    modifications_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/ul/li[4]/a')
    extras_orders_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/ul/li[5]/a')
    qc_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/ul/li[6]/a')

    '''loc for "Order" section in this page'''
    number_doors_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/h5/b[1]')
    proposal_no_loc = (By.XPATH,
                       '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/thead/'
                       'tr/th[1]/div/span')
    client_name_loc = (By.XPATH,
                       '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/thead/'
                       'tr/th[2]/div/span')
    supply_type_loc = (By.XPATH,
                       '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/thead/'
                       'tr/th[3]/div/span')
    door_no_loc = (By.XPATH,
                   '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/thead/tr/'
                   'th[4]/div/span')
    status_loc = (By.XPATH,
                  '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/thead/tr/'
                  'th[5]/div/span')
    extraorders_doc_loc = (By.XPATH,
                           '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/'
                           'thead/tr/th[6]/div/span')
    save_changes_order_btn_loc = (By.ID, 'saveSingleSkinOrderData')
    first_orderid_loc = (By.XPATH,
                         '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/table/'
                         'tbody/tr[1]/td[1]/a')
    search_order_box_loc = (By.ID, 'SingleSkinOrderSearchInput')
    searched_order_status_loc = (By.XPATH, "//select[contains(@id, '_status')]")

    '''loc for "Rollforming" section in this page'''
    number_doors_roll_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/h5/b[1]')
    reschedule_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/label')
    date_filter_loc = (By.ID, 'reschedule-from')
    apply_btn = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/input')
    search_job_box = (By.ID, 'search-door')
    search_job_btn = (
    By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/button')
    save_changes_rollforming_btn = (By.ID, 'saveSingleSkinRollingData')
    table_frame_loc = (
    By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]')

    proposal_num_searched_loc = (By.XPATH,
                                 '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/'
                                 'div[38]/div/div/div[2]/ul/li/span[1]')
    searched_popup_loc = (By.CLASS_NAME, 'modal-dialog')
    searched_result_job_loc = (By.XPATH,
                               '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[37]/'
                               'div/div/div[2]/ul/li')
    actual_height_loc = (By.XPATH,
                         '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[36]/div/'
                         'div/div/div/table/tbody/tr[1]/td[10]')

    '''loc for "Assembly" section in this page'''
    number_doors_assembly_loc = (
    By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/h5/b[1]')
    prop_no_loc = (By.XPATH,
                   '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[2]/div/div/table/thead/'
                   'tr/th[1]/div/span')
    door_no_assembly_loc = (By.XPATH,
                            '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[2]/div/div/table/'
                            'thead/tr/th[2]/div/span')
    status_assembly_loc = (By.XPATH,
                           '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[2]/div/div/table/'
                           'thead/tr/th[13]/div/span')
    save_assembly_btn_loc = (By.ID, 'saveSingleSkinAssemblyData')

    '''loc for "Modification" section in this page'''
    number_doors_modification_loc = (
    By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[1]/div[1]/h5/b[1]')
    prop_no_modification_loc = (By.XPATH,
                                '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[2]/div[2]/div/div/'
                                'table/thead/tr/th[1]/div/span')
    door_colour_loc = (By.XPATH,
                       '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[2]/div[2]/div/div/table/'
                       'thead/tr/th[4]/div/span')
    extradoc_modification_loc = (By.XPATH,
                                 '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[2]/div[2]/div/'
                                 'div/table/thead/tr/th[12]/div/span')
    save_modification_btn_loc = (By.ID, 'saveSingleSkinModificationData')

    '''loc for "Extra Orders" section in this page'''
    number_doors_extra_loc = (
    By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[1]/div[1]/h5/b[1]')
    prop_no_extra_loc = (By.XPATH,
                         '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/div[2]/div/div/table/'
                         'thead/tr/th[1]/div/span')
    colour_category_loc = (By.XPATH,
                           '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/div[2]/div/div/table/'
                           'thead/tr/th[5]/div/span')
    extradoc_extra_loc = (By.XPATH,
                          '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/div[2]/div/div/table/'
                          'thead/tr/th[13]/div/span')
    save_extrasorders_btn_loc = (By.ID, 'saveSingleSkinExtrasData')

    '''loc for "Paint" section in this page'''
    number_doors_paint_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[1]/div[1]/h5/'
                                       'b[1]')
    prop_no_paint_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div/div/'
                                  'table/thead/tr/th[1]/div/span')
    actual_height_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div/div/'
                                  'table/thead/tr/th[4]/div/span')
    status_paint_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div/div/'
                                 'table/thead/tr/th[11]/div/span')
    save_paint_btn_loc = (By.ID,'saveSinglePaintData')

    '''loc for "Painted" section in this page'''
    number_doors_painted_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[7]/div[1]/div[1]/'
                                         'h5/b[1]')
    prop_no_painted_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[7]/div[2]/div[2]/div/'
                                    'div/table/thead/tr/th[1]/div/span')
    number_panels_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[7]/div[2]/div[2]/div/'
                                  'div/table/thead/tr/th[3]/div/span')
    status_painted_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[7]/div[2]/div[2]/div/'
                                   'div/table/thead/tr/th[11]/div/span')
    save_painted_btn_loc = (By.ID, 'saveSinglePaintedData')

    '''loc for "QC" section in this page'''
    number_doors_qc_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[1]/div[1]/h5/b[1]')
    prop_no_qc_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div/div/'
                               'table/thead/tr/th[1]/div/span')
    actual_width_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div/div/'
                                 'table/thead/tr/th[5]/div/span')
    status_qc_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div/div/table/'
                              'thead/tr/th[11]/div/span')
    qc_fail_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[1]/div[3]/div/label')
    qc_pass_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[1]/div[4]/div/label')
    qc_fail_radiobox_loc = (By.ID,'SSQCFailRadiobutton')
    qc_pass_radiobox_loc = (By.ID, 'SSQCPassRadiobutton')
    save_qc_btn_loc = (By.ID, 'saveSingleQCData')

    def go_optilift(self):
        '''Switch to OptiLift section in Production'''
        self.driver.find_element(*self.optilift_doors_loc).click()
        sleep(2)

    def go_rollforming(self):
        '''Switch to Rollforming screen'''
        self.driver.find_element(*self.rollforming_loc).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.number_doors_roll_loc))


    @property
    def check_optilift_doors_section(self):
        '''check each section in OptiLift Doors page'''
        order = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.order_tab_loc)).text
        rollforming = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.rollforming_loc)).text
        assembly = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.assembly_loc)).text
        modifications = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.modifications_loc)).text
        extras_orders = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.extras_orders_loc)).text
        qc = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.qc_loc)).text
        print (order,assembly,modifications,extras_orders,qc)
        return order,assembly,modifications,extras_orders,qc

    @property
    def get_first_orderid(self):
        '''get the first order's job id, this fun is for change_quote_status module'''
        first_order_id = self.driver.find_element(*self.first_orderid_loc).text
        print(first_order_id)
        return  first_order_id

    @property
    def check_order_table(self):
        '''check each column in Order table'''
        self.driver.implicitly_wait(10)
        number_doors = self.driver.find_element(*self.number_doors_loc).text
        proposal_no = self.driver.find_element(*self.proposal_no_loc).text
        client_name = self.driver.find_element(*self.client_name_loc).text
        supply_type = self.driver.find_element(*self.supply_type_loc).text
        door_no = self.driver.find_element(*self.door_no_loc).text
        status = self.driver.find_element(*self.status_loc).text
        extraorders_doc = self.driver.find_element(*self.extraorders_doc_loc).text
        print (number_doors,proposal_no,client_name,supply_type,door_no,status,extraorders_doc)
        return number_doors,proposal_no,client_name,supply_type,door_no,status,extraorders_doc

    @property
    def check_rollforming_table(self):
        '''check each elements in Rollforming table'''
        self.driver.find_element(*self.rollforming_loc).click()
        number_doors = WebDriverWait(self.driver, 180).until(
            EC.visibility_of_element_located(self.number_doors_roll_loc))
        number_doors_roll = number_doors.text
        reschedule = self.driver.find_element(*self.reschedule_loc).text
        print (number_doors_roll,reschedule)
        return  number_doors_roll,reschedule

    @property
    def check_rollforming_date_filter(self):
        '''check Date Filter fun in Rollforming table'''
        date_filter = WebDriverWait(self.driver, 180).until(
            EC.visibility_of_element_located(self.date_filter_loc))
        if date_filter.is_displayed():
            print('true')
            return True
        else:
            return False

    @property
    def check_rollforming_save(self):
        '''check Save Changes button in Rollforming table'''
        save_changes_btn = WebDriverWait(self.driver, 180).until(
            EC.visibility_of_element_located(self.save_changes_rollforming_btn))
        if save_changes_btn.is_displayed() and save_changes_btn.is_enabled():
            print("Button is present and visible")
            return True
        else:
            print('Button is not present or visible')
            return False

    @property
    def check_rollforming_tableframe(self):
        '''check Table display in Rollforming screen'''
        table_frame = WebDriverWait(self.driver,180).until(EC.visibility_of_element_located(self.table_frame_loc))
        if table_frame.is_displayed():
            print('yes')
            return True
        else:
            print('no')
            return False


    @property
    def check_assembly_table(self):
        '''check each elements in Assembly table'''
        self.driver.find_element(*self.assembly_loc).click()
        self.driver.implicitly_wait(10)
        number_doors_assembly = WebDriverWait(self.driver,180).until(EC.visibility_of_element_located
                                                                     (self.number_doors_assembly_loc)).text
        prop_no = WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located(self.prop_no_loc)).text
        door_no_assembly = WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located
                                                                 (self.door_no_assembly_loc)).text
        status_assembly = WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located
                                                                (self.status_assembly_loc)).text
        print (number_doors_assembly,prop_no,door_no_assembly,status_assembly)
        return  number_doors_assembly,prop_no,door_no_assembly,status_assembly

    @property
    def check_assembly_save(self):
        '''check the Save fun in Assembly table'''
        save_assembly_btn = self.driver.find_element(*self.save_assembly_btn_loc)
        if save_assembly_btn.is_enabled:
            return True
        else:
            return False

    @property
    def check_modification_table(self):
        '''check each elements in Modification table'''
        self.driver.find_element(*self.modifications_loc).click()
        self.driver.implicitly_wait(10)
        number_doors_modification = WebDriverWait(self.driver,100).until(EC.visibility_of_element_located
                                                                         (self.number_doors_modification_loc)).text
        prop_no_modification = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located
                                                                    (self.prop_no_modification_loc)).text
        door_colour = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located
                                                           (self.door_colour_loc)).text
        extradoc_modification = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                                                     (self.extradoc_modification_loc)).text
        print (number_doors_modification,prop_no_modification,door_colour,extradoc_modification)
        return  number_doors_modification,prop_no_modification,door_colour,extradoc_modification

    @property
    def check_modification_save(self):
        '''check the Save fun in Modification table'''
        save_modification_btn = self.driver.find_element(*self.save_modification_btn_loc)
        if save_modification_btn.is_enabled:
            return True
        else:
            return False


    @property
    def check_paint_table(self):
        '''check each elements in Paint table'''
        self.driver.find_element(*self.paint_loc).click()
        self.driver.implicitly_wait(10)
        number_doors_paint = WebDriverWait(self.driver,100).until(EC.visibility_of_element_located
                                                                  (self.number_doors_paint_loc)).text
        prop_no_paint = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located
                                                                    (self.prop_no_paint_loc)).text
        actual_height = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located
                                                           (self.actual_height_loc)).text
        status_paint = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                                                     (self.status_paint_loc)).text
        print (number_doors_paint,prop_no_paint,actual_height,status_paint)
        return  number_doors_paint,prop_no_paint,actual_height,status_paint

    @property
    def check_paint_save(self):
        '''check the Save fun in Paint table'''
        save_paint_btn = self.driver.find_element(*self.save_paint_btn_loc)
        if save_paint_btn.is_enabled:
            return True
        else:
            return False

    @property
    def check_painted_table(self):
        '''check each elements in Painted table'''
        self.driver.find_element(*self.painted_loc).click()
        self.driver.implicitly_wait(10)
        number_doors_painted = WebDriverWait(self.driver,100).until(EC.visibility_of_element_located
                                                                    (self.number_doors_painted_loc)).text
        prop_no_painted = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located
                                                                    (self.prop_no_painted_loc)).text
        number_panel_painted = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located
                                                           (self.number_panels_loc)).text
        status_paint = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                                                     (self.status_painted_loc)).text
        print (number_doors_painted,prop_no_painted,number_panel_painted,status_paint)
        return  number_doors_painted,prop_no_painted,number_panel_painted,status_paint

    @property
    def check_painted_save(self):
        '''check the Save fun in Painted table'''
        save_painted_btn = self.driver.find_element(*self.save_painted_btn_loc)
        if save_painted_btn.is_enabled:
            return True
        else:
            return False

    @property
    def check_extraorder_table(self):
        '''check each elements in Extra Order table'''
        self.driver.find_element(*self.extras_orders_loc).click()
        self.driver.implicitly_wait(10)
        number_doors_extraorder = WebDriverWait(self.driver,180).until(EC.visibility_of_element_located
                                                                       (self.number_doors_extra_loc)).text
        prop_no_extra = WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located
                                                             (self.prop_no_extra_loc)).text
        colour_category = WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located
                                                               (self.colour_category_loc)).text
        extradoc_extra = WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located
                                                              (self.extradoc_extra_loc)).text
        print (number_doors_extraorder,prop_no_extra,colour_category,extradoc_extra)
        return  number_doors_extraorder,prop_no_extra,colour_category,extradoc_extra

    @property
    def check_extrasorders_save(self):
        '''check the Save fun in Modification table'''
        save_extrasorders_btn = self.driver.find_element(*self.save_extrasorders_btn_loc)
        if save_extrasorders_btn.is_enabled:
            return True
        else:
            return False

    @property
    def check_qc_table(self):
        '''check each elements in QC table'''
        self.driver.find_element(*self.qc_loc).click()
        self.driver.implicitly_wait(10)
        number_doors_qc = (WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(self.number_doors_qc_loc))
                           .text)
        prop_no_qc = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.prop_no_qc_loc)).text
        actual_width = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.actual_width_loc)).text
        status_qc = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.status_qc_loc)).text
        print (number_doors_qc,prop_no_qc,actual_width,status_qc)
        return  number_doors_qc,prop_no_qc,actual_width,status_qc

    @property
    def check_qc_save(self):
        '''check the Save fun in QC table'''
        save_qc_btn = self.driver.find_element(*self.save_qc_btn_loc)
        if save_qc_btn.is_enabled:
            return True
        else:
            return False

    @property
    def check_qc_table_new(self):
        '''check qc pass and qc fail radio box in QC table'''
        qc_fail = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(self.qc_fail_loc)).text
        qc_pass = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.qc_pass_loc)).text
        print (qc_fail,qc_pass)
        return  qc_fail,qc_pass

    @property
    def check_qc_fail(self):
        '''check qc fail radio box status'''
        qc_fail_radiobox = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(self.qc_fail_radiobox_loc))
        if qc_fail_radiobox.is_selected():
            print('selected, correct')
            return  True
        else:
            print("not selected, wrong")
            return False

    @property
    def check_qc_pass(self):
        '''check qc pass radio box status'''
        qc_pass_radiobox = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(self.qc_pass_radiobox_loc))
        if qc_pass_radiobox.is_selected():
            print('selected, wrong')
            return  False
        else:
            print("not selected, correct")
            return True


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// )
    driver.implicitly_wait(10)

    login = OptiLift_Production(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_production_wa()
    login.go_optilift()
    # login.check_optilift_doors_section
    # login.check_order_table
    # login.check_rollforming_table
    # login.check_rollforming_date_filter
    # login.check_rollforming_tableframe
    # login.check_assembly_table
    # login.check_assembly_save
    # login.check_modification_table
    # login.check_paint_table
    # login.check_paint_save
    # login.check_painted_table
    # login.check_painted_save
    # login.check_extraorder_table
    login.check_qc_table

