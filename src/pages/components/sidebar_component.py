from src.locators import sidebar_locators
from src.pages.base_page import BasePage
from src.locators.sidebar_locators import SidebarLocators


class SidebarComponent(BasePage):

    def verify_sidebar_visible(self):
        self.expect_visible(SidebarLocators.Sidebar)

    def verify_logo_visible(self):
        self.expect_visible(SidebarLocators.Logo_Banner)

    def verify_menu_item_visible(self, menu_name: str):
        self.expect_visible(SidebarLocators.menu_item(menu_name))


    def click_menu_item(self, menu_name:str):
        self.safe_click(SidebarLocators.menu_item(menu_name))
        self.wait_for_page_load()

    def search_menu(self, menu_name:str):
        self.clear_and_fill(SidebarLocators.Menu_Search_input, menu_name)


    def collapse_sidebar(self):
        self.safe_click(SidebarLocators.Collapse_button)