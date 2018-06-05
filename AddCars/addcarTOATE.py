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
from AddCars import car_detail1
from AddCars import car_detail2
from AddCars import car_detail3
from AddCars import car_detail4
from AddCars import car_detail5
from AddCars import car_detail6
from AddCars import car_detail7
from AddCars import car_detail8
from AddCars import car_detail9
from AddCars import car_detail10
from AddCars import car_detail11
from AddCars import car_detail12
from AddCars import car_detail13
from AddCars import car_detail14
from AddCars import car_detail15
from AddCars import car_detail16
from AddCars import car_detail17
from AddCars import car_detail18
from AddCars import car_detail19
#from AddCars import car_detail20
from AddCars import car_detail21



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
    def test_addcar101(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail1)
    
    #@unittest.skip("skip car") 
    def test_addcar102(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail2)
    
    #@unittest.skip("skip car")   
    def test_addcar103(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail3)
     
    #@unittest.skip("skip car")   
    def test_addcar104(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail4)
        
    #@unittest.skip("skip car")
    def test_addcar105(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail5)
    
    #@unittest.skip("skip car")
    def test_addcar106(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail6)
    
    #@unittest.skip("skip car")    
    def test_addcar107(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail7)
    
    #@unittest.skip("skip car")    
    def test_addcar108(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail8)
    
    #@unittest.skip("skip car")
    def test_addcar109(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail9)
 
    #@unittest.skip("skip car") 
    def test_addcar110(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail10)
        
    #@unittest.skip("skip car") 
    def test_addcar111(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail11)
        
    #@unittest.skip("skip car") 
    def test_addcar112(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail12)
        
    #@unittest.skip("skip car") 
    def test_addcar113(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail13)
        
    #@unittest.skip("skip car") 
    def test_addcar114(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail14)
        
    #@unittest.skip("skip car") 
    def test_addcar115(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail15)

    #@unittest.skip("skip car") 
    def test_addcar116(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail16)
        
    #@unittest.skip("skip car") 
    def test_addcar117(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail17)
        
    #@unittest.skip("skip car") 
    def test_addcar118(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail18)
        
    #@unittest.skip("skip car") 
    def test_addcar119(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail19)
        
    #===========================================================================
    # #@unittest.skip("skip car") 
    # def test_addcar120(self):
    #     GeneralFunctions.deleteAddCarFunction(self, car_detail20)
    #===========================================================================
        
    #@unittest.skip("skip car") 
    def test_addcar121(self):
        GeneralFunctions.deleteAddCarFunction(self, car_detail21)
 
    
        
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AdaugaMasini)
    return suite        

if __name__ == "__main__":
    unittest.main()