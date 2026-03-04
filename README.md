# CredKart Project - Automated Testing Suite

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![Pytest](https://img.shields.io/badge/Pytest-7.x-yellow)
![Allure Reports](https://img.shields.io/badge/Allure%20Reports-2.x-brightgreen)

## 📋 Overview

**CredKart Project** is a comprehensive automated testing suite for the CredKart e-commerce platform. This project implements end-to-end test automation using **Selenium WebDriver** with **Pytest** framework, featuring advanced testing patterns including Page Object Model (POM), Data-Driven Testing (DDT), and Parameterized Testing.

The test suite covers critical user workflows including user authentication, registration, shopping cart management, wishlist operations, and complete checkout processes with detailed reporting and logging capabilities.

**Live Application**: [https://automation.credence.in/shop](https://automation.credence.in/shop)

---

## 🚀 Key Features

### Core Testing Capabilities
- ✅ **User Authentication** - Login with valid/invalid credentials
- ✅ **User Registration** - Complete registration workflow with data generation
- ✅ **Shopping Cart Management** - Add, view, and remove items from cart
- ✅ **Wishlist Operations** - Add items to wishlist and manage wishlists
- ✅ **End-to-End Checkout** - Complete purchase flow with payment processing
- ✅ **URL & Page Validation** - Verify page titles and URLs

### Testing Methodologies
- ✅ **Data-Driven Testing (DDT)** - Multiple test data sets from Excel files
- ✅ **Parameterized Testing** - Dynamic test execution with multiple parameters
- ✅ **Page Object Model** - Maintainable and scalable test structure
- ✅ **BDD Integration** - Allure reporting with Epic, Feature, Story labels

### Reporting & Logging
- ✅ **Allure Reports** - Beautiful, detailed HTML test reports
- ✅ **HTML Reports** - Additional HTML test execution reports
- ✅ **Comprehensive Logging** - Detailed logs for every test step
- ✅ **Screenshot Capture** - Automatic screenshots on pass/fail
- ✅ **Jenkins Integration** - CI/CD pipeline support via Jenkinsfile

---

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.x | Programming Language |
| **Selenium** | 4.x | Web Browser Automation |
| **Pytest** | 7.x | Test Framework |
| **Allure** | 2.x | Test Reporting |
| **Openpyxl** | Latest | Excel Data Handling |
| **WebDriverManager** | Latest | Driver Management |

---

## 📂 Project Structure

---

## 📋 Test Case Documentation

### 1. **test_url_check.py** - URL Validation
- **Purpose**: Verify that the application URL loads correctly and page title matches
- **Severity**: CRITICAL
- **Type**: Smoke Test
- **Expected Result**: Page title should match configured title

### 2. **test_login.py** - Basic Login
- **Purpose**: Test login functionality with valid credentials
- **Severity**: NORMAL
- **Type**: Functional Test
- **Precondition**: Valid credentials must be configured
- **Expected Result**: User successfully logs in and dashboard displays

### 3. **test_login_param.py** - Parameterized Login
- **Purpose**: Test login with multiple parameter sets (Pass/Fail scenarios)
- **Severity**: NORMAL
- **Type**: Parameterized Test
- **Scenarios**: Valid credentials (Pass), Invalid credentials (Fail)
- **Expected Result**: Appropriate success/failure behavior for each scenario

### 4. **test_login_ddt.py** - Data-Driven Login
- **Purpose**: Test login with multiple data sets from Excel file
- **Severity**: NORMAL
- **Type**: Data-Driven Test
- **Data Source**: `test_data/Credkart_Login_Data.xlsx`
- **Expected Result**: Login succeeds/fails based on Excel data

### 5. **test_register.py** - User Registration
- **Purpose**: Test new user registration with auto-generated data
- **Severity**: CRITICAL
- **Type**: Sanity Test
- **Data**: Auto-generated email, name, password
- **Expected Result**: New user registered successfully

### 6. **test_add_item.py** - Add to Cart
- **Purpose**: Test adding items to shopping cart
- **Severity**: NORMAL
- **Type**: Functional Test
- **Flow**: Login → Select Item → Add to Cart → Verify confirmation
- **Expected Result**: Item successfully added to cart with confirmation message

### 7. **test_add_item_to_wishlist.py** - Add to Wishlist
- **Purpose**: Test adding items to wishlist
- **Severity**: NORMAL
- **Type**: Functional Test
- **Flow**: Login → Select Item → Add to Wishlist → Verify confirmation
- **Expected Result**: Item successfully added to wishlist

### 8. **test_empty_cart.py** - Remove from Cart
- **Purpose**: Test removing items from shopping cart
- **Severity**: NORMAL
- **Type**: Functional Test
- **Flow**: Login → Add Item → Empty Cart → Verify empty state
- **Expected Result**: Cart successfully emptied with confirmation

### 9. **test_empty_wishlist.py** - Remove from Wishlist
- **Purpose**: Test removing items from wishlist
- **Severity**: NORMAL
- **Type**: Functional Test
- **Flow**: Login → Add to Wishlist → Remove → Verify empty state
- **Expected Result**: Wishlist successfully cleared

### 10. **test_end_to_end.py** - Complete Checkout
- **Purpose**: Test complete purchase workflow from login to order placement
- **Severity**: NORMAL
- **Type**: End-to-End Test
- **Flow**: Login → Add Multiple Items → Checkout → Payment → Order Confirmation
- **Expected Result**: Order successfully placed with confirmation message

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Chrome/Firefox browser installed
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/ganesh7eliwar/credkart_project.git
cd credkart_project
