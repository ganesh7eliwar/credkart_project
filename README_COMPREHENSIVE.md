# 📖 CredKart Project - Comprehensive Documentation

> **Complete Guide to the CredKart Automated Testing Framework**  
> Setup | Execution | Reporting | CI/CD | Best Practices

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Complete Installation Guide](#complete-installation-guide)
4. [Project Architecture](#project-architecture)
5. [Test Structure & Organization](#test-structure--organization)
6. [Configuration Guide](#configuration-guide)
7. [Test Execution Guide](#test-execution-guide)
8. [Data-Driven Testing](#data-driven-testing)
9. [Logging & Debugging](#logging--debugging)
10. [Allure Reporting](#allure-reporting)
11. [Pytest Plugins & Features](#pytest-plugins--features)
12. [CI/CD Integration](#cicd-integration)
13. [Page Object Model Guide](#page-object-model-guide)
14. [Best Practices](#best-practices)
15. [Troubleshooting](#troubleshooting)
16. [FAQ](#faq)

---

## 🎯 Project Overview

### Purpose
The **CredKart Project** is an enterprise-grade automation framework designed to thoroughly test e-commerce web applications. It automates critical workflows including:
- User authentication (login/registration)
- Product browsing and searching
- Shopping cart management
- Wishlist operations
- Checkout and payment processing
- End-to-end purchase flows

### Framework Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Test Execution Layer                     │
│          (Pytest | Fixtures | Markers | Reports)            │
├─────────────────────────────────────────────────────────────┤
│                   Page Object Model Layer                    │
│  (Login | Register | Cart | Wishlist | Checkout | URL Check)│
├─────────────────────────────────────────────────────────────┤
│                    Utilities & Helpers Layer                 │
│   (Logger | Config Reader | Excel Utils | Data Generator)   │
├─────────────────────────────────────────────────────────────┤
│                   Selenium WebDriver Layer                   │
│         (Chrome | Firefox | Headless | Driver Pool)         │
├─────────────────────────────────────────────────────────────┤
│                   Browser Automation Layer                   │
│    (Element Interactions | Waits | Screenshots | Actions)    │
├─────────────────────────────────────────────────────────────┤
│                    Application Under Test                    │
│             (https://automation.credence.in/shop)            │
└─────────────────────────────────────────────────────────────┘
```

### Key Features
- ✅ **Page Object Model (POM)** for maintainability
- ✅ **Data-Driven Testing (DDT)** with Excel support
- ✅ **Parameterized Tests** using pytest fixtures
- ✅ **Rich Logging** with introspection-based logger
- ✅ **Allure Reporting** with epic/feature/story organization
- ✅ **Screenshot Capture** on pass/fail for debugging
- ✅ **Multiple Browser Modes** (headless, visible, specific browsers)
- ✅ **Test Markers** for categorization and filtering
- ✅ **CI/CD Ready** with Jenkinsfile
- ✅ **Cross-Platform** support (Windows, macOS, Linux)

---

## 📋 Prerequisites

### System Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **Memory**: Minimum 2GB RAM
- **Disk Space**: 500MB for dependencies + logs

### Required Software

```bash
# Check Python version (should be 3.8+)
python --version

# Git (for cloning repository)
git --version
```

### Browser Requirements
- **Chrome 90+** (auto-managed via webdriver-manager)
- **Firefox 88+** (auto-managed via webdriver-manager)
- Does NOT require manual ChromeDriver/GeckoDriver download

---

## 📦 Complete Installation Guide

### Step 1: Clone Repository

```bash
# Clone the repository
git clone https://github.com/ganesh7eliwar/credkart_project.git

# Navigate to project directory
cd CredKart_Project_2025
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# Verify installation (should list all packages with versions)
pip list
```

### Step 4: Create Required Directories

```bash
# Create logs directory
mkdir logs

# Create screenshots directory (if not exists)
mkdir screenshots

# Create html_reports directory
mkdir html_reports
```

### Step 5: Verify Installation

```bash
# Run sanity check test
pytest testcases/test_url_check.py -v

# Should display: PASSED
```

---

## 🏗️ Project Architecture

### Complete Directory Structure

```
CredKart_Project_2025/
│
├── 📁 testcases/
│   ├── conftest.py                      # Pytest fixtures & configuration hooks
│   ├── test_url_check.py                # Sanity check - URL & page title validation
│   ├── test_register.py                 # Registration workflow with valid data
│   ├── test_login.py                    # Login with valid credentials
│   ├── test_login_ddt.py                # Data-driven login (Excel-based)
│   ├── test_login_param.py              # Parameterized login (fixture-based)
│   ├── test_add_item_to_cart.py         # Add random item to shopping cart
│   ├── test_empty_cart.py               # Empty cart functionality
│   ├── test_add_item_to_wishlist.py     # Add item to wishlist
│   ├── test_empty_wishlist.py           # Empty wishlist functionality
│   └── test_end_to_end.py               # Complete purchase flow (registration → checkout)
│
├── 📁 page_objects/
│   ├── login_page.py                    # Login page interactions & locators
│   ├── register_page.py                 # Registration form elements
│   ├── add_item_to_cart.py              # Shopping cart operations
│   ├── add_item_to_wishlist.py          # Wishlist operations
│   ├── empty_cart_wishlist.py           # Clear cart/wishlist operations
│   ├── checkout.py                      # Checkout & payment page
│   └── url_check.py                     # URL sanity check page object
│
├── 📁 utilities/
│   ├── logger.py                        # Introspection-based logging utility
│   ├── read_config.py                   # Configuration file reader
│   ├── generator.py                     # Test data generator (names, emails, passwords)
│   └── excelutils.py                    # Excel operations (read/write)
│
├── 📁 configurations/
│   └── config.ini                       # Test configuration (URLs, credentials, messages)
│
├── 📁 test_data/
│   ├── Credkart_Login_Data.xlsx         # DDT: Login credentials for parameterized tests
│   ├── user_details.json                # Last registered user details
│   └── all_user_details.json            # Historical user records
│
├── 📁 logs/
│   └── credkart_logs.log                # Consolidated test execution logs
│
├── 📁 screenshots/
│   ├── pass_screenshots/                # Screenshots from passed tests
│   └── fail_screenshots/                # Screenshots from failed tests
│
├── 📁 html_reports/
│   └── report.html                      # HTML test report (generated)
│
├── 📁 allure_reports/
│   ├── *.json                           # Allure report data (generated)
│   └── (index.html after serving)
│
├── 📄 README.md                         # Quick reference & overview
├── 📄 README_COMPREHENSIVE.md           # This file - detailed documentation
├── 📄 CONTRIBUTING.md                   # Contribution guidelines
├── 📄 STYLE_GUIDE.md                    # Code standards & naming conventions
├── 📄 IMPROVEMENTS_SUMMARY.md           # Recent enhancements & changes
├── 📄 LICENSE                           # MIT License
├── 📄 requirements.txt                  # Python dependencies (61 packages)
├── 📄 pytest.ini                        # Pytest configuration & markers
├── 📄 Jenkinsfile                       # Jenkins CI/CD pipeline
└── 📄 .gitignore                        # Git ignore rules
```

### Test Count & Organization

| Category | Count | Markers |
|----------|-------|---------|
| Sanity/Smoke | 1 | `@pytest.mark.smoke` |
| Registration | 1 | `@pytest.mark.sanity`, `@pytest.mark.user_management` |
| Login (Standard) | 1 | `@pytest.mark.sanity`, `@pytest.mark.user_management` |
| Login (Data-Driven) | 1 | `@pytest.mark.ddt`, `@pytest.mark.regression` |
| Login (Parameterized) | 1 | `@pytest.mark.parametrize`, `@pytest.mark.regression` |
| Cart Operations | 2 | `@pytest.mark.cart_management`, `@pytest.mark.regression` |
| Wishlist Operations | 2 | `@pytest.mark.wishlist_management`, `@pytest.mark.regression` |
| End-to-End | 1 | `@pytest.mark.integration`, `@pytest.mark.e2e` |
| **Total** | **10** | Various markers |

---

## 📋 Test Structure & Organization

### Test File Anatomy

Every test file follows this structure:

```python
# 1. Imports section
from page_objects.module_name import ClassName
from utilities.logger import Loggen
from utilities.read_config import ReadConfig
import allure, pytest

# 2. Test class definition
class TestSomething:
    # 2a. Class variables (fixtures, config, logger)
    title = ReadConfig.page_title()
    log = Loggen.log_generator()
    
    # 2b. Test methods with decorators
    @allure.epic('Credkart Project')
    @allure.feature('Feature Name')
    @allure.story('Story Description')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Test Title')
    @allure.description('Detailed test description')
    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_something(self, setup):
        # 2c. Arrange: Initialize driver and page object
        self.driver = setup
        self.page_obj = ClassName(self.driver)
        
        # 2d. Act: Perform actions
        self.page_obj.action_method()
        
        # 2e. Assert: Verify results
        assert expected == actual
        
        # 2f. Cleanup (automatic via fixtures)
```

---

## ⚙️ Configuration Guide

### config.ini Structure

Located at: `configurations/config.ini`

```ini
# [Page Details] - Application URLs
[Page Details]
base_url = https://automation.credence.in/shop
page_title = Credkart

# [Login Page] - Login credentials
[Login Page]
username = admin_user
password = admin_pass
expected_message = Login Successful

# [Add Item] - Shopping cart messages
[Add Item]
add_item_message = Item Added to Cart
continue_shopping = Continue Shopping
item_added_message = Product successfully added

# [Billing Shipping address] - Address information
[Billing Shipping address]
first_name = John
last_name = Doe
street_address = 123 Main Street
city = Springfield
state = Illinois
postal_code = 62701
country = United States

# [Payment] - Payment details
[Payment]
cardholder_name = John Doe
card_type = VISA
expiry_month = 12
expiry_year = 2025

# [Card Number] - Store card in parts (PCI compliance)
[Card Number]
card_part1 = 4111
card_part2 = 1111
card_part3 = 1111
card_part4 = 1111
```

### Reading Configuration in Tests

```python
from utilities.read_config import ReadConfig

# Method 1: Direct access
username = ReadConfig.user_name()  # From [Login Page] section
password = ReadConfig.password()   # From [Login Page] section

# Method 2: Using config sections
config = ReadConfig()
title = config.page_title()
```

---

## 🧪 Test Execution Guide

### Basic Execution

```bash
# Run all tests (headless - fastest)
pytest testcases/ -v

# Run specific test file
pytest testcases/test_login.py -v

# Run specific test class
pytest testcases/test_login.py::TestLogin -v

# Run specific test method
pytest testcases/test_login.py::TestLogin::test_login_positive -v
```

### Browser Selection

```bash
# Run with visible Chrome browser
pytest testcases/ -v --browser chrome

# Run with visible Firefox browser
pytest testcases/ -v --browser firefox

# Run in headless mode (default)
pytest testcases/ -v --browser headless
```

### Test Filtering

```bash
# Run only smoke tests
pytest testcases/ -v -m smoke

# Run only regression tests
pytest testcases/ -v -m regression

# Run sanity OR smoke tests
pytest testcases/ -v -m "sanity or smoke"

# Exclude slow tests
pytest testcases/ -v -m "not slow"

# Run tests by order
pytest testcases/ -v --order asc   # Ascending order
pytest testcases/ -v --order desc  # Descending order
```

### Output & Display Options

```bash
# Verbose output
pytest testcases/ -v

# Very verbose (show all details)
pytest testcases/ -vv

# Show print statements
pytest testcases/ -v -s

# Stop on first failure
pytest testcases/ -v -x

# Stop after N failures
pytest testcases/ -v --maxfail=3

# Show slowest N tests
pytest testcases/ -v --durations=10
```

### Generate Reports

```bash
# HTML Report
pytest testcases/ -v --html=html_reports/report.html --self-contained-html

# Allure Report (requires allure CLI)
pytest testcases/ -v --alluredir=allure_reports

# JUnit XML Report
pytest testcases/ -v --junit=xml=junit_reports/report.xml

# Combined reports
pytest testcases/ -v \
  --html=html_reports/report.html \
  --alluredir=allure_reports \
  --junit=xml=junit_reports/report.xml
```

---

## 📊 Data-Driven Testing

### Excel-Based Data-Driven Tests

#### File Location
`test_data/Credkart_Login_Data.xlsx`

#### File Structure
```
Row 1: Headers      | Username | Password | Expected Result
Row 2: User 1       | admin    | pass123  | Login Successful
Row 3: User 2       | user123  | userpass | Login Successful
Row 4: Invalid User | invalid  | invalid  | Invalid credentials
```

#### Test Implementation

```python
from utilities.excelutils import ExcelUtils

class TestLoginDDT:
    def test_login_ddt(self, setup):
        # Read Excel file
        excel = ExcelUtils("test_data/Credkart_Login_Data.xlsx")
        rows = excel.total_rows()
        
        # Iterate through each row
        for row in range(1, rows):
            username = excel.read_data(row, 1)
            password = excel.read_data(row, 2)
            
            # Perform test
            page_obj.login(username, password)
            
            # Verify result
            if success:
                excel.green_color(row, 3)  # Mark as PASS
            else:
                excel.red_color(row, 3)    # Mark as FAIL
```

### Fixture-Based Parameterized Tests

#### Implementation in conftest.py

```python
@pytest.fixture(params=[
    {"username": "admin", "password": "pass123"},
    {"username": "user123", "password": "userpass"},
    {"username": "invalid", "password": "invalid"}
])
def data_for_login(request):
    return request.param
```

#### Using in Test

```python
def test_login_param(self, setup, data_for_login):
    username = data_for_login["username"]
    password = data_for_login["password"]
    
    # Perform login test
    page_obj.login(username, password)
```

---

## 📝 Logging & Debugging

### Logger Usage

```python
from utilities.logger import Loggen

class TestSomething:
    log = Loggen.log_generator()
    
    def test_example(self, setup):
        self.log.info("Test started")           # Information
        self.log.debug("Debug information")     # Detail info
        self.log.warning("Warning message")     # Warning
        self.log.error("Error occurred")        # Error
        self.log.critical("Critical issue")     # Critical
```

### Log Output

```
2026-05-01 14:23:45,123 - TestSomething - INFO - ========== Test Session Started. ==========
2026-05-01 14:23:45,456 - TestSomething - INFO - Driver Setup Successful.
2026-05-01 14:23:46,789 - TestSomething - INFO - Navigated to login page
2026-05-01 14:23:47,012 - TestSomething - INFO - Entered username: admin
2026-05-01 14:23:47,234 - TestSomething - INFO - Entered password: ****
2026-05-01 14:23:47,567 - TestSomething - INFO - Clicked login button
2026-05-01 14:23:48,890 - TestSomething - INFO - Login successful
2026-05-01 14:23:49,123 - TestSomething - INFO - Screenshot captured
2026-05-01 14:23:49,456 - TestSomething - INFO - ========== Test Session Finished. ==========
```

### Accessing Logs

```bash
# View last 50 lines
tail -50 logs/credkart_logs.log

# Search for errors in logs
grep ERROR logs/credkart_logs.log

# Search for specific test
grep "test_login" logs/credkart_logs.log

# Full log file
cat logs/credkart_logs.log
```

---

## 📊 Allure Reporting

### Allure Decorators Used

```python
import allure

@allure.epic('Credkart Project')          # High-level grouping
@allure.feature('User Management')        # Feature grouping
@allure.story('Login Functionality')      # Story description
@allure.title('Login with Valid Credentials')  # Test title
@allure.description('Test login with valid credentials')  # Description
@allure.severity(allure.severity_level.CRITICAL)  # Severity
@allure.label('owner', 'ganesh_sateliwar')      # Custom labels
@allure.link('https://example.com')             # Link to documentation
@allure.step('Step description')                # Step in execution
```

### Generate Allure Report

```bash
# Step 1: Run tests with Allure reporting
pytest testcases/ -v --alluredir=allure_reports

# Step 2: Serve interactive report
allure serve allure_reports/

# Step 3: Browser opens with interactive dashboard
# - View pass/fail statistics
# - Explore tests by epic/feature/story
# - Check severity levels
# - View execution history
```

### Report Structure

```
EPIC: Credkart Project
├── FEATURE: User Management
│   ├── STORY: Login
│   │   ├── TEST: Login - Valid Credentials [PASSED]
│   │   ├── TEST: Login - Invalid Password [FAILED]
│   │   └── TEST: Login - Locked Account [SKIPPED]
│   └── STORY: Registration
│       ├── TEST: Register - Valid Data [PASSED]
│       └── TEST: Register - Duplicate Email [FAILED]
├── FEATURE: Shopping
│   ├── STORY: Cart Management
│   │   ├── TEST: Add Item to Cart [PASSED]
│   │   └── TEST: Empty Cart [PASSED]
│   └── STORY: Wishlist
│       ├── TEST: Add to Wishlist [PASSED]
│       └── TEST: Remove from Wishlist [PASSED]
└── FEATURE: Checkout
    ├── STORY: Payment
    │   └── TEST: Process Payment [PASSED]
    └── STORY: Order Confirmation
        └── TEST: Verify Order Placed [PASSED]
```

---

## 🔧 Pytest Plugins & Features

### Installed Plugins

| Plugin | Version | Purpose |
|--------|---------|---------|
| pytest-order | 1.3.0 | Enforce test execution order |
| pytest-dependency | 0.6.1 | Declare test dependencies |
| pytest-html | 4.1.1 | HTML report generation |
| pytest-xdist | 3.8.0 | Parallel test execution |
| allure-pytest | 2.14.3 | Allure report integration |
| pytest-metadata | 3.1.1 | Test metadata collection |

### pytest-order Usage

```python
@pytest.mark.order(1)   # Run first
def test_first():
    pass

@pytest.mark.order(2)   # Run second
def test_second():
    pass

@pytest.mark.order(-1)  # Run last
def test_last():
    pass
```

Run in specific order:
```bash
pytest testcases/ -v  # Respects @pytest.mark.order
```

### pytest-dependency Usage

```python
@pytest.mark.dependency()
def test_login():
    pass

@pytest.mark.dependency(depends=["test_login"])
def test_add_to_cart():
    # Only runs if test_login passed
    pass
```

---

## 🔄 CI/CD Integration

### Jenkins Pipeline

Located at: `Jenkinsfile`

```groovy
pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'source venv/bin/activate && pytest testcases/ -v --alluredir=allure_reports'
            }
        }
        
        stage('Report') {
            steps {
                // Publish Allure report
                publishHTML([reportDir: 'allure_html', reportFiles: 'index.html'])
            }
        }
    }
    
    post {
        always {
            // Archive test results
            junit 'test_results.xml'
            archiveArtifacts artifacts: 'logs/*.log'
        }
    }
}
```

### GitHub Actions Example

```yaml
name: CredKart Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10']
    
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests
        run: |
          pytest testcases/ -v --alluredir=allure_reports
      
      - name: Upload Allure results
        if: always()
        uses: actions/upload-artifact@v2
        with:
          name: allure-results
          path: allure_reports/
```

---

## 🖥️ Page Object Model Guide

### Page Object Template

```python
"""
Module: page_objects/example_page.py
Description: Example page object showing POM best practices.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Loggen
import allure

class ExamplePage:
    """
    Page Object for Example Page
    
    This class encapsulates all interactions with the example page,
    including element selection and user actions.
    """
    
    # ==================== LOCATORS ====================
    # All XPath/CSS selectors are defined here for easy maintenance
    login_button_xpath = "//button[@id='login']"
    email_input_id = "email_field"
    password_input_css = "input[type='password']"
    
    # ==================== CONSTRUCTOR ====================
    def __init__(self, driver):
        """Initialize page object with WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Loggen.log_generator()
    
    # ==================== ACTIONS ====================
    @allure.step("Entering email: {email}")
    def enter_email(self, email):
        """
        Enter email in email field.
        
        Args:
            email (str): Email address to enter
        
        Returns:
            None
        """
        try:
            email_element = self.wait.until(
                EC.presence_of_element_located((By.ID, self.email_input_id))
            )
            email_element.clear()
            email_element.send_keys(email)
            self.log.info(f"Email entered: {email}")
        except Exception as e:
            self.log.error(f"Failed to enter email: {str(e)}")
            raise
    
    @allure.step("Clicking login button")
    def click_login(self):
        """Click login button."""
        try:
            login_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
            )
            login_btn.click()
            self.log.info("Login button clicked")
        except Exception as e:
            self.log.error(f"Failed to click login: {str(e)}")
            raise
    
    # ==================== VERIFICATIONS ====================
    def is_login_successful(self):
        """Check if login was successful."""
        try:
            dashboard = self.wait.until(
                EC.presence_of_element_located((By.ID, "dashboard"))
            )
            self.log.info("Login successful - dashboard visible")
            return True
        except:
            self.log.info("Login failed - dashboard not visible")
            return False
```

### POM Best Practices

✅ **DO:**
- Group related selectors together
- Use descriptive naming for methods
- Add docstrings to every method
- Use explicit waits
- Log all significant actions
- Return relevant data from methods

❌ **DON'T:**
- Hardcode selectors in test files
- Mix multiple concerns in one method
- Use implicit waits only
- Have methods with multiple return types
- Skip error handling

---

## ✨ Best Practices

### 1. Test Independence
- Each test should be runnable independently
- Don't share state between tests
- Clean up after each test

### 2. Clear Assertions
```python
# ✅ GOOD - Clear and specific
assert login_page.is_welcome_message_displayed(), \
    "Welcome message not displayed after login"

# ❌ BAD - Vague assertion
assert True
```

### 3. Meaningful Test Names
```python
# ✅ GOOD - Describes what, given what, expects what
def test_login_with_valid_credentials_should_display_dashboard(self):
    pass

# ❌ BAD - Unclear intent
def test_login(self):
    pass
```

### 4. Comprehensive Logging
```python
# ✅ GOOD - Logs every step
self.log.info("Step 1: Navigating to login page")
page_obj.navigate()
self.log.info("Step 2: Entering credentials")
page_obj.enter_credentials()
self.log.info("Step 3: Verifying login success")
assert page_obj.is_logged_in()

# ❌ BAD - No logging
page_obj.navigate()
page_obj.enter_credentials()
assert page_obj.is_logged_in()
```

### 5. Use AAA Pattern
```python
# Arrange - Set up test data and objects
user_data = {"username": "admin", "password": "pass"}
login_page = LoginPage(driver)

# Act - Perform actions
login_page.login(user_data["username"], user_data["password"])

# Assert - Verify results
assert login_page.is_logged_in()
```

---

## 🐛 Troubleshooting

### Issue: Tests Not Discovered

**Problem:** Pytest shows "No tests found"

**Solution:**
```bash
# Verify test file naming (must start with test_)
ls testcases/test_*.py

# Verify test class naming (must start with Test)
grep "class Test" testcases/test_*.py

# Verify test method naming (must start with test_)
grep "def test_" testcases/test_*.py

# Run with verbose discovery
pytest testcases/ --collect-only
```

### Issue: ChromeDriver Version Mismatch

**Problem:** "ChromeDriver version doesn't match Chrome version"

**Solution:**
```bash
# webdriver-manager auto-manages drivers
# Simply upgrade it
pip install --upgrade webdriver-manager

# Clear cached drivers (if needed)
rm -rf ~/.wdm  # macOS/Linux
rmdir %USERPROFILE%\.wdm  # Windows
```

### Issue: Fixture Not Found

**Problem:** "fixture 'setup' not found"

**Solution:**
```bash
# Verify conftest.py is in testcases/ directory
ls testcases/conftest.py

# Verify fixture is defined
grep "def setup" testcases/conftest.py

# Check fixture scope
grep -A2 "@pytest.fixture" testcases/conftest.py
```

### Issue: Configuration Not Read

**Problem:** "KeyError: 'Login Page'" when reading config

**Solution:**
```bash
# Verify config.ini exists and is readable
cat configurations/config.ini

# Verify section names match (case-sensitive)
grep "\[Login Page\]" configurations/config.ini

# Check for typos in method names
grep "def page_title" utilities/read_config.py
```

### Issue: Logs Not Generated

**Problem:** logs/credkart_logs.log is empty or missing

**Solution:**
```bash
# Create logs directory manually
mkdir -p logs

# Verify write permissions
touch logs/test.log
rm logs/test.log

# Check logger initialization in conftest.py
grep "Loggen" testcases/conftest.py
```

### Issue: Screenshots Not Captured

**Problem:** screenshots/ directory is empty after test failure

**Solution:**
```bash
# Create screenshots directory
mkdir -p screenshots

# Verify screenshot method is called
grep "screenshot" page_objects/*.py

# Check method implementation
grep -A5 "def screenshot" page_objects/*.py
```

---

## ❓ FAQ

### Q: How do I run a single test?
```bash
pytest testcases/test_login.py::TestLogin::test_login_positive -v
```

### Q: How do I run tests in parallel?
```bash
pytest testcases/ -v -n 4  # Run 4 tests in parallel
```

### Q: How do I skip a flaky test temporarily?
```python
@pytest.mark.skip(reason="Flaky test - waiting for fix")
def test_flaky():
    pass
```

### Q: How do I increase the default wait time?
```python
# In conftest.py
wait = WebDriverWait(driver, 30)  # 30 seconds instead of 10
```

### Q: How do I run tests on a specific environment?
```bash
# Create environment-specific config
# configurations/config_staging.ini
# Then read it in conftest.py based on environment variable
```

### Q: How do I generate reports in CI/CD?
```bash
# In CI/CD pipeline
pytest testcases/ -v \
    --html=html_reports/report.html \
    --alluredir=allure_reports \
    --junit=xml=junit_reports/report.xml
```

### Q: How do I add a new test to the framework?
See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

### Q: How do I follow coding standards?
See [STYLE_GUIDE.md](STYLE_GUIDE.md) for naming conventions and best practices.

---

## 📚 Additional Resources

- 🌐 [Test Application](https://automation.credence.in/shop)
- 📖 [Selenium Documentation](https://www.selenium.dev/documentation/)
- 🧪 [Pytest Documentation](https://docs.pytest.org/)
- 📊 [Allure Reporting](https://docs.qameta.io/allure/)
- 🎯 [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)

---

**Version:** 2.0 | **Last Updated:** May 1, 2026 | **Status:** ✅ Complete


