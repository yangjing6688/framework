from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.compliance.ComplianceWebElementsDefinitions import ComplianceWebElementsDefinitions


class ComplianceWebElements(ComplianceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_dashboard_tab(self):
        """
        :return: Dashboard Tab on the Compliance page
        """
        return self.weh.get_element(self.dashboard_tab)

    def get_audit_tests_tab(self):
        """
        :return: Audit Tests Tab on the Compliance page
        """
        return self.weh.get_element(self.audit_tests_tab)
