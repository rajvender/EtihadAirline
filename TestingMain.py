from __builtin__ import set
from Locators import Locators as lc
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import Testdata

class test_Booking(unittest.TestCase):


    def test_searchFlights(self):
       try:
        driver = webdriver.Chrome(Testdata.Path)
        driver.get(Testdata.URL)
        driver.maximize_window()
        time.sleep(10)

        Cookiebtn=driver.find_element_by_class_name(Testdata.Cookiebutton)
        Cookiebtn.click()
        time.sleep(10)
        driver.find_element_by_id("onetrust-pc-sdk").click()
        print "ttt"
        Cookieselectbtn=driver.find_element_by_xpath()
        Cookieselectbtn.click()
        time.sleep(10)
        print "ttt"
        #driver.execute_script("window.scrollTo(0, 50)")
        FromDst=driver.find_element_by_id(Testdata.FromDestination)

        FromDst.clear()
        print "ttt"
        time.sleep(5)
       except:
        pass




if __name__ == "__main__":
        unittest.main()