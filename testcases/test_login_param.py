from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage


class TestLoginParam:
    user_name = RCLoginPage.name()
    log = Loggen.log_generator()

    def test_login_param(self, setup, data_for_login):

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
