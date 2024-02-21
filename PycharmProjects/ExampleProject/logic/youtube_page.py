from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class YouTubePage(BasePage):
    SEARCH_INPUT = "//input[@id='search']"

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)

    def fill_search_input(self, text):
        self.search_input.send_keys(text)  # logic

    def press_enter_on_search_input(self,text):
        # WebDriverWait(self._driver, 10).until(EC.title_contains(text))
        # self.search_input.send_keys(Keys.RETURN)
        self.search_input.send_keys(text, Keys.RETURN)
        WebDriverWait(self._driver, 10).until(EC.title_contains(text))

    def search_flow(self, text):
        self.fill_search_input(text)
        self.press_enter_on_search_input(text)



