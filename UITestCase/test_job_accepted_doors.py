# Author:Yi Sun(Tim) 2024-11-13

'''Test Job Accepted Page'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.job_accepted_doors import *

class Job_Accepted_Test(unittest.TestCase,Job_Accepted):
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
        cls.login.login(cls.admin_username, cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.go_jobaccepted = Job_Accepted(cls.driver)
        cls.go_jobaccepted.go_job_accepted()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_job_accepted_ui_001(self):
        '''Verify the URL for Job Accepted screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual("http://aabb/Quote/JobExcepted",self.check_jobaccepted_url)

    def test_job_accetped_ui_002(self):
        '''Verify the title for Job Accepted screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual("Job Accepted Quotes",self.check_jobaccepted_title)

    def test_job_accetped_ui_003(self):
        '''Verify the elements for Details section'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Client Details","Client Name","Contact Number","Location","Suburb",
                          "Site Address","Quote Information","Proposal No","User"),self.check_details)

    def test_job_accetped_ui_004(self):
            '''Verify the title for Job Accepted screen'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.search_quotes_btn_loc)

    def test_job_accetped_ui_005(self):
            '''Verify the title for Job Accepted screen'''
            self.driver.implicitly_wait(2)
            self.assertIn("Results Found", self.check_results_found)

    def test_job_accetped_ui_006(self):
        '''Verify each column of Job Accepted'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Proposal", "Account", "Payment Type", "Client Name", "Site Address",
                          "Door No", "Sale Amount", "Deposit", "Door Status"), self.check_columns)

    def test_job_accetped_ui_007(self):
        '''Verify the Save Changes button in Job Accepted screen'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_save_button)

if __name__ == "__main__":
    unittest.main(verbosity=2)