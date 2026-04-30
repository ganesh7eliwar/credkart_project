# 🛒 CredKart Project - Automated E-Commerce Testing Framework

> **Professional-Grade Test Automation Framework for E-Commerce Applications**  
> Built with Python, Selenium, Pytest, and Allure | Production-Ready | CI/CD Integrated

---

## 📋 Quick Navigation

- 🚀 **[Quick Start](#quick-start)** - Get started in 5 minutes
- 📚 **[Comprehensive Guide](#comprehensive-guide)** - Detailed documentation
- 📊 **[Test Execution](#test-execution)** - Run tests with various options
- 📈 **[Allure Reporting](#allure-reporting)** - Advanced test reports
- 🐛 **[Troubleshooting](#troubleshooting)** - Common issues & solutions

---

## 🎯 Project Overview

The **CredKart Project** is a robust, scalable, and extensible automated testing framework specifically designed for e-commerce web applications. It implements industry best practices including **Page Object Model (POM)**, **Data-Driven Testing (DDT)**, and **Behavior-Driven Development (BDD)** principles.

### ✨ Key Highlights

✅ **11 Comprehensive Tests** - Complete coverage of e-commerce workflows  
✅ **Page Object Model** - Modular, maintainable, and scalable architecture  
✅ **Data-Driven Testing** - Excel-based and pytest fixture parameterization  
✅ **Professional Reporting** - Allure and HTML reports with detailed metrics  
✅ **Rich Logging** - Introspection-based logging with complete traceability  
✅ **CI/CD Ready** - Jenkinsfile and GitHub Actions support  
✅ **Multiple Browsers** - Chrome, Firefox, Headless modes  
✅ **Screenshot Capture** - Automatic captures on pass/fail for debugging  

### 📊 Test Coverage

| Test Category | Count | Markers |
|---|---|---|
| **Sanity/Smoke Tests** | 2 | `@smoke`, `@sanity` |
| **Authentication Tests** | 4 | `@user_management`, `@regression` |
| **Shopping Cart Tests** | 2 | `@cart_management`, `@regression` |
| **Wishlist Tests** | 2 | `@wishlist_management`, `@regression` |
| **End-to-End Tests** | 1 | `@integration`, `@checkout` |
| **Data-Driven Tests** | 2 | `@ddt`, `@parametrize` |
| **Total** | **11** | All markers enabled |

---

## 🚀 Quick Start

### 1️⃣ Installation (2 minutes)

```bash
# Clone repository
git clone https://github.com/ganesh7eliwar/credkart_project.git
cd CredKart_Project_2025

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Create logs directory
mkdir logs
```

### 2️⃣ Run Tests (30 seconds)

```bash
# Run all tests (headless - fastest)
pytest testcases/ -v

# Run with visible Chrome browser
pytest testcases/ -v --browser chrome

# Run only smoke tests
pytest testcases/ -v -m smoke

# Generate Allure report
pytest testcases/ -v --alluredir=allure_reports
allure serve allure_reports/
```

---

## 📚 Comprehensive Guide

For **detailed documentation** covering:
- Complete project structure
- Installation & setup (step-by-step)
- All test execution options  
- Logging & debugging
- Allure reporting (advanced)
- Pytest plugins & markers
- CI/CD integration
- Best practices
- Troubleshooting guide

👉 **[See README_COMPREHENSIVE.md](README_COMPREHENSIVE.md)**

---

## 🛠️ Technology Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Core automation language |
| Selenium WebDriver | 4.34.2 | Browser automation |
| Pytest | 8.4.1 | Test runner & framework |
| Allure Pytest | 2.14.3 | Advanced reporting |
| pytest-order | 1.3.0 | Test execution control |
| openpyxl | 3.1.5 | Excel data handling |
| webdriver-manager | 4.0.2 | Automatic driver management |

---

## 📁 Project Structure

```
CredKart_Project_2025/
├── testcases/                    # Test files (11 comprehensive tests)
│   ├── conftest.py              # Pytest fixtures & configuration
│   ├── test_url_check.py        # Sanity check
│   ├── test_register.py         # User registration
│   ├── test_login.py            # Login with valid credentials
│   ├── test_login_ddt.py        # Data-driven (Excel)
│   ├── test_login_param.py      # Parameterized (fixtures)
│   ├── test_add_item_to_cart.py # Cart management
│   ├── test_empty_cart.py       # Empty cart
│   ├── test_add_item_to_wishlist.py  # Wishlist
│   ├── test_empty_wishlist.py   # Empty wishlist
│   └── test_end_to_end.py       # Complete purchase flow
│
├── page_objects/                 # Page Object Model classes
│   ├── login_page.py            # Login interactions
│   ├── register_page.py         # Registration form
│   ├── add_item_to_cart.py      # Shopping cart
│   ├── checkout.py              # Checkout & payment
│   └── ...                       # Other page classes
│
├── utilities/                    # Helper utilities
│   ├── logger.py                # Introspection-based logging
│   ├── read_config.py           # Config file reader
│   ├── generator.py             # Test data generation
│   └── excelutils.py            # Excel operations
│
├── configurations/               # Test configuration
│   └── config.ini               # URL, credentials, test data
│
├── test_data/                    # External test data
│   ├── user_details.json        # Current user
│   ├── all_user_details.json    # Historical records
│   └── Credkart_Login_Data.xlsx # DDT credentials
│
├── logs/                         # Test execution logs
│   └── credkart_logs.log        # Consolidated logs
│
├── screenshots/                  # Pass/fail screenshots
├── html_reports/                 # HTML test reports
├── allure_reports/               # Allure report data
│
├── README.md                     # This file (overview)
├── README_COMPREHENSIVE.md       # Detailed guide
├── requirements.txt              # Python dependencies
├── pytest.ini                    # Pytest configuration
├── Jenkinsfile                   # CI/CD pipeline
└── LICENSE                       # MIT License
```

---

## ⚡ Test Execution

### Basic Commands

```bash
# Run all tests
pytest testcases/ -v

# Run specific test
pytest testcases/test_login.py -v

# Run by marker
pytest testcases/ -v -m smoke          # Smoke tests only
pytest testcases/ -v -m regression     # All regression tests
pytest testcases/ -v -m "not slow"     # Exclude slow tests

# Run with options
pytest testcases/ -v --browser chrome  # Visible browser
pytest testcases/ -v -s                # Show print statements
pytest testcases/ -v -x                # Stop on first failure
```

### With Reporting

```bash
# HTML Report
pytest testcases/ -v --html=html_reports/report.html

# Allure Report (interactive)
pytest testcases/ -v --alluredir=allure_reports
allure serve allure_reports/

# Combined
pytest testcases/ -v \
  --html=html_reports/report.html \
  --alluredir=allure_reports \
  --browser chrome
```

---

## 📊 Allure Reporting

### Generate & View Report

```bash
# Run tests with Allure data
pytest testcases/ -v --alluredir=allure_reports

# View interactive report (requires Java/Allure CLI)
allure serve allure_reports/

# Or generate static HTML
allure generate allure_reports/ -o allure_html
```

### Report Features
- 📈 Visual test metrics & pass/fail rates
- 📖 Organized by Epic/Feature/Story
- 🎯 Severity levels (Critical, Normal, Minor)
- 📸 Screenshots & attachments
- 📝 Step-by-step execution logs
- 💾 Historical trends

---

## 🏷️ Pytest Markers

### Available Markers

```bash
@pytest.mark.smoke           # Quick sanity checks
@pytest.mark.sanity          # Basic functional tests
@pytest.mark.regression      # Full test suite
@pytest.mark.integration     # End-to-end flows
@pytest.mark.user_management # Auth & profile tests
@pytest.mark.cart_management # Shopping cart tests
@pytest.mark.wishlist_management  # Wishlist tests
@pytest.mark.checkout        # Checkout flow tests
@pytest.mark.ddt            # Data-driven Excel tests
@pytest.mark.parametrize    # Parameterized tests
```

### Run by Marker

```bash
pytest testcases/ -v -m smoke              # Only smoke tests
pytest testcases/ -v -m "sanity or smoke"  # Multiple markers
pytest testcases/ -v -m "not slow"         # Exclude marker
```

---

## 📊 Logging & Debugging

### Log Location
- **File**: `./logs/credkart_logs.log`
- **Format**: Centralized (all tests write to one file)
- **Access**: Open with any text editor

### Debugging Failed Tests

```bash
# View logs
tail -100 logs/credkart_logs.log

# Run with verbose output
pytest testcases/test_login.py -v -s --tb=long

# View screenshots
ls -lat screenshots/

# Check Allure report for detailed steps
allure serve allure_reports/
```

---

## 🔄 CI/CD Integration

### Jenkins Pipeline

```bash
# A Jenkinsfile is included for CI/CD automation
# Configure in Jenkins:
# 1. New Pipeline job
# 2. GitHub repository URL
# 3. Jenkinsfile path
# 4. Set build triggers
# 5. Run build
```

### GitHub Actions / GitLab CI

See `README_COMPREHENSIVE.md` for example workflows.

---

## ✨ Best Practices

### ✅ Page Object Model
- Encapsulate locators and methods in page classes
- Avoid hardcoding XPath in tests
- Reusable across multiple tests

### ✅ Data-Driven Testing
- Use external data sources (Excel, JSON, fixtures)
- Avoid hardcoding test data
- Enable multiple test scenarios

### ✅ Logging
- Log every significant action
- Use appropriate log levels (INFO, ERROR, etc.)
- Review logs for debugging failed tests

### ✅ Test Independence
- Each test can run standalone
- Don't rely on test execution order (though some tests depend on data)
- Clean up after tests

### ✅ Assertions
- Use clear, specific assertions
- Include meaningful error messages
- Assert one thing per assert (ideally)

---

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| ChromeDriver version mismatch | `pip install --upgrade webdriver-manager` (auto-managed) |
| Logs directory not found | `mkdir logs` |
| Tests not discovered | Verify `test_*.py` naming pattern |
| Fixture not found | Ensure `conftest.py` in `testcases/` directory |
| Allure not generating | Install: `brew install allure` or `apt-get install allure2` |
| Excel file not readable | Ensure openpyxl installed: `pip install openpyxl` |

For detailed troubleshooting:
👉 **[See README_COMPREHENSIVE.md - Troubleshooting section](README_COMPREHENSIVE.md#-troubleshooting)**

---

## 📚 Documentation Files

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Overview & quick reference (this file) |
| [README_COMPREHENSIVE.md](README_COMPREHENSIVE.md) | Detailed documentation & guides |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines |
| [STYLE_GUIDE.md](STYLE_GUIDE.md) | Coding standards & conventions |
| [IMPROVEMENTS_SUMMARY.md](IMPROVEMENTS_SUMMARY.md) | Recent enhancements & changes |
| [pytest.ini](pytest.ini) | Pytest configuration with markers |
| [Jenkinsfile](Jenkinsfile) | CI/CD pipeline configuration |

---

## 🤝 Contributing

Found a bug or want to add a feature?

1. 📝 Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. 🔄 Follow [STYLE_GUIDE.md](STYLE_GUIDE.md) for code standards
3. 📤 Create a Pull Request with clear description

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file.

---

## 🔗 Resources & Links

- 🌐 [Test Application](https://automation.credence.in/shop)
- 📚 [Selenium Documentation](https://www.selenium.dev/documentation/)
- 🧪 [Pytest Documentation](https://docs.pytest.org/)
- 📊 [Allure Reporting](https://docs.qameta.io/allure/)
- 💻 [GitHub Repository](https://github.com/ganesh7eliwar/credkart_project)

---

## 👥 Authors

**Ganesh Sateliwar** - QA Automation Architect  
📧 ganesh.sateliwar@example.com  
🐙 [@ganesh7eliwar](https://github.com/ganesh7eliwar)

---

## 📞 Support

- 📧 Email: ganesh.sateliwar@example.com
- 🐙 GitHub Issues: [Create an issue](https://github.com/ganesh7eliwar/credkart_project/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/ganesh7eliwar/credkart_project/discussions)

---

**✨ Happy Testing! 🚀**

*Framework Version: 2.0 (Enhanced Documentation & Organization)*  
*Last Updated: April 30, 2026*  
*Status: ✅ Production Ready*
