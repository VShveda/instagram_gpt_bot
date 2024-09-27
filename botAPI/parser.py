import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstagramParser:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(self.username)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
