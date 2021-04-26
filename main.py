import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 20
PROMISED_UP = 60
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.upload = 0
        self.download = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 180)

        go_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "start-text")))
        go_button.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "result-container-meta")))
        self.upload = self.driver.find_element_by_class_name("upload-speed").text
        self.download = self.driver.find_element_by_class_name("download-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        wait = WebDriverWait(self.driver, 180)

        wait.until(EC.presence_of_element_located((By.NAME, "redirect_after_login")))
        username_input = self.driver.find_element_by_name("session[username_or_email]")
        username_input.clear()
        username_input.send_keys(TWITTER_EMAIL)
        password_input = self.driver.find_element_by_name("session[password]")
        password_input.clear()
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()
