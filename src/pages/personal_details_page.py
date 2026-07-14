from src.locators.pim_locators import PimLocators
from src.pages.base_page import BasePage
from utils.helper.common.calendra_helper import CalendraHelper
from utils.helper.common.dropdown_helper import DropdownHelper


class PersonalDetailsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.dropdown_helper = DropdownHelper(page)
        self.calendar_helper = CalendraHelper(page)


    def verify_personal_details_page_opened(self):
        self.expect_visible(PimLocators.personal_details_header)


    def enter_driver_license_number(self, license_number: str):
        self.clear_and_fill(PimLocators.driver_license_input, license_number)


    def enter_license_expiry_date(self, expiry_date: str):
        self.calendar_helper.enter_date(PimLocators.license_expiry_input, expiry_date)


    def select_nationality(self, nationality: str):
        self.dropdown_helper.select_dropdown_value(
            PimLocators.nationality_dropdown, nationality
        )


    def select_marital_status(self, marital_status: str):
        self.dropdown_helper.select_dropdown_value(
            PimLocators.marital_status_dropdown, marital_status
        )

    def enter_date_of_birth(self, dob: str, minimum_age: int):
        assert self.calendar_helper.is_age_equal_or_above(
            dob=dob,
            minimum_age=minimum_age,
        ), f"Date of birth '{dob}' does not make employee age above or equal to {minimum_age}"

        self.calendar_helper.enter_date(PimLocators.date_of_birth_input, dob)


    def select_gender(self, gender: str):
        if gender.lower() == "male":
            self.click(PimLocators.male_radio)
        elif gender.lower() == "female":
            self.click(PimLocators.female_radio)
        else:
            raise ValueError(f"Unsupported gender value: {gender}")


    def click_personal_details_save(self):
        self.page.locator(PimLocators.save_button).first.click()


    def select_blood_type(self, blood_type: str):
        self.dropdown_helper.select_dropdown_value(
            PimLocators.blood_type_dropdown, blood_type
        )


    def enter_test_field(self, value: str):
        self.clear_and_fill(PimLocators.test_field_input, value)


    def click_custom_fields_save(self):
        self.page.locator(PimLocators.save_button).nth(1).click()
        self.wait_for_page_load()


    def fill_personal_details(self, employee_data: dict):
        self.enter_driver_license_number(employee_data["license_number"])
        self.enter_license_expiry_date(employee_data["license_expiry_date"])
        self.select_nationality(employee_data["nationality"])
        self.select_marital_status(employee_data["marital_status"])

        self.enter_date_of_birth(
            dob=employee_data["date_of_birth"],
            minimum_age=employee_data["minimum_age"]
        )

        self.select_gender(employee_data["gender"])
        self.click_personal_details_save()

    def fill_custom_fields(self, employee_data: dict):
        self.select_blood_type(employee_data["blood_type"])
        self.enter_test_field(employee_data["test_field_value"])
        self.click_custom_fields_save()


