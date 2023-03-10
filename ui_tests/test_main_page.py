import os

import allure
import pytest
import requests
from allure import severity, severity_level

from ui_tests.pages.data import MainPageData
from ui_tests.pages.locators import MainPageLocators
from ui_tests.pages.main_page import MainPage

# username = os.environ.get('USERNAME') or 'username'
# password = os.environ.get('PASSWORD') or 'password'


class TestMainPage:
    URL = f'https://fojin.tech/ru'

    @allure.title('The server is alive')
    @severity(severity_level.BLOCKER)
    @allure.feature('User can see the main page')
    def test_main_page_response(self) -> None:
        """
        server is alive
        """
        r = requests.get(self.URL)
        assert r.status_code == 200, f'Server returned {r.status_code} status code'

    @severity(severity_level.CRITICAL)
    @allure.feature('User can go to all top links')
    @allure.title('User can see and go to the "{endpoint}" link')
    @pytest.mark.parametrize('endpoint, locator', list(zip(MainPageData.ENDPOINTS, MainPageData.LINKS_LIST)))
    def test_link_names(self, browser, endpoint: str, locator: tuple) -> None:
        """
        user can go to all top links from the main page
        """
        page = MainPage(browser, self.URL)
        page.open()
        page.scroll_to_and_click_element(locator)
        page.expl_wait_for_page_download(endpoint)
        page.should_be_some_page(endpoint)

    @severity(severity_level.MINOR)
    @allure.feature('User can go to the policy page and to the social page links')
    @allure.title('User can see and go to the "{element}" link')
    @pytest.mark.parametrize('element, locator',
                             list(zip(MainPageData.BOTTOM_ENDPOINTS, MainPageData.BOTTOM_ELEM_LIST)))
    def test_bottom_elements_are_active(self, element: str, locator: tuple, browser) -> None:
        """
        user can go to all bottom links from the main page
        """
        page = MainPage(browser, self.URL)
        page.open()
        page.scroll_to_the_bottom()
        if page.is_element_present(MainPageLocators.COOKIES):
            page.scroll_to_and_click_element(MainPageLocators.COOKIES)
        page.scroll_to_and_click_element(locator)
        if element != 'policy':
            page.next_window()
        page.expl_wait_for_page_download(element)
        page.should_be_some_page(element)
