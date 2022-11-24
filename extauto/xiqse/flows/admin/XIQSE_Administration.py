from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.AdministrationWebElements import AdministrationWebElements


class XIQSE_Administration(AdministrationWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_admin_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Tab    Profiles``
        - ``XIQSE Administration Select Tab    Users``
        - ``XIQSE Administration Select Tab    Server Information``
        - ``XIQSE Administration Select Tab    Certificates``
        - ``XIQSE Administration Select Tab    Options``
        - ``XIQSE Administration Select Tab    Device Types``
        - ``XIQSE Administration Select Tab    Backup/Restore``
        - ``XIQSE Administration Select Tab    Diagnostics``
        - ``XIQSE Administration Select Tab    Client API Access``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Profiles":
            the_tab = self.get_profiles_tab()
        elif tab_name == "Users":
            the_tab = self.get_users_tab()
        elif tab_name == "Server Information":
            the_tab = self.get_server_information_tab()
        elif tab_name == "Licenses":
            the_tab = self.get_licenses_tab()
        elif tab_name == "Certificates":
            the_tab = self.get_certificates_tab()
        elif tab_name == "Options":
            the_tab = self.get_options_tab()
        elif tab_name == "Device Types":
            the_tab = self.get_device_types_tab()
        elif tab_name == "Backup/Restore" or tab_name == "Backup Restore":
            the_tab = self.get_backup_restore_tab()
        elif tab_name == "Diagnostics":
            the_tab = self.get_diagnostics_tab()
        elif tab_name == "Client API Access":
            the_tab = self.get_client_api_access_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Administration page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Administration page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_admin_select_profiles_tab(self):
        """
        - This keyword selects the Profiles tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Profiles Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Profiles")

    def xiqse_admin_select_users_tab(self):
        """
        - This keyword selects the Users tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Users Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Users")

    def xiqse_admin_select_server_information_tab(self):
        """
        - This keyword selects the Server Information tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Server Information Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Server Information")

    def xiqse_admin_select_licenses_tab(self):
        """
        - This keyword selects the Licenses tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Licenses Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Licenses")

    def xiqse_admin_select_certificates_tab(self):
        """
        - This keyword selects the Certificates tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Certificates Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Certificates")

    def xiqse_admin_select_options_tab(self):
        """
        - This keyword selects the Options tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Options Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Options")

    def xiqse_admin_select_device_types_tab(self):
        """
        - This keyword selects the Device Types tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Device Types Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Device Types")

    def xiqse_admin_select_backup_restore_tab(self):
        """
        - This keyword selects the Backup/Restore tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Backup Restore Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Backup/Restore")

    def xiqse_admin_select_diagnostics_tab(self):
        """
        - This keyword selects the Diagnostics tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Diagnostics Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Diagnostics")

    def xiqse_admin_select_client_api_access_tab(self):
        """
        - This keyword selects the Client API Access tab of the Administration page
        - Keyword Usage
        - ``XIQSE Administration Select Client API Access Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_admin_select_tab("Client API Access")
