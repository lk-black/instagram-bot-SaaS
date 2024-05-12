from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com')
        
        sleep(3)
        
        
    def login(self, username, password):
        self.username_field = self.driver.find_element(by=By.NAME, value="username")
        self.username_field.send_keys(username)
        sleep(2)
        self.password_field = self.driver.find_element(by=By.NAME, value="password")
        self.password_field.send_keys(password, Keys.ENTER)
        sleep(3)
        
        
    def findFollowers(self, target_account_url, number_following_per_hour, time_for_each_follow):
        self.number_following_per_hour = int(number_following_per_hour)
        self.time_for_each_follow = int(time_for_each_follow)
        self.target_account_url = target_account_url
        target_account_followers_url = self.target_account_url + 'followers'
        
        self.driver.get(self.target_account_url)
        sleep(2)
        self.driver.get(target_account_followers_url)
        sleep(4)
        
        modal_xpath = "//div[@class='_aano']"
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1)
        self.button_list = self.driver.find_elements(By.XPATH, value="//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1') and contains(@class, '_ap30')]")

        
    def followAll(self):
        count = self.number_following_per_hour
        interval = self.time_for_each_follow / 2
        
        for element in self.button_list:
            try:
                sleep(interval)
                element.click()
                count =- 1
                sleep(interval)
            except ElementClickInterceptedException:
                print('Deu ruim')
                continue
            if count == 0:
                break
        

# if __name__ == '__main__':
#     instagramBot = InstaFollower()
#     instagramBot.login()
#     # instagramBot.findFollowers()
#     # instagramBot.followAll()