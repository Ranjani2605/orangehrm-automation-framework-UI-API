import configparser
import json
import os
from pathlib import Path
from dotenv import load_dotenv

from src.core.constants import *

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

    def get(self, key:str, default=None):
        return self.config.get(key, default)

    def get_base_url(self) -> str:
        return self.config["base_url"]

    def get_dashboard_url(self) -> str:
        return self.config["dashboard_url"]

    def get_api_base_url(self) -> str:
        return self.config["api_base_url"]




