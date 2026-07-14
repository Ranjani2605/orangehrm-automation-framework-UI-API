import pytest

from src.locators.pim_locators import PimLocators
from src.pages.pim_page import PimPage


def test_first_name_is_required(logged_in_page):
    page = logged_in_page
    pim_page = PimPage(page)

    pim_page.open_pim_module()
    pim_page.click_add_employee()

    page.locator(PimLocators.middle_name_input).fill("OnlyMiddle")
    page.locator(PimLocators.last_name_input).fill("OnlyLast")


    pim_page.click_save()

    pim_page.verify_first_name_is_required()


