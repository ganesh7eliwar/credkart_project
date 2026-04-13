from page_objects.register_page import RegisterPage
from utilities.generator import Generator
from utilities.logger import Loggen
import allure, pytest


class TestRegister:
    log = Loggen.log_generator()
    name = Generator.name()
    email = Generator.generate_email()
    password = Generator.password()

    @allure.epic('Credkart Project')
    @allure.feature('Registration')
    @allure.story('Registering a user for the first time.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.tag('sanity', 'regression')
    @allure.link('https://automation.credence.in/shop', 'Registration')
    @allure.title('Credkart')
    @allure.description('This is a registration test.')
    @pytest.mark.order(2)
    def test_register(self, setup):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.rp = RegisterPage(self.driver)
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.rp.register_button()
        self.log.info('Clicked on Register Button Link and navigate to Register Page.')
        self.rp.name(self.name)
        self.log.info(f'Entered Name in Name Text Box. --> {self.name}')
        self.rp.email(self.email)
        self.log.info(f'Entered Email in Email Text Box. --> {self.email}')
        self.rp.password(self.password)
        self.log.info(f'Entered Password in Password Text Box. --> {self.password}')
        self.rp.confirm_password(self.password)
        self.log.info(f'Entered Password in Confirm Password Text Box. {self.password}')
        self.rp.register_btn()
        self.log.info('Clicked on Register Button.')

        if self.rp.user_name() == self.name:
            self.log.info('Entered info If block.')
            self.log.info(f'{self.rp.user_name()} == {self.name}')
            self.log.info('User Registration Successful.')
            self.log.info('Test Register Passed.')
            self.rp.screenshot_on_pass()
            self.log.info('Captured Screenshot.')
            self.rp.allure_pass()
            assert True
        else:
            self.log.info('Entered into Else Block.')
            self.log.info('User Registration Unsuccessful.')
            self.log.info('Test Register Failed.')
            self.rp.screenshot_on_fail()
            self.log.info('Captured Screenshot.')
            self.rp.allure_fail()
            assert False

        self.log.info('========== Test Session Finished. ==========')
