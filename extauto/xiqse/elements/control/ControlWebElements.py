from extauto.common.WebElementHandler import *
from xiqse.defs.control.ControlWebElementsDefinitions import *


class ControlWebElements(ControlWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_dashboard_tab(self):
        """
        :return: Dashboard Tab on the Control page
        """
        return self.weh.get_element(self.dashboard_tab)

    def get_policy_tab(self):
        """
        :return: Policy Tab on the Control page
        """
        return self.weh.get_element(self.policy_tab)

    def get_access_control_tab(self):
        """
        :return: Access Control Tab on the Control page
        """
        return self.weh.get_element(self.access_control_tab)

    def get_end_systems_tab(self):
        """
        :return: End-Systems Tab on the Control page
        """
        return self.weh.get_element(self.end_systems_tab)

    def get_reports_tab(self):
        """
        :return: Reports Tab on the Control page
        """
        return self.weh.get_element(self.reports_tab)

    def get_engines_title_header(self, title):
        """
        :return: All Policy / Engines Tabs on the Control page> Title Header in the tree
        """

        if title == 'Configuration':
            engines_title_header_def = {'XPATH': '//div[contains(@id, "nacConfigConfigTree") and contains(text(),"' + title + '")]',
            'wait_for': 10}

        elif title == 'Group Editor':
            engines_title_header_def = {'XPATH': '//div[contains(@id, "nacConfigDeltaGroupTree") and contains(text(),"' + title + '")]',
            'wait_for': 10}

        elif title == 'Engines':
            engines_title_header_def = {'XPATH': '//div[contains(@id, "nacConfigApplianceTree") and contains(text(),"' + title + '")]',
            'wait_for': 10}

        elif title == 'VLANs' or title == 'Class of Service' or title == 'Network Resources' or title == 'Roles/Services':
            engines_title_header_def = {'XPATH': '//div[contains(@id, "treepanel") and contains(text(),"' + title + '")]',
            'wait_for': 10}

        elif title == 'Devices/Port Groups':
            engines_title_header_def = {'XPATH': '//div[contains(@id, "tabpanel") and contains(text(), "Devices/Port Groups")]',
            'wait_for': 10}

        else:
            self.utils.print_info(f"Unable to find Title")
            self.utils.print_info(title)
            return 0

        return self.weh.get_element(engines_title_header_def)