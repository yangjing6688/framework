from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.control.ControlWebElements import ControlWebElements


class XIQSE_Control(ControlWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.add_control_els = ControlWebElements()
        self.screen = Screen()

    def xiqse_control_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Control page
         - Keyword Usage
          - ``XIQSE Control Select Tab    Dashboard``
          - ``XIQSE Control Select Tab    Policy``
          - ``XIQSE Control Select Tab    Access Control``
          - ``XIQSE Control Select Tab    End-Systems``
          - ``XIQSE Control Select Tab    Reports``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Dashboard":
            the_tab = self.get_dashboard_tab()
        elif tab_name == "Policy":
            the_tab = self.get_policy_tab()
        elif tab_name == "Access Control":
            the_tab = self.get_access_control_tab()
        elif tab_name == "End-Systems" or tab_name == "End Systems":
            the_tab = self.get_end_systems_tab()
        elif tab_name == "Reports":
            the_tab = self.get_reports_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Control page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Control page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_control_select_dashboard_tab(self):
        """
         - This keyword selects the Dashboard tab of the Control page
         - Keyword Usage
          - ``XIQSE Control Select Dashboard Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_control_select_tab("Dashboard")

    def xiqse_control_select_policy_tab(self):
        """
         - This keyword selects the Policy tab of the Control page
         - Keyword Usage
          - ``XIQSE Control Select Policy Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_control_select_tab("Policy")

    def xiqse_control_select_access_control_tab(self):
        """
         - This keyword selects the Access Control tab of the Control page
         - Keyword Usage
          - ``XIQSE Control Select Access Control Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_control_select_tab("Access Control")

    def xiqse_control_select_end_systems_tab(self):
        """
         - This keyword selects the End Systems tab of the Control page
         - Keyword Usage
          - ``XIQSE Control Select End systems Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_control_select_tab("End-Systems")

    def xiqse_control_select_reports_tab(self):
        """
         - This keyword selects the Reports tab of the Control page
         - Keyword Usage
          - ``XIQSE Control Select Reports Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_control_select_tab("Reports")

    def xiqse_control_select_title_header(self, title):
        """
         - This keyword selects the title header on the Control> Policy or Access Control tab.
         - You need to be in the correct page (i.e. Policy or Access Control) to use this keyword.
         - Keyword Usage
          - ``XIQSE Control Select Title Header   ${TITLE Header}``
          -  Examples:
                For Policy,
                    XIQSE Control Select Title Header     Roles/Services
                    XIQSE Control Select Title Header     Class of Service
                    XIQSE Control Select Title Header     VLANs
                    XIQSE Control Select Title Header     Network Resources
                    XIQSE Control Select Title Header     Devices/Port Groups
                For Access Control
                    XIQSE Control Select Title Header     Configuration
                    XIQSE Control Select Title Header     Group Editor
                    XIQSE Control Select Title Header     Engines

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.add_control_els.get_engines_title_header(title)
        if the_node:
            self.utils.print_info(f"Selecting {title} title header...")
            self.auto_actions.click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select {title} title header")
            self.screen.save_screen_shot()
        return ret_val
