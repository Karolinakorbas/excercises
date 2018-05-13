from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from test.test_robotparser import PasswordProtectedSiteTestCase

class SendemailTest(unittest.TestCase):

def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()

def test_sendWithCorrectRecipientTest(self):
    
    #given
    driver = self.driver
    self.loginToGmailAccount('karolina.korbas1@gmail.com', 'password')

    #and
    composeButton = driver.find_element_by_xpath("//div[contains(@text, 'COMPOSE')]")
    composeButton.click()
    self.driver.implicitly_wait(3000) 
    
    #and
    recipientField= driver.find_element_by_name("to")
    recipientField.send_keys("test.mail12345@gmail.com")
   
    #and
    emailtext = driver.find_element_by_class_name("Am Al editable LW-avf")
    emailtext.send_keys("This is message.")
    
    #and
    sendButton= driver.find_element_by_id("118")
    sendButton.click()
    self.driver.implicitly_wait(3000) 
    
    Assert(river.find_by_class_name("vh").text == "Your message has been sent. View message”)
    
def loginToGmailAccount(self, user, password): 
    driver = self.driver
    driver.get("https://www.google.com/gmail/")
    driver.implicitly_wait(1000)

    loginField = driver.find_element_by_id ("identifierId")
    loginField.send_keys(user)
    
    buttonNext = driver.find_element_by_class_name("RveJvd")
    buttonNext.click()
    self.driver.implicitly_wait(1000)    
    
    driver.find_element_by_name("password").send_kyes("password1")
    driver.find_element_by_class_name("RveJvd").click()
    self.driver.implicitly_wait(2000)
    
def tearDown(self):
    self.driver.close()
        
        
        
        
              
