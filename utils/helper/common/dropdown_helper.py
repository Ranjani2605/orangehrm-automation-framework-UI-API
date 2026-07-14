from playwright.sync_api import Page


class DropdownHelper:

    def __init__(self, page : Page):
        self.page = page



    def select_dropdown_value(self, dropdown_locator: str, option_text: str):
        self.page.locator(dropdown_locator).click()
        self.page.locator(f"//div[@role='option']//span[text()='{option_text}']").click()



