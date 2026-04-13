from page_objects.add_item_to_cart import AddItemInCart
from page_objects.add_item_to_wishlist import AddItemToWishlist
from page_objects.empty_cart_wishlist import EmptyCartOrWishlist
from page_objects.login_page import LoginPage
from utilities.logger import Loggen
from utilities.read_config import RCLoginPage, RCEmptyCartWishlist
import allure, pytest


class TestEmptyWishlist:
    log = Loggen.log_generator()
    email = RCLoginPage.email()
    password = RCLoginPage.password()
    confirmation_text = RCEmptyCartWishlist.empty_wishlist_confirmation()

    @allure.epic('Credkart Project')
    @allure.feature('Empty Wishlist')
    @allure.story('Remove Items from the wishlist.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    # @allure.tag('smoke')
    @allure.link('https://automation.credence.in/shop', 'Cart')
    @allure.title('CredKart')
    @allure.description('This Test Case removes the Items from the Wishlist.')
    @pytest.mark.order(7)
    def test_empty_wishlist(self, setup):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.log.info('Driver Setup Successful.')
        self.log.info(f'Test Run on Driver --> {self.driver}')
        self.lp.login()
        self.log.info('Clicked on Login Button Link and navigate to Login Page.')
        self.lp.user_email(self.email)
        self.log.info(f'Entered Name in Name Text Box. --> {self.email}')
        self.lp.user_password(self.password)
        self.log.info(f'Entered Password in Password Text Box. --> {self.password}')
        self.lp.login_button()
        self.log.info('Clicked on Login Button.')

        self.ai = AddItemInCart(self.driver)
        self.ai.select_item()
        self.log.info('Item Selected.')

        self.aiw = AddItemToWishlist(self.driver)
        self.aiw.add_item_to_wishlist_button()
        self.log.info('Item was Added to Wishlist.')
        self.aiw.wishlist_button()
        self.log.info('Clicked on Wishlist Button.')

        self.ec = EmptyCartOrWishlist(self.driver)
        self.ec.empty_wishlist_button()
        self.log.info('Clicked on Empty Wishlist Button.')

        if self.confirmation_text == self.ec.wishlist_empty_confirmation():
            self.log.info('Entered info If block.')
            self.log.info('Item Removed From Wishlist Successfully.')
            self.ec.empty_wishlist_screenshot_on_pass()
            self.log.info('Captured Screenshot.')
            self.lp.allure_pass()
            self.lp.logout_dd_button()
            self.log.info('Clicked on Logout Dropdown Button.')
            self.lp.logout_button()
            self.log.info('Clicked on Logout Button.')
            self.log.info('Test "Test Empty Wishlist" Passed.')
            assert True

        else:
            self.log.info('Entered into Else Block.')
            self.ec.empty_wishlist_screenshot_on_fail()
            self.log.info('Captured Screenshot.')
            self.lp.allure_fail()
            self.log.info('Test "Test Empty Wishlist" Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
