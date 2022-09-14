from a3.defs.NavigatorWebElementDefinitions import *
from common.AutoActions import *
from common.WebElementHandler import *
from time import sleep


class NavigatorWebElements(NavigatorWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

        self.utils = Utils()

    def get_configuration_tab(self):
        return self.weh.get_element(self.configuration_tab)

    def get_tools_tab(self):
        return self.weh.get_element(self.tools_tab)

    def get_auditing_tab(self):
        return self.weh.get_element(self.auditing_tab)

    def get_clients_tab(self):
        return self.weh.get_element(self.clients_tab)

    def get_policies_access_control(self):
        return self.weh.get_element(self.policies_tab)

    def get_system_configuration(self):
        return self.weh.get_element(self.system_config_tab)

    def get_system_configuration_menu_link(self):
        return self.weh.get_element(self.system_configuration_menu)

    def get_menu_popup_icon(self):
        return self.weh.get_element(self.menu_popup_icon)

    def get_management_menu_popup(self):
        return self.weh.get_element(self.management_menu_popup)
