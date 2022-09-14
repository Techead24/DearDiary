from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

import time



class E2E_DearDiary(LiveServerTestCase):
    
    def test_signup(self):
        driver = webdriver.Chrome()
                
        #Logging in
        time.sleep(5)
        
        driver.get('http://127.0.0.1:8000/login/')
        assert "My Diary" in driver.title
        
        driver.find_element(By.ID, 'signup').send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.ID, 'id_username').send_keys('mike')
        time.sleep(3)
        driver.find_element(By.ID, 'id_email').send_keys('mike@mike.com')
        time.sleep(3)
        driver.find_element(By.ID, 'id_password1').send_keys('money191')
        time.sleep(3)
        driver.find_element(By.ID, 'id_password2').send_keys('money191')
        time.sleep(3)
        driver.find_element(By.ID, 'signup-btn').send_keys(Keys.RETURN)
        time.sleep(3)
    
    
    def test_loginpage(self):
        driver = webdriver.Chrome()
        
        time.sleep(5)
        
        driver.get('http://127.0.0.1:8000/login/')
        assert "My Diary" in driver.title

        username = driver.find_element(By.ID, 'id_username')
        password = driver.find_element(By.ID, 'id_password')
        login = driver.find_element(By.ID, 'login-btn')
        
        time.sleep(5)
        
        username.send_keys('harry')
        password.send_keys('Testing123456')
        login.send_keys(Keys.RETURN)
        
        assert 'uche' in driver.page_source
        
        
        
    def test_createentry(self):
        driver = webdriver.Chrome()
        
        time.sleep(5)
        
        driver.get('http://127.0.0.1:8000/login/')
        assert "My Diary" in driver.title

        username = driver.find_element(By.ID, 'id_username')
        password = driver.find_element(By.ID, 'id_password')
        login = driver.find_element(By.ID, 'login-btn')
        
        time.sleep(5)
    
        username.send_keys('harry')
        password.send_keys('Testing123456')
        login.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        
        driver.get('http://127.0.0.1:8000')
        
        
        time.sleep(5)
        
        driver.find_element(By.ID,'addentry').send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.ID, 'id_title').send_keys('automated test')
        time.sleep(3)
        driver.find_element(By.ID,'id_content').send_keys('automation is cool!')
        time.sleep(3)
        driver.find_element(By.ID, 'save').send_keys(Keys.RETURN)
        time.sleep(5)
       
    
    
    def test_edit_del_entry(self):
        driver = webdriver.Chrome()
        
        #Logging in
        time.sleep(5)
        
        driver.get('http://127.0.0.1:8000/login/')
        assert "My Diary" in driver.title

        username = driver.find_element(By.ID, 'id_username')
        password = driver.find_element(By.ID, 'id_password')
        login = driver.find_element(By.ID, 'login-btn')
        
        time.sleep(5)
    
        username.send_keys('harry')
        password.send_keys('Testing123456')
        login.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        #getting to entry list view
        driver.get('http://127.0.0.1:8000')
        
        #editing an entry
        driver.find_element(By.ID, 'entry-title').send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.ID, 'edit').send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.ID, 'id_title').send_keys('auto editing')
        time.sleep(3)
        driver.find_element(By.ID,'id_content').send_keys('auto editing')
        time.sleep(5)
        driver.find_element(By.ID, 'save').send_keys(Keys.RETURN)
        time.sleep(5)
        
        
        #deleting an entry
        driver.find_element(By.ID, 'delete').send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.ID, 'confirm-del').send_keys(Keys.RETURN)
        time.sleep(3)
        
        #navigating to profile
        driver.find_element(By.CLASS_NAME, 'profile').send_keys(Keys.RETURN)
        time.sleep(3)
        
    
        #logging out
        driver.find_element(By.CLASS_NAME, 'logout').send_keys(Keys.RETURN)
        time.sleep(3)


        

    


    

