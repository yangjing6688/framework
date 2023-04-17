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
        item['XPATH'] = self.xiq_page_account_username_title['XPATH'] + '"' + username + '"' + ')]'
        item['wait_for'] = 3
        return item

    def get_adfs_page_username_text(self):
        return self.weh.get_element(self.adfs_page_username_text)

    def get_adfs_page_password_text(self):
        return self.weh.get_element(self.adfs_page_password_text)

    def get_adfs_page_submit_button(self):
        return self.weh.get_element(self.adfs_page_password_button)

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
