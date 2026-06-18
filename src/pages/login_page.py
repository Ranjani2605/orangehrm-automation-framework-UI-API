from playwright.sync_api import Page, expect

from src.core.constants import ErrorMessages
from src.pages.base_page import BasePage
from src.core.config_manager import ConfigManager


class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)




    def open(self):
        self.open_url(ConfigManager.get_base_url())

    def enter_username(self, username:str):
        self.fill(self.username_input, username)

    def enter_password(self, password:str):
        self.fill(self.password_input, password)

    def click_login_button(self):
        self.click(self.login_button)

    def login(self, username:str, password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()


    def login_with_default_user(self):
        self.login(
            ConfigManager.get_username(),
            ConfigManager.get_password()
        )

    def verify_invalid_credentials_message(self):
        expect(self.invalid_credentials_alert).to_contain_text(
            ErrorMessages.INVALID_CREDENTIALS,
            timeout=self.timeout
        )

    def verify_required_error_displayed(self):
        expect(self.required_errors.first).to_contain_text(
            ErrorMessages.REQUIRED,
            timeout=self.timeout
        )

    def get_required_error_count(self) -> int:
        return self.required_errors.count()

    def verify_login_page_displayed(self):
        expect(self.username_input).to_be_visible(timeout=self.timeout)
        expect(self.password_input).to_be_visible(timeout=self.timeout)
        expect(self.login_button).to_be_visible(timeout=self.timeout)




