import configparser

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class ReadConfigPD:
    @staticmethod
    def url():
        page_url = config.get('Page Details', 'url')
        return page_url

    @staticmethod
    def page_title():
        title = config.get('Page Details', 'title')
        return title


class RCLoginPage:
    @staticmethod
    def email():
        email_address = config.get('Login Page', 'email')
        return email_address

    @staticmethod
    def password():
        pass_word = config.get('Login Page', 'password')
        return pass_word

    @staticmethod
    def name():
        user_name = config.get('Login Page', 'name')
        return user_name


class RCAddItem:
    @staticmethod
    def confirmation_text():
        cnf_text = config.get('Add Item', 'confirmation_text')
        return cnf_text


class RCWishlist:
    @staticmethod
    def confirmation_text():
        cnf_text = config.get('Wishlist', 'confirmation_text')
        return cnf_text


class RCEmptyCartWishlist:
    @staticmethod
    def empty_cart_confirmation():
        confirmation_text = config.get('Empty Cart Wishlist', 'empty_cart')
        return confirmation_text

    @staticmethod
    def empty_wishlist_confirmation():
        confirmation_text = config.get('Empty Cart Wishlist', 'empty_wishlist')
        return confirmation_text


class RCBillingShippingAddress:
    @staticmethod
    def first_name():
        f_name = config.get('Billing Shipping address', 'first_name')
        return f_name

    @staticmethod
    def last_name():
        l_name = config.get('Billing Shipping address', 'last_name')
        return l_name

    @staticmethod
    def phone():
        phone_number = config.get('Billing Shipping address', 'phone')
        return phone_number

    @staticmethod
    def address():
        address_of_customer = config.get('Billing Shipping address', 'address')
        return address_of_customer

    @staticmethod
    def zip_code():
        zipcode = config.get('Billing Shipping address', 'zip_code')
        return zipcode


class RCPayment:
    @staticmethod
    def owner():
        payment_details = config.get('Payment', 'owner')
        return payment_details

    @staticmethod
    def cvv():
        cvv_number = config.get('Payment', 'cvv')
        return cvv_number


class RCCardNumber:
    @staticmethod
    def card_number():
        first_part = config.get('Card Number', 'first_part')
        second_part = config.get('Card Number', 'second_part')
        third_part = config.get('Card Number', 'third_part')
        fourth_part = config.get('Card Number', 'fourth_part')

        card_details = [first_part, second_part, third_part, fourth_part]

        return card_details


class RCOrderPlaced:
    @staticmethod
    def confirmation_msg():
        cnf_msg = config.get('Order Placed', 'confirmation_msg')
        return cnf_msg
