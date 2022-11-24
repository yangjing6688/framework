from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.connect.ConnectWebElements import ConnectWebElements


class XIQSE_Connect(ConnectWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_connect_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Connect page
        - Keyword Usage
        - ``XIQSE Connect Select Tab    Configuration``
        - ``XIQSE Connect Select Tab    Diagnostics``
        - ``XIQSE Connect Select Tab    Services API``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Configuration":
            the_tab = self.get_configuration_tab()
        elif tab_name == "Diagnostics":
            the_tab = self.get_diagnostics_tab()
        elif tab_name == "Services API":
            the_tab = self.get_services_api_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Connect page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Connect page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_connect_select_configuration_tab(self):
        """
        - This keyword selects the Configuration tab of the Connect page
        - Keyword Usage
        - ``XIQSE Connect Select Configuration Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_select_tab("Configuration")

    def xiqse_connect_select_diagnostics_tab(self):
        """
        - This keyword selects the Diagnostics tab of the Connect page
        - Keyword Usage
        - ``XIQSE Connect Select Diagnostics Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_select_tab("Diagnostics")

    def xiqse_connect_select_services_api_tab(self):
        """
        - This keyword selects the Services API tab of the Connect page
        - Keyword Usage
        - ``XIQSE Connect Select Services API Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_select_tab("Services API")
