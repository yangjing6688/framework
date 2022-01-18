from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.reports.ReportsWebElements import ReportsWebElements


class XIQSE_Reports(ReportsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_reports_select_tab(self, tab_name):
        """
         - This keyword selects the specified tab of the Reports page
         - Keyword Usage
          - ``XIQSE Reports Select Tab    Reports``
          - ``XIQSE Reports Select Tab    Custom Report``
          - ``XIQSE Reports Select Tab    Report Designer``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Reports":
            the_tab = self.get_reports_tab()
        elif tab_name == "Custom Report":
            the_tab = self.get_custom_report_tab()
        elif tab_name == "Report Designer":
            the_tab = self.get_report_designer_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Reports page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Reports page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_reports_select_reports_tab(self):
        """
         - This keyword selects the Reports tab of the Reports page
         - Keyword Usage
          - ``XIQSE Reports Select Reports Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_reports_select_tab("Reports")

    def xiqse_reports_select_custom_report_tab(self):
        """
         - This keyword selects the Custom Report tab of the Reports page
         - Keyword Usage
          - ``XIQSE Reports Select Custom Report Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_reports_select_tab("Custom Report")

    def xiqse_reports_select_report_designer_tab(self):
        """
         - This keyword selects the Report Designer tab of the Reports page
         - Keyword Usage
          - ``XIQSE Reports Select Report Designer Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_reports_select_tab("Report Designer")
