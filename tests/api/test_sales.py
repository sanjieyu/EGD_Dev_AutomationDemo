# Author:Yi Sun(Tim) 2023-8-20

'''API Testing for Sales Module'''

import requests
import json
import unittest
from utils.read_excel_title import *
from requests.sessions import Session

class SALES_API(unittest.TestCase,ExcelData):
    def setUp(self) -> None:
        global set_cookie
        global set_cookie_admin
        self.data = ExcelData().read_excel()
        self.session = Session()
        self.url = self.data[0]['Endpoint']
        # print('url is:',self.url)
        send_cookie = '__RequestVerificationToken=awpTmu0IkoW-COSacwuXVwRsu4QmRPwCWzd0LKiKOblXVKy2D7qQaWe3n3hpWPXbFxbo447Z3vbTl-yLNO9B6y0HizsBuD8AeVt0j5zqK2c1; ASP.NET_SessionId=ezbhduyl3qcviptvwqms5fpx'
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie":send_cookie,
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
            "Host":"egd2.sighte.com",
        }
        self.payload = {
            # "ReturnUrl": "%2F",
            "__RequestVerificationToken":"ovrBUpoHsDVXgaieJrrqGI-JIL5V_sMOVGwWepto-HDU-G12MGztWa0tO3pMilmfSQygyDR3J008FbBhcUYYcwUwNb3tNR6AxJHNoLzQ_dI1",
            "Email":"ysun%40ecogaragedoors.com.au",
            "Password":"Tims%40123",
            "RememberMe":"false"
        }
        # self.data1 = self.data[0]['payload']
        self.r = requests.request(method=self.data[0]['method'], url=self.url, headers=self.header, data=self.payload)
        if self.r.status_code == 200:
            cookies = self.r.cookies
            print('cookie is:',cookies)
            application_cookie = cookies.get('.AspNet.ApplicationCookie')
            print('applicate cookie is:',application_cookie)
        else:
            print("login failed with code:",self.r.status_code)

        # set_cookie_admin = send_cookie + '.AspNet.ApplicationCookie' + application_cookie
        # print("set cookie is:",set_cookie_admin)
        # print('status code:',self.r.status_code)
        # cookie_info = self.r.cookies.get_dict()
        # print('cookie_info:',cookie_info)
        # cookie_info_str = json.dumps(cookie_info)

        # set_cookie1 = self.r.headers.get('Set-Cookie')
        set_cookie = "__RequestVerificationToken=m43Y9WkT8Vh0b-LTcZFEd5BdcgDTA7vtDoUsGK42QX2gWFNyfMEAs6Ff0FSrseKAW4NoS7-ZeCsF68tIBXOpCUhDHMMeJVZJy4uIuexKKiY1; .AspNet.ApplicationCookie=DlvlLiI0Rq1_7uSKnY-Fd7vKlVFDkWdsHLYZZWIfljgtxzOrNiTWE0LKJtiIC5Mq33Adb7FnUGliN0uinIocx792cZcWse63VWt5P07BOawUHwCCooGwsnV7H-3dU3xXrB_M6Cydm1hGcBRHsWWeTMjlDr4Uq8U5MJSSxSVNPunROq1FXs2xT_Z7UHoUxBQuX_GLaI-k8s2tbEWJEcekk9EOC5LiuxmIIZUvQRB3kFCqilAwaN7j9f97fD8EsoAQ6_GnKEtI3H7kEEs2eq2PZGsJoXH1IGdKGQED6MHUtdcH0lSsruEYvmv5r9IQMSkn41tyOQb-ibhjdodJVTfIGkHL5ZK1gEExhAvcKqZg1vu3RfQhP6bsjC7qbXmFPFjZQBKWyBPaUZxwIsegK_TQoMgG-CBGTrg6V-9v8JFb5n11gKXQO0Elsg5dUmmjsRHYo_IqdL7US5h7A3nP0Uxm8Nk7nrMupgqIpXAeExpAHKcXjvfFzs-0cl3nQIwB1KWtVxMpb2nDrdTNKElzqDLuyseQtTbAQ0MslUaX9GvQJJcRJvU74x7lfgVuQ8LXBxgU"
        # set_cookie_admin = "__RequestVerificationToken=m43Y9WkT8Vh0b-LTcZFEd5BdcgDTA7vtDoUsGK42QX2gWFNyfMEAs6Ff0FSrseKAW4NoS7-ZeCsF68tIBXOpCUhDHMMeJVZJy4uIuexKKiY1; .AspNet.ApplicationCookie=5XhUvGuBSIfsIe-rKw9ihVLtfWzQOG0hdckJLBpRRgOgV-igEQxGb-ugROj0PRbU52dvS3bZ1HpmLvkP4I5Pgm23_PAt24WOiQ5w8x7qH5KeKZNiUoHonOIWdXsFx5DZlY1IOCJ8zKeXAkpkzgEXRBGDRyeqlW4YF-aOKz-Ah3Aw0X3YrwB1F0kc_BHGAdldbzMATR_NWalT-27IoyJ3fiFkCFwORnrPAhy5uaWYp4THWuWRDH9iiwIS9rWWaZAy2_PLjswdICVOtKBrvzf7GQyX4JjcMxvLJ76yb6kXmUWRnZCnXuWrdjdW7l_BE4ayUMVaazW1PLqQdWCtnal4TXIq9etntngn3OAsykTVNOjwgx_GMj-4fAWBkOJZD-Ls0WdhdPuOoyhem1NZotPf5wF6PUfPDT7mog4lFr4ssXaOCA8KZGGeTSGyTM49SRkew4_Sx6u2pBs6Inttw2EQ6AzvnwA1VfnB9hu9BdsumwvLpH5_6Mk44C3sbLl8y8gCi7IX1Ht7N5e7UwTu6FZLXs2E9z1hKEMZzpg5q4biOl4"
        set_cookie_admin_old = "__RequestVerificationToken=awpTmu0IkoW-COSacwuXVwRsu4QmRPwCWzd0LKiKOblXVKy2D7qQaWe3n3hpWPXbFxbo447Z3vbTl-yLNO9B6y0HizsBuD8AeVt0j5zqK2c1; ASP.NET_SessionId=ezbhduyl3qcviptvwqms5fpx; .AspNet.ApplicationCookie=ROPkiDEaYai8dBQTQsGOa778cfHkMSvAskn3Gv86lhhoOHQ1YsBzHXvzK02dgSKMfPf7bDjrq90btPLzhgfkR6-OAFvc0DBa4gWDPY0JUSCsT7Qobdtnsa3f2M0kJJkZGXU-S6YcBDmFXWPJs6opRex64bAK0chKucaBNVi2Gia_oGRgrffAbhx9RGc0LLwYYVo40cA38P8HfTHBgi232-jEVchjbQsZN5Z2UXkphgE_Si6sga6_b9dKEhwpUwh-nwkkvDmWwlVQaTWAzhG6ITWWZZC-iNpfjicNlaGoPXWUqayrzpeZAhQBTYb13rM6NzK7lQilqNEHYAisIt6sfON6qJpC_LFg9rcIgrTQbeK-M_7PYfebGYSu3Aq7hix0E0jpwbCw8Kj8hU5Ydh9Acer-8eXzmdkR4PbhF5fk9gKxM9Mpv3Jw_hX4mSqpNJMcrcHQ-7ZVNB4xvmAzL0BaBqD7X2AOk0hB3ooaMULJ40t4V-xameSrB_R_OyLNEKevC14tNCAOeTPeNzPVy2im2lXersypSLTXcRDyRVZ3veTh8n6qL7HOnnnjNfa5s1Kr"
        set_cookie_admin_old1 = "__RequestVerificationToken=r2d38XQFKpWUhmqi_aQEJ_fGJuikEEyBvo_v7vBjuNpOZJmxIUr_PhVEbU0oQNoLd_AreNin0nafL07edkNqnRsOR1YztiLC8CchB5FB1Os1; .AspNet.ApplicationCookie=rx1G0H6h8aaGVXdQKO4pC8csjpYci1895sLtKVIoo-ieslHOS_7o9mOW6pbfS6r4Ukzp8yUP9DJEmAlMy2Wb29g0MK8pF7_vz3q1UKZKSNApnOFmTdv0EDKIL9-vH-V9q5Jc5vhmUOfOBND3s4ABJassk0CNqEDcXz728KcEVDnGUqMeN-sqRl4UDS2h4-wyfZMtQSbxeYolyCZq01AHF19Jmn5JFIv3nEOIiUqO6tGArfiltH8OVuzGfOok0wCOm9iUJLMe0J2w-BDpz24B9u76cvWUFHSJoAJ8cXwIjIVvyCVd3NJ9bi9fO9GEpoWwwSRcO7EbY3mehkxxzROxPY7HlUxaiVRi8A16AP0qxb1DSLpVwVycVr0rbte-6dEkueC60oqM1o0Uodbst96gFE6wpJ6uMKG8hqQPKqM2tatT5bUanqwQ6f4ZCGmfFs2GRQeQ8rBK5rCOwJRHfVoyRg0siXx4l4fLs53GBVmd1NhMWStHSF51hJqmAQ7F48ydgjdTdcMwacVjbA2M3MqnAn7HkRCmNyzoYlN7mrIr4-o"
        set_cookie_admin = "__RequestVerificationToken=PZH0nyskGi3gTCCkvNZ6HoqEHI8iN2T9Djr6mjivOmFVZl-9lXO2ZVgr4TiMtwMTW72NTf4GKJf6HwEfLTltIKPQDGuaHtDV8q7tih9EXUc1; ASP.NET_SessionId=lnlvakqwakf2f23imuqvsnrf; .AspNet.ApplicationCookie=ilTtoX7P05lLRVikQjXERmEIE7Q2FkOHhbo3DYNDkaO875ueWW1B7gigbLSM03LDIKgjiahNHu2k5OKmwngWp-ttnxd5jp3iSyvR18lM0KvwiTuWoo5w9kOfdLs0fkLKFcgvWL5d3YYsk3YIYNyEtX8lU-F961sya92Eib2iTZLYM5gWAleoShGKPON_cmXWp2tXHs1D1a0HlALXgPRrq4gE7ugDQg8KG_L73Fag9-Ez6ngIUqVVfRnK4LsVdh_myzKKiB0WDHV-sG-nSvWLpT8FV7SQBG5jxisXG64oY49cdmKx9wZD_qQCkXhjRLSwKnkcO_PSycsxuEHn35L6apCUUuBHPKZVRu5vlwx8wS3_FSO0XLcVsQjFi7fMpY-otP5E9ia5UmPebCm6-ZsnoaATVnucsRjre02a7kwvTxpbIrnbCWbMJ-tnf5h_uA-rOLimesMMfFhtVH-CXK1bYQKRg5N9RaQPfSuFBhDwE92afQ-GNPhUNvblnC-ddbyzg9cxmKp2OTZ_hX_mXx4nhmzNt_BysMIataZtGVGlDLMSa5o3xAKYm7RNzooCHrJ4"
        # print('set_cookie is:',set_cookie)
        # login_info =
        # return set_cookie_admin

    def tearDown(self) -> None:
        pass

    def test_sales001(self):
        '''Verify the status code for the specified quote'''
        self.url = self.data[1]['Endpoint']
        print('url is:',self.url)
        self.header = {
            "content-type":"application/json",
        }
        self.r = requests.request(method=self.data[1]['method'], url=self.url, headers=self.header)
        self.assertEqual(self.data[1]['return code'],self.r.status_code)

    def test_sales002(self):
        '''Returns an array of doors data for the specified quote'''
        self.url = self.data[2]['Endpoint']
        self.header = {
            # "content-type":"application/json",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[2]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertIn(self.data[2]['response'],self.r.text)

    def test_sales003(self):
        '''verify the status code for Returns data for one specified door'''
        self.url = self.data[3]['Endpoint']
        self.header = {
            "content-type":"application/json",
        }
        self.r = requests.request(method=self.data[3]['method'], url=self.url, headers=self.header)
        self.assertEqual(self.data[3]['return code'],self.r.status_code)
    #
    def test_sales004(self):
        '''verify the Returns data for one specified door'''
        self.url = self.data[4]['Endpoint']
        self.header = {
            # "content-type":"application/json",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[4]['method'], url=self.url, headers=self.header,data=self.data[4]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[4]['response'],self.r.text)

    def test_sales005(self):
        '''verify the status code for Updates Height of one specific door'''
        self.url = self.data[5]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[5]['method'], url=self.url, headers=self.header,data=self.data[5]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[5]['return code'],self.r.status_code)

    def test_sales006(self):
        '''verify the sUpdates Height of one specific door'''
        self.url = self.data[6]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[6]['method'], url=self.url, headers=self.header,data=self.data[6]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[6]['response'],self.r.text)

    def test_sales007(self):
        '''verify the status code for Updates Width of one specific door'''
        self.url = self.data[7]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[7]['method'], url=self.url, headers=self.header,data=self.data[7]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[7]['return code'],self.r.status_code)
    # #
    def test_sales008(self):
        '''verify the sUpdates Width of one specific door'''
        self.url = self.data[8]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[8]['method'], url=self.url, headers=self.header,data=self.data[8]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[8]['response'],self.r.text)
    #
    @unittest.skip
    def test_sales009(self):
        '''verify the status code for Updates details of one specific door'''
        self.url = self.data[9]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.payload = {
            "DoorData": "%5B%7B%22InstallTypeListStandard%22%3A%5B%7B%22Disabled%22%3Afalse%2C%22Group%22%3Anull%2C%22Selected%22%3Afalse%2C%22Text%22%3A%22Please+Select%22%2C%22Value%22%3A%220%22%7D%2C%7B%22Disabled%22%3Afalse%2C%22Group%22%3Anull%2C%22Selected%22%3Afal",
            "QuoteId":"100569",
            # "SitePhotosData":"",
        }
        self.r = requests.request(method=self.data[9]['method'], url=self.url, headers=self.header,json=self.data[9]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[9]['return code'],self.r.status_code)

    def test_sales010(self):
        '''verify the status code for Updates all doors of the specific quote. Marks whether each door requires Measure (or Technician Measure)'''
        self.url = self.data[10]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[10]['method'], url=self.url, headers=self.header,data=self.data[10]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[10]['return code'],self.r.status_code)


    def test_sales011(self):
        '''verify the status code for Quotation page'''
        self.url = self.data[11]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[11]['method'], url=self.url, headers=self.header,data=self.data[11]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[11]['return code'],self.r.status_code)

    def test_sales012(self):
        '''verify the status code for Recalculates price of the specified door'''
        self.url = self.data[12]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[12]['method'], url=self.url, headers=self.header,data=self.data[12]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[12]['return code'],self.r.status_code)

    def test_sales013(self):
        '''verify the status code for Returns an array of quote documents details'''
        self.url = self.data[13]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[13]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[13]['return code'],self.r.status_code)

    def test_sales014(self):
        '''verify Returns an array of quote documents details'''
        self.url = self.data[14]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[14]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertIn(self.data[14]['response'],self.r.text)

    def test_sales015(self):
        '''verify the status code for Returns an array of quote documents (including Schedule and Production Sheets which actually belong to door) '''
        self.url = self.data[15]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[15]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[15]['return code'],self.r.status_code)
    #
    def test_sales016(self):
        '''verify Returns an array of quote documents (including Schedule and Production Sheets which actually belong to door)'''
        self.url = self.data[16]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[16]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertIn(self.data[16]['response'],self.r.text)

    def test_sales017(self):
        '''verify the status code for Returns an array of door documents details '''
        self.url = self.data[17]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[17]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[17]['return code'],self.r.status_code)

    def test_sales018(self):
        '''verify Returns an array of door documents details'''
        self.url = self.data[18]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[18]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertIn(self.data[18]['response'],self.r.text)

    def test_sales019(self):
        '''verify the status code for Recalculates payment terms based on the quoted and sale prices '''
        self.url = self.data[19]['Endpoint']
        self.header = {
            "Connection":"keep-alive",
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin,
            "Origin":"http://egd2.sighte.com",
            "Referer":"http://egd2.sighte.com/Quote/Final/90578",
            "Host":"egd2.sighte.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
            "X-Requested-With":"XMLHttpRequest",
        }
        self.r = requests.request(method=self.data[19]['method'], url=self.url, headers=self.header,data=self.data[19]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[19]['return code'],self.r.status_code)

    @unittest.skip
    def test_sales020(self):
        '''verify Recalculates payment terms based on the quoted and sale prices'''
        self.url = self.data[20]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[20]['method'], url=self.url, headers=self.header,data=self.data[20]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[20]['response'],self.r.text)

    def test_sales021(self):
        '''verify the status code for Copies specified quote '''
        self.url = self.data[21]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[21]['method'], url=self.url, headers=self.header,data=self.data[21]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[21]['return code'],self.r.status_code)


    def test_sales022(self):
        '''verify the status code for Increment proposal number '''
        self.url = self.data[22]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[22]['method'], url=self.url, headers=self.header,data=self.data[22]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[22]['return code'],self.r.status_code)

    def test_sales023(self):
        '''verify the Increment proposal number '''
        self.url = self.data[23]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[23]['method'], url=self.url, headers=self.header,data=self.data[23]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[23]['response'],self.r.text)

    def test_sales024(self):
        '''verify the status code for Saves changes to status of the quote. '''
        self.url = self.data[24]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[24]['method'], url=self.url, headers=self.header,data=self.data[24]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[24]['return code'],self.r.status_code)

    def test_sales025(self):
        '''verify the status code for Calculate Actual Height for the specified door '''
        self.url = self.data[25]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[25]['method'], url=self.url, headers=self.header,data=self.data[25]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[25]['return code'],self.r.status_code)

    def test_sales026(self):
        '''verify the Calculate Actual Height for the specified door '''
        self.url = self.data[26]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[26]['method'], url=self.url, headers=self.header,data=self.data[26]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[26]['response'], int(self.r.text))

    def test_sales027(self):
        '''verify the status code for Calculate Actual Width for the specified door'''
        self.url = self.data[27]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[27]['method'], url=self.url, headers=self.header,data=self.data[27]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[27]['return code'],self.r.status_code)

    def test_sales028(self):
        '''verify the Calculate Actual Width for the specified door'''
        self.url = self.data[28]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[28]['method'], url=self.url, headers=self.header,data=self.data[28]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[28]['response'], int(self.r.text))

    def test_sales029(self):
        '''verify the status code for GetEmailReceiversList(from the Quotation page)'''
        self.url = self.data[29]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[29]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[29]['return code'],self.r.status_code)

    def test_sales030(self):
        '''verify the GetEmailReceiversList(from the Quotation page)'''
        self.url = self.data[30]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[30]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertIn(self.data[30]['response'], self.r.text)

    @unittest.skip
    def test_sales031(self):
        '''verify the status code for Sends email (from the Quotation page)'''
        self.url = self.data[31]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[31]['method'], url=self.url, headers=self.header,data=self.data[31]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[31]['return code'],self.r.status_code)

    @unittest.skip
    def test_sales032(self):
        '''verify the status code for Sends email with Schedule sheet. Note: doesn't work in DEV as mail server is not installed'''
        self.url = self.data[32]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[32]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[32]['return code'],self.r.status_code)

    def test_sales033(self):
        '''verify the status code for Returns Schedule sheet from 'generate-nightly-schedule-sheet' call'''
        self.url = self.data[33]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[33]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[33]['return code'],self.r.status_code)


    @unittest.skip
    def test_sales034(self):
        '''verify the status code for Sends email with MYOB sheet. Note: doesn't work in DEV as mail server is not installed'''
        self.url = self.data[34]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[34]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[34]['return code'],self.r.status_code)

    def test_sales035(self):
        '''verify the status code for Returns MYOB sheet from 'generate-nightly-myob-sheet' call'''
        self.url = self.data[35]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[35]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[35]['return code'],self.r.status_code)

    @unittest.skip
    def test_sales036(self):
        '''verify the status code for Sends email with Door Label sheet. Note: doesn't work in DEV as mail server is not installed'''
        self.url = self.data[36]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[36]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[36]['return code'],self.r.status_code)

    def test_sales037(self):
        '''verify the status code for Returns Door Label from 'generate-nightly-new-door-label-sheet' call'''
        self.url = self.data[37]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[37]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[37]['return code'],self.r.status_code)

    @unittest.skip
    def test_sales038(self):
        '''verify the status code for Sends Door On Hold email'''
        self.url = self.data[38]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[38]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[38]['return code'],self.r.status_code)

    def test_sales039(self):
        '''verify the status code for Gets Door On Hold document'''
        self.url = self.data[39]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[39]['method'], url=self.url, headers=self.header)
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[39]['return code'],self.r.status_code)

    def test_sales040(self):
        '''verify the status code for Returns list of quotes with specified order number'''
        self.url = self.data[40]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[40]['method'], url=self.url, headers=self.header,data=self.data[40]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[40]['return code'],self.r.status_code)

    def test_sales041(self):
        '''verify the Returns list of quotes with specified order number'''
        self.url = self.data[41]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[41]['method'], url=self.url, headers=self.header,data=self.data[41]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[41]['response'], self.r.text)

    def test_sales042(self):
        '''verify the status code for Get postcode'''
        self.url = self.data[42]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[42]['method'], url=self.url, headers=self.header,data=self.data[42]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[42]['return code'],self.r.status_code)

    def test_sales043(self):
        '''verify the Get postcode'''
        self.url = self.data[43]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[43]['method'], url=self.url, headers=self.header,data=self.data[43]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[43]['response'], self.r.text)

    def test_sales044(self):
        '''verify the status code for Get suburb'''
        self.url = self.data[44]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[44]['method'], url=self.url, headers=self.header,data=self.data[44]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[44]['return code'],self.r.status_code)

    def test_sales045(self):
        '''verify the Get suburb'''
        self.url = self.data[45]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[45]['method'], url=self.url, headers=self.header,data=self.data[45]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[45]['response'], self.r.text)

    def test_sales046(self):
        '''verify the status code for Returns and array of possible options for the specified selection category'''
        self.url = self.data[46]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[46]['method'], url=self.url, headers=self.header,data=self.data[46]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[46]['return code'],self.r.status_code)

    def test_sales047(self):
        '''verify the Returns and array of possible options for the specified selection category'''
        self.url = self.data[47]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[47]['method'], url=self.url, headers=self.header,data=self.data[47]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[47]['response'], self.r.text)

    def test_sales048(self):
        '''verify the status code for Returns and array of possible options for the specified selection category'''
        self.url = self.data[48]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[48]['method'], url=self.url, headers=self.header,data=self.data[48]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[48]['return code'],self.r.status_code)

    def test_sales049(self):
        '''verify the Returns and array of possible options for the specified selection category'''
        self.url = self.data[49]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[49]['method'], url=self.url, headers=self.header,data=self.data[49]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[49]['response'], self.r.text)

    def test_sales050(self):
        '''verify the status code for Get bar width'''
        self.url = self.data[50]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[50]['method'], url=self.url, headers=self.header,data=self.data[50]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[50]['return code'],self.r.status_code)

    def test_sales051(self):
        '''verify the Get bar width'''
        self.url = self.data[51]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[51]['method'], url=self.url, headers=self.header,data=self.data[51]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[51]['response'], self.r.text)

    def test_sales052(self):
        '''verify the status code for Get bar depth'''
        self.url = self.data[52]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[52]['method'], url=self.url, headers=self.header,data=self.data[52]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[52]['return code'],self.r.status_code)

    def test_sales053(self):
        '''verify the Get bar depth'''
        self.url = self.data[53]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[53]['method'], url=self.url, headers=self.header,data=self.data[53]['payload'])
        print('return ext is:', self.r.text)
        self.assertIn(self.data[53]['response'], self.r.text)

    def test_sales054(self):
        '''verify the status code for Get total number of Roller doors in Production'''
        self.url = self.data[54]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[54]['method'], url=self.url, headers=self.header,data=self.data[54]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[54]['return code'],self.r.status_code)

    def test_sales055(self):
        '''verify the status code for Get total number of Single Skin, Order doors in Production'''
        self.url = self.data[55]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[55]['method'], url=self.url, headers=self.header,data=self.data[55]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[55]['return code'],self.r.status_code)

    def test_sales056(self):
        '''verify the status code for Get total number of Single Skin, Roller doors in Production'''
        self.url = self.data[56]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[56]['method'], url=self.url, headers=self.header,data=self.data[56]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[56]['return code'],self.r.status_code)

    def test_sales057(self):
        '''verify the status code for Get total number of Single Skin, Assembly doors in Production'''
        self.url = self.data[57]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[57]['method'], url=self.url, headers=self.header,data=self.data[57]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[57]['return code'],self.r.status_code)

    def test_sales058(self):
        '''verify the status code for Get total number of Single Skin, Modification doors in Production'''
        self.url = self.data[58]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[58]['method'], url=self.url, headers=self.header,data=self.data[58]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[58]['return code'],self.r.status_code)

    def test_sales059(self):
        '''verify the status code for Get total number of Single Skin, Paint doors in Production'''
        self.url = self.data[59]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[59]['method'], url=self.url, headers=self.header,data=self.data[59]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[59]['return code'],self.r.status_code)

    def test_sales060(self):
        '''verify the status code for Get total number of Insulated, Order doors in Production'''
        self.url = self.data[60]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[60]['method'], url=self.url, headers=self.header,data=self.data[60]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[60]['return code'],self.r.status_code)

    def test_sales061(self):
        '''verify the status code for Get total number of Custom doors in Production'''
        self.url = self.data[61]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[61]['method'], url=self.url, headers=self.header,data=self.data[61]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[61]['return code'],self.r.status_code)

    def test_sales062(self):
        '''verify the status code for Get total number of Shutter doors in Production'''
        self.url = self.data[62]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[62]['method'], url=self.url, headers=self.header,data=self.data[62]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[62]['return code'],self.r.status_code)

    def test_sales063(self):
        '''verify the status code for Get total number of all doors in Production'''
        self.url = self.data[63]['Endpoint']
        self.header = {
            "content-type":"application/json;charset=UTF-8",
            "Cookie":set_cookie_admin
        }
        self.r = requests.request(method=self.data[63]['method'], url=self.url, headers=self.header,data=self.data[63]['payload'])
        print('return ext is:', self.r.text)
        self.assertEqual(self.data[63]['return code'],self.r.status_code)


if __name__ == '__main__':
    unittest.main(verbosity=2)