import datetime
import json
from pathlib import Path
from uuid import uuid4

from faker import Faker

from src.core.constants import DATA_DIR
from utils.helper.common.calendra_helper import CalendraHelper


class EmployeeDataGenerator:


    def __init__(self):
        self.fake = Faker()
        self.test_config = self._load_employee_test_config()


    def _load_employee_test_config(self) -> dict:
        file_path = Path(DATA_DIR)/"employee_test_config.json"

        if not file_path.exists():
            raise FileNotFoundError(f"Employee test config file not found at {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)


    def generate_employee_data(self) -> dict:
        employee_rules = self.test_config["employee_rules"]
        personal_details = self.test_config["personal_details"]
        custom_fields = self.test_config["custom_fields"]

        minimum_age = employee_rules["minimum_age"]
        license_expiry_years = personal_details["license_expiry_years_from_today"]


        first_name = self.fake.first_name()
        middle_name = self.fake.middle_name()
        last_name = self.fake.last_name()

        unique_text = uuid4().hex[:6].upper()

        dob = CalendraHelper.generate_dod_above_age(
            minimum_age=minimum_age,
            extra_years=1
        )

        license_expiry_date = CalendraHelper.generate_dod_above_age(
            years_from_today=license_expiry_years
        )

        return {

            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "license_number": f"DL{unique_text}",
            "license_expiry_date": license_expiry_date,
            "date_of_birth": dob,
            "minimum_age": minimum_age,
            "nationality": personal_details["nationality"],
            "marital_status": personal_details["marital_status"],
            "gender": personal_details["gender"],
            "blood_type": personal_details["blood_type"],
            "test_field_value": f"{custom_fields['test_field_value']} {unique_text}",
            "validate_employee_id_exact_digits": employee_rules["validate_employee_id_exact_digits"],
            "employee_id_digits": employee_rules["employee_id_digits"]
            }




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