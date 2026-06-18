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
