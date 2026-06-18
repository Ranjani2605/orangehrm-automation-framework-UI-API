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

    def wait_for_page_load(self):
        self.page.wait_for_load_state("domcontentloaded")

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

    def expect_visible(self, selector:str):
        expect(self.page.locator(selector)).to_be_visible()

    def expect_hidden(self, selector:str):
        expect(self.page.locator(selector)).to_be_hidden()

    def expect_text_visible(self, text: str):
        expect(self.page.get_by_text(text)).to_be_visible()

    def select_dropdown_options(self, dropdown_selector:str, option_selector:str):
        self.safe_click(dropdown_selector)
        self.safe_click(option_selector)

    def press_key(self, key:str):
        self.page.keyboard.press(key)

    def verify_url_contains(self, expected_url_part:str):
        assert expected_url_part in self.page.url, (
            f"Expected URL to contain '{expected_url_part}', actual URL: {self.page.url}"
        )

    def verify_title_contains(self, expected_title: str):
        actual_title = self.page.title()
        assert expected_title in actual_title, (
            f"Expected title to contain '{expected_title}', actual title: {actual_title}"
        )


    def verify_no_server_error_visible(self):
        server_errors = [
            "500",
            "Internal Server Error",
            "Application Error",
            "Server Error"
        ]
        body_text = self.page.locator("body").inner_text()

        for error in server_errors:
            assert error not in body_text,f"Unexpected server error visible: {error}"

