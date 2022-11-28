from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.network.devices.site.actions.NetworkDevicesSiteActionsWebElements import NetworkDevicesSiteActionsWebElements


class XIQSE_NetworkDevicesSiteActions(NetworkDevicesSiteActionsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_actions_set_automatically_add_devices(self, value="true"):
        """
        - This keyword sets the selection state of the 'Automatically Add Devices' checkbox on the Network> Devices> Site> Actions Tab
        - It is assumed the view is already navigated to the Actions tab.
        - Keyword Usage
        - ``XIQSE Actions Set Automatically Add Devices``
        - ``XIQSE Actions Set Automatically Add Devices  true``
        - ``XIQSE Actions Set Automatically Add Devices  false``

        :param value:  Indicates whether to select (true) or deselect (false) the checkbox; default is "true"
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_automatically_add_devices_checkbox()
        if the_button:
            if value == "true":
                self.utils.print_info("Enabling 'Automatically Add Devices' checkbox")
                self.auto_actions.enable_check_box(the_button)
            else:
                self.utils.print_info("Disabling 'Automatically Add Devices' checkbox")
                self.auto_actions.disable_check_box(the_button)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the 'Automatically Add Devices' checkbox")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_actions_set_add_trap_receiver(self, value="true"):
        """
        - This keyword sets the selection state of the 'Add Trap Receiver' checkbox on the Network> Devices> Site> Actions Tab
        - It is assumed the view is already navigated to the Actions tab.
        - Keyword Usage
        - ``XIQSE Actions Set Add Trap Receiver``
        - ``XIQSE Actions Set Add Trap Receiver  true``
        - ``XIQSE Actions Set Add Trap Receiver  false``

        :param value:   Indicates whether to select (true) or deselect (false) the checkbox; default is "true"
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_add_trap_receiver_checkbox()
        if the_button:
            if value == "true":
                self.utils.print_info("Enabling 'Add Trap Receiver' checkbox")
                self.auto_actions.enable_check_box(the_button)
            else:
                self.utils.print_info("Disabling 'Add Trap Receiver' checkbox")
                self.auto_actions.disable_check_box(the_button)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the 'Add Trap Receiver' checkbox")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_actions_set_add_syslog_receiver(self, value="true"):
        """
        - This keyword sets the selection state of the 'Add Syslog Receiver' checkbox on the Network> Devices> Site> Actions Tab
        - It is assumed the view is already navigated to the Actions tab.
        - Keyword Usage
        - ``XIQSE Actions Set Add Syslog Receiver``
        - ``XIQSE Actions Set Add Syslog Receiver  true``
        - ``XIQSE Actions Set Add Syslog Receiver  false``

        :param value: Indicates whether to select (true) or deselect (false) the checkbox; default is "true"
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_add_syslog_receiver_checkbox()
        if the_button:
            if value == "true":
                self.utils.print_info("Enabling 'Add Syslog Receiver' checkbox")
                self.auto_actions.enable_check_box(the_button)
            else:
                self.utils.print_info("Disabling 'Add Syslog Receiver' checkbox")
                self.auto_actions.disable_check_box(the_button)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the 'Add Syslog Receiver' checkbox")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_actions_set_add_to_archive(self, value="true"):
        """
        - This keyword sets the selection state of the 'Add to Archive' checkbox on the Network> Devices> Site> Actions Tab
        - It is assumed the view is already navigated to the Actions tab.
        - Keyword Usage
        - ``XIQSE Actions Set Add to Archive``
        - ``XIQSE Actions Set Add to Archive  true``
        - ``XIQSE Actions Set Add to Archive  false``

        :param value: Indicates whether to select (true) or deselect (false) the checkbox;  default is "true"
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_button = self.get_add_to_archive_checkbox()
        if the_button:
            if value == "true":
                self.utils.print_info("Enabling 'Add to Archive' checkbox")
                self.auto_actions.enable_check_box(the_button)
            else:
                self.utils.print_info("Disabling 'Add to Archive' checkbox")
                self.auto_actions.disable_check_box(the_button)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the 'Add to Archive' checkbox")
            self.screen.save_screen_shot()
        return ret_val
