from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.access_control.ControlAccessControlCommonWebElements import ControlAccessControlCommonWebElements
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class XIQSE_AccessControlCommon(ControlAccessControlCommonWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.ac_common_els = ControlAccessControlCommonWebElements()
        self.screen = Screen()

    def xiqse_control_click_button(self, buttonname):
        """
        This is a general keyword in NAC to click on a button within Dialog.
        This is using data-ref="btnInnerEl" with Button Name
        - Keyword Usage
            XIQSE CONTROL CLICK BUTTON  Close
        :return: XXX if action was successful, else -1
        """
        ret_val = -1
        btn = self.ac_common_els.click_innerel_button(buttonname)
        if btn:
            self.utils.print_info(f"Clicking {buttonname} ...")
            self.auto_actions.click(btn)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select {buttonname} menu ")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_control_select_tab_inpanel(self, tabpanel):
        """
        This is a general keyword in Access Control to click on a tab within panel.
        - Keyword Usage
            XIQSE CONTROL SELECT TAB INPANEL  Switches
            XIQSE CONTROL SELECT TAB INPANEL  End-Systems
            XIQSE CONTROL SELECT TAB INPANEL  Details
        :return: XXX if action was successful, else -1
        """
        ret_val = -1
        tab = self.ac_common_els.select_tab_panel(tabpanel)
        if tab:
            self.utils.print_info(f"Clicking {tabpanel} ...")
            self.auto_actions.click(tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select {tabpanel} menu ")
            self.screen.save_screen_shot()

        return ret_val
