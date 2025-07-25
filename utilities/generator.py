from random import shuffle, choice, randint
import names

first_name = names.get_first_name()
last_name = names.get_last_name()


class Generator:

    @staticmethod
    def name():
        full_name = f'{first_name} {last_name}'
        return full_name

    @staticmethod
    def generate_email():
        user_name = f'{first_name}_{last_name}'.lower()
        domain_name = choice(['gmail.com', 'rediffmail.com', 'hotmail.com', 'yahoomail.com', 'credence.in'])
        return f'{user_name}@{domain_name}'

    @staticmethod
    def password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols

        shuffle(password_list)

        password = ''.join(password_list)
        return password
