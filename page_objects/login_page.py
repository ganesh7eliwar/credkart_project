"""
Login Page Object Module

This module implements the Page Object Model (POM) for the CredKart login page.
It encapsulates all selectors and actions related to user authentication including
login, logout, and user profile verification.

Classes:
    LoginPage: Represents the login page and all its interactions

Usage Example:
    >>> from selenium import webdriver
    >>> from page_objects.login_page import LoginPage
    >>> driver = webdriver.Chrome()
    >>> driver.get('https://automation.credence.in/shop')
    >>> login_page = LoginPage(driver)
    >>> login_page.login()
    >>> login_page.user_email('test@example.com')
    >>> login_page.user_password('password123')
    >>> login_page.login_button()

Design Pattern:
    - Encapsulates all page-specific selectors as class variables
    - Provides method-based actions instead of exposing Selenium directly
    - Handles exceptions gracefully and returns meaningful errors
    - Integrates with Allure reporting for screenshots on pass/fail
"""

from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import allure

now = datetime.now().strftime('%d%m%Y%H%M%S')


class LoginPage:
    """
    Login Page Object for CredKart application.
    
    Encapsulates all interactions with the login page including element selectors,
    user authentication, logout functionality, and screenshot capture for reporting.
    
    Attributes:
        login_xpath (str): XPath selector for the Login button in navigation
        email_address_id (str): ID selector for email input field
        password_id (str): ID selector for password input field
        login_button_xpath (str): XPath selector for the form submit button
        logout_dd_css_selector (str): CSS selector for logout dropdown button
        logout_btn_xpath (str): XPath selector for the Logout menu item
        user_name_xpath (str): XPath selector for logged-in user display name
        wait (WebDriverWait): Explicit wait with 3-second timeout for element interactions
    """

    # ========================= PAGE ELEMENT SELECTORS =========================
    login_xpath = "//a[normalize-space()='Login']"  # Login link in navigation bar
    email_address_id = "email"  # Email input field on login form
    password_id = "password"  # Password input field on login form
    login_button_xpath = "//button[@type='submit']"  # Submit button on login form
    logout_dd_css_selector = "a[role='button']"  # Dropdown toggle for logout
    logout_btn_xpath = "//a[normalize-space()='Logout']"  # Logout menu item
    user_name_xpath = "//div[@id='navbar']/ul/li/a[@class='dropdown-toggle']"  # User display name

    def __init__(self, driver):
        """
        Initialize the LoginPage object.
        
        Args:
            driver (WebDriver): Selenium WebDriver instance for browser interaction
            
        Sets:
            self.driver: The WebDriver instance
            self.wait: WebDriverWait instance with 3-second timeout for explicit waits
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def login(self):
        """
        Clicks the Login link to navigate to log in form.
        
        This is the first step in the login workflow. It clicks the "Login" link
        in the navigation bar to open the login form modal/page.
        
        Returns:
            str: "Encountered an Error." if element not found or click fails
            None: On successful click
            
        Exceptions Handled:
            - TimeoutException: Element not visible within timeout
            - NoSuchElementException: Element not found in DOM
            - ElementClickInterceptedException: Element not clickable (blocked by other element)
        """
        try:
            login_button = self.driver.find_element(By.XPATH, self.login_xpath)
            login_button.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def user_email(self, email):
        """
        Enters user email address into the email input field.
        
        Args:
            email (str): User's email address (e.g., 'test@example.com')
            
        Returns:
            None
            
        Raises:
            NoSuchElementException: If email input field not found
            
        Example:
            # >>> login_page.user_email('john_doe@gmail.com')
        """
        email_text_box = self.driver.find_element(By.ID, self.email_address_id)
        email_text_box.send_keys(email)

    def user_password(self, password):
        """
        Enters user password into the password input field.
        
        Args:
            password (str): User's password in plain text
            
        Returns:
            None
            
        Raises:
            NoSuchElementException: If password input field not found
            
        Example:
            # >>> login_page.user_password('SecurePassword123!')
            
        Note:
            Password is sent directly using send_keys(); consider using
            pyperclip for additional security in sensitive environments.
        """
        password_text_box = self.driver.find_element(By.ID, self.password_id)
        password_text_box.send_keys(password)

    def login_button(self):
        """
        Clicks the login form submit button to authenticate.
        
        This is called after email and password have been entered.
        Triggers the authentication process on the backend.
        
        Returns:
            None
            
        Raises:
            NoSuchElementException: If login button not found
            
        Example:
            # >>> login_page.login_button()
            
        Note:
            After clicking, the page should redirect to the user dashboard
            if credentials are valid, or show error message if invalid.
        """
        login_btn = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_btn.click()

    def logout_dd_button(self):
        """
        Clicks the logout dropdown toggle button.
        
        Opens the dropdown menu containing the logout option.
        This is the first step in the logout process.
        
        Returns:
            str: "Encountered an Error." if element not found or click fails
            None: On successful click
            
        Exceptions Handled:
            - TimeoutException: Element not visible within timeout
            - NoSuchElementException: Element not found in DOM
            - ElementClickInterceptedException: Element blocked by overlay
        """
        try:
            logout_dd = self.driver.find_element(By.CSS_SELECTOR, self.logout_dd_css_selector)
            logout_dd.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def logout_button(self):
        """
        Clicks the Logout menu item from the dropdown.
        
        This is called after the logout dropdown has been opened.
        Completes the logout process and returns user to home page.
        
        Returns:
            str: "Encountered an Error." if element not found or click fails
            None: On successful click
            
        Exceptions Handled:
            - TimeoutException: Element not visible within timeout
            - NoSuchElementException: Element not found in DOM
            - ElementClickInterceptedException: Element blocked by overlay
        """
        try:
            logout_btn = self.driver.find_element(By.XPATH, self.logout_btn_xpath)
            logout_btn.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def user_name(self):
        """
        Retrieves the currently logged-in user's display name.
        
        This method extracts the username from the navigation bar dropdown
        that appears when a user is logged in. Used to verify successful login.
        
        Returns:
            str: Logged-in user's name from the page
            str: "Encountered an Error." if element not found
            
        Example:
            # >>> logged_in_user = login_page.user_name()
            # >>> # Returns: 'David Shearing'
            
        Exceptions Handled:
            - TimeoutException: Element not visible within timeout
            - NoSuchElementException: Element not found (user may not be logged in)
            - ElementClickInterceptedException: Element blocked by overlay
        """
        try:
            user_name = self.driver.find_element(By.XPATH, self.user_name_xpath).text
            return user_name
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    # ========================= SCREENSHOT CAPTURE METHODS =========================
    
    def screenshot_on_pass(self):
        """
        Captures a screenshot on successful login and saves to local filesystem.
        
        File location: ./screenshots/Test_Login_Pass_{timestamp}.png
        
        Returns:
            None
            
        Example:
            # >>> login_page.screenshot_on_pass()
            # >>> # Saves file like: Test_Login_Pass_15012025103045.png
        """
        self.driver.save_screenshot(f'./screenshots/Test_Login_Pass_{now}.png')

    def screenshot_on_fail(self):
        """
        Captures a screenshot on failed login and saves to local filesystem.
        
        File location: ./screenshots/Test_Login_Fail_{timestamp}.png
        Useful for debugging failed authentication attempts.
        
        Returns:
            None
            
        Example:
            # >>> login_page.screenshot_on_fail()
            # >>> # Saves file like: Test_Login_Fail_15012025103045.png
        """
        self.driver.save_screenshot(f'./screenshots/Test_Login_Fail_{now}.png')

    # ========================= ALLURE REPORTING METHODS =========================
    
    def allure_pass(self):
        """
        Attaches a screenshot to Allure report on test pass.
        
        Captures the current screen and embeds it as PNG attachment in Allure report.
        Used for visual evidence of successful test execution.
        
        Returns:
            None
            
        Example:
            # >>> login_page.allure_pass()
            
        Side Effect:
            Adds attachment to current Allure test report with name 'Test_Login_Pass_{timestamp}.png'
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Login_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        """
        Attaches a screenshot to Allure report on test failure.
        
        Captures the current screen and embeds it as PNG attachment in Allure report.
        Provides visual context for debugging failed login attempts.
        
        Returns:
            None
            
        Example:
            # >>> login_page.allure_fail()
            
        Side Effect:
            Adds attachment to current Allure test report with name 'Test_Login_Fail_{timestamp}.png'
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Login_Fail_{now}',
                      attachment_type=AttachmentType.PNG)
