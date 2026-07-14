import allure
import pytest


@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_admin_page_loads_successfully(logged_in_admin_page):
    logged_in_admin_page.verify_admin_page_loaded()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_logo_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_logo_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_sidebar_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_sidebar_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_admin_menu_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_admin_menu_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_sidebar_search_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_sidebar_search_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_system_users_heading_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_system_users_heading_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_system_button_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_search_button_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_reset_button_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_reset_button_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_add_button_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_add_button_is_visible()

@allure.feature("Admin")
@allure.story("smoke")
@pytest.mark.smoke
def test_table_is_visible(logged_in_admin_page):
    logged_in_admin_page.verify_table_is_visible()

