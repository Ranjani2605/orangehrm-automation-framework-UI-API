import datetime
from uuid import uuid4


class DataGenerator:

    @staticmethod
    def unique_text(prefix: str = 'Auto') -> str:
        return f"{prefix}{str(uuid4())[:8]}"


    @staticmethod
    def unique_employee_name() -> dict:
        suffix = str(uuid4())[:6]

        return {
            "first_name": f"Auto{suffix}",
            "middle_name": "QA",
            "last_name": "User"

        }

    @staticmethod
    def timestamp() -> str:
        return datetime.now().strftime("%Y%m%d%H%M%S")