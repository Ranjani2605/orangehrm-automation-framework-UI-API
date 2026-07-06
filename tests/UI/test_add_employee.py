
import pytest
from src.pages.pim_page import PimPage
from src.pages.personal_details_page import PersonalDetailsPage
from utils.data_generator import EmployeeDataGenerator
from utils.helper.common.table_helper import TableHelper

@pytest.mark.ui
@pytest.mark.e2e
@pytest.mark.regression
def test_add_employee_and_validate_employee_details(logged_in_page):
    page = logged_in_page
    employee_data = EmployeeDataGenerator().generate_employee_data()

    pim_page = PimPage(page)
    personal_details_page = PersonalDetailsPage(page)
    table_helper = TableHelper(page)

    pim_page.open_pim_module()
    pim_page.click_add_employee()
    pim_page.verify_add_employee_age_opened()

    pim_page.verify_employee_full_name_is_mandatory()
    pim_page.verify_name_fields_are_displayed()


    pim_page.enter_employee_name(
        first_name=employee_data["first_name"],
        middle_name=employee_data["middle_name"],
        last_name=employee_data["last_name"]
    )

    employee_id = pim_page.get_employee_id()
    pim_page.verify_employee_id_generated(employee_id)
    pim_page.verify_employee_id_numeric(employee_id)

    if employee_data["validate_employee_id_exact_digits"]:
        pim_page.verify_employee_id_exact_digits(employee_id=employee_id, expected_digits=employee_data["employee_id_digits"])

    pim_page.click_save()
    pim_page.wait_for_personal_details_page()

    personal_details_page.verify_personal_details_page_opened()

    personal_details_page.fill_personal_details(employee_data)
    personal_details_page.fill_personal_details(employee_data)

    pim_page.click_employee_list_tab()
    pim_page.search_employee_by_id(employee_id)

    table_helper.assert_employee_row(
        employee_id=employee_id,
        first_name=employee_data["first_name"],
        middle_name=employee_data["middle_name"],
        last_name=employee_data["last_name"]
    )

