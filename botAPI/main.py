import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

from botAPI.parser import InstagramParser
from botAPI.data_analyzer import img_description
from botAPI.message_generator import get_message

load_dotenv()


def main(profile_url: str) -> None:
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    parser = InstagramParser(driver, username, password)
    parser.login()

    bio, img_url = parser.get_profile_info(profile_url)

    img_desc = img_description(img_url)
    print(get_message(bio, img_desc))
    driver.quit()


if __name__ == "__main__":
    target_profile_url = ""
    main(target_profile_url)
