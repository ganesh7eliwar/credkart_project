# 🤝 Contributing to CredKart Project

> **Guidelines for Contributing to the CredKart Automated Testing Framework**

Thank you for considering contributing to the CredKart Project! This document contains guidelines and instructions for contributing code, documentation, and improvements to the framework.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Adding New Tests](#adding-new-tests)
5. [Adding New Page Objects](#adding-new-page-objects)
6. [Coding Standards](#coding-standards)
7. [Commit Guidelines](#commit-guidelines)
8. [Pull Request Process](#pull-request-process)
9. [Testing Your Changes](#testing-your-changes)
10. [Documentation](#documentation)
11. [Issue & Feature Request Templates](#issue--feature-request-templates)

---

## 📖 Code of Conduct

### Our Commitment

We are committed to providing a welcoming and inspiring community for all. We expect all contributors to:

✅ **Be Respectful** - Treat all contributors with respect  
✅ **Be Professional** - Keep discussions constructive and focused  
✅ **Be Inclusive** - Welcome contributors from all backgrounds  
✅ **Be Helpful** - Support fellow contributors  
✅ **Report Issues** - Raise concerns privately with maintainers  

### Unacceptable Behavior

❌ Harassment, discrimination, or abusive language  
❌ Deliberate intimidation or threats  
❌ Trolling or insulting comments  
❌ Publishing private information without consent  
❌ Other conduct that violates professional standards  

**Consequences:** Violations will result in action ranging from warnings to removal from the project.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git installed and configured
- GitHub account
- Familiarity with Selenium and Pytest

### Fork & Clone

```bash
# 1. Fork the repository on GitHub
#    (Click "Fork" button on GitHub)

# 2. Clone your forked repository
git clone https://github.com/YOUR_USERNAME/credkart_project.git

# 3. Navigate to project directory
cd CredKart_Project_2025

# 4. Add upstream remote
git remote add upstream https://github.com/ganesh7eliwar/credkart_project.git

# 5. Verify remotes
git remote -v
# Should show: origin (your fork), upstream (original repo)
```

### Setup Development Environment

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create required directories
mkdir logs screenshots html_reports

# 5. Verify installation
pytest testcases/test_url_check.py -v
# Should output: PASSED
```

---

## 🔄 Development Workflow

### Step 1: Create Feature Branch

```bash
# Update local repository
git fetch upstream
git checkout main
git pull upstream main

# Create feature branch with descriptive name
git checkout -b feature/add-payment-validation

# Branch naming conventions:
# - feature/description      - New feature
# - bugfix/description       - Bug fix
# - refactor/description     - Code refactoring
# - docs/description         - Documentation
# - test/description         - Test additions
```

### Step 2: Make Changes

```bash
# Edit files, create new tests, update documentation
# Follow STYLE_GUIDE.md for naming conventions
# Follow existing code patterns

# Examples:
# - Adding test: testcases/test_new_feature.py
# - Adding page object: page_objects/new_page.py
# - Adding utility: utilities/new_utility.py
```

### Step 3: Commit Changes

```bash
# View changes
git status
git diff

# Stage changes
git add .  # All changes
git add testcases/test_new.py  # Specific file

# Commit with descriptive message
git commit -m "feat: add payment validation test"

# Commit conventions (see Commit Guidelines section)
```

### Step 4: Stay Updated

```bash
# Fetch latest changes from upstream
git fetch upstream

# Rebase your branch on top of latest
git rebase upstream/main

# Push your changes
git push origin feature/add-payment-validation
```

### Step 5: Create Pull Request

```bash
# Go to GitHub and create PR from your feature branch
# Provide detailed description
# Link related issues
# Request reviewers
```

---

## 📝 Adding New Tests

### Test File Template

Create `testcases/test_new_feature.py`:

```python
"""
Module: testcases/test_new_feature.py
Purpose: Test new feature functionality
Author: Your Name
Date: 2026-05-01

Description:
    This module contains comprehensive tests for the new feature.
    Tests cover positive flows, edge cases, and error scenarios.
"""

from page_objects.relevant_page import RelevantPage
from utilities.logger import Loggen
from utilities.read_config import ReadConfig
import allure
import pytest


class TestNewFeature:
    """
    Test class for new feature.
    
    This class contains all tests related to the new feature,
    organized by functionality and test scenario.
    """
    
    # ==================== CLASS VARIABLES ====================
    title = ReadConfig.page_title()
    log = Loggen.log_generator()
    
    # ==================== POSITIVE FLOW TESTS ====================
    
    @allure.epic('CredKart Project')
    @allure.feature('New Feature')
    @allure.story('Positive Test Cases')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Feature - Valid Input')
    @allure.description('Test feature with valid input data')
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.order(1)
    def test_feature_positive(self, setup):
        """
        Test feature with valid inputs.
        
        Workflow:
            1. Initialize page object
            2. Perform action with valid data
            3. Verify expected result
            4. Capture screenshot
        
        Expected Result:
            Feature should work correctly with valid inputs
        """
        # Arrange
        self.driver = setup
        self.log.info('========== Test Session Started. ==========')
        self.log.info('Driver Setup Successful.')
        
        page_obj = RelevantPage(self.driver)
        test_data = {
            'input1': 'valid_data_1',
            'input2': 'valid_data_2'
        }
        
        try:
            # Act
            self.log.info('Performing action with valid data')
            page_obj.perform_action(test_data)
            self.log.info('Action completed successfully')
            
            # Assert
            self.log.info('Verifying expected result')
            assert page_obj.is_expected_result_displayed(), \
                'Expected result not displayed'
            self.log.info('Verification passed')
            
            # Screenshot
            page_obj.screenshot()
            self.log.info('Screenshot captured')
            
        except Exception as e:
            self.log.error(f'Test failed: {str(e)}')
            page_obj.screenshot_on_fail()
            raise
        
        finally:
            self.log.info('========== Test Session Finished. ==========')
    
    # ==================== EDGE CASE TESTS ====================
    
    @allure.epic('CredKart Project')
    @allure.feature('New Feature')
    @allure.story('Edge Cases')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Feature - Empty Input')
    @allure.description('Test feature with empty input')
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_feature_empty_input(self, setup):
        """Test feature with empty inputs."""
        # Implementation
        pass
    
    # ==================== ERROR SCENARIO TESTS ====================
    
    @allure.epic('CredKart Project')
    @allure.feature('New Feature')
    @allure.story('Error Handling')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Feature - Invalid Input')
    @allure.description('Test feature error handling')
    @pytest.mark.regression
    @pytest.mark.order(3)
    def test_feature_invalid_input(self, setup):
        """Test feature with invalid inputs."""
        # Implementation
        pass
```

### Test Development Checklist

- ✅ Test file named as `test_*.py`
- ✅ Test class named as `Test*` (PascalCase)
- ✅ Test method named as `test_*` (snake_case)
- ✅ Comprehensive docstrings for class and methods
- ✅ AAA pattern (Arrange, Act, Assert)
- ✅ Appropriate Allure decorators
- ✅ Relevant pytest markers
- ✅ Logging at key points
- ✅ Screenshot on failure
- ✅ Exception handling with finally block
- ✅ Test is independent and doesn't depend on other tests
- ✅ Test passes when feature works correctly
- ✅ Test fails when feature is broken

### Allure Decorator Requirements

Every test MUST have:
```python
@allure.epic('CredKart Project')                  # Always this for consistency
@allure.feature('Feature Name')                   # What feature is being tested
@allure.story('Story Description')                # What specific story/scenario
@allure.title('Clear Test Title')                 # What the test does
@allure.description('Detailed description')       # Why and how it works
@allure.severity(allure.severity_level.CRITICAL)  # CRITICAL/NORMAL/MINOR
```

### Pytest Marker Requirements

Choose appropriate markers:
```python
@pytest.mark.smoke              # Quick sanity check
@pytest.mark.sanity             # Basic functionality
@pytest.mark.regression         # Full test suite
@pytest.mark.integration        # End-to-end flows
@pytest.mark.order(N)           # Execution order
@pytest.mark.dependency         # Depends on other tests
```

---

## 🖥️ Adding New Page Objects

### Page Object Template

Create `page_objects/new_page.py`:

```python
"""
Module: page_objects/new_page.py
Purpose: Page object for new feature page
Author: Your Name

Description:
    Contains locators and interactions for the new feature page.
    Follows POM pattern for maintainability and reusability.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Loggen
import allure
import time


class NewPage:
    """
    Page Object for New Feature Page
    
    This class encapsulates all interactions with the new feature page,
    including element locators, user actions, and verifications.
    
    Attributes:
        driver: WebDriver instance
        wait: WebDriverWait instance with 10 second timeout
        log: Logger instance for logging actions
    """
    
    # ==================== LOCATORS ====================
    # Organize locators into logical sections
    
    # Element locators (input fields, buttons, etc.)
    input_field_id = "input_field_id"
    submit_button_xpath = "//button[@id='submit']"
    success_message_css = ".success-message"
    
    # Error locators
    error_message_xpath = "//div[@class='error-message']"
    validation_error_css = ".validation-error"
    
    # Navigation locators
    next_button_xpath = "//button[text()='Next']"
    back_button_xpath = "//button[text()='Back']"
    
    # ==================== CONSTRUCTOR ====================
    
    def __init__(self, driver):
        """
        Initialize page object.
        
        Args:
            driver: Selenium WebDriver instance
        
        Returns:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Loggen.log_generator()
    
    # ==================== ACTIONS ====================
    
    @allure.step("Entering text: {text} in input field")
    def enter_input(self, text):
        """
        Enter text in input field.
        
        Args:
            text (str): Text to enter
        
        Raises:
            TimeoutException: If element not found within timeout
            NoSuchElementException: If element doesn't exist
        
        Returns:
            None
        """
        try:
            element = self.wait.until(
                EC.presence_of_element_located((By.ID, self.input_field_id))
            )
            element.clear()
            element.send_keys(text)
            self.log.info(f"Entered text: {text}")
        
        except Exception as e:
            self.log.error(f"Failed to enter text: {str(e)}")
            raise
    
    @allure.step("Clicking submit button")
    def click_submit(self):
        """
        Click submit button.
        
        Raises:
            TimeoutException: If button not clickable within timeout
        
        Returns:
            None
        """
        try:
            button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.submit_button_xpath))
            )
            button.click()
            self.log.info("Submit button clicked")
        
        except Exception as e:
            self.log.error(f"Failed to click submit: {str(e)}")
            raise
    
    # ==================== VERIFICATIONS ====================
    
    def is_success_message_displayed(self):
        """
        Verify success message is displayed.
        
        Returns:
            bool: True if success message visible, False otherwise
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.success_message_css))
            )
            self.log.info("Success message displayed")
            return True
        
        except:
            self.log.info("Success message not displayed")
            return False
    
    def get_error_message(self):
        """
        Get error message text.
        
        Returns:
            str: Error message text or empty string if not found
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.error_message_xpath))
            )
            message = element.text
            self.log.info(f"Error message: {message}")
            return message
        
        except:
            self.log.info("No error message found")
            return ""
    
    # ==================== UTILITIES ====================
    
    @allure.step("Capturing screenshot")
    def screenshot(self):
        """
        Capture screenshot of current page.
        
        Returns:
            None
        """
        try:
            filename = f"screenshots/pass_screenshot_{int(time.time())}.png"
            self.driver.save_screenshot(filename)
            self.log.info(f"Screenshot saved: {filename}")
        
        except Exception as e:
            self.log.error(f"Failed to capture screenshot: {str(e)}")
    
    @allure.step("Capturing failure screenshot")
    def screenshot_on_fail(self):
        """
        Capture screenshot on test failure.
        
        Returns:
            None
        """
        try:
            filename = f"screenshots/fail_screenshot_{int(time.time())}.png"
            self.driver.save_screenshot(filename)
            self.log.error(f"Failure screenshot saved: {filename}")
        
        except Exception as e:
            self.log.error(f"Failed to capture failure screenshot: {str(e)}")
```

### Page Object Checklist

- ✅ All locators defined as class variables at top
- ✅ Locators organized into logical sections
- ✅ Constructor initializes driver, wait, and logger
- ✅ Methods have clear, descriptive names
- ✅ Methods have comprehensive docstrings
- ✅ Methods use explicit waits (WebDriverWait)
- ✅ Methods include exception handling
- ✅ Methods use @allure.step decorators
- ✅ Logging included for all significant actions
- ✅ Each method does one thing well (Single Responsibility)
- ✅ No assertions in page objects (only in tests)
- ✅ Verification methods return boolean or value

---

## 📝 Coding Standards

Refer to [STYLE_GUIDE.md](STYLE_GUIDE.md) for comprehensive coding standards.

### Key Standards

#### Naming Conventions

```python
# Classes - PascalCase
class LoginPage:
    pass

# Methods/Functions - snake_case
def login_with_valid_credentials():
    pass

# Variables - snake_case
username = "admin"
password = "pass123"

# Constants - UPPER_SNAKE_CASE
MAX_TIMEOUT = 10
BASE_URL = "https://automation.credence.in/shop"

# Private methods - _snake_case
def _wait_for_element():
    pass

# Locators - Include selector type suffix
login_button_xpath = "//button[@id='login']"
email_input_id = "email_field"
password_input_css = "input[type='password']"
```

#### Docstring Format

```python
def method_name(param1, param2):
    """
    Short description of what method does.
    
    Longer description if needed. Explain the purpose,
    workflow, and important details.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
    
    Returns:
        bool: True if successful, False otherwise
    
    Raises:
        TimeoutException: If element not found
        NoSuchElementException: If element doesn't exist
    
    Examples:
        >>> result = method_name("value1", 10)
        >>> assert result == True
    """
    pass
```

#### Code Style

```python
# Line length - 80 characters max for docstrings, 100 for code
# Imports - Group by: standard library, third-party, local
import os
import sys
from time import sleep

import pytest
import allure
from selenium import webdriver

from utilities.logger import Loggen
from page_objects.login_page import LoginPage

# Spacing
# 2 empty lines between class definitions
class FirstClass:
    pass


class SecondClass:
    pass

# 1 empty line between methods
def method_one(self):
    pass

def method_two(self):
    pass
```

---

## 📝 Commit Guidelines

### Conventional Commits Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat** - New feature
- **fix** - Bug fix
- **test** - Adding/updating tests
- **docs** - Documentation changes
- **refactor** - Code refactoring
- **style** - Code style changes (formatting, etc.)
- **chore** - Maintenance tasks

### Examples

```bash
# Good commits
git commit -m "feat(login): add two-factor authentication"
git commit -m "fix(cart): resolve item quantity calculation bug"
git commit -m "test(checkout): add payment validation tests"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(page_objects): improve wait strategy"

# Bad commits
git commit -m "fixed bug"
git commit -m "updated files"
git commit -m "changes"
```

### Multi-line Commits

```bash
git commit -m "feat(login): add email verification

- Verify email before account activation
- Send verification link to registered email
- Resend link if not clicked within 24 hours

Closes #123"
```

---

## 🔄 Pull Request Process

### Before Submitting PR

1. **Update your branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests locally**
   ```bash
   pytest testcases/ -v
   # All tests should pass before PR
   ```

3. **Check code style**
   ```bash
   # Follow STYLE_GUIDE.md
   # All code should follow naming conventions
   # All methods should have docstrings
   ```

4. **Run linter (optional)**
   ```bash
   pip install flake8
   flake8 testcases/ page_objects/ utilities/
   ```

### PR Template

```markdown
## Description
Concise description of changes

## Related Issues
Fixes #123
Relates to #456

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Test addition

## Testing
- [ ] All tests pass locally
- [ ] Added new tests (if applicable)
- [ ] Tested on Chrome, Firefox
- [ ] No console errors

## Screenshots
Add before/after screenshots if applicable

## Checklist
- [ ] Code follows STYLE_GUIDE.md
- [ ] All methods have docstrings
- [ ] Commits follow conventional format
- [ ] No hardcoded values or credentials
- [ ] Logging included for debugging
- [ ] Test logic not modified
```

### Review Process

1. **Request reviews** from maintainers
2. **Address feedback** with new commits
3. **Update PR description** if scope changed
4. **Wait for approval** (usually 24-48 hours)
5. **Maintainer merges** when approved

---

## 🧪 Testing Your Changes

### Before Submitting PR

```bash
# Run all tests
pytest testcases/ -v

# Run specific test file
pytest testcases/test_your_test.py -v

# Run with coverage
pip install pytest-cov
pytest testcases/ --cov=testcases/ --cov-report=html

# Run with specific marker
pytest testcases/ -v -m sanity

# Run in parallel (if no dependencies)
pytest testcases/ -v -n 4
```

### Test Requirements

- ✅ All tests pass locally
- ✅ No new warnings or errors
- ✅ No breaking changes
- ✅ Backward compatible
- ✅ Code coverage maintained
- ✅ Tests are independent

---

## 📚 Documentation

### Documentation Standards

1. **Docstrings for All Methods**
   ```python
   def method(self):
       """Short description."""
       pass
   ```

2. **Comments for Complex Logic**
   ```python
   # Calculate discounted price
   # Discount = base_price * discount_percentage / 100
   discounted_price = price * (1 - discount / 100)
   ```

3. **README Updates**
   - Update README.md if adding major features
   - Update STYLE_GUIDE.md if new patterns
   - Add examples if introducing new utilities

4. **Inline Comments**
   ```python
   # ✅ GOOD - Explains WHY
   # Use explicit wait instead of implicit sleep
   # to handle dynamic content loading
   element = wait.until(EC.presence_of_element_located((By.ID, "id")))
   
   # ❌ BAD - States the obvious
   # Wait for element
   element = wait.until(EC.presence_of_element_located((By.ID, "id")))
   ```

---

## 🐛 Issue & Feature Request Templates

### Bug Report Template

```markdown
## Description
Clear and concise description of the bug

## Steps to Reproduce
1. Run test X
2. Observe behavior
3. Verify result

## Expected Behavior
What should happen?

## Actual Behavior
What actually happened?

## Environment
- OS: Windows 10
- Python: 3.9
- Browser: Chrome 90

## Screenshots/Logs
Include relevant screenshots or logs

## Additional Context
Any other relevant information
```

### Feature Request Template

```markdown
## Feature Description
Clear description of desired feature

## Motivation
Why is this feature needed?

## Proposed Solution
How should it work?

## Examples
Provide usage examples

## Alternative Solutions
Are there alternatives?

## Additional Context
Any other relevant information
```

---

## ✅ Contribution Checklist

Before submitting PR, verify:

- [ ] Branch created from latest `main`
- [ ] All tests pass locally
- [ ] Code follows STYLE_GUIDE.md
- [ ] New tests added for new features
- [ ] Docstrings added to all methods
- [ ] No hardcoded credentials
- [ ] Logging included
- [ ] Commits follow conventional format
- [ ] PR description comprehensive
- [ ] No merge conflicts
- [ ] Screenshots added (if UI changes)
- [ ] Documentation updated

---

## 🙏 Recognition

Contributors will be:
- ✅ Added to contributors list
- ✅ Credited in release notes
- ✅ Mentioned in project acknowledgments
- ✅ Featured in contributor spotlights

---

## 📞 Contact

- 📧 Email: ganesh.sateliwar@example.com
- 💬 GitHub Issues: [Create Issue](https://github.com/ganesh7eliwar/credkart_project/issues)
- 💡 GitHub Discussions: [Start Discussion](https://github.com/ganesh7eliwar/credkart_project/discussions)

---

## 📖 Additional Resources

- [STYLE_GUIDE.md](STYLE_GUIDE.md) - Coding standards
- [README_COMPREHENSIVE.md](README_COMPREHENSIVE.md) - Detailed documentation
- [Selenium Best Practices](https://www.selenium.dev/documentation/webdriver/best_practices/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Thank you for contributing! 🎉**

*Last Updated: May 1, 2026*


