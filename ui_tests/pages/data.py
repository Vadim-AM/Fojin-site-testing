from ui_tests.pages.locators import FormLocators, CasesLocators, MainPageLocators


class MainPageData:
    LINKS_LIST: list[tuple[str, str]] = [
        MainPageLocators.MAIN_PAGE,
        MainPageLocators.ABOUT_US,
        MainPageLocators.SERVICES,
        MainPageLocators.STACK,
        MainPageLocators.CASES,
        MainPageLocators.CONTACTS
    ]
    ENDPOINTS: list[str] = ['', 'about-us', '', '', 'cases', 'contacts']

    BOTTOM_ELEM_LIST: list[tuple[str, str]] = [
        MainPageLocators.POLICY,
        MainPageLocators.VK,
        MainPageLocators.TELEGRAM
    ]

    BOTTOM_ENDPOINTS: list[str] = ['policy', 'vk.com/fojin', 't.me/fojin_tech']


class CasesData:
    CASES_LIST: list[str] = [i for i in '123456789']

    LOCATORS: list[tuple[str, str]] = [
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


class FormData:
    POSITIVE_CASE: list[str] = ['test_user', 'test@fojin.tech', '12345678901', 'some useless information']
    SUCCESS_TEXT: str = 'Сообщение отправлено. В ближайшее время мы с вами свяжемся'
    UNSUCCESSFUL_TEXT: str = 'Поле обязательно'
    LOCATORS: list[tuple[str, str]] = [
        FormLocators.NAME,
        FormLocators.EMAIL,
        FormLocators.NUMBER,
        FormLocators.ABOUT_PROJECT
    ]
    NEGATIVE_CASE_1: list[str] = ['          ', 'test@fojin.tech', '12345678901', 'some useless information']
    NEGATIVE_CASE_2: list[str] = ['test_user', '', '12345678901', 'some useless information']
    NEGATIVE_CASE_3: list[str] = ['test_user', 'test@fojin.tech', '   ', 'some useless information']
    NEGATIVE_CASE_4: list[str] = ['test_user', 'test@fojin.tech', '12345678901', '     ']
    NEGATIVE_CASES: list[list[str]] = [NEGATIVE_CASE_1, NEGATIVE_CASE_2, NEGATIVE_CASE_3, NEGATIVE_CASE_4]
