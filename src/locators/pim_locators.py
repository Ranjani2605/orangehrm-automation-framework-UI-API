class PimLocators:
    # Navigation

    pim_menu = "a[href*='/pim/viewPimModule']"
    employee_list_tab ="a.oxd-topbar-body-nav-tab-item:has-text('Employee List')"

    # Employee List page
    employee_information_header = "h5:has-text('Employee Information')"
    add_button = "button:has-text('Add')"
    search_button = "button[type='submit']:has-text('search')"


    employee_id_search_input = (
        "//label[text()='Employee id']"
         "//ancestor::div[contains(@class, 'oxd-input-group')]"
         "//input"
    )

    # Add employee page
    add_employee_header = "h6:has-text('Add Employee')"
    employee_full_name_label = "label:has-text('Employee Full Name')"


    first_name_input = "input[placeholder='First Name']"
    middle_name_input = "input[placeholder='Middle Name']"
    last_name_input = "input[placeholder='Last Name']"


    employee_id_input = (
        "//label[text()='Employee id']"
        "//ancestor::div[contains(@class, 'oxd-input-group')]"
        "//input"
    )

    save_button = "button[type='submit']:has-text('Save')"
    required_validation_message = "span:has-text('Required')"

    # Personal details page
    personal_details_header = "h6:has-text('Personal Details')"


    driver_license_input = (
        "//label[text()=\"Driver's License Number\"]"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    license_expiry_input = (
        "//label[text()='License Expiry Date']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    nationality_dropdown = (
        "//label[text()='Nationality']"
        "/ancestor::div[contains(@class, 'oxd-input-group')]"
        "//div[contains(@class, 'oxd-select-text')]"
    )

    marital_status_dropdown = (
        "//label[text()='Nationality]"
        "/ancestor::div[contains(@class, 'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]"
    )

    date_of_birth_input = (
        "//label[text()='Date of Birth']"
        "/ancestor::div[contains(@class, 'oxd-input-group')]"
        "//input"
    )

    male_radio = "//label[contains(normalize-space(),'Male')]//span"
    female_radio = "//label[contains(normalize-space(),'Female')]//span"

    blood_type_dropdown = (
        "//label[text()='Blood Type']"
        "/ancestor::div[contains(@class, 'oxd-input-group')]"
        "//div[contains(@class, 'oxd-select-text')]"
    )

    test_field_input = (
        "//label[text()='Test_Field']"
        "//ancestor::div[contains(@class, 'oxd-input-group')]"
        "//input"
    )

    # table
    table_row = ".oxd-table-body .oxd-table-card"
    table_cell = ".oxd-table-cell"