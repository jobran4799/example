import time
import unittest

from selenium.common import TimeoutException

from infra.browser_wrapper import BrowserWrapper
from logic.Choose_Category import Choose_Category
from logic.Choose_Song_To_Play import YouTubeSearchPage
from logic.History_Page import YouTubeHistoryPage
from logic.Press_On_Mute_Clicker import PressOnMuteClicker
from logic.youtube_page import YouTubePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Press_On_Mute_Clicker:
    pass


class Youtube_Page_Test(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")

    def test_check_title_for_search(self):
        self.youtube_page = YouTubePage(self.driver)
        self.youtube_page.search_flow("Python programming")
        WebDriverWait(self.driver, 20).until(EC.title_contains("Python programming"))
        self.assertIn("Python programming", self.driver.title, "the title not show")
    #
    # def test_choose_category(self):
    #     self.youtube_Choose_Category = Choose_Category(self.driver)
    #     self.youtube_Choose_Category.navigate_to_categories()
    #     self.youtube_Choose_Category.choose_category("Music")
    #     try:
    #         WebDriverWait(self.driver, 20).until(EC.alert_is_present())
    #         alert = self.driver.switch_to.alert
    #         print("Alert text:", alert.text)
    #         # Handle the alert if necessary
    #         # For example, you can accept the alert using alert.accept()
    #     except TimeoutException:
    #         print("No alert found within the specified timeout period.")
    #     self.assertTrue(self.youtube_Choose_Category,"Category not fuound")
    #
    #
    # def test_enter_history_list_play(self):
    #     self.youtube_history_page = YouTubeHistoryPage(self.driver)
    #     self.youtube_history_page.navigate_to_history()
    #     self.assertTrue(self.youtube_history_page,"History list doesn't Showed up")
    #
    # def test_choose_song_to_play(self):
    #     self.youtube_search_page = YouTubeSearchPage(self.driver)
    #     self.youtube_search_page.search_for_song("liszt- la campanella")
    #     self.youtube_search_page.choose_video_to_play()
    #     self.assertTrue(self.youtube_search_page,"sound doesn't played")
    #
    # def test_press_mute_mode(self):
    #     self.youtube_search_page = YouTubeSearchPage(self.driver)
    #     self.youtube_player_page = PressOnMuteClicker(self.driver)
    #
    #     # Search for a song and play it
    #     self.youtube_search_page.search_for_song("liszt- la campanella")
    #     self.youtube_search_page.choose_video_to_play()
    #     time.sleep(10)
    #
    #     # Press mute mode button after 10 seconds
    #     self.youtube_player_page.press_mute_mode_button()
    #
    #     # Wait for another 10 seconds while the song continues playing
    #     time.sleep(10)
    #     self.assertTrue(self.youtube_player_page,"song doesn't been stopped")

    def tearDown(self):
        self.driver.close()


