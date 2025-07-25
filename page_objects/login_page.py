from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class LoginPage:
    login_xpath = "//a[normalize-space()='Login']"
    email_address_id = "email"
    password_id = "password"
    login_button_xpath = "//button[@type='submit']"
    logout_dd_css_selector = "a[role='button']"
    logout_btn_xpath = "//a[normalize-space()='Logout']"
    user_name_xpath = "//div[@id='navbar']/ul/li/a[@class='dropdown-toggle']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def login(self):

        try:
            login_button = self.driver.find_element(By.XPATH, self.login_xpath)
            login_button.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def user_email(self, email):
        email_text_box = self.driver.find_element(By.ID, self.email_address_id)
        email_text_box.send_keys(email)

    def user_password(self, password):
        password_text_box = self.driver.find_element(By.ID, self.password_id)
        password_text_box.send_keys(password)

    def login_button(self):
        login_btn = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_btn.click()

    def logout_dd_button(self):

        try:
            logout_dd = self.driver.find_element(By.CSS_SELECTOR, self.logout_dd_css_selector)
            logout_dd.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def logout_button(self):

        try:
            logout_btn = self.driver.find_element(By.XPATH, self.logout_btn_xpath)
            logout_btn.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def user_name(self):

        try:
            user_name = self.driver.find_element(By.XPATH, self.user_name_xpath).text
            return user_name
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            return "Encountered an Error."

    def ss_on_pass(self):
        self.driver.save_screenshot(f'./screenshots/Test_Login_Pass_{now}.png')

    def ss_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_Login_Fail_{now}.png')
