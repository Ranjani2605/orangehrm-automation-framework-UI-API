import json
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent[1]
CONFIG_PATH = ROOT_DIR/"config"/"config.json"

load_dotenv()


class Settings:
    def __init__(self, env:str):
        self.env = env
        self._config = self._load_config()

        if env not in self._config:
            raise ValueError(f"Invalid env '{env}'. valid environments: {list(self._config.keys())}")

        self._env_config = self._config[env]

    def _load_config(self) -> dict:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            return json.load(file)


    @property
    def base_url(self) -> str:
        return self._env_config["base_url"]

    @property
    def username(self) -> str:
        return os.getenv(self._env_config["username"], "")

    @property
    def password(self) -> str:
        return os.getenv(self._env_config["password"], "")

    @property
    def default_timeout(self) -> int:
        return self._config["timeout"]["default_timeout"]

    @property
    def navigation_timeout(self) -> int:
        return self._config["timeout"]["navigation_timeout"]

    @property
    def screenshot_dir(self) -> str:
        return self._config["artifacts"]["screenshots"]

    @property
    def video_dir(self) -> str:
        return self._config["artifacts"]["videos"]

    @property
    def trace_dir(self) -> str:
        return self._config["artifacts"]["traces"]






