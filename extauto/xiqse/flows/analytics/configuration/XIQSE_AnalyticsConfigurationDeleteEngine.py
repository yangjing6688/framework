from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.analytics.configuration.AnalyticsConfigurationDeleteEngineWebElements import AnalyticsConfigurationDeleteEngineWebElements

class XIQSE_AnalyticsConfigurationDeleteEngine(AnalyticsConfigurationDeleteEngineWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_delete_engine_dialog_click_yes(self):
        """
        - This keyword clicks Yes in the Delete Engine dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Delete Engine Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        yes_btn = self.get_delete_engine_yes_button()
        if yes_btn:
            self.utils.print_info("Clicking Yes button")
            self.auto_actions.click(yes_btn)
        else:
            self.utils.print_info("Could not find Yes button in Delete Engine dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_engine_dialog_click_no(self):
        """
        - This keyword clicks No in the Delete Engine dialog.
        - It is assumed the dialog is already opened.
        - Keyword Usage
        - ``XIQSE Delete Engine Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        no_btn = self.get_delete_engine_no_button()
        if no_btn:
            self.utils.print_info("Clicking No button")
            self.auto_actions.click(no_btn)
        else:
            self.utils.print_info("Could not find No button in Delete Engine dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
