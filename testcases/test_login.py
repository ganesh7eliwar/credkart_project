from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage, ReadConfigPD


class TestLogin:
    log = Loggen.log_generator()
    email = RCLoginPage.email()
    password = RCLoginPage.password()
    name = RCLoginPage.name()
    title = ReadConfigPD.page_title()

    def test_login(self, setup):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.lp = LoginPage(self.driver)
        self.lp.login()
        self.log.info('Clicked on Login Button Link and navigate to Login Page.')
        self.lp.user_email(self.email)
        self.log.info(f'Entered Name in Name Text Box. --> {self.email}')
        self.lp.user_password(self.password)
        self.log.info(f'Entered Password in Name Text Box. --> {self.password}')
        self.lp.login_button()
        self.log.info('Clicked on Login Button.')

        if self.driver.title == self.title:
            self.log.info('Entered info If block.')
            self.log.info('User Login Successful.')
            self.log.info('Test Login Passed.')
            self.lp.ss_on_pass()
            self.log.info('Captured Screenshot.')
            self.lp.logout_dd_button()
            self.lp.logout_button()
            self.log.info('Clicked on Logout Button')
            assert True
        else:
            self.log.info('Entered into Else Block.')
            self.log.info('User Login Unsuccessful.')
            self.log.info('Test Login Failed.')
            self.lp.ss_on_fail()
            self.log.info('Captured Screenshot.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
