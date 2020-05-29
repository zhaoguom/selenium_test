import unittest
from selenium import webdriver
from pages.searchPage import SearchPage

class TestSearchPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearch(self):
        driver = self.driver
        url = "https://www.baidu.com"
        text = "selenium"
        assert_title = "selenium_百度搜索"

        search_page = SearchPage(driver, url)
        search_page.goto_homepage()
        search_page.input_search_text(text)
        search_page.click_search_btn()
        import time
        time.sleep(10)
        self.assertEqual(search_page.get_title(), assert_title)

    def tearDown(self):
        self.driver.quit()