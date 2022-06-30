from time import sleep

from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.manage.Client import *
from extauto.xiq.flows.manage.Devices import *
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DeviceActions import *
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.xiq.elements.MLInsightsPlanWebElements import *
from extauto.xiq.elements.Device360WebElements import *


class Location:

    def __init__(self):
        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.device_actions = DeviceActions()
        self.utils = Utils()
        self.devices = Devices()
        self.screen = Screen()
        self.client = Client()
        self.devices_web_elements = DevicesWebElements()
        self.ml_insights_plan_web_elements = MLInsightsPlanWebElements()
        self.d360_web_elements = Device360WebElements()


    def assign_location_with_hyperlink(self, device_serial=None, dev_location=None):
        """
        - This keyword assigns location to device by clicking on Assign Location hyperlink in Devices page.
        -Flow: Manage --> Devices --> based on device serial clicks on the Assign Location hyperlink present in Devices grid.
        - Keyword Usage:
         - ``Assign Location With Hyperlink    ${AP1_SERIAL}              San Jose, building_01, floor_02``
        :param device_serial: device serial number
        :param dev_location: location where the device is to be assigned in the above format
        :return: 1 if success else -1
        """
        self.navigator.navigate_to_devices()
        if device_serial:
            row = self.devices.get_device_row(device_serial=device_serial)
            location = self.get_device_location(device_serial)
            if row:
                cells = self.devices_web_elements.get_device_row_cells(row)
                for cell in cells:
                    if location in cell.text:
                        self.utils.print_info("Clicking on the Assign Location Hyperlink")
                        self.auto_actions.click(self.devices_web_elements.get_cell_href(cell))
                        sleep(5)

                        self.screen.save_screen_shot()
                        return self._assign_location(device_serial, dev_location)
            else:
                self.utils.print_info("Unable to access Devices Grid")
                return -1
        else:
            self.utils.print_info("Device serial is not provided")
            return -1

    def assign_location_with_device_actions(self, device_serial=None, dev_location=None):
        """
        - This keyword assigns location to device by clicking on Actions button in Devices page.
        -Flow: Manage --> Devices --> selects the device based on serial number --> Actions --> Assign Location
        - Keyword Usage:
         - ``Assign Location With Device Actions    ${AP1_SERIAL}              San Jose, building_01, floor_02``
        :param device_serial: device serial number
        :param dev_location: location where the device is to be assigned in the above format
        :return: 1 if success else -1
        """

        self.navigator.navigate_to_devices()
        if self.devices.select_ap(device_serial):
            self.utils.print_info("Clicking on Actions Button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())
            sleep(2)

            self.utils.print_info("Clicking on Assign Location")
            self.auto_actions.click(self.device_actions.get_device_actions_assign_location())
            sleep(2)

            self.screen.save_screen_shot()
            return self._assign_location(device_serial, dev_location)

        else:
            self.utils.print_info("Device not found in Devices Grid")
            return -1

    def _assign_location(self, device_serial='default', dev_location='default'):
        """
        - This keyword assigns the specified location to the specified device and confirms the assignment was successful.
        :param device_serial: device serial number
        :param dev_location: location to select, in a comma-separated list format; e.g., San Jose, building_01, floor_02
        :return: 1 if success, else -1
        """
        try:
            self.select_location(dev_location)

            location_list = dev_location.split(',')
            expected_location = " >>".join(location_list)
            observed_location = self.get_device_location(device_serial)
            self.utils.print_info("Expected location string: ", expected_location)
            self.utils.print_info("Device location from Device -> Manage: ", observed_location)

            if expected_location.strip() in observed_location:
                self.utils.print_info("Successfully Assigned Location")
                return 1
            else:
                self.utils.print_info("Unable to Assign Location")
                return -1
        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Unable to Assign Location to device")
            return -1

    def select_location(self, sel_loc):
        """
        - This keyword selects a location in the location dialog and clicks the "Assign" button.
          It is assumed the location dialog is already open.
        - Keyword Usage:
         - ``Select Location  ${LOCATION}``

        :param sel_loc: location to select, in a comma-separated list format; e.g., San Jose, building_01, floor_02
        :return: 1 if location is selected, else -1'
        """
        ret_val = -1
        if sel_loc:
            try:
                location_list = sel_loc.split(',')

                location_generics = self.device_actions.get_locations_generic()
                location_buildings = self.device_actions.get_locations_building()
                location_floors = self.device_actions.get_locations_floors()

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

                self.utils.print_info("Placing The Device To FloorPlan")
                source_el = self.device_actions.get_device_location_ap_node()
                target_el = self.device_actions.get_device_location_floor_map_section()
                self.auto_actions.drag_and_drop_element(source_el, target_el)
                self.screen.save_screen_shot()

                self.utils.print_info("Clicking on Assign Location Button")
                self.auto_actions.click(self.device_actions.get_assign_location_button())
                sleep(5)

                ret_val = 1

            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to select location")
        else:
            self.utils.print_info("Cannot select location - location not specified")

        return ret_val

    def _verify_device_location(self, device_serial="default", location_floor='default'):
        """
        - This keyword  verifies the location of device
        :param device_serial: Device serial number
        :param location_floor: floor of the location where AP has been assigned
        :return: 1 if success else -1
        """
        if self.navigator.navigate_to_devices():
            try:
                row = self.devices.get_manage_device_row(device_serial)
                if location_floor not in row.text:
                    self.utils.print_info("Location is not assigned to the Device")
                    return -1

                self.utils.print_info("Location is assigned to the Device")
                return 1
            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to Assign Location to device")
                return -1
        else:
            return -1

    def get_device_location(self, device_serial="default"):
        """
        - This keyword returns the location of a device
        - location string format: auto_location_01 >> San Jose >> building_01 >> floor_01
        :param device_serial: client name
        :return: returns location string if success else -1
        """
        return self.devices.get_device_details(device_serial, 'LOCATION')

    def _verify_client_location(self, client_name='default', location_floor='default'):
        """
        - This keyword verifies the location of client
        :param client_name: client name
        :param location_floor: floor of the location where AP has been assigned
        :return: 1 if success else -1
        """
        if self.navigator.navigate_to_clients():
            try:
                row = self.client.get_client_row(client_name)
                if location_floor not in row.text:
                    self.utils.print_info("Location is not assigned to Client")
                    return -1
                self.utils.print_info("Location is assigned to Client")
                return 1
            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to Verify Client Location")
                return -1
        else:
            return -1

    def get_assigned_floor(self, device_serial):
        """
        - Pre-condition - this keyword assumes that location already assigned to device
        - Clicks on device location link
        - Returns the floor, which is highlighted from the location popup
        :param device_serial: Device Serial
        :return: floor highlighted if success else -1
        """

        self.device.get_device_location_link()


    def create_location_building_floor(self, location, building, floor, width="50", height="50"):
        """
        -This function is to create location, building and floor in MLInsights >> N360plan
        :param location:
        :param building:
        :param floor:
        :return:
        """
        sleep(5)
        self.utils.print_info("Clicking on Devices Planning")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_manage_left_pane_click())
        sleep(1)
        self.utils.print_info("Clicking on Manage -> Planning")
        if self.auto_actions.click(self.ml_insights_plan_web_elements.get_network_360_plan_click()):
            self.utils.print_info("Button found")
        else:
            self.utils.print_info("Button not found")
            return -1
        sleep(3)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_plan_add_global_view())

        sleep(3)
        self.utils.print_info("Creating Location")
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_location_name(), location)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_plan_location_save())

        sleep(5)
        self.utils.print_info("Creating Building")
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_search_box(), location)
        sleep(5)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_select_locn())
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_add_building_btn())
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_building_name(), building)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_plan_building_save())

        sleep(5)
        self.utils.print_info("Creating Floor")
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_search_box(), location)
        sleep(5)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_select_building_tab())
        #self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_add_floor_btn())
        sleep(5)
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_floor_name(), floor)
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_floor_size_width(), width)
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_floor_size_height(), height)

        self.utils.print_info("Saving created map.....")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_plan_floor_save_button())

        self.utils.print_info("Getting back to Manage > Devices")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_manage_left_pane_click())
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_manage_devices_click())

        return 1

    def delete_location_building_floor(self, location, building, floor):
        """
        -This function is to delete location, building and floor in MLInsights >> N360plan
        :param location:
        :param building:
        :param floor:
        :return:
        """
        sleep(5)

        self.utils.print_info("Clicking on Devices Planning")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_manage_left_pane_click())
        sleep(1)
        self.utils.print_info("Clicking on Manage -> Planning")
        if self.auto_actions.click(self.ml_insights_plan_web_elements.get_network_360_plan_click()):
            self.utils.print_info("Button found")
        else:
            self.utils.print_info("Button not found")
            return -1

        sleep(3)
        self.utils.print_info("Searching floor ....")
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_search_box(), floor)

        sleep(0.5)
        self.utils.print_info("Deleting floor ....")
        if self.ml_insights_plan_web_elements.get_n360_select_floor_more():
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_select_floor_more())
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_delete_floor())
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_delete_yes())
            sleep(3)
        else:
            self.utils.print_info("The floor doesn't exist ")
            return 1
        self.utils.print_info("Searching Building ....")
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_search_box(), building)

        sleep(0.5)
        self.utils.print_info("Deleting Building ....")
        if self.ml_insights_plan_web_elements.get_n360_select_building_more():
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_select_building_more())
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_delete_building())
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_delete_yes())
            sleep(3)
        else:
            self.utils.print_info("The build doesn't exist ")
            return 1

        self.utils.print_info("Searching Location ....")
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_search_box(), location)
        sleep(0.5)
        self.utils.print_info("Deleting Location ....")
        if self.ml_insights_plan_web_elements.get_n360_select_location_more():
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_select_location_more())
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_delete_location())
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_delete_yes())
        else:
            self.utils.print_info("The Location doesn't exist ")
            return 1
        return 1

    def assign_location_using_hostname(self, device_host, dev_location=None):
        """
        - This keyword assigns location to device by clicking on Assign Location hyperlink in Devices page.
        -Flow: Manage --> Devices --> based on hostname clicks on the Assign Location hyperlink present in Devices grid.
        - Keyword Usage:
         - ``Assign Location With Hostname    ${SW_HOST}              San Jose, building_01, floor_02``
        :param device_serial: switch host
        :param dev_location: location where the device is to be assigned in the above format
        :return: 1 if success else -1
        """
        self.navigator.navigate_to_devices()
        if device_host:
            row = self.devices.get_device_row(device_name=device_host)
            location = self.get_device_location_using_hostname(device_host)
            if row:
                cells = self.devices_web_elements.get_device_row_cells(row)
                for cell in cells:
                    if location in cell.text:
                        self.utils.print_info("Clicking on the Assign Location Hyperlink")
                        self.auto_actions.click(self.devices_web_elements.get_cell_href(cell))
                        sleep(5)

                        self.screen.save_screen_shot()
                        return self._assign_location(device_host, dev_location)
            else:
                self.utils.print_info("Unable to access Devices Grid")
                return -1
        else:
            self.utils.print_info("Switch host is not provided")
            return -1

    def get_device_location_using_hostname(self, device_host="default"):
        """
        - This keyword returns the location of a device
        - location string format: auto_location_01 >> San Jose >> building_01 >> floor_01
        :param device_serial: client name
        :return: returns location string if success else -1
        """
        return self.devices.get_device_details(device_host, 'LOCATION')

    def assign_location_with_device_actions_using_hostname(self, device_name="default", dev_location=None):
        """
        - This keyword assigns location to device by clicking on Actions button in Devices page.
        -Flow: Manage --> Devices --> selects the device based on host name --> Actions --> Assign Location
        - Keyword Usage:
         - ``Assign Location With Device Actions    ${SW_HOST}              San Jose, building_01, floor_02``
        :param device_serial: device host name
        :param dev_location: location where the device is to be assigned in the above format
        :return: 1 if success else -1
        """

        self.navigator.navigate_to_devices()
        if self.devices.select_device(device_name):
            self.utils.print_info("Clicking on Actions Button")
            self.auto_actions.click(self.device_actions.get_device_actions_button())
            sleep(2)

            self.utils.print_info("Clicking on Assign Location")
            self.auto_actions.click(self.device_actions.get_device_actions_assign_location())
            sleep(2)

            self.screen.save_screen_shot()
            return self._assign_location(device_name, dev_location)

        else:
            self.utils.print_info("Device not found in Devices Grid")
            return -1

    def input_new_snmp_location(self, new_locn):
        """
        - This keyword is used to input new value to SNMP location in D360 >> device config
        - location string format: auto_location_01 >> San Jose >> building_01 >> floor_01
        :param loction name
        :return: returns 1 if success else -1
        """

        self.utils.print_info("Input New Location to the SNMP location field ")
        self.auto_actions.send_keys(self.d360_web_elements.get_device360_stack_configure_device_snmp_location(), new_locn)
        self.auto_actions.click(self.d360_web_elements.get_device360_dev_config_save_button())
        self.auto_actions.click(self.d360_web_elements.get_close_dialog())

        return 1

    def create_first_organization(self, organization, street, city, country, width="50", height="50"):
        '''
        This keyword create new organization if this isn't created
        - Keyword Usage:
                create_first_organization                     Luxoft       Doftanei        Bucuresti     Romania
        :param organization: name of organization
        :param street: name of street
        :param city: name of city
        :param country: select the country
        :return: return 1 if the organization was created successfully, else -1
        '''

        self.utils.print_info("Clicking on Devices Planning")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_manage_left_pane_click())
        sleep(1)
        self.utils.print_info("Clicking on Manage -> Planning")
        if self.auto_actions.click(self.ml_insights_plan_web_elements.get_network_360_plan_click()):
            self.utils.print_info("Button found")
        else:
            self.utils.print_info("Button not found")
            return -1
        sleep(3)
        if self.ml_insights_plan_web_elements.get_create_new_map_btn():
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_create_new_map_btn())
            self.utils.print_info("New map button found")
        else:
            self.utils.print_info("Organisation already existed")
            return 1
        if self.ml_insights_plan_web_elements.get_n360_plan_map_organization_text():
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_plan_map_organization_text())
            sleep(3)
        else:
            self.utils.print_info("Organisation already existed")
            return 1

        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_map_organization_text(),organization)
        sleep(3)
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_create_map_street_address(), street)
        sleep(3)
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_plan_map_city_text(), city)
        if self.ml_insights_plan_web_elements.get_n360_country_list_click():
            self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_country_list_click())
        else:
            self.utils.print_info("No button found")
        sleep(3)
        list_item = self.ml_insights_plan_web_elements.get_n360_country_change_item()
        found_country = False
        if list_item:
            self.utils.print_info("Select the country")
            self.utils.print_info(country)
            for opt in list_item:
                if country in opt.text:
                    self.utils.print_info("Selected country: {}".format(opt.text))
                    self.auto_actions.click(opt)
                    found_country = True
            if found_country:
                self.utils.print_info("Country found")
        else:
            self.utils.print_info("List country not found")
            return -1
        if self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_plan_map_save_btn()):
            self.utils.print_info("Click on save button")
        else:
            self.utils.print_info("Save button not found")
            return -1
        sleep(3)
        if self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_click_x_button()):
            self.utils.print_info("Click on close button Floor Plan")
        else:
            self.utils.print_info("Close button not found")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_extend_floor())
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_click_floor())
        self.utils.print_info("Click on Upload floor map")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_upload_floor_map())
        sleep(3)
        self.utils.print_info("Choose from Library")
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_choose_from_library())
        sleep(3)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_choose_image())
        sleep(3)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_save_button_floor())
        sleep(3)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_size_floor_plan())
        sleep(3)
        self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_width_floor(), width)
        sleep(3)
        #Comment below lines until XIQ-8469 will be resolved 
        #self.auto_actions.send_keys(self.ml_insights_plan_web_elements.get_n360_height_floor(), height)
        #sleep(3)
        self.auto_actions.click(self.ml_insights_plan_web_elements.get_n360_apply_button())
        return 1