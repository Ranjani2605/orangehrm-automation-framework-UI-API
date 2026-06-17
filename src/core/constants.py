from pathlib import Path

class ProjectPaths:

    ROOT_DIR = Path(__file__).resolve().parent[2]
    CONFIG_DIR = ROOT_DIR/ "config"
    DATA_DIR = ROOT_DIR/ "data"
    REPORTS_DTR = ROOT_DIR / "reports"
    SCREENSHOTS_DIR = ROOT_DIR/ "screenshots"
    VIDEOS_DIR = REPORTS_DTR / "videos"
    LOGS_DIR = REPORTS_DTR / "logs"
    ALLURE_RESULTS_DIR = REPORTS_DTR/ "allure-results"


class DefaultValues:
    DEFAULT_ENV = "qa"
    DEFAULT_BROWSER = "chromium"
    DEFAULT_TIMEOUT = 30000


class ErrorMessages:
    INVALID_CREDENTIALS = "Invalid credentials"
    REQUIRED = "Required"
    NO_RECORDS_FOUND = "No Recoeds Found"


