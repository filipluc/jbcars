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
import time
import subprocess
from selenium.webdriver.chrome.options import Options
from AddCars.general import GeneralFunctions
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

class AdaugaMasini(unittest.TestCase):

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
        pass

    def test_car101(self):
        GeneralFunctions.deleteAddCarFunction(self, car101)

    def test_car102(self):
        GeneralFunctions.deleteAddCarFunction(self, car102)

    def test_car103(self):
        GeneralFunctions.deleteAddCarFunction(self, car103)

    def test_car104(self):
        GeneralFunctions.deleteAddCarFunction(self, car104)

    def test_car105(self):
        GeneralFunctions.deleteAddCarFunction(self, car105)
    
    def test_car106(self):
        GeneralFunctions.deleteAddCarFunction(self, car106)

    def test_car107(self):
        GeneralFunctions.deleteAddCarFunction(self, car107)

    def test_car108(self):
        GeneralFunctions.deleteAddCarFunction(self, car108)

    def test_car109(self):
        GeneralFunctions.deleteAddCarFunction(self, car109)

    def test_car110(self):
        GeneralFunctions.deleteAddCarFunction(self, car110)

    def test_car111(self):
        GeneralFunctions.deleteAddCarFunction(self, car111)

    def test_car112(self):
        GeneralFunctions.deleteAddCarFunction(self, car112)

    def test_car113(self):
        GeneralFunctions.deleteAddCarFunction(self, car113)

    def test_car114(self):
        GeneralFunctions.deleteAddCarFunction(self, car114)
        
    # def test_car115(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car115)

    def test_car116(self):
        GeneralFunctions.deleteAddCarFunction(self, car116)

    def test_car117(self):
        GeneralFunctions.deleteAddCarFunction(self, car117)

    def test_car118(self):
        GeneralFunctions.deleteAddCarFunction(self, car118)
        
    def test_car119(self):
        GeneralFunctions.deleteAddCarFunction(self, car119)

    # def test_car120(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car120)

    def test_car121(self):
        GeneralFunctions.deleteAddCarFunction(self, car121)

    def test_car122(self):
        GeneralFunctions.deleteAddCarFunction(self, car122)

    def test_car123(self):
        GeneralFunctions.deleteAddCarFunction(self, car123)

    def test_car124(self):
        GeneralFunctions.deleteAddCarFunction(self, car124)

    def test_car125(self):
        GeneralFunctions.deleteAddCarFunction(self, car125)

    def test_car126(self):
        GeneralFunctions.deleteAddCarFunction(self, car126)

    # def test_car127(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car127)

    # def test_car128(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car128)

    # def test_car129(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car129)

    def test_car130(self):
        GeneralFunctions.deleteAddCarFunction(self, car130)

    def test_car131(self):
        GeneralFunctions.deleteAddCarFunction(self, car131)

    def test_car132(self):
        GeneralFunctions.deleteAddCarFunction(self, car132)

    # def test_car133(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car133)

    # def test_car134(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car134)

    # def test_car135(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car135)
        
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AdaugaMasini)
    return suite        

if __name__ == "__main__":
    unittest.main()