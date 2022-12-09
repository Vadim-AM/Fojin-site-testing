import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui_tests.pages.data import FormData


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser that the automation will run in")


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    yield browser
    browser.quit()


# @pytest.fixture(params=["chrome"])
# def browser(request):
#     """
#     the fixture downloads the latest driver and creates the browser instance with passed options
#     """
#     headless = False  # changes the headless parameter for all browsers
#     match request.param:
#         case "chrome":
#             options = webdriver.ChromeOptions()
#             options.headless = headless
#             options.add_argument('--no-sandbox')
#             options.add_argument("--disable-dev-shm-usage")
#             browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#         case "firefox":
#             options = webdriver.FirefoxOptions()
#             options.headless = headless
#             options.add_argument('--no-sandbox')
#             options.add_argument("--disable-dev-shm-usage")
#             browser = webdriver.Firefox(GeckoDriverManager().install(), options=options)
#     request.cls.driver = browser
#     browser.maximize_window()
#     yield browser
#     browser.quit()


@pytest.fixture()
def positive_data_case() -> list[tuple[tuple, list]]:
    """
    The fixture returns list of tuples with locators and data passed into fields
    """
    return list(zip(FormData.LOCATORS, FormData.POSITIVE_CASE))


@pytest.fixture(params=FormData.NEGATIVE_CASES)
def negative_data_case(request) -> list[tuple[tuple, list]]:
    """
    The fixture calls one time for each parameter and return values one by one
    """
    return list(zip(FormData.LOCATORS, request.param))
