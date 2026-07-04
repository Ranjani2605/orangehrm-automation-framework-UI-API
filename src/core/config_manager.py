
import json
import os
from pathlib import Path
from dotenv import load_dotenv

from .constants import CONFIG_DIR

class ConfigManager:

    def __init__(self):
        load_dotenv()
        self.env = os.getenv("ENV", "dev")
        self.config = self._load_config()

    def _load_config(self) -> dict:
        config_file = Path(CONFIG_DIR)/f"{self.env}.json"

        if not config_file.exists():
            raise FileNotFoundError(f"config file not found: {config_file}")

        with open(config_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_base_url(self) -> str:
        return self.config["base_url"]

    def get_dashboard_url(self) -> str:
        return self.config["dashboard_url"]

    def get_api_base_url(self) -> str:
        return self.config["api_base_url"]

    def get_username(self) -> str:
        username = os.getenv("ORANGEHRM_USERNAME")
        if not username:
            raise ValueError("ORANGEHRM_USERNAME is missing in .env file")
        return username

    def get_password(self) -> str:
        password = os.getenv("ORANGEHRM_PASSWORD")
        if not password:
            raise ValueError("ORANGEHRM_PASSWORD is missing in .env file")
        return password

    def get_browser(self) -> str:
        return self.config.get("browser", "chromium")

    def is_headless(self) -> bool:
        return self.config.get("headless", True)

    def get_default_timeout(self) -> int:
        return self.config.get("default_timeout", 10000)

    def get_navigation_timeout(self) -> int:
        return self.config.get("navigation_timeout", 30000)

    def get_viewport(self) -> dict:
        return self.config.get("viewport", {"width": 1366, "height": 768})

    def is_db_enabled(self) -> bool:
        return self.config.get("db_enabled", False)

    def get_db_config(self) -> dict:
        return{
            "host": os.getenv("DB_HOST"),
            "port": int(os.getenv("DB_PORT", 3306)),
            "user": os.getenv("DB_USERNAME"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),



        }






