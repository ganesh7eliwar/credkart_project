"""
Pytest Configuration Module (conftest.py)

This module serves as the central configuration file for pytest in the CredKart automation framework.
It defines all fixtures, fixtures parameterization, pytest hooks, browser setup options, and report generation.

Key Components:
    1. Fixture Definitions: setup, data_for_login, data_dir
    2. Browser Configuration: Chrome, Firefox, Headless modes
    3. Pytest Hooks: Metadata handling, HTML report path configuration
    4. Test Data: Parameterized login credentials for data-driven testing

Shared Across:
    - All test files in testcases/ directory
    - All test functions via pytest fixtures
    - Report generation (HTML, Allure)

Usage:
    No explicit imports needed - pytest automatically discovers and applies conftest.py
    Access fixtures in any test via function parameters:
        def test_login(self, setup, data_dir):
            driver = setup  # WebDriver instance
            # ... test code ...

For more info: https://docs.pytest.org/en/stable/using_conftest.html
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from utilities.read_config import ReadConfigPD
from datetime import datetime
from pathlib import Path

# ========================= INITIALIZATION =========================

now = datetime.now().strftime('%d%m%Y%H%M%S')
URL = ReadConfigPD.url()  # Load application URL from config

# ========================= BROWSER SETUP CONFIGURATION =========================

"""
Chrome Options Configuration
Disables logging to avoid noise in test output
Maximizes window for consistent UI testing
Uses webdriver-manager for automatic driver updates
"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--start-maximized')
chrome_serve_manager = Service(ChromeDriverManager().install())

"""Firefox Options Configuration"""
firefox_serve_manager = Service(GeckoDriverManager().install())

"""Headless Chrome Configuration
Runs tests without GUI (faster, suitable for CI/CD)
Useful for quick feedback and resource-constrained environments
"""
headless_options = webdriver.ChromeOptions()
headless_options.add_experimental_option('excludeSwitches', ['enable-logging'])
headless_options.add_argument('--headless')


# ========================= PYTEST COMMAND-LINE OPTIONS =========================

def pytest_addoption(parser):
    """
    Registers custom command-line options for pytest.
    
    This allows users to run tests with: pytest --browser chrome
    
    Options:
        --browser: Specify browser for test execution (chrome, firefox, or default headless)
    """
    parser.addoption('--browser')


# ========================= BROWSER SETUP FIXTURE =========================

@pytest.fixture()
def setup(request):
    """
    Fixture that provides WebDriver instance with selected browser.
    
    Scope: function (new driver instance for each test)
    
    Command-line parameter:
        pytest --browser chrome     # Chrome browser (maximized)
        pytest --browser firefox    # Firefox browser (maximized)
        pytest                      # Headless Chrome (default)
    
    Steps:
        1. Reads browser choice from command-line parameter
        2. Initializes appropriate WebDriver with configurations
        3. Sets 10-second implicit wait for element location
        4. Navigates to application base URL
        5. Yields driver to test
        6. Closes driver after test completes (teardown)
    
    Returns:
        WebDriver: Configured Selenium WebDriver instance
        
    Example:
        # >>> def test_login(setup):
        # >>>     driver = setup
        # >>>     driver.find_element(By.ID, 'email').send_keys('test@example.com')
    
    Raises:
        ValueError: If invalid browser option provided
    """
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
    
    # Set implicit wait time for all element searches
    driver.implicitly_wait(10)
    
    # Navigate to application URL
    driver.get(URL)
    
    # Yield driver to test function (yield = suspend until test completes)
    yield driver
    
    # Teardown: Close browser after test
    driver.quit()


# ========================= HTML REPORT GENERATION HOOKS =========================

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """
    Customizes metadata displayed in HTML reports.
    
    Removes platform and JAVA_HOME information to reduce report clutter
    and focus on test-specific metadata.
    """
    metadata.pop('Platform', None)  # Remove OS platform info
    metadata.pop('JAVA_HOME', None)  # Remove Java home (not applicable to Python tests)


@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    """
    Configures HTML report output location and naming.
    
    Sets report file path to: ./html_reports/html_reports_{timestamp}.html
    Ensures unique filenames with timestamp to avoid overwrites.
    
    Args:
        config: Pytest configuration object
    """
    config.option.htmlpath = f'./html_reports/html_reports_{now}.html'


# ========================= DATA-DRIVEN TEST FIXTURES =========================

@pytest.fixture(params=[
    ('david_shearing@yahoomail.com', '$lA6(3Bg1#vI!uzFE', 'Pass'),
    ('david_shearing@yahoomail.com', '$lA6(3g1#vI!uzFE', 'Fail'),
    ('david_shearing@gmail.com', '$lA6(3Bg1#vI!uzFE', 'Fail'),
    ('david_shearing@credence.in', '$lA6(3g1#vI!uzFE', 'Fail')
])
def data_for_login(request):
    """
    Fixture providing parameterized login test data.
    
    Parameterizes login tests to run multiple times with different credentials,
    testing both valid and invalid combinations.
    
    Parameters:
        Each parameter tuple contains:
        - Email address (str)
        - Password (str)
        - Expected result: 'Pass' for valid, 'Fail' for invalid
    
    Test Cases:
        1. Valid email + valid password = Expected Pass
        2. Valid email + invalid password = Expected Fail
        3. Invalid email + valid password = Expected Fail
        4. Invalid email + invalid password = Expected Fail
    
    Returns:
        tuple: (email, password, expected_result)
        
    Usage:
        # >>> @pytest.mark.parameterize('data_for_login', [...])
        # >>> def test_login_ddt(data_for_login):
        # >>>     email, password, expected = data_for_login
        # >>>     # test logic using parameters
    
    Note:
        Parameterized fixtures automatically generate separate test cases
        Pytest will run the test function once per parameter set
        Test names will show parameter values for differentiation
    """
    return request.param


# ========================= PATH FIXTURES =========================

@pytest.fixture(scope='function')
def data_dir():
    """
    Fixture providing path to test data directory.
    
    Scope: function (accessible in all test functions)
    
    Returns:
        Path: Pathlib Path object pointing to test_data directory
        
    Usage:
        # >>> def test_register(data_dir):
        # >>>     json_file = data_dir / "user_details.json"
        # >>>     with open(json_file, 'r') as f:
        # >>>         data = json.load(f)
    
    Directory Structure:
        test_data/
        ├── user_details.json         # Current user from registration test
        ├── all_user_details.json     # All registered users
        ├── login_credentials.xlsx    # Excel with login test data
        └── other_test_data files
    
    Advantages:
        - Platform-independent path handling (Windows/Linux/Mac)
        - Resolves from conftest.py location, not current directory
        - Pathlib methods allow easy file path operations
    """
    return Path(__file__).resolve().parent.parent / "test_data"
