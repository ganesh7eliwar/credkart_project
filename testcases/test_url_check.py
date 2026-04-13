from page_objects.url_check import URLCheck
from utilities.logger import Loggen
from utilities.read_config import ReadConfigPD
import allure, pytest


class TestURLCheck:
    title = ReadConfigPD.page_title()
    log = Loggen.log_generator()

    @allure.epic('Credkart Project')
    @allure.feature('Url')
    @allure.story('Verify Url')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.tag('smoke', 'regression')
    @allure.link('https://automation.credence.in/shop', 'URL')
    @allure.title('Credkart')
    @allure.description('This is to check whether the Url is working Properly or not.')
    @pytest.mark.order(1)
    def test_url_check(self, setup):

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
