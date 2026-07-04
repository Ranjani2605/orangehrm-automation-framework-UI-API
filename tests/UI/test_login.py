import pytest

from src.core.constants import DATA_DIR
from src.pages.login_page import LoginPage
from utils.file_reader import read_json_file

@pytest.mark.ui
@pytest.mark.smoke
def test_valid_admin_user_can_login(login_page, config):

    login_page.open_login_page(config.get_base_url())
    login_page.login(config.get_username(), config.get_password())

    assert "/dashboard/index" in login_page.page.url
