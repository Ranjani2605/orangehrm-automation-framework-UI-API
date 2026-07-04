import pytest

from src.core.constants import DATA_DIR
from src.pages.login_page import LoginPage
from utils.file_reader import read_json_file

@pytest.mark.ui
def test_valid_admin_user_can_login(page, config):

    login_page = LoginPage(page)

    login_page.open_login_page(config.get_base_url())
    login_page.enter_username(config.get_username)
    login_page.enter_password(config.get_password)
