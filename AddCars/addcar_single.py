'''
Created on May 31st, 2018

@author: Filip

Add car - 2dehands.be
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from xmlrunner import *
from AddCars.general import GeneralFunctions
# import webbrowser
import time
from selenium.webdriver.chrome.options import Options
from AddCars.cars import car102



class AdaugaMasiniSingle(unittest.TestCase):

    def setUp(self):
        # myurl = 'https://www.2dehands.be/my-account/sell/index.html'
        # chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-window --remote-debugging-port=1111"
        # webbrowser.get(chromedir).open(myurl, new=1)

        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        #options.add_argument("--incognito")
        options.add_experimental_option("debuggerAddress", "127.0.0.1:1111")
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome(options=options)
        driver = self.driver
        time.sleep(5)
        # #driver.implicitly_wait(5)
        # driver.get("https://www.2dehands.be/login.html")
        # #driver.get("https://www.2dehands.be")
        # self.assertIn("2dehands", driver.title, "Page was not opened correctly")
        # elem1 = driver.find_element_by_name("j_username")
        # elem1.clear()
        # # elem1.send_keys("ljale@hotmail.com")
        # elem1.send_keys("jb.cars@hotmail.com")
        # elem2 = driver.find_element_by_name("j_password")
        # elem2.clear()
        # # elem2.send_keys("Boni/1994")
        # elem2.send_keys("103robel")
        # elem2.send_keys(Keys.RETURN)
        # #time.sleep(600)
        #
        # #using explicit wait with assert
        # try:
        #     WebDriverWait(driver, 5).until(EC.title_contains("Tweedehands"), "Login was not successfull")
        # except TimeoutException:
        #     self.assertIn("Tweedehands", driver.title, "Login was not successfull")
        # finally:
        #     #driver.quit()
        pass
        
    def tearDown(self):
        # self.driver.quit()
        pass

    #@unittest.skip("skip car") 
    def test_car102(self):
        GeneralFunctions.deleteAddCarFunction(self, car102)

        
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AdaugaMasiniSingle)
    return suite        

if __name__ == "__main__":
    unittest.main()