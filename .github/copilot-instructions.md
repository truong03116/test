# Copilot instructions — automation

Purpose: help AI coding agents quickly understand and edit this Selenium + pytest test repository.

Quick overview
- Structure: `pages/` contains Page Object classes; `tests/` contains pytest tests; `utils/` holds helpers (currently empty); `pytest.ini` sets `pythonpath=.`.
- Runtime: tests use Selenium WebDriver (Chrome) created by the `driver` fixture in `tests/conftest.py`.

How tests run (explicit)
- Requirements: Python, `selenium` package, Chrome browser and a matching `chromedriver` available on PATH.
- Run tests from repository root: `pytest -q` (pytest.ini already adds project root to `PYTHONPATH`).

Important project-specific conventions
- Fixture: always use the `driver` pytest fixture defined in `tests/conftest.py` (scope=function). Do not create separate WebDriver instances in tests or helpers unless adding a new fixture.
- Page objects: placed in `pages/`. Two styles coexist:
  - Inline locator usage and direct `find_element` calls (see `pages/login_page.py`).
  - Locator tuples with `self.loc = (By.NAME, "...")` and `find_element(*self.loc)` (see `pages/login_page_ngay3.py`).
  Prefer the tuple style for new page methods (it is easier to reuse and mock).
- Mixed patterns: many tests use direct `driver.find_element(...)` (see `tests/test_login.py`) while others call page object methods. When modifying tests, preserve existing behavior; prefer refactoring to `pages/*` POMs only when you update all affected assertions/selectors.

Selectors and assertions
- Tests and pages use CSS/XPath and expect exact text matches for assertions (e.g., Dashboard header and "Invalid credentials"). Keep string comparisons exact unless intentionally loosening checks.

Test data and external endpoints
- Tests use live demo sites: `https://opensource-demo.orangehrmlive.com/` and `https://www.letskodeit.com/practice`. Avoid changing endpoints in patches unless addressing flakiness with configuration.
- There is a `tests/data.csv` file present but most tests use hard-coded credentials (`Admin` / `admin123`). Check and reuse `data.csv` only if adding data-driven tests.

Configuration and placeholders
- `testsetting.json` and `utils/config_reader.py` are present but empty — do not assume config-driven behavior exists. If adding config support, update `utils/config_reader.py` and keep backward compatibility.

Quick examples for common edits
- Use the `driver` fixture in new tests:

```py
def test_example(driver):
    # driver is provided by tests/conftest.py
    driver.get("https://example.com")
```

- Use Page Object tuple style for new POMs (example based on `pages/login_page_ngay3.py`):

```py
from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.NAME, "username")
    def enter_username(self, username_val):
        self.driver.find_element(*self.username).send_keys(username_val)
```

Notes for AI agents
- Preserve the `driver` fixture lifecycle — it handles browser startup and teardown.
- Avoid adding global sleeps; prefer explicit waits when improving flakiness (but follow existing code style if making minimal fixes).
- When changing selectors, run (or request to run) `pytest -q` because tests interact with live sites and selectors may change upstream.
- If you add dependencies (e.g., `webdriver-manager`), include a short README or update CI config — there is no dependency manifest in the repo.

Key files to inspect when making changes
- `tests/conftest.py` — `driver` fixture and WebDriver setup
- `pages/login_page.py` and `pages/login_page_ngay3.py` — POM examples and locator styles
- `tests/test_login.py` and `tests/test_Practice_Page.py` — canonical test examples showing direct `find_element` usage and POM usage
- `pytest.ini` — `pythonpath` setting

If anything above is unclear or you want the file to contain more examples (e.g., snippets for converting direct-find tests into POM-based tests), tell me which area to expand.
