from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest
import openpyxl
from constants import globalConstants as c


class Test_Case_Homework1:
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window() 

    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()

    def test_invalid_login1(self):
        usernameInput=self.driver.find_element(By.ID,c.USERNAME_ID).send_keys("")
        passwordInput=self.driver.find_element(By.ID,c.PASSWORD_ID).send_keys("")
        loginButton=self.driver.find_element(By.ID,c.LOGIN_BUTTON_ID).click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Username is required"
        sleep(1)

    def test_invalid_login2(self):
        usernameInput=self.driver.find_element(By.ID,c.USERNAME_ID).send_keys("standard_user")
        passwordInput=self.driver.find_element(By.ID,c.PASSWORD_ID).send_keys("")
        loginButton=self.driver.find_element(By.ID,c.LOGIN_BUTTON_ID).click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Password is required"
        sleep(1)
    
    def test_invalid_login3(self):
        usernameInput=self.driver.find_element(By.ID,c.USERNAME_ID).send_keys("locked_out_user")
        passwordInput=self.driver.find_element(By.ID,c.PASSWORD_ID).send_keys("secret_sauce")
        loginButton=self.driver.find_element(By.ID,c.LOGIN_BUTTON_ID).click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        sleep(1)
    
    def test_valid_login(self):
        usernameInput=self.driver.find_element(By.ID,c.USERNAME_ID).send_keys("standard_user")
        passwordInput=self.driver.find_element(By.ID,c.PASSWORD_ID).send_keys("secret_sauce")
        loginButton=self.driver.find_element(By.ID,c.LOGIN_BUTTON_ID).click()
        listOfInventory=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(listOfInventory)== 6
        sleep(1)

       