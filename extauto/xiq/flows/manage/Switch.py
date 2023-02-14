from time import sleep
from robot.libraries.BuiltIn import BuiltIn

from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from extauto.common.CommonValidation import CommonValidation

from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator

from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.LoginWebElements import LoginWebElements
from ExtremeAutomation.Utilities.deprecated import deprecated


class Switch(SwitchWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.screen = Screen()
        self.robot_built_in = BuiltIn()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.devices_web_elements = DevicesWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.login_web_elements = LoginWebElements()
        self.devices = Devices()
        self.common_validation = CommonValidation()

    @deprecated("Please use onboard_device_quick(...)")
    def onboard_switch(self, switch_serial, switch_make="default", device_os="default", location=None, switch_type="Real", entry_type="Manual"):
        """
        - This keyword onboards an Switch Device based on Switch Type(ie Exos) using Quick onboard flow.
        - Flow  Manage--> Devices--> Add --> Quick Add Devices--> Select Device Make --> Serial Number--> Add Devices
        - Keyword Usage
        - ``Onboard Switch    ${SWITCH_SERIAL}  ${SWITCH_MAKE_TYPE}``

        :param switch_serial: serial number of Switch
        :param switch_make: Switch Make
        :param device_os: Switch OS
        :param location: switch location
        :param switch_type: Device Type ie Real or Simulated
        :param entry_type: Device Entry Type ie Manual or CSV
        :return: 1 if Switch OnBoarding is Successful without Error Message
        """

        if self.devices.search_device(device_serial=switch_serial, ignore_failure=True) == 1:
            self.utils.print_info(f"Switch with {switch_serial} serial number already onboarded")
            return 1
        else:
            self.utils.print_info(f"Onboarding Switch with serial number '{switch_serial}'")

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_button)

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click_reference(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item)

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), switch_serial)
        sleep(5)

        self.utils.print_info("Checking for the Device Make dropdown or Switch/Fabric Engine selection option")
        dropdown_make = self.get_switch_make_drop_down()

        if "VOSS" in device_os.upper() or "VOSS" in switch_make.upper():
            if dropdown_make.is_displayed():
                self.utils.print_info("Device Make dropdown selection is displayed, selecting VOSS")
                self.auto_actions.click_reference(self.get_switch_make_drop_down)
                sleep(2)
                self.select_drop_down_options(self.get_switch_make_drop_down_options(), "VOSS")
            else:
                self.utils.print_info("Switch/Fabric Engine radio options are displayed, selecting Fabric Engine")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_voss_radio)

        if "EXOS" in device_os.upper() or "EXOS" in switch_make.upper():
            if dropdown_make.is_displayed():
                self.utils.print_info("Device Make dropdown selection is displayed, selecting EXOS")
                self.auto_actions.click_reference(self.get_switch_make_drop_down)
                sleep(2)
                self.select_drop_down_options(self.get_switch_make_drop_down_options(), "EXOS")
            else:
                self.utils.print_info("Switch/Fabric Engine radio options are displayed, selecting Switch Engine")
                self.auto_actions.click_reference(self.devices_web_elements.get_device_os_exos_radio)

        sleep(2)
        if location:
            self.auto_actions.click_reference(self.devices_web_elements.get_location_button)
            self.devices._select_location(location)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click_reference(self.devices_web_elements.get_devices_add_devices_button)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()
        self.utils.print_info("Dialog Message: ", dialog_message)
        if dialog_message:
            if switch_serial + BuiltIn().get_variable_value('${MSG_DUPLICATE_DEVICE}', default='Device already onboarded') in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click_reference(self.dialogue_web_elements.get_dialog_box_ok_button)
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}", default='-600'))
                return -1

        self.utils.print_info("Clicking on DEVICES REFRESH Page button...")
        self.devices.refresh_devices_page()

        if "," in switch_serial:
            switch_serial_list = switch_serial.split(",")
            for serial in switch_serial_list:
                if self.devices.search_device(device_serial=serial, ignore_failure=True) == 1:
                    self.utils.print_info(f"Successfully Onboarded Switch With Serial no. {serial}")
                else:
                    self.utils.print_error(f"Switch with serial no. {serial} is not successfully onboarded...")
                    return -1
            return 1
        else:
            if self.devices.search_device(device_serial=switch_serial, ignore_failure=True) == 1:
                self.utils.print_info(f"Successfully Onboarded Switch With Serial no. {switch_serial}")
                return 1
            else:
                self.utils.print_error(f"Switch with serial no. {switch_serial} is not successfully onboarded...")
                return -1



    def select_switch(self, sw_serial, **kwargs):
        """
        - This keyword Select Aerohive Switch based on Switch Serial Number From Devices Grid
        - Flow  Manage--> Devices--> Select Aerohive SWitch
        - Keyword Usage
        - ``Select Switch    ${SWITCH_SERIAL}``

        :param sw_serial: serial number of Switch
        :return: 1 if Aerohive Switch selected Successfully else -1
        """
        rows = self.get_grid_rows()
        for row in rows:
            if sw_serial in row.text:
                self.utils.print_info("Found Switch Row: ", row.text)
                self.auto_actions.click_reference(self.get_switch_name)
                sleep(2)
                kwargs['pass_msg'] = "Aerohive Switch selected Successfully"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['fail_msg'] = "Aerohive Switch selected unsuccessfully"
        self.common_validation.failed(**kwargs)
        return -1

    def get_switch_port_details(self, sw_serial, port_number):
        """
        - This keyword return Switch Port Details ie Status based on serial Number and Port Number of the Switch
        - Flow  Manage--> Devices--> SWitch hyper Link --> Click Port Number
        - Keyword Usage
        - ``Get Switch Port Details    ${SWITCH_SERIAL}  ${PORT_NUMBER}``

        :param sw_serial: serial number of Switch
        :param port_number: Port Number of the Switch
        :return: Port Details ie Port Status
        """
        self.select_switch(sw_serial)
        self.utils.print_info("Clicking Switch Port Number")
        self.auto_actions.click(self.get_switch_port_button(port_number))

        port_details = []
        rows = self.get_switch_port_detail_rows()
        for el in rows:
            port_details.append(el.text)
        return port_details

    def get_switch_port_status(self, sw_serial, port_number):
        """
        - This keyword return Switch Port Status(Enabled/Disabled) based on serial Number and Port Number of the Switch
        - Flow  Manage--> Devices--> SWitch hyper Link --> Click Port Number
        - Keyword Usage
        - ``Get Switch Port Status   ${SWITCH_SERIAL}  ${PORT_NUMBER}``

        :param sw_serial: serial number of Switch
        :param port_number: Port Number of the Switch
        :return: Port Status ie Enabled/Disabled
        """
        port_status = None
        port_details = self.get_switch_port_details(sw_serial, port_number)
        for value in port_details:
           if "Port Status" in value:
               port_status = value.split("Port Status")[-1]
               break
        return port_status
