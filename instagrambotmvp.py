from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com')
        
        sleep(5)
        
        
    def login(self, username, password):
        self.username_field = self.driver.find_element(by=By.NAME, value="username")
        self.username_field.send_keys(username)
        sleep(2)
        self.password_field = self.driver.find_element(by=By.NAME, value="password")
        self.password_field.send_keys(password, Keys.ENTER)
        sleep(5)

        
    def findFollowers(self):
        url_perfil = 'https://www.instagram.com/' + SIMILAR_ACCOUNT
        url_followers = 'https://www.instagram.com/' + SIMILAR_ACCOUNT + '/followers'
        self.driver.get(url_perfil)
        sleep(3)
        self.driver.get(url_followers)
        sleep(5.2)
        modal_xpath = "//div[@class='_aano']"
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
        self.button_list = self.driver.find_elements(By.XPATH, value="//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1') and contains(@class, '_ap30')]")
        
        
    def followAll(self):
        for element in self.button_list:
            cont = 0
            try:
                sleep(5)
                element.click()
                cont =+ 1
                print(f'{cont} Pessoa seguida!')
                sleep(2)
            except ElementClickInterceptedException:
                print('Deu ruim')
                continue
        

# if __name__ == '__main__':
#     instagramBot = InstaFollower()
#     instagramBot.login()
#     # instagramBot.findFollowers()
#     # instagramBot.followAll()