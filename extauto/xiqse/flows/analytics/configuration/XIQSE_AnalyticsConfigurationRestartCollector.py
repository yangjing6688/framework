from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.analytics.configuration.AnalyticsConfigurationRestartCollectorWebElements import AnalyticsConfigurationRestartCollectorWebElements


class XIQSE_AnalyticsConfigurationRestartCollector(AnalyticsConfigurationRestartCollectorWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_restart_collector_dialog_click_yes(self):
        """
        - This keyword clicks Yes in the Restart Collector dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Restart Collector Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_restart_collector_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking Yes button")
            self.auto_actions.click(yes_btn)
            sleep(20)
        else:
            self.utils.print_info("Could not find Yes button in Restart Collector dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_restart_collector_dialog_click_no(self):
        """
        - This keyword clicks No in the Restart Collector dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Restart Collector Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_restart_collector_no_button()
        if no_btn:
            self.utils.print_info("Clicking No button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find No button in Restart Collector dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_close_restart_collector_error_dialog(self):
        """
        - This keyword closes the Restart Collector Error dialog which may appear when an error has occurred while restarting the collector on an engine
        - Keyword Usage
        - ``XIQSE Close Restart Collector Error Dialog``

        :return: 1 if action successful, else -1
        """
        ret_val = 1

        the_dialog = self.get_restart_collector_error_dialog()
        if the_dialog and the_dialog.is_displayed:
            ok_btn = self.get_restart_collector_error_dialog_ok_button()
            if ok_btn:
                self.utils.print_info("An error has occurred while restarting collector on the engine.  Closing 'Restart Collector Error' dialog.")
                self.auto_actions.click(ok_btn)
                sleep(1)
            ret_val = -1
        else:
            self.utils.print_info("'Restart Collector Error' dialog not displayed")

        return ret_val
