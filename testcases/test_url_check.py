from page_objects.url_check import URLCheck
from utilities.logger import Loggen
from utilities.read_config import ReadConfigPD
import allure, pytest


class TestURLCheck:
    """
    Test class for basic URL and page accessibility of the CredKart application.

    This class contains sanity check tests to verify that the application
    is accessible and loads correctly. It serves as a foundational test
    that should run before other functional tests.

    Test Flow:
    1. Navigate to the application URL
    2. Verify page title matches expected value
    3. Capture screenshot for visual verification

    Dependencies:
    - URLCheck page object class for screenshot utilities
    - Configuration utility for expected page title
    - Logger utility for detailed test execution logs
    """
    title = ReadConfigPD.page_title()
    log = Loggen.log_generator()

    @allure.epic('CredKart Project - E-Commerce Automation')
    @allure.feature('Application Accessibility')
    @allure.story('Verify Application URL and Page Load')
    @allure.title('URL Check - Application Accessibility Sanity Check')
    @allure.description('Validates that the CredKart application is accessible and loads correctly. '
                        'This sanity check verifies page title and basic page structure. '
                        'Should run first in test suite to confirm environment readiness.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.label('severity', 'critical')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'sanity', 'accessibility', 'critical-path', 'prerequisite')
    @allure.link('https://automation.credence.in/shop', 'Application URL')
    @pytest.mark.order(1)
    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.accessibility
    @pytest.mark.critical
    @pytest.mark.prerequisite
    def test_url_check(self, setup):
        """
        Test basic URL accessibility and page title verification.

        This sanity test ensures the CredKart application is reachable and
        loads correctly by checking the page title against expected value.

        Steps:
        1. Navigate to application URL (handled by setup fixture)
        2. Verify page title matches configured expected title
        3. Capture screenshot for manual verification if needed

        Args:
            setup: Pytest fixture providing WebDriver instance (includes URL navigation)

        Asserts:
            True if page title matches expected title
            False if title doesn't match or page fails to load

        Notes:
            - This is typically the first test to run in a test suite
            - Critical severity as it validates basic application accessibility
            - Should be included in smoke test suites
        """

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.uc = URLCheck(self.driver)

        if self.driver.title == self.title:
            self.log.info('Entered into If Block.')
            self.log.info(f'Title of the Page is: {self.driver.title}')
            self.log.info('Test URL Check Passed')
            self.uc.container()
            self.log.info('Screenshot Captured.')
            assert True
        else:
            self.log.info('Entered into Else Block.')
            self.log.info('Test URL Check Failed.')
            self.uc.screenshot_on_fail()
            self.log.info('Screenshot Captured.')
            self.uc.allure_fail()
            assert False

        self.log.info('========== Test Session Finished. ==========')
