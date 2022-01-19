from xiqse.defs.control.access_control.ControlAccessControlPanelWebElementsDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class ControlAccessControlPanelWebElements(ControlAccessControlPanelWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def get_nac_status_ok(self):
        """
        :return: 'ID" for NAC status with OK text in the panel
        """
        return self.weh.get_element(self.nac_status_ok)

    def get_nac_status(self):
        """
        :return: 'ID" for NAC status in the panel
        """
        return self.weh.get_element(self.nac_status)

    def get_nac_unlicensed_text(self):
        """
        :return: 'ID" for NAC unlicensed text in the panel
        """
        return self.weh.get_element(self.nac_unlicensed_text)

    def get_nac_validlicensed_text(self):
        """
        :return: 'ID" for Valid Virtual Appliance License text in the panel
        """
        return self.weh.get_element(self.nac_validlicensed_text)

    def select_row_grid_by_ip(self, ipaddr):
        """
        :return: Using IP address (name), select a row in the right grid
        """
        return self.weh.get_template_element(self.row_grid_by_ip, element_name=ipaddr)



