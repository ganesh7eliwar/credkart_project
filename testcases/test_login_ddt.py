from page_objects.login_page import LoginPage
from utilities import excelutils
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage


class TestLoginDDT:
    file = './test_data/Credkart_Login_Data.xlsx'
    sheet = 'login_data'
    log = Loggen.log_generator()
    user_name = RCLoginPage.name()

    def test_login_ddt(self, setup):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.rows = excelutils.total_rows(self.file, self.sheet)
        self.log.info(f'Number of Rows in Table: {self.rows} including Header.')
        self.status_list = []
        self.lp = LoginPage(self.driver)
        self.iteration = 0

        for row in range(2, self.rows + 1):

            self.iteration += 1
            self.log.info(f'Entered into for loop, Interation No.: {self.iteration}.')
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
