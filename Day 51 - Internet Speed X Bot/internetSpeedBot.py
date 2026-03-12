import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

SPEED_TEST_URL = "https://www.speedtest.net/"

class InterNetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 90)
    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        try:
            cookie_button = self.wait.until(ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            cookie_button.click()
            print("Accepted cookies.")
        except TimeoutException:
            print("No cookie banner found, proceeding...")

        go_button = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".js-start-test")))
        go_button.click()
        print("Start Button Clicked. Waiting ~60 seconds for the test to complete...")

        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "eot-info")))
        download_element = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload_element = self.driver.find_element(By.CLASS_NAME, "upload-speed")

        self.down = float(download_element.text)
        self.up = float(upload_element.text)

        print(f"Test Complete! \nDownload: {self.down} Mbps \nUpload: {self.up} Mbps")

        self.driver.quit()
    def tweet_at_provider(self):
        pass