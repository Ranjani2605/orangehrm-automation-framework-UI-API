import re
from asyncio import wait_for

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from src.core.config_manager import ConfigManager
from utils.logger import get_logger


class BasePage:

    def __init__(self, page:Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def goto(self, url: str):
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)
        self.wait_for_page_load()

    def locator(self, selector: str):
        return self.page.locator(selector)

    def click(self, selector: str):
        self.logger.info(f"Clicking: {selector}")
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        element.click()

    def safe_click(self, selector:str):
        self.logger.info(f"Safe clicking: {selector}")
        element = self.page.locator(selector)
        element.wait_for(state="visible")
        element.scroll_into_view_if_needed()
        element.click()

    def fill(self, selector : str, value:str):
        self.logger.info(f"Filling: {selector}")
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        element.fill(value)

    def clear_and_fill(self, selector: str, value:str):
        self.logger.info(f"Clearing and filling : {selector}")
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        element.clear()
        element.fill(value)

    def get_text(self, selector:str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector, timeout: int = 5000) -> bool:
        try:
            selector.wait_for(state="visible", timeout=timeout)
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
