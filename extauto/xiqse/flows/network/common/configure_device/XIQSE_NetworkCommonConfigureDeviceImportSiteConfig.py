from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.common.configure_device.NetworkCommonConfigureDeviceImportSiteConfigWebElements import NetworkCommonConfigureDeviceImportSiteConfigWebElements


class XIQSE_NetworkCommonConfigureDeviceImportSiteConfig(NetworkCommonConfigureDeviceImportSiteConfigWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_answer_import_site_configuration_question(self, the_answer="No"):
        """
        - This keyword clicks Yes or No in the Import Site Configuration dialog, which is seen when changing the
        - Default Site field on the Device tab of the Configure Device dialog.
        - Keyword Usage
        - ``XIQSE Answer Import Site Configuration Question``

        :param the_answer:  Specifies how to answer the question in the dialog - Yes or No
        :return: 1 if action was successful, 2 if dialog was not displayed, else -1
        """
        ret_val = -1

        import_dlg = self.get_import_site_configuration_dialog()
        if import_dlg:
            self.utils.print_info(f"Import Site Configuration question dialog was displayed; answer with '{the_answer}'")
            if the_answer.upper() == "NO":
                ret_val = self.xiqse_import_site_configuration_dialog_click_no()
            elif the_answer.upper() == "YES":
                ret_val = self.xiqse_import_site_configuration_dialog_click_yes()
            else:
                self.utils.print_info(f"Unknown Import Site Configuration answer '{the_answer}' - enter Yes or No")
        else:
            self.utils.print_info("Import Site Configuration question dialog was not displayed")
            ret_val = 2

        return ret_val

    def xiqse_import_site_configuration_dialog_click_yes(self):
        """
        - This keyword clicks 'Yes' in the Import Site Configuration dialog, which is seen when changing the
        - Default Site field on the Device tab of the Configure Device dialog.
         -
        - It is assumed the Import Site Configuration question dialog is already open.
         -
        - Keyword Usage
        - ``XIQSE Import Site Configuration Dialog Click Yes``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_btn = self.get_import_site_configuration_dialog_yes_button()
        if the_btn:
            self.utils.print_info("Clicking 'Yes'")
            self.auto_actions.click(the_btn)
        else:
            self.utils.print_info("Could not find 'Yes' button in Import Site Configuration dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_import_site_configuration_dialog_click_no(self):
        """
        - This keyword clicks 'No' in the Import Site Configuration dialog, which is seen when changing the
        - Default Site field on the Device tab of the Configure Device dialog.
         -
        - It is assumed the Import Site Configuration question dialog is already open.
         -
        - Keyword Usage
        - ``XIQSE Import Site Configuration Dialog Click No``

        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        the_btn = self.get_import_site_configuration_dialog_no_button()
        if the_btn:
            self.utils.print_info("Clicking 'No'")
            self.auto_actions.click(the_btn)
        else:
            self.utils.print_info("Could not find 'No' button in Import Site Configuration dialog")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val
