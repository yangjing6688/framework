from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.compliance.ComplianceWebElements import ComplianceWebElements


class XIQSE_Compliance(ComplianceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_compliance_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Compliance page
         - Keyword Usage
          - ``XIQSE Compliance Select Tab    Dashboard``
          - ``XIQSE Compliance Select Tab    Audit Tests``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Dashboard":
            the_tab = self.get_dashboard_tab()
        elif tab_name == "Audit Tests":
            the_tab = self.get_audit_tests_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Compliance page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Compliance page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_compliance_select_dashboard_tab(self):
        """
         - This keyword selects the Dashboard tab of the Compliance page
         - Keyword Usage
          - ``XIQSE Compliance Select Dashboard Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_compliance_select_tab("Dashboard")

    def xiqse_compliance_select_audit_tests_tab(self):
        """
         - This keyword selects the Audit Tests tab of the Compliance page
         - Keyword Usage
          - ``XIQSE Compliance Select Audit Tests Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_compliance_select_tab("Audit Tests")
