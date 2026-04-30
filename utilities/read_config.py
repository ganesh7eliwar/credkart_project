"""
Configuration Reader Module

This module provides centralized configuration management for the CredKart automation framework.
It reads test data, application URLs, credentials, and payment information from config.ini,
allowing for easy maintenance and centralized management of test constants.

Classes:
    ReadConfigPD: Reads page-level configuration (URL, page title)
    RCLoginPage: Reads login credentials and user information
    RCAddItem: Reads cart item confirmation messages
    RCWishlist: Reads wishlist confirmation messages
    RCEmptyCartWishlist: Reads empty cart/wishlist confirmation messages
    RCBillingShippingAddress: Reads billing and shipping address details
    RCPayment: Reads payment owner information
    RCCardNumber: Reads card number parts for PCI-compliant entry
    RCOrderPlaced: Reads order confirmation messages

Usage Example:
    # >>> from utilities.read_config import ReadConfigPD, RCLoginPage
    # >>> url = ReadConfigPD.url()
    # >>> email = RCLoginPage.email()

Note:
    - Configuration file must be located at './configurations/config.ini'
    - All credentials and sensitive data should be stored in config.ini, NOT in code
    - For CI/CD environments, consider using environment variables instead
"""

import configparser

# Load configuration from the config.ini file
config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class ReadConfigPD:
    """
    Reads Page Details configuration.
    Responsible for retrieving fundamental page information like URL and title.
    """

    @staticmethod
    def url():
        """
        Retrieves the application base URL from config file.
        
        Returns:
            str: The CredKart application URL
            
        Example:
            # >>> url = ReadConfigPD.url()
            # >>> # Returns: 'https://automation.credence.in/shop'
        """
        page_url = config.get('Page Details', 'url')
        return page_url

    @staticmethod
    def page_title():
        """
        Retrieves the expected page title from config file.
        
        Returns:
            str: The expected page title (e.g., 'CredKart')
            
        Example:
            # >>> title = ReadConfigPD.page_title()
            # >>> # Returns: 'CredKart'
        """
        title = config.get('Page Details', 'title')
        return title


class RCLoginPage:
    """
    Reads Login Page configuration.
    Manages test user credentials used for authentication tests.
    """

    @staticmethod
    def email():
        """
        Retrieves the test user email for login validation.
        
        Returns:
            str: Test user email address
            
        Example:
            # >>> email = RCLoginPage.email()
            # >>> # Returns: 'david_shearing@yahoomail.com'
        """
        email_address = config.get('Login Page', 'email')
        return email_address

    @staticmethod
    def password():
        """
        Retrieves the test user password for login validation.
        
        Returns:
            str: Test user password
            
        Warning:
            In production environments, credentials should not be stored in plain text.
            Consider using environment variables or secure vaults for sensitive data.
        """
        pass_word = config.get('Login Page', 'password')
        return pass_word

    @staticmethod
    def name():
        """
        Retrieves the test user full name.
        
        Returns:
            str: Test user's full name
            
        Example:
            # >>> name = RCLoginPage.name()
            # >>> # Returns: 'David Shearing'
        """
        user_name = config.get('Login Page', 'name')
        return user_name


class RCAddItem:
    """
    Reads Add Item to Cart configuration.
    Manages confirmation messages shown when items are added to cart.
    """

    @staticmethod
    def confirmation_text():
        """
        Retrieves the expected confirmation message when item is added to cart.
        
        Returns:
            str: Confirmation message text to be verified in assertions
            
        Example:
            # >>> msg = RCAddItem.confirmation_text()
            # >>> # Returns: 'Item was added to your cart!'
        """
        cnf_text = config.get('Add Item', 'confirmation_text')
        return cnf_text


class RCWishlist:
    """
    Reads Wishlist configuration.
    Manages confirmation messages shown when items are added to wishlist.
    """

    @staticmethod
    def confirmation_text():
        """
        Retrieves the expected confirmation message when item is added to wishlist.
        
        Returns:
            str: Confirmation message text to be verified in wishlist tests
            
        Example:
            # >>> msg = RCWishlist.confirmation_text()
            # >>> # Returns: 'Item was added to your wishlist!'
        """
        cnf_text = config.get('Wishlist', 'confirmation_text')
        return cnf_text


class RCEmptyCartWishlist:
    """
    Reads Empty Cart and Wishlist configuration.
    Manages confirmation messages for clearing cart and wishlist.
    """

    @staticmethod
    def empty_cart_confirmation():
        """
        Retrieves the confirmation message when cart is emptied.
        
        Returns:
            str: Cart cleared confirmation message
            
        Example:
            # >>> msg = RCEmptyCartWishlist.empty_cart_confirmation()
            # >>> # Returns: 'Your cart has been cleared!'
        """
        confirmation_text = config.get('Empty Cart Wishlist', 'empty_cart')
        return confirmation_text

    @staticmethod
    def empty_wishlist_confirmation():
        """
        Retrieves the confirmation message when wishlist is emptied.
        
        Returns:
            str: Wishlist cleared confirmation message
            
        Example:
            # >>> msg = RCEmptyCartWishlist.empty_wishlist_confirmation()
            # >>> # Returns: 'Your wishlist has been cleared!'
        """
        confirmation_text = config.get('Empty Cart Wishlist', 'empty_wishlist')
        return confirmation_text


class RCBillingShippingAddress:
    """
    Reads Billing and Shipping Address configuration.
    Manages customer address details used during checkout process.
    """

    @staticmethod
    def first_name():
        """
        Retrieves customer first name from billing address.
        
        Returns:
            str: Customer's first name
        """
        f_name = config.get('Billing Shipping address', 'first_name')
        return f_name

    @staticmethod
    def last_name():
        """
        Retrieves customer last name from billing address.
        
        Returns:
            str: Customer's last name
        """
        l_name = config.get('Billing Shipping address', 'last_name')
        return l_name

    @staticmethod
    def phone():
        """
        Retrieves customer phone number for shipping.
        
        Returns:
            str: Customer's phone number
        """
        phone_number = config.get('Billing Shipping address', 'phone')
        return phone_number

    @staticmethod
    def address():
        """
        Retrieves customer street address for shipping.
        
        Returns:
            str: Customer's physical address
        """
        address_of_customer = config.get('Billing Shipping address', 'address')
        return address_of_customer

    @staticmethod
    def zip_code():
        """
        Retrieves customer postal/zip code.
        
        Returns:
            str: Customer's postal code
        """
        zipcode = config.get('Billing Shipping address', 'zip_code')
        return zipcode


class RCPayment:
    """
    Reads Payment configuration.
    Manages payment information like cardholder name and CVV.
    """

    @staticmethod
    def owner():
        """
        Retrieves cardholder name for payment processing.
        
        Returns:
            str: Name on the payment card
        """
        payment_details = config.get('Payment', 'owner')
        return payment_details

    @staticmethod
    def cvv():
        """
        Retrieves CVV (Card Verification Value) for payment validation.
        
        Returns:
            str: Three or four digit CVV code
            
        Warning:
            CVV should never be stored in production code or version control.
            Use environment variables for sensitive payment data.
        """
        cvv_number = config.get('Payment', 'cvv')
        return cvv_number


class RCCardNumber:
    """
    Reads Card Number configuration.
    Manages card number parts stored separately for PCI compliance (not storing full card numbers).
    """

    @staticmethod
    def card_number():
        """
        Constructs card number from stored parts in config.
        Retrieves and combines all four parts of the credit card number.
        
        Returns:
            list: List containing four parts of card number
            
        Example:
            # >>> card_parts = RCCardNumber.card_number()
            # >>> # Returns: ['5281', '0370', '4891', '6168']
            
        Note:
            Card number is split into parts for better security practice.
            In production, use proper payment gateway SDKs and never store card data.
        """
        first_part = config.get('Card Number', 'first_part')
        second_part = config.get('Card Number', 'second_part')
        third_part = config.get('Card Number', 'third_part')
        fourth_part = config.get('Card Number', 'fourth_part')

        card_details = [first_part, second_part, third_part, fourth_part]

        return card_details


class RCOrderPlaced:
    """
    Reads Order Placed configuration.
    Manages order confirmation messages and related information.
    """

    @staticmethod
    def confirmation_msg():
        """
        Retrieves the expected order confirmation message.
        Used to verify successful order placement in end-to-end tests.
        
        Returns:
            str: Order confirmation message displayed after successful purchase
            
        Example:
            # >>> msg = RCOrderPlaced.confirmation_msg()
            # >>> # Returns: 'Your order has been placed successfully.'
        """
        cnf_msg = config.get('Order Placed', 'confirmation_msg')
        return cnf_msg
