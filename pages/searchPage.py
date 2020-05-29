from pages.basePage import Page
from selenium.webdriver.common.by import By


class SearchPage(Page):
    search_input = (By.ID, 'kw')
    search_button = (By.ID, 'su')

    def __init__(self, driver, base_url="http://www.baidu.com"):
        Page.__init__(self, driver, base_url)

    def goto_homepage(self):
        self.driver.get(self.base_url)

    def input_search_text(self, text="selenium"):
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        self.click(self.search_button)
