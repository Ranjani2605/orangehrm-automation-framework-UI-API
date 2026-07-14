


def test_search_user_by_valid_username(logged_in_admin_page, admin_search_data):
    username = admin_search_data['valid_search']['username']
    logged_in_admin_page.search_user_by_username(username)

    logged_in_admin_page.verify_serach_result_contains_username(username)





def test_search_user_by_valid_role(logged_in_admin_page, admin_search_data):
    role = admin_search_data['valid_search']['user_role']

    logged_in_admin_page.search_user_by_role(role)
    logged_in_admin_page.verify_page_does_not_crash()




def test_search_user_by_valid_status(logged_in_admin_page, admin_search_data):
    status = admin_search_data["valid_search"]["user_status"]
    logged_in_admin_page.search_user_by_status(status)
    logged_in_admin_page.verify_page_does_not_crash()


def test_search_user_with_username_and_role(logged_in_admin_page, admin_search_data):
    username = admin_search_data["valid_search"]["username"]
    role = admin_search_data["valid_search"]["user_role"]

    logged_in_admin_page.search_user_with_username_and_role(username=username, role=role)
    logged_in_admin_page.verify_page_does_not_crash()


def test_search_user_with_username_and_status(logged_in_admin_page, admin_search_data):
    username = admin_search_data["valid_search"]["username"]
    status = admin_search_data["valid_search"]["user_status"]
    logged_in_admin_page.search_user_with_username_and_status(username=username, status=status)
    logged_in_admin_page.verify_page_does_not_crash()


def test_reset_clears_username(logged_in_admin_page, admin_search_data):
    username = admin_search_data["valid_search"]["username"]
    logged_in_admin_page.search_user_by_username(username)
    logged_in_admin_page.click_reset()

    logged_in_admin_page.verify_reset_clears_username()

