import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from infra.base_page import BasePage


class YouTubeHistoryPage(BasePage):
    HISTORY_MENU = "//a[@title='History']"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_history(self):
        print("Navigating to history...")
        try:
            history_menu = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.HISTORY_MENU)))
            print("History menu found. Clicking...")
            history_menu.click()
            print("Clicked on history menu.")
            WebDriverWait(self._driver, 5).until(EC.alert_is_present())
            time.sleep(4)
        except Exception as e:
            print("Failed to navigate to history page:", str(e))