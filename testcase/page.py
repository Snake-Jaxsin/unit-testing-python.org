from locator import *
from element import BasePageElement

class SearchBaseElement(BasePageElement):
    locator = "q"

class GoButtonElement(BasePageElement):
    locator = "go"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchBaseElement()

    def is_title_matchs(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source

