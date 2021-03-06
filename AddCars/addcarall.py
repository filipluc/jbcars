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
from AddCars.cars import car101
from AddCars.cars import car102
from AddCars.cars import car103
from AddCars.cars import car104
from AddCars.cars import car105
#from AddCars.cars import car106
from AddCars.cars import car107
from AddCars.cars import car108
from AddCars.cars import car109
from AddCars.cars import car110



class AdaugaMasini(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=options)
        
        driver = self.driver
        #driver.implicitly_wait(5)
        driver.get("https://www.2dehands.be/login.html")
        self.assertIn("2dehands.be", driver.title, "Page was not opened correctly")
        elem1 = driver.find_element_by_name("email")
        elem1.clear()
        #elem1.send_keys("ljale@hotmail.com")
        elem1.send_keys("jb.cars@hotmail.com")
        elem2 = driver.find_element_by_name("password")
        elem2.clear()
        #elem2.send_keys("Boni/1994")
        elem2.send_keys("103robel")
        elem2.send_keys(Keys.RETURN)
        
        #using explicit wait with assert
        try:
            WebDriverWait(driver, 5).until(EC.title_contains("Persoonlijke"), "Login was not successfull")
        except TimeoutException:
            self.assertIn("Persoonlijke", driver.title, "Login was not successfull")  
        finally:
            #driver.quit()
            pass
        
    def tearDown(self):
        self.driver.quit()

    #@unittest.skip("skip car")
    def test_car101(self):
        GeneralFunctions.deleteAddCarFunction(self, car101)
    
    #@unittest.skip("skip car") 
    def test_car102(self):
        GeneralFunctions.deleteAddCarFunction(self, car102)
    
    #@unittest.skip("skip car")   
    def test_car103(self):
        GeneralFunctions.deleteAddCarFunction(self, car103)
     
    #@unittest.skip("skip car")   
    def test_car104(self):
        GeneralFunctions.deleteAddCarFunction(self, car104)
        
    #@unittest.skip("skip car")
    def test_car105(self):
        GeneralFunctions.deleteAddCarFunction(self, car105)
    
    #===========================================================================
    # #@unittest.skip("skip car")
    # def test_car106(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car106)
    #===========================================================================
    
    #@unittest.skip("skip car")    
    def test_car107(self):
        GeneralFunctions.deleteAddCarFunction(self, car107)
    
    #@unittest.skip("skip car")    
    def test_car108(self):
        GeneralFunctions.deleteAddCarFunction(self, car108)
    
    #@unittest.skip("skip car")
    def test_car109(self):
        GeneralFunctions.deleteAddCarFunction(self, car109)
 
    #@unittest.skip("skip car") 
    def test_car110(self):
        GeneralFunctions.deleteAddCarFunction(self, car110)
 
    
        
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AdaugaMasini)
    return suite        

if __name__ == "__main__":
    unittest.main()