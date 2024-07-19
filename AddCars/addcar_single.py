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
import subprocess
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from AddCars.cars import car101
from AddCars.cars import car102
from AddCars.cars import car103
from AddCars.cars import car104
from AddCars.cars import car105
from AddCars.cars import car106
from AddCars.cars import car107
from AddCars.cars import car108
from AddCars.cars import car109
from AddCars.cars import car110
from AddCars.cars import car111
from AddCars.cars import car112
from AddCars.cars import car113
from AddCars.cars import car114
from AddCars.cars import car115
from AddCars.cars import car116
from AddCars.cars import car117
from AddCars.cars import car118
from AddCars.cars import car119
from AddCars.cars import car120
from AddCars.cars import car121
from AddCars.cars import car122
from AddCars.cars import car123
from AddCars.cars import car124
from AddCars.cars import car125
from AddCars.cars import car126
from AddCars.cars import car127
from AddCars.cars import car128
from AddCars.cars import car129
from AddCars.cars import car130
from AddCars.cars import car131
from AddCars.cars import car132
from AddCars.cars import car133
from AddCars.cars import car134
from AddCars.cars import car135



class AdaugaMasiniSingle(unittest.TestCase):

    def setUp(self):
        # myurl = 'https://www.2dehands.be/my-account/sell/index.html'
        # chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-window --remote-debugging-port=1111"
        # webbrowser.get(chromedir).open(myurl, new=1)

        taskkill_command = ['TASKKILL', '/IM', 'chrome.exe', '/F']
        start_chrome_command = [
            'start', 'chrome',
            'https://www.2dehands.be/my-account/sell/index.html',
            '--new-window', '--remote-debugging-port=2222'
        ]
        # Run the TASKKILL command
        try:
            subprocess.run(taskkill_command, check=True)
            print("All instances of chrome.exe have been terminated.")
        except subprocess.CalledProcessError as e:
            print(f"Error terminating chrome.exe: {e}")

        # Run the command to start Chrome
        try:
            subprocess.run(start_chrome_command, shell=True, check=True)
            print("Chrome has been started with the specified URL and options.")
        except subprocess.CalledProcessError as e:
            print(f"Error starting Chrome: {e}")


        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        #options.add_argument("--incognito")
        options.add_experimental_option("debuggerAddress", "127.0.0.1:2222")
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
    def test_car114(self):
        GeneralFunctions.deleteAddCarFunction(self, car114)

        
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AdaugaMasiniSingle)
    return suite        

if __name__ == "__main__":
    unittest.main()