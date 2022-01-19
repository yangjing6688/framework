from xiqse.defs.control.dashboard.ControlDashboardWebElementsDefinitions import *
from common.AutoActions import *
from common.WebElementHandler import *

class ControlDashboardWebElements(ControlDashboardWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def select_dashboard_combo(self, menu):
        """
        :return: Menu pick from Dashboard page - This is to expand the dropdown menu
        """
        return self.weh.get_template_element(self.dashboard_combo, element_name=menu)

    def select_dashboard_combo_menu(self, menu_item):
        """
        :return: Menu pick from Dashboard page
        """
        return self.weh.get_template_element(self.dashboard_combo_menu, element_name=menu_item)

    def get_id_for_overview_label(self, labeltxt):
        """
        :return: 'This is to get the element ID using label text in the Control Dashboard Overview panel'
        """
        return self.weh.get_template_element(self.id_for_overview_label, element_name=labeltxt)
