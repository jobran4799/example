import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class PressOnMuteClicker(BasePage):
    MUTE_BUTTON = "//button[@aria-label='Mute']"

    def __init__(self, driver):
        super().__init__(driver)

    def press_mute_mode_button(self):
        print("Waiting for mute button...")
        mute_button = WebDriverWait(self._driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.MUTE_BUTTON)))
        print("Mute button found. Clicking...")
        mute_button.click()


