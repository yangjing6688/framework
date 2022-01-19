from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.connect.diagnostics.ConnectDiagnosticsWebElements import ConnectDiagnosticsWebElements


class XIQSE_ConnectDiagnostics(ConnectDiagnosticsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_connect_diagnostics_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Connect> Diagnostics page
         - Keyword Usage
          - ``XIQSE Connect Diagnostics Select Tab    End-Systems``
          - ``XIQSE Connect Diagnostics Select Tab    End-System Groups``
          - ``XIQSE Connect Diagnostics Select Tab    Statistics``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # These tabs are within an iframe, so switch to the iframe
        self.utils.switch_to_iframe_with_attr(self.auto_actions.driver, self.get_iframe_attr())

        if tab_name == "End-Systems":
            the_tab = self.get_end_systems_tab()
        elif tab_name == "End-System Groups":
            the_tab = self.get_end_system_groups_tab()
        elif tab_name == "Statistics":
            the_tab = self.get_statistics_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Connect> Diagnostics page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Connect> Diagnostics page")
            self.screen.save_screen_shot()

        # Switch out of the iframe
        self.utils.switch_to_default(self.auto_actions.driver)

        return ret_val

    def xiqse_connect_diagnostics_select_end_systems_tab(self):
        """
         - This keyword selects the End-Systems tab on the Connect> Diagnostics Tab
         - Keyword Usage
          - ``XIQSE Connect Diagnostics Select End Systems Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_diagnostics_select_tab("End-Systems")

    def xiqse_connect_diagnostics_select_end_system_groups_tab(self):
        """
         - This keyword selects the End-System Groups tab on the Connect> Diagnostics Tab
         - Keyword Usage
          - ``XIQSE Connect Diagnostics Select End System Groups Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_diagnostics_select_tab("End-System Groups")

    def xiqse_connect_diagnostics_select_statistics_tab(self):
        """
         - This keyword selects the Statistics tab on the Connect> Diagnostics Tab
         - Keyword Usage
          - ``XIQSE Connect Diagnostics Select Statistics Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_connect_diagnostics_select_tab("Statistics")
