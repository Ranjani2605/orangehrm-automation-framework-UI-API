import re

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from src.core.config_manager import ConfigManager


class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.timeout = ConfigManager.get_timeout()

    def open_url(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")


    def click(self, locator):
        expect(locator).to_be_visible(timeout=self.timeout)
        expect(locator).to_be_enabled(timeout=self.timeout)
        locator.click()

    def fill(self, locator, value:str):
        expect(locator).to_be_visible(timeout=self.timeout)
        locator.fill(value)

    def get_text(self, locator) -> str:
        expect(locator).to_be_visible(timeout=self.timeout)
        return locator.inner_text()

    def is_visible(self, locator, timeout: int = 5000) -> bool:
        try:
            locator.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def wait_for_page_load(self):
        self.page.wait_for_load_state("domcontentloaded")

    def wait_for_network_idle(self):
        self.page.wait_for_load_state("networkidle")


    def verify_page_loaded(self, url_part :str, page_title: str):
        expect(self.page).to_have_url(re.compile(f".*{url_part}.*"))
        expect(self.page.locator("h6").filter(has_text=page_title)).to_be_visible(timeout=self.timeout)
