# OrangeHRM Automation Framework

Enterprise-style automation framework for OrangeHRM using Python, Playwright, Pytest, Page object Model, API testing, DB validation, Allure reporting and GitHub Actions.

### Tech Stack

-Python
-Playwright
-Pytest
-Page Object Model
-Requests
-PyMySQL
-Allure
-GitHub Actions
-Ruff
-Bandit
-pip-audit

## Project Structure
```text
config/                  Environment config
data/                    Test data
src/pages/               Page Object classes
src/locators/            Reusable locators
src/api/                 API client layer
src/db/                  DB client layer
tests/ui/                UI test
tests/api/               API test
tests/db/                DB tests
tests/e2e/               End-to-end tests
utils/                   Logger and file readers
reporting/               Allure helpers