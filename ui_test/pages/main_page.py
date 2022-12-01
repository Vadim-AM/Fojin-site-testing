from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    def __init__(self, browser, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: By, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_active(self, how: By, what):
        return self.browser.find_element(how, what).is_enabled()

    def find_and_click_element(self, locator: tuple):
        element = self.browser.find_element(*locator)
        element.click()

    def should_be_some_page(self, page_name: str):
        assert page_name in self.browser.current_url, self.browser.current_url

    def scroll_to_the_bottom(self):
        html = self.browser.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)

    def expl_wait_for_visibility(self, element: str):
        WebDriverWait(self.browser, 5).until(EC.url_contains(element))

    def next_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
