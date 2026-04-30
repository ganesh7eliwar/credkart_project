from page_objects.register_page import RegisterPage
from testcases.conftest import data_dir
from utilities.generator import Generator
from utilities.logger import Loggen
import allure, json, pytest


class TestRegister:
    """
    Test class for user registration functionality of the CredKart application.

    This class contains test methods to verify new user registration process.
    It generates random user data, performs registration, and saves the
    credentials for use in subsequent tests.

    Test Flow:
    1. Generate random user details (name, email, password)
    2. Navigate to registration page
    3. Fill registration form and submit
    4. Verify successful registration
    5. Save user details to JSON files for later use

    Dependencies:
    - RegisterPage page object class
    - Generator utility for random data creation
    - Logger utility for detailed test execution logs
    """
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
    def test_register(self, setup, data_dir):
        """
        Test user registration with randomly generated credentials.

        This test verifies the complete user registration process by:
        1. Generating unique user data (name, email, password)
        2. Filling out the registration form
        3. Submitting the registration
        4. Verifying successful registration by checking user name display
        5. Saving user details to JSON files for use in other tests

        Args:
            setup: Pytest fixture providing WebDriver instance
            data_dir: Pytest fixture providing path to test_data directory

        Asserts:
            True if registration successful and user name matches generated name
            False if registration fails

        Side Effects:
            Creates/updates test_data/user_details.json with new user credentials
            Appends to test_data/all_user_details.json for historical records
        """

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

        self.log.info('Saving User Details to JSON File.')
        user_details = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

        with open(data_dir / "user_details.json", 'w') as f:
            json.dump(user_details, f, indent=4)

        self.log.info('User Details saved to all_user_details.json file.')
        file_path = data_dir / "all_user_details.json"
        try:
            with open(file_path, "r") as f:
                all_user_details = json.load(f)
                if not isinstance(all_user_details, list):
                    all_user_details = [all_user_details]
        except (FileNotFoundError, json.JSONDecodeError):
            all_user_details = []

        self.log.info('Appending new user details to all_user_details list.')
        all_user_details.append(user_details)

        with open(file_path, "w") as f:
            json.dump(all_user_details, f, indent=4)

        self.log.info('========== Test Session Finished. ==========')
