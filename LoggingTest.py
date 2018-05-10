from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class LoggingTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox() #.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def test_incorrectLoginTest(self):
        
        #given
        driver = self.driver
        driver.get("https://www.google.com/gmail/")
        driver.implicitly_wait(2000)

        #when
        loginField = driver.find_element_by_id ("identifierId")
        loginField.send_keys("karolina.korbas1@gmail.com")
        #and
        buttonNext = driver.find_element_by_class_name("RveJvd")
        buttonNext.click()
        self.driver.implicitly_wait(2000) 

        #and
        driver.find_element_by_name("password").send_kyes("wrong password")
        driver.find_element_by_class_name("RveJvd").click()
        self.driver.implicitly_wait(2000)

        #then
        warningDiv = driver.find_element_by_class_name("dEOOab")
        warningText = warningDiv.text
        assert( warningText == "Wrong password. Try again or click Forgot password to reset it." )
        
        
    def tearDown(self):
        self.driver.close()
        
        
        
        
              