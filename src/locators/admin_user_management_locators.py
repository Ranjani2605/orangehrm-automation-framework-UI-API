class AdminUserManagementLocators:
    Page_Header = "//h6[normalze-space()='Admin']"
    System_users_heading = "//h5[normalize-space()='System Users']"

    Username_input = (
        "//label[normalize-space()='Username']"
        "//ancestor::div[contains@class,'oxd-input-group')]//input"
    )

    User_role_dropdown =(
        "//label[normalize-space()='User Role']"
        "//ancestor::div[contains@class,'oxd-input-group']"
        "//div[contains(@class,'oxd-select-text')]"
    )

    Employee_name_input = (
        "//label[normalize-space()='Employee Name']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    Status_dropdown = (
        "//label[normalize-space()='Status']"
        "ancestor::div[contains@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]"
    )

    Search_button = "//button[normalize-space()='Search']"
    Reset_button = "//button[normalize-space()='Reset']"
    Add_button = "//button[normalize-space()='Add']"

    Table = ".oxd-table"
    Table_Header = ".oxd-table-header"
    Table_Rows = ".oxd-table-body .oxd-table-row"
    Record_count = "//span[contains(normalize-space(), 'Record')]"
    No_Records_Found = "//span[normalize-space()='No Records Found']"


    Edit_Buttons = "button:has(i.bi-pencil-fill)"
    Delete_Buttons = "button:has(i.bi-trash)"

    Save_button = "//button[normalize-space()='Save']"
    Cancel_button = "//button[normalize-space()='Cancel']"
    Required_messages = "//span[normalize-space()='Required']"
    Toast_message = ".oxd-toast"


    @staticmethod
    def dropdown_option(option: str) -> str:
        return f"//div[@role='option']//span[normalize-space()='{option}']"

    @staticmethod
    def table_cell(value: str) -> str:
        return f"//div[contains(@class,'oxd-table-cell') and .//*[normalize-space()='{value}']]"


