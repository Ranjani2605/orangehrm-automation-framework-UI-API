import json
import os


from dotenv import load_dotenv

from src.core.constants import DefaultValues, ProjectPaths
from src.core.exceptions import ConfigNotFoundException

load_dotenv()

class ConfigManager:
    _environment = DefaultValues.DEFAULT_ENV
    _config = None

    @classmethod
    def set_environment(cls,environment: str):
        cls._environment = environment
        cls._config = None


    @classmethod
    def get_environment(cls) -> str:
        return cls._environment

    @classmethod
    def load_config(cls) -> dict:
        if cls._config is not None:
            return cls._config

        config_file = ProjectPaths.CONFIG_DIR / f"{cls._environment}.json"

        if not config_file.exists():
            raise ConfigNotFoundException(
                f"Config file not found for environment '{cls._environment}' : {config_file}"
            )

        with open(config_file, "r" , encoding = "utf-8") as file:
            cls._config = json.load(file)

        return cls._config

    @classmethod
    def get(cls, key:str, default=None):
        return cls.load_config().get(key, default)

    @classmethod
    def get_base_url(cls) -> str:
        return cls.get("base_url")

    @classmethod
    def get_api_base_url(cls) -> str:
        return cls.get("api_base_url")

    @classmethod
    def get_timeout(cls) -> int:
        return cls.get("timeout", DefaultValues.DEFAULT_TIMEOUT)

    def is_headless(cls) -> bool:
        return bool(cls.get("headless", True))

    def get_username(cls) -> str:
        return os.getenv("ORANGEHRM_USERNAME")

    def get_password(cls) -> str:
        return os.getenv("ORANGEHRM_PASSWORD")

    def get_api_token(cls) -> str:
        return os.getenv("API_TOKEN", "")

    def is_db_enabled(cls) -> bool:
        return str(cls.get("db_enabled", False)).lower() == "true"

    def get_db_config(cls) -> dict:
        db_config = cls.get("db", {})

        return {
            "host" : os.getenv("DB_HOST", db_config.get("host", "localhost")),
            "port" : int(os.getenv("DB_PORT", db_config.get("port", 5432))),
            "username" : os.getenv("DB_USERNAME", db_config.get("username", "root")),
            "password" : os.getenv("DB_PASSWORD", db_config.get("password", "password")),
            "database": os.getenv("DB_NAME", db_config.get("database", "orangehrm"))
        }



