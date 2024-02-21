from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from selenium.webdriver.common.by import By

class Choose_Category(BasePage):
    CATEGORIES_MENU = "//a[@title='Categories']"
    CATEGORY_OPTION = "//a[contains(@href, '/channel/')]"  # XPath for category options

    def __init__(self, driver):
        super().__init__(driver)


    def navigate_to_categories(self):
        print("Navigating to categories...")
        try:
            categories_menu = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CATEGORIES_MENU)))
            print("Categories menu found. Clicking...")
            categories_menu.click()
        except Exception as e:
            print("Failed to navigate to categories:", str(e))
    def choose_category(self, category_name):
        category_option = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"{self.CATEGORY_OPTION}[contains(text(), '{category_name}')]")))
        category_option.click()

