from extauto.portal.defs.PortalWebElementsDefinitions import PortalWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class PortalWebElements(PortalWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_login_portal_page_username_text(self):
        return self.weh.get_element(self.login_portal_page_username_text)

    def get_login_portal_page_password_text(self):
        return self.weh.get_element(self.login_portal_page_password_text)

    def get_login_portal_page_login_button(self):
        return self.weh.get_element(self.login_portal_page_login_button)

    def get_login_portal_check_error(self):
        elements = self.weh.get_elements(self.login_portal_check_error)
        if elements:
            for el in elements:
                if el.is_displayed():
                    return el
                else:
                    return None
        else:
            return None

    def get_add_button_portal(self):
        return self.weh.get_element(self.add_button_portal)

    def get_logout_portal_user_menu_item(self):
        return self.weh.get_element(self.logout_menu_portal)

    def get_users_menu_item(self):
        return self.weh.get_element(self.users_menu_portal)

    def get_customers_menu_item(self):
        return self.weh.get_element(self.customers_menu_portal)

    def get_users_page_add_button(self):
        return self.weh.get_element(self.users_page_add_button)

    def get_add_users_page_fullname_text(self):
        return self.weh.get_element(self.add_users_page_fullname_text)

    def get_add_users_page_email_text(self):
        return self.weh.get_element(self.add_users_page_email_text)

    def get_add_users_page_role_msp_text(self):
        return self.weh.get_element(self.add_users_page_role_msp_text)

    def get_add_users_page_role_viq_text(self):
        return self.weh.get_element(self.add_users_page_role_viq_text)

    def get_users_page_submit_button(self):
        return self.weh.get_element(self.add_users_page_submit_button)

    def get_users_page_name_filter_item(self):
        return self.weh.get_element(self.users_page_name_filter_item)

    def get_users_page_email_filter_item(self):
        return self.weh.get_element(self.users_page_email_filter_item)

    def get_users_page_name_filter_text(self):
        return self.weh.get_element(self.users_page_name_filter_text)

    def get_filter_user_name_list(self, username):
        item = {}
        item['XPATH'] = self. users_page_filter_list['XPATH'] + '"' + username + '"' +')]'
        item['wait_for'] = 3
        return item

    def get_add_users_page_datacenter_checkbox(self):
        return self.weh.get_element(self.add_users_page_datacenter_checkbox)

    def get_add_users_page_datacenter_label(self):
        return self.weh.get_element(self.add_users_page_datacenter_label)

    def get_users_page_lastpage_button(self):
        return self.weh.get_element(self.users_page_lastpage_button)

    def get_users_page_nextpage_button(self):
        return self.weh.get_element(self.users_page_nextpage_button)

    def get_users_page_displayName_item(self, username):
        item = {}
        item['XPATH'] = self.users_page_displayName_item['XPATH'] + '"' + username + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_delete_button_portal(self):
        return self.weh.get_element(self.delete_button_portal)

    def get_delete_confirm_yes_item(self):
        return self.weh.get_element(self.delete_confirm_yes_item)

    def get_edit_button_portal(self):
        return self.weh.get_element(self.edit_button_portal)

    def get_edit_users_page_email_text(self, email):
        item = {}
        item['XPATH'] = self.edit_users_page_email_text['XPATH'] + '"' + email + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_edit_users_page_email_input(self):
        return self.weh.get_element(self.edit_users_page_email_input)

    def get_edit_users_page_edit_accept_button(self):
        return self.weh.get_element(self.edit_users_page_edit_accept_button)

    def get_add_customers_page_customername_text(self):
        return self.weh.get_element(self.add_customers_page_customername_text)

    def get_add_customers_page_firstname_text(self):
        return self.weh.get_element(self.add_customers_page_firstname_text)

    def get_add_customers_page_lastname_text(self):
        return self.weh.get_element(self.add_customers_page_lastname_text)

    def get_add_customers_page_adminemail_text(self):
        return self.weh.get_element(self.add_customers_page_adminemail_text)

    def get_add_customers_page_adminpasswored_text(self):
        return self.weh.get_element(self.add_customers_page_adminpassword_text)

    def get_add_customers_page_submit_button(self):
        return self.weh.get_element(self.add_customers_page_submit_button)

    def get_customers_page_filter_text(self):
        return self.weh.get_element(self.customers_page_filter_text)




