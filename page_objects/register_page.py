"""
Register Page Object Module

Encapsulates all interactions with the CredKart user registration page.
Handles new user account creation with name, email, and password validation.

Classes:
    RegisterPage: Page Object for registration form and user management
"""

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from datetime import datetime
import allure

now = datetime.now().strftime('%d%m%Y%H%M%S')


class RegisterPage:
    """
    Register Page Object for CredKart application.
    
    Encapsulates selectors and methods for user registration workflow including
    form filling, validation, and screenshot capture for pass/fail scenarios.
    """

    # ========================= PAGE ELEMENT SELECTORS =========================
    register_button_link_text = "Register"  # Register link in navigation
    name_id = "name"  # Full name input field
    email_address_id = "email"  # Email address input field
    password_id = "password"  # Password input field
    confirm_password_id = "password-confirm"  # Confirm password input field
    register_button_class_name = "btn.btn-primary"  # Submit button for registration
    navbar_id = "navbar"  # Navbar container for screenshot
    user_name_xpath = "//li[@class='dropdown']/a"  # Logged-in user display name

    def __init__(self, driver):
        """Initialize RegisterPage with WebDriver instance."""
        self.driver = driver

    def register_button(self):
        """Clicks the Register link in navigation to open registration form."""
        register_btn = self.driver.find_element(By.LINK_TEXT, self.register_button_link_text)
        register_btn.click()

    def name(self, name):
        """
        Enters user full name into registration form.
        
        Args:
            name (str): Full name (e.g., 'John Doe')
        """
        name_txt_box = self.driver.find_element(By.ID, self.name_id)
        name_txt_box.send_keys(name)

    def email(self, email):
        """
        Enters email address into registration form.
        
        Args:
            email (str): Valid email address (e.g., 'john@example.com')
        """
        email_txt_box = self.driver.find_element(By.ID, self.email_address_id)
        email_txt_box.send_keys(email)

    def password(self, pass_word):
        """
        Enters password into registration form.
        
        Args:
            pass_word (str): Password meeting complexity requirements
        """
        password_txt_box = self.driver.find_element(By.ID, self.password_id)
        password_txt_box.send_keys(pass_word)

    def confirm_password(self, cnf_password):
        """
        Enters confirm password into registration form.
        
        Args:
            cnf_password (str): Password confirmation (must match password field)
        """
        cnf_pass_word = self.driver.find_element(By.ID, self.confirm_password_id)
        cnf_pass_word.send_keys(cnf_password)

    def register_btn(self):
        """Clicks the Registration submit button to create new account."""
        register_button = self.driver.find_element(By.CLASS_NAME, self.register_button_class_name)
        register_button.click()

    def user_name(self):
        """
        Retrieves newly created user's display name from navbar.
        
        Returns:
            str: Registered user's name shown in navbar after successful registration
        """
        user = self.driver.find_element(By.XPATH, self.user_name_xpath).text
        return user

    def screenshot_on_pass(self):
        """Captures navbar screenshot on successful registration."""
        successful_reg_ss = self.driver.find_element(By.ID, self.navbar_id)
        successful_reg_ss.screenshot(f'./screenshots/Test_Register_Pass_{now}.png')

    def screenshot_on_fail(self):
        """Captures full page screenshot on failed registration."""
        self.driver.save_screenshot(f'./screenshots/Test_Register_Fail_{now}.png')

    def allure_pass(self):
        """Attaches screenshot to Allure report on successful registration."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Register_Pass_{now}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        """Attaches screenshot to Allure report on failed registration."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Register_Fail_{now}',
                      attachment_type=AttachmentType.PNG)
