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
import regex

class GeneralFunctions():
    
    global car_detail
    
    def check_exists_by_xpath_multiple(self, car_detail):
        driver = self.driver
        try:
            driver.find_elements_by_xpath("//span[contains(text(),'" + str(car_detail.var_title) + "')]")[1]
        except NoSuchElementException:        
            return False
        except IndexError:
            print('Eroare: Index out of range - exista maxim o masina')
            return False
        return True
    
    def check_exists_by_xpath(self, car_detail):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//span[contains(text(),'" + str(car_detail.var_title) + "')]")
        except NoSuchElementException:
            return False
        return True
    
    def deleteAddCarFunction(self, car_detail):
        self.driver.get("https://www.2dehands.be/my-account/sell/index.html/")
        time.sleep(4)
        if GeneralFunctions.check_exists_by_xpath(self, car_detail):
            print(str(car_detail) + '---Masina exista, va fi adaugata din nou')
            GeneralFunctions.addCarFunction(self, car_detail)
            time.sleep(1)
            self.driver.get("https://www.2dehands.be/my-account/sell/index.html/")
            time.sleep(2)
            if GeneralFunctions.check_exists_by_xpath_multiple(self, car_detail):
                print(str(car_detail) + '---Masina veche va fi stearsa')
                GeneralFunctions.deleteCarFunction(self, car_detail)
            else:
                print('Eroare: Masina noua nu a putut fi adaugata, a ramas cea veche' + str(car_detail))
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
        elem101 = driver.find_elements_by_xpath("//span[contains(text(),'" + str(car_detail.var_title) + "')]")[1]
        elem101.click()
        time.sleep(2)
        elem102 = driver.find_element_by_xpath("//span[text()='Verwijder']")
        time.sleep(2)
        elem102.click()
        time.sleep(2)
        elem103 = driver.find_element_by_xpath("//button[contains(text(), 'Verkocht via 2dehands')]")
        time.sleep(1)
        elem103.click()
        time.sleep(1)
        try:
            elem104 = driver.find_element_by_xpath("//button[text() = 'Direct']")
            elem104.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        time.sleep(2)

    
    def addCarFunction(self, car_detail):
        driver = self.driver
        #Adauga anunt nou
        driver.find_element_by_link_text('Plaats zoekertje').click()
        try:
            WebDriverWait(driver, 5).until(EC.title_contains("tweedehands"), "Pagina de Adauga anunt nu a fost gasita")
        except TimeoutException:
            self.assertIn("tweedehands", driver.title, "Pagina de Adauga anunt nu a fost gasita")
        finally:
            pass
        time.sleep(1)
        elem3 = driver.find_element_by_id("category-keywords")
        elem3.clear()
        elem3.send_keys(car_detail.var_title)
        elem3.send_keys(Keys.TAB)
        time.sleep(1)

        select1 = Select(driver.find_element_by_id('cat_sel_1'))
        select1.select_by_visible_text(car_detail.var_categorie)
        time.sleep(1)

        select11 = Select(driver.find_element_by_id('cat_sel_3'))
        select11.select_by_visible_text(car_detail.var_brand)
        time.sleep(1)
        elem77 = driver.find_element_by_id('category-selection-submit')
        elem77.click()
        time.sleep(3)

        if os.path.exists("d:\Github\jbcars\AddCars\pics"):
            picspathgeneral = "d:\Github\jbcars\AddCars\pics"
        else:
            picspathgeneral = "c:\Github\jbcars\AddCars\pics"
        picspath = os.path.join(picspathgeneral, car_detail.var_picspath)
        for dirname, dirnames, filenames in os.walk(picspath):
            # print(filenames)
            for filename in filenames:
                elem15 = driver.find_elements_by_xpath("//input[contains(@id, 'html5_')]")[-1]
                time.sleep(0.5)
                elem15.send_keys(os.path.join(dirname, filename))
                time.sleep(6)
        time.sleep(2)

        # elem8 = driver.find_element_by_id("description_ifr")
        elem8 = driver.find_element_by_id("description_nl-BE_ifr")
        # elem8.send_keys("\nBeste klanten,\nin de periode 20/07/2020 tot 21/08/2020(vakantie)\nwij zijn open enkel op afspraak 0485/673404\ndank u\n\n")
        # elem8.send_keys("\nVanaf zaterdag 27 maart enkel op afspraak, met maximaal 2 personen.\nU kan telefonisch of per email een afspraak maken.\n")
        elem8.send_keys(car_detail.var_desc)
        #elem8.send_keys("\nMeer Info 0485/673404\n\nopeningsuren\nmaandag tot vrijdag 10-17 uur\nzaterdag 10-14 uur\nadres\nLIERSESTEENWEG 153\n2547 LINT")
        elem8.send_keys("\nMeer Info 0485/673404\nE-mail: jb.cars@hotmail.com\nOpgelet: Tijdelijk enkel op afspraak\nAttention: Temporairement uniquement sur rendez-vous\n\nadres\nLIERSESTEENWEG 153\n2547 LINT")
        time.sleep(1)

        elem9 = driver.find_element_by_xpath("//input[contains(@id, 'js-feature-url')]")
        elem9.send_keys("www.jbcars.be")
        time.sleep(0.2)

        elem81 = ""
        try:
            elem81 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[model]']")
            elem81.click()
        except NoSuchElementException:
            try:
                elem81 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[brand]']")
                elem81.click()
            except NoSuchElementException:
                pass
        if elem81 != "":
            elem81.send_keys(car_detail.var_model)
            elem81.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem82 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[fuel]']")
        elem82.click()
        elem82.send_keys(car_detail.var_gas)
        elem82.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem83 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[euronorm]']")
        elem83.click()
        elem83.send_keys(car_detail.var_euro)
        elem83.send_keys(Keys.TAB)
        time.sleep(0.5)

        try:
            elem84 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[body]']")
            elem84.click()
            elem84.send_keys(car_detail.var_carroserie)
            elem84.send_keys(Keys.TAB)
            time.sleep(0.5)
        except NoSuchElementException:
            pass

        elem85 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[aantaldeurenBE]']")
        elem85.click()
        elem85.send_keys(car_detail.var_doors)
        elem85.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem86 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[transmission]']")
        elem86.click()
        elem86.send_keys(car_detail.var_transmissie)
        elem86.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem87 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[color]']")
        elem87.click()
        elem87.send_keys(car_detail.var_carcolor)
        elem87.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem87 = driver.find_element_by_xpath("//select[@name='singleSelectAttribute[interiorcolor]']")
        elem87.click()
        elem87.send_keys(car_detail.var_interiorcolor)
        elem87.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem88 = driver.find_element_by_xpath("//input[contains(@id, 'numericAttribute[constructionYear]')]")
        elem88.click()
        elem88.send_keys(car_detail.var_year)
        elem88.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem89 = driver.find_element_by_xpath("//input[contains(@id, 'numericAttribute[co2emission]')]")
        elem89.click()
        elem89.send_keys(car_detail.var_co2)
        elem89.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem90 = driver.find_element_by_xpath("//input[contains(@id, 'numericAttribute[mileage]')]")
        elem90.click()
        elem90.send_keys(car_detail.var_km)
        elem90.send_keys(Keys.TAB)
        time.sleep(0.5)


        elem91 = driver.find_element_by_xpath("//input[contains(@id, 'numericAttribute[engineDisplacement]')]")
        elem91.click()
        elem91.send_keys(car_detail.var_cilinder)
        elem91.send_keys(Keys.TAB)
        time.sleep(0.5)


        #optiuni
        #for x in car_detail.var_options.split(','):
        for x in regex.split(',|\n', car_detail.var_options):
            y = ''
            if x == "4x4":
                y = "4x4"
            if x == "ABS":
                y = "ABS"
            if x == "Adaptieve lichten":
                y = "Adaptieve-lichten"
            if x == "Adaptive Cruise Control":
                y = "AdaptiveCruiseControl"
            if x == "Airbags":
                y = "Airbags"
            if x == "Airconditioning":
                y = "Climate control Airconditioning"
            if x == "Alarm":
                y = "Alarm"
            if x == "Lederen bekleding":
                y = "Bekleding leder"
            if x == "Bluetooth":
                y = "Bluetooth"
            if x == "Boordcomputer":
                y = "Boordcomputer"
            if x == "Centrale vergrendeling":
                y = "Centrale vergrendeling"
            if x == "Climate control":
                y = "Climate control"
            if x == "Cruise Control":
                y = "Cruise Control"
            if x == "Dodehoekdetectie":
                y = "Dodehoekdetectie"
            if x == "Elektrische koffer":
                y = "Elektrische achterklep"
            if x == "Elektrische buitenspiegels":
                y = "Elektrische buitenspiegels"
            if x == "Elektrische stoelverstelling":
                y = "Elektrische stoelverstelling"
            if x == "Electronic Stability Program (ESP)":
                y = "Electronict Stability Program"
            if x == "Elektrische ramen":
                y = "Elektrische ramen"
            if x == "Emergency brake assist":
                y = "Emergency brake assist"
            if x == "Keyless entry":
                y = "Keyless entry"
            if x == "Isofix":
                y = "Isofix"
            if x == "Lichtmetalen velgen":
                y = "Lichtmetalen velgen"
            if x == "Metaalkleur":
                y = "Metallic lak"
            if x == "Mistlampen":
                y = "Mistlampen"
            if x == "Navigatiesysteem":
                y = "Navigatiesysteem"
            if x == "Open dak":
                y = "Open of panorama dak"
            if x == "Panoramadak":
                y = "Panoramadak"
            if x == "Parkeerassistent":
                y = "Parkeerassistent"
            if x == "Parkeercamera":
                y = "Parkeercamera"
            if x == "Parkeersensor":
                y = "Parkeersensor"
            if x == "Radio":
                y = "Radio"
            if x == "Schuifdeur":
                y = "Shuifdeur"
            if x == "Sportpakket":
                y = "Sportpakket"
            if x == "Sportstoelen":
                y = "Sportstoelen"
            if x == "Spraakbediening":
                y = "Spraakbediening"
            if x == "Startonderbreker":
                y = "Startonderbreker"
            if x == "Start-stop-systeem":
                y = "Start-stop-systeem"
            if x == "Stuurwielverwarming":
                y = "Stuurwielverwarming"
            if x == "Zetelverwarming":
                y = "Stoelverwarming"
            if x == "Stoelventilatie":
                y = "Stoelventilatie"
            if x == "Stoelmassage":
                y = "Stoelmassage"
            if x == "Traction-control":
                y = "Traction-control"
            if x == "Trekhaak":
                y = "Trekhaak"
            if x == "USB":
                y = "USB"
            if x == "Verkeersbordherkenning":
                y = "Verkeersbordherkenning"
            if x == "Vermoeidheidsdetectie":
                y = "Vermoeidheidsdetectie"
            if x == "Verwarmde buitenspiegels":
                y = "Verwarmde buitenspiegels"
            if x == "Xenon verlichting":
                y = "Xenon verlichting"
            driver.find_element_by_xpath("//input[@value='" + str(y) + "']").click()
            time.sleep(0.1)



        elem92 = driver.find_element_by_xpath("//input[contains(@name, 'price.value')]")
        elem92.click()
        elem92.send_keys(car_detail.var_price)
        elem92.send_keys(Keys.TAB)
        time.sleep(0.5)

        elem93 = driver.find_element_by_xpath("//input[contains(@id, 'syi-bidding-switch')]")
        #elem93 = driver.find_element_by_xpath("//span[@class='mp-Toggle-round']")
        elem93.click()
        time.sleep(0.5)


        try:
            elem94 = driver.find_element_by_xpath("//span[text()='Gratis']")
            elem94.click()
            time.sleep(1)
        # except NoSuchElementException:
        #     elem94 = driver.find_element_by_xpath("//*[@id='js-products']/div[1]/div[2]/div/div[2]/label/div[1]/div[2]/p")
        #     elem94.click()
        #     time.sleep(1)
        except NoSuchElementException:
            elem94 = driver.find_element_by_xpath("//*[@id='feature-bundles']/div/div[2]/div/div[2]/label/div[1]/div[1]")
            elem94.click()
            time.sleep(3)

        elem95 = driver.find_element_by_xpath("//a[contains(@id, 'syi-place-ad-button')]")
        elem95.click()
        time.sleep(20)
