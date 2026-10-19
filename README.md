# Python Playwright Automation Framework

A UI test automation framework built with **Python, Playwright, and Pytest**, following the **Page Object Model (POM)** design pattern.

The project automates end-to-end testing of [SauceDemo](https://www.saucedemo.com/), covering authentication, product inventory, shopping cart functionality, and checkout workflows.

The framework includes reusable fixtures, data-driven testing, Allure reporting, and a GitHub Actions CI pipeline with cross-browser execution.

## Tech Stack

- **Python 3.13** — Programming language
- **Playwright** — Browser automation
- **Pytest** — Test execution and fixtures
- **Allure** — Test reporting and failure screenshots
- **GitHub Actions** — Continuous Integration
- **Chromium & Firefox** — Cross-browser testing

## Test Coverage

The framework currently includes **28 automated test cases**, covering:

| Module | Test Scenarios |
|---|---|
| Homepage | Browser title verification |
| Login | Valid credentials, invalid credentials, locked-out users, required field validation |
| Inventory | Product selection, sorting by price and name, cart badge validation |
| Shopping Cart | Adding and removing products, empty cart validation |
| Checkout | Checkout navigation, customer information validation, successful order completion |

Parameterized tests are used to cover multiple scenarios without duplicating test logic.

## Project Structure

```text
python-playwright-automation/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── data/
│   ├── __init__.py
│   ├── sort_options.py
│   └── test_data.py
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   └── test_inventory.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Design

### Page Object Model

Each application page is represented by a dedicated Python class.

Page Objects encapsulate locators and page interactions, keeping test cases readable and maintainable.

### Pytest Fixtures

Reusable fixtures handle browser setup and common test prerequisites, including authenticated sessions.

### Data-Driven Testing

Pytest parameterization is used to execute multiple test scenarios with different inputs.

Enums and centralized test data improve consistency and maintainability.

### Failure Reporting

Allure integrates with Pytest to provide execution steps, test results, and screenshots captured automatically when tests fail.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BenKeidar/python-playwright-automation.git
cd python-playwright-automation
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
python -m playwright install chromium firefox
```

## Running Tests

Run the complete test suite:

```bash
python -m pytest tests/ -v
```

Run tests in Chromium:

```bash
python -m pytest tests/ -v --browser chromium
```

Run tests in Firefox:

```bash
python -m pytest tests/ -v --browser firefox
```

Run a specific test module:

```bash
python -m pytest tests/test_login.py -v
```

## Allure Reporting

Generate Allure results:

```bash
python -m pytest tests/ -v --alluredir=allure-results --clean-alluredir
```

View the report locally (requires Allure CLI):

```bash
allure serve allure-results
```

The framework automatically attaches screenshots to Allure results when a test fails during execution.

## Continuous Integration

GitHub Actions automatically executes the test suite on:

- Push events
- Pull requests
- Manual workflow triggers

The CI pipeline uses a **matrix strategy** to run the test suite independently on Chromium and Firefox.

Each browser executes all 28 tests, resulting in **56 test executions per complete CI run**.

After execution, the pipeline:

1. Uploads Allure results for each browser.
2. Combines the results into a single report.
3. Generates an Allure HTML report.
4. Includes environment information and a link to the GitHub Actions execution.
5. Uploads the HTML report as a downloadable artifact.

### CI Results

**Latest verified execution: 56/56 tests passed across Chromium and Firefox.**

Reports are available as downloadable artifacts from the GitHub Actions workflow runs.

## Key Automation Practices

- Page Object Model for separation of concerns
- Reusable fixtures for test setup
- Parameterized tests for data-driven coverage
- Centralized test data and enums
- Playwright auto-waiting assertions
- Allure steps and failure screenshots
- Cross-browser testing
- Automated CI execution and reporting

## Application Under Test

[**SauceDemo**](https://www.saucedemo.com/) — A sample e-commerce application used for UI automation practice.

## Author

**BenKeidar**

[GitHub Profile](https://github.com/BenKeidar)