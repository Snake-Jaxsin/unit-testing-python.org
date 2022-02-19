import unittest
from selenium import webdriver as wd
import page

class PageOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setUp")
        # Browser and webdriver Path
        self.driver_path = "/usr/local/bin/chromedriver"
        self.brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        # Options/Browser settings
        self.option = wd.ChromeOptions()
        self.option.binary_location = self.brave_path
        # self.option.add_argument("--incognito")
        # self.option.add_argument("--headless") OPTIONAL
    # Instance of Chrome
        self.driver = wd.Chrome(executable_path=self.driver_path, options=self.option)
        self.driver.get("http://www.python.org")

    #def test_title(self):
        #mainPage = page.MainPage()
        #assert mainPage.is_title_matchs()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matchs()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
