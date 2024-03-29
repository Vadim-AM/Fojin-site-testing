"""Contains data for tests"""
from ui_tests.pages.locators import CasesLocators, MainPageLocators


class MainPageData:
    """Contains links and endpoints for the main page"""
    URL = 'https://fojin.tech/ru'

    links_list: list[tuple[str, str]] = [
        MainPageLocators.MAIN_PAGE,
        MainPageLocators.ABOUT_US,
        MainPageLocators.SERVICES,
        MainPageLocators.STACK,
        MainPageLocators.CASES,
        MainPageLocators.CONTACTS
    ]
    endpoints: list[str] = ['', 'about-us', '', '', 'cases', 'contacts']

    bottom_elem_list: list[tuple[str, str]] = [
        MainPageLocators.VK,
        MainPageLocators.TELEGRAM
    ]

    bottom_endpoints: list[str] = ['vk.com/fojin', 't.me/fojin_tech']

    main_page_data_list = list(zip(endpoints, links_list))
    main_page_bottom_list = list(zip(bottom_endpoints, bottom_elem_list))


class CasesData:
    """Contains lists from endpoints and locators for the case page check"""

    URL = 'https://fojin.tech/cases/'

    cases_nums_list: list[str] = list('123456789')

    locators: list[tuple[str, str]] = [
        CasesLocators.CASE_1,
        CasesLocators.CASE_2,
        CasesLocators.CASE_3,
        CasesLocators.CASE_4,
        CasesLocators.CASE_5,
        CasesLocators.CASE_6,
        CasesLocators.CASE_7,
        CasesLocators.CASE_8,
        CasesLocators.CASE_9,
    ]
    cases_list = list(zip(cases_nums_list, locators))


class FormData:
    """Contains data for the form"""

    positive_case: list[str] = [['test_user', 'test@fojin.tech', '12345678901', 'some useless information']]
    success_text: str = 'Сообщение отправлено. В ближайшее время мы с вами свяжемся'
    unsuccessful_text: str = 'Подтвердите согласие на обработку персональных данных'
    negative_case_1: list[str] = ['          ', 'test@fojin.com', '12345678901', 'some useless information']
    negative_case_2: list[str] = ['test_user', '', '12345678901', 'some  information']
    negative_case_3: list[str] = ['test_user', 'test@fojin.ru', '   ', ' useless information']
    negative_case_4: list[str] = ['test_user', 'test@fojin.fr', '12345678901', '     ']
    negative_cases: list[list[str]] = [negative_case_1, negative_case_2, negative_case_3, negative_case_4]
