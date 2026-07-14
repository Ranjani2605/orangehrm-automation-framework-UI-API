import re

from playwright.sync_api import expect

from src.locators.pim_locators import PimLocators
from src.pages.base_page import BasePage


class PimPage(BasePage):

    def open_pim_module(self):
        self.click(PimLocators.pim_menu)
        self.expect_visible(PimLocators.employee_information_header)


    def click_add_employee(self):
        self.click(PimLocators.add_button)
        self.expect_visible(PimLocators.add_employee_header)


    def verify_add_employee_age_opened(self):
        self.expect_visible(PimLocators.add_employee_header)

    def verify_employee_full_name_is_mandatory(self):
        self.expect_visible(PimLocators.employee_full_name_label)

        class_value = self.page.locator(
            PimLocators.employee_full_name_label).get_attribute("class")

        assert class_value is not None
        assert "oxd-input-field-required" in class_value, (
            "Employee Full Name field is not marked as mandatory"
        )

    def verify_name_fields_are_displayed(self):
        self.expect_visible(PimLocators.first_name_input)
        self.expect_visible(PimLocators.middle_name_input)
        self.expect_visible(PimLocators.last_name_input)


    def verify_first_name_is_required(self):
        self.click(PimLocators.save_button)
        expect(self.page.locator(PimLocators.required_validation_message)).to_be_visible()


    def enter_employee_name(self, first_name: str, middle_name: str = "", last_name: str = "" ):
        first_name_field = self.locator(PimLocators.first_name_input)
        middle_name_field = self.locator(PimLocators.middle_name_input)
        last_name_field = self.locator(PimLocators.last_name_input)

        first_name_field.wait_for(state="visible")
        first_name_field.click()
        first_name_field.fill(first_name)

        if middle_name:
            middle_name_field.wait_for(state="visible")
            middle_name_field.click()
            middle_name_field.fill(middle_name)

        if last_name:
            last_name_field.wait_for(state="visible")
            last_name_field.click()
            last_name_field.fill(last_name)

    def get_employee_id(self) -> str:
        return self.get_input_value(PimLocators.employee_id_input)

    def verify_employee_id_generated(self, employee_id: str):
        assert employee_id != "", "Employee ID should not be empty"

    def verify_employee_id_numeric(self, employee_id: str):
        assert employee_id.isdigit(),f"Employee ID should be numeric, but got: '{employee_id}'"

    def verify_employee_id_exact_digits(self, employee_id: str, expected_digits: int):
        pattern =rf"\d{{{expected_digits}}}"

        assert re.fullmatch(pattern, employee_id), (
            f"Employee ID should contain exactly {expected_digits} digits, but got: '{employee_id}'"
        )

    def click_save(self):
        self.click(PimLocators.save_button)

    def wait_for_personal_details_page(self):
        self.expect_visible(PimLocators.personal_details_header)

    def click_employee_list_tab(self):
        self.click(PimLocators.employee_list_tab)
        self.expect_visible(PimLocators.employee_list_tab)
        self.expect_visible(PimLocators.employee_information_header)

    def search_employee_by_id(self, employee_id: str):
        self.clear_and_fill(PimLocators.employee_id_search_input, employee_id)
        self.click(PimLocators.search_button)
        self.page.wait_for_load_state("networkidle")

