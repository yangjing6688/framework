from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.control.access_control.ControlAccessControlPanelWebElements import ControlAccessControlPanelWebElements
from common.AutoActions import *
from common.WebElementHandler import *

class XIQSE_AccessControlPanel(ControlAccessControlPanelWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.ac_panel_els = ControlAccessControlPanelWebElements()
        self.screen = Screen()

    def xiqse_get_nac_status_in_panel(self):
        """
         - This keyword gets NAC status via Control> Access Control Tab
         - First you will need to select the NAC appliance in the tree node
         - If NAC status shows 'OK', the keyword is successful and return 1.
         - Keyword Usage
          - XIQSE GET NAC STATUS IN PANEL
        :return: 1 if action was successful, else -1
        """
        ret_val = 1
        nac_status_ok = self.ac_panel_els.get_nac_status_ok()
        if nac_status_ok:
            self.utils.print_info("Found NAC Status OK")
        else:
            self.utils.print_info("Could not find NAC status OK")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_get_nac_status(self):
        """
         - This keyword gets NAC status via Control> Access Control Tab
         - First you will need to select the NAC appliance in the tree node.
         - This keyword returns a status in text format (i.e. OK, Not Reachable and etc)
         - Keyword Usage
          - XIQSE GET NAC STATUS
        :return: nac status text if action was successful, else None
        """
        nac_status_text = None
        nac_status = self.ac_panel_els.get_nac_status()
        if nac_status:
            self.utils.print_info("Found NAC Status")
            return str(nac_status.text)
        else:
            self.utils.print_info("Could not find NAC status")
            self.screen.save_screen_shot()

        return nac_status_text

    def is_xiqse_nac_unlicensed(self):
        ret_value = -1
        unlicensed_text = self.ac_panel_els.get_nac_unlicensed_text()
        if unlicensed_text:
            self.utils.print_info("Found Unlicensed Virtual Appliance")
            ret_value = 1
        else:
            self.utils.print_info("Unable to find Unlicensed message")
            self.screen.save_screen_shot()

        return ret_value

    def is_xiqse_nac_license_valid(self):
        ret_value = -1
        validlicensed_text = self.ac_panel_els.get_nac_validlicensed_text()
        if validlicensed_text:
            self.utils.print_info("Found Valid Virtual Appliance License")
            ret_value = 1
        else:
            self.utils.print_info("Unable to find Valid Virtual Appliance License message")
            self.screen.save_screen_shot()

        return ret_value
