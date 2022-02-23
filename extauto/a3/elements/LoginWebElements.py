from extauto.a3.defs.LoginWebElementsDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *
from selenium.common.exceptions import NoSuchElementException


class LoginWebElements(LoginWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def get_login_page_username_text(self):
        return self.weh.get_element(self.login_page_username_text_ids)

    def get_login_page_password_text(self):
        return self.weh.get_element(self.login_page_password_text_ids)

    def get_login_page_login_button(self):
        return self.weh.get_element(self.login_page_login_button_ids)

    def get_dialog_message(self):
        try:
            db = self.weh.get_element(self.dialog_box)
            if db:
                if self.weh.get_element(self.dialog_box).is_displayed():
                    return True
                else:
                    return False
        except Exception as e:
            self.utils.print_info('Error: ', e)
            return False

    def get_dialog_box_close_button(self):
        try:
            parents = self.weh.get_elements(self.dialog_box)
            for parent in parents:
                if "CLOSE" in parent.text.upper():
                    children = self.weh.get_elements(self.dialog_box_close_button)

                    for child in children:
                        if "CLOSE" in child.text.upper():
                            return child
        except NoSuchElementException:
            return None

    def get_logout_link(self):
        element = self.weh.get_element(self.logout_account_info)
        self.auto_actions.move_to_element(element)

        menu = self.weh.get_element(self.logout_user_menu_item)
        menu_items = self.weh.get_elements(self.menu_item, menu)
        for menu_item in menu_items:
            self.utils.print_debug("Menu Items: ", menu_item.text.upper())
            if 'LOGOUT' in menu_item.text.upper():
                return menu_item

    def get_credentials_error_message(self):
        try:
            errors = self.weh.get_elements(self.login_page_wrong_password_message)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception as e:
            return "No Message"

    def get_welcome_page_done_button(self):
        buttons = self.weh.get_elements(self.welcome_page_done_button)
        for button in buttons:
            if "DONE" in button.text:
                return button

    def get_header_text(self):
        return self.weh.get_element(self.header_text).text

    def get_build_version_details(self):
        return self.weh.get_element(self.build_version_details).text

    def get_about_extreme_cloudiq_link(self):
        element = self.weh.get_element(self.user_account_nav)
        self.auto_actions.move_to_element(element)

        menu = self.weh.get_element(self.logout_user_menu_item)
        menu_items = self.weh.get_elements(self.menu_item, menu)
        for menu_item in menu_items:
            self.utils.print_debug("Menu Items: ", menu_item.text.upper())
            if 'ABOUT EXTREMECLOUD IQ' in menu_item.text.upper():
                return menu_item

    def get_cancel_about_extremecloudiq_dialogue(self):
        return self.weh.get_element(self.cancel_about_extremecloudiq_dialogue)

    def get_viq_id_field(self):
        return self.weh.get_element(self.viq_id_field)


    def get_30_days_trial_txt(self):
        return self.weh.get_element(self.txt_30_days_trial)

    def get_option_30_days_trial(self):
        return self.weh.get_element(self.option_30_days_trial)

    def get_get_started_button(self):
        return self.weh.get_element(self.started_button)

    def get_drawer_trigger(self):
        return self.weh.get_element(self.drawer_trigger)

    def get_drawer_content(self):
        return self.weh.get_element(self.drawer_content)

    def get_wips_dialog_message(self):
        try:
            errors = self.weh.get_elements(self.wips_dialog_message)
            if errors:
                for error in errors:
                    if error.is_displayed():
                        return error.text
            else:
                return "No Message"
        except Exception as e:
            return "No Message"

    def get_wips_popup_dialog_close_button(self):
        return self.weh.get_element(self.wips_popup_dialog_close_button)

    def get_wips_popup_dialog_dont_show_again_checkbox(self):
        return self.weh.get_element(self.wips_popup_dialog_dont_show_again_checkbox)
