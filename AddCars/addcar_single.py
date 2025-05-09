'''
Created on May 31st, 2018

@author: Filip

Add car - 2dehands.be
'''

import unittest
import subprocess
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from xmlrunner import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from AddCars.general import GeneralFunctions

# Import all cars
from AddCars.cars import (
    car101, car102, car103, car104, car105, car106, car107, car108, car109, car110,
    car111, car112, car113, car114, car115, car116, car117, car118, car119, car120,
    car121, car122, car123, car124, car125, car126, car127, car128, car129, car130,
    car131, car132, car133, car134, car135
)

class AdaugaMasiniSingle(unittest.TestCase):

    def setUp(self):
        # myurl = 'https://www.2dehands.be/my-account/sell/index.html'
        # chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-window --remote-debugging-port=1111"
        # webbrowser.get(chromedir).open(myurl, new=1)

        # Kill all running Chrome instances
        taskkill_command = ['TASKKILL', '/IM', 'chrome.exe', '/F']
        try:
            subprocess.run(taskkill_command, check=True, shell=True)
            print("All instances of chrome.exe have been terminated.")
        except subprocess.CalledProcessError as e:
            print(f"Error terminating chrome.exe: {e}")

        # Define the path to Chrome and setup debugging options
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        user_data_dir = r'C:\ChromeDebugProfile'
        url = 'https://www.2dehands.be/my-account/sell/index.html'

        # Start Chrome with remote debugging enabled
        try:
            chrome_cmd = f'"{chrome_path}" --remote-debugging-port=2222 --user-data-dir="{user_data_dir}" --start-maximized --new-window "{url}"'
            subprocess.Popen(chrome_cmd, shell=True)
            print("Chrome has been started with the specified URL and options.")
        except Exception as e:
            print(f"Error starting Chrome: {e}")
            raise

        # Give Chrome time to start
        time.sleep(3)

        # Connect to the running Chrome instance
        options = Options()
        # options.add_argument("--start-maximized")
        # options.add_argument("--incognito")
        # options.add_experimental_option("debuggerAddress", "127.0.0.1:2222")
        options.debugger_address = "127.0.0.1:2222"
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome(options=options)
        driver = self.driver
        time.sleep(5)
        # driver.implicitly_wait(5)

        # driver.get("https://www.2dehands.be/login.html")
        # self.assertIn("2dehands", driver.title, "Page was not opened correctly")

        # elem1 = driver.find_element_by_name("j_username")
        # elem1.clear()
        # elem1.send_keys("jb.cars@hotmail.com")

        # elem2 = driver.find_element_by_name("j_password")
        # elem2.clear()
        # elem2.send_keys("103robel")
        # elem2.send_keys(Keys.RETURN)

        # using explicit wait with assert
        # try:
        #     WebDriverWait(driver, 5).until(EC.title_contains("Tweedehands"), "Login was not successful")
        # except TimeoutException:
        #     self.assertIn("Tweedehands", driver.title, "Login was not successful")
        # finally:
        #     driver.quit()
        pass

    def tearDown(self):
        # self.driver.quit()
        if hasattr(self, 'driver'):
            self.driver.quit()

    # @unittest.skip("skip car")
    def test_car114(self):
        GeneralFunctions.deleteAddCarFunction(self, car114)

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AdaugaMasiniSingle)
    return suite

if __name__ == "__main__":
    unittest.main()
