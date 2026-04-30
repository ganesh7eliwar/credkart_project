from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import ReadConfigPD
import allure, json, pytest


class TestLogin:
    """
    Test class for login functionality of the CredKart application.

    This class contains test methods to verify user login with valid credentials.
    It uses the Page Object Model for interacting with the login page and
    includes comprehensive logging and screenshot capture for test results.

    Test Flow:
    1. Load user credentials from JSON file
    2. Navigate to login page
    3. Enter credentials and submit
    4. Verify successful login by checking user name
    5. Logout and assert test result

    Dependencies:
    - Valid user data in test_data/user_details.json (created by test_register)
    - LoginPage page object class
    - Logger utility for detailed test execution logs
    """
    log = Loggen.log_generator()
    title = ReadConfigPD.page_title()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('User Management & Authentication')
    @allure.story('User Login with Valid Credentials')
    @allure.title('User Login - Successful Authentication with Valid Credentials')
    @allure.description('Verifies that registered users can successfully authenticate using valid email and password. '
                        'Tests complete login flow including credential entry, authentication, and user session establishment.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'normal')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('regression', 'user-management', 'authentication', 'critical-path', 'login-flow')
    @allure.link('https://automation.credence.in/shop', 'Login Page')
    @pytest.mark.order(3)
    @pytest.mark.regression
    @pytest.mark.user_management
    @pytest.mark.authentication
    @pytest.mark.login
    @pytest.mark.critical
    def test_login(self, setup, data_dir):
        """
        Test login functionality with valid user credentials.

        This test verifies that a registered user can successfully log in
        using credentials stored in the user_details.json file.

        Steps:
        1. Read user credentials from JSON file
        2. Navigate to login page
        3. Enter email and password
        4. Click login button
        5. Verify login success by checking displayed user name
        6. Logout and capture screenshot

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if login successful and user name matches
            False if login fails or user name doesn't match
        """

        with open(data_dir / "user_details.json", "r") as f:
            user_details = json.load(f)
            self.name = user_details["name"]
            self.email = user_details["email"]
            self.password = user_details["password"]

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.lp = LoginPage(self.driver)

        # Step 1: Navigate to login page
        with allure.step("Navigate to Login Page"):
            self.lp.login()
            self.log.info('Clicked on Login Button Link and navigate to Login Page.')

        # Step 2: Enter email credentials
        with allure.step(f"Enter user email: {self.email}"):
            self.lp.user_email(self.email)
            self.log.info(f'Entered Name in Name Text Box. --> {self.email}')

        # Step 3: Enter password credentials
        with allure.step(f"Enter user password"):
            self.lp.user_password(self.password)
            self.log.info(f'Entered Password in Name Text Box. --> {self.password}')

        # Step 4: Click login button to authenticate
        with allure.step("Click login button to authenticate"):
            self.lp.login_button()
            self.log.info('Clicked on Login Button.')

        # Step 5: Verify login success
        if self.name == self.lp.user_name():
            with allure.step("Verify successful authentication"):
                self.log.info('Entered info If block.')
                self.log.info('User Login Successful.')
                self.log.info('Test Login Passed.')
                self.lp.screenshot_on_pass()
                self.log.info('Captured Screenshot.')
                self.lp.allure_pass()

            # Step 6: Logout
            with allure.step("Logout from application"):
                self.lp.logout_dd_button()
                self.lp.logout_button()
                self.log.info('Clicked on Logout Button')

            assert True
        else:
            with allure.step("Verify login failure"):
                self.log.info('Entered into Else Block.')
                self.log.info('User Login Unsuccessful.')
                self.log.info('Test Login Failed.')
                self.lp.screenshot_on_fail()
                self.log.info('Captured Screenshot.')
                self.lp.allure_fail()

            assert False

        self.log.info('========== Test Session Finished. ==========')
