## CredKart Project - Automated E-commerce Testing Framework

The **CredKart Project** is a robust, scalable, and extensible automated testing framework specifically designed for the CredKart e-commerce web application. This project utilizes the powerful combination of Python (53.9%), HTML (41.2%), and CSS (4.9%) to deliver end-to-end quality assurance through automation.

### 🎯 Project Goals

- **Comprehensive Test Coverage:** Automate functional, regression, smoke, and end-to-end scenarios for critical e-commerce workflows — including user authentication, registration, cart and wishlist management, and checkout.
- **Maintainable Test Suite:** Introduce best practices like Page Object Model (POM), Data-Driven Testing (DDT), and modular design for easy test expansion and long-term maintainability.
- **Rich Reporting:** Offer actionable, visually appealing test reports and logs (Allure, HTML) for both developers and QA teams.
- **Integration-ready:** Designed for CI/CD environments (Jenkinsfile included) and easy adoption of parallelism and advanced reporting.

---

### 🛠️ Technology Summary

- **Python:** Core logic, test scripts, and utilities
- **Selenium WebDriver:** Browser automation for UI validation
- **Pytest:** Test runner with fixture and marker support
- **Allure Reports:** Advanced reporting with test story, epic, and feature labeling
- **openpyxl:** Read and manage Excel-driven test data for DDT
- **HTML & CSS:** Custom reporting and style enhancements
- **Jenkins:** CI/CD pipeline automation

---

### 📦 Main Features

- **Login, Registration, and User Flows:** Automate login with valid/invalid credentials, new user registration, and verification of all key user flows.
- **Shopping Cart and Wishlist:** Add, remove, and validate items in cart and wishlist. Check empty states and user notifications.
- **End-to-End Checkout:** Automate entire purchase flow — from login to cart to payment to order confirmation.
- **Data-Driven & Parameterized Testing:** Fetch test cases and credentials dynamically from Excel sheets or parameter inputs.
- **Modular Page Objects:** Each application page has a dedicated, reusable Python class representing its UI and actions.
- **Powerful Logging & Screenshots:** Every test step is logged; failures/successes trigger automatic screenshots for rapid debugging.
- **Extensive Reporting:** Generate both HTML and Allure reports summarizing test runs with statistics, logs, and screenshots.

---

### 📁 Project Structure Highlights

- `testcases/` – All automated test classes and scripts  
- `page_objects/` – POM implementation (e.g., login, register, cart, wishlist, checkout)  
- `utilities/` – Helpers for logging, Excel read/write, config parsing, data generation, and screenshots  
- `configurations/` – Centralized test config (browser, URL, credentials)  
- `test_data/` – External data sources (e.g., Excel) for data-driven tests  
- `logs/`, `screenshots/`, `html_reports/`, `allure_reports/` – Auto-generated artifacts on each test run  
- `Jenkinsfile` – Pipeline steps for CI execution

---

### ⚡ Example Workflows Automated

- Login with valid/invalid credentials (data-driven)
- New user registration (randomized/parameterized data)
- Add/remove items to/from cart and wishlist
- Validate successful checkout and order confirmation
- URL and page title checks (sanity checks)
- Complete end-to-end scenario: landing -> login -> add to cart -> checkout -> payment -> order

---

### 💡 Why Use This Project?

- **Accelerate Releases:** Fast feedback and early bug detection pre-release
- **Easy Maintenance:** Modular, data-driven design, and abundant logging
- **Professional Reports:** Allure & HTML reporting for all stakeholders
- **Integration Ready:** Works with both local and CI/CD test environments (pip, ChromeDriver, Jenkins support)
- **Future-proof:** Designed for easy future expansion: API/mobile/performance testing, cloud/grid execution, etc.

---

### 🔗 Learn More

- [Project Repository](https://github.com/ganesh7eliwar/credkart_project)
- [Live Application](https://automation.credence.in/shop)
- Owner: [Ganesh Sateliwar](https://github.com/ganesh7eliwar)

---

**CredKart Project** offers a professional-grade foundation for any e-commerce test automation program! 🚀
