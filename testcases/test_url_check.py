from page_objects.url_check import URLCheck
from utilities.logger import Loggen
from utilities.read_config import ReadConfigPD


class TestURLCheck:
    title = ReadConfigPD.page_title()
    log = Loggen.log_generator()

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
            self.uc.ss_on_fail()
            self.log.info('Screenshot Captured.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
