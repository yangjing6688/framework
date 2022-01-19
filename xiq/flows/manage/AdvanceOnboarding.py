from time import sleep
from common.Screen import Screen
from common.Utils import Utils
from common.AutoActions import AutoActions
from xiq.flows.manage.Location import Location
from xiq.flows.manage.Devices import Devices
import xiq.flows.common.ToolTipCapture as tool_tip
from xiq.flows.common.Navigator import Navigator
from xiq.elements.DialogWebElements import DialogWebElements
from xiq.elements.AdvanceOnboardingWebElements import AdvanceOnboardingWebElements
from xiq.elements.DevicesWebElements import DevicesWebElements


class AdvanceOnboarding(AdvanceOnboardingWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.dialogue_web_elements = DialogWebElements()
        self.devices_web_elements = DevicesWebElements()

        self.screen = Screen()
        self.navigator = Navigator()
        self.devices = Devices()

    def advance_onboard_device(self, device_serial, device_make="", dev_location="", device_type="Real",
                               entry_type="Manual", csv_location='', create_location=False):
        """
         - This keyword is used to onboard Device using Advance Onboarding Method
         - Keyword Usage:
          - ``Onboard Device  ${DEVICE_SERIAL}   device_make=${DEVICE_MAKE_AEROHIVE}   dev_location=${LOCATION}``

        :param device_serial: serial number of Device
        :param device_make: Model of the Device ex:Extreme-aerohive,ExOS,VOSS,DELL
        :param dev_location: Location details in Comma format
        :param device_type: Real or Simulated Device type
        :param entry_type: Either Manual or CSV Entry Type
        :param csv_location: Absolute Path of Device onboarding CSV File Location on remote Machine
        :param create_location: Create new location during onboarding
        :return: 1 if Device Onboarded Sucessfully else -1
        """
        self.utils.print_info("Navigate to advance on board tab")
        self._got_to_advanced_onboard_tab()

        self.utils.print_info("Click Location:Next Button")
        self.auto_actions.click(self.get_deploy_devices_next_location_button())
        sleep(3)

        if not create_location:
            self.utils.print_info("Click Next:Building Button ")
            self.auto_actions.click(self.get_deploy_devices_next_location_button())
            sleep(3)

            self.utils.print_info("Click Next:Floor Button ")
            self.auto_actions.click(self.get_deploy_devices_next_location_button())
            sleep(3)

        else:
            location_list = dev_location.split(',')
            self.utils.print_info("Enter Location")
            self.auto_actions.send_keys(self.get_location_input(), location_list[1].strip())
            sleep(1)

            self.utils.print_info("Save Location")
            self.auto_actions.click(self.get_onboard_devices_button())
            sleep(2)

            self.utils.print_info("Click Next:Building Button ")
            self.auto_actions.click(self.get_deploy_devices_next_location_button())
            sleep(1)

            self.utils.print_info("Enter Building")
            self.auto_actions.send_keys(self.get_building_input(), location_list[2].strip())
            sleep(1)
            self.auto_actions.send_keys(self.get_building_address(), location_list[2].strip())

            self.utils.print_info("Save Building")
            self.auto_actions.click(self.get_onboard_devices_button())
            sleep(1)

            self.utils.print_info("Click Next:Floor Button ")
            self.auto_actions.click(self.get_deploy_devices_next_location_button())
            sleep(1)

            self.utils.print_info("Add a Floor")
            self.auto_actions.send_keys(self.get_floor_input(), location_list[3].strip())
            sleep(1)

            self.utils.print_info("Save Floor")
            self.auto_actions.click(self.get_floor_button())
            sleep(2)

        self.utils.print_info("Click Next:Onboard Devices Button ")
        self.auto_actions.click(self.get_deploy_devices_next_location_button())
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        if device_type == "Real":
            self.utils.print_info("Selecting Real Device type Radio Button")
            self.auto_actions.click(self.get_devices_type_real_radio_button())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("Selecting Simulated Device type Radio Button")
            self.auto_actions.click(self.get_devices_type_simulated_radio_button())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

        if entry_type == "Manual":
            self.utils.print_info("Selecting Entry Type as Manual")
            self.auto_actions.click(self.get_entry_type_manual_radio_button())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Entering Device Serial Number...")
            self.auto_actions.send_keys(self.get_serial_number_textfield(), device_serial)
            sleep(8)

            self.screen.save_screen_shot()
            sleep(2)

            if device_make:
                self.utils.print_info(f"Clicking Device Make Type Drop Down")
                if self.get_device_make_aerohive_dropdown().is_displayed():
                    self.auto_actions.click(self.get_device_make_aerohive_dropdown())
                    sleep(3)

                    self.utils.print_info(f"Selecting Device Make Type Option : {device_make}")
                    self.auto_actions.select_drop_down_options(self.get_devices_make_drop_down_options(), device_make)
                    sleep(3)

                    self.screen.save_screen_shot()
                    sleep(2)

                if self.get_device_make_select_one_dropdown():
                    self.auto_actions.click(self.get_device_make_select_one_dropdown())
                    sleep(3)
                    self.utils.print_info(f"Selecting Device Make Type Option : {device_make}")
                    self.auto_actions.select_drop_down_options(self.get_devices_make_drop_down_options(), device_make)
                    sleep(3)

                    self.screen.save_screen_shot()
                    sleep(2)

                if self.get_advance_onboard_cloudiq_engine_button().is_displayed():
                    self.utils.print_info("Selecting CloudIQEngine Radio Button")
                    self.auto_actions.click(self.get_advance_onboard_cloudiq_engine_button())
                    sleep(3)

        else:
            self.utils.print_info("Selecting Entry Type as CSV")
            self.auto_actions.click(self.get_entry_type_csv_radio_button())
            sleep(2)

            # Select the 'Device Make' field value and enter the serial number depending on which device type is being added
            if 'exos' in device_make.lower():
                self.utils.print_info("Selecting 'EXOS' from the 'Device Make' drop down...")
                self.auto_actions.click(self.devices_web_elements.get_devices_advanced_add_device_make_drop_down())
                self.auto_actions.click(self.devices_web_elements.get_devices_advanced_add_device_make_voss_choice())
                sleep(1)

                if entry_type == "CSV":
                    if csv_location:
                        upload_button = self.devices_web_elements.get_device_entry_exos_csv_upload_button_advanced_onboard()
                        if upload_button:
                            self.utils.print_info("Specifying CSV file '" + csv_location + "' for VOSS device")
                            self.auto_actions.send_keys(upload_button, csv_location)
                        else:
                            self.utils.print_info(">>> CSV file could not be specified - upload button not located")
                            self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                            self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                            return -1
                    else:
                        self.utils.print_info(">>> CSV file was not specified")
                        self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                        self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                        return -1

            else:
                self.utils.print_info(">>> Unsupported device type " + device_make)
                self.utils.print_info(">>> Clicking Cancel and exiting - device NOT on-boarded")
                self.auto_actions.click(self.devices_web_elements.get_devices_add_devices_cancel_button())
                return -1

        self.utils.print_info("Click Onboard Devices Button")
        self.auto_actions.click(self.get_onboard_devices_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking for Errors...")
        dialog_message = self.dialogue_web_elements.get_dialog_message()

        if dialog_message:
            self.utils.print_info("Dialog Message: ", dialog_message)
            if "Device already onboarded" in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -1
            if "A stake record of the device was found in the redirector." in dialog_message:
                self.utils.print_info("Error: ", dialog_message)
                self.auto_actions.click(self.dialogue_web_elements.get_dialog_box_ok_button())
                return -2

        sleep(3)
        success_message = self.get_onboard_success_status_textfield().text
        self.utils.print_info("Onboard Success Message :", success_message)
        self.utils.print_info("Validating ToolTip Message on Advance Onboard Page")
        if success_message:
            if not "Device(s) Successfully Onboarded" in success_message:
                self.utils.print_info("Tooltip Validation Failed on Advance Onboard Page")
                return -1

        sleep(3)

        self.utils.print_info("Click Next Topology Button")
        self.auto_actions.click(self.get_deploy_devices_next_topology_button())
        sleep(2)

        self.utils.print_info("Click Finish Button")
        self.auto_actions.click(self.get_advance_onboard_device_finish_button())
        sleep(2)

        if self.get_drawer_content().is_displayed():
            self.utils.print_info("Closing Advance Onboard Dialogue PopUp window")
            self.auto_actions.click(self.get_drawer_trigger())
            sleep(4)

        self.navigator.navigate_to_devices()
        sleep(2)

        self.utils.print_info("Validating Device Entry on Manage--> Devices Page")
        serials = device_serial.split(",")
        self.utils.print_info("Device Serials Numbers: ", serials)

        for serial in serials:
            if self.devices.search_ap_serial(serial):
                self.utils.print_info("Successfully Onboarded Device(s): ", serials)
                return 1
            else:
                return -1

    def _got_to_advanced_onboard_tab(self):
        """
        - This method is used to navigate to the device advanced on board tab
        - Flow:
         - Manage --> Devices --> Click on Device Add Button(+) --> Advanced Onboarding
        :return:
        """
        self.navigator.navigate_to_onboard_tab()
        self.utils.print_info("Clicking Deploy devices directly to the cloud button...")
        self.auto_actions.click(self.get_deploy_devices_to_cloud_radio_button())
        sleep(5)

        self.utils.print_info("Clicking Lets Get Started Menu")
        self.auto_actions.click(self.get_deploy_devices_get_started_button())

    def _assign_location(self, dev_location='default'):
        """
        - This keyword assigns location to device.
        :param dev_location: location where the device is to be assigned in the above format
        :return: 1 if success else -1
        """
        self.utils.print_info("Click Select Location Button")
        self.auto_actions.click(self.get_assign_location_select_button())

        try:
            location_list = dev_location.split(',')
            location_generics = self.get_locations_generic()
            location_buildings = self.get_locations_building()
            location_floors = self.get_locations_floors()

            for location_item in location_list:
                self.utils.print_info("Location items ", location_item)

            for location_generic in location_generics:
                self.utils.print_info("Generic locations on UI:", location_generic.text)

            for location_building in location_buildings:
                self.utils.print_info("Building locations on UI:", location_building.text)

            for location_floor in location_floors:
                self.utils.print_info("Floor locations on UI:", location_floor.text)

            generic_set = False
            building_set = False
            floor_set = False

            for location_item in location_list:

                if not generic_set:
                    self.utils.print_info("Selecting Generic location: ", location_item)
                    for location_generic in location_generics:
                        if location_item.strip() in location_generic.text:
                            self.utils.print_info("Match found for location type Generic:", location_generic.text)
                            self.auto_actions.click(location_generic)
                            generic_set = True
                            sleep(5)

                if not building_set:
                    self.utils.print_info("Selecting Building: ", location_item)
                    for location_building in location_buildings:
                        if location_item.strip() in location_building.text:
                            self.utils.print_info("Match found for location type Building:", location_building.text)
                            self.auto_actions.click(location_building)
                            building_set = True
                            sleep(5)

                if not floor_set:
                    self.utils.print_info("Selecting Floor: ", location_item)
                    for location_floor in location_floors:
                        if location_item.strip() in location_floor.text:
                            self.utils.print_info("Match found for location type Generic:", location_floor.text)
                            self.auto_actions.click(location_floor)
                            floor_set = True
                            sleep(5)

            self.utils.print_info("Clicking Select Assign Location Button")
            self.auto_actions.click(self.get_select_assign_location_button())
            sleep(5)
            return 1
        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to Assign Location to device")
            return -1