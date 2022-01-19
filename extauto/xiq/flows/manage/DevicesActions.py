import re
from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from xiq.flows.common.Navigator import Navigator
import xiq.flows.common.ToolTipCapture as tool_tip
from xiq.flows.common.DeviceCommon import DeviceCommon
from xiq.flows.manage.Devices import Devices
from xiq.elements.DevicesWebElements import DevicesWebElements
from xiq.elements.DialogWebElements import DialogWebElements
from xiq.elements.DeviceActions import DeviceActions
from xiq.elements.DeviceUpdate import DeviceUpdate
from xiq.elements.SwitchWebElements import SwitchWebElements


class DevicesActions:
    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.devices_web_elements = DevicesWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.switch_web_elements = SwitchWebElements()

        self.navigator = Navigator()
        self.device_actions = DeviceActions()
        self.device_update = DeviceUpdate()
        self.device_common = DeviceCommon()
        self.device_common = DeviceCommon()
        self.devices = Devices()

        self.screen = Screen()
        self.robot_built_in = BuiltIn()

    def clear_audit_mismatch_on_device(self, device_serial):
        """
        - Assumes that already navigated to Manage --> Devices
        - This method Clear Audit Mismatch for the device matching the serial(s)
        - Keyword Usage:
         - ``clear_audit_mismatch_on_device  ${DEVICE_SERIAL}``

        :param device_serial: device serial number
        :return: None
        """
        self.utils.print_info("Clearing Device Audit Mismatch with serial: ", device_serial)

        if self.devices.select_ap(device_serial):
            self.utils.print_info("Selecting Actions button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())
            sleep(2)

            self.utils.print_info("Selecting Clear Audit Mismatch menu item")
            self.auto_actions.click(self.device_actions.get_device_actions_clear_audit_mismatch_menu())
            sleep(2)

            return 1
        else:
            self.utils.print_info("Unable to Clear Audit Mismatch On Device ")
            return -1

    def perform_device_factory_reset(self, *device_list):
        """
        - This Keyword performs factory reset on AP
        - Navigate to Manage --> Device
        - Select the device row based on the passed device serial
        - Click on Utilities --> Status --> Reset Device to Default
        - Handles device reset pop up and validates reset dialogue box message.
        - Keyword Usage:
         - ``Perform Device Factory Reset     ${AP1_SERIAL}   ${AP2_SERIAL}``

        :param device_list: serial numbers of the devices
        :return: 1 if Reset is Successful else -1
        """
        self.utils.print_info("Device serial :", *device_list)
        self.select_device_utilities(*device_list)
        sleep(2)
        self.utils.print_info("Hovering to Device reset button...")

        device_list_len = len(device_list)
        self.utils.print_info("device_list_len :", device_list_len)

        if device_list_len > 1:
            device_reset_button = self.device_actions.get_multiple_device_reset_button()
        else:
            device_reset_button = self.device_actions.get_single_device_reset_button()

        self.auto_actions.move_to_element(device_reset_button)
        self.screen.save_screen_shot()
        sleep(1)

        self.utils.print_info("Clicking on Device reset button")
        self.auto_actions.click(device_reset_button)
        sleep(2)

        reset_msg = self.device_actions.get_device_reset_warning_msg().text
        self.utils.print_info("Reset warning message:  ", reset_msg)
        self.utils.print_info("Confirming to device reset by hitting 'yes' button ")
        self.auto_actions.click(self.device_actions.get_device_reset_yes_dialog())
        self.utils.print_info("Device reset dialogue box takes more than 5 seconds"
                              " to load, so giving adequate sleep of 10 seconds")
        sleep(10)
        diag_msg = self.device_actions.get_device_reset_dialog_box_msg().text
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("dialogue box message :", diag_msg)
        reset_list = self.validate_reset_dialogue_box_msg(diag_msg, *device_list)
        self.utils.print_info("Return values of failed and success list :", reset_list)
        self.utils.print_info("Closing the Reset dialogue box")
        self.auto_actions.click(self.device_actions.get_device_reset_close_dialog())
        self.screen.save_screen_shot()
        sleep(1)
        return reset_list

    def validate_reset_dialogue_box_msg(self, diag_msg, *device_list):
        """
        - This Keyword validates reset status of dialogue box message
        - Validates whether the device is success or fail in performing reset
        - Assumes already in dialogue box pop up page
        :param diag_msg: dialogue box message
        :param device_list: Device list
        :return: Returns failed list and success device list
        """
        success_list = []
        failed_list = []

        for device in device_list:
            if device not in diag_msg:
                self.utils.print_info("Reset operation not performed on device ", device)
                failed_list.append(device)
            else:
                self.utils.print_info("Device serial found in diag msg")
            for line in diag_msg.splitlines():
                if re.search(rf'Failed.*{device}.*not supported', line):
                    self.utils.print_info(line)
                    failed_list.append(device)
                    self.utils.print_info("Failed device list ", failed_list)
                elif 'Success' and device in line:
                    self.utils.print_info(line)
                    success_list.append(device)
                    self.utils.print_info("success_list ", success_list)
        return failed_list, success_list

    def select_device_utilities(self, *device_list):
        """
        - This Keyword selects device utilities
        - Select the device row based on the passed device serial --> clicks on Utilities
        - Keyword Usage:
         - ``Select Device Utilities   ${DEVICE_SERIAL}``

        :param device_list: Device list
        :return: 1 if selecting Utilities is successful
        """
        self.navigator.navigate_to_devices()
        for device in device_list:
            if self.devices.select_device(device_serial=device):
                self.utils.print_info(f"Selected device {device}")
            else:
                self.utils.print_info(f"Unable to select device {device}")
        self.utils.print_info("Clicking on Utilities")
        self.auto_actions.click(self.device_actions.get_device_utilities())
        sleep(2)
        return 1
