from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        wait = WebDriverWait(self.browser, 10)
        usernameInput = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")))
        passwordInput = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")))

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(50)



instgrm = Instagram(username, password)
instgrm.signIn()