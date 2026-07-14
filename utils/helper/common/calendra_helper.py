from time import strftime

from playwright.sync_api import Page
from datetime import date, datetime

class CalendraHelper:

    def __init__(self, page:Page):
        self.page = page


    def enter_date(self, input_locator: str, date_value: str):
        self.page.locator(input_locator).clear()
        self.page.locator(input_locator).fill(date_value)

    @staticmethod
    def generate_dod_above_age(
            minimum_age: int = 18,
            extra_years: int = 1,
            date_formate: str = "%Y-%m-%d"
    ) -> str:

        """Dynamically generate a date of birth above the required age."""
        today = date.today()
        birth_date = today.year - minimum_age - extra_years

        dob = date(
            year= birth_date,
            month= today.month,
            day= today.day
        )

        return dob.strftime(date_formate)

    @staticmethod
    def generate_future_date(
        years_from_today: int,
        date_format: str = "%Y-%m-%d") -> str:
        today = date.today()

        future_date = date(
            year=today.year + years_from_today,
            month=today.month,
            day=today.day
       )
        return future_date.strftime(date_format)

    @staticmethod
    def is_age_equal_or_above(dob: str, minimum_age: int =18, date_formate: str = "%Y-%m-%d") -> bool:
        """Checks whether DOB age is equal to or above the required age."""
        dob_date = datetime.strptime(dob, date_formate).date()
        today = date.today()

        age = today.year - dob_date.year

        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1

        return age >= minimum_age

