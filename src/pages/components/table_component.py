from src.pages.base_page import BasePage
from src.locators.admin_user_management_locators import AdminUserManagementLocators

class TableComponent(BasePage):

    def verify_table_visible(self):
        self.expect_visible(AdminUserManagementLocators.Table)


    def verify_table_header_visible(self):
        self.expect_visible(AdminUserManagementLocators.Table_Header)

    def verify_table_has_rows(self):
        rows = self.page.locator(AdminUserManagementLocators.Table_Rows)
        assert rows.count() > 0,  "Expected at least one table row"

    def verify_no_records_found(self):
        self.expect_visible(AdminUserManagementLocators.No_Records_Found)

    def verify_record_count_visible(self):
        self.expect_visible(AdminUserManagementLocators.Record_count)

    def verify_record_count_format(self):
        count_text = self.get_text(AdminUserManagementLocators.Record_count)
        assert "Record" in count_text, f"Invaid record count text: {count_text}"

    def verify_edit_button_visible(self):
        count = self.page.locator(AdminUserManagementLocators.Edit_Buttons).count()
        assert count > 0, "Expected edit button to be visible"


    def verify_delete_button_visible(self):
        count = self.page.locator(AdminUserManagementLocators.Delete_Buttons).count()
        assert count > 0, "Expected delete button to be visible"
