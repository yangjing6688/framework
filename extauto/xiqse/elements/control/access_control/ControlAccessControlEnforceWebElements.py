from xiqse.defs.control.access_control.ControlAccessControlEnforceWebElementsDefinitions import ControlAccessControlEnforceWebElementsDefinitions
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.WebElementHandler import WebElementHandler

class ControlAccessControlEnforceWebElements(ControlAccessControlEnforceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def select_enforce_combo(self, menu):
        """
        :return: Menu pick from Control page - This is to expand the dropdown menu
        """
        return self.weh.get_template_element(self.enfoce_combo, element_name=menu)

    def select_nacenforce_combo_menu(self, menu_item):
        """
        :return: Menu pick from NAC enforce
        """
        return self.weh.get_template_element(self.nacenforce_combo_menu, element_name=menu_item)
