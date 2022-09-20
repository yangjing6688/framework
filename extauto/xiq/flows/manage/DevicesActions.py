import re
from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.SwitchWebElements import SwitchWebElements


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

    def is_actions_button_enabled(self):
        """
        - This keyword checks if the 'Actions' button is enabled within Manage > Devices view.
        - It is assumed that the Manage > Device view is open.
        - Keyword Usage
         - ``Is Actions Button Enabled``
        :return: True if the button is enabled, False if the button is disabled, else -1
        """
        ret_val = -1
        self.utils.print_info("Checking if 'Actions' button is enabled.")
        actions_btn = self.device_actions.get_device_actions_button()

        if actions_btn:
            btn_state = actions_btn.get_attribute("class")
            self.utils.print_debug(f"'Actions' button Class value: {btn_state}")
            if "btn-disabled" in btn_state:
                self.utils.print_info("The 'Actions' button is disabled.")
                self.screen.save_screen_shot()
                ret_val = False
            else:
                self.utils.print_info("The 'Actions' button is enabled.")
                self.screen.save_screen_shot()
                ret_val = True
        else:
            self.utils.print_info("Could not find the 'Actions' button.")

        return ret_val

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

    def reset_device_to_default(self, *device_list):
        """
        - This Keyword performs factory reset on AP
        - Navigate to Manage --> Device
        - Select the device row based on the passed device serial
        - Click Utilities --> Reset Device to Default
        - Handles device reset pop up and validates reset dialogue box message.
        - Keyword Usage:
         - ``Reset Device to Default     ${AP1_SERIAL}   ${AP2_SERIAL}``
        :param device_list: serial numbers of the devices
        :return: 1 if Reset is Successful else -1
        """
        self.utils.print_info("Device serial(s) : ", device_list)
        select = self.select_device_utilities(*device_list)
        self.screen.save_screen_shot()
        sleep(2)
        if select == -1:
            return ['False'], ['Unable to select any device(s)']

        self.utils.print_info("Click Reset Device to Default.")
        self.auto_actions.click(self.device_actions.get_reset_devices_to_default())
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info(self.device_actions.get_device_reset_warning_msg().text)
        self.utils.print_info("Click 'yes' button ")
        self.auto_actions.click(self.device_actions.get_device_reset_yes_dialog())
        self.utils.print_info("Wait....")
        sleep(10)
        msg = self.device_actions.get_device_reset_dialog_box_msg().text
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("dialogue box message :", msg)
        reset_list = self.validate_reset_dialogue_box_msg(msg, *device_list)
        self.utils.print_info("Return values of failed and success list :", reset_list)
        self.utils.print_info("Closing the Reset dialogue box")
        self.auto_actions.click(self.device_actions.get_device_reset_close_dialog())
        self.screen.save_screen_shot()
        sleep(1)
        return reset_list

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
        select = False
        for device in device_list:
            if self.devices.select_device(device_serial=device):
                self.utils.print_info(f"Selected device {device}")
                select = True
            else:
                self.utils.print_info(f"Unable to select device {device}")

        if select:
            self.utils.print_info("Clicking on Utilities")
            self.auto_actions.click(self.device_actions.get_device_utilities())
            sleep(2)
            return 1
        else:
            return -1

    def is_actions_relaunch_digital_twin_visible(self):
        """
        - This keyword checks if the ACTIONS > Relaunch Digital Twin menu option is visible
        - It is assumed that the Manage > Device window is open and that a device is selected.
        - Keyword Usage
         - ``Is Actions Relaunch Digital Twin Visible``
        :return: 1 if the menu item is displayed, else -1
        """
        ret_val = -1
        self.utils.print_info("Opening Actions menu")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        sleep(2)

        relaunch_link = self.device_actions.get_digital_twin_relaunch_action_menu_item()
        if relaunch_link:
            hidden = relaunch_link.get_attribute("class")
            self.utils.print_debug(f"'Relaunch Digital Twin' menu item Class value: {hidden}")
            if "fn-hidden" in hidden:
                self.utils.print_info("The 'Relaunch Digital Twin' link is not displayed.")
                self.screen.save_screen_shot()
            else:
                self.utils.print_info("The 'Relaunch Digital Twin' link is displayed.")
                self.screen.save_screen_shot()
                ret_val = 1
        else:
            self.utils.print_info("Could not find the 'Actions > Relaunch Digital Twin' link.")

        self.utils.print_info("Closing Actions menu")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        return ret_val

    def actions_relaunch_digital_twin(self, confirm="yes"):
        """
        - This keyword clicks on the ACTIONS > Relaunch Digital Twin
        - It is assumed that the Manage > Device window is open and a Digital Twin device is selected.
        - Keyword Usage
         - ``Actions Relaunch Digital Twin    confirm="no"``
        :param confirm: Click Yes or No button within the confirmation panel
        :return: 1 if action was successful, else -1
        """
        self.utils.print_info("Clicking on Actions Button")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        sleep(2)

        relaunch_link = self.device_actions.get_digital_twin_relaunch_action()
        if relaunch_link:
            hidden = relaunch_link.get_attribute("class")
            self.utils.print_info(f"'Relaunch Digital Twin' menu item Class value: {hidden}")
            if "fn-hidden" in hidden:
                self.utils.print_info("The 'Relaunch Digital Twin' link is not displayed.")
                self.utils.print_info("Closing Actions menu")
                self.auto_actions.click(self.device_actions.get_device_actions_button())
                return -1
            else:
                self.utils.print_info("Clicking the 'Relaunch Digital Twin' link.")
                self.screen.save_screen_shot()
                self.auto_actions.click(relaunch_link)
                if confirm.lower() == 'yes':
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    self.utils.print_info("Confirming the relaunch.")
                    self.screen.save_screen_shot()
                    tool_tp_text_error = self.devices_web_elements.get_ui_banner_error_message()
                    if tool_tp_text_error:
                        self.utils.print_info(tool_tp_text_error.text)
                        return -1
                    return 1
                else:
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_cancel_button())
                    return 1
        else:
            self.utils.print_info("Could not find the 'Actions > Relaunch Digital Twin' link.")

        return -1

    def is_actions_shutdown_digital_twin_visible(self):
        """
        - This keyword checks if the ACTIONS > Shutdown Digital Twin menu option is visible
        - It is assumed that the Manage > Device window is open and that a device is selected.
        - Keyword Usage
         - ``Is Actions Shutdown Digital Twin Visible``
        :return: 1 if the menu item is displayed, else -1
        """
        ret_val = -1
        self.utils.print_info("Opening Actions menu")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        sleep(2)

        shutdown_link = self.device_actions.get_digital_twin_shutdown_action_menu_item()
        if shutdown_link:
            hidden = shutdown_link.get_attribute("class")
            self.utils.print_debug(f"'Shutdown Digital Twin' menu item Class value: {hidden}")
            if "fn-hidden" in hidden:
                self.utils.print_info("The 'Shutdown Digital Twin' link is not displayed.")
                self.screen.save_screen_shot()
            else:
                self.utils.print_info("The 'Shutdown Digital Twin' link is displayed.")
                self.screen.save_screen_shot()
                ret_val = 1
        else:
            self.utils.print_info("Could not find the 'Actions > Shutdown Digital Twin' link.")

        self.utils.print_info("Closing Actions menu")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        return ret_val

    def actions_shutdown_digital_twin(self, confirm="yes"):
        """
        - This keyword clicks on the ACTIONS > Shutdown Digital Twin
        - It is assumed that the Manage > Device window is open and a Digital Twin device is selected.
        - Keyword Usage
         - ``Actions Shutdown Digital Twin    confirm="no"``
        :param confirm: Click Yes or No button within the confirmation panel
        :return: 1 if action was successful, else -1
        """
        self.utils.print_info("Clicking on Actions Button")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        sleep(2)

        shutdown_link = self.device_actions.get_digital_twin_shutdown_action()
        if shutdown_link:
            hidden = shutdown_link.get_attribute("class")
            self.utils.print_info(f"'Shutdown Digital Twin' menu item Class value: {hidden}")
            if "fn-hidden" in hidden:
                self.utils.print_info("The 'Shutdown Digital Twin' link is not displayed.")
                self.utils.print_info("Closing Actions menu")
                self.auto_actions.click(self.device_actions.get_device_actions_button())
                return -1
            else:
                self.utils.print_info("Clicking the 'Shutdown Digital Twin' link.")
                self.screen.save_screen_shot()
                self.auto_actions.click(shutdown_link)
                if confirm.lower() == 'yes':
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_yes_button())
                    self.utils.print_info("Confirming the shutdown.")
                    self.screen.save_screen_shot()
                    tool_tp_text_error = self.devices_web_elements.get_ui_banner_error_message()
                    if tool_tp_text_error:
                        self.utils.print_info(tool_tp_text_error.text)
                        return -1
                    return 1
                else:
                    self.auto_actions.click(self.dialogue_web_elements.get_confirm_cancel_button())
                    return 1
        else:
            self.utils.print_info("Could not find the 'Actions > Shutdown Digital Twin' link.")

        return -1
