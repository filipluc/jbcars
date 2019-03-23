'''
Created on Jun 3, 2018

@author: Filip.LUCHIANOV
'''

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import os
from selenium.webdriver.support.ui import Select

class GeneralFunctions():
    
    global car_detail
    
    def check_exists_by_xpath_multiple(self, car_detail):
        driver = self.driver
        try:
            driver.find_elements_by_xpath("//div[@class='listed-item-description'][contains(., '" + str(car_detail.var_title) + "')]")[1]
        except NoSuchElementException:        
            return False
        except IndexError:
            print ('Eroare: Index out of range - exista maxim o masina')
            return False
        return True
    
    def check_exists_by_xpath(self, car_detail):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//div[@class='listed-item-description'][contains(., '" + str(car_detail.var_title) + "')]")
        except NoSuchElementException:
            return False
        return True
    
    def deleteAddCarFunction(self, car_detail):
        if GeneralFunctions.check_exists_by_xpath(self, car_detail):
            print (str(car_detail) + '---Masina exista, va fi adaugata din nou')
            GeneralFunctions.addCarFunction(self, car_detail)
            time.sleep(1)
            self.driver.get("https://www.2dehands.be/beheer/advertenties/overzicht/")
            time.sleep(2)
            if GeneralFunctions.check_exists_by_xpath_multiple(self, car_detail):
                print (str(car_detail) + '---Masina veche va fi stearsa')
                GeneralFunctions.deleteCarFunction(self, car_detail)
                time.sleep(1)
                # check again, in case the old car was not deleted the first time
                if GeneralFunctions.check_exists_by_xpath_multiple(self, car_detail):
                    GeneralFunctions.deleteCarFunction(self, car_detail)
            else:
                print ('Eroare: Masina noua nu a putut fi adaugata, a ramas cea veche' + str(car_detail))
        else:
            print(str(car_detail) + '--Masina nu exista pe site. De vazut daca trebuie stearsa din script')     

    
    def deleteAddCarFunction_old(self, car_detail):
        #not  used
        if GeneralFunctions.check_exists_by_xpath(self, car_detail):
            print ('Masina exista, va fi stearsa' + str(car_detail))
            GeneralFunctions.deleteCarFunction(self, car_detail)
            time.sleep(2)
            if not GeneralFunctions.check_exists_by_xpath(self, car_detail):
                GeneralFunctions.addCarFunction(self, car_detail)
            else:
                print('Masina nu a putut fi stearsa, nu se va adauga din nou') 
        else:
            print('Masina nu exista' + str(car_detail))
        

    def deleteCarFunction(self, car_detail):
        driver = self.driver
        time.sleep(2)
        elem101 = driver.find_elements_by_xpath("//div[@class='listed-item-description'][contains(., '" + str(car_detail.var_title) + "')]")[1]     
        elem101.click()
        time.sleep(2)
        elem102 = driver.find_element_by_xpath("//span[text()='Verwijder']")
        elem102.click()
        time.sleep(2)
        elem103 = driver.find_element_by_id("delete_confirm")
        elem103.click()
        time.sleep(5)       
    
    def addCarFunction(self, car_detail):
        driver = self.driver
        #Adauga anunt nou
        driver.find_element_by_link_text('Plaats een zoekertje').click()
        try:
            WebDriverWait(driver, 5).until(EC.title_contains("Plaats zoekertje"), "Pagina de Adauga anunt nu a fost gasita")
        except TimeoutException:
            self.assertIn("Plaats zoekertje", driver.title, "Pagina de Adauga anunt nu a fost gasita")  
        finally:
            pass       
        elem3 = driver.find_element_by_id("title")
        elem3.clear()
        elem3.send_keys(car_detail.var_title)
        elem3.send_keys(Keys.TAB)
        elem4 = driver.find_element_by_class_name("icon-radiobutton")
        elem4.click()
        select1 = Select(driver.find_element_by_id('level1-option'))

        select1.select_by_visible_text(car_detail.var_categorie)

        elem5 = driver.find_element_by_id('level1-option')
        elem5.send_keys(Keys.TAB)
        time.sleep(1)
        elem6 = driver.find_element_by_id('level2-option')
        elem6.click()
        time.sleep(2)
        elem6.send_keys(car_detail.var_brand)
        time.sleep(1)
        elem6.send_keys(Keys.TAB)
        time.sleep(1)
        elem7 = driver.find_element_by_id('level3-option')
        elem7.click()
        time.sleep(2)
        elem7.send_keys(car_detail.var_model)
        time.sleep(1)
        elem7.send_keys(Keys.TAB)     
        time.sleep(1)
        elem8 = driver.find_element_by_id("description")
        elem8.send_keys(car_detail.var_desc)
        elem8.send_keys("\nopeningsuren\nmaandag tot vrijdag 10-17 uur\nzaterdag 10-14 uur\nadres\nLIERSESTEENWEG 153\n2547 LINT")
        # elem8.send_keys("\nVan 19/12/2018 tot 03/01/2019 is OPEN enkel op afspraak\n\nadres\nLIERSESTEENWEG 153\n2547 LINT")

        elem9 = driver.find_element_by_id('price')
        elem9.click()
        elem9.send_keys("Bedrag")
        elem9.send_keys(Keys.TAB)
          
        elem10 = driver.find_element_by_id('bedragplaats_prijs_waarde')
        elem10.click()
        elem10.send_keys(car_detail.var_price)
          
        elem11 = driver.find_element_by_xpath("//span[text()='Biedingen toestaan']")
        elem11.click()
          
        elem12 = driver.find_element_by_id('condition')
        elem12.click()
        elem12.send_keys("Gebruikt")
        elem12.send_keys(Keys.TAB)    
                
        elem13 = driver.find_element_by_id("website")
        elem13.clear()
        elem13.send_keys("www.jbcars.be")
        elem13.send_keys(Keys.TAB)
        if os.path.exists("d:\Github\jbcars\AddCars\pics"):
            picspathgeneral = "d:\Github\jbcars\AddCars\pics"
        else:
            picspathgeneral = "c:\Github\jbcars\AddCars\pics"
        picspath = os.path.join(picspathgeneral, car_detail.var_picspath)
        for dirname, dirnames, filenames in os.walk(picspath):
            # print path to all filenames.
            for filename in filenames:
                elem15 = driver.find_element_by_css_selector("input[type=file]")
                #print(os.path.join(dirname, filename))
                time.sleep(1.5)
                elem15.send_keys(os.path.join(dirname, filename))
        time.sleep(2)
        try:
            elem16 = driver.find_element_by_id('auto_carrosserie')
            elem16.click()
        except NoSuchElementException:
            elem16 = driver.find_element_by_id('auto_bedrijf_type')
            elem16.click()
        elem16.send_keys(car_detail.var_carroserie)
        elem16.send_keys(Keys.TAB)     
        try:
            elem17 = driver.find_element_by_name('adv.auto_bj.maand')
            elem17.click()
        except NoSuchElementException:
            elem17 = driver.find_element_by_name('adv.auto_bedr_bj.maand')
            elem17.click()
        elem17.send_keys(car_detail.var_month)
        elem17.send_keys(Keys.TAB)    
        try:
            elem18 = driver.find_element_by_name('adv.auto_bj.jaar')
            elem18.click()
        except NoSuchElementException:
            elem18 = driver.find_element_by_name('adv.auto_bedr_bj.jaar')
            elem18.click()
        elem18.send_keys(car_detail.var_year)
        elem18.send_keys(Keys.TAB)      
          
        elem19 = driver.find_element_by_xpath("//span[text()='" + str(car_detail.var_gas) + "']")
        elem19.click()
          
        elem20 = driver.find_element_by_id('auto_transmissie')
        elem20.click()
        elem20.send_keys(car_detail.var_transmissie)
        elem20.send_keys(Keys.TAB)   
          
        elem21 = driver.find_element_by_id('km_stand')
        elem21.click()
        elem21.send_keys(car_detail.var_km)
        elem21.send_keys(Keys.TAB)    
                  
        elem22 = driver.find_element_by_id('auto_deurs')
        elem22.click()
        elem22.send_keys(car_detail.var_doors)
        elem22.send_keys(Keys.TAB)        
          
        elem23 = driver.find_element_by_id('vermogen_pk')
        elem23.click()
        elem23.send_keys(car_detail.var_pk)
        elem23.send_keys(Keys.TAB)            
          
        elem24 = driver.find_element_by_id('cilinderinhoud_cc')
        elem24.click()
        elem24.send_keys(car_detail.var_cilinder)
        elem24.send_keys(Keys.TAB)  

        try:
            elem24 = driver.find_element_by_id('co2_emissie')
            elem24.click()
            elem24.send_keys(car_detail.var_co2)
            elem24.send_keys(Keys.TAB)
        except NoSuchElementException:
            pass
               
        elem25 = driver.find_element_by_id('euro_norm')
        elem25.click()
        elem25.send_keys(car_detail.var_euro)
        elem25.send_keys(Keys.TAB)      

        #optiuni
        for x in car_detail.var_options.split(', '):
            driver.find_element_by_xpath("//span[text()='" + str(x) + "']").click()
            
       
        #culoare masina
        elem28 = driver.find_elements_by_xpath("//span[text()='" + str(car_detail.var_carcolor) + "']")[0]
        elem28.click()      
        
        #culoare interior
        try:
            elem29 = driver.find_elements_by_xpath("//span[text()='" + str(car_detail.var_interiorcolor) + "']")[1]
            elem29.click()
        except NoSuchElementException:
            pass
        except IndexError:
            pass
        
             
        
        #submit
        elem30 = driver.find_element_by_xpath("//button[@class='submit-form-button ui-button-primary icon-punaise']")
        elem30.click()
              
        time.sleep(3)