from extauto.common.Utils import Utils
from extauto.common.Cli import *
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from time import sleep
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesRestartDeviceWebElements import NetworkDevicesDevicesRestartDeviceWebElements


class XIQSE_NetworkDevicesDevicesRestartDevice(NetworkDevicesDevicesRestartDeviceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.view_el = NetworkDevicesDevicesRestartDeviceWebElements()

    def xiqse_click_start_restart_button(self):
        """
        - This keyword clicks the "Start" button on the Restart Device menu to begin restarting the device selected
        - It assumes the Restart Device dialog is already open
        - Keyword Usage:
        - 'XIQSE Click Start Restart Button'
        :return: 1 if action is successful, else -1
        """

        ret_val = 1

        start_restart = self.get_start_restart_button_item()
        if start_restart:
            self.utils.print_info("Clicking 'Start' button")
            self.auto_actions.click(start_restart)

        else:
            ret_val = -1
            self.utils.print_info("Unable to find 'Start' button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_click_start_restart_yes_button(self):
        """
        - This Keyword clicks the "Yes" button to begin the switch restart
        - Keyword usage:
        - 'XIQSE Click Start Restart Yes Button'
        :return: 1 if action is successful, else -1
        """

        ret_val = 1

        start_yes = self.get_start_restart_yes_button()
        if start_yes:
            self.utils.print_info("Clicking 'Yes' Button")
            self.auto_actions.click(start_yes)
            ret_val = self.xiqse_wait_for_restart_operation_to_complete()
        else:
            ret_val = -1
            self.utils.print_info("Unable to find 'Yes' button to start switch restart")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_for_restart_operation_to_complete(self, seconds=900):
        """
        - This keyword waits for the "Restart Operation Complete" element to appear before continuing
        - Keyword Usage
        - ''XIQSE Wait For Restart Operation Complete''
        :param retry_duration: amount of time to wait in between each check for the refresh to be complete
        :param retry_count: Number of times for the check to be complete
        :return: 1 if action was successful, else -1
        """

        self.utils.print_info("wait_until_appears")
        while seconds > 0:
            time.sleep(5)
            self.utils.print_info("get element")
            element = self.get_restart_operation_complete()
            if element:
                self.utils.print_info("Restart completed")
                return 1
            else:
                seconds = seconds - 5

        self.utils.print_info("Restart failed")
        self.screen.save_screen_shot()
        return -1

    def xiqse_click_restart_devices_close_button(self):
        """
        - This keyword clicks the "Close" button on the Restart Device menu
        - It assumes the Restart Device dialog is already open
        - Keyword Usage:
        - 'XIQSE Click Restart Devices Close Button'
        :return: 1 if action is successful, else -1
        """

        ret_val = 1

        close_restart = self.get_restart_device_close_button()
        if close_restart:
            self.utils.print_info("Clicking 'Close' button")
            self.auto_actions.click(close_restart)
        else:
            ret_val = -1
            self.utils.print_info("Unable to find 'Close' button")
            self.screen.save_screen_shot()

        return ret_val