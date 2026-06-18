class SidebarLocators:
    Sidebar = "aside.oxd-sidepanel"
    Logo_Banner ="img[alt='client brand banner']"
    Menu_Search_input = "input[placeholder='Search']"
    Collapse_button = "button.oxd-main-menu-button"

    Admin_Menu = "//span[normalize-space()='Admin']/ancestor::a"
    PIM_Menu = "//span[normalize-space()='PIM']/ancestor::a"
    Leave_Menu = "//span[normalize-space()='Leave']/ancestor::a"
    Time_menu = "//span[normalize-space()='Time']/ancestor::a"
    Recruitment_menu = "//span[normalize-space()='Recruitment']/ancestor::a"

    @staticmethod
    def menu_item(menu_name:str) -> str:
        return f"//span[normalize-space()='{menu_name}'/ancestor::a"
