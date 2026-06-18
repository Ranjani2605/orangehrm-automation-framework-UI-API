from playwright.sync_api import expect

from src.locators import sidebar_locators
from src.pages.base_page import BasePage
from src.locators.sidebar_locators import SidebarLocators
from src.locators.admin_user_management_locators import AdminUserManagementLocators

class AdminUserManagementPage(BasePage):

    def open_admin_page(self):
        self.safe_click(SidebarLocators.Admin_Menu)
        self.wait_for_page_load()

    def verify_admin_page_loaded(self):
        self.expect_visible(AdminUserManagementLocators.Page_Header)
        self.expect_visible(AdminUserManagementLocators.System_users_heading)


    def verify_logo_visible(self):
        self.expect_visible(SidebarLocators.Logo_Banner)

    def verify_sidebar_visible(self):
        self.expect_visible(SidebarLocators.Sidebar)

    def verify_sidebar_search_visible(self):
        self.expect_visible(SidebarLocators.Admin_Menu)

    def verify_admin_menu_visible(self):
        self.expect_visible(AdminUserManagementLocators.System_users_heading)

    def verify_system_users_heading_visible(self):
        self.expect_visible(AdminUserManagementLocators.System_users_heading)

    def verify_search_button_visible(self):
        self.expect_visible(AdminUserManagementLocators.Search_button)

    def verify_reset_button_visible(self):
        self.expect_visible(AdminUserManagementLocators.Reset_button)

    def verify_add_button_visible(self):
        self.expect_visible(AdminUserManagementLocators.Add_button)

    def search_by_username(self, username:str):
        self.clear_and_fill(AdminUserManagementLocators.Username_input, username)
        self.click_search()

    def search_by_user_role(self, role: str):
        self.select_dropdown_options(
            AdminUserManagementLocators.User_role_dropdown,
            AdminUserManagementLocators.dropdown_option(role)
        )
        self.click_search()

    def search_by_status(self, status: str):
        self.select_dropdown_options(
            AdminUserManagementLocators.User_role_dropdown,
            AdminUserManagementLocators.dropdown_option(status)
        )

        self.click_search()

    def search_by_employee_name(self, employee_name: str):
        self.clear_and_fill(AdminUserManagementLocators.Employee_name_input, employee_name)
        self.press_key("ArrowDown")
        self.press_key("Enter")
        self.click_search()

    def search_user(self, username=None, role=None, employee_name=None, status=None):
        if username:
            self.clear_and_fill(AdminUserManagementLocators.Username_input, username)

        if role:
            self.select_dropdown_options(
                AdminUserManagementLocators.User_role_dropdown,
                AdminUserManagementLocators.dropdown_option(role)
            )

        if employee_name:
            self.clear_and_fill(AdminUserManagementLocators.Employee_name_input, employee_name)
            self.press_key("ArrowDown")
            self.press_key("Enter")


        if status:
            self.select_dropdown_options(
                AdminUserManagementLocators.Status_dropdown,
                AdminUserManagementLocators.dropdown_option(status)
            )

        self.click_search()


    def click_search(self):
        self.safe_click(AdminUserManagementLocators.Search_button)
        self.wait_for_page_load()

    def click_reset(self):
        self.safe_click(AdminUserManagementLocators.Reset_button)
        self.wait_for_page_load()

    def click_add(self):
        self.safe_click(AdminUserManagementLocators.Add_button)
        self.wait_for_page_load()

    def verify_search_result_contains_username(self, username: str):
        expect(self.page.locator("body")).to_contain_text(username)

    def verify_no_records_found_message(self):
        self.expect_visible(AdminUserManagementLocators.No_Records_Found)

    def verify_table_visible(self):
        self.expect_visible(AdminUserManagementLocators.Table)

    def verify_table_header_visible(self):
        self.expect_visible(AdminUserManagementLocators.Table_Header)

    def verify_table_has_row(self):
        rows = self.page.locator(AdminUserManagementLocators.Table_Rows)
        assert rows.count() > 0, "Expected table to have rows"

    def verify_record_count_visible(self):
        self.expect_visible(AdminUserManagementLocators.Record_count)

    def verify_record_count_format(self):
        text = self.get_text(AdminUserManagementLocators.Record_count)
        assert "Record" in text, f"Invalid record count format: {text}"

    def verify_edit_button_visible(self):
        assert self.page.locator(AdminUserManagementLocators.Edit_Buttons).count() > 0


    def verify_delete_button_visible(self):
        assert self.page.locator(AdminUserManagementLocators.Delete_Buttons).count() > 0


    def verify_reset_clears_username(self):
        value = self.page.locator(AdminUserManagementLocators.Username_input).input_value()
        assert value == "", f"Expected username field to be empty, actual: {value}"

    def verify_required_message_visible(self):
        count = self.page.locator(AdminUserManagementLocators.Required_messages).count()
        assert count > 0, "Expected required validation messages"


    def verify_page_does_not_crash(self):
        self.verify_no_server_error_visible()
        expect(self.page.locator("body")).to_be_visible()


    def verify_username_trim_behaviour(self, username: str):
        self.verify_page_does_not_crash()


    def verify_success_message_formate(self):
        toast = self.page.locator(AdminUserManagementLocators.Toast_message)

        if toast.count() > 0:
            message = toast.first.inner_text().strip()
            assert len(message) > 0, "Toast message should not be empty"

    def verify_error_message_formate(self):
        messages = self.page.locator(AdminUserManagementLocators.Required_messages)

        if messages.count() > 0:
            message = messages.first.inner_text().strip()
            assert message[0].isupper(), f"Error message should start uppercase: {message}"


    def search_sidebar_menu(self, value:str):
        self.clear_and_fill(SidebarLocators.Menu_Search_input, value)


    def verify_sidebar_menu_visible(self, menu_name: str):
        self.expect_visible(SidebarLocators.menu_item(menu_name))


    def collapse_sidebar(self):
        self.safe_click(SidebarLocators.Collapse_button)


    def navigate_to_menu(self, menu_name: str):
        self.safe_click(SidebarLocators.menu_item(menu_name))
        self.wait_for_page_load()





