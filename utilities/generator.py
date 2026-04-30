"""
Test Data Generator Module

This module provides utilities for generating random and realistic test data
for user registration and account creation scenarios in the CredKart framework.

The module uses the 'names' library to generate authentic-sounding names
and crafts realistic email addresses with varied domain names.

Classes:
    Generator: Provides static methods for generating test data

Key Functions:
    - Generate random full names using the names library
    - Create realistic email addresses with randomized local parts and domains
    - Generate valid password strings with required complexity (letters, numbers, symbols)

Usage Example:
    # >>> from utilities.generator import Generator
    # >>> name = Generator.name()  # Returns: 'Alice Johnson'
    # >>> email = Generator.generate_email()  # Returns: 'alice_johnson@gmail.com'
    # >>> password = Generator.password()  # Returns: 'aB3$cDe9!fGh#i'

Benefits:
    - Enables registration tests without data repetition or conflicts
    - Generates unique test data for each test run
    - Supports data-driven testing for user creation scenarios
    - Reduces hardcoded test data maintenance burden

Dependencies:
    - names library: For realistic name generation
"""

from random import shuffle, choice, randint
import names

# Pre-generate first and last names for consistent use within module
first_name = names.get_first_name()
last_name = names.get_last_name()


class Generator:
    """
    Test data generator for user registration and account creation.
    
    Provides static methods to generate various types of test data including
    names, emails, and passwords suitable for e-commerce application testing.
    
    Attributes:
        All methods are static - no instance variables needed
    """

    @staticmethod
    def name():
        """
        Generates a random full name (first + last).
        
        Returns:
            str: Full name in format "FirstName LastName"
            
        Example:
            # >>> name = Generator.name()
            # >>> # Returns: 'John Doe'
            
        Note:
            Uses the names library which provides realistic names
            from multiple cultures and backgrounds.
        """
        full_name = f'{first_name} {last_name}'
        return full_name

    @staticmethod
    def generate_email():
        """
        Generates a realistic email address with randomized components.
        
        Format: {first_name}_{last_name}@{domain}
        
        Returns:
            str: Valid email address format
            
        Example:
            # >>> email = Generator.generate_email()
            # >>> # Returns: 'john_doe@gmail.com' or 'john_doe@credence.in', etc.
            
        Email Domains:
            Randomly selects from a pool of common and custom domains:
            - gmail.com
            - rediffmail.com
            - hotmail.com
            - yahoomail.com
            - credence.in (custom domain)
        """
        # Construct username part from first and last names (lowercase)
        user_name = f'{first_name}_{last_name}'.lower()

        # Randomly select a domain from available options
        domain_name = choice(['gmail.com', 'rediffmail.com', 'hotmail.com', 'yahoomail.com', 'credence.in'])

        # Combine to form complete email address
        return f'{user_name}@{domain_name}'

    @staticmethod
    def password():
        """
        Generates a strong password with mixed character types.
        
        Generates a password containing:
        - 8-10 random letters (uppercase and lowercase)
        - 2-4 random digits
        - 2-4 random special characters
        
        Returns:
            str: Valid password meeting complexity requirements
            
        Example:
            # >>> password = Generator.password()
            # >>> # Returns: 'aB3$cDe9!fGh#i' (varies each call)
            
        Password Complexity:
            - Minimum length: 12 characters (8+2+2)
            - Maximum length: 18 characters (10+4+4)
            - Always contains: uppercase, lowercase, digits, symbols
            
        Supported Special Characters:
            ! # $ % & ( ) * + 
            
        Security Note:
            This is for test automation only. Production passwords should be
            generated using cryptographically secure methods (secrets module).
        """
        # Define character pools for password generation
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # Generate random quantities of each character type
        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        # Combine all password components into a single list
        password_list = password_letters + password_numbers + password_symbols

        # Shuffle to ensure random character distribution
        shuffle(password_list)

        # Join list into string
        password = ''.join(password_list)
        return password
