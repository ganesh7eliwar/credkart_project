import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from utilities.read_config import ReadConfigPD
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')
URL = ReadConfigPD.url()

""" ############################################# BROWSER SETUP #################################################### """

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--start-maximized')
chrome_serve_manager = Service(ChromeDriverManager().install())

firefox_serve_manager = Service(GeckoDriverManager().install())

headless_options = webdriver.ChromeOptions()
headless_options.add_experimental_option('excludeSwitches', ['enable-logging'])
headless_options.add_argument('--headless')


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def setup(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        print('\nTest Run on Chrome Browser.')
        driver = webdriver.Chrome(service=chrome_serve_manager, options=chrome_options)
    elif browser == 'firefox':
        print('\nTest Run on Firefox Browser.')
        driver = webdriver.Firefox(service=firefox_serve_manager)
        driver.maximize_window()
    else:
        print('\nTest Run on Headless Browser.')
        driver = webdriver.Chrome(service=chrome_serve_manager, options=headless_options)
    driver.implicitly_wait(10)
    driver.get(URL)
    yield driver
    driver.quit()


""" ######################################### HTML REPORT GENERATION ############################################### """


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('Platform', None)
    metadata.pop('JAVA_HOME', None)


@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath = f'./html_reports/html_reports_{now}.html'


""" ########################################### PARAMETERIZED TEST ################################################# """


@pytest.fixture(params=[
    ('david_shearing@yahoomail.com', '$lA6(3Bg1#vI!uzFE', 'Pass'),
    ('david_shearing@yahoomail.com', '$lA6(3g1#vI!uzFE', 'Fail'),
    ('david_shearing@gmail.com', '$lA6(3Bg1#vI!uzFE', 'Fail'),
    ('david_shearing@credence.in', '$lA6(3g1#vI!uzFE', 'Fail')
])
def data_for_login(request):
    return request.param
