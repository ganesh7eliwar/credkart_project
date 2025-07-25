from selenium.webdriver.common.by import By
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class RegisterPage:
    register_button_link_text = "Register"
    name_id = "name"
    email_address_id = "email"
    password_id = "password"
    confirm_password_id = "password-confirm"
    register_button_class_name = "btn.btn-primary"
    navbar_id = "navbar"
    user_name_xpath = "//li[@class='dropdown']/a"

    def __init__(self, driver):
        self.driver = driver

    def register_button(self):
        register_btn = self.driver.find_element(By.LINK_TEXT, self.register_button_link_text)
        register_btn.click()

    def name(self, name):
        name_txt_box = self.driver.find_element(By.ID, self.name_id)
        name_txt_box.send_keys(name)

    def email(self, email):
        email_txt_box = self.driver.find_element(By.ID, self.email_address_id)
        email_txt_box.send_keys(email)

    def password(self, pass_word):
        password_txt_box = self.driver.find_element(By.ID, self.password_id)
        password_txt_box.send_keys(pass_word)

    def confirm_password(self, cnf_password):
        cnf_pass_word = self.driver.find_element(By.ID, self.confirm_password_id)
        cnf_pass_word.send_keys(cnf_password)

    def register_btn(self):
        register_button = self.driver.find_element(By.CLASS_NAME, self.register_button_class_name)
        register_button.click()

    def user_name(self):
        user = self.driver.find_element(By.XPATH, self.user_name_xpath).text
        return user

    def successful_register_ss(self):
        successful_reg_ss = self.driver.find_element(By.ID, self.navbar_id)
        successful_reg_ss.screenshot(f'./screenshots/Test_Register_Pass_{now}.png')

    def ss_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/Test_Register_Fail_{now}.png')
