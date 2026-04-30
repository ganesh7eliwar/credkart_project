from page_objects.login_page import LoginPage
from utilities import excelutils
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage
import allure, pytest


class TestLoginDDT:
    """
    Test class for data-driven login testing of the CredKart application.

    This class implements Data-Driven Testing (DDT) approach for login functionality,
    reading test data from Excel files to test multiple login scenarios including
    valid and invalid credential combinations.

    Test Flow:
    1. Read test data from Excel file (Credkart_Login_Data.xlsx)
    2. Iterate through each row of test data
    3. Attempt login with each set of credentials
    4. Verify expected vs actual results
    5. Track pass/fail status for each iteration
    6. Assert overall test result based on status list

    Dependencies:
    - Excel file: test_data/Credkart_Login_Data.xlsx with login_data sheet
    - LoginPage page object class
    - excelutils utility for Excel file operations
    - Logger utility for detailed test execution logs
    """
    file = './test_data/Credkart_Login_Data.xlsx'
    sheet = 'login_data'
    log = Loggen.log_generator()
    user_name = RCLoginPage.name()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('User Management & Authentication')
    @allure.story('Data-Driven Login Testing with Multiple Credentials from Excel')
    @allure.title('Login Data-Driven Tests - Excel-Based Credential Validation')
    @allure.description('Data-driven test validating login functionality with multiple credential combinations '
                        'loaded from Excel file. Tests both valid and invalid credential scenarios to verify '
                        'proper authentication and error handling.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'normal')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('regression', 'user-management', 'authentication', 'login-flow', 'data-driven',
                'ddt', 'excel-based', 'credential-validation')
    @allure.link('https://automation.credence.in/shop', 'Login Page')
    @pytest.mark.order(9)
    @pytest.mark.regression
    @pytest.mark.user_management
    @pytest.mark.authentication
    @pytest.mark.login
    @pytest.mark.ddt
    @pytest.mark.data_driven
    @pytest.mark.parametrize_excel
    def test_login_ddt(self, setup):
        """
        Test login functionality using data-driven approach with Excel data.

        This test reads login credentials and expected results from an Excel file
        and performs multiple login attempts to validate both successful and failed
        login scenarios.

        Excel Data Format (login_data sheet):
        | Email | Password | Expected Result |
        |-------|----------|-----------------|
        | valid@email.com | valid-pass | Pass |
        | valid@email.com | invalidpass | Fail |
        | invalid@email.com | valid-pass | Fail |

        Steps:
        1. Read total rows from Excel sheet
        2. Loop through each data row (starting from row 2)
        3. Extract email, password, and expected result
        4. Attempt login and verify against expected result
        5. Track results in status list
        6. Assert test passes only if no failures occurred

        Args:
            setup: Pytest fixture providing WebDriver instance

        Asserts:
            True if all login attempts match expected results
            False if any login attempt doesn't match expected result

        Notes:
            - Does not perform logout between iterations for efficiency
            - Uses status list to track individual test case results
            - Comprehensive logging for each iteration
        """

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.rows = excelutils.total_rows(self.file, self.sheet)
        self.log.info(f'Number of Rows in Table: {self.rows} including Header.')
        self.status_list = []
        self.lp = LoginPage(self.driver)
        self.iteration = 0

        # Iterate through each data row in Excel (starting from row 2, skipping header)
        for row in range(2, self.rows + 1):

            self.iteration += 1
            self.log.info(f'Entered into for loop, Interation No.: {self.iteration}.')

            # Read test data from Excel: email (column 1), password (column 2), expected result (column 3)
            self.email = excelutils.read_data(self.file, self.sheet, row, 1)
            self.password = excelutils.read_data(self.file, self.sheet, row, 2)
            self.expected_result = excelutils.read_data(self.file, self.sheet, row, 3)

            self.lp.login()
            self.log.info('Clicked on Login Button.')
            self.lp.user_email(self.email)
            self.log.info(f'Entered Email Address: {self.email}.')
            self.lp.user_password(self.password)
            self.log.info(f'Entered Password: {self.password}.')
            self.lp.login_button()
            self.log.info(f'Clicked on Login Button.')

            if self.expected_result == 'Pass':
                self.log.info('Entered into If Block.')
                if self.lp.user_name() == self.user_name:
                    self.log.info('Entered into Nested If Block within If Block.')
                    self.status_list.append('Pass')
                    self.log.info('Appended data to Status List.')
                    self.lp.logout_dd_button()
                    self.log.info('Clicked on Logout DropDown Button.')
                    self.lp.logout_button()
                    self.log.info('Clicked on Logout Button.')

                else:
                    self.log.info('Entered into Else Block.')
                    self.status_list.append('Fail')
                    self.log.info('Appended data to Status List.')

            elif self.expected_result == 'Fail':
                self.log.info('Entered into Elif Block.')
                if self.lp.user_name() == self.user_name:
                    self.log.info('Entered into If Block within Elif Block.')
                    self.status_list.append('Fail')
                    self.log.info('Appended data to Status List.')
                    self.lp.logout_dd_button()
                    self.log.info('Clicked on Logout DropDown Button.')
                    self.lp.logout_button()
                    self.log.info('Clicked on Logout Button.')

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
