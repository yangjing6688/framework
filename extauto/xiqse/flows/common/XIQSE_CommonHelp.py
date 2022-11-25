from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonHelpWebElements import CommonHelpWebElements


class XIQSE_CommonHelp(CommonHelpWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_close_help_panel(self):
        """
        - This keyword closes the Context Help panel, if it is open
        - Keyword Usage
        - ``XIQSE Close Help Panel``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        the_panel = self.get_help_panel()
        if the_panel:
            panel_expanded = the_panel.get_attribute("aria-expanded")
            if panel_expanded == "true":
                panel_title = self.get_help_panel_title()
                if panel_title:
                    self.utils.print_info("Closing Help Panel")
                    self.auto_actions.click(panel_title)
                    sleep(2)
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to find Help panel title")
            else:
                self.utils.print_info("Help panel is already closed")
                ret_val = 1
        else:
            self.utils.print_info("Unable to find Help panel")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
