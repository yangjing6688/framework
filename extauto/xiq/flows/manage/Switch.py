from time import sleep
from robot.libraries.BuiltIn import BuiltIn

from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen

from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator

from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.LoginWebElements import LoginWebElements


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
        if self.search_switch_serial(switch_serial) == 1:
            self.utils.print_info(f"Switch with {switch_serial} serial number already onboarded")
            return 1

        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

        self.utils.print_info("Selecting Quick Add Devices menu")
        self.auto_actions.move_to_element(self.devices_web_elements.get_devices_quick_add_devices_menu_item())

        self.utils.print_info("Selecting Deploy your devices directly to the cloud ")
        self.auto_actions.click(self.devices_web_elements.get_deploy_devices_to_cloud_menu_item())

        self.utils.print_info("Entering Serial Number...")
        self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), switch_serial)
        sleep(5)

        self.utils.print_info("Checking for the Device Make dropdown or Switch/Fabric Engine selection option")
        dropdown_make = self.get_switch_make_drop_down()
      
        if "VOSS" in device_os.upper() or "VOSS" in switch_make.upper():
            if dropdown_make.is_displayed():
                self.utils.print_info("Device Make dropdown selection is displayed, selecting VOSS")
                self.auto_actions.click(self.get_switch_make_drop_down())
                sleep(2)
                self.select_drop_down_options(self.get_switch_make_drop_down_options(), "VOSS")
            else:
                self.utils.print_info("Switch/Fabric Engine radio options are displayed, selecting Fabric Engine")
                self.auto_actions.click(self.devices_web_elements.get_device_os_voss_radio())
      
        if "EXOS" in device_os.upper() or "EXOS" in switch_make.upper():
            if dropdown_make.is_displayed():
                self.utils.print_info("Device Make dropdown selection is displayed, selecting EXOS")
                self.auto_actions.click(self.get_switch_make_drop_down())
                sleep(2)
                self.select_drop_down_options(self.get_switch_make_drop_down_options(), "EXOS")
            else:
                self.utils.print_info("Switch/Fabric Engine radio options are displayed, selecting Switch Engine")
                self.auto_actions.click(self.devices_web_elements.get_device_os_exos_radio())          

        sleep(2)
        if location:
            self.auto_actions.click(self.devices_web_elements.get_location_button())
            self.devices._select_location(location)

        self.utils.print_info("Clicking on ADD DEVICES button...")
        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()
        self.utils.print_info("Dialog Message: ", dialog_message)
        if dialog_message:
            if switch_serial + BuiltIn().get_variable_value('${MSG_DUPLICATE_DEVICE}') in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                self.utils.print_info("EXIT LEVEL: ", BuiltIn().get_variable_value("${EXIT_LEVEL}"))
                return -1

        self.utils.print_info("Clicking on DEVICES REFRESH Page button...")
        self.auto_actions.click(self.get_devices_refresh_button())
        sleep(5)

        if "," in switch_serial:
            switch_serial_list = switch_serial.split(",")
            for serial in switch_serial_list:
                if self.devices.search_device(device_serial=serial):
                    self.utils.print_info(f"Successfully Onboarded Switch With Serial no. {serial}")
                else:
                    self.utils.print_error(f"Switch with serial no. {serial} is not successfully onboarded...")
                    return -1
            return 1
        else:
            if self.devices.search_device(device_serial=switch_serial):
                self.utils.print_info(f"Successfully Onboarded Switch With Serial no. {switch_serial}")
                return 1
            else:
                self.utils.print_error(f"Switch with serial no. {switch_serial} is not successfully onboarded...")
                return -1

    def onboard_aerohive_switch(self, switch_serial, switch_type):
        """
        - This keyword onboards an Aerohive Switch using Quick onboarding flow.
        - Flow  Manage--> Devices--> Add --> Quick Add Devices--> Select Aerohive Device Make --> Enter Serial Number
                 --> Add Devices
        - Keyword Usage
         - ``Onboard Aerohive Switch    ${SWITCH_SERIAL}  ${SWITCH_MAKE_TYPE}``

        :param switch_serial: serial number of Switch
        :param switch_type: Model of the Switch
        :return: 1 if Aerohive Switch OnBoarding is Successful without Error Message
        """

        self.navigator.navigate_to_devices()
        sleep(2)
        if 'aerohive' in switch_type:
            self.utils.print_info("Clicking on ADD button...")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_button())

            self.utils.print_info("Selecting Quick Add menu")
            self.auto_actions.click(self.devices_web_elements.get_devices_quick_add_menu_item())

            self.utils.print_info("Entering Serial Number....:", switch_serial)
            self.auto_actions.send_keys(self.devices_web_elements.get_devices_serial_text_area(), switch_serial)

            self.utils.print_info("Clicking on ADD DEVICES button...")
            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_button())

            tooltip_text = self.dialogue_web_elements.get_tooltip_text()
            sleep(5)

            """
            self.utils.print_info("tooltip_text: ", tooltip_text)
            if "1 device was  added successfully!" in tooltip_text:
                return 1
            """

            self.utils.print_info("Checking for Errors...")
            dialog_message = self.dialogue_web_elements.get_dialog_message()

            if dialog_message:
                self.utils.print_info("Dialog Message: ", dialog_message)
                if "Device already onboarded" in dialog_message:
                    self.utils.print_info("Error: ", dialog_message)
                    self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -1
            else:
                self.utils.print_info("No Dialog box")

            serials = switch_serial.split(",")
            self.utils.print_info("Serials: ", serials)
            self.auto_actions.click(self.devices_web_elements.get_refresh_devices_page())
            for serial in serials:
                if self.devices.search_device(device_serial=serial):
                    self.utils.print_info("Successfully Onboarded switch(s): ", serials)
                    return 1
                else:
                    return -1

    def select_switch(self, sw_serial):
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
                self.auto_actions.click(self.get_switch_name())
                sleep(2)
                return 1
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

    def search_switch_serial(self, sw_serial):
        """
        - Searches for Switch matching Switch's Serial Number
        - Flow  Manage--> Devices--> Search Switch Row based on Serial Number
        - Keyword Usage
         - ``Search Switch Serial   ${SWITCH_SERIAL}``

        :param sw_serial: Switch's Serial Number
        :return: return 1 if Switch found on Devices Grid Row else -1
        """
        rows = self.devices_web_elements.get_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_info("Device row data: ", row.text)
                if sw_serial in row.text:
                    self.utils.print_info("Found Switch Row: ", row.text)
                    return 1
        return -1

    def search_switch_mac(self, sw_mac):
        """
        - Searches for Switch matching Switch's Mac Address
        - Flow  Manage--> Devices--> Search Switch Row based on Mac Address
        - Keyword Usage
         - ``Search Switch Mac   ${SWITCH_SERIAL}``

        :param sw_mac: Switch's Mac Address
        :return: return 1 if Switch found on Devices Grid Row else -1
        """
        rows = self.devices_web_elements.get_grid_rows()
        for row in rows:
            if sw_mac in row.text:
                self.utils.print_info("Found Switch Row: ", row.text)
                return 1
        return -1

    def search_switch_name(self, sw_name):
        """
        - Searches for Switch matching Switch's Name
        - Flow  Manage--> Devices--> Search Switch Row based on Switch Name
        - Keyword Usage
         - ``Search Switch Name   ${SWITCH_NAME}``

        :param sw_name: Switch's Name
        :return: return 1 if Switch found on Devices Grid Row else -1
        """
        rows = self.devices_web_elements.get_grid_rows()
        for row in rows:
            if sw_name in row.text:
                self.utils.print_info("Found Switch Row: ", row.text)
                return 1
        return -1

    def search_switch(self, sw_serial=None, sw_name=None, sw_mac=None):
        """
        - This keyword returns Searches Switch using serial number,name or mac address
        - Flow  Manage--> Devices--> Search Switch Row using Serial Number,Name or mac address
        - Keyword Usage
         - ``Search Switch sw_serial=${SWITCH_SERIAL}``
         - ``Search Switch sw_name=${SWITCH_NAME}``
         - ``Search Switch sw_mac=${SWITCH_MAC}``

        :param sw_serial: Switch Serial Number
        :param sw_name: Switch Name
        :param sw_mac: Switch MAC Address
        :return: 'green' if the AP is online else return -1
        """
        if sw_serial:
            self.utils.print_info("Searching Switch with Serial: ", sw_serial)
            return self.devices.search_device(device_serial=sw_serial)
        if sw_name:
            self.utils.print_info("Searching Switch with Name: ", sw_name)
            return self.devices.search_device(device_name=sw_name)
        if sw_mac:
            self.utils.print_info("Searching Switch with MAC: ", sw_mac)
            return self.devices.search_device(device_mac=sw_mac)
        return 1

    def delete_switch(self, sw_serial):
        """
        - This keyword Deletes Switch using serial number
        - Flow  Manage--> Devices--> Select Switch Row using serial number-->Click Delete Button
        - Keyword Usage
         - ``Delete Switch ${SWITCH_SERIAL}``

        :param sw_serial: Switch Serial Number
        :return: 1 if the AP is online else return -1
        """
        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)
        rows = self.devices_web_elements.get_grid_rows()
        for row in rows:
            self.utils.print_debug("row data: ", row.text)
            if sw_serial in row.text:
                self.utils.print_info("Found switch Row: ", row.text)
                self.auto_actions.click(self.devices_web_elements.get_ap_select_checkbox(row))
                sleep(3)
                self.auto_actions.click(self.devices_web_elements.get_delete_button())
                self.auto_actions.click(self.devices_web_elements.get_device_delete_confirm_ok_button())
        for row in rows:
            if sw_serial in row.text:
                self.utils.print_info("Unable to delete switch")
                return -1
            else:
                self.utils.print_info("Deleted  Successfully: ", sw_serial)
                return 1

    def get_switch_status(self, serial='default', name='default', mac='default'):
        """
        - This keyword Get the status of the Switch using serial number,Switch Name and Mac address
        - Flow  Manage--> Devices
        - Keyword Usage
         - ``Get Switch Status serial=${SWITCH_SERIAL}``
         - ``Get Switch Status name=${SWITCH_NAME}``
         - ``Get Switch Status mac=${SWITCH_MAC}``

        :param serial: Switch Serial Number
        :param name: Switch Name
        :param mac: Switch MAC Address
        :return: Green if the AP is online
        """
        row = -1

        self.utils.print_info('Getting Switch Status using')
        if serial != 'default':
            self.utils.print_info("Getting status of Switch with serial: ", serial)
            row = self.get_switch_row(serial)

        if name != 'default':
            self.utils.print_info("Getting status of switch with name: ", name)
            row = self.get_switch_row(name)

        if mac != 'default':
            self.utils.print_info("Getting status of AP with MAC: ", mac)
            row = self.get_switch_row(mac)

        if row:
            sleep(5)
            status = self.devices_web_elements.get_status_cell(row)
            if status:
                self.utils.print_info("Switch Status: Connected")
                return 'green'

    def get_switch_row(self, sw_serial='default', sw_name='default', sw_mac='default'):
        """
        - This keyword Get presence of Switch row in devices grid using serial number,Switch Name and Mac address
        - Flow  Manage--> Devices
        - Keyword Usage
         - ``Get Switch Row sw_serial=${SWITCH_SERIAL}``
         - ``Get Switch Row sw_name=${SWITCH_NAME}``
         - ``Get Switch Row sw_mac=${SWITCH_MAC}``

        :param sw_serial: Switch Serial Number
        :param sw_name: Switch Name
        :param sw_mac: Switch MAC Address
        :return: row if the AP is present on devices grid else -1
        """
        self.utils.print_info('Getting Switch row...')
        rows = self.devices_web_elements.get_grid_rows()
        for row in rows:
            if sw_serial != 'default':
                if sw_serial in row.text:
                    self.utils.print_info("Found Switch row: ", row.text)
                    return row
            if sw_name != 'default':
                if sw_name in row.text:
                    self.utils.print_info("Found Switch row: ", row.text)
                    return row
            if sw_mac != 'default':
                if sw_mac in row.text:
                    self.utils.print_info("Found Switch row: ", row.text)
                    return row
        return -1

    def capture_xiq_switch_connection_host(self):
        """
        - This keyword Get Switch Connection Host
        - Flow  Manage--> Devices
        - Keyword Usage
         - ``Capture XIQ Switch Connection Host``

        :param sw_serial: Switch Serial Number
        :param sw_name: Switch Name
        :param sw_mac: Switch MAC Address
        :return: row if the AP is present on devices grid else -1
        """
        self.utils.print_info("Clicking on About ExtremecloudIQ link")
        self.auto_actions.move_to_element(self.login_web_elements.get_user_account_nav())
        sleep(2)
        self.auto_actions.click(self.login_web_elements.get_about_extreme_cloudiq_link())
        sleep(2)

        switch_connection_host = self.get_switch_connection_host_details()
        self.utils.print_info("XIQ SWitch Connection Host Is: ", switch_connection_host)
        sleep(4)

        self.utils.print_info("Close About ExtremecloudIQ Link Dialogue Page")
        self.auto_actions.click(self.login_web_elements.get_cancel_about_extremecloudiq_dialogue())
        sleep(2)

        return switch_connection_host
