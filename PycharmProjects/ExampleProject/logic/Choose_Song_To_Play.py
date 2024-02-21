import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class YouTubeSearchPage(BasePage):
    SEARCH_INPUT = "//input[@id='search']"
    SEARCH_BUTTON = "//button[@id='search-icon-legacy']"
    VIDEO_LINK = "(//a[@id='video-title'])[1]"  # Assuming we select the first video

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_song(self, song_name):
        search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search_input.send_keys(song_name)
        search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
        search_button.click()

    # def choose_video_to_play(self):
    #     video_link = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.VIDEO_LINK)))
    #     video_link.click()
    #     time.sleep(25)
    def choose_video_to_play(self):
        video_link = WebDriverWait(self._driver, 60).until(EC.presence_of_element_located((By.XPATH, self.VIDEO_LINK)))
        video_link.click()

