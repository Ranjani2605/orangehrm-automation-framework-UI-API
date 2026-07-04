import os
from datetime import datetime
from pathlib import Path

import allure
import pytest
from playwright.sync_api import sync_playwright

from src.core import config_manager
from src.core.config_manager import ConfigManager
from src.core.constants import SCREENSHOTS_DIR, VIDEOS_DIR
from src.pages.login_page import LoginPage
from src.db.db_connection import *

@pytest.fixture(scope="session")
def config():
    return config_manager.ConfigManager()

def create_artifact_folders():
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session", autouse=True)
def setup_folders():
    create_artifact_folders()

@pytest.fixture(scope="session", autouse=True)
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser_context(playwright_instance, config):
    browser_name = config.get_browser()
    browser_type = getattr(playwright_instance, browser_name)

    browser = browser_type.launch(headless=config.is_headless())

    context = browser.new_context(viewport=config.get_viewport(), record_video_dir=str(VIDEOS_DIR))

    context.set_default_timeout(config.get_default_timeout())
    context.set_default_navigation_timeout(config.get_navigation_timeout())

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page


@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def logged_in_page(page, config):
    login_page = LoginPage(page)

    login_page.open_login_page(config.get_base_url())
    login_page.login(config.get_username(), config.get_password())
    return page



