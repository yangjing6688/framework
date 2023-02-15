from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.reports.ReportsWebElementsDefinitions import ReportsWebElementsDefinitions


class ReportsWebElements(ReportsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_reports_tab(self):
        """
        :return: Reports Tab on the Reports page
        """
        return self.weh.get_element(self.reports_tab)

    def get_custom_report_tab(self):
        """
        :return: Custom Report Tab on the Reports page
        """
        return self.weh.get_element(self.custom_report_tab)

    def get_report_designer_tab(self):
        """
        :return: Report Designer Tab on the Reports page
        """
        return self.weh.get_element(self.report_designer_tab)
