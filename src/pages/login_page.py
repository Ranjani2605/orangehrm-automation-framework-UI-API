

from src.pages.base_page import BasePage
from src.locators.login_loacators import LoginLocators



class LoginPage(BasePage):

    def enter_username(self, username:str):
        self.clear_and_fill(LoginLocators.username_input, username)

    def enter_password(self, password:str):
        self.clear_and_fill(LoginLocators.password_input, password)

    def click_login_button(self):
        self.click(LoginLocators.login_button)

    def login(self, username:str, password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_invalid_credentials_message_visible(self):
        self.expect_visible(LoginLocators.invalid_credentials_alert)




