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
