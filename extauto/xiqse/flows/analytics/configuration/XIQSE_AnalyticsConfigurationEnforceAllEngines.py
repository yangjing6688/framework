from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.analytics.configuration.AnalyticsConfigurationEnforceAllEnginesWebElements import AnalyticsConfigurationEnforceAllEnginesWebElements


class XIQSE_AnalyticsConfigurationEnforceAllEngines(AnalyticsConfigurationEnforceAllEnginesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_enforce_all_engines_dialog_click_yes(self):
        """
        - This keyword clicks Yes in the Enforce Engines dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Enforce All Engines Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_enforce_all_engines_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking Yes button")
            self.auto_actions.click(yes_btn)
            sleep(10)
        else:
            self.utils.print_info("Could not find Yes button in Enforce Engines dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_enforce_all_engines_dialog_click_no(self):
        """
        - This keyword clicks No in the Enforce Engines dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Enforce All Engines Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_enforce_all_engines_no_button()
        if no_btn:
            self.utils.print_info("Clicking No button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find No button in Enforce Engines dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_close_enforce_engines_error_dialog(self):
        """
        - This keyword closes the Enforce Engines Error dialog which may appear when an error has occurred while enforcing an engine
        - Keyword Usage
        - ``XIQSE Close Enforce Engines Error Dialog``

        :return: 1 if action successful, else -1
        """
        ret_val = 1

        the_dialog = self.get_enforce_engines_error_dialog()
        if the_dialog and the_dialog.is_displayed:
            ok_btn = self.get_enforce_engines_error_dialog_ok_button()
            if ok_btn:
                self.utils.print_info("An error has occurred while enforcing all engines.  Closing 'Enforce Engines Error' dialog.")
                self.auto_actions.click(ok_btn)
                sleep(1)
            ret_val = -1
        else:
            self.utils.print_info("'Enforce Engines Error' dialog not displayed")

        return ret_val
