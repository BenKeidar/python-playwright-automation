# Python Playwright Automation Framework

A comprehensive UI test automation framework built with **Python, Playwright, and Pytest**, demonstrating modern test automation practices, reusable architecture, cross-browser testing, visual regression testing, reporting, and continuous integration.

The framework automates end-to-end testing of the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution and fixtures |
| Pillow | Screenshot comparison for visual regression |
| Allure | Test reporting and failure attachments |
| GitHub Actions | Continuous integration |
| Git / GitHub | Version control |

## Key Features

- **Page Object Model (POM)** for maintainable and reusable page interactions.
- **Pytest Fixtures** for test setup, login flows, and reusable test state.
- **Data-Driven Testing** using `pytest.mark.parametrize`.
- **Cross-Browser Testing** with Chromium and Firefox.
- **Visual Regression Testing** with baseline screenshot comparison.
- **Screenshot on Failure** automatically attached to Allure reports.
- **Centralized Test Data** for credentials, products, and checkout information.
- **Enum-Based Sorting Options** for readable product sorting tests.
- **Allure Reporting** with test results, environment information, and CI execution details.
- **GitHub Actions CI/CD** with automated functional and visual test execution.

## Test Coverage

The framework contains **31 unique test cases**, executed across multiple environments.

### Functional Tests — 28 Cases

**Login Tests**
- Successful login with valid credentials.
- Invalid username and password combinations.
- Locked-out user validation.
- Required-field validation.

**Inventory and Cart Tests**
- Adding individual products to the cart.
- Adding multiple products.
- Removing products.
- Verifying cart contents.
- Validating empty-cart behavior.
- Product sorting by name and price.

**Checkout Tests**
- Checkout navigation.
- Customer information entry.
- Required-field validation.
- Complete end-to-end purchase flow.

**Homepage Tests**
- Homepage title verification.

### Visual Regression Tests — 3 Cases

| Page | Validation |
|---|---|
| Login | Compare the login page against a baseline screenshot |
| Inventory | Compare the product listing page against a baseline screenshot |
| Cart | Compare the shopping cart against a baseline screenshot |

Visual tests use Playwright screenshots and Pillow to detect pixel-level differences.

When a difference is detected, the framework saves and attaches the following images to Allure:

1. **Visual Baseline** — the expected screenshot.
2. **Actual Screenshot** — the screenshot from the current test run.
3. **Visual Difference** — the pixels that differ between the images.

The framework also captures an additional screenshot automatically when a test fails.

## Project Structure

```text
python-playwright-automation/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
│
├── data/
│   ├── __init__.py
│   ├── test_data.py
│   └── sort_options.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_visual.py
│
├── utils/
│   ├── __init__.py
│   └── visual_comparison.py
│
├── visual_baselines/
│   ├── login_page.png
│   ├── inventory_page.png
│   └── cart_page.png
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.13
- Git
- Chromium and Firefox (installed through Playwright)
- Allure CLI (optional, for viewing local reports)

### 1. Clone the Repository

```bash
git clone https://github.com/BenKeidar/python-playwright-automation.git
cd python-playwright-automation
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
py -3.13 -m venv .venv
```

### 3. Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```powershell
.\.venv\Scripts\python.exe -m playwright install chromium firefox
```

## Running Tests

All commands below are intended to run from the project root directory using Windows PowerShell.

### Run All Tests with Chromium

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v --browser chromium
```

### Run Functional Tests Only

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v -m "not visual" --browser chromium
```

### Run Visual Regression Tests Only

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v -m visual --browser chromium
```

### Run Tests with Firefox

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v -m "not visual" --browser firefox
```

### Run a Specific Test File

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_login.py -v --browser chromium
```

## Visual Regression Architecture

Visual regression tests use a shared screenshot comparison utility located at:

`utils/visual_comparison.py`

The comparison process follows these steps:

1. Navigate to the page and verify the expected UI is visible.
2. Wait for relevant page content and images to load.
3. Capture an actual screenshot using a consistent viewport.
4. Load the corresponding baseline screenshot.
5. Compare image dimensions and pixel values.
6. Fail the test if a visual difference is detected.
7. Attach the baseline, actual, and difference images to Allure.

Example usage:

```python
compare_screenshots(page, "login_page")
```

Baseline images are stored in `visual_baselines/`.

Generated screenshots and difference images are stored in `test-results/`.

### Visual Testing Considerations

Visual regression tests are sensitive to browser rendering, operating systems, fonts, image loading, and viewport settings.

The committed baseline images were created using **Windows and Chromium**.

The GitHub Actions workflow therefore runs visual regression tests separately on Windows with Chromium, while functional tests run on Ubuntu with Chromium and Firefox.

Baseline images should only be updated after reviewing and approving an intentional UI change.

## Allure Reporting

The framework integrates **Allure** to provide detailed test execution reports.

### Generate Test Results

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v --browser chromium --alluredir=allure-results --clean-alluredir
```

### Open the Allure Report

After installing the Allure CLI:

```powershell
allure serve allure-results
```

Allure reports include:

- Test execution status and duration.
- Test suites and parameterized test cases.
- Screenshots captured on failure.
- Baseline, actual, and difference screenshots for visual failures.
- CI environment information.
- GitHub Actions executor details and links.

## GitHub Actions CI/CD

The project includes an automated GitHub Actions workflow:

`.github/workflows/playwright-tests.yml`

The workflow runs automatically on:

- Push events.
- Pull requests.
- Manual execution using `workflow_dispatch`.

### CI Test Matrix

| Job | Operating System | Browser | Tests |
|---|---|---|---:|
| Functional Tests | Ubuntu Linux | Chromium | 28 |
| Functional Tests | Ubuntu Linux | Firefox | 28 |
| Visual Regression Tests | Windows | Chromium | 3 |
| **Total** | | | **59** |

### CI Workflow

1. Check out the repository.
2. Set up Python 3.13.
3. Install project dependencies.
4. Install the required Playwright browsers.
5. Execute functional and visual test jobs.
6. Upload Allure result artifacts.
7. Merge results from all test jobs.
8. Generate a combined Allure HTML report.
9. Upload the final report as a downloadable artifact.

The workflow also uploads visual test output files when the visual job fails.

### CI Results

**Latest verified project milestone: 59/59 successful test executions**, including all three visual regression tests.

Allure reports are available as downloadable artifacts from GitHub Actions workflow runs.

## Design Principles

The framework follows several software engineering and test automation principles:

- **Separation of Concerns:** Tests describe scenarios while Page Objects handle UI interactions.
- **DRY (Don't Repeat Yourself):** Shared fixtures and utilities minimize duplicated logic.
- **Maintainability:** UI locators and reusable actions are centralized.
- **Readability:** Test methods use descriptive names and business-oriented operations.
- **Reusability:** Common workflows can be shared across multiple test cases.
- **CI Readiness:** Automated execution and reporting are integrated into the development workflow.

## Author

**Ben Keidar**

QA Automation Engineer

[GitHub Profile](https://github.com/BenKeidar)