# 📖 CredKart Project - Comprehensive Documentation

> **Complete Technical Guide | In-Depth Tutorials | Advanced Configurations**

---

## 📑 Table of Contents

1. [Installation Guide](#installation-guide)
2. [Project Architecture](#project-architecture)
3. [Test Execution Guide](#test-execution-guide)
4. [Page Object Model](#page-object-model)
5. [Data-Driven Testing](#data-driven-testing)
6. [Pytest Configuration](#pytest-configuration)
7. [Logging System](#logging-system)
8. [Allure Reporting](#allure-reporting)
9. [CI/CD Integration](#cicd-integration)
10. [Debugging Guide](#debugging-guide)
11. [Best Practices](#best-practices)
12. [Troubleshooting](#troubleshooting)

---

## Installation Guide

### System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 4 GB
- **Disk**: Minimum 2 GB free space
- **Browser**: Chrome 90+ or Firefox 88+

### Verify Prerequisites

```bash
# Check Python version
python --version  # Should be 3.8+

# Check pip is installed
pip --version

# Check git is installed
git --version
```

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
# Using HTTPS (recommended for first-time)
git clone https://github.com/ganesh7eliwar/credkart_project.git

# OR using SSH (if you have SSH key configured)
git clone git@github.com:ganesh7eliwar/credkart_project.git

# Navigate to project directory
cd credkart_project
```

#### 2. Create Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Verify activation (should show (venv) prefix)
python --version
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation
python --version
```

#### 3. Install Dependencies

```bash
# Upgrade pip (important!)
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Verify installation
pip list
```

#### 4. Create Required Directories

```bash
# Create logs directory
mkdir logs

# Create screenshots directory (if not exists)
mkdir screenshots

# Verify directories are created
ls -la  # macOS/Linux
dir     # Windows
```

#### 5. Verify Installation

```bash
# Run a quick test to verify setup
pytest testcases/test_url_check.py -v

# You should see: PASSED (test completed successfully)
```

### Troubleshooting Installation

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'pytest'` | Run `pip install -r requirements.txt` again |
| `Permission denied: ./venv/bin/activate` | Use `source venv/bin/activate` instead |
| `python: command not found` | Use `python3` on macOS/Linux |
| `Chrome driver error` | `pip install --upgrade webdriver-manager` |

---

## Project Architecture

### Directory Structure Explained

```
credkart_project/
│
├── testcases/                    # All test files
│   ├── conftest.py              # Pytest configuration & fixtures
│   ├── test_*.py                # Individual test files
│   └── __pycache__/             # Cache (auto-generated)
│
├── page_objects/                 # Page Object Model classes
│   ├── login_page.py            # Login page elements & methods
│   ├── register_page.py         # Registration page
│   ├── add_item_to_cart.py      # Cart operations
│   ├── checkout.py              # Checkout flow
│   ├── wishlist_page.py         # Wishlist management
│   └── common_elements.py       # Shared UI elements
│
├── utilities/                    # Helper functions
│   ├── logger.py                # Logging utility
│   ├── read_config.py           # Configuration reader
│   ├── generator.py             # Test data generation
│   ├── excelutils.py            # Excel file operations
│   └── wait_utilities.py        # Wait helper functions
│
├── configurations/               # Configuration files
│   └── config.ini               # Test configuration
│
├── test_data/                    # Test data files
│   ├── user_details.json        # Single user data
│   ├── all_user_details.json    # Multiple users
│   └── Credkart_Login_Data.xlsx # DDT Excel file
│
├── logs/                         # Test execution logs
│   └── credkart_logs.log        # Main log file
│
├── screenshots/                  # Test screenshots
│   └── YYYY-MM-DD_HH-MM-SS_*.png
│
├── html_reports/                 # HTML reports
│   └── report.html              # Test report
│
├── allure_reports/               # Allure report data
│   └── (auto-generated)
│
├── README.md                     # Quick start guide
├── README_COMPREHENSIVE.md       # This file
├── CONTRIBUTING.md              # Contribution guidelines
├── IMPROVEMENTS_SUMMARY.md      # Changelog
├── requirements.txt             # Python dependencies
├── pytest.ini                   # Pytest configuration
├── Jenkinsfile                  # Jenkins pipeline
├── .gitignore                   # Git ignore rules
└── LICENSE                      # MIT License
```

### Architecture Diagram

```
┌─────────────────────────────────────┐
│      Pytest Test Runner             │
│  (Executes tests with fixtures)     │
└────────────┬────────────────────────┘
             │
    ┌────────▼─────────┐
    │   Test Cases     │
    │  (test_*.py)     │
    └────────┬─────────┘
             │
    ┌────────▼──────────────┐
    │  Page Object Model    │
    │  (Selenium locators   │
    │   & interactions)     │
    └────────┬──────────────┘
             │
    ┌────────▼──────────────┐
    │  Browser/WebDriver    │
    │  (Chrome, Firefox)    │
    └────────┬──────────────┘
             │
    ┌────────▼──────────────┐
    │   Test Application    │
    │  (AUT - credence.in)  │
    └──────────────────────┘

    ▼ (Parallel Process)
┌──────────────────────┐
│   Logging System     │
│  (credkart_logs.log) │
└──────────────────────┘

    ▼ (Post-Execution)
┌──────────────────────┐
│   Report Generation  │
│  (HTML, Allure)      │
└──────────────────────┘
```

---

## Test Execution Guide

### Running All Tests

```bash
# Basic execution (headless)
pytest testcases/ -v

# With specific browser
pytest testcases/ -v --browser chrome

# With detailed output
pytest testcases/ -v -s

# Stop on first failure
pytest testcases/ -v -x

# Show test names only
pytest testcases/ --collect-only
```

### Running Specific Test File

```bash
# Run single file
pytest testcases/test_login.py -v

# Run multiple specific files
pytest testcases/test_login.py testcases/test_register.py -v

# Run tests in specific class
pytest testcases/test_login.py::TestLogin -v

# Run specific test method
pytest testcases/test_login.py::TestLogin::test_valid_login -v
```

### Running by Markers

```bash
# Smoke tests only
pytest testcases/ -v -m smoke

# Regression tests
pytest testcases/ -v -m regression

# Multiple markers (OR)
pytest testcases/ -v -m "smoke or sanity"

# Exclude markers
pytest testcases/ -v -m "not slow"

# Complex expressions
pytest testcases/ -v -m "regression and not slow"
```

### Advanced Execution

```bash
# Parallel execution (requires pytest-xdist)
pytest testcases/ -v -n 4  # Run on 4 workers

# Show timing information
pytest testcases/ -v --durations=10  # Top 10 slowest

# Keep test database between runs
pytest testcases/ -v --lf  # Last failed
pytest testcases/ -v --ff  # Failed first

# Verbose output with step details
pytest testcases/ -vv

# Quieter output
pytest testcases/ -q
```

### With Reporting

```bash
# HTML Report
pytest testcases/ -v --html=html_reports/report.html --self-contained-html

# Allure Report
pytest testcases/ -v --alluredir=allure_reports

# Combined (all reporting)
pytest testcases/ -v \
  --html=html_reports/report.html \
  --alluredir=allure_reports \
  --browser chrome
```

---

## Page Object Model

### Concept

The Page Object Model (POM) is a design pattern that improves test maintainability by:

- **Encapsulating** page elements and interactions
- **Reducing** code duplication
- **Improving** readability and maintainability
- **Centralizing** element locators

### Structure

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

class BasePage:
    """Base page class with common functionality."""
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger()
        self.wait = WebDriverWait(driver, 10)


class LoginPage(BasePage):
    """Login page object model."""
    
    # Locators (private attributes)
    _USERNAME_INPUT = (By.ID, "username")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    _ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")
    
    # Public methods
    def navigate_to_login(self):
        """Navigate to login page."""
        self.logger.info("Navigating to login page")
        self.driver.get("https://automation.credence.in/shop/auth/login")
    
    def enter_username(self, username):
        """Enter username."""
        self.logger.info(f"Entering username: {username}")
        element = self.wait.until(
            EC.presence_of_element_located(self._USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)
    
    def enter_password(self, password):
        """Enter password."""
        self.logger.info("Entering password")
        element = self.wait.until(
            EC.presence_of_element_located(self._PASSWORD_INPUT)
        )
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        """Click login button."""
        self.logger.info("Clicking login button")
        button = self.wait.until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        )
        button.click()
    
    def is_logged_in(self):
        """Check if user is logged in."""
        try:
            self.driver.find_element(By.XPATH, "//h1[text()='Dashboard']")
            self.logger.info("User successfully logged in")
            return True
        except:
            self.logger.error("Login failed - Dashboard not found")
            return False
    
    def get_error_message(self):
        """Get error message text."""
        self.logger.info("Retrieving error message")
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self._ERROR_MESSAGE)
            )
            return element.text
        except:
            self.logger.error("Error message not found")
            return None
```

### Usage in Tests

```python
import pytest
from page_objects.login_page import LoginPage


class TestLoginFunctionality:
    """Login feature tests."""
    
    def test_valid_login(self, driver):
        """Test login with valid credentials."""
        # Arrange
        page = LoginPage(driver)
        username = "valid_user"
        password = "valid_password"
        
        # Act
        page.navigate_to_login()
        page.enter_username(username)
        page.enter_password(password)
        page.click_login()
        
        # Assert
        assert page.is_logged_in(), "User should be logged in"
    
    def test_invalid_login(self, driver):
        """Test login with invalid credentials."""
        page = LoginPage(driver)
        
        page.navigate_to_login()
        page.enter_username("invalid_user")
        page.enter_password("wrong_password")
        page.click_login()
        
        error_message = page.get_error_message()
        assert error_message is not None, "Error message should be displayed"
```

### Best Practices

✅ **Do**
- Use descriptive method names
- Keep methods focused on single action
- Use explicit waits
- Add logging to methods
- Inherit from BasePage
- Use descriptive locator names

❌ **Don't**
- Create page objects for every small interaction
- Use implicit waits only
- Mix multiple actions in one method
- Hardcode waits with time.sleep()
- Create methods that do too much
- Use page objects in multiple unrelated ways

---

## Data-Driven Testing

### Excel-Based DDT

#### Create Excel File

File: `test_data/Credkart_Login_Data.xlsx`

```
┌─────────────┬──────────────┬──────────────┬──────────┐
│ Username    │ Password     │ ExpectedResult│ TestCase │
├─────────────┼──────────────┼──────────────┼──────────┤
│ user1       │ pass1        │ success      │ Valid1   │
│ user2       │ pass2        │ success      │ Valid2   │
│ invalid_usr │ wrong_pass   │ failure      │ Invalid1 │
│ blank       │ pass3        │ failure      │ Invalid2 │
└─────────────┴──────────────┴──────────────┴──────────┘
```

#### Read Excel Data

```python
from utilities.excelutils import ExcelUtils

class TestLoginDataDriven:
    """Data-driven login tests from Excel."""
    
    def test_login_ddt(self, driver):
        """Test login with Excel data."""
        excel = ExcelUtils("test_data/Credkart_Login_Data.xlsx")
        rows = excel.read_data("Sheet1")
        
        for row in rows:
            username = row["Username"]
            password = row["Password"]
            expected = row["ExpectedResult"]
            
            page = LoginPage(driver)
            page.navigate_to_login()
            page.enter_username(username)
            page.enter_password(password)
            page.click_login()
            
            if expected == "success":
                assert page.is_logged_in()
            else:
                assert page.get_error_message() is not None
```

### Fixture-Based Parameterization

#### Define Fixtures

File: `testcases/conftest.py`

```python
import pytest


@pytest.fixture(
    params=[
        {"username": "user1", "password": "pass1", "expected": "success"},
        {"username": "user2", "password": "pass2", "expected": "success"},
        {"username": "invalid", "password": "wrong", "expected": "failure"},
    ]
)
def login_credentials(request):
    """Parameterized login credentials fixture."""
    return request.param
```

#### Use in Tests

```python
def test_login_with_fixture(self, driver, login_credentials):
    """Test login using parameterized fixture."""
    page = LoginPage(driver)
    page.navigate_to_login()
    page.enter_username(login_credentials["username"])
    page.enter_password(login_credentials["password"])
    page.click_login()
    
    if login_credentials["expected"] == "success":
        assert page.is_logged_in()
    else:
        assert page.get_error_message() is not None
```

---

## Pytest Configuration

### pytest.ini File

```ini
[pytest]
# Minimum version
minversion = 6.0

# Test discovery patterns
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Marker definitions
markers =
    smoke: Quick sanity checks
    sanity: Basic functional tests
    regression: Full regression suite
    integration: End-to-end tests
    user_management: User auth tests
    cart_management: Shopping cart tests
    wishlist_management: Wishlist tests
    checkout: Checkout flow tests
    ddt: Data-driven tests
    parametrize: Parameterized tests
    slow: Long-running tests
    skip_ci: Skip in CI/CD

# Console output options
addopts = 
    -v
    --strict-markers
    --tb=short

# Logging configuration
log_cli = true
log_cli_level = INFO
log_file = logs/pytest.log
log_file_level = DEBUG
```

### Running with Configuration

```bash
# Pytest automatically finds pytest.ini

# Using markers
pytest testcases/ -m smoke  # Uses markers from pytest.ini

# With custom config
pytest testcases/ -c custom_pytest.ini
```

---

## Logging System

### Logger Implementation

```python
# utilities/logger.py
import logging
import inspect


class Logger:
    """Custom logger with introspection."""
    
    @staticmethod
    def get_logger():
        """Get configured logger instance."""
        logger = logging.getLogger(__name__)
        
        if not logger.handlers:
            # File handler
            fh = logging.FileHandler("logs/credkart_logs.log")
            fh.setLevel(logging.DEBUG)
            
            # Console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            
            # Formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            
            logger.addHandler(fh)
            logger.addHandler(ch)
            logger.setLevel(logging.DEBUG)
        
        return logger
    
    @staticmethod
    def log_with_context(message, level="info"):
        """Log with function context."""
        logger = Logger.get_logger()
        frame = inspect.currentframe().f_back
        function_name = frame.f_code.co_name
        line_number = frame.f_lineno
        
        log_message = f"{function_name}() [Line {line_number}]: {message}"
        
        if level.lower() == "debug":
            logger.debug(log_message)
        elif level.lower() == "warning":
            logger.warning(log_message)
        elif level.lower() == "error":
            logger.error(log_message)
        else:
            logger.info(log_message)
```

### Usage in Code

```python
from utilities.logger import Logger

class MyTestClass:
    """Test class using logger."""
    
    def __init__(self):
        self.logger = Logger.get_logger()
    
    def test_example(self):
        """Example test with logging."""
        self.logger.info("Starting test")
        self.logger.debug("Debug information")
        self.logger.warning("Warning message")
        self.logger.error("Error occurred")
```

### Log File Location

```bash
# View logs
tail -100 logs/credkart_logs.log  # Last 100 lines
tail -f logs/credkart_logs.log     # Follow live logs

# Search logs
grep "ERROR" logs/credkart_logs.log
grep "test_login" logs/credkart_logs.log
```

---

## Allure Reporting

### Generate Allure Report

```bash
# Run tests with Allure
pytest testcases/ -v --alluredir=allure_reports

# Serve report (requires Allure CLI installed)
allure serve allure_reports/

# Or generate static HTML
allure generate allure_reports/ -o allure_html
```

### Add Allure Decorators

```python
import allure


@allure.feature("User Authentication")
@allure.story("Login with valid credentials")
@allure.title("Valid Login Test")
@allure.description("Test login with valid username and password")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    """Test login functionality."""
    page = LoginPage(driver)
    page.navigate_to_login()
    page.enter_username("valid_user")
    page.enter_password("valid_pass")
    
    with allure.step("Click login button"):
        page.click_login()
    
    with allure.step("Verify user is logged in"):
        assert page.is_logged_in()
```

### Severity Levels

```python
@allure.severity(allure.severity_level.CRITICAL)   # Critical
@allure.severity(allure.severity_level.NORMAL)     # Normal
@allure.severity(allure.severity_level.MINOR)      # Minor
@allure.severity(allure.severity_level.TRIVIAL)    # Trivial
@allure.severity(allure.severity_level.BLOCKER)    # Blocker
```

---

## CI/CD Integration

### Jenkins Pipeline

File: `Jenkinsfile`

```groovy
pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    python -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest testcases/ -v \
                        --html=html_reports/report.html \
                        --alluredir=allure_reports
                '''
            }
        }
        
        stage('Report') {
            steps {
                publishHTML([
                    reportDir: 'html_reports',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
                
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure_reports']]
                ])
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'screenshots/**', 
                             allowEmptyArchive: true
        }
    }
}
```

### GitHub Actions

File: `.github/workflows/tests.yml`

```yaml
name: Automated Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10']
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest testcases/ -v \
          --html=html_reports/report.html \
          --alluredir=allure_reports
    
    - name: Upload reports
      if: always()
      uses: actions/upload-artifact@v2
      with:
        name: reports
        path: |
          html_reports/
          allure_reports/
          screenshots/
```

---

## Debugging Guide

### Debug Failed Tests

```bash
# Run with verbose output
pytest testcases/test_login.py -v -s --tb=long

# Show local variables
pytest testcases/test_login.py -v --showlocals

# Stop on first failure
pytest testcases/ -v -x

# Last failed tests
pytest testcases/ --lf

# Failed first
pytest testcases/ --ff
```

### Using Python Debugger

```python
def test_with_debugger(driver):
    """Test with debugger."""
    page = LoginPage(driver)
    page.navigate_to_login()
    
    # Set breakpoint
    import pdb; pdb.set_trace()
    
    page.enter_username("user")
```

### Using Print Debugging

```python
def test_with_prints(driver):
    """Test with print statements."""
    page = LoginPage(driver)
    print("Page object created")
    
    page.navigate_to_login()
    print("Navigated to login")
    
    page.enter_username("user")
    print("Username entered")
```

### Check Screenshots

```bash
# List all screenshots
ls -lat screenshots/

# View specific screenshot
open screenshots/YYYY-MM-DD_HH-MM-SS_test_name.png
```

---

## Best Practices

### 1. Test Independence

✅ Each test should be standalone
✅ No dependencies between tests
✅ Can run in any order

### 2. Explicit Over Implicit

✅ Use explicit waits
❌ Avoid `time.sleep()`

```python
# Good
wait.until(EC.presence_of_element_located(locator))

# Bad
time.sleep(5)
```

### 3. Page Object Model

✅ Centralize locators
✅ Encapsulate interactions
✅ Reuse across tests

### 4. Meaningful Assertions

✅ Use clear assertions
❌ Generic assertions

```python
# Good
assert page.is_logged_in(), "User should be logged in after valid login"

# Bad
assert True
```

### 5. Logging & Documentation

✅ Log significant actions
✅ Add docstrings
✅ Use descriptive names

### 6. Error Handling

✅ Handle expected errors
✅ Log exceptions
✅ Fail with clear messages

```python
try:
    element = driver.find_element(By.ID, "username")
except NoSuchElementException:
    self.logger.error("Username element not found")
    raise
```

---

## Troubleshooting

### Common Issues

#### 1. ChromeDriver Version Mismatch

**Error**: `SessionNotCreatedException`

**Solution**:
```bash
pip install --upgrade webdriver-manager
```

#### 2. Element Not Found

**Error**: `NoSuchElementException`

**Solution**:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "element_id")))
```

#### 3. Stale Element Reference

**Error**: `StaleElementReferenceException`

**Solution**: Refetch element before interaction
```python
element = driver.find_element(By.ID, "username")  # Refetch
element.send_keys("value")
```

#### 4. Logs Directory Not Found

**Error**: `FileNotFoundError: logs/credkart_logs.log`

**Solution**:
```bash
mkdir logs
```

#### 5. Tests Not Discovered

**Error**: `no tests ran`

**Solution**:
- Verify file names start with `test_`
- Verify test methods start with `test_`
- Check pytest can find files: `pytest --collect-only`

#### 6. Fixture Not Found

**Error**: `fixture 'driver' not found`

**Solution**: Ensure `conftest.py` is in `testcases/` directory

---

## 📊 Performance Optimization

### Run Tests Faster

```bash
# Headless mode (default)
pytest testcases/ -v  # ~1min 45sec

# Parallel execution (4 workers)
pytest testcases/ -v -n 4  # ~45 seconds

# Specific markers only
pytest testcases/ -v -m smoke  # ~30 seconds
```

### Profile Test Execution

```bash
# Show slowest tests
pytest testcases/ --durations=10

# Time individual tests
pytest testcases/ --durations=0
```

---

## 🔗 Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [Python Logging](https://docs.python.org/3/library/logging.html)

---

**Last Updated**: May 1, 2026  
**Status**: ✅ Production Ready  
**Version**: 2.0
