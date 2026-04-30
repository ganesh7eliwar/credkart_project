"""URL Validation Page Object Module - Validates basic page structure."""

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from datetime import datetime
import allure

now = datetime.now().strftime('%d%m%Y%H%M%S')


class URLCheck:
    """Page Object for URL and basic page structure validation (sanity checks)."""

    page_container_xpath = "//div[@class='jumbotron text-center clearfix']"  # Main page container

    def __init__(self, driver):
        """Initialize with WebDriver instance."""
        self.driver = driver

    def container(self):
        """Captures screenshot of main page container for URL validation."""
        container = self.driver.find_element(By.XPATH, self.page_container_xpath)
        container.screenshot(f'./screenshots/Test_URLCheck_Pass_{now}.png')

    def screenshot_on_fail(self):
        """Captures full page screenshot on URL check failure."""
        self.driver.save_screenshot(f'./screenshots/Test_URLCheck_Fail_{now}.png')

    def allure_fail(self):
        """Attaches fail screenshot to Allure report."""
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_URLCheck_Fail_{now}',
                      attachment_type=AttachmentType.PNG)
