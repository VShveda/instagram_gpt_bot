import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


class InstagramParser:
    def __init__(self, driver, username, password) -> None:
        self.driver = driver
        self.username = username
        self.password = password

    def login(self) -> None:
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(self.username)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_profile_info(self, profile_url) -> tuple[dict, str]:
        self.driver.get(profile_url)
        time.sleep(3)

        full_name = self.driver.find_element(By.CSS_SELECTOR, "div.x9f619 > span.x1lliihq")
        description = self.driver.find_element(By.CSS_SELECTOR, "span._ap3a._aaco._aacu._aacx._aad7._aade")

        bio = {"full_name": full_name.text, "description": description.text}

        profile_img = self.driver.find_element(By.CSS_SELECTOR, "a[role='link'] img")
        img_url = profile_img.get_attribute("src")

        return bio, img_url
