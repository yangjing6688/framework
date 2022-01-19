from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.licenses.AdminLicensesAddLicenseWebElements import AdminLicensesAddLicenseWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable


class XIQSE_AdminLicensesAddLicense(AdminLicensesAddLicenseWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_table = XIQSE_CommonTable()

    def xiqse_add_license_set_license(self, legacy_license):
        """
        - Entering legacy license string in Add License Dialog Text Area.

        :return: returns 1 if action is successful, else -1
        """
        ret_val = -1

        text_area_add_license = self.get_text_area_add_license()
        if text_area_add_license:
            self.utils.print_info("Inserting License in Add License Dialog")
            self.auto_actions.send_keys(text_area_add_license, legacy_license)
            sleep(2)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Text Area In Add License Dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_license_click_ok(self):
        """
        - Clicking OK button in Add License Dialog.

        :return: returns 1 if action is successful, else -1
        """
        ret_val = -1

        ok_button = self.get_ok_button_add_license()
        if ok_button:
            self.utils.print_info("Clicking OK button in Add License Dialog")
            self.auto_actions.click(ok_button)
            sleep(2)
            ret_val = 1
        else:
            self.utils.print_info("Could not find OK button in Add License Dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_license_click_cancel(self):
        """
        - Clicking Cancel button in Add License Dialog.

        :return: returns 1 if action is successful, else -1
        """
        ret_val = -1

        cancel_button = self.get_cancel_button_add_license()
        if cancel_button:
            self.utils.print_info("Clicking Cancel button in Add License Dialog")
            self.auto_actions.click(cancel_button)
            sleep(2)
            ret_val = 1
        else:
            self.utils.print_info("Could not find Cancel button in Add License Dialog")
            self.screen.save_screen_shot()

        return ret_val
