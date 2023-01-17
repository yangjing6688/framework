import re
from time import sleep
from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_location.ExtremeLocationWebElements import ExtremeLocationWebElements
from selenium.common.exceptions import *
from extauto.common.CommonValidation import CommonValidation


class ExtremeLocation(ExtremeLocationWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    def subscribe_extreme_location_essentials(self):
        """
        - This keyword Will Subscribe extreme location essentials
        - Flow: Extreme Location--> Subscribe-->Apply

        :return:
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_location_menu()
        sleep(15)

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_extreme_location_subscribe_page().is_displayed():
            self.utils.print_info("Click Extreme Location Subscribe button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click Extreme Location Subscribe Apply button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_apply_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed Extreme Location Page")
        return 1

    def _go_to_extreme_location_page(self):
        """
        - This keyword Will Navigate to Extreme Location Menu Window
        - Flow: Extreme Location--> More Insights-->Extreme Location Menu Window

        :return: 1 if navigation success
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_location_menu()
        sleep(15)

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_extreme_location_subscribe_page().is_displayed():
            self.utils.print_info("Click Extreme Location Subscribe button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click Extreme Location Subscribe Apply button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_apply_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed Extreme Location Page")

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        self.utils.print_info("Click More Insights button")
        self.auto_actions.click_reference(self.get_extreme_location_more_insights_tab)
        sleep(15)

        self.utils.print_info("Switch to New Extreme Location Window")
        CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[1])

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)

        return 1

    def _go_to_extreme_location_devices_menu(self):
        """
        - This keyword Will Navigate to Devices Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Devices

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_devices_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_sites_menu(self):
        """
        - This keyword Will Navigate to Sites Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Sites

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_sites_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def _search_common_object(self, search_string):
        """
        Search the passed search string object in grid rows
        :param search_string:
        :return search value if value is present:
        :return False: if search value is not present
        """
        self.utils.print_info("Entering the Ibeacon Name in search field: ", search_string)
        self.auto_actions.click(self.get_xloc_search_name_field())
        self.auto_actions.send_keys(self.get_xloc_search_name_field(), search_string)
        sleep(2)
        passed_value = self.get_common_object_grid_rows()
        pass1 = passed_value.text
        if pass1 == search_string:
            self.screen.save_screen_shot()
            return passed_value
        self.utils.print_info(f"common object row {search_string} not present")
        return False

    def go_to_extreme_location_category_menu(self):
        """
        - This keyword Will Navigate to Category Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Category

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_category_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_access_points_menu(self):
        """
        - This keyword Will Navigate to Access Points Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Access Points

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_access_points_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_beacons_menu(self):
        """
        - This keyword Will Navigate to Beacons Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Beacons

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_beacons_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_asset_management_menu(self):
        """
        - This keyword Will Navigate to Asset Management Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Asset Management

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_asset_management_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_asset_management_assets_menu(self):
        """
        - This keyword Will Navigate to Asset Management Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Asset Management-->Assets

        :return:
        """
        self.go_to_extreme_location_asset_management_menu()
        self.navigator.navigate_to_extreme_location_assets_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_asset_management_alarm_menu(self):
        """
        - This keyword Will Navigate to Asset Management Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Asset Management-->Alarm

        :return:
        """
        self.go_to_extreme_location_asset_management_menu()
        self.navigator.navigate_to_extreme_location_alarms_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_devices_wireless_devices_menu(self):
        """
        - This keyword Will Navigate to Wireless Devices Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Devices-->Wireless Devices

        :return:
        """
        self._go_to_extreme_location_page()

        self.navigator.navigate_to_extreme_location_devices_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_devices_bss_devices_menu(self):
        """
        - This keyword Will Navigate to BSS Devices Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Devices-->BSS Devices

        :return:
        """
        self._go_to_extreme_location_devices_menu()
        self.navigator.navigate_to_extreme_location_bss_devices_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def _go_to_extreme_location_settings_menu(self):
        """
        - This keyword Will Navigate to Settings Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Settings

        :return:
        """
        self._go_to_extreme_location_page()
        self.navigator.navigate_to_extreme_location_settings_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_settings_device_classification_menu(self):
        """
        - This keyword Will Navigate to device classification Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Settings-->Device Classification

        :return:
        """
        self._go_to_extreme_location_settings_menu()
        self.navigator.navigate_to_extreme_location_device_classification_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_settings_thresholds_menu(self):
        """
        - This keyword Will Navigate to Thresholds Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Settings-->Thresholds

        :return:
        """
        self._go_to_extreme_location_settings_menu()
        self.navigator.navigate_to_extreme_location_threshold_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_settings_third_party_config_menu(self):
        """
        - This keyword Will Navigate to Third Party Configuration Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Settings-->Third Party Configuration

        :return:
        """
        self._go_to_extreme_location_settings_menu()
        self.navigator.navigate_to_extreme_location_third_party_config_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_location_settings_alarms_menu(self):
        """
        - This keyword Will Navigate to Alarm Settings Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Settings-->Alarms

        :return:
        """
        self._go_to_extreme_location_settings_menu()
        self.navigator.navigate_to_extreme_location_settings_alarms_submenu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def check_location_assigned_to_ap_in_xloc(self, device_hostname, dev_location, **kwargs):
        """
        - This Keyword Will check new location assigned to AP in XLOC AP Page
        - Flow: Extreme Location--> More Insights--> AP page--> New location assgined to AP
        - Keyword Usage:
        - ``Check Location Assigned to AP in XLOC     ${AP1_SERIAL}       ${NEW_LOCATION}``
        :param device_hostname: hostname of access point
        :param dev_location: location hierarchy in terms of location, building, floor
        :return: 1 if edited location is successfully seen in ADSP Sensor page else -1
        """

        self.go_to_extreme_location_access_points_menu()

        self.utils.print_info("Clicking search button on XLOC AP page")
        self.auto_actions.click_reference(self.get_search_xloc_ap_page)

        self.utils.print_info("Seraching ap hostname in XLOC APp page")
        self.auto_actions.send_keys(self.get_host_to_xloc_ap_page(), device_hostname)

        location_list = dev_location.split(',')
        location_list_floor = location_list[-1]
        location_list_building = location_list[-2]
        observed_building = self.get_device_building_from_xloc().text
        observed_floor = self.get_device_floor_from_xloc().text
        self.utils.print_info("Expected building string: ", location_list_building)
        self.utils.print_info("Device location from XLOC AP page: ", observed_building)
        self.utils.print_info("Expected floor string: ", location_list_floor)
        self.utils.print_info("Device Floor from XLOC AP page: ", observed_floor)

        if location_list_building.strip() in observed_building and location_list_floor.strip() in observed_floor:
            self.utils.print_info("Edited/Assigned Location is successfully seen in XLOC AP page")
            return 1
        else:
            kwargs['fail_msg'] = "'check_location_assigned_to_ap_in_xloc()' -> Edited/Assigned Location cannot be seen" \
                                 " in XLOC AP page"
            self.common_validation.failed(**kwargs)
            return -1

    def get_client_information_in_extreme_location_devices_page(self, client_mac=None, site_name=None, retry_duration=30, retry_count=5, **kwargs):
        """
        - get client information in extreme location devices page
        - - Flow: Extreme Location--> More Insights--> Devices-->Wireless Devices
        - Keyword Usage:
        - ``Get Client Information In Extreme Location Devices Page    ${CLIENT_MAC}   ${SITE_NAME}``

        :param client_mac: client mac address
        :param site_name: Device Assigned Site Name
        :return: client details dictionary if MAC entry found on Wireless Devices grid else -1
        """

        self.utils.print_info("Clicking Site Name Drop Down Button")
        self.auto_actions.click_reference(self.get_devices_wireless_devices_sites_dropdown_button)
        sleep(2)

        self.utils.print_info("select the Site Name: ", site_name)
        site_name_items = self.get_devices_wireless_devices_sites_dropdown_items()
        for el in site_name_items:
            if not el:
                pass
            if site_name.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
            print(el.text)
        sleep(3)

        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Client Mac Searching Check - Loop: {count}")
            self.utils.print_info(f"Time elapsed for searching {retry_duration} seconds")
            self.refresh_button_eloc_devices_page()
            self.screen.save_screen_shot()
            sleep(2)

            if client_mac:
                self.utils.print_info("Search grid based on Client Mac search filter")
                self.utils.print_info("Entering search_string  ", client_mac)
                self.screen.save_screen_shot()
                sleep(2)
                self.auto_actions.send_keys(self.get_devices_wireless_devices_search_textfield(), client_mac)
                sleep(2)

                self.screen.save_screen_shot()
                sleep(5)

                self.utils.print_info("Checking Client Mac Entry Row in Grid")
                row = self.get_grid_row()
                if row:
                    wireless_device_details = self._get_wireless_device_details()
                    return wireless_device_details
                if not row:
                    self.utils.print_info(f"Wireless Device Information For:{client_mac} is not Found")
                    self.utils.print_info(f"Did not find client mac. Waiting for {retry_duration} seconds...")
                    sleep(retry_duration)
                count += 1

        kwargs['fail_msg'] = "'get_client_information_in_extreme_location_devices_page()' -> Client mac failed to" \
                             " display on Devices Page. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def _get_wireless_device_details(self):
        """
        - This keyword gets Client Information from Extreme Location Devices Page
        - It Assumes That Already Navigated to Extreme Location Devices Page
        - Flow : Devices Page

        :return: dictionary of client Entry information
        """

        self.utils.print_info("Getting Wireless device Grid Information.")
        wireless_device_info = {}
        wireless_device_info["client_mac"] = self.get_devices_wireless_devices_client_mac_textfield().text
        wireless_device_info["host_name"] = self.get_devices_wireless_devices_host_name_textfield().text
        wireless_device_info["ip_address"] = self.get_devices_wireless_devices_ip_address_textfield().text
        wireless_device_info["user_name"] = self.get_devices_wireless_devices_user_name_textfield().text
        wireless_device_info["device_type"] = self.get_devices_wireless_devices_device_type_textfield().text
        wireless_device_info["floor_name"] = self.get_devices_wireless_devices_floor_name_textfield().text
        wireless_device_info["category"] = self.get_devices_wireless_devices_category_textfield().text
        wireless_device_info["site_enter_time"] = self.get_devices_wireless_devices_site_enter_time_textfield().text
        wireless_device_info["category_enter_time"] = self.get_devices_wireless_devices_category_enter_time_textfield().text

        self.utils.print_info("******************Wireless device Grid Information************************")
        for key, value in wireless_device_info.items():
            self.utils.print_info(f"{key}:{value}")

        return wireless_device_info

    def validate_client_entry_in_extreme_location_sites_page(self, site_name=None, floor_name=None, client_mac=None, retry_duration=30, retry_count=5, **kwargs):
        """
        - validate_client_entry_in_extreme_location_sites_page
        - Flow : Extreme Location--> More Insights-->Sites
        - Keyword Usage:
        - ``Validate Client Entry In Extreme Location Sites Page    ${SITE_NAME}   ${CLIENT_MAC}``

        :param site_name: Site_name to View the Wireless Device
        :param floor_name: Floor name to View the Wireless Device
        :param client_mac: Mac Address of the Wireless Device
        :return: Mac entry of Client if its founds on site Floor plan search text field
        """

        self.navigator.navigate_to_extreme_location_sites_menu()
        sleep(2)

        self.utils.print_info("Clicking Site Name Drop Down Button")
        self.auto_actions.click_reference(self.get_extreme_location_sites_menu_dropdown_button)
        sleep(2)

        self.utils.print_info("select the Site Name: ", site_name)
        site_name_items = self.get_extreme_location_sites_menu_dropdown_items()
        for el in site_name_items:
            if not el:
                pass
            if site_name.upper() in el.text.upper():
                self.auto_actions.click(el)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(el.text)
        sleep(3)

        self.utils.print_info("Clicking Site Name Icon")
        self.auto_actions.click_reference(self.get_extreme_location_sites_name_icon)
        sleep(2)

        self.utils.print_info("Clicking Floor Link for the Selected Site")
        self.auto_actions.click_reference(self.get_extreme_location_sites_name_floor_link)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Floor name Name Drop Down Button")
        self.auto_actions.click_reference(self.get_extreme_location_sites_menu_floor_name_dropdown_button)
        sleep(2)

        self.utils.print_info("Selecting the Floor Name")
        self.auto_actions.select_drop_down_options(self.get_extreme_location_sites_menu_floor_name_dropdown_items(),
                                                   floor_name)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Client Mac Searching Check - Loop: {count}")
            self.utils.print_info(f"Time elapsed for searching {retry_duration} seconds")
            self.refresh_button_eloc_sites_page()
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Entering Client MAC search_string  ", client_mac)
            self.auto_actions.send_keys(self.get_extreme_location_sites_client_mac_search_textfield(), client_mac)
            sleep(4)

            """
            mac_suggestion_presence = self.get_extreme_location_sites_client_mac_search_suggestions_textfield().text
            self.utils.print_info("Auto suggestion Text after Entering Client MAC :", mac_suggestion_presence)
            sleep(2)
            """

            self.screen.save_screen_shot()
            sleep(2)

            self.auto_actions.send_enter(self.get_extreme_location_sites_client_mac_search_textfield())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

            if not self.get_extreme_location_sites_device_preference_apply_button_disabled().is_displayed():
                self.utils.print_info("Client Entry Present In the Selected the Location")
                self.utils.print_info("Clicking Apply Button")
                self.auto_actions.click_reference(self.get_extreme_location_sites_device_preference_apply_button)
                sleep(5)

                self.screen.save_screen_shot()
                sleep(2)

                search_mac_entry = self.get_extreme_location_sites_client_mac_search_entered_textfield().text
                return search_mac_entry
            else:
                self.utils.print_info("Client Entry Not Present In the Selected the Location")
                self.utils.print_info(f"Did not find client mac. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "'validate_client_entry_in_extreme_location_sites_page()' -> Client mac failed to display" \
                             " on floor. Please check."
        self.common_validation.failed(**kwargs)
        return -1

    def async_subscribe_extreme_location_essentials(self, presence='enable', ibeacon='enable'):
        """
        - This keyword Will Subscribe extreme location essentials and enable or disable the presence and ibeaocn option on subscription window
        - Flow: Extreme Location--> Subscribe-->Presence=enable or disable --> Apply

        :return:
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_location_menu()
        sleep(15)

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_extreme_location_subscribe_page().is_displayed():
            self.utils.print_info("Click Extreme Location Subscribe button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            if presence == 'enable':
                self.utils.print_info("Enable Presence button")
                self.auto_actions.enable_check_box(self.get_extreme_location_subscribe_async_presence_button())

            if presence == 'disable':
                self.utils.print_info("disable Presence button")
                self.auto_actions.disable_check_box(self.get_extreme_location_subscribe_async_presence_button())

            if ibeacon == 'enable':
                self.utils.print_info("Enable Ibeacon button")
                #self.auto_actions.click_reference(self.get_extreme_location_subscribe_async_ibeacon_button)
                self.auto_actions.enable_check_box(self.get_extreme_location_subscribe_async_ibeacon_button())


            if ibeacon == 'disable':
                self.utils.print_info("Disable Ibeacon button")
                self.auto_actions.disable_check_box(self.get_extreme_location_subscribe_async_ibeacon_button())
                #self.auto_actions.click_reference(self.get_extreme_location_subscribe_async_ibeacon_button)

            self.utils.print_info("Click Extreme Location Subscribe Apply button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_apply_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed Extreme Location Page")
        return 1

    def go_to_extreme_location_xloc_application(self, **kwargs):
        """
        - This keyword Will Navigate to Wireless Devices Menu on Extreme Location Page
        - Flow: Extreme Location--> More Insights

        :return:
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_location_menu()
        sleep(15)

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_extreme_location_subscribe_page().is_displayed():
            self.utils.print_info("Click Extreme Location Subscribe button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click Extreme Location Subscribe Apply button")
            self.auto_actions.click_reference(self.get_extreme_location_subscribe_apply_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed Extreme Location Page")

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(20)

        obj_type = self.get_xloc_authentication_error()
        if type(obj_type) == bool:
            self.utils.print_info("No Authentication Error Seen")

        if type(obj_type) == list:
            kwargs['fail_msg'] = "'go_to_extreme_location_xloc_application()' -> Authentication Error Seen"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Click More Insights button")
        self.auto_actions.click_reference(self.get_extreme_location_more_insights_tab)
        sleep(15)

        return 1

    def create_wifi_asset_in_xloc(self, wifi_asset_name, xloc_site_name, as_category_name, client_mac, confined_category='default', prohibited_category='default'):
        """
        - create_wifi_asset_in_xloc
        - Flow : Extreme Location--> More Insights-->Asset Management-->Assets
        - Keyword Usage:
        - ``Create WIFI Asset In XLOC    ${WIFI_ASSET_NAME}   ${XLOC_SITE_NAME}   ${AS_CATEGORY_NAME}    ${CLIENT_MAC}   ${CONFINED_CATEGORY_NAME}   ${PROHIBITED_CATEGORY_NAME}``

        :param wifi_asset_name: Name of the WIFI Asset
        :param xloc_site_name: Site name for which asset needs to be created
        :param as_category_name: Name of the Asset Category
        :param client_mac: Mac Address of the Wireless Device for wifi asset
        :param confined_category: name of confined category
        :param prohibited_category: name of prohibited category
        :return: 1 if successfully created wifi asset
        """

        self.utils.print_info("Clicking Add button of Assets Page in XLOC-Asset Management")
        self.auto_actions.click_reference(self.get_extreme_location_asset_add_button)
        sleep(3)

        self.utils.print_info("Entering Asset Name", wifi_asset_name)
        self.auto_actions.send_keys(self.get_xloc_assetname_textfield(), wifi_asset_name)
        sleep(4)

        self.utils.print_info("Clicking drop down button of sites in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_sites_click)
        sleep(3)
        self.utils.print_info("Searching the Site Name: ", xloc_site_name)
        self.auto_actions.send_keys(self.get_xloc_asset_sites_search_field(), xloc_site_name)
        sleep(2)
        self.utils.print_info("Clicking drop down button of sites in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_sites_search_click)
        sleep(3)

        self.utils.print_info("Clicking drop down button of asset category in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_assetcategory_click)
        sleep(3)

        self.utils.print_info("Select the Asset Category Name: ", as_category_name)
        as_name_items = self.get_xloc_asset_assetcategory_dropdown_items()
        for ele in as_name_items:
            if not ele:
                pass
            if as_category_name.upper() in ele.text.upper():
                self.auto_actions.click(ele)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(ele.text)
        sleep(3)

        self.auto_actions.scroll_down()
        sleep(2)

        self.utils.print_info("Selecting WIFI Asset button")
        self.auto_actions.click_reference(self.enable_wifi_button)
        sleep(2)

        self.utils.print_info("Entering WIFI MAC Address for WIFI Asset: ", client_mac)
        client_mac_formatted = ':'.join(client_mac[i:i+2] for i in range(0,12,2))
        self.utils.print_info("Entering the Client Mac Address with format: ", client_mac_formatted)
        self.auto_actions.send_keys(self.get_xloc_wifi_asset_mac(), client_mac_formatted)
        sleep(4)

        if confined_category != 'default':
            self.utils.print_info("Clicking drop down button of confined category in assets page")
            self.auto_actions.click_reference(self.get_xloc_asset_cc_click)
            sleep(3)
            self.utils.print_info("Select the Confined Category: ", confined_category)
            cc_name_items = self.get_xloc_asset_cc_dropdown_items()
            for eleme in cc_name_items:
                if not eleme:
                    pass
                if confined_category.upper() in eleme.text.upper():
                    self.auto_actions.click(eleme)

                    self.screen.save_screen_shot()
                    sleep(2)
                    break
                print(eleme.text)
            sleep(3)

        if prohibited_category != 'default':
            self.utils.print_info("Clicking drop down button of prohibited category in assets page")
            self.auto_actions.click_reference(self.get_xloc_asset_pc_click)
            sleep(3)
            self.utils.print_info("Select the Prohibited Category: ", prohibited_category)
            pc_name_items = self.get_xloc_asset_pc_dropdown_items()
            for elemen in pc_name_items:
                if not elemen:
                    pass
                if prohibited_category.upper() in elemen.text.upper():
                    self.auto_actions.click(elemen)

                    self.screen.save_screen_shot()
                    sleep(2)
                    break
                print(elemen.text)
            sleep(3)

        self.utils.print_info("Clicking Save button of created Assets in XLOC-Asset Management")
        self.auto_actions.click_reference(self.get_extreme_location_asset_save_button)
        sleep(3)

        self.utils.print_info("Successfully Created WIFI Assets in Asset Management Page")
        sleep(3)

        return 1

    def create_ble_asset_in_xloc(self, ble_asset_name, xloc_site_name, as_category_name, ibeacon_name, confined_category='default', prohibited_category='default'):
        """
        - create_ble_asset_in_xloc
        - Flow : Extreme Location--> More Insights-->Asset Management-->Assets
        - Keyword Usage:
        - ``Create BLE Asset In XLOC    ${BLE_ASSET_NAME}   ${XLOC_SITE_NAME}   ${AS_CATEGORY_NAME}    ${IBEACON_NAME}   ${CONFINED_CATEGORY_NAME}   ${PROHIBITED_CATEGORY_NAME}``

        :param ble_asset_name: Name of the BLE Asset
        :param xloc_site_name: Site name for which asset needs to be created
        :param as_category_name: Name of the Asset Category
        :param ble_asset: BLE Asset
        :param ibeacon_name: name of ibeacon for ble asset
        :param confined_category: name of confined category
        :param prohibited_category: name of prohibited category
        :return: 1 if successfully created ble asset
        """

        self.utils.print_info("Clicking Add button of Assets Page in XLOC-Asset Management")
        self.auto_actions.click_reference(self.get_extreme_location_asset_add_button)
        sleep(3)

        self.utils.print_info("Entering Asset Name", ble_asset_name)
        self.auto_actions.send_keys(self.get_xloc_assetname_textfield(), ble_asset_name)
        sleep(4)

        self.utils.print_info("Clicking drop down button of sites in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_sites_click)
        sleep(3)
        self.utils.print_info("Searching the Site Name: ", xloc_site_name)
        self.auto_actions.send_keys(self.get_xloc_asset_sites_search_field(), xloc_site_name)
        sleep(2)
        self.utils.print_info("Clicking drop down button of sites in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_sites_search_click)
        sleep(3)

        self.utils.print_info("Clicking drop down button of asset category in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_assetcategory_click)
        sleep(3)

        self.utils.print_info("Select the Asset Category Name: ", as_category_name)
        as_name_items = self.get_xloc_asset_assetcategory_dropdown_items()
        for ele in as_name_items:
            if not ele:
                pass
            if as_category_name.upper() in ele.text.upper():
                self.auto_actions.click(ele)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(ele.text)
        sleep(3)

        self.utils.print_info("Selecting BLE Asset button")
        self.auto_actions.click_reference(self.enable_ble_button)
        sleep(5)

        self.utils.print_info("Clicking drop down button of ibeacon in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_ibeacon_click)
        sleep(3)
        self.utils.print_info("Ibeacon from dropdown: ", ibeacon_name)
        ibeacon_name_items = self.get_xloc_asset_ibeacon_dropdown_items()
        for elem in ibeacon_name_items:
            if not elem:
                pass
            if ibeacon_name.upper() in elem.text.upper():
                self.auto_actions.click(elem)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(elem.text)
        sleep(3)

        if confined_category != 'default':
            self.utils.print_info("Clicking drop down button of confined category in assets page")
            self.auto_actions.click_reference(self.get_xloc_asset_cc_click)
            sleep(3)
            self.utils.print_info("Select the Confined Category: ", confined_category)
            cc_name_items = self.get_xloc_asset_cc_dropdown_items()
            for eleme in cc_name_items:
                if not eleme:
                    pass
                if confined_category.upper() in eleme.text.upper():
                    self.auto_actions.click(eleme)

                    self.screen.save_screen_shot()
                    sleep(2)
                    break
                print(eleme.text)
            sleep(3)

        if prohibited_category != 'default':
            self.utils.print_info("Clicking drop down button of prohibited category in assets page")
            self.auto_actions.click_reference(self.get_xloc_asset_pc_click)
            sleep(3)
            self.utils.print_info("Select the Prohibited Category: ", prohibited_category)
            pc_name_items = self.get_xloc_asset_pc_dropdown_items()
            for elemen in pc_name_items:
                if not elemen:
                    pass
                if prohibited_category.upper() in elemen.text.upper():
                    self.auto_actions.click(elemen)

                    self.screen.save_screen_shot()
                    sleep(2)
                    break
                print(elemen.text)
            sleep(3)

        self.utils.print_info("Clicking Save button of created Assets in XLOC-Asset Management")
        self.auto_actions.click_reference(self.get_extreme_location_asset_save_button)
        sleep(3)

        self.utils.print_info("Successfully Created BLE Assets in Asset Management Page")
        sleep(3)

        return 1

    def create_none_asset_in_xloc(self, none_asset_name, xloc_site_name, as_category_name, confined_category='default', prohibited_category='default'):
        """
        - create_none_asset_in_xloc
        - Flow : Extreme Location--> More Insights-->Asset Management-->Assets
        - Keyword Usage:
        - ``Create None Asset In XLOC    ${NONE_ASSET_NAME}   ${XLOC_SITE_NAME}   ${AS_CATEGORY_NAME}    ${CONFINED_CATEGORY_NAME}   ${PROHIBITED_CATEGORY_NAME}``

        :param none_asset_name: Name of the None Asset
        :param xloc_site_name: Site name for which asset needs to be created
        :param as_category_name: Name of the Asset Category
        :param confined_category: name of confined category
        :param prohibited_category: name of prohibited category
        :return: 1 if successfully created none asset
        """

        self.utils.print_info("Clicking Add button of Assets Page in XLOC-Asset Management")
        self.auto_actions.click_reference(self.get_extreme_location_asset_add_button)
        sleep(3)

        self.utils.print_info("Entering Asset Name", none_asset_name)
        self.auto_actions.send_keys(self.get_xloc_assetname_textfield(), none_asset_name)
        sleep(4)

        self.utils.print_info("Clicking drop down button of sites in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_sites_click)
        sleep(3)
        self.utils.print_info("Searching the Site Name: ", xloc_site_name)
        self.auto_actions.send_keys(self.get_xloc_asset_sites_search_field(), xloc_site_name)
        sleep(2)
        self.utils.print_info("Clicking drop down button of sites in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_sites_search_click)
        sleep(3)

        self.utils.print_info("Clicking drop down button of asset category in assets page")
        self.auto_actions.click_reference(self.get_xloc_asset_assetcategory_click)
        sleep(3)

        self.utils.print_info("Select the Asset Category Name: ", as_category_name)
        as_name_items = self.get_xloc_asset_assetcategory_dropdown_items()
        for ele in as_name_items:
            if not ele:
                pass
            if as_category_name.upper() in ele.text.upper():
                self.auto_actions.click(ele)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(ele.text)
        sleep(3)

        self.utils.print_info("Selecting NONE Asset button")
        self.auto_actions.click_reference(self.enable_none_button)
        sleep(3)

        self.auto_actions.scroll_down()
        sleep(2)

        if confined_category != 'default':
            self.utils.print_info("Clicking drop down button of confined category in assets page")
            self.auto_actions.click_reference(self.get_xloc_asset_cc_click)
            sleep(3)
            self.utils.print_info("Select the Confined Category: ", confined_category)
            cc_name_items = self.get_xloc_asset_cc_dropdown_items()
            for eleme in cc_name_items:
                if not eleme:
                    pass
                if confined_category.upper() in eleme.text.upper():
                    self.auto_actions.click(eleme)

                    self.screen.save_screen_shot()
                    sleep(2)
                    break
                print(eleme.text)
            sleep(3)

        if prohibited_category != 'default':
            self.utils.print_info("Clicking drop down button of prohibited category in assets page")
            self.auto_actions.click_reference(self.get_xloc_asset_pc_click)
            sleep(3)
            self.utils.print_info("Select the Prohibited Category: ", prohibited_category)
            pc_name_items = self.get_xloc_asset_pc_dropdown_items()
            for elemen in pc_name_items:
                if not elemen:
                    pass
                if prohibited_category.upper() in elemen.text.upper():
                    self.auto_actions.click(elemen)

                    self.screen.save_screen_shot()
                    sleep(2)
                    break
                print(elemen.text)
            sleep(3)

        self.utils.print_info("Clicking Save button of created Assets in XLOC-Asset Management")
        self.auto_actions.click_reference(self.get_extreme_location_asset_save_button)
        sleep(3)

        self.utils.print_info("Successfully Created NONE Assets in Asset Management Page")
        sleep(3)

        return 1

    def delete_asset_in_xloc(self, asset_name, **kwargs):

        self.utils.print_info("Search grid based on Asset Name search filter")
        self.utils.print_info("Entering search_string for assetname  ", asset_name)
        self.auto_actions.send_keys(self.get_assets_search_textfield(), asset_name)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Checking Asset Name Entry Row in Grid")
        row = self.get_grid_row_assets()
        if not row:
            kwargs['fail_msg'] = f"'delete_asset_in_xloc()' -> Assets For:{asset_name} is not Found in the Assets Grid"
            self.common_validation.failed(**kwargs)
            return -1
        if row:
            self.utils.print_info(f"Deleting the asset:{asset_name} from Assets Grid")
            self.auto_actions.click_reference(self.get_delete_asset)
            self.screen.save_screen_shot()
            sleep(5)
            self.utils.print_info("Confirming deletion of asset by clicking Yes")
            self.auto_actions.click_reference(self.get_delete_asset_yes)
            sleep(2)
            self.screen.save_screen_shot()
            sleep(5)
            self.utils.print_info(f"Successfully deleted respective asset:{asset_name} from Assets Grid")
            sleep(2)

            return 1

    def edit_wifi_asset_in_xloc(self, asset_name, client_mac_new='default', confined_category='default', prohibited_category='default', **kwargs):
        self.utils.print_info("Search grid based on Asset Name search filter")
        self.utils.print_info("Entering search_string for assetname  ", asset_name)
        self.auto_actions.send_keys(self.get_assets_search_textfield(), asset_name)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Checking Asset Name Entry Row in Grid")
        row = self.get_grid_row_assets()
        if not row:
            kwargs['fail_msg'] = f"'edit_wifi_asset_in_xloc()' -> Assets For:{asset_name} is not Found in the" \
                                 " Assets Grid"
            self.common_validation.failed(**kwargs)
            return -1
        if row:
            self.utils.print_info(f"Click Actions for the asset:{asset_name} from Assets Grid")
            self.auto_actions.click_reference(self.get_actions_asset)
            self.screen.save_screen_shot()
            sleep(5)
            self.auto_actions.click_reference(self.get_actions_edit_asset)
            self.screen.save_screen_shot()
            sleep(5)

            if client_mac_new != 'default':
                self.auto_actions.scroll_down()
                sleep(2)
                self.utils.print_info("Selecting WIFI Asset button")
                self.auto_actions.click_reference(self.enable_wifi_button)
                sleep(2)
                self.utils.print_info("Entering New WIFI MAC Address for WIFI Asset: ", client_mac_new)
                client_mac_formatted = ':'.join(client_mac_new[i:i+2] for i in range(0,12,2))
                self.utils.print_info("Entering the Client Mac Address with format: ", client_mac_formatted)
                self.auto_actions.send_keys(self.get_xloc_wifi_asset_mac(), client_mac_formatted)
                sleep(4)

            if confined_category != 'default':
                self.utils.print_info("Clicking drop down button of confined category in assets page")
                self.auto_actions.click_reference(self.get_xloc_asset_cc_click)
                sleep(3)
                self.utils.print_info("Select the Confined Category: ", confined_category)
                cc_name_items = self.get_xloc_asset_cc_dropdown_items()
                for eleme in cc_name_items:
                    if not eleme:
                        pass
                    if confined_category.upper() in eleme.text.upper():
                        self.auto_actions.click(eleme)

                        self.screen.save_screen_shot()
                        sleep(2)
                        break
                    print(eleme.text)
                sleep(3)

            if prohibited_category != 'default':
                self.utils.print_info("Clicking drop down button of prohibited category in assets page")
                self.auto_actions.click_reference(self.get_xloc_asset_pc_click)
                sleep(3)
                self.utils.print_info("Select the Prohibited Category: ", prohibited_category)
                pc_name_items = self.get_xloc_asset_pc_dropdown_items()
                for elemen in pc_name_items:
                    if not elemen:
                        pass
                    if prohibited_category.upper() in elemen.text.upper():
                        self.auto_actions.click(elemen)

                        self.screen.save_screen_shot()
                        sleep(2)
                        break
                    print(elemen.text)
                sleep(3)

            self.utils.print_info("Clicking Save button of created Assets in XLOC-Asset Management")
            self.auto_actions.click_reference(self.get_extreme_location_asset_save_button)
            sleep(3)

            kwargs['pass_msg'] = "Successfully Created WIFI Assets in Asset Management Page"
            self.common_validation.passed(**kwargs)
            return 1

    def check_xloc_data_points_after_resetviq(self):
        """
        - This keyword Will check XLOC data points "Online Sensor" and "Live Devices" after reset viq
        - This keyword can be used only after performing reset viq
        - Keyword Usage:
        - `` Check Xloc Data Points After Resetviq ``

        :return: 1 if data points of XLOC are resetted to zero which confirms pass of reset viq feature wrt XLOC
            """

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_location_menu()
        sleep(20)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        self.utils.print_info("Clicking Refresh button of XLOC Summary")
        self.auto_actions.click_reference(self.click_refresh_xloc_summary_page)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking datapoint1 and datapoint2 of xloc summary page")
        sleep(2)

        datapoint1 = self.get_datapoint1_value_xloc().text
        self.utils.print_info("XLOC Datapoint1 value is: ", datapoint1)
        datapoint2 = self.get_datapoint2_value_xloc().text
        self.utils.print_info("XLOC Datapoint2 value is: ", datapoint2)

        if datapoint1 == '0' and datapoint2 == '0':
            self.utils.print_info("Data points are resetted to 0 and Reset VIQ wrt to XLOC is PASS")
            sleep(2)
        else:
            self.utils.print_info("Data points are NOT resetted to 0 and Reset VIQ wrt to XLOC is FAIL")
            sleep(2)

        return 1

    def create_xloc_third_party_ibeacon(self, ibeacon_name, uuid_name, xloc_site_name, as_category_name,
                                        ibeacon_mac_address, major_version="", minor_version="", **kwargs):
        """
        - This keyword Will create third party ibeacon on Extreme Location Page
        - Flow: Extreme Location--> More Insights-->Beacons->Onboard Third Party Ibeacon
        - Keyword Usage:
        - ``Create XLOC Third Party Ibeacon   ${IBEACON_NAME}   ${XLOC_SITE_NAME}   ${AS_CATEGORY_NAME}   ${IBEACON_MAC_ADDRESS}``

        :param ibeacon_name: name of the third party ibeacon
        :param xloc_site_name: name of xloc site
        :param as_category_name: name of asset category which is mapped to xloc_site_name
        :param ibeacon_mac_address: mac address of ibeacon
        :param ibeacon_rssi: rssi value of ibeacon
        :param ibeacon_adv_interval: advertisement interval of ibeacon
        :return: successfully creates asset category with the following details or else -1
        """

        self.go_to_extreme_location_beacons_menu()
        sleep(2)

        self.utils.print_info("Clicking Add Button of Third Party Ibeacon")
        self.auto_actions.click_reference(self.get_xloc_ibeacon_add_button)
        sleep(2)

        self.utils.print_info("Entering the Ibeacon Name: ", ibeacon_name)
        self.auto_actions.send_keys(self.get_xloc_ibeacon_name(), ibeacon_name)
        sleep(2)

        self.utils.print_info("Clicking Site Name Drop Down Button")
        self.auto_actions.click_reference(self.get_xloc_ibeacon_site_dropdown)
        sleep(2)

        self.utils.print_info("Selecting the Site Name for the ibeacon from dropdown: ", xloc_site_name)
        site_name_items = self.get_xloc_ibeacon_site_name()
        for ele in site_name_items:
            if not ele:
                pass
            if xloc_site_name.upper() in ele.text.upper():
                self.auto_actions.click(ele)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(ele.text)
        sleep(3)

        self.utils.print_info("Clicking Asset Category Drop Down Button")
        self.auto_actions.click_reference(self.get_xloc_ibeacon_as_category_dropdown)
        sleep(2)

        self.utils.print_info("Selecting the Asset Category Name for the ibeacon from dropdown: ", as_category_name)
        category_name_items = self.get_xloc_ibeacon_as_category_name()
        for elem in category_name_items:
            if not elem:
                pass
            if as_category_name.upper() in elem.text.upper():
                self.auto_actions.click(elem)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(elem.text)
        sleep(3)

        self.auto_actions.scroll_down()
        sleep(5)

        self.utils.print_info("Entering the Ibeacon Mac Address without format: ", ibeacon_mac_address)
        ibeacon_mac_address_formatted = ':'.join(ibeacon_mac_address[i:i+2] for i in range(0,12,2))
        self.utils.print_info("Entering the Ibeacon Mac Address with format: ",ibeacon_mac_address_formatted)
        self.auto_actions.send_keys(self.get_xloc_ibeacon_ibeacon_mac_address(), ibeacon_mac_address_formatted)
        sleep(2)

        self.utils.print_info("Entering the UUID Name: ", uuid_name)
        self.auto_actions.click_reference(self.get_xloc_uuid_name)
        self.auto_actions.send_keys(self.get_xloc_uuid_name(), uuid_name)
        sleep(2)

        self.utils.print_info("Entering the Major version: ", major_version)
        self.auto_actions.send_keys(self.get_xloc_major_version(), major_version)
        sleep(2)

        self.utils.print_info("Entering the Minor version: ", minor_version)
        self.auto_actions.send_keys(self.get_xloc_minor_version(), minor_version)
        sleep(2)

        self.utils.print_info("Clicking Save Button of Third party Ibeacon")
        self.auto_actions.click_reference(self.get_xloc_ibeacon_save)
        self.screen.save_screen_shot()

        try:
            if self.get_xloc_third_party_major_minor_error_message().is_displayed():
                self.screen.save_screen_shot()
                self.utils.print_info("configuration not saved sucessfully")
                kwargs['fail_msg'] = "'create_xloc_third_party_ibeacon()' -> configuration not saved sucessfully"
                self.common_validation.fault(**kwargs)
                return -1
        except Exception as e:
            self.utils.print_info("configuration sucessfully saved")
            self.screen.save_screen_shot()
            pass

        if self._search_common_object(ibeacon_mac_address):
            self.screen.save_screen_shot()
            self.utils.print_info(f"third party ibeacon {ibeacon_mac_address} created")
            kwargs['pass_msg'] = f"third party ibeacon {ibeacon_mac_address} created"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"third party ibeacon {ibeacon_mac_address} was not created"
            self.common_validation.failed(**kwargs)
            return -1

    def edit_Ibeacon_in_XLOC(self, ibeacon_mac_address, uuid_name, major_version="", minor_version="", **kwargs):

        """
        - edit_Ibeacon_in_XLOC
        - Flow : Extreme Location--> More Insights-->Asset Management-->Assets
        - Keyword Usage:
        - ``Edit Ibeacon in XLOC    ${IBEACON_MAC_ADDRESS}    ${uuid}    major_version=''    minor_version='' ``

        :return: 1 if successfully Edited
        :return: -1 if not successfully Edited
        """
        self.go_to_extreme_location_beacons_menu()
        sleep(2)

        self.utils.print_info("Search grid based on ibeacon mac address in search filter")
        self.utils.print_info("Entering search_string for ibeacon mac address  ", ibeacon_mac_address)

        self.auto_actions.click_reference(self.get_xloc_search_name_field)
        self.auto_actions.send_keys(self.get_xloc_search_name_field(), ibeacon_mac_address)
        sleep(2)

        self.utils.print_info("clicking view ibeacon details button")
        self.auto_actions.click_reference(self.get_view_ibeacon_details_button)

        sleep(2)
        self.utils.print_info("clicking xloc third party beacon edit button")
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_edit_button)

        sleep(2)
        self.utils.print_info("clicking xloc third party beacon edit settings")
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_settings)
        self.screen.save_screen_shot()

        sleep(2)
        self.utils.print_info("Entering the UUID Name: ", uuid_name)
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_uuid_text)
        self.auto_actions.send_keys(self.get_xloc_third_party_beacon_uuid_text(), uuid_name)
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Entering Major and Minor Version: ", major_version, minor_version)
        a = (str(major_version),str(minor_version))
        Formatted_major_minor_Value = ":".join(a)
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_major_minor_version)
        self.auto_actions.send_keys(self.get_xloc_third_party_beacon_major_minor_version(),Formatted_major_minor_Value)
        self.screen.save_screen_shot()

        sleep(2)
        self.utils.print_info("clicking xloc third party beacon save settings")
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_save_btn)
        self.screen.save_screen_shot()

        self.utils.print_info("verifying configuration sucessfully save")
        if self.get_xloc_third_party_success_message().is_displayed():
            self.screen.save_screen_shot()
            sleep(2)
            self.utils.print_info("configuration sucessfully saved")
            return 1
        else:
            kwargs['fail_msg'] = "'edit_Ibeacon_in_XLOC()' -> configuration not saved sucessfully"
            self.common_validation.failed(**kwargs)
            return -1


    def delete_ibeacon_in_xloc(self, ibeacon_mac_address, **kwargs):

        """
        - delete_ibeacon_in_xloc
        - Flow : Extreme Location--> More Insights-->Beacons->Delete selected Ibeacon
        - Keyword Usage:
        - ``Delete ibeacon in xloc    ${IBEACON_MAC_ADDRESS}``

        :return: 1 if successfully Deleted
        :return: -1 if not Deleted
        """

        self.go_to_extreme_location_beacons_menu()
        sleep(2)
        self.utils.print_info("Search grid based on ibeacon mac address in search filter")
        self.utils.print_info("Entering search_string for ibeacon mac address  ", ibeacon_mac_address)

        self.auto_actions.click_reference(self.get_xloc_search_name_field)
        self.auto_actions.send_keys(self.get_xloc_search_name_field(), ibeacon_mac_address)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking xloc ibeacon mac address in Grid")
        if self._search_common_object(ibeacon_mac_address):
            self.utils.print_info(f"third party ibeacon {ibeacon_mac_address} is avaliable")

        else:
            self.utils.print_info("third party ibeacon is not avaliable")
            kwargs['fail_msg'] = f"'edit_Ibeacon_in_XLOC()' -> third party ibeacon {ibeacon_mac_address}" \
                                 " is avaliable"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Clicking Delete Button")
        self.screen.save_screen_shot()
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_delete_button)

        sleep(2)
        self.utils.print_info("Clicking Confirm Button")
        self.screen.save_screen_shot()
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_confirm_button)
        sleep(2)
        self.screen.save_screen_shot()

        try:
            if self._search_common_object(ibeacon_mac_address):
                kwargs['fail_msg'] = f"'edit_Ibeacon_in_XLOC()' -> third party ibeacon {ibeacon_mac_address}" \
                                     " is avaliable"
                self.common_validation.fault(**kwargs)
                return -1
        except:
            self.utils.print_info("third party ibeacon is not avaliable")
            self.screen.save_screen_shot()
            kwargs['pass_msg'] = "third party ibeacon is not avaliable"
            self.common_validation.passed(**kwargs)
            return 1

    def get_ibeacon_status(self, ibeacon_mac_address, **kwargs):

        """
        - get_ibeacon_status
        - Flow : Extreme Location--> More Insights-->Beacons-->Get Ibeacon status
        - Keyword Usage:
        - ``Get ibeacon Status       ${IBEACON_MAC_ADDRESS}``

        :return: status of ibeacon(Online or Offline)
        :return: 1 if ibeacon in Online
        :return: -1 if ibeacon in Offline

        """

        self.utils.print_info("Getting the status of ibeacon")
        count = 1
        retry_duration = 10
        while True:
            try:
                while count <= 5:
                    self.utils.print_info(f"Ibeacon Online Status Check - Loop: {count}")
                    get_status_value  = self.get_common_object_grid_ap_status()
                    get_status_value = get_status_value.text
                    self.utils.print_info("",get_status_value)
                    if get_status_value == "Online":
                        self.screen.save_screen_shot()
                        self.utils.print_info("Ibeacon in Online State")
                        kwargs['pass_msg'] = "Ibeacon in Online State"
                        self.common_validation.passed(**kwargs)
                        return 1
                    elif get_status_value != "Online":
                        self.screen.save_screen_shot()
                        self.utils.print_info("Refreshing Ibeacon")
                        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_refresh_button)

                        sleep(2)
                        self.utils.print_info("Search grid based on ibeacon mac address in search filter")
                        self.utils.print_info("Entering search_string for ibeacon mac address  ", ibeacon_mac_address)
                        self.auto_actions.click_reference(self.get_xloc_search_name_field)
                        self.auto_actions.send_keys(self.get_xloc_search_name_field(), ibeacon_mac_address)
                        self.screen.save_screen_shot()
                        sleep(2)
                        self.utils.print_info(f"Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)
                    count += 1
                break
            except:
                pass
        kwargs['fail_msg'] = "Ibeacon in Offline State"
        self.common_validation.failed(**kwargs)
        return -1

    def download_ibeacon_report(self):

        """
        - download_ibeacon_report
        - Flow : Extreme Location--> More Insights-->
        - Keyword Usage:
        - ``Download ibeacon report``
        :return: 1 if successfully report download
        """

        self.go_to_extreme_location_beacons_menu()
        sleep(2)
        self.utils.print_info("downloading ibeacon report")
        self.utils.print_info("Clicking Download button")
        self.screen.save_screen_shot()
        self.auto_actions.click_reference(self.get_xloc_third_party_beacon_download_button)
        sleep(2)
        self.screen.save_screen_shot()
        return 1

    def create_time_based_device_classification_rule(self, user_type, visiting_hours="", visiting_minutes="", **kwargs):
        """
        - This Keyword will Create Time Based Device Classification Rule
        - Flow : Extreme Location--> More Insights--> Settings-->Device Classification–> Add Device Rule
        - Keyword Usage:
        - ``Create Time Based Device Classification Rule   ${USER_TYPE}   visiting_hours=${HOUR_TIME}   visiting_minutes=${MINUTES_TIME}``

        :param user_type: User Type Option
        :param visiting_hours: Visiting Time in Hours
        :param visiting_minutes: Visiting Time in Minutes
        :return:1 if Device Classification Rule Successfully else -1
        """

        self.go_to_extreme_location_settings_device_classification_menu()
        sleep(2)

        self.utils.print_info("Clicking Add Device Classification Button")
        self.auto_actions.click_reference(self.get_xloc_device_classification_add_button)
        sleep(2)

        self.utils.print_info("Clicking Add Device Rule Menu Button")
        self.auto_actions.click_reference(self.get_xloc_device_classification_add_device_rule_menu_button)
        sleep(2)

        self.utils.print_info("Clicking User Type Drop Down Button")
        self.auto_actions.click_reference(self.get_xloc_device_classification_user_type_drop_down_button)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info(f"Selecting User Type:{user_type} From Drop Down")
        self.auto_actions.select_drop_down_options(
            self.get_xloc_device_classification_user_type_drop_down_options(), user_type)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Visitor Duration Radio Button")
        self.auto_actions.click_reference(self.get_xloc_device_classification_visitor_duration_radio_button)
        sleep(2)

        if visiting_hours:
            self.utils.print_info("Entering Visiting Hours: ", visiting_hours)
            self.auto_actions.send_keys(self.get_xloc_device_classification_duration_hours_textfield(), visiting_hours)
            self.screen.save_screen_shot()
            sleep(2)

        if visiting_minutes:
            self.utils.print_info("Entering Visiting Minutes ", visiting_minutes)
            self.auto_actions.send_keys(self.get_xloc_device_classification_duration_minutes_textfield(), visiting_minutes)
            self.screen.save_screen_shot()
            sleep(2)
        self.utils.print_info("Clicking Save Button")
        self.auto_actions.click_reference(self.get_xloc_device_classification_save_button)
        sleep(5)
        self.screen.save_screen_shot()

        expected_duration = f"{visiting_hours} Hrs & {visiting_minutes} Min"
        self.utils.print_info('Getting Device Classification row...')
        rows = self.get_xloc_device_classification_rows()
        for row in rows:
            if user_type and expected_duration in row.text:
                self.utils.print_info(f'Device Classification Rule Created successfully with {user_type} '
                                      f'with Duration {expected_duration}')
                kwargs['pass_msg'] = f"Device Classification Rule Created successfully with {user_type} with Duration {expected_duration}"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "'create_time_based_device_classification_rule()' -> Device Classification Rule" \
                                     " Not Created successfully"
                self.common_validation.failed(**kwargs)
                return -1

    def update_ssid_in_device_rule(self, rule_type, ssid, option, **kwargs):
        """
        - This keyword is used to update SSID in device classification rule
        - Flow : Assumes already in Device classification rule page of Location
        - Keyword Usage:
        - ``Update SSID in device rule    ${RULE_TYPE}   ${SSID}    ${OPTION}``

        :param rule_type: rule type (eg: Assets/Faculty/Excluded Devices)
        :param ssid: SSID name to edit
        :param option: update option for SSID(either add or delete)
        :return: returns 1 if success else -1 or -2
        """

        self.utils.print_info("Getting the device classification rule rows")
        rows = self.get_device_classification_grid_row()
        if rows:
            self.utils.print_debug("Rule : ", rule_type)
            for idx, row in enumerate(rows):
                if rule_type.upper() in row.text.upper():
                    self.utils.print_info("Found Device Classification Rule : ", rule_type)

                    edit_rule_rows = self.get_device_classification_edit_btn()
                    self.screen.save_screen_shot()
                    self.utils.print_info("Editing device classification rule :", rule_type)

                    if re.search(r'x-item-disabled', edit_rule_rows[idx].get_attribute("class")):
                        self.utils.print_info("Edit option is disabled for rule : ", rule_type)
                        kwargs['fail_msg'] = "'update_ssid_in_device_rule()' -> Edit option is disabled for" \
                                             f" rule: {rule_type}"
                        self.common_validation.failed(**kwargs)
                        return -2
                    else:
                        self.auto_actions.click(edit_rule_rows[idx])

                    self.utils.print_info("Clicking on ssid option radio button ")
                    self.auto_actions.click_reference(self.get_device_classification_ssid_radio_btn)
                    ssid_text = self.get_device_classification_ssid_text_field().text

                    self.utils.print_debug("SSID text field content : ", ssid_text)
                    if option == "add":
                        if ssid in ssid_text:
                            self.utils.print_info("SSID already present :", ssid)
                            return 1
                        else:
                            self.utils.print_info("Adding SSID :", ssid)
                            self.auto_actions.move_to_element(self.get_device_classification_ssid_dropdown_button())
                            self.utils.print_info("Clicking on SSID dropdown button")
                            self.auto_actions.click_reference(self.get_device_classification_ssid_dropdown_button)
                            dd_items = self.get_device_classification_ssid_dropdown_items()
                            self.utils.print_info("Selecting SSID from dropdown")
                            self.auto_actions.select_drop_down_options(dd_items, ssid)
                            self.screen.save_screen_shot()
                            sleep(5)

                    elif option == "delete":
                        if ssid in ssid_text:
                            self.utils.print_info("Deleting SSID from rule :", rule_type)
                            ssid_list = self.get_device_classification_ssid_list()
                            self.screen.save_screen_shot()
                            for idx1, param in enumerate(ssid_list):
                                if ssid in param.text:
                                    close_buttons = self.get_device_classification_ssid_close_btn()
                                    self.utils.print_info("Deleting SSID :", ssid)
                                    self.auto_actions.click(close_buttons[idx1])
                                    sleep(2)
                        else:
                            self.utils.print_info("SSID not present to delete :", ssid)
                    self.utils.print_info("Saving the Device Classification Rule")
                    self.auto_actions.click_reference(self.get_device_classification_save_btn)
                    self.screen.save_screen_shot()
                    sleep(5)
                    return 1
        self.utils.print_info("Device classification rules not found")
        kwargs['fail_msg'] = "'update_ssid_in_device_rule()' -> Device classification rules not found"
        self.common_validation.failed(**kwargs)
        return -1

    def update_visitor_duration_for_device_rule(self, rule_type, duration, **kwargs):
        """
        - This keyword updates visitor duration for device classification rule
        - Flow : Assumes already in Device classification rule page of location.
        - Keyword Usage:
        - ``Update Visitor Duration For Device Rule    ${RULE_TYPE}   ${DURATION}``

        :param rule_type: rule type (eg: Assets/Faculty/Excluded Devices)
        :param duration: Duration in hours and minutes(eg: 2:30)
        :return: returns 1 if success else -1 or -2
        """
        self.utils.print_info("Getting the device classification rule rows")
        rows = self.get_device_classification_grid_row()
        hr_min = duration.split(":")

        if rows:
            self.utils.print_info("Updating Device classification rule : ", rule_type)

            for idx, row in enumerate(rows):
                if rule_type.upper() in row.text.upper():
                    self.utils.print_info("Found Device Classification Rule : ", self.format_row(row.text))

                    edit_rule_rows = self.get_device_classification_edit_btn()
                    self.screen.save_screen_shot()
                    self.utils.print_info("Editing Device Classification Rule :", rule_type)

                    if re.search(r'x-item-disabled', edit_rule_rows[idx].get_attribute("class")):
                        self.utils.print_info("Edit option is disabled for rule : ", rule_type)
                        kwargs['fail_msg'] = "'update_visitor_duration_for_device_rule()' -> Edit option is disabled" \
                                             f" for rule: {rule_type}"
                        self.common_validation.fault(**kwargs)
                        return -1
                    else:
                        self.auto_actions.click(edit_rule_rows[idx])

                    self.utils.print_info("Clicking on visitor duration radio button")
                    self.auto_actions.click_reference(self.get_visitor_duration_checkbox)

                    self.utils.print_info("Entering hours field for visitor duration")
                    self.auto_actions.send_keys(self.get_visitor_duration_hrs_textbox(), hr_min[0])
                    sleep(2)

                    self.utils.print_info("Entering minutes field for visitor duration")
                    self.auto_actions.send_keys(self.get_visitor_duration_min_textbox(), hr_min[1])
                    sleep(2)

                    self.utils.print_info("Saving the Device Classification Rule")
                    self.auto_actions.click_reference(self.get_device_classification_save_btn)
                    self.screen.save_screen_shot()
                    sleep(2)
                    return 1
        self.utils.print_info("Device classification rules not found")
        kwargs['fail_msg'] = "'update_visitor_duration_for_device_rule()' -> Device classification rules not found"
        self.common_validation.fault(**kwargs)
        return -1

    def format_row(self, row):
        cell_values = row.split("\n")
        formatted_row = list()
        for cell_value in cell_values:
            formatted_row.append(cell_value)
        return formatted_row

    def configure_xloc_third_party_configurations(self, subscriber_push_url, username, password):
        '''
        - This Keyword will Create Time Based Device Classification Rule
        - Flow : Extreme Location--> More Insights--> Settings-->Third Party Configurations
        - Keyword Usage:
        - ``Configure XLOC Third Party Configurations   ${SUBSCRIBER_PUSH_URL}   ${USERNAME}   ${PASSWORD}``

        :param subscriber_push_url: URL to be configured
        :param username: username for url
        :param password: password for url
        :return: 1 if able to successfully configure the required fields for third party configurations in XLOC else -1
        '''

        self.utils.print_info("Enter the Subscriber Push URL")
        self.auto_actions.click_reference(self.get_enter_subscriber_url)
        self.auto_actions.send_keys(self.get_enter_subscriber_url(), subscriber_push_url)
        sleep(2)

        self.utils.print_info("Enter the Username of URL")
        self.auto_actions.click_reference(self.get_enter_subscriber_url_username)
        self.auto_actions.send_keys(self.get_enter_subscriber_url_username(), username)
        sleep(2)

        self.utils.print_info("Enter the Password of URL")
        self.auto_actions.click_reference(self.get_enter_subscriber_url_password)
        self.auto_actions.send_keys(self.get_enter_subscriber_url_password(), password)
        sleep(2)

        self.utils.print_info("Clicking presence event")
        self.auto_actions.click_reference(self.get_click_presence_event)
        sleep(2)

        self.utils.print_info("Clicking category event")
        self.auto_actions.click_reference(self.get_click_category_event)
        sleep(2)

        self.utils.print_info("Clicking location event")
        self.auto_actions.click_reference(self.get_click_location_event)
        sleep(2)

        self.utils.print_info("Clicking rssi event")
        self.auto_actions.click_reference(self.get_click_rssi_event)
        sleep(2)

        self.utils.print_info("Clicking crowding event")
        self.auto_actions.click_reference(self.get_click_crowding_event)
        sleep(2)

        self.utils.print_info("Clicking alarm event")
        self.auto_actions.click_reference(self.get_click_alarm_event)
        sleep(2)

        self.utils.print_info("Successfully configured third party configurations")
        sleep(2)

        return 1

    def save_xloc_third_party_configurations(self, subscriber_push_url, username, password):
        '''
        - This Keyword will Create Time Based Device Classification Rule
        - Flow : Extreme Location--> More Insights--> Settings-->Third Party Configurations
        - Keyword Usage:
        - ``Save XLOC Third Party Configurations   ${SUBSCRIBER_PUSH_URL}   ${USERNAME}   ${PASSWORD}``

        :param subscriber_push_url: URL to be configured
        :param username: username for url
        :param password: password for url
        :return: 1 if able to successfully save required fields for third party configurations in XLOC else -1
        '''

        self.configure_xloc_third_party_configurations(subscriber_push_url, username, password)
        self.utils.print_info("Clicking Save button of third party configurations")
        self.auto_actions.click_reference(self.get_click_save_third_party_btn)
        sleep(2)

        self.utils.print_info("Successfully saved third party configurations")
        sleep(2)

        return 1

    def reset_xloc_third_party_configurations(self, subscriber_push_url, username, password):
        '''
        - This Keyword will Create Time Based Device Classification Rule
        - Flow : Extreme Location--> More Insights--> Settings-->Third Party Configurations
        - Keyword Usage:
        - ``Reset XLOC Third Party Configurations   ${SUBSCRIBER_PUSH_URL}   ${USERNAME}   ${PASSWORD}``

        :param subscriber_push_url: URL to be configured
        :param username: username for url
        :param password: password for url
        :return: 1 if able to successfully reset the required fields for third party configurations in XLOC
        '''

        self.configure_xloc_third_party_configurations(subscriber_push_url, username, password)
        self.utils.print_info("Clicking Reset button of third party configurations")
        self.auto_actions.click_reference(self.get_click_reset_third_party_btn)
        sleep(2)

        self.utils.print_info("Successfully Resetted third party configurations")
        sleep(2)

        return 1

    def check_xloc_test_connection_button(self, subscriber_push_url, username, password, **kwargs):
        '''
        - This Keyword will Create Time Based Device Classification Rule
        - Flow : Extreme Location--> More Insights--> Settings-->Third Party Configurations
        - Keyword Usage:
        - ``Check XLOC Test Connection Button   ${SUBSCRIBER_PUSH_URL}   ${USERNAME}   ${PASSWORD}``

        :param subscriber_push_url: URL to be configured
        :param username: username for url
        :param password: password for url
        :return: 1 if able to successfully test connection for the given subscriber push URL in third party configurations in XLOC else -1
        '''

        self.configure_xloc_third_party_configurations(subscriber_push_url, username, password)
        self.utils.print_info("Clicking Test Connection button of third party configurations")
        self.auto_actions.click_reference(self.get_click_test_connection_btn_third_party)
        sleep(2)

        xloc_test_connection_status = self.get_test_connection_xloc_status_textfield().text
        self.utils.print_info("Test Connection Status is:", xloc_test_connection_status)

        if "Test connection to third-party configuration successful." in xloc_test_connection_status:
            self.utils.print_info("Test Connection was Successful")
            sleep(2)
            self.utils.print_info("Closing Test Connection Status Window")
            self.auto_actions.click_reference(self.get_click_xloc_test_connection_close_btn)
            sleep(2)
            return 1
        else:
            self.utils.print_info("Test Connection was Failed")
            sleep(2)
            self.utils.print_info("Closing Test Connection Status Window")
            self.auto_actions.click_reference(self.get_click_xloc_test_connection_close_btn)
            sleep(2)
            kwargs['fail_msg'] = "'check_xloc_test_connection_button()' -> Test Connection was Failed"
            self.common_validation.failed(**kwargs)
            return -1

    def check_subscription_of_extreme_location_page(self, **kwargs):
        """
        - This keyword Will Check Extreme Location Page is Subscribed or Not after Reset VIQ
        - Flow: Login to XIQ -> Click XLOC Icon -> Check Subscription Status

        :return: 1 if not subscribed
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_location_menu()
        sleep(15)

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_extreme_location_subscribe_page().is_displayed():
            self.utils.print_info("Location Essentials Subscription Page is Visible")
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
            return 1
        else:
            kwargs['fail_msg'] = "'check_subscription_of_extreme_location_page()' -> Check for Auth Error or User" \
                                 " Already Subscribed to Extreme Location"
            self.common_validation.failed(**kwargs)
            return -1

    def create_engagement_category_xloc(self, en_category_name, en_category_threshold, xloc_site_name):
        """
        - This keyword Will Navigate to Create Engagement Category on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Category-->Engagement Category
        - Keyword Usage:
        - ``Create Engagement Category XLOC     ${EN_CATEGORY_NAME}     ${EN_CATEGORY_THRESHOLD}     ${XLOC_SITE_NAME}``

        :param en_category_name: name of engagement category
        :param en_category_threshold: value of category threshold
        :param xloc_site_name: Category Assigned Site Name
        :return: successfully create engagement category using given category name and map it to given site name else -1
        """
        self.go_to_extreme_location_category_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking XLOC Engagement Category")
        self.auto_actions.click_reference(self.click_xloc_engagement_category)

        self.utils.print_info("Clicking Add button of Engagement Category")
        self.auto_actions.click_reference(self.click_xloc_engagement_category_add)

        self.utils.print_info("Clicking Engagement Category Name Area and inputting category name:", en_category_name)
        self.auto_actions.send_keys(self.click_xloc_engagement_category_name(), en_category_name)
        sleep(2)

        self.utils.print_info("Clicking Engagement Category Threshold Area and inputting category threshold value:", en_category_threshold)
        self.auto_actions.send_keys(self.click_xloc_engagement_category_threshold(), en_category_threshold)
        sleep(2)

        self.utils.print_info("Clicking Engagement Category Save Button")
        self.auto_actions.click_reference(self.click_xloc_engagement_category_save)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Engagement Category Site Button")
        self.auto_actions.click_reference(self.click_xloc_engagement_category_site)
        sleep(2)

        self.utils.print_info("Clicking Engagement Category Site Edit Button")
        self.auto_actions.click_reference(self.click_xloc_engagement_category_site_edit)
        sleep(2)

        self.utils.print_info("Clicking Engagement Category Site Map Button")
        self.auto_actions.click_reference(self.click_xloc_engagement_category_site_map)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Selecting xloc site name in engagement category, site name:", xloc_site_name)
        xloc_site_name_items = self.get_xloc_category_site_list()
        for ele in xloc_site_name_items:
            if not ele:
                pass
            if xloc_site_name.upper() in ele.text.upper():
                self.auto_actions.click(ele)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(ele.text)
        sleep(3)

        self.utils.print_info("Clicking Engagement Category Site Select Next Button")
        self.auto_actions.click_reference(self.click_xloc_category_site_select_next)
        sleep(2)

        self.utils.print_info("Clicking Engagement Category Site Map Final Button")
        self.auto_actions.click_reference(self.click_xloc_category_site_map_final)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Successfully Created Engagement Category")
        sleep(2)

        return 1

    def create_asset_category_xloc(self, as_category_name, xloc_site_name):
        """
        - This keyword Will Navigate to Create Asset Category on Extreme Location Page
        - Flow: Extreme Location--> More Insights--> Category-->Asset Category
        - Keyword Usage:
        - ``Create Asset Category XLOC    ${AS_CATEGORY_NAME}     ${XLOC_SITE_NAME}``

        :param as_category_name: name of engagement category
        :param xloc_site_name: Category Assigned Site Name
        :return: successfully create asset category using given category name and map it to given site name else -1
        """
        self.go_to_extreme_location_category_menu()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking XLOC Asset Category")
        self.auto_actions.click_reference(self.click_xloc_asset_category)

        self.utils.print_info("Clicking Add button of Asset Category")
        self.auto_actions.click_reference(self.click_xloc_asset_category_add)

        self.utils.print_info("Clicking Asset Category Name Area and inputting category name:", as_category_name)
        self.auto_actions.send_keys(self.click_xloc_asset_category_name(), as_category_name)
        sleep(2)

        self.utils.print_info("Clicking Asset Category Save Button")
        self.auto_actions.click_reference(self.click_xloc_asset_category_save)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Asset Category Site Button")
        self.auto_actions.click_reference(self.click_xloc_asset_category_site)
        sleep(2)

        self.utils.print_info("Clicking Asset Category Site Edit Button")
        self.auto_actions.click_reference(self.click_xloc_asset_category_site_edit)
        sleep(2)

        self.utils.print_info("Clicking Asset Category Site Map Button")
        self.auto_actions.click_reference(self.click_xloc_asset_category_site_map)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Selecting xloc site name in asset category, site name:", xloc_site_name)
        xloc_site_name_items = self.get_xloc_category_site_list()
        for ele in xloc_site_name_items:
            if not ele:
                pass
            if xloc_site_name.upper() in ele.text.upper():
                self.auto_actions.click(ele)

                self.screen.save_screen_shot()
                sleep(2)
                break
            print(ele.text)
        sleep(3)

        self.utils.print_info("Clicking Asset Category Site Select Next Button")
        self.auto_actions.click_reference(self.click_xloc_category_site_select_next)
        sleep(2)

        self.utils.print_info("Clicking Asset Category Site Map Final Button")
        self.auto_actions.click_reference(self.click_xloc_category_site_map_final)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Successfully Created Asset Category")
        sleep(2)

        return 1

    def go_back_to_xloc(self):
        """
        - This keyword Will Navigate back to XIQ Window
        - Keyword Usage:
            ''Go Back To Xiq''

        :return: 1 if success
        """
        self.utils.print_info("Switch to XIQ Window")
        CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[0])

        return 1

    def switch_to_extreme_location_window(self, win_index=1):
        """
        - Switches to the specified window

        :param:  win_index - Index of the window to switch to
        :return: None
        """
        CloudDriver().switch_to_window(win_index)

    def close_extreme_location_window(self, win_index=1):
        """
        - Closes the specified window

        :param:  win_index - Index of the window to close
        :return: None
        """
        CloudDriver().close_window(win_index)