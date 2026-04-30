from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage
import allure, pytest


class TestLoginParam:
    """
    Test class for parameterized login testing of the CredKart application.

    This class implements parameterized testing for login functionality using
    pytest fixtures with parameters. It tests multiple login scenarios including
    valid and invalid credential combinations through fixture parameterization.

    Test Flow:
    1. Use parameterized fixture from conftest.py (data_for_login)
    2. Receive email, password, and expected result as parameters
    3. Attempt login with provided credentials
    4. Verify expected vs actual results
    5. Assert test result based on parameter expectations

    Dependencies:
    - Parameterized fixture 'data_for_login' in conftest.py
    - LoginPage page object class
    - Logger utility for detailed test execution logs
    """
    user_name = RCLoginPage.name()
    log = Loggen.log_generator()

    @allure.epic('Credkart Project')
    @allure.feature('Parameterized Test')
    @allure.story('Verify Login with Data')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    # @allure.tag('smoke', 'login')
    @allure.link('https://automation.credence.in/shop', 'Login')
    @allure.title('Credkart')
    @allure.description('This is a Parameterized test which gives different Inputs while Login.')
    @pytest.mark.order(10)
    def test_login_param(self, setup, data_for_login):
        """
        Test login functionality using parameterized pytest fixtures.

        This test uses the 'data_for_login' fixture from conftest.py to receive
        parameterized login data and validates both successful and failed login
        scenarios based on expected results.

        Parameter Structure (from data_for_login fixture):
        - data_for_login[0]: Email address (string)
        - data_for_login[1]: Password (string)
        - data_for_login[2]: Expected result ('Pass' or 'Fail')

        Test Cases Covered:
        1. Valid email + valid password → Expected Pass
        2. Valid email + invalid password → Expected Fail
        3. Invalid email + valid password → Expected Fail
        4. Invalid email + invalid password → Expected Fail

        Steps:
        1. Extract email, password, expected result from parameters
        2. Attempt login with provided credentials
        3. Verify login result against expected outcome
        4. Track result in status list
        5. Assert based on whether test should pass or fail

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_for_login: Parameterized fixture with (email, password, expected)

        Asserts:
            True if login result matches expected parameter
            False if login result doesn't match expected parameter

        Notes:
            - Each parameter set runs as a separate test case
            - Pytest automatically generates test names with parameter values
            - Logout performed only for successful login attempts
        """

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.lp = LoginPage(self.driver)
        self.status_list = []

        self.lp.login()
        self.log.info('Clicked on login button.')
        self.lp.user_email(data_for_login[0])
        self.log.info(f'Inserted data into Email textbox. --> {data_for_login[0]}')
        self.lp.user_password(data_for_login[1])
        self.log.info(f'Inserted data into first name textbox. --> {data_for_login[1]}')
        self.lp.login_button()
        self.log.info('Clicked on login button.')

        if data_for_login[2] == 'Pass':
            self.log.info('Entered into if Block')
            if self.lp.user_name() == self.user_name:
                self.log.info('Entered into Nested if Block')
                self.status_list.append('Pass')
                self.log.info('Appended data to Status List.')
                self.lp.logout_dd_button()
                self.log.info('Clicked on log out dropdown button.')
                self.lp.logout_button()
                self.log.info('Clicked on log out button')
            else:
                self.log.info('Entered into Else Block.')
                self.status_list.append('Fail')
                self.log.info('Appended data to Status List.')

        elif data_for_login[2] == 'Fail':
            self.log.info('Entered into Elif Block.')
            if self.lp.user_name() == self.user_name:
                self.log.info('Entered into If Block within Elif Block.')
                self.status_list.append('Fail')
                self.log.info('Appended data to Status List.')
                self.lp.logout_dd_button()
                self.log.info('Clicked on log out dropdown button.')
                self.lp.logout_button()
                self.log.info('Clicked on log out button')
            else:
                self.log.info('Entered into Else Block.')
                self.status_list.append('Pass')
                self.log.info('Appended Data to Status List.')

        if 'Fail' not in self.status_list:
            self.log.info('Entered into If Block for Assertion.')
            self.log.info('If Fail not in Status List Testcase Passed.')
            self.log.info(f'Status List: {self.status_list}')
            self.log.info('Test "Test_Login_DDT" Passed.')
            assert True
        else:
            self.log.info('Entered into Else Block For Assertion.')
            self.log.info('If Fail in Status list Testcase Failed')
            self.log.info(f'Status List: {self.status_list}')
            self.log.info('Test "Test_Login_DDT" Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
