from selenium.webdriver.common.by import By
from datetime import datetime

now = datetime.now().strftime('%d%m%Y%H%M%S')


class URLCheck:
    page_container_xpath = "//div[@class='jumbotron text-center clearfix']"

    def __init__(self, driver):
        self.driver = driver

    def container(self):
        container = self.driver.find_element(By.XPATH, self.page_container_xpath)
        container.screenshot(f'./screenshots/Test_URLCheck_Pass_{now}.png')

    def ss_on_fail(self):
        self.driver.save_screenshot(f'./screenshots/URLCheck_Fail_{now}.png')
