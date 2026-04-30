# CredKart Automation Framework - Style Guide

This document outlines the coding standards, conventions, and best practices for the CredKart Automation Framework. All contributors must adhere to these guidelines to maintain code quality and consistency.

---

## Table of Contents

- [Python Code Style](#python-code-style)
- [Naming Conventions](#naming-conventions)
- [Page Object Model Guidelines](#page-object-model-guidelines)
- [Test Development Standards](#test-development-standards)
- [Documentation Standards](#documentation-standards)
- [File Organization](#file-organization)
- [Error Handling](#error-handling)
- [Logging Conventions](#logging-conventions)
- [Configuration Management](#configuration-management)

---

## Python Code Style

### PEP 8 Compliance

All code must comply with [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these specific guidelines:

- **Line Length**: Maximum 100 characters (not strict 79)
- **Indentation**: 4 spaces (never tabs)
- **Blank Lines**: 2 before class definitions, 1 before methods
- **Imports**: Grouped and sorted (built-in, third-party, local)

### Code Example

```python
"""
Module docstring describing purpose and usage.
"""

# Standard library
import json
from datetime import datetime
from pathlib import Path

# Third-party
import pytest
from selenium.webdriver.common.by import By

# Local imports
from utilities.logger import Loggen
from utilities.read_config import ReadConfigPD


class LoginPage:
    """
    Page Object for login functionality.
    
    Handles user authentication and related operations.
    """
    
    # Element selectors
    login_button_xpath = "//a[normalize-space()='Login']"
    email_input_id = "email"
    
    def __init__(self, driver):
        """Initialize with WebDriver instance."""
        self.driver = driver
    
    def login(self, email, password):
        """Complete login workflow."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
```

---

## Naming Conventions

### Classes

**Format**: `PascalCase`  
**Purpose**: Page Objects, Test Classes, Utilities

```python
class LoginPage:
    pass

class AddItemToCart:
    pass

class TestLogin:
    pass

class Generator:
    pass
```

### Functions and Methods

**Format**: `snake_case`  
**Purpose**: Methods, functions, test functions

```python
def test_user_login():
    pass

def Enter_email(email):  # ❌ Wrong
    pass

def enter_email(email):  # ✅ Correct
    pass

def calculate_total():
    pass
```

### Constants

**Format**: `UPPER_SNAKE_CASE`  
**Purpose**: Fixed values, configuration constants

```python
# Good
DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3
BASE_URL = "https://automation.credence.in/shop"
PRICE_THRESHOLD = 100.00

# Bad
defaultTimeout = 10
max_retries = 3
```

### Variables

**Format**: `snake_case`  
**Purpose**: Local and instance variables

```python
# Good
email_address = "test@example.com"
confirmation_text = "Order placed successfully"
is_logged_in = True
item_count = 5

# Bad
emailAddress = "test@example.com"  # Camel case
Email_Address = "test@example.com"  # Mixed case
```

### Private Methods

**Format**: `_snake_case` (leading underscore)  
**Purpose**: Methods not intended for external use

```python
class PageObject:
    def public_method(self):
        """Called externally."""
        result = self._helper_method()
        return result
    
    def _helper_method(self):
        """Internal helper, not part of public API."""
        pass
```

### Selectors and Locators

**Format**: Descriptive with locator type suffix  
**Purpose**: Element locators in Page Objects

```python
class CheckoutPage:
    # XPath selectors
    checkout_button_xpath = "//button[@id='checkout']"
    shipping_address_xpath = "//input[@name='address']"
    
    # ID selectors
    email_input_id = "email"
    phone_input_id = "phone"
    
    # CSS selectors
    confirm_button_css = ".btn-primary"
    error_message_css = ".alert-danger"
    
    # Class name selectors
    price_class = "price-amount"
```

---

## Page Object Model Guidelines

### Structure

```python
"""
Module docstring explaining page and its purpose.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure


class PageName:
    """
    Page Object for PageName.
    
    Encapsulates elements and interactions for this page.
    """
    
    # ==================== ELEMENT SELECTORS ====================
    # Group selectors by type and location
    
    # Header/Navigation
    login_link_xpath = "//a[@href='/login']"
    logout_link_xpath = "//a[@href='/logout']"
    
    # Forms
    email_input_id = "email"
    password_input_id = "password"
    
    # Buttons
    submit_button_xpath = "//button[@type='submit']"
    cancel_button_xpath = "//button[@type='cancel']"
    
    # Messages/Alerts
    success_message_css = ".alert-success"
    error_message_css = ".alert-danger"
    
    # ==================== INITIALIZATION ====================
    
    def __init__(self, driver):
        """
        Initialize PageObject with WebDriver.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # ==================== USER ACTIONS ====================
    # Public methods representing user interactions
    
    def perform_action(self):
        """Descriptive action name."""
        self._click_element(self.button_xpath)
    
    # ==================== HELPER METHODS ====================
    # Private helper methods
    
    def _click_element(self, selector_xpath):
        """Click element using XPath."""
        element = self.driver.find_element(By.XPATH, selector_xpath)
        element.click()
    
    def _enter_text(self, selector_id, text):
        """Enter text into element."""
        element = self.driver.find_element(By.ID, selector_id)
        element.send_keys(text)
```

### Do's

✅ **Encapsulate** element selectors as class variables  
✅ **Provide** methods for user interactions  
✅ **Handle** exceptions gracefully  
✅ **Use** descriptive method names  
✅ **Document** complex logic with comments  
✅ **Group** related selectors together  

### Don'ts

❌ **Don't** expose Selenium WebDriver directly in tests  
❌ **Don't** hardcode selectors in test methods  
❌ **Don't** mix assertions with Page Object logic  
❌ **Don't** create complex Page Objects for simple pages  
❌ **Don't** duplicate selectors across files  

---

## Test Development Standards

### Test Structure (AAA Pattern)

```python
@pytest.mark.smoke
@allure.feature("Login")
def test_user_login_valid(setup, data_dir):
    """
    Test user login with valid credentials.
    
    Objective: Verify user can login with valid email/password
    """
    # ==================== ARRANGE ====================
    # Setup: Data, mocks, preconditions
    driver = setup
    email = "test@example.com"
    password = "SecurePassword123!"
    
    # ==================== ACT ====================
    # Execute: Main workflow being tested
    with allure.step("Navigate to login"):
        login_page = LoginPage(driver)
    
    with allure.step("Enter credentials"):
        login_page.login(email, password)
    
    # ==================== ASSERT ====================
    # Verify: Check expected outcomes
    with allure.step("Verify login success"):
        assert "Dashboard" in driver.title
        assert login_page.user_name() == "John Doe"
```

### Test Naming

**Format**: `test_<feature>_<scenario>_<expected_result>`

```python
# Good names
def test_login_valid_credentials_redirects_to_dashboard():
    pass

def test_checkout_empty_cart_shows_error_message():
    pass

def test_wishlist_add_item_updates_count():
    pass

# Bad names
def test_1():
    pass

def test_login():  # Too vague
    pass

def test_it_works():  # Not descriptive
    pass
```

### Test Data Management

```python
# ✅ Good: Use config for all test data
from utilities.read_config import ReadConfigPD, RCLoginPage

email = RCLoginPage.email()
password = RCLoginPage.password()

# ✅ Good: Use fixtures for dynamic data
@pytest.fixture
def test_user(data_dir):
    with open(data_dir / "user_details.json") as f:
        return json.load(f)

# ❌ Bad: Hardcode in test
email = "test@example.com"
password = "password123"

# ❌ Bad: Mix with logic
email = RCLoginPage.email() + "_extra"
```

### Parameterized Tests

```python
# Data-driven test with multiple scenarios
@pytest.mark.parametrize("email,password,expected_result", [
    ("valid@example.com", "ValidPass123!", "success"),
    ("valid@example.com", "WrongPassword", "error"),
    ("invalid@example.com", "ValidPass123!", "error"),
    ("", "ValidPass123!", "error"),
])
def test_login_scenarios(setup, email, password, expected_result):
    """Test login with various credential combinations."""
    login_page = LoginPage(setup)
    result = login_page.login(email, password)
    assert result == expected_result
```

---

## Documentation Standards

### Module Docstring

```python
"""
Module name - Brief description.

Longer description of the module's purpose, usage, and key components.

Usage Example:
    >>> from module import ClassName
    >>> obj = ClassName()
    >>> result = obj.method()

Classes:
    ClassName: Description of the class
    OtherClass: Description of another class

Functions:
    function_name: Description of function
"""
```

### Class Docstring

```python
class LoginPage:
    """
    Page Object for login functionality.
    
    Encapsulates all selectors and interactions for the login page.
    Provides methods for entering credentials and submitting the form.
    
    Attributes:
        driver: Selenium WebDriver instance
        wait: WebDriverWait for explicit waits
    
    Example:
        >>> login_page = LoginPage(driver)
        >>> login_page.login("test@example.com", "password")
    """
```

### Method/Function Docstring

```python
def login(self, email, password):
    """
    Perform user login with email and password.
    
    Complete login workflow including entering credentials and
    clicking the login button. Handles delays and retries automatically.
    
    Args:
        email (str): User email address
        password (str): User password
        
    Returns:
        bool: True if login successful, False otherwise
        
    Raises:
        TimeoutException: If login button not found within timeout
        NoSuchElementException: If required elements not present
        
    Example:
        >>> success = login_page.login("user@example.com", "pass123")
        >>> assert success is True
    """
    self.enter_email(email)
    self.enter_password(password)
    return self.click_login()
```

---

## File Organization

### Configuration Files

**Location**: `configurations/config.ini`

```ini
# ============================================================================
# [Section Name] - Brief Description
# ============================================================================
# Comments explaining the section

[Section Name]
# Configuration key description
key = value

# Another description
another_key = another_value
```

### Test Files

**Location**: `testcases/test_<feature>.py`

```python
"""
Test module for <feature> functionality.

Tests cover:
- Scenario 1
- Scenario 2
- Scenario 3
"""

import pytest
import allure
from page_objects import ...
from utilities import ...


class Test<Feature>:
    """Test suite for <feature>."""
    
    @pytest.mark.smoke
    def test_scenario_1(self, setup):
        pass
    
    @pytest.mark.regression
    def test_scenario_2(self, setup):
        pass
```

### Page Object Files

**Location**: `page_objects/<page_name>.py`

```python
"""
<Page Name> Page Object Module

Encapsulates all selectors and interactions for <page name> page.
"""

from selenium.webdriver.common.by import By
import allure


class <PageName>:
    """Page Object for <Page Name>."""
    
    # Selectors...
    # Methods...
```

### Utility Files

**Location**: `utilities/<utility_name>.py`

```python
"""
<Utility Name> Module

Provides <utility functionality> for the framework.

Usage:
    >>> from utilities.utility_name import function_name
    >>> result = function_name(parameter)
"""

# Implementation...
```

---

## Error Handling

### Exception Handling

```python
# ✅ Good: Specific exception handling
from selenium.common import TimeoutException, NoSuchElementException

try:
    element = self.wait.until(EC.presence_of_element_located((By.ID, "id")))
    element.click()
except TimeoutException:
    self.log.error("Element not found within timeout")
    self.allure_fail()
    raise
except NoSuchElementException:
    self.log.error("Element not present in DOM")
    self.allure_fail()
    raise

# ❌ Bad: Generic exception handling
try:
    element.click()
except:
    pass

# ❌ Bad: Swallowing exceptions
try:
    element = self.driver.find_element(By.ID, "button")
except:
    element = None  # Do not do this
```

### Logging Errors

```python
from utilities.logger import Loggen

log = Loggen.log_generator()

try:
    perform_action()
except Exception as e:
    log.error(f"Action failed: {str(e)}", exc_info=True)
    raise
```

---

## Logging Conventions

### Logging Levels

```python
from utilities.logger import Loggen

log = Loggen.log_generator()

# DEBUG: Very detailed, diagnostic
log.debug(f"Attempting to find element: {selector}")

# INFO: General informational messages
log.info("User logged in successfully")

# WARNING: Something unexpected but recoverable
log.warning("Element not found, retrying...")

# ERROR: Failed operation
log.error(f"Login failed: {exception}")

# CRITICAL: System will fail
log.critical("Database connection lost")
```

### Logging Format

```python
# ✅ Good: Include context and data
log.info("User login for email: john@example.com")
log.info(f"Subtotal: ${subtotal}, Tax: ${tax}, Total: ${total}")

# ❌ Bad: Too generic
log.info("Done")
log.info("Success")

# ❌ Bad: Too verbose
log.info("Starting test")
log.info("Going to click button")
log.info("Clicked button")
log.info("Checking for result")
```

---

## Configuration Management

### Using Config.ini

```python
# ✅ Good: Load from config
from utilities.read_config import ReadConfigPD, RCLoginPage

url = ReadConfigPD.url()
email = RCLoginPage.email()
password = RCLoginPage.password()

# ❌ Bad: Hardcoded values
url = "https://automation.credence.in/shop"
email = "test@example.com"
```

### Environment Variables

```python
# For sensitive data in CI/CD
import os

api_key = os.getenv("API_KEY")
secret_password = os.getenv("TEST_PASSWORD")

if not api_key:
    raise ValueError("API_KEY environment variable not set")
```

---

## Summary

| Guideline | Standard | Example |
|-----------|----------|---------|
| **Classes** | PascalCase | `LoginPage`, `TestLogin` |
| **Methods** | snake_case | `test_login()`, `enter_email()` |
| **Constants** | UPPER_SNAKE_CASE | `DEFAULT_TIMEOUT`, `BASE_URL` |
| **Variables** | snake_case | `email_address`, `is_valid` |
| **Private** | _snake_case | `_helper_method()` |
| **Selectors** | *_suffix | `button_xpath`, `input_id` |
| **Line Length** | 100 chars max | Keep readable |
| **Docstrings** | Google style | See examples above |
| **Comments** | Explain WHY | Not what (obvious from code) |
| **Logging** | Info/Error/Debug | Include context |
| **Config** | External file | config.ini, environment vars |

---

**Last Updated**: April 2025  
**Maintained by**: CredKart QA Team

