from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.access_control.ControlAccessControlEnforceWebElements import ControlAccessControlEnforceWebElements
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class XIQSE_AccessControlEnforce(ControlAccessControlEnforceWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.ac_enforce_els = ControlAccessControlEnforceWebElements()
        self.screen = Screen()

    def xiqse_expand_control_enforce_dropdown(self):
        """
        This is a keyword to expand the dropdown menu in Control Access Control page
        - Keyword Usage
            XIQSE EXPAND CONTROL ENFORCE DROPDOWN
        :return: XXX if action was successful, else -1
        """
        ret_val = -1
        enforce_menu = self.ac_enforce_els.select_enforce_combo("Enforce")
        if enforce_menu:
            self.utils.print_info("Selecting Enforce dropdown in Console ...")
            self.auto_actions.click(enforce_menu)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info("Unable to select dropdown menu ")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_control_enforce_dropdown_menu(self, combomenu):
        """
        This is a keyword to select the dropdown menu in Control Access Control page
        - Keyword Usage
            XIQSE EXPAND CONTROL ENFORCE DROPDOWN   All...
        :return: XXX if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.ac_enforce_els.select_nacenforce_combo_menu(combomenu)
        if the_menu:
            self.utils.print_info(f"Selecting {combomenu} menu...")
            self.auto_actions.click(the_menu)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select {combomenu} menu... ")
            self.screen.save_screen_shot()
        return ret_val
