import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


class InstagramParser:
    def __init__(self, driver, username, password) -> None:
        self.driver = driver
        self.username = username
        self.password = password

    def accept_cookies(self) -> None:
        try:
            accept_button = self.driver.find_element(
                By.CSS_SELECTOR, "button._a9--._ap36._a9_0"
            )
            accept_button.click()
            time.sleep(2)
        except Exception as e:
            print("Error while accepting cookies:", e)

    def login(self) -> None:
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        self.accept_cookies()
        time.sleep(2)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(self.username)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_profile_info(self, profile_url) -> tuple[dict, str]:
        self.driver.get(profile_url)
        time.sleep(3)
        try:
            full_name = self.driver.find_element(
                By.CSS_SELECTOR, "div.x9f619 > span.x1lliihq"
            )
            full_name = full_name.text
        except NoSuchElementException as e:
            full_name = None
        try:
            description = self.driver.find_element(
                By.CSS_SELECTOR, "span._ap3a._aaco._aacu._aacx._aad7._aade"
            )
            description = description.text
        except NoSuchElementException as e:
            description = None

        bio = {"full_name": full_name, "description": description}

        profile_img = self.driver.find_element(By.CSS_SELECTOR, "a[role='link'] img")
        img_url = profile_img.get_attribute("src")

        return bio, img_url

    @staticmethod
    def download_img(url, save_path="data/profile_img.jpg") -> str:
        response = requests.get(url)
        with open(save_path, "wb") as file:
            file.write(response.content)

        return save_path
