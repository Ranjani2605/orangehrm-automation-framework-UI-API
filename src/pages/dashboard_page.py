from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class DashboardPage(BasePage):

    quick_lunch_items = {
            "Assign Leave": ("assignLeave", "Assign Leave"),
            "Leave List": ("viewLeaveList", "Leave"),
            "Timesheets": ("viewEmployeeTimesheet", "Timesheets"),
            "Apply Leave": ("applyLeave", "Apply Leave"),
            "My Leave": ("viewMyLeaveList", "Leave"),
            "My Timesheet": ("viewMyTimesheet", "Timesheet"),
        }

    def __init__(self, page: Page):
        super().__init__(page)
        #
        #Quick Launch widget

        self.quick_lunch_widget_name = page.locator("text=Quick Launch")
        self.assign_leave = page.locator('button[title= "Assign Leave"]')
        self.leave_list = page.locator('button[title="Leave List"]')
        self.timesheets = page.locator('button[title="Timesheets"]')
        self.apply_leave = page.locator('button[title="Apply Leave"]')
        self.my_leave = page.locator('button[title="My Leave"]')
        self.my_timesheet = page.locator('button[title="My Timesheet"]')

        self.pim_menu = page.get_by_role("link", name="PIM")
        self.user_dropdown = page.locator(".oxd-userdropdown-tab")
        self.logout_link = page.get_by_role("menuitem", name="Logout")


    def verify_dashboard_displayed(self):
        expect(self.dashboard_header).to_be_visible(timeout=self.timeout)


    def go_to_pim(self):
        self.click(self.pim_menu)


    def click_leave_list(self):
        self.click(self.leave_list)

    def click_timesheets(self):
        self.click(self.timesheets)

    def click_apply_leave(self):
        self.click(self.apply_leave)

    def click_myLeave(self):
        self.click(self.my_leave)

    def click_my_timesheet(self):
        self.click(self.my_timesheet)


    def click_quick_launch(self, name :str):
        self.click(f"button[title='{name}']")
        url_part, page_title = self.quick_lunch_items[name]
        self.verify_page_loaded(url_part, page_title)

    def logout(self):
        self.click(self.user_dropdown)
        self.click(self.logout_link)



