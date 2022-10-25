from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
chrome_driver = os.getenv('driver')

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def log_in(self, email, password):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(email)
        login_btn = self.driver.find_element_by_name('password')
        login_btn.send_keys(password)
        login_btn.send_keys(Keys.ENTER)
        sleep(5)
        self.driver.get('https://www.instagram.com/python.advance.projects/')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(5)
        all_btn = self.driver.find_elements_by_css_selector('li button')
        for i in all_btn:
            i.click()
            sleep(2)


bot = InstagramBot()
bot.log_in(EMAIL, PASSWORD)
