from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.admin.device_types.AdminDeviceTypesWebElements import AdminDeviceTypesWebElements


class XIQSE_AdminDeviceTypes(AdminDeviceTypesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_device_types_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Administration> Device Types page
        - Keyword Usage
        - ``XIQSE Device Types Select Tab    Detection and Profiling``
        - ``XIQSE Device Types Select Tab    MAC OUI Vendors``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Detection and Profiling":
            the_tab = self.get_detection_and_profiling_tab()
        elif tab_name == "MAC OUI Vendors":
            the_tab = self.get_mac_oui_vendors_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Administration> Device Types page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Administration> Device Types page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_device_types_select_detection_and_profiling_tab(self):
        """
        - This keyword selects the Detection and Profiling tab on the Administration> Device Types page.
        - It is assumed the Administration> Device Types page is currently being displayed.
        - Keyword Usage
        - ``XIQSE Device Types Select Detection and Profiling Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_device_types_select_tab("Detection and Profiling")

    def xiqse_device_types_select_mac_oui_vendors_tab(self):
        """
        - This keyword selects the MAC OUI Vendors tab on the Administration> Device Types page.
        - It is assumed the Administration> Device Types page is currently being displayed.
        - Keyword Usage
        - ``XIQSE Device Types Select MAC OUI Vendors Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_device_types_select_tab("MAC OUI Vendors")
