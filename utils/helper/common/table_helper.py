
class TableHelper:

    def __init__(self, page):
        self.page = page


    def get_table_rows(self):
        return self.page.locator(".oxd-table-body .oxd-table-card")

    def get_row_count(self) -> int:
        return self.get_table_row().count()

    def get_row_values(self, row_index: int) -> list[str]:
        row = self.get_table_row().nth(row_index)
        cells = row.locator(".oxd-table-cell")

        values = []

        for index in range(cells.count()):
            values.append(cells.nth(index).innerText().strip())

        return values


    def find_row_by_cell_value(self, expected_value:str) -> list[str] | None:
        rows = self.get_table_rows()

        for row_index in range(rows.count()):
            row_values = self.get_row_values(row_index)

            if expected_value in row_values:
                return row_values

        return None


    def assert_employee_row(self, employee_id: str, first_name: str, middle_name: str, last_name: str):

        row_values = self.find_row_by_cell_value(employee_id)
        assert row_values is not None, f"Employee ID' {employee_id} was not found in table"

        actual_employee_id = row_values[1]
        actual_first_middle_name = row_values[2]
        actual_last_name = row_values[3]

        assert actual_employee_id == employee_id, (
            f"Expected employee ID '{employee_id}', but got '{actual_employee_id}'"

        )

        assert first_name in actual_first_middle_name, (
            f"Expected first name '{first_name}', but got '{actual_employee_id}'"
        )

        if middle_name:
            assert middle_name in actual_first_middle_name, (
                f"Expected middle name '{middle_name}', but got '{actual_first_middle_name}'"
            )

        if last_name:
            assert actual_last_name == last_name, (
                f"Expected last name '{last_name}', but got '{actual_last_name}'"
            )
