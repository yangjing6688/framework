from extauto.iam.defs.IAMWebElementsDefinitions import IAMWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class IAMWebElements(IAMWebElementsDefinitions):

    def __init__(self):
        self.weh = WebElementHandler()

    def get_login_page_sso_button(self):
        return self.weh.get_element(self.login_page_sso_button)

    def get_saml_login_page_username_text(self):
        return self.weh.get_element(self.saml_login_page_username_text)

    def get_saml_login_page_continue_button(self):
        return self.weh.get_element(self.saml_login_page_continue_button)

    def get_saml_login_page_selecting_your_organization_title(self):
        return self.weh.get_element(self.saml_login_page_selecting_your_organization_title)

    def get_saml_login_page_idp_server_item(self, username):
        item = {}
        item['XPATH'] = self.saml_login_page_idp_server_item['XPATH'] + '"' + username + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_adfs_page_username_text(self):
        return self.weh.get_element(self.adfs_page_username_text)

    def get_adfs_page_password_text(self):
        return self.weh.get_element(self.adfs_page_password_text)

    def get_adfs_page_submit_button(self):
        return self.weh.get_element(self.adfs_page_submit_button)

    def get_xiq_page_account_username_title(self, username):
        item = {}
        item['XPATH'] = self.xiq_page_account_username_title['XPATH'] + '"' + username + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_xiq_page_account_orgname_title(self, orgname):
        item = {}
        item['XPATH'] = self.xiq_page_account_username_title['XPATH'] + '"' + orgname + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_user_account_nav(self):
        return self.weh.get_element(self.user_account_nav)

    def get_logout_link(self):
        menu = self.weh.get_element(self.logout_user_menu_item)
        menu_items = self.weh.get_elements(self.menu_item, menu)
        for menu_item in menu_items:
            if 'LOGOUT' in menu_item.text.upper():
                return menu_item

    def get_add_idp_button(self):
        return self.weh.get_element(self.iam_idp_page_add_idp_button)

    def get_iam_idp_page_domain_text(self):
        return self.weh.get_element(self.iam_idp_page_domain_text)

    def get_iam_idp_page_description_text(self):
        return self.weh.get_element(self.iam_idp_page_description_text)

    def get_iam_idp_page_continue_button_1(self):
        return self.weh.get_element(self.iam_idp_page_continue_button_1)


    def get_iam_idp_page_continue_button_2(self):
        return self.weh.get_element(self.iam_idp_page_continue_button_2)

    def get_iam_idp_page_import_from_url_button(self):
        return self.weh.get_element(self.iam_idp_page_import_from_url_button)

    def get_iam_idp_page_idp_metadata_url_text(self):
        return self.weh.get_element(self.iam_idp_page_idp_metadata_url_text)

    def get_iam_idp_page_import_button(self):
        return self.weh.get_element(self.iam_idp_page_import_button)

    def get_iam_idp_page_email_text(self):
        return self.weh.get_element(self.iam_idp_page_email_text)

    def get_iam_idp_page_entity_id(self):
        return self.weh.get_element(self.iam_idp_page_entity_id)

    def get_iam_idp_page_sso_binding(self):
        return self.weh.get_element(self.iam_idp_page_sso_binding)

    def get_iam_idp_page_slo_binding(self):
        return self.weh.get_element(self.iam_idp_page_slo_binding)

    def get_iam_idp_page_sloResponse_binding(self):
        return self.weh.get_element(self.iam_idp_page_sloResponse_binding)

    def get_iam_idp_page_group_text(self):
        return self.weh.get_element(self.iam_idp_page_group_text)

    def get_iam_idp_page_default_group_dropdown(self):
        return self.weh.get_element(self.iam_idp_page_default_group_dropdown)

    def get_iam_idp_page_default_group_item(self, default_group):
        item = {}
        item['XPATH'] = self.iam_idp_page_default_group_item['XPATH'] + '"' + default_group + '"' + ')]'
        item['wait_for'] = 3
        return item
    def get_iam_idp_page_save_button(self):
        return self.weh.get_element(self.iam_idp_page_save_button)

    def get_iam_page_list_idp(self,idp_name):
        item = {}
        item['XPATH'] = self.iam_page_list_idp['XPATH'] + '"' + idp_name + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_iam_console_link(self):
        return self.weh.get_element(self.iam_console_link)


