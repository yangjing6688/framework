from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.CopilotWebElements import CopilotWebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
import re
from extauto.common.CommonValidation import CommonValidation
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.manage.Tools import Tools


class Copilot(CopilotWebElements):
    def __init__(self):
        super().__init__()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()
        self.tools = Tools()
        self.devices_web_elements = DevicesWebElements()

    def enable_copilot_menu_feature(self, **kwargs):
        """
        - Enables CoPilot Feature in CoPilot Menu Page
        - Flow : CoPilot Menu Page
        - Keyword Usage
        - ``Enable CoPilot Menu Feature``
        :return: True if successfully enabled CoPilot feature or False if unable to enable feature
        """

        if self.navigator.navigate_to_copilot_menu() == 1:
            sleep(2)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.utils.print_info("Checking for Copilot button..")
        enable_copilot_button = self.get_enable_copilot_menu_feature_button()
        self.utils.print_info(f"Enable CoPilot Button: {enable_copilot_button}")
        alert_message = self.get_copilot_menu_alert_message_banner()
        self.utils.print_info(f"Alert Message: {alert_message}")

        if enable_copilot_button:
            # check for alert message
            if not self.get_copilot_menu_alert_message_banner():
                self.utils.print_info("Enabling CoPilot feature..")
                self.auto_actions.click_reference(self.get_enable_copilot_menu_feature_button)
                sleep(1)
                self.screen.save_screen_shot()
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                return True
            elif self.get_copilot_menu_alert_message_banner():
                kwargs['fail_msg'] = "'enable_copilot_menu_feature()' -> Unable to enable feature - CoPilot " \
                                     "deactivated due to lack of licenses"
                self.utils.print_info("Unable to enable feature - CoPilot deactivated due to lack of licenses")
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                self.common_validation.failed(**kwargs)
                return False
        else:
            kwargs['pass_msg'] = "'enable_copilot_menu_feature()' -> CoPilot feature already enabled"
            self.common_validation.passed(**kwargs)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return True

    def confirm_copilot_deactivated_due_to_lack_of_licenses_banner_displayed(self, **kwargs):
        """
        - This keyword confirms if the "CoPilot deactivated due to lack of licenses" banner message is displayed or not
        - Keyword Usage
        - ``Confirm CoPilot Deactivated Due To Lack Of Licenses Banner Displayed``

        :return: true if banner is displayed and return false if banner is not displayed
        """

        if self.devices_web_elements.get_ui_banner_warning_message():
            tool_tp_text_warning = self.devices_web_elements.get_ui_banner_warning_message()
            if "CoPilot deactivated due to lack of licenses" in tool_tp_text_warning.text:
                self.utils.print_info(tool_tp_text_warning.text)
                self.screen.save_screen_shot()
                return True
            else:
                self.utils.print_info(f"Warning Message: {tool_tp_text_warning.text}")
                self.screen.save_screen_shot()
                return False
        else:
            kwargs['fail_msg'] = "'confirm_copilot_deactivated_due_to_lack_of_licenses_banner_displayed()' -> " \
                                 "No warning message banner was found"
            self.common_validation.fault(**kwargs)
            return False

    def get_wifi_capacity_widget_summary(self, **kwargs):
        """
        - Gets wifi capacity widget summary in copilot
        - Flow : Copilot page -->Wifi Capacity widget
        - Keyword Usage
        - ``Get WiFi Capacity Widget Summary``
        - This keyword developed on q3r1 - g7r1 environment.
        :return: returns Buildings and APs count if success else returns -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Wi-Fi capacity widget Summary")
        self.utils.print_info("Widgets taking more than 10 sec to display, so adding adequate sleep")
        sleep(15)
        self.auto_actions.move_to_element(self.get_wifi_capacity_widget())
        self.screen.save_screen_shot()
        try:
            wifi_summary = self.get_wifi_capacity_content().text
            self.utils.print_info("Wi-Fi capacity widget Summary : ", wifi_summary)
            if re.search(r'(\d+) places .* (\d+) devices', wifi_summary):
                summary = re.search(r'(\d+) places .* (\d+) devices', wifi_summary)
                buildings = summary.group(1)
                aps = summary.group(2)

                self.utils.print_info("Total Buildings : ", buildings)
                self.utils.print_info("Total APs : ", aps)
                return buildings, aps
            else:
                kwargs['fail_msg'] = "'get_wifi_capacity_widget_summary()' -> Unable to get Buildings and APs " \
                                     "information in wifi capacity summary"
                self.common_validation.failed(**kwargs)
                return -2
        except Exception as e:
            kwargs['fail_msg'] = "'get_wifi_capacity_widget_summary()' -> Unable to get Wi-FI Summary"
            self.common_validation.fault(**kwargs)
            return -1

    def get_wifi_capacity_widget_status(self, **kwargs):
        """
        - Gets wifi capacity widget status in copilot
        - Flow : Copilot page -->Wifi Capacity widget
        - Keyword Usage
        - ``Get WiFi Capacity Widget Status``
        :return: returns status of show/hide muted button in wifi capacity widget-1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Wi-Fi capacity widget Summary")
        self.utils.print_info("Widgets taking more than 10 sec to display, so adding adequate sleep")
        sleep(15)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.auto_actions.move_to_element(self.get_wifi_capacity_widget())
        self.screen.save_screen_shot()
        try:
            wifi_capacity_status = self.get_wifi_capacity_status()
            self.utils.print_info("status of muted button in wifi capacity widget:", wifi_capacity_status.text)
            return wifi_capacity_status.text
        except Exception as e:
            kwargs['fail_msg'] = "'get_wifi_capacity_widget_status()' -> Unable to get status of muted button in " \
                                 "wifi capacity widget"
            self.common_validation.fault(**kwargs)
            return -1

    def pin_anomaly_for_location_in_wifi_capacity_widget(self, location_name, **kwargs):
        """
        - This Keyword will pin an anomaly at building level in wifi capacity widget
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get Location Name in Rows and Click Pin Button
        - Keyword Usage:
        - ``Pin Anomaly For location In WiFi Capacity Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in wifi capacity widget
        :return: 1 if able to click anomaly Pin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)

        for row in self.get_wifi_capacity_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting Pin Button for the Location: {location_name}")
                if not self.get_wifi_capacity_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Pin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_wifi_capacity_widget_location_pin_button(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_wifi_capacity_widget()' -> Pinned Anomaly " \
                                         f"successfully for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_wifi_capacity_widget()' -> Already Pinned " \
                                         f"Anomaly for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'pin_anomaly_for_location_in_wifi_capacity_widget()' -> Not found Location row " \
                             f"with name:{location_name}"
        self.common_validation.fault(**kwargs)
        return -1

    def unpin_anomaly_for_location_in_wifi_capacity_widget(self, location_name, **kwargs):
        """
        - This Keyword will unpin an anomaly at building level in wifi capacity widget
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get Location Name in Rows and Click UnPin Button
        - Keyword Usage:
        - ``Unpin Anomaly For location In WiFi Capacity Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in wifi capacity widget
        :return: 1 if able to click anomaly unpin button for the Location Name or already unpinned else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)

        for row in self.get_wifi_capacity_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting UnPin Button for the Location: {location_name}")
                if self.get_wifi_capacity_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Unpin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_wifi_capacity_widget_location_already_pinned_status(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'unpin_anomaly_for_location_in_wifi_capacity_widget()' -> Successfully " \
                                         f"UnPinned Anomaly for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_wifi_capacity_widget()' -> Already UnPinned " \
                                         f"Anomaly for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'unpin_anomaly_for_location_in_wifi_capacity_widget()' -> Not found Location row " \
                             f"with name:{location_name}"
        self.common_validation.fault(**kwargs)
        return -1

    def mute_anomaly_for_location_in_wifi_capacity_widget(self, location_name, **kwargs):
        """
        - This Keyword will mute an anomaly at building level in wifi capacity widget
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get Location Name in Rows and Click More options and mute Button
        - Keyword Usage:
        - ``Mute Anomaly For location In WiFi Capacity Widget   ${LOCATION_NAME}``


        :param location_name: Location name to Mute anomaly in wifi capacity widget
        :return: 1 if able to click anomaly Mute button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)

        if self.get_wifi_capacity_widget_location_muted_grid_rows():
            for row in self.get_wifi_capacity_widget_location_muted_grid_rows():
                if location_name in row.text:
                    kwargs['pass_msg'] = "'mute_anomaly_for_location_in_wifi_capacity_widget()' -> Already Mute " \
                                         f"Anomaly Enabled for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1
        else:
            for row in self.get_wifi_capacity_widget_location_grid_rows():
                if location_name in row.text:
                    self.utils.print_info(f"Selecting Mute Button for the Location: {location_name}")
                    self.utils.print_info("Clicking More Options Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_wifi_capacity_widget_location_more_options_button(row))
                    sleep(2)

                    self.utils.print_info("Clicking Mute Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_wifi_capacity_widget_location_more_options_mute_button(row))
                    sleep(5)

                    self.screen.save_screen_shot()
                    for row1 in self.get_wifi_capacity_widget_location_muted_grid_rows():
                        if location_name in row1.text:
                            kwargs['pass_msg'] = "'mute_anomaly_for_location_in_wifi_capacity_widget()' -> Muted " \
                                                 f"Anomaly successfully for the location : {location_name}"
                            self.common_validation.passed(**kwargs)
                            return 1

            kwargs['fail_msg'] = "'mute_anomaly_for_location_in_wifi_capacity_widget()' -> Not found Location " \
                                 f"row with name:{location_name}"
            self.common_validation.fault(**kwargs)
            return -1

    def unmute_anomaly_for_location_in_wifi_capacity_widget(self, location_name, **kwargs):
        """
        - This Keyword will unmute an anomaly at building level in wifi capacity widget
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get Location Name in Rows and Click More options and unmute Button
        - Keyword Usage:
        - ``Unmute Anomaly For location In WiFi Capacity Widget   ${LOCATION_NAME}``


        :param location_name: Location name to unMute anomaly in wifi capacity widget
        :return: 1 if able to click anomaly unMute button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)

        if self.get_wifi_capacity_widget_location_muted_grid_rows():
            self.utils.print_info(f"Checking Location Name {location_name} in Grid Rows")
            for row in self.get_wifi_capacity_widget_location_muted_grid_rows():
                if location_name in row.text:
                    self.utils.print_info(f"Selecting Un mute Button for the Location: {location_name}")
                    self.utils.print_info("Clicking More Options Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_wifi_capacity_widget_location_more_options_button(row))
                    sleep(5)

                    self.utils.print_info("Clicking UnMute Button in the Location Name Matched Row")
                    self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_more_options_unmute_button)
                    sleep(5)

                    for row1 in self.get_wifi_capacity_widget_location_grid_rows():
                        if location_name in row1.text:
                            kwargs['pass_msg'] = "'unmute_anomaly_for_location_in_wifi_capacity_widget()' -> UnMuted " \
                                                 f"Anomaly successfully for the location : {location_name}"
                            self.common_validation.passed(**kwargs)
                            return 1

                    self.screen.save_screen_shot()
                else:
                    kwargs['fail_msg'] = "'unmute_anomaly_for_location_in_wifi_capacity_widget()' -> Not Found " \
                                         f"Location row with name:{location_name}"
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            kwargs['pass_msg'] = "'unmute_anomaly_for_location_in_wifi_capacity_widget()' -> Unable to find " \
                                 f"Muted rows in wifi capacity widget. Location {location_name} already Un Muted"
            self.common_validation.passed(**kwargs)
            return 1

    def get_total_numbers_of_anomalies_detected(self, **kwargs):
        """
        - This Keyword will Get Total Number of Anomalies Notification Detected.
        - Keyword Usage:
        - ``Get Total Numbers Of Anomalies Detected``

        :return:Total anomalies count if notification found else -1
        """
        total_count = self.get_total_anomalies_detected_from_icon().text
        if total_count:
            self.utils.print_info(f"Total Numbers Of Anomaly Notification Detected is:{total_count}")
            self.screen.save_screen_shot()
            return total_count
        else:
            kwargs['fail_msg'] = "'get_total_numbers_of_anomalies_detected()' -> Unable to find Anomalies Notification"
            self.common_validation.fault(**kwargs)
            return -1

    def dismiss_anomaly_in_wifi_capacity(self, location_name, option, **kwargs):
        """
        - This Keyword dismiss an anomaly for location based on provided option
        - If option provided is 'yes' it will dismiss anomaly else it won't dismiss
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get Location Name and dismiss anomaly
        - Keyword Usage:
        - ``Dismiss Anomaly In WiFi Capacity   ${LOCATION_NAME}    ${OPTION}``

        :param location_name: Location name to enable anomaly Pin in wifi capacity widget
        :param option: confirmation option to delete anomaly(options: yes, no)
        :return: 1 if able to perform dismiss operation with provided option, -1 if anomaly not found
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)
        self.auto_actions.move_to_element(self.get_wifi_capacity_widget())

        for row in self.get_wifi_capacity_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Found location name : {location_name}")
                self.auto_actions.move_to_element(self.get_wifi_capacity_more_options_btn(row))
                self.utils.print_info("Clicking on more options in Wi-Fi capacity widget")
                self.auto_actions.click(self.get_wifi_capacity_more_options_btn(row))
                sleep(1)
                self.screen.save_screen_shot()
                self.auto_actions.move_to_element(self.get_wifi_capacity_dismiss_option())
                self.utils.print_info("Clicking on Dismiss button in Wi-Fi capacity widget")
                self.auto_actions.click_reference(self.get_wifi_capacity_dismiss_option)
                sleep(1)
                self.utils.print_info("Reading warning message...")
                warning_msg = self.get_wifi_capacity_dismiss_warning().text
                self.screen.save_screen_shot()
                self.utils.print_info("warning message : ", warning_msg)
                if option == 'no':
                    self.auto_actions.move_to_element(self.get_wifi_capacity_dismiss_no_option())
                    self.auto_actions.click_reference(self.get_wifi_capacity_dismiss_no_option)
                    sleep(1)
                    self.utils.print_info(f"Clicking on {option} option")
                elif option == 'yes':
                    self.auto_actions.move_to_element(self.get_wifi_capacity_dismiss_yes_option())
                    self.auto_actions.click_reference(self.get_wifi_capacity_dismiss_yes_option)
                    sleep(5)
                    self.utils.print_info(f"Clicking on {option} option")
                return 1
        kwargs['fail_msg'] = f"'dismiss_anomaly_in_wifi_capacity()' -> Anomaly not found for location :{location_name}"
        self.common_validation.fault(**kwargs)
        return -1

    def pin_individual_ap_for_location_in_wifi_capacity_widget(self, location_name, ap_name, **kwargs):
        """
        - This Keyword will pin an AP at building level in wifi capacity widget
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> click Location Name in Rows --> Click AP row pin Button
        - Keyword Usage:
        - ``Pin Individual AP For Location In WiFi Capacity Widget   ${LOCATION_NAME}  ${AP_NAME}``


        :param location_name: Location name to enable anomaly Pin in wifi capacity widget
        :param ap_name: AP name to enable pin in wifi capacity widget of particular location
        :return: 1 if able to click pin button for the AP in Location or already pinned else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)

        for row in self.get_wifi_capacity_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting Pin Button for the Location: {location_name}")
                self.utils.print_info("Clicking Pin Button in the Location Name Matched Row")
                self.auto_actions.click(row)
                sleep(10)

                for row1 in self.get_wifi_capacity_widget_location_grid_individual_ap_rows():
                    if ap_name in row1.text:
                        self.utils.print_info(f"Selecting Pin Button for the AP: {ap_name}")
                        if not self.get_wifi_capacity_widget_location_already_pinned_status(row1):
                            self.utils.print_info(f"Clicking Pin Button in the AP Name {ap_name} Matched Row")
                            self.auto_actions.click(self.get_wifi_capacity_widget_location_individual_ap_pin_button(row1))
                            sleep(5)

                            self.screen.save_screen_shot()
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
                            sleep(5)
                            kwargs['pass_msg'] = "'pin_individual_ap_for_location_in_wifi_capacity_widget()' -> " \
                                                 f"Pinned Anomaly successfully for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
                            sleep(5)
                            kwargs['pass_msg'] = "'pin_individual_ap_for_location_in_wifi_capacity_widget()' -> " \
                                                 f"Already Pinned Anomaly for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.common_validation.passed(**kwargs)
                            return 1

        kwargs['fail_msg'] = "'pin_individual_ap_for_location_in_wifi_capacity_widget()' -> Not found AP row " \
                             f"{ap_name} with Location:{location_name}"
        self.common_validation.fault(**kwargs)
        return -1

    def unpin_individual_ap_for_location_in_wifi_capacity_widget(self, location_name, ap_name, **kwargs):
        """
        - This Keyword will unpin an AP at building level in wifi capacity widget
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> click Location Name in Rows --> Click AP row Unpin Button
        - Keyword Usage:
        - ``Unpin Individual AP For Location In WiFi Capacity Widget   ${LOCATION_NAME}  ${AP_NAME}``


        :param location_name: Location name to enable anomaly Unpin in wifi capacity widget
        :param ap_name: AP name to enable unpin in wifi capacity widget of particular location
        :return: 1 if able to click unpin button for the AP in Location or already unpinned else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        sleep(15)

        for row in self.get_wifi_capacity_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting unpin Button for the Location: {location_name}")
                self.utils.print_info("Clicking unpin Button in the Location Name Matched Row")
                self.auto_actions.click(row)
                sleep(10)

                for row1 in self.get_wifi_capacity_widget_location_grid_individual_ap_rows():
                    if ap_name in row1.text:
                        self.utils.print_info(f"Selecting unpin Button for the AP: {ap_name}")
                        if self.get_wifi_capacity_widget_location_already_pinned_status(row1):
                            self.utils.print_info(f"Clicking unpin Button in the AP Name {ap_name} Matched Row")
                            self.auto_actions.click(self.get_wifi_capacity_widget_location_individual_ap_unpin_button(row1))
                            sleep(5)

                            self.screen.save_screen_shot()
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
                            sleep(5)
                            kwargs['pass_msg'] = "'unpin_individual_ap_for_location_in_wifi_capacity_widget()' -> " \
                                                 f"Already UnPinned Anomaly for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
                            sleep(5)
                            kwargs['pass_msg'] = "'unpin_individual_ap_for_location_in_wifi_capacity_widget()' -> " \
                                                 f"Already unPinned Anomaly for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.common_validation.passed(**kwargs)
                            return 1

        kwargs['fail_msg'] = "'unpin_individual_ap_for_location_in_wifi_capacity_widget()' -> Not found AP row " \
                             f"{ap_name} with Location:{location_name}"
        self.common_validation.fault(**kwargs)
        return -1

    def navigate_to_copilot_through_view_all_anomaly(self, **kwargs):
        """
        - This Keyword navigates to Copilot Anomaly Notification Icon
        - Clicks on view all button and validates whether we are in Copilot page or not
        - Flow: Login--> Click on View ALl of copilot Anomaly ---> Copilot page
        - Keyword Usage:
        - ``Navigate To Copilot Through View All Anomaly``
        :return: 1 if Navigation Successful else -1
        """
        self.utils.print_info("Navigating to Copilot Anomaly notification icon")
        self.navigator.navigate_to_copilot_anomaly_notification_icon()
        self.utils.print_info("Clicking on View ALL button...")
        self.auto_actions.click_reference(self.get_anomalies_view_all_btn)
        sleep(5)
        self.utils.print_info("Checking whether we are in Copilot page or not")
        if self.get_copilot_branded_image():
            kwargs['pass_msg'] = "'navigate_to_copilot_through_view_all_anomaly()' -> Copilot page found after " \
                                 "navigation"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'navigate_to_copilot_through_view_all_anomaly()' -> Copilot page noy found"
            self.common_validation.fault(**kwargs)
            return -1

    def get_total_assurance_scan_count(self, **kwargs):
        """
        - Gets total scan count in Assurance scan widget
        - Flow : Copilot page -->Assurance Scan widget
        - Keyword Usage
        - ``Get Total Assurance Scan Count``
        - This keyword developed on q3r1 - g7r1 environment.
        :return: if success returns Total Assurance Scan Count else returns -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Widgets taking more than 10 sec to display, so adding adequate sleep")
        sleep(15)
        self.utils.print_info("Getting data from Assurance scan widget...")
        self.auto_actions.move_to_element(self.get_assurance_scan_widget())
        self.screen.save_screen_shot()
        try:
            total_scan = self.get_assurance_total_scan_count().text
            self.utils.print_info("Getting Total scans count : ", total_scan)
            return total_scan
        except Exception as e:
            kwargs['fail_msg'] = "'get_total_assurance_scan_count()' -> Unable to total scan count in Assurance " \
                                 "scan widget"
            self.common_validation.fault(**kwargs)
            return -1

    def hide_muted_anomaly_in_wifi_capacity_widget(self, location_name, **kwargs):
        """
        - This keyword hides the muted anomalies
        - Flow : Copilot page -->WiFi capacity widget
        - Keyword Usage
        - ``Hide Muted Anomaly In WiFi Capacity Widget		${LOCATION_NAME}``
        :param location_name: Location name to verify in WiFi capacity widget
        :return: returns 1 if successfully hides muted anomalies else returns -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        sleep(15)

        self.utils.print_info("Click Hide Muted Button in WiFi Capacity Widget")
        button_text = self.get_show_or_hide_muted_button_in_wifi_capacity_widget().text
        self.utils.print_info(f"Button Text is {button_text}")
        self.screen.save_screen_shot()
        if "HIDE MUTED" in button_text.upper():
            self.utils.print_info("Clicking Hide Muted Button")
            self.auto_actions.click_reference(self.get_show_or_hide_muted_button_in_wifi_capacity_widget)
            sleep(5)
        else:
            self.utils.print_info("Already Clicked Hide Muted Button in WiFi Capacity Widget")
            sleep(5)

        self.utils.print_info("Checking for Un muted Rows in WiFi Capacity Widget")
        if self.get_wifi_capacity_widget_location_muted_grid_rows():
            for row in self.get_wifi_capacity_widget_location_muted_grid_rows():
                if location_name in row.text:
                    kwargs['fail_msg'] = "'hide_muted_anomaly_in_wifi_capacity_widget()' -> Muted Entry Displays " \
                                         "after Clicking Hide Muted Button"
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            kwargs['pass_msg'] = "'hide_muted_anomaly_in_wifi_capacity_widget()' -> Muted Entry Not Displays after " \
                                 "Clicking Hide Muted Button as Expected"
            self.common_validation.passed(**kwargs)
            return 1

    def show_muted_anomalies_in_wifi_capacity_widget(self, location_name, **kwargs):
        """
        - This keyword shows the muted anomalies
        - Flow : Copilot page -->WiFi capacity widget
        - Keyword Usage
        - ``Show Muted Anomalies In WiFi Capacity Widget		${LOCATION_NAME}``
        :param location_name: Location name to verify in WiFi capacity widget
        :return: returns 1 if successfully clicks show muted button else returns -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        sleep(15)
        self.utils.print_info("Click Show Muted Button in WiFi Capacity Widget")
        button_text = self.get_show_or_hide_muted_button_in_wifi_capacity_widget().text
        self.utils.print_info(f"Button Text is {button_text}")
        self.screen.save_screen_shot()
        if "HIDE MUTED" in button_text.upper():
            self.utils.print_info("Already Clicked Show Muted Button Enabled in WiFi Capacity Widget")
            sleep(5)
        else:
            self.utils.print_info("Clicking Show Muted Button")
            self.auto_actions.click_reference(self.get_show_or_hide_muted_button_in_wifi_capacity_widget)
            sleep(5)
        self.utils.print_info("Checking for muted Rows in WiFi Capacity Widget")
        if self.get_wifi_capacity_widget_location_muted_grid_rows():
            for row in self.get_wifi_capacity_widget_location_muted_grid_rows():
                if location_name in row.text:
                    kwargs['pass_msg'] = "'show_muted_anomalies_in_wifi_capacity_widget()' -> Location Entry Displays " \
                                         "after Clicking Show Muted Button"
                    self.common_validation.passed(**kwargs)
                    return 1
            kwargs['fail_msg'] = "'show_muted_anomalies_in_wifi_capacity_widget()' -> Location entry is not " \
                                 "displaying after Clicking Show Muted Button"
            self.common_validation.failed(**kwargs)
            return -2
        else:
            kwargs['fail_msg'] = "'show_muted_anomalies_in_wifi_capacity_widget()' -> Muted entries not displayed " \
                                 "after clicking show muted button"
            self.common_validation.fault(**kwargs)
            return -1

    def get_anomaly_details_for_location_in_anomaly_notification_icon(self, location_name, **kwargs):
        """
        - This keyword will return total notification rows displaying and row details matching the location name
          after clicking anomaly Notification icon
        -  Flow : Click Anomaly Notification Icon --> Check Notification entries list
        - Keyword Usage
        - ``${ROW_INFO}  ${ROW_COUNT} = Get Anomaly Details For Location In Anomaly Notification Icon  ${LOCATION_NAME}``

        :param location_name: Location name to verify in anomaly Notification Entries
        :return: if notification entries found returns Total rows and location name matched row information in
                 dictionary format else -1
        """
        self.utils.print_info("Navigating to Anomalies Detected Icon..")
        self.navigator.navigate_to_copilot_anomaly_notification_icon()
        self.screen.save_screen_shot()
        sleep(10)

        for row in self.get_anomaly_notification_grid_rows():
            if location_name in row.text:
                notification_text = row.text
                anomalies_notification_summary = notification_text.replace("\n", " ")
                self.utils.print_info("Getting Location Name in the anomalies detected row")
                pattern = r'(\d+\w{1,4}) (\S+\s+\w{1,8}) (High|Low|Medium) \w+\s+\w+\s+((\w+\s+){6}\d+\s+\w+.) ' \
                          r'\w+\s+\w+\:\s+(\w+\s+\d+\s+\d+)'
                site = re.match(pattern, anomalies_notification_summary)
                if site:
                    total_rows = len(self.get_anomaly_notification_grid_rows())
                    self.utils.print_info(f"Totally {total_rows} Notification Rows found")
                    self.utils.print_info(f"Getting Anomaly Notification Information for Location {location_name}")
                    anomaly_notification_info = dict()
                    anomaly_notification_info["location_name"] = site.group(1)
                    anomaly_notification_info["widget_name"] = site.group(2)
                    anomaly_notification_info["severity"] = site.group(3)
                    anomaly_notification_info["Aggregated_devices"] = site.group(4)
                    anomaly_notification_info["last_detected"] = site.group(6)
                    return anomaly_notification_info, total_rows
                else:
                    kwargs['fail_msg'] = "'get_anomaly_details_for_location_in_anomaly_notification_icon()' -> Unable " \
                                         "to get Anomaly Notification details"
                    self.common_validation.failed(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "'get_anomaly_details_for_location_in_anomaly_notification_icon()' -> " \
                                     f"Location {location_name} not found in Anomaly Notification Rows"
                self.common_validation.fault(**kwargs)
                return -1

    def get_links_present_in_wifi_capacity_additional_resources(self):
        """
        - This keyword will get the both video and documentation url Links From WiFi Capacity Additional Resources Page
        - Flow : Copilot page -->WiFi capacity widget--> Video Icon ---> Additional Resources
        - Keyword Usage
        - ``${DOCS_URL_LIST}    ${VIDEO_URL_LIST} =     Get Links Present In WiFi Capacity Additional Resources``

        :return: ${DOCS_URL_LIST} Documentation URL Links available in WiFi Capacity Additional Resources Page in a list
        :return: ${VIDEO_URL_LIST} Video URL Links available in WiFi Capacity Additional Resources Page in a list
        """

        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        sleep(15)

        self.utils.print_info("Clicking Video Help Icon")
        self.auto_actions.click_reference(self.get_wifi_capacity_video_help_icon)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Getting Documentation Links Present In WiFi Capacity Additional Resources ")
        docs_urls = self.get_wifi_capacity_additional_resources_docs_links()
        docs_url_list = []
        if docs_urls:
            for url in docs_urls:
                doc_url = url.get_attribute('href')
                if doc_url is not None:
                    docs_url_list.append(doc_url)
            self.utils.print_info(f"Documentation Links Present In WiFi Capacity Additional Resources : {docs_url_list}")

        self.utils.print_info("Getting Video Links Present In WiFi Capacity Additional Resources ")
        video_urls = self.get_wifi_capacity_additional_resources_video_links()
        video_url_list = []
        if video_urls:
            for url1 in video_urls:
                video_url = url1.get_attribute('src')
                if video_url is not None:
                    video_url_list.append(video_url)
            self.utils.print_info(f"Video Links Present In WiFi Capacity Additional Resources : {video_url_list}")

        self.utils.print_info("Closing WiFi Capacity Additional Resources")
        self.auto_actions.click_reference(self.get_wifi_capacity_additional_resources_close_button)

        return docs_url_list, video_url_list

    def validate_loading_additional_resources_documentation_links_in_wifi_capacity(self, **kwargs):
        """
        - This keyword will validate loading documentation links from wifi capacity additional resources Page
        - Flow : Copilot page -->WiFi capacity widget--> Video Icon ---> Additional Resources
        - Keyword Usage
        - ``Validate Loading Additional Resources Documentation Links In WiFi Capacity``

        :return: 1 if All the Additional resources Documentation links loaded Successfully else -1
        """
        self.utils.print_info("Navigating to Copilot menu....")
        self.navigator.navigate_to_copilot_menu()
        sleep(15)

        self.utils.print_info("Clicking Video Help Icon")
        self.auto_actions.click_reference(self.get_wifi_capacity_video_help_icon)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Validating Documentation Links Present In WiFi Capacity Additional Resources ")
        docs_urls = self.get_wifi_capacity_additional_resources_docs_links()
        if docs_urls:
            loaded_doc_title = False
            for url in docs_urls:
                page_title_in_xiq = url.text
                self.utils.print_info(f"Validating Documentation Link : {page_title_in_xiq} ")
                self.utils.print_info(f"Documentation Link Title In XIQ Page is : {page_title_in_xiq} ")
                if url is not None:
                    self.utils.print_info(f"Clicking Documentation Link {page_title_in_xiq} in XIQ Page")
                    self.auto_actions.click(url)
                    sleep(10)

                    parent_window = CloudDriver().cloud_driver.window_handles[0]
                    child_window = CloudDriver().cloud_driver.window_handles[1]

                    self.utils.print_info("Switch To New Tab")
                    CloudDriver().cloud_driver.switch_to.window(child_window)
                    self.screen.save_screen_shot()

                    loaded_doc_title = CloudDriver().cloud_driver.title
                    self.utils.print_info(f"Loaded Documentation Link Title Is {loaded_doc_title} ")
                    CloudDriver().cloud_driver.close()

                    self.utils.print_info("Switch To Parent")
                    CloudDriver().cloud_driver.switch_to.window(parent_window)

                    if page_title_in_xiq in loaded_doc_title:
                        self.utils.print_info("Loaded Documentation Title Is Same As XIQ Page Link Title ")
                        loaded_doc_title = True
                    else:
                        self.utils.print_info("Loaded Documentation Title Is Not same As XIQ Page Link Title ")
                        loaded_doc_title = False
                        break

            self.utils.print_info("Closing WiFi Capacity Additional Resources")
            self.auto_actions.click_reference(self.get_wifi_capacity_additional_resources_close_button)

            if loaded_doc_title:
                kwargs['pass_msg'] = "'validate_loading_additional_resources_documentation_links_in_wifi_capacity()' " \
                                     "-> All the Additional resources Documentation links loaded Successfully"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "'validate_loading_additional_resources_documentation_links_in_wifi_capacity()' " \
                                     "-> All the Additional resources Documentation Links Not Loaded Successfully"
                self.common_validation.failed(**kwargs)
                return -1

    def validate_loading_additional_resources_video_links_in_wifi_capacity(self, **kwargs):
        """
        - This keyword will validate loading you tube links from wifi capacity additional resources Page
        - Flow : Copilot page -->WiFi capacity widget--> Video Icon ---> Additional Resources
        - Keyword Usage
        - ``Validate Loading Additional Resources Video Links In WiFi Capacity``

        :return: 1 if All the Additional resources Video links loaded Successfully else -1
        """
        self.utils.print_info("Navigating to Copilot menu...")
        self.navigator.navigate_to_copilot_menu()
        sleep(15)

        self.utils.print_info("Clicking Video Help Icon")
        self.auto_actions.click_reference(self.get_wifi_capacity_video_help_icon)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Validating YouTube Links Present In WiFi Capacity Additional Resources ")
        video_urls = self.get_wifi_capacity_additional_resources_video_links()
        if video_urls:
            loaded_video_flag = False
            for url in video_urls:
                video_url = url.get_attribute('src')
                self.utils.print_info(f"Validating Youtube Video Link : {video_url} ")
                if url is not None:
                    self.utils.print_info("Loading Page with URL: ", video_url)
                    CloudDriver().cloud_driver.execute_script("window.open('');")
                    CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[1])
                    sleep(3)

                    parent_window = CloudDriver().cloud_driver.window_handles[0]
                    self.screen.save_screen_shot()

                    CloudDriver().cloud_driver.get(video_url)
                    self.screen.save_screen_shot()
                    loaded_video_title = CloudDriver().cloud_driver.title
                    self.utils.print_info(f"Loaded You Tube Link Title Is :  {loaded_video_title} ")

                    CloudDriver().cloud_driver.close()
                    self.utils.print_info("Switch To Parent")
                    CloudDriver().cloud_driver.switch_to.window(parent_window)
                    if "YOUTUBE" in loaded_video_title.upper():
                        loaded_video_flag = True
                    else:
                        loaded_video_flag = False
                        break

            self.utils.print_info("Closing WiFi Capacity Additional Resources")
            self.auto_actions.click_reference(self.get_wifi_capacity_additional_resources_close_button)

            if loaded_video_flag:
                kwargs['pass_msg'] = "'validate_loading_additional_resources_video_links_in_wifi_capacity()' " \
                                     "-> All the Additional resources Video links loaded Successfully"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "'validate_loading_additional_resources_video_links_in_wifi_capacity()' " \
                                     "-> All the Additional resources Video Links Not Loaded Successfully"
                self.common_validation.failed(**kwargs)
                return -1

    def sort_anomalies_in_wifi_capacity_widget(self, parameter="Location", **kwargs):
        """
        - This keyword sorts anomalies based on input parameter and provides details of anomalies
        - Flow : Copilot page -->WiFi capacity widget
        - Keyword Usage
        - ``Sort Anomalies In WiFi Capacity Widget		${PARAMETER}``
        :param parameter: parameter(location/severity/most recent) to sort WiFi capacity widget
        :return: returns 1 if success else returns -1 or -2
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        sleep(15)
        self.auto_actions.move_to_element(self.get_wifi_capacity_widget())
        self.utils.print_info("Clicking on sorting options.")
        self.auto_actions.click_reference(self.get_wifi_capacity_widget_sort)
        self.screen.save_screen_shot()
        sleep(2)
        sort_options = self.get_wifi_capacity_widget_sort_options()
        self.utils.print_info(f"Sorting with {parameter}")
        self.auto_actions.select_drop_down_options(sort_options, parameter)
        sleep(2)

        self.utils.print_info("Getting WiFi capacity widget grid rows")
        anomaly_rows = self.get_wifi_capacity_widget_location_grid_rows()
        list1 = []
        if anomaly_rows:
            for row in anomaly_rows:
                self.utils.print_debug(f" Row: {row.text}")
                pattern = r'(.*)\n(High|Low|Medium)(\n(.*))?\n(.*)\n.*across\s(\d+) devices.*\nLast Detected\:\s(\w+\s+\d+\s+\d+)'
                details = re.match(pattern, row.text)
                if details:
                    anomaly_details = dict()
                    anomaly_details["location_name"] = details.group(1)
                    anomaly_details["severity"] = details.group(2)
                    status = self.get_wifi_capacity_widget_anomaly_pinned_status(row)
                    self.utils.print_debug(f" pinned status: {status}")
                    if self.get_wifi_capacity_widget_anomaly_pinned_status(row):
                        anomaly_details["pinned"] = 'True'
                    else:
                        anomaly_details["pinned"] = 'False'
                    anomaly_details["Aggregated_devices"] = details.group(6)
                    anomaly_details["last_detected"] = details.group(7)
                    list1.append(anomaly_details)
                else:
                    kwargs['fail_msg'] = "'sort_anomalies_in_wifi_capacity_widget()' " \
                                         "-> Could not get details for anomaly row: {row.text}"
                    self.common_validation.failed(**kwargs)
                    return -1
            return list1
        else:
            kwargs['fail_msg'] = "'sort_anomalies_in_wifi_capacity_widget()' -> No anomalies were detected"
            self.common_validation.fault(**kwargs)
            return -2

    def get_wifi_efficiency_widget_summary(self, **kwargs):
        """
        - Gets WiFi efficiency widget summary in copilot
        - Flow : Copilot page -->Wifi efficiency widget
        - Keyword Usage
        - ``Get WiFi Efficiency Widget Summary``
        :return: returns Buildings and APs count if success else returns -1 or -2
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Wi-Fi efficiency widget Summary")
        self.utils.print_info("Widgets taking more than 10 sec to display, so adding adequate sleep")
        sleep(15)
        self.auto_actions.move_to_element(self.get_wifi_efficiency_widget())
        self.screen.save_screen_shot()
        try:
            wifi_summary = self.get_wifi_efficiency_widget_content().text
            self.utils.print_info("Wi-Fi efficiency widget Summary : ", wifi_summary)
            if re.search(r'(\d+) places .* (\d+) devices', wifi_summary):
                summary = re.search(r'(\d+) places .* (\d+) devices', wifi_summary)
                buildings = summary.group(1)
                aps = summary.group(2)
                self.utils.print_info("Total Buildings : ", buildings)
                self.utils.print_info("Total APs : ", aps)
                return buildings, aps
            else:
                kwargs['fail_msg'] = "'get_wifi_efficiency_widget_summary()' -> No anomalies detected for WiFi " \
                                     "efficiency widget"
                self.common_validation.fault(**kwargs)
                return -2
        except Exception as e:
            kwargs['fail_msg'] = "'get_wifi_efficiency_widget_summary()' -> Unable to get WiFI efficiency Summary"
            self.common_validation.fault(**kwargs)
            return -1

    def pin_anomaly_for_location_in_wifi_efficiency_widget(self, location_name, **kwargs):
        """
        - This Keyword will pin an anomaly at building level in wifi efficiency widget
        - Flow: CoPilot--> Wi-Fi Efficiency ---> Get Location Name in Rows and Click Pin Button
        - Keyword Usage:
        - ``Pin Anomaly For location In WiFi Efficiency Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in wifi efficiency widget
        :return: 1 if able to click anomaly Pin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Wi-Fi Efficiency Widget")
        sleep(15)

        for row in self.get_wifi_efficiency_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting Pin Button for the Location: {location_name}")
                if not self.get_wifi_efficiency_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Pin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_wifi_efficiency_widget_location_pin_button(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_wifi_efficiency_widget()' -> Pinned Anomaly " \
                                         f"successfully for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_wifi_efficiency_widget()' -> Already Pinned " \
                                         f"Anomaly for the location : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'pin_anomaly_for_location_in_wifi_efficiency_widget()' -> Not found Location row " \
                             f"with name:{location_name}"
        self.common_validation.fault(**kwargs)
        return -1

    def get_poe_stability_widget_summary(self, **kwargs):
        """
        - Gets poe stability summary in copilot
        - Flow : Copilot page -->POE stability widget
        - Keyword Usage
        - ``Get POE Stability Widget Summary``
        :return: returns Buildings and APs count if success else returns -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting POE stability widget Summary")
        self.utils.print_info("Widgets taking more than 10 sec to display, so adding adequate sleep")
        sleep(10)
        self.auto_actions.move_to_element(self.get_poe_stability_widget())
        self.screen.save_screen_shot()
        try:
            poe_summary = self.get_poe_stability_content().text
            self.utils.print_info("POE stability widget Summary : ", poe_summary)
            if re.search(r'(\d+) places .* (\d+) devices', poe_summary):
                summary = re.search(r'(\d+) places .* (\d+) devices', poe_summary)
                buildings = summary.group(1)
                aps = summary.group(2)

                self.utils.print_info("Total Buildings : ", buildings)
                self.utils.print_info("Total APs : ", aps)
                return buildings, aps
            else:
                kwargs['fail_msg'] = "'get_poe_stability_widget_summary()' -> Unable to get Buildings and APs " \
                                     "information in POE stability widget"
                self.common_validation.failed(**kwargs)
                return -2
        except Exception as e:
            kwargs['fail_msg'] = "'get_poe_stability_widget_summary()' -> Unable to get POE stability widget " \
                                 "summary details"
            self.common_validation.fault(**kwargs)
            return -1

    def pin_anomaly_for_location_in_poe_stability_widget(self, location_name, **kwargs):
        """
        - This Keyword will pin an anomaly at building level in PoE Stability widget
        - Flow: CoPilot-->  PoE STABILITY ---> Get Location Name in Rows and Click Pin Button
        - Keyword Usage:
        - ``Pin Anomaly For location In PoE Stability Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in PoE Stability widget
        :return: 1 if able to click anomaly Pin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on PoE Capacity Widget")
        sleep(15)

        for row in self.get_poe_stability_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting Pin Button for the Location: {location_name}")
                if not self.get_poe_stability_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Pin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_poe_stability_widget_location_pin_button(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_poe_stability_widget()' -> Pinned Anomaly " \
                                         f"successfully for the location : {location_name} in PoE Stability Widget"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_poe_stability_widget()' -> Already Pinned " \
                                         f"Anomaly for the location : {location_name} in PoE Stability Widget"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'pin_anomaly_for_location_in_poe_stability_widget()' -> Not found Location row with " \
                             f"name:{location_name} in PoE Stability Widget"
        self.common_validation.fault(**kwargs)
        return -1

    def get_port_efficiency_widget_summary(self):
        """
        - Gets port efficiency widget summary in copilot
        - Flow : Copilot page -->POE stability widget
        - Keyword Usage
        - ``Get POE Stability Widget Summary``
        :return: returns Buildings and APs count if success else returns -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting port efficiency widget Summary")
        self.utils.print_info("Widgets taking more than 10 sec to display, so adding adequate sleep")
        sleep(10)
        self.auto_actions.move_to_element(self.get_port_efficiency_widget())
        self.screen.save_screen_shot()
        buildings = -2
        aps = -2
        try:
            port_summary = self.get_port_efficiency_widget_details().text
            self.utils.print_info("Port efficiency widget Summary : ", port_summary)
            if re.search(r'(\d+) places .* (\d+) devices', port_summary):
                summary = re.search(r'(\d+) places .* (\d+) devices', port_summary)
                buildings = summary.group(1)
                aps = summary.group(2)

                self.utils.print_info("Total Buildings : ", buildings)
                self.utils.print_info("Total APs : ", aps)
                return [buildings, aps]
            else:
                self.utils.print_info("No anomalies detected in port efficiency widget")
                return [buildings, aps]
        except Exception as e:
            self.utils.print_info("Unable to get port efficiency widget in copilot page")
            return [buildings, aps]

    def pin_anomaly_for_location_in_port_efficiency_widget(self, location_name, **kwargs):
        """
        - This Keyword will pin an anomaly at building level in Port Efficiency widget
        - Flow: CoPilot-->  Port Efficiency ---> Get Location Name in Rows and Click Pin Button
        - Keyword Usage:
        - ``Pin Anomaly For location In Port Efficiency Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in Port Efficiency widget
        :return: 1 if able to click anomaly Pin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Port Efficiency Widget")
        sleep(15)

        for row in self.get_port_efficiency_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting Pin Button for the Location: {location_name}")
                if not self.get_port_efficiency_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Pin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_port_efficiency_widget_location_pin_button(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_port_efficiency_widget()' -> Pinned Anomaly " \
                                         f"successfully for the location : {location_name} in Port Efficiency Widget"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_port_efficiency_widget()' -> Already Pinned " \
                                         f"Anomaly for the location : {location_name} in Port Efficiency Widget"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'pin_anomaly_for_location_in_port_efficiency_widget()' -> Not found Location row with " \
                             f"name:{location_name} in Port Efficiency Widget"
        self.common_validation.fault(**kwargs)
        return -1

    def unpin_anomaly_for_location_in_port_efficiency_widget(self, location_name, **kwargs):
        """
        - This Keyword will unpin an anomaly at building level in Port Efficiency widget
        - Flow: CoPilot-->  Port Efficiency ---> Get Location Name in Rows and Click UnPin Button
        - Keyword Usage:
        - ``Unpin Anomaly For location In Port Efficiency Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly UnPin in Port Efficiency widget
        :return: 1 if able to click anomaly UnPin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on Port Efficiency Widget")
        sleep(15)

        for row in self.get_port_efficiency_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting UnPin Button for the Location: {location_name}")
                if self.get_port_efficiency_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking UnPin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_port_efficiency_widget_location_already_pinned_status(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'unpin_anomaly_for_location_in_port_efficiency_widget()' -> unPinned Anomaly " \
                                         f"successfully for the location : {location_name} in Port Efficiency Widget"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'unpin_anomaly_for_location_in_port_efficiency_widget()' -> Already " \
                                         f"UnPinned Anomaly for the location : {location_name} in Port Efficiency Widget"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'unpin_anomaly_for_location_in_port_efficiency_widget()' -> Not found Location row with " \
                             f"name:{location_name} in Port Efficiency Widget"
        self.common_validation.fault(**kwargs)
        return -1

    def get_dfs_recurrence_widget_summary(self, **kwargs):
        """
        - Gets DFS Recurrence widget summary in copilot
        - Flow : Copilot page --> DFS Recurrence widget
        - Keyword Usage
        - ``Get DFS Recurrence Widget Summary``
        :return: returns Buildings and APs count if success else returns -1 or -2
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting DFS Recurrence widget Summary")

        sleep(10)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_dfs_recurrence_widget())
        self.screen.save_screen_shot()
        sleep(20)

        try:
            dfs_recurrence_summary = self.get_dfs_recurrence_widget_content().text
            self.utils.print_info("DFS Recurrence widget Summary : ", dfs_recurrence_summary)
            if re.search(r'(\d+) places in your environment, affecting (\d+) devices.', dfs_recurrence_summary):
                summary = re.search(r'(\d+) places in your environment, affecting (\d+) devices', dfs_recurrence_summary)
                buildings = summary.group(1)
                aps = summary.group(2)
                self.utils.print_info("Total Buildings : ", buildings)
                self.utils.print_info("Total APs : ", aps)
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                return dfs_recurrence_summary, buildings, aps
            else:
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                kwargs['fail_msg'] = "'get_dfs_recurrence_widget_summary()' -> No anomalies detected for DFS " \
                                     "Recurrence widget"
                self.common_validation.failed(**kwargs)
                return -2
        except Exception as e:
            kwargs['fail_msg'] = "'get_dfs_recurrence_widget_summary()' -> Unable to get DFS Recurrence Summary"
            self.utils.print_info(e)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            self.common_validation.fault(**kwargs)
            return -1

    def get_ap_details_from_dfs_recurrence_widget_location(self, location_name, **kwargs):
        """
        - Gets all device details from DFS Recurrence Widget Location Details
        - Flow : Copilot page --> DFS Recurrence widget
        - param: location - location name
        - Keyword Usage
          ``Get AP Details from DFS Recurrence Widget Location``

        :return: returns devices list with the information in format : [['Device_669966055461379', 'High', 'Last Detected: Sep 15 2021', False], ['Device_669966055461377', 'High', 'Last Detected: Sep 14 2021', False]
        :return: -1 in case of error
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting DFS Recurrence widget Summary")

        sleep(10)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_dfs_recurrence_widget())
        self.screen.save_screen_shot()

        try:
            anomalies = self.get_dfs_recurrence_anomaly_list()
            for anomaly in anomalies:
                anomaly_location = self.get_anomaly_location(anomaly).text
                if location_name in anomaly_location:
                    self.utils.print_info("Anomaly Location match found: ", anomaly_location)

                    self.auto_actions.click(self.get_anomaly_location(anomaly))
                    sleep(5)
                    anomaly_device_details = self.get_anomaly_device_details()
                    anomaly_device_details_list = []
                    for anomaly_device_detail in anomaly_device_details:
                        anomaly_device_detail_list = []
                        device_anomaly_pinned_status = False
                        self.utils.print_info("Device details: ", anomaly_device_detail.text)

                        device_name = self.get_anomaly_device_name(anomaly_device_detail).text
                        self.utils.print_info("device_name: ", device_name)

                        device_last_detected = self.get_anomaly_device_last_detected(anomaly_device_detail).text
                        self.utils.print_info("device_last_detected: ", device_last_detected)

                        device_anomaly_severity = self.get_anomaly_device_anomaly_severity(anomaly_device_detail).text
                        self.utils.print_info("device_anomaly_severity: ", device_anomaly_severity)

                        device_anomaly_pinned = self.get_anomaly_device_pinned_status(anomaly_device_detail)

                        if device_anomaly_pinned:
                            device_anomaly_pinned_status = True
                        self.utils.print_info("device_anomaly_pinned_status: ", device_anomaly_pinned_status)
                        anomaly_device_detail_list.append(device_name)
                        anomaly_device_detail_list.append(device_anomaly_severity)
                        anomaly_device_detail_list.append(device_last_detected)
                        anomaly_device_detail_list.append(device_anomaly_pinned_status)

                        anomaly_device_details_list.append(anomaly_device_detail_list)
                        self.utils.switch_to_default(CloudDriver().cloud_driver)
                    return anomaly_device_details_list
                else:
                    self.utils.print_info("Unable to find the location in the anomaly list")

        except Exception as e:
            kwargs['fail_msg'] = "'get_ap_details_from_dfs_recurrence_widget_location()' -> Unable to get DFS " \
                                 "Recurrence Summary"
            self.utils.print_info(e)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            self.common_validation.fault(**kwargs)
            return -1

    def get_dfs_recurrence_muted_button_status(self):
        """
        - Get DFS Recurrence Muted Button Status
        - Flow : Copilot page --> DFS Recurrence widget
        - Keyword Usage
        - ``Get DFS Recurrence Muted Button Status``
        :return: returns either HIDE MUTED or SHOW MUTED
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting DFS Recurrence widget Summary")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_dfs_recurrence_widget())
        self.screen.save_screen_shot()
        status = self.get_dfs_recurrence_anomaly_muted().text

        self.utils.switch_to_default(CloudDriver().cloud_driver)

        return status

    def show_muted_dfs_recurrence_anomalies(self, **kwargs):
        """
        - Changes the DFS Recurrence Anomalies MUTED Button status to "SHOW MUTED"
        - Flow : Copilot page --> DFS Recurrence widget
        - Keyword Usage
        - ``Show Muted DFS Recurrence Anomalies``
        :return: returns 1 if successfully pressed SHOW MUTED button else -1
        """
        # if navigate:
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting DFS Recurrence widget Summary")

        sleep(10)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_dfs_recurrence_widget())
        self.screen.save_screen_shot()

        if 'HIDE MUTED' in self.get_dfs_recurrence_anomaly_muted().text:
            pass
        else:
            self.auto_actions.click_reference(self.get_dfs_recurrence_anomaly_muted)

        status = self.get_dfs_recurrence_anomaly_muted().text
        sleep(1)
        self.screen.save_screen_shot()
        self.utils.switch_to_default(CloudDriver().cloud_driver)

        if 'HIDE MUTED' in status:
            kwargs['pass_msg'] = "'show_muted_dfs_recurrence_anomalies()' -> Successfully Clicked button"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'show_muted_dfs_recurrence_anomalies()' -> UnSuccessfully Clicked button"
            self.common_validation.failed(**kwargs)
            return -1

    def hide_muted_dfs_recurrence_anomalies(self, **kwargs):
        """
        - Changes the DFS Recurrence Anomalies MUTED Button status to "HIDE MUTED"
        - Flow : Copilot page --> DFS Recurrence widget
        - Keyword Usage
        - ``Hide Muted DFS Recurrence Anomalies``
        :return: returns 1 if successfully pressed HIDE MUTED button else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting DFS Recurrence widget Summary")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_dfs_recurrence_widget())
        self.screen.save_screen_shot()

        if 'SHOW MUTED' in self.get_dfs_recurrence_anomaly_muted().text:
            pass
        else:
            self.auto_actions.click_reference(self.get_dfs_recurrence_anomaly_muted)

        sleep(1)
        self.screen.save_screen_shot()
        status = self.get_dfs_recurrence_anomaly_muted().text
        self.utils.switch_to_default(CloudDriver().cloud_driver)

        if 'SHOW MUTED' in status:
            kwargs['pass_msg'] = "'hide_muted_dfs_recurrence_anomalies()' -> Successfully Clicked button"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'hide_muted_dfs_recurrence_anomalies()' -> UnSuccessfully Clicked button"
            self.common_validation.failed(**kwargs)
            return -1

    def get_dfs_recurrence_widget_location_details(self, location_name=False, **kwargs):
        """
        - Get DFS Recurrence Widget Location Details
        - Flow : Copilot page --> DFS Recurrence widget
        - param: location_name - location name
        - Keyword Usage
        - ``Get DFS Recurrence Widget Location Details``
        :return: returns location details as an array matching the location name passed as an argument: [1, '5544Location', 'Medium', False, False, '2', 'Last Detected: Sep 15 2021']
        :return: returns all locations details as an array of arrays like: [[1, '5544Location', 'Medium', False, False, '2', 'Last Detected: Sep 15 2021'], [2, '6699Location', 'High', False, False, '3', 'Last Detected: Sep 15 2021']]
        :return: returns -1 if error
        :return: returns -2 if error

        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting DFS Recurrence widget summary")

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(2)

        self.auto_actions.move_to_element(self.get_dfs_recurrence_widget())
        sleep(5)

        self.screen.save_screen_shot()

        try:
            anomalies = self.get_dfs_recurrence_anomaly_list()
            index = 1
            anomaly_list = []
            for anomaly in anomalies:
                summary_array = []

                anomaly_summary = anomaly.text
                anomaly_location = self.get_anomaly_location(anomaly).text

                device_count = 0
                pinned = False
                muted = False
                # self.utils.print_info("Anomaly Location match found: ", anomaly_location)

                if re.search(r'We detected problems with channels changing too often across (\d+) devices', anomaly_summary):
                    device_count = re.search(r'We detected problems with channels changing too often across (\d+) devices', anomaly_summary).group(1)

                severity = self.get_anomaly_severity(anomaly).text
                pinned_flag = self.get_anomaly_pinned(anomaly)
                muted_flag = self.get_anomaly_muted(anomaly)
                last_detected = self.get_anomaly_last_detected(anomaly).text

                if pinned_flag:
                    pinned = True

                if muted_flag:
                    muted = True

                summary_array.append(index)
                summary_array.append(anomaly_location)
                summary_array.append(severity)
                summary_array.append(pinned)
                summary_array.append(muted)
                summary_array.append(device_count)
                summary_array.append(last_detected)
                self.utils.print_debug("summary_array : ", summary_array)

                anomaly_list.append(summary_array)
                index += 1

            self.utils.print_debug("Anomaly List: ", anomaly_list)

            self.utils.switch_to_default(CloudDriver().cloud_driver)

            if location_name:
                for anomaly_element in anomaly_list:
                    if location_name in anomaly_element:
                        self.utils.print_info("Anomaly matched: ", anomaly_element)
                        return anomaly_element
                kwargs['fail_msg'] = "'get_dfs_recurrence_widget_location_details()' -> No Anomaly matched"
                self.common_validation.failed(**kwargs)
                return -2
            else:
                self.utils.print_info("Returning Anomaly List: ", anomaly_list)
                return anomaly_list
        except Exception as e:
            kwargs['fail_msg'] = "'get_dfs_recurrence_widget_location_details()' -> Unable to get DFS Recurrence Summary"
            self.utils.print_info(e)
            self.common_validation.fault(**kwargs)
            return -1

    def get_copilot_account_summary(self):
        """
        - Returns CoPilot Account Summary as a dictionary
        - Flow : Copilot page --> Account Summary
        - Keyword Usage
        - ``Get CoPilot Account Summary``
        :return: Returns CoPilot Account Summary as a dictionary, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Account Summary")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_account_summary_widget())
        self.screen.save_screen_shot()
        sleep(2)
        rows = self.get_account_summary_rows()
        account_summary = dict()
        for row in rows:
            member_since = self.get_account_summary_row_key(row).text
            member_since_value = self.get_account_summary_row_value(row).text
            account_summary[member_since] = member_since_value

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.utils.print_info("Account Summary: ", account_summary)

        return account_summary

    def get_extremecloud_iq_applications(self):
        """
        - Returns Get ExtremeCloud IQ Applications as a dictionary
        - Flow : Copilot page -->  ExtremeCloud IQ Applications
        - Keyword Usage
        - ``Get ExtremeCloud IQ Applications``
        :return: Returns ExtremeCloud IQ Applications Summary as a dictionary, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting ExtremeCloud IQ Applications")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_extremecloud_iq_applications_widget())
        self.screen.save_screen_shot()

        sleep(2)
        rows = self.get_extremecloud_iq_applications_rows()
        extremecloud_iq_applications = dict()
        for row in rows:
            _key = self.get_extremecloud_iq_applications_row_key(row).text
            _value = self.get_extremecloud_iq_applications_row_value(row).text
            if 'Learn More' in _value:
                extremecloud_iq_applications[_key] = 'Learn More'
            if 'Subscribed' in _value:
                extremecloud_iq_applications[_key] = 'Subscribed'

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.utils.print_info("ExtremeCloud IQ Applications: ", extremecloud_iq_applications)
        return extremecloud_iq_applications

    def get_devices_by_os(self):
        """
        - Returns Get Devices By OS as a dictionary
        - Flow : Copilot page -->  Get Devices By OS
        - Keyword Usage
        - ``Get Devices By OS``
        :return: Returns Get Devices By OS as a dictionary, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Devices By OS")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        widget = self.get_devices_by_os_widget()
        self.auto_actions.move_to_element(widget)
        self.screen.save_screen_shot()

        sleep(2)
        rows = self.get_devices_by_os_rows(widget)
        devices_by_os = dict()
        for row in rows:
            try:
                _key = self.get_devices_by_os_row_key(row).text
                _value = self.get_devices_by_os_row_value(row).text
                if "IQ ENGINE RELEASE NOTES" in _key:
                    pass
                else:
                    devices_by_os[_key] = _value
            except Exception as e:
                pass

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.utils.print_info("Devices by OS: ", devices_by_os)
        return devices_by_os

    def get_devices_by_os_iqagent_notes(self, **kwargs):
        """
        - Returns Get Devices By OS as a dictionary
        - Flow : Copilot page -->  Get Devices By OS
        - Keyword Usage
        - ``Get Devices By OS``
        :return: Returns Get Devices By OS as a dictionary, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Devices By OS")
        sleep(25)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        widget = self.get_devices_by_os_widget()
        self.screen.save_screen_shot()

        sleep(2)
        self.auto_actions.click_reference(self.get_devices_by_os_iqagent)
        parent_window = CloudDriver().cloud_driver.window_handles[0]
        child_window = CloudDriver().cloud_driver.window_handles[1]

        self.utils.print_info("Switch To New Tab")
        CloudDriver().cloud_driver.switch_to.window(child_window)
        self.screen.save_screen_shot()
        loaded_doc_title = CloudDriver().cloud_driver
        sleep(15)
        if "Learning What's New" in loaded_doc_title.title:
            kwargs['pass_msg'] = "'get_devices_by_os_iqagent_notes()' -> IQ ENGINE RELEASE NOTES page loaded successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'get_devices_by_os_iqagent_notes()' -> IQ ENGINE RELEASE NOTES page not loaded " \
                                 "successfully"
            self.common_validation.failed(**kwargs)
            return -1
        CloudDriver().cloud_driver.close()
        self.utils.print_info("Closing the browser")
        self.utils.switch_to_default(CloudDriver().cloud_driver)

    def get_devices_by_type(self):
        """
        - Returns Get Devices By Type as a dictionary
        - Flow : Copilot page -->  Get Devices By Type
        - Keyword Usage
        - ``Get Devices By Type``
        :return: Returns Get Devices By Type as a dictionary, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Devices By Type")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        widget = self.get_devices_by_type_widget()
        self.auto_actions.move_to_element(widget)
        self.screen.save_screen_shot()

        sleep(2)
        rows = self.get_devices_by_type_rows(widget)
        devices_by_type = dict()
        for row in rows:
            try:
                member_since = self.get_devices_by_type_row_key(row).text
                member_since_value = self.get_devices_by_type_row_value(row).text
                devices_by_type[member_since] = member_since_value
            except Exception as e:
                pass

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.utils.print_info("Devices by OS: ", devices_by_type)
        return devices_by_type

    def get_copilot_licenses(self):
        """
        - Returns Get CoPilot Licenses as a dictionary
        - Flow : Copilot page -->  Get CoPilot Licenses
        - Keyword Usage
        - ``Get CoPilot Licenses``
        :return: Returns Get CoPilot Licenses as a dictionary, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting CoPilot Licenses")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        widget = self.get_copilot_widget()
        self.auto_actions.move_to_element(widget)
        self.screen.save_screen_shot()

        # Refresh the page in case this page was already loaded so the data will be current
        self.refresh_copilot_dashboard_page()

        sleep(2)
        rows = self.get_copilot_widget_rows(widget)

        licenses_list = []
        for row in rows:
            licenses = dict()
            row_line = row.text
            list1 = row_line.split("Consumed :")
            licenses['license_type'] = list1[0].strip()
            list2 = list1[1].split('Available :')
            licenses['consumed'] = list2[0].strip()
            licenses['available'] = list2[1].strip()
            licenses_list.append(licenses)
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.utils.print_info("Licenses List: ", licenses_list)
        return licenses_list

    def pin_anomaly_for_location_in_dfs_recurrence_widget(self, location_name, **kwargs):
        """
        - This Keyword will pin an anomaly at building level in DFS Recurrence widget
        - Flow: CoPilot--> DFS RECURRENCE ---> Get Location Name in Rows and Click Pin Button
        - Keyword Usage:
        - ``Pin Anomaly For location In DFS Recurrence Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in DFS Recurrence widget
        :return: 1 if able to click anomaly Pin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_dfs_recurrence_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting Pin Button for the Location: {location_name} in in DFS Recurrence")
                if not self.get_dfs_recurrence_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Pin Button in the Location Name Matched Row in in DFS Recurrence")
                    self.auto_actions.click(self.get_dfs_recurrence_widget_location_pin_button(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_dfs_recurrence_widget()' -> Pinned Anomaly " \
                                         f"successfully for the location : {location_name} in DFS Recurrence"
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_dfs_recurrence_widget()' -> Already Pinned " \
                                         f"Anomaly for the location : {location_name} in DFS Recurrence"
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'pin_anomaly_for_location_in_dfs_recurrence_widget()' -> Not found Location row with " \
                             f"name:{location_name} in DFS Recurrence"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def unpin_anomaly_for_location_in_dfs_recurrence_widget(self, location_name, **kwargs):
        """
        - This Keyword will unpin an anomaly at building level in DFS Recurrence widget
        - Flow: CoPilot--> DFS RECURRENCE ---> Get Location Name in Rows and Click UnPin Button
        - Keyword Usage:
        - ``UnPin Anomaly For location In DFS Recurrence Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly UnPin in DFS Recurrence widget
        :return: 1 if able to click anomaly UnPin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_dfs_recurrence_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Selecting UnPin Button for the Location: {location_name} in DFS Recurrence")
                if self.get_dfs_recurrence_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Unpin Button in the Location Name Matched Row in DFS Recurrence")
                    self.auto_actions.click(self.get_dfs_recurrence_widget_location_already_pinned_status(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'unpin_anomaly_for_location_in_dfs_recurrence_widget()' -> Successfully " \
                                         f"UnPinned Anomaly for the location : {location_name} in DFS Recurrence"
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'unpin_anomaly_for_location_in_dfs_recurrence_widget()' -> Already UnPinned " \
                                         f"Anomaly for the location : {location_name} in DFS Recurrence"
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'unpin_anomaly_for_location_in_dfs_recurrence_widget()' -> Not found Location row with " \
                             f"name:{location_name} in DFS Recurrence"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def mute_anomaly_for_location_in_dfs_recurrence_widget(self, location_name, **kwargs):
        """
        - This Keyword will mute an anomaly at building level in DFS Recurrence widget
        - Flow: CoPilot--> DFS Recurrence ---> Get Location Name in Rows and Click More options and mute Button
        - Keyword Usage:
        - ``Mute Anomaly For location In DFS Recurrence Widget   ${LOCATION_NAME}``
        :param location_name: Location name to Mute anomaly in DFS Recurrence Widget
        :return: 1 if able to click anomaly Mute button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        if self.get_dfs_recurrence_widget_location_grid_muted_rows():
            for row in self.get_dfs_recurrence_widget_location_grid_muted_rows():
                if location_name in row.text:
                    kwargs['pass_msg'] = "'mute_anomaly_for_location_in_dfs_recurrence_widget()' -> Already Mute " \
                                         f"Anomaly Enabled for the location : {location_name} in DFS Recurrence Widget"
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    self.common_validation.passed(**kwargs)
                    return 1
        else:
            for row in self.get_dfs_recurrence_widget_location_grid_rows():
                if location_name in row.text:
                    self.utils.print_info(f"Selecting Mute Button for the Location: {location_name} "
                                          "in DFS Recurrence Widget")
                    self.utils.print_info("Clicking More Options Button in the Location Name Matched Row "
                                          "in DFS Recurrence Widget")
                    self.auto_actions.click(self.get_dfs_recurrence_widget_location_more_options_button(row))
                    sleep(2)

                    self.utils.print_info("Clicking Mute Button in the Location Name Matched Row "
                                          "in DFS Recurrence Widget")
                    self.auto_actions.click(self.get_dfs_recurrence_widget_location_more_options_mute_button(row))
                    sleep(5)

                    self.screen.save_screen_shot()
                    for row1 in self.get_dfs_recurrence_widget_location_grid_muted_rows():
                        if location_name in row1.text:
                            kwargs['pass_msg'] = "'mute_anomaly_for_location_in_dfs_recurrence_widget()' -> Muted " \
                                                 f"Anomaly successfully for the location : {location_name}"
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.passed(**kwargs)
                            return 1

            kwargs['fail_msg'] = "'mute_anomaly_for_location_in_dfs_recurrence_widget()' -> Not found Location row with " \
                                 f"name:{location_name} in DFS Recurrence"
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            self.common_validation.fault(**kwargs)
            return -1

    def unmute_anomaly_for_location_in_dfs_recurrence_widget(self, location_name, **kwargs):
        """
        - This Keyword will unmute an anomaly at building level in DFS Recurrence widget
        - Flow: CoPilot--> DFS Recurrence ---> Get Location Name in Rows and Click More options and unmute Button
        - Keyword Usage:
        - ``UnMute Anomaly For location In DFS Recurrence Widget   ${LOCATION_NAME}``


        :param location_name: Location name to UnMute anomaly in DFS Recurrence Widget
        :return: 1 if able to click anomaly UnMute button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        if self.get_dfs_recurrence_widget_location_grid_muted_rows():
            self.utils.print_info(f"Checking Location Name {location_name} in Grid Rows")
            for row in self.get_dfs_recurrence_widget_location_grid_muted_rows():
                if location_name in row.text:
                    self.utils.print_info(f"Selecting Un mute Button for the Location: {location_name}")
                    self.screen.save_screen_shot()
                    self.utils.print_info("Clicking UnMute Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_dfs_recurrence_widget_location_grid_unmute_button(row))
                    self.screen.save_screen_shot()
                    sleep(5)

                    for row1 in self.get_dfs_recurrence_widget_location_grid_rows():
                        if location_name in row1.text:
                            kwargs['pass_msg'] = "'unmute_anomaly_for_location_in_dfs_recurrence_widget()' -> UnMuted " \
                                                 f"Anomaly successfully for the location : {location_name}"
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.passed(**kwargs)
                            return 1

                    self.screen.save_screen_shot()
                else:
                    kwargs['fail_msg'] = "'unmute_anomaly_for_location_in_dfs_recurrence_widget()' -> Not Found " \
                                         f"Location row with name:{location_name}"
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            kwargs['pass_msg'] = "'unmute_anomaly_for_location_in_dfs_recurrence_widget()' -> Unable to find L" \
                                 f"ocation {location_name} in DFS Recurrence Widget Muted rows. " \
                                 f"Location {location_name} already Un Muted"
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            self.common_validation.passed(**kwargs)
            return 1

    def dismiss_anomaly_for_location_in_dfs_recurrence_widget(self, location_name, option='yes', **kwargs):
        """
        - This Keyword dismiss an anomaly for location based on provided option in DFS Recurrence Widget
        - If option provided is 'yes' it will dismiss anomaly else it won't dismiss
        - Default Option(yes) is to dismiss the Anomaly for Location in DFS Recurrence Widget
        - Flow: CoPilot--> on DFS Recurrence ---> Get Location Name and dismiss anomaly
        - Keyword Usage:
        - ``Dismiss Anomaly For Location In DFS Recurrence Widget   ${LOCATION_NAME}``
        - ``Dismiss Anomaly For Location In DFS Recurrence Widget   ${LOCATION_NAME}    option=${OPTION}``

        :param location_name: Location name to enable anomaly Pin in DFS Recurrence Widget
        :param option: confirmation option to delete anomaly(options: yes, no)
        :return: 1 if able to perform dismiss operation with provided option, -1 if anomaly not found
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows on DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_dfs_recurrence_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Found location name : {location_name} in DFS Recurrence Widget")
                self.auto_actions.move_to_element(self.get_dfs_recurrence_widget_location_more_options_btn(row))
                self.utils.print_info("Clicking on more options in DFS Recurrence Widget")
                self.auto_actions.click(self.get_dfs_recurrence_widget_location_more_options_btn(row))
                sleep(1)
                self.screen.save_screen_shot()
                self.auto_actions.move_to_element(self.get_dfs_recurrence_widget_location_dismiss_option())
                self.utils.print_info("Clicking on Dismiss button in DFS Recurrence Widget")
                self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_dismiss_option)
                sleep(1)
                self.utils.print_info("Reading warning message...")
                warning_msg = self.get_dfs_recurrence_widget_location_dismiss_warning().text
                self.screen.save_screen_shot()
                self.utils.print_info("warning message : ", warning_msg)

                if option == 'no':
                    self.utils.print_info(f"Clicking on {option} option")
                    self.auto_actions.move_to_element(self.get_dfs_recurrence_widget_location_dismiss_no_option())
                    self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_dismiss_no_option)
                    sleep(1)

                elif option == 'yes':
                    self.utils.print_info(f"Clicking on {option} option")
                    self.auto_actions.move_to_element(self.get_dfs_recurrence_widget_location_dismiss_yes_option())
                    self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_dismiss_yes_option)
                    sleep(5)

                    for row1 in self.get_dfs_recurrence_widget_location_grid_rows():
                        if location_name in row1.text:
                            kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_dfs_recurrence_widget()' -> " \
                                                 f"Location name : {location_name} in DFS Recurrence Widget Not " \
                                                 "Dismissed Successfully"
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.failed(**kwargs)
                            return -1
                        else:
                            kwargs['pass_msg'] = "'dismiss_anomaly_for_location_in_dfs_recurrence_widget()' -> " \
                                                 f"Location name : {location_name} in DFS Recurrence Widget Dismissed " \
                                                 "Successfully"
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.passed(**kwargs)
                            return 1
                return 1
        kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_dfs_recurrence_widget()' -> Anomaly not found for " \
                             f"Location :{location_name} in DFS Recurrence Widget"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def pin_individual_ap_for_location_in_dfs_recurrence_widget(self, location_name, ap_name, **kwargs):
        """
        - This Keyword will pin an AP at building level in DFS Recurrence Widget
        - Flow: CoPilot--> DFS Recurrence Widget ---> click Location Name in Rows --> Click AP row pin Button
        - Keyword Usage:
        - ``Pin Individual AP For Location In DFS Recurrence Widget   ${LOCATION_NAME}  ${AP_NAME}``


        :param location_name: Location name to enable anomaly Pin in DFS Recurrence Widget
        :param ap_name: AP name to enable pin in DFS Recurrence Widget of particular location
        :return: 1 if able to click pin button for the AP in Location or already pinned else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows in DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_dfs_recurrence_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Expanding Location: {location_name} Row in DFS Recurrence Widget")
                self.auto_actions.click(row)
                sleep(10)

                for row1 in self.get_dfs_recurrence_widget_location_grid_individual_ap_rows():
                    if ap_name in row1.text:
                        self.utils.print_info(f"Selecting Pin Button for the AP: {ap_name}")
                        if not self.get_dfs_recurrence_widget_location_already_pinned_status(row1):
                            self.utils.print_info(f"Clicking Pin Button in the AP Name {ap_name} Matched Row")
                            self.auto_actions.click(self.get_dfs_recurrence_widget_location_individual_ap_pin_button(row1))
                            sleep(5)

                            self.screen.save_screen_shot()
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_detailed_view_close_button)
                            sleep(5)
                            kwargs['pass_msg'] = "'pin_individual_ap_for_location_in_dfs_recurrence_widget()' -> " \
                                                 f"Pinned Anomaly successfully for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            kwargs['pass_msg'] = "'pin_individual_ap_for_location_in_dfs_recurrence_widget()' -> " \
                                                 f"Already Pinned Anomaly for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_detailed_view_close_button)
                            sleep(5)
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.passed(**kwargs)
                            return 1

        kwargs['fail_msg'] = "'pin_individual_ap_for_location_in_dfs_recurrence_widget()' -> Not found AP row " \
                             f"{ap_name} with Location:{location_name}"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def unpin_individual_ap_for_location_in_dfs_recurrence_widget(self, location_name, ap_name, **kwargs):
        """
        - This Keyword will Unpin an AP at building level in DFS Recurrence Widget
        - Flow: CoPilot--> DFS Recurrence Widget ---> click Location Name in Rows --> Click AP row Unpin Button
        - Keyword Usage:
        - ``UnPin Individual AP For Location In DFS Recurrence Widget   ${LOCATION_NAME}  ${AP_NAME}``


        :param location_name: Location name to enable anomaly UnPin in DFS Recurrence Widget
        :param ap_name: AP name to enable Unpin in DFS Recurrence Widget of particular location
        :return: 1 if able to click Unpin button for the AP in Location or already unpinned else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows in DFS Recurrence Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_dfs_recurrence_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Expanding Location: {location_name} Row in DFS Recurrence Widget")
                self.auto_actions.click(row)
                sleep(10)

                for row1 in self.get_dfs_recurrence_widget_location_grid_individual_ap_rows():
                    if ap_name in row1.text:
                        self.utils.print_info(f"Selecting unpin Button for the AP: {ap_name}")
                        if self.get_wifi_capacity_widget_location_already_pinned_status(row1):
                            self.utils.print_info(f"Clicking unpin Button in the AP Name {ap_name} Matched Row")
                            self.auto_actions.click(self.get_dfs_recurrence_widget_location_individual_ap_unpin_button(row1))
                            sleep(5)

                            self.screen.save_screen_shot()
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_detailed_view_close_button)
                            sleep(5)
                            kwargs['pass_msg'] = "'unpin_individual_ap_for_location_in_dfs_recurrence_widget()' -> " \
                                                 f"UnPinned Anomaly successfully for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.fault(**kwargs)
                            return 1
                        else:
                            kwargs['pass_msg'] = "'unpin_individual_ap_for_location_in_dfs_recurrence_widget()' -> " \
                                                 f"Already Unpinned Anomaly for the AP : {ap_name} in Location " \
                                                 f"{location_name}"
                            self.utils.print_info("Closing Detailed view")
                            self.auto_actions.click_reference(self.get_dfs_recurrence_widget_location_detailed_view_close_button)
                            sleep(5)
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            self.common_validation.fault(**kwargs)
                            return 1

        kwargs['fail_msg'] = "'unpin_individual_ap_for_location_in_dfs_recurrence_widget()' -> Not found AP row " \
                             f"{ap_name} with Location:{location_name}"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def verify_copilot_license_widget_manage_link(self, **kwargs):
        """
        - Verifies whether clicking on Manage link taking us to license page in Global Settings
        - Flow : Copilot page -->  Get CoPilot Licenses
        - Keyword Usage
        - ``Verify Copilot License Widget Manage Link``
        :return: Returns 1 if navigation successfully verified, -1 in case of any errors
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting CoPilot Licenses")
        sleep(30)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        widget = self.get_copilot_widget()
        self.auto_actions.move_to_element(widget)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on Manage link..")
        self.auto_actions.click_reference(self.get_copilot_license_mange_link)
        sleep(10)

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(10)

        license_page_header = self.get_license_page_heading()
        self.screen.save_screen_shot()

        if "License Information" in license_page_header.text:
            kwargs['pass_msg'] = "'verify_copilot_license_widget_manage_link()' -> Successfully navigated to Licenses " \
                                 "Information page"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'verify_copilot_license_widget_manage_link()' -> Unable to navigated to Licenses " \
                                 "Information page"
            self.common_validation.failed(**kwargs)
            return -1

    def refresh_copilot_dashboard_page(self):
        """
        - Refreshes the CoPilot Dashboard page so the data contained within it is current
        - Flow : Copilot page -->  Refresh CoPilot Dashboard Page
        - Keyword Usage
        - ``Refresh CoPilot Dashboard Page``
        :return: Returns 1 if the refresh action was successfully initiated, -1 in case of any errors
        """
        ret_val = 1

        refresh_btn = self.get_page_refresh_button()
        if refresh_btn:
            self.utils.print_info("Refreshing CoPilot Dashboard page")
            self.auto_actions.click(refresh_btn)
        else:
            self.utils.print_info("Unable to find Refresh button on CoPilot Dashboard page")
            ret_val = -1

        return ret_val

    def pin_anomaly_for_location_in_adverse_traffic_patterns_widget(self, location_name, **kwargs):
        """
        - This Keyword will pin an anomaly at building level in Adverse Traffic Patterns Widget
        - Flow: CoPilot--> ADVERSE TRAFFIC PATTERNS ---> Get Location Name in Rows and Click Pin Button
        - Keyword Usage:
        - ``Pin Anomaly For location In Adverse Traffic Patterns Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in Adverse Traffic Patterns widget
        :return: 1 if able to click anomaly Pin button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows in Adverse Traffic Patterns Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_adverse_traffic_patterns_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info("Selecting Pin Button for the Location in Adverse Traffic Patterns Widget: "
                                      f"{location_name}")
                if not self.get_adverse_traffic_patterns_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Pin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_adverse_traffic_patterns_widget_location_pin_button(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> Pinned " \
                                         "Anomaly successfully for the location in Adverse Traffic Patterns " \
                                         f"Widget : {location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> Already " \
                                         "Pinned Anomaly for the location in Adverse Traffic Patterns Widget: " \
                                         f"{location_name}"
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'pin_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> Not found Location " \
                             f"row with name:{location_name} in Adverse Traffic Patterns Widget"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def unpin_anomaly_for_location_in_adverse_traffic_patterns_widget(self, location_name, **kwargs):
        """
        - This Keyword will unpin an anomaly at building level in Adverse Traffic Patterns Widget
        - Flow: CoPilot--> ADVERSE TRAFFIC PATTERNS ---> Get Location Name in Rows and Click UnPin Button
        - Keyword Usage:
        - ``Unpin Anomaly For location In Adverse Traffic Patterns Widget   ${LOCATION_NAME}``


        :param location_name: Location name to enable anomaly Pin in Adverse Traffic Patterns Widget
        :return: 1 if able to click anomaly unpin button for the Location Name or already unpinned else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows in Adverse Traffic Patterns Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_adverse_traffic_patterns_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info("Selecting UnPin Button for the Location in Adverse Traffic Patterns Widget: "
                                      f"{location_name}")
                if self.get_adverse_traffic_patterns_widget_location_already_pinned_status(row):
                    self.utils.print_info("Clicking Unpin Button in the Location Name Matched Row")
                    self.auto_actions.click(self.get_adverse_traffic_patterns_widget_location_already_pinned_status(row))
                    sleep(5)

                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                         f"Successfully UnPinned Anomaly for the location : {location_name} " \
                                         "in Adverse Traffic Patterns Widget"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['pass_msg'] = "'pin_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> Already " \
                                         "unPinned Anomaly for the location in Adverse Traffic Patterns Widget."
                    self.common_validation.passed(**kwargs)
                    return 1

        kwargs['fail_msg'] = "'unpin_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> Not found Location " \
                             f"row with name:{location_name}"
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.common_validation.fault(**kwargs)
        return -1

    def show_muted_adverse_traffic_patterns_widget_anomalies(self, **kwargs):
        """
        - Changes the Adverse Traffic Patterns Widget Anomalies MUTED Button status to "SHOW MUTED"
        - Flow : Copilot page --> ADVERSE TRAFFIC PATTERNS
        - Keyword Usage
        - ``Show Muted Adverse Traffic Patterns Widget Anomalies``
        :return: returns 1 if successfully pressed SHOW MUTED button else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Adverse Traffic Patterns widget Summary")

        sleep(10)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_adverse_traffic_patterns_widget())
        self.screen.save_screen_shot()

        if 'HIDE MUTED' in self.get_adverse_traffic_patterns_widget_anomaly_muted().text:
            pass
        else:
            self.auto_actions.click_reference(self.get_adverse_traffic_patterns_widget_anomaly_muted)

        status = self.get_adverse_traffic_patterns_widget_anomaly_muted().text
        sleep(1)
        self.screen.save_screen_shot()
        self.utils.switch_to_default(CloudDriver().cloud_driver)

        if 'HIDE MUTED' in status:
            kwargs['pass_msg'] = "'show_muted_adverse_traffic_patterns_widget_anomalies()' -> Successfully Clicked button"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'show_muted_adverse_traffic_patterns_widget_anomalies()' -> UnSuccessfully Clicked button"
            self.common_validation.failed(**kwargs)
            return -1

    def hide_muted_adverse_traffic_patterns_widget_anomalies(self, **kwargs):
        """
        - Changes the Adverse Traffic Patterns Widget anomalies MUTED Button status to "HIDE MUTED"
        - Flow : Copilot page --> ADVERSE TRAFFIC PATTERNS
        - Keyword Usage
        - ``Hide Muted Adverse Traffic Patterns Widget Anomalies``
        :return: returns 1 if successfully pressed HIDE MUTED button else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Adverse Traffic Patterns widget Summary")

        sleep(10)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.auto_actions.move_to_element(self.get_adverse_traffic_patterns_widget())
        self.screen.save_screen_shot()

        if 'SHOW MUTED' in self.get_adverse_traffic_patterns_widget_anomaly_muted().text:
            pass
        else:
            self.auto_actions.click_reference(self.get_adverse_traffic_patterns_widget_anomaly_muted)

        sleep(1)
        self.screen.save_screen_shot()
        status = self.get_adverse_traffic_patterns_widget_anomaly_muted().text
        self.utils.switch_to_default(CloudDriver().cloud_driver)

        if 'SHOW MUTED' in status:
            kwargs['pass_msg'] = "'hide_muted_adverse_traffic_patterns_widget_anomalies()' -> Successfully Clicked button"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "'hide_muted_adverse_traffic_patterns_widget_anomalies()' -> UnSuccessfully Clicked button"
            self.common_validation.failed(**kwargs)
            return -1

    def get_adverse_traffic_patterns_widget_location_details(self, location_name=False, **kwargs):
        """
        - Get Adverse Traffic Patterns Widget Location Details
        - Flow : Copilot page --> Adverse Traffic Patterns Widget
        - param: location_name - location name
        - Keyword Usage
        - ``Get Adverse Traffic Patterns Widget Location Details``
        - ``Get Adverse Traffic Patterns Widget Location Details    location_name={LOCATION}``
        :return: returns location details as an array matching the location name passed as an argument: [1, '5544Location', 'Medium', False, False, '2', 'Last Detected: Sep 15 2021']
        :return: returns all locations details as an array of arrays like: [[1, '5544Location', 'Medium', False, False, '2', 'Last Detected: Sep 15 2021'], [2, '6699Location', 'High', False, False, '3', 'Last Detected: Sep 15 2021']]
        :return: returns -1 if error
        :return: returns -2 if error

        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Adverse Traffic Patterns Widget summary")

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(2)

        self.auto_actions.move_to_element(self.get_adverse_traffic_patterns_widget())
        sleep(5)

        self.screen.save_screen_shot()

        try:
            anomalies = self.get_adverse_traffic_patterns_list()
            index = 1
            anomaly_list = []
            for anomaly in anomalies:
                summary_array = []

                anomaly_summary = anomaly.text
                anomaly_location = self.get_adverse_traffic_patterns_anomaly_location(anomaly).text

                device_count = 0
                pinned = False
                muted = False

                if re.search(r'We detected problems with channels changing too often across (\d+) devices', anomaly_summary):
                    device_count = re.search(r'We detected problems with channels changing too often across (\d+) devices', anomaly_summary).group(1)

                severity = self.get_adverse_traffic_patterns_anomaly_severity(anomaly).text
                pinned_flag = self.get_adverse_traffic_patterns_anomaly_pinned(anomaly)
                muted_flag = self.get_adverse_traffic_patterns_anomaly_muted(anomaly)
                last_detected = self.get_adverse_traffic_patterns_anomaly_last_detected(anomaly).text

                if pinned_flag:
                    pinned = True

                if muted_flag:
                    muted = True

                summary_array.append(index)
                summary_array.append(anomaly_location)
                summary_array.append(severity)
                summary_array.append(pinned)
                summary_array.append(muted)
                summary_array.append(device_count)
                summary_array.append(last_detected)
                self.utils.print_debug("summary_array : ", summary_array)

                anomaly_list.append(summary_array)
                index += 1

            self.utils.print_debug("Anomaly List: ", anomaly_list)

            self.utils.switch_to_default(CloudDriver().cloud_driver)

            if location_name:
                for anomaly_element in anomaly_list:
                    if location_name in anomaly_element:
                        self.utils.print_info("Anomaly matched: ", anomaly_element)
                        return anomaly_element
                kwargs['fail_msg'] = "'get_adverse_traffic_patterns_widget_location_details()' -> No anomaly matched"
                self.common_validation.failed(**kwargs)
                return -2
            else:
                self.utils.print_info("Returning Anomaly List: ", anomaly_list)
                return anomaly_list
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "'get_adverse_traffic_patterns_widget_location_details()' -> Unable to get Adverse " \
                                 "Traffic Patterns Widget Summary"
            self.common_validation.fault(**kwargs)
            return -1

    def get_adverse_traffic_patterns_widget_ap_details_for_location(self, location_name, ap_name=False, **kwargs):
        """
        - This Keyword will pin an AP at building level in Adverse Traffic Patterns Widget
        - Flow: CoPilot--> Adverse Traffic Patterns Widget ---> click Location Name in Rows --> Get AP's Informations
        - Keyword Usage:
        - ``get_adverse_traffic_patterns_widget_ap_details_for_location   ${LOCATION_NAME}``
        - ``get_adverse_traffic_patterns_widget_ap_details_for_location   ${LOCATION_NAME}  ap_name=${AP_NAME}``

        :param location_name: Location name to enable anomaly Pin in Adverse Traffic Patterns Widget
        :return: returns location details as an array matching the ap name passed as an argument: [1, '13333366666666662AP', 'High', True, 0, 'Last Detected: Jan 16 2022']
        :return: returns all locations details as an array of arrays like: [[[1, '26666166666666661AP', 'Low', False, 0, 'Last Detected: Jan 16 2022'], [2, '26666266666666661AP', 'Medium', False, 0, 'Last Detected: Jan 16 2022']]
        :return: returns -1 if error
        :return: returns -2 if error
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Adverse Traffic Patterns Widget summary")

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(2)

        self.auto_actions.move_to_element(self.get_adverse_traffic_patterns_widget())
        sleep(5)

        self.screen.save_screen_shot()

        for row in self.get_adverse_traffic_patterns_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info(f"Expanding Location: {location_name} Row in Adverse Traffic Patterns Widget")
                self.auto_actions.click(row)
                sleep(10)

                try:
                    anomalies = self.get_adverse_traffic_patterns_device_list()
                    index = 1
                    anomaly_list = []
                    for anomaly in anomalies:
                        summary_array = []

                        anomaly_summary = anomaly.text
                        anomaly_location = self.get_adverse_traffic_patterns_anomaly_device_location(anomaly).text

                        device_count = 0
                        pinned = False

                        if re.search(r'We detected problems with channels changing too often across (\d+) devices',
                                     anomaly_summary):
                            device_count = re.search(
                                r'We detected problems with channels changing too often across (\d+) devices',
                                anomaly_summary).group(1)

                        severity = self.get_adverse_traffic_patterns_anomaly_device_severity(anomaly).text
                        pinned_flag = self.get_adverse_traffic_patterns_anomaly_device_pinned(anomaly)
                        last_detected = self.get_adverse_traffic_patterns_anomaly_device_last_detected(anomaly).text

                        if pinned_flag:
                            pinned = True

                        summary_array.append(index)
                        summary_array.append(anomaly_location)
                        summary_array.append(severity)
                        summary_array.append(pinned)
                        summary_array.append(device_count)
                        summary_array.append(last_detected)
                        self.utils.print_debug("summary_array : ", summary_array)

                        anomaly_list.append(summary_array)
                        index += 1

                    self.utils.print_debug("Anomaly List: ", anomaly_list)

                    self.utils.switch_to_default(CloudDriver().cloud_driver)

                    if ap_name:
                        for anomaly_element in anomaly_list:
                            if ap_name in anomaly_element:
                                self.utils.print_info("Anomaly matched: ", anomaly_element)
                                return anomaly_element
                        kwargs['fail_msg'] = "'get_adverse_traffic_patterns_widget_ap_details_for_location()' -> No " \
                                             "anomaly matched"
                        self.common_validation.failed(**kwargs)
                        return -2
                    else:
                        self.utils.print_info("Returning Anomaly List: ", anomaly_list)
                        return anomaly_list
                except Exception as e:
                    self.utils.print_info("Unable to get Adverse Traffic Patterns Widget Summary")
                    self.utils.print_info(e)
                    kwargs['fail_msg'] = "'get_adverse_traffic_patterns_widget_ap_details_for_location()' -> Unable " \
                                         "to get Adverse Traffic Patterns Widget Summary"
                    self.common_validation.fault(**kwargs)
                    return -1

    def mute_anomaly_for_location_in_adverse_traffic_patterns_widget(self, location_name, **kwargs):
        """
        - This Keyword will mute an anomaly at building level in Adverse Traffic Patterns Widget
        - Flow: CoPilot--> ADVERSE TRAFFIC PATTERNS ---> Get Location Name in Rows and Click Mute Button
        - Keyword Usage:
        - ``Mute Anomaly For Location In Adverse Traffic Patterns Widget   ${LOCATION_NAME}``


        :param location_name: Location name to Mute in Adverse Traffic Patterns widget
        :return: 1 if able to click anomaly Mute button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        sleep(5)
        self.utils.print_info("Scrolling down...")
        self.auto_actions.scroll_down()
        sleep(5)
        self.utils.print_info("Getting Location Name rows in Adverse Traffic Patterns Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_adverse_traffic_patterns_widget_location_grid_rows():
            if location_name in row.text:
                if 'Unmute' in row.text:
                    self.utils.print_info("Location entry " + location_name + " already muted")
                    return 1
                self.utils.print_info("Selecting More button from the Location in Adverse Traffic Patterns Widget: "
                                      f"{location_name}")
                more_options_button = self.get_adverse_traffic_patterns_widget_location_more_button(row)
                self.auto_actions.click(more_options_button)
                if more_options_button:
                    self.utils.print_info("Clicking Mute button in the Adverse Traffic Patterns Widget")
                    # get the button panel
                    button_panel = self.get_adverse_traffic_patterns_widget_location_mute_and_dismiss_div()
                    if button_panel:
                        mute_button = self.get_adverse_traffic_patterns_widget_location_mute_button(button_panel)
                        if mute_button:
                            self.auto_actions.click(mute_button)
                            sleep(10)
                            self.screen.save_screen_shot()
                            return 1
                        else:
                            kwargs['fail_msg'] = "'mute_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                                 "Unable to click Mute button in the Adverse Traffic Patterns Widget"
                            self.common_validation.failed(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "'mute_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                             "Unable to click Mute button in the Adverse Traffic Patterns Widget"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "'mute_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                         "Unable to click Mute button in the Adverse Traffic Patterns Widget"
                    self.common_validation.failed(**kwargs)
                    return -1
        # if code made it here then location was not found
        kwargs['fail_msg'] = "'mute_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                             f"Unable to location : {location_name} " "in Adverse Traffic Patterns Widget"
        self.common_validation.fault(**kwargs)
        return -1

    def unmute_anomaly_for_location_in_adverse_traffic_patterns_widget(self, location_name, **kwargs):
        """
        - This Keyword will unmute an anomaly at building level in Adverse Traffic Patterns Widget
        - Flow: CoPilot--> ADVERSE TRAFFIC PATTERNS ---> Get Location Name in Rows and Click Unmute Button
        - Keyword Usage:
        - ``Unmute Anomaly For Location In Adverse Traffic Patterns Widget   ${LOCATION_NAME}``


        :param location_name: Location name to Unmute in Adverse Traffic Patterns widget
        :return: 1 if able to click anomaly Mute button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        sleep(5)
        self.utils.print_info("Scrolling down...")
        self.auto_actions.scroll_down()
        sleep(5)
        self.utils.print_info("Getting Location Name rows in Adverse Traffic Patterns Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_adverse_traffic_patterns_widget_location_grid_rows():
            if location_name in row.text:
                if 'Unmute' not in row.text:
                    self.utils.print_info("Location entry " + location_name + " already unmuted")
                    return 1
                self.utils.print_info("Selecting Unmute button for the entry in the Adverse Traffic Patterns Widget: "
                                      f"{location_name}")
                unmute_button = self.get_adverse_traffic_patterns_widget_location_unmute_button(row)
                if unmute_button:
                    self.auto_actions.click(unmute_button)
                    sleep(10)
                    self.screen.save_screen_shot()
                    return 1
                else:
                    kwargs['fail_msg'] = "'unmute_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                         "Unable to select unmute button in the Adverse Traffic Patterns Widget"
                    self.common_validation.failed(**kwargs)
                    return -1
        # if code made it here then location was not found
        kwargs['fail_msg'] = "'unmute_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                             f"Unable to location : {location_name} " "in Adverse Traffic Patterns Widget"
        self.common_validation.fault(**kwargs)
        return -1

    def dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget(self, location_name, **kwargs):
        """
        - This Keyword will dismiss an anomaly entry in the Adverse Traffic Patterns Widget
        - Flow: CoPilot--> ADVERSE TRAFFIC PATTERNS ---> Get Location Name in Rows and Click Dismiss Button
        - Keyword Usage:
        - ``Dismiss Anomaly For Location In Adverse Traffic Patterns Widget   ${LOCATION_NAME}``


        :param location_name: Location name to Dismiss in Adverse Traffic Patterns widget
        :return: 1 if able to click anomaly Dismiss button for the Location Name or already clicked else -1
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Location Name rows in Adverse Traffic Patterns Widget")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        for row in self.get_adverse_traffic_patterns_widget_location_grid_rows():
            if location_name in row.text:
                self.utils.print_info("Selecting More Button from the Location in Adverse Traffic Patterns Widget: "
                                      f"{location_name}")
                more_options_button = self.get_adverse_traffic_patterns_widget_location_more_button(row)
                self.auto_actions.click(more_options_button)
                if more_options_button:
                    self.utils.print_info("Clicking Dismiss button in the Adverse Traffic Patterns Widget")
                    # get the button panel
                    button_panel = self.get_adverse_traffic_patterns_widget_location_mute_and_dismiss_div()
                    if button_panel:
                        dismiss_button = self.get_adverse_traffic_patterns_widget_location_dismiss_button(button_panel)
                        if dismiss_button:
                            self.auto_actions.click(dismiss_button)
                            self.utils.print_info("Clicking the OK button in the Adverse Traffic Patterns Widget Popup")
                            confirm_dialog = self.get_adverse_traffic_patterns_widget_location_dismiss_confirm_dialog()
                            sleep(5)
                            if confirm_dialog:
                                ok_button = self.get_adverse_traffic_patterns_widget_location_dismiss_confirm_dialog_okay(
                                    confirm_dialog)
                                if ok_button:
                                    self.auto_actions.click(ok_button)
                                    return 1
                                else:
                                    kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                                         "Unable to click the OK button"
                                    self.common_validation.failed(**kwargs)
                                    return -1
                            else:
                                kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                                  "Unable to locate Confirmation dialog"
                                self.common_validation.failed(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                              "Unable to click Mute button in the Adverse Traffic Patterns Widget"
                            self.common_validation.failed(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                             "Unable to click Mute button in the Adverse Traffic Patterns Widget"
                        self.common_validation.failed(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                                         "Unable to select more button in the Adverse Traffic Patterns Widget"
                    self.common_validation.failed(**kwargs)
                    return -1
        # if code made it here then location was not found
        kwargs['fail_msg'] = "'dismiss_anomaly_for_location_in_adverse_traffic_patterns_widget()' -> " \
                             f"Unable to location : {location_name} " "in Adverse Traffic Patterns Widget"
        self.common_validation.fault(**kwargs)
        return -1

    def get_adverse_traffic_patterns_widget_summary(self):
        """
        - Gets adverse traffic patterns widget summary in copilot Page
        - Flow : Copilot page --> adverse traffic patterns
        - Keyword Usage
        - ``${SUMMARY}  ${BUILDINGS}   ${AP}= Get Adverse Traffic Patterns Widget Summary``
        :return: returns Buildings and APs count if success else returns -1 or -2
        """
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.print_info("Getting Adverse Traffic Patterns Widget Summary")
        sleep(15)

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        adverse_traffic_patterns_summary = -1
        buildings = -1
        aps = -1

        try:
            adverse_traffic_patterns_summary = self.get_adverse_traffic_patterns_widget_content().text
            self.utils.print_info("Adverse Traffic Patterns widget Summary : ", adverse_traffic_patterns_summary)
            if re.search(r'(\d+) places in your environment, affecting (\d+) devices.',
                         adverse_traffic_patterns_summary):
                summary = re.search(r'(\d+) places in your environment, affecting (\d+) devices',
                                    adverse_traffic_patterns_summary)
                buildings = summary.group(1)
                aps = summary.group(2)
                self.utils.print_info("Total Buildings : ", buildings)
                self.utils.print_info("Total APs : ", aps)
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                return adverse_traffic_patterns_summary, buildings, aps
            else:
                self.utils.print_info("No anomalies detected for Adverse Traffic Patterns widget Summary")
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                return adverse_traffic_patterns_summary, buildings, aps
        except Exception as e:
            self.utils.print_info("Unable to get Adverse Traffic Patterns widget Summary")
            self.utils.print_info(e)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return adverse_traffic_patterns_summary, buildings, aps

    def click_wifi_capacity_anomaly_location_row(self, location_name, **kwargs):
        """
        - This Keyword will click the Location (location name) displaying the list of APs
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the Location row and click it
        - Keyword Usage:
        - ``Click Wifi Capacity Anomaly Location Row ${LOCATION_NAME}``

        :param location_name: Location name
        :return: 1 if successfully clicking the row else return -1
        """
        return_value = self.display_wifi_capacity_anomaly_ap_rows(location_name, **kwargs)
        return return_value

    def wifi_capacity_anomaly_ap_individual_details(self, location_name, ap_name, **kwargs):
        """
        - This Keyword will get details of issue and recommended actions from individual aps APs
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the Location row and click it
        - Keyword Usage:
        - ``Wifi Capacity Anomaly Ap Individual Details``

        :return: 1 if successfully clicking the row else return -1
        """
        self.click_wifi_capacity_anomaly_location_row(location_name)
        self.click_wifi_capacity_anomaly_ap_row(ap_name)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        issue_details = self.get_wifi_capacity_anomaly_ap_issue_details()
        recommended_actions_details = self.get_wifi_capacity_anomaly_ap_recommended_actions_details()
        if issue_details and recommended_actions_details:
            self.utils.print_info("Issue :", issue_details.text)
            self.utils.print_info("Recommended Actions :", recommended_actions_details.text)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return issue_details.text, recommended_actions_details.text
        else:
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            kwargs['fail_msg'] = "'wifi_capacity_anomaly_ap_individual_details()' -> Unsuccessfully clicking the row"
            self.common_validation.failed(**kwargs)
            return -1

    def display_wifi_capacity_anomaly_ap_rows(self, location_name, **kwargs):
        """
        - This Keyword will click the Location (location name) displaying the list of APs
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the Location row and click it
        - Keyword Usage:
        - ``Display Wifi Capacity Anomaly Ap Rows  ${LOCATION_NAME}``

        :param location_name: Location name
        :return: 1 if successfully clicking the row else return -1
        """
        return_value = -1
        searching_for_location_row = -1
        fail_message = ""
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)
        wifi_cap_widget = self.get_wifi_capacity_widget()
        if not wifi_cap_widget:
            self.utils.print_info("Unable to get WIFI capacty widget")
            fail_message = "Unable to get WIFI capacty widget"
            self.common_validation.failed(**kwargs)
        else:
            location_rows = self.get_wifi_capacity_widget_location_grid_rows_from_widget(wifi_cap_widget)
            if not location_rows:
                self.utils.print_info("Unable to get rows from widget")
                fail_message = "Unable to get rows from widget"
                self.common_validation.failed(**kwargs)
            else:
                self.utils.print_info("Searching for loacation : " + location_name)
                searching_for_location_row = 1
                for row in location_rows:
                    self.utils.print_info("Current location :" + row.text)
                    if location_name in row.text:
                        self.utils.print_info("Location : " + location_name + " found")
                        self.utils.print_info("Clicking on row")
                        self.auto_actions.click(row)
                        sleep(4)
                        return_value = 1
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        if return_value == -1:
            if searching_for_location_row == 1:
                fail_message = "Unable to find location : " + location_name
                self.utils.print_info(fail_message)
            kwargs['fail_msg'] = fail_message
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Location successfully clicked to display AP list"
            self.common_validation.passed(**kwargs)
        return return_value

    def click_wifi_capacity_anomaly_ap_row(self, ap_name, **kwargs):
        """
        - This Keyword will click the AP (ap name) based on the list of APs under a Location
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the ap row and click it
        - Keyword Usage:
        - ``Click Wifi Capacity Anomaly Ap Row {$AP_NAME}``

        :param ap_name: Ap name
        :return: 1 if sucessfully clicking the row else return -1
        """

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.utils.print_info("Attempting to gather all APs from loacation")
        internal_rows = self.get_wifi_capacity_widget_location_grid_internal_rows()
        if not internal_rows:
            self.utils.print_info("Unable to get APs from location")
            kwargs['fail_msg'] = "Unable to get APs from location"
            self.common_validation.failed(**kwargs)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return -1
        else:
            self.utils.print_info("Searching for AP : " + ap_name)
            for ap_row in internal_rows:
                self.utils.print_info("Current AP :" + ap_row.text)
                if ap_name in ap_row.text:
                    self.utils.print_info("AP name : " + ap_name + " found")
                    self.utils.print_info("Clicking on row")
                    self.auto_actions.click(ap_row)
                    kwargs['pass_msg'] = "Successfully clicked on AP : " + ap_name
                    self.common_validation.passed(**kwargs)
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    return 1
        self.utils.print_info("Unable to find AP : " + ap_name)
        kwargs['fail_msg'] = "Unable to find AP : " + ap_name
        self.common_validation.failed(**kwargs)
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        return -1

    def wifi_capacity_anomaly_ap_like_button(self, location_name, ap_name, **kwargs):
        """
        - This Keyword will click like button in WiFi Capacity widget specific location and access point.
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the Location row and click AP---> Click like Button
        - Keyword Usage:
        - ``Wifi Capacity Anomaly Ap Like Button   {LOCATION_NAME}   {AP_NAME}``
        :return: 1 if successfully clicked like Button for specific Location and ap the else return -1
        """
        self.click_wifi_capacity_anomaly_location_row(location_name)
        self.click_wifi_capacity_anomaly_ap_row(ap_name)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.screen.save_screen_shot()
        self.utils.print_info(f"Clicking like Button for the Location {location_name} and AP {ap_name}")
        self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_ap_like)
        self.screen.save_screen_shot()

        like_tooltip = self.get_wifi_capacity_widget_location_ap_like_tooltip()
        self.utils.print_info("Tooltip Message displayed on UI is :", like_tooltip.text)
        self.screen.save_screen_shot()
        if "Feedback saved successfully" in like_tooltip.text:
            self.utils.print_info(f"successfully liked the Wi-Fi capacity widget location {location_name} "
                                  f"for the ap {ap_name}")
            kwargs['pass_msg'] = "successfully liked the Wi-Fi capacity widget location"
            self.utils.print_info("Closing Detailed view")
            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
            self.screen.save_screen_shot()

            self.utils.switch_to_default(CloudDriver().cloud_driver)
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Unable to click like button for the Wi-Fi capacity widget location "
                                  f"{location_name} with ap {ap_name}")
            self.utils.print_info(f"successfully liked the Wi-Fi capacity widget location {location_name} "
                                  f"for the ap {ap_name}")
            kwargs['fail_msg'] = "Unable to click like button for the Wi-Fi capacity widget location"
            self.utils.print_info("Closing Detailed view")
            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
            self.screen.save_screen_shot()
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            self.common_validation.failed(**kwargs)
            return -1

    def is_wifi_capacity_anomaly_ap_i_icon_present(self, ap_name, **kwargs):
        """
        - This Keyword will check to see if the i icon is present on  the AP (ap name) row
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the ap row and see if the i icon is present
        - Keyword Usage:
        - ``Is Wifi Capacity Anomaly Ap i ICON Present {$AP_NAME}``

        :param ap_name: Ap name
        :return: 1 if Icon is present else return -1
        """

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.utils.print_info("Attempting to gather all APs from loacation")
        internal_rows = self.get_wifi_capacity_widget_location_grid_internal_rows()
        if not internal_rows:
            self.utils.print_info("Unable to get APs from location")
            kwargs['fail_msg'] = "Unable to get APs from location"
            self.common_validation.failed(**kwargs)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return -1
        for ap_row in internal_rows:
            self.utils.print_info("Current location :" + ap_row.text)
            if ap_name in ap_row.text:
                self.utils.print_info("AP name : " + ap_name + " found")
                self.utils.print_info("Checking for i ICON Presence")
                if "info" in ap_row.text:
                    self.utils.print_info("i ICON Found in AP row")
                    kwargs['pass_msg'] = "i ICON Found in AP row"
                    self.common_validation.passed(**kwargs)
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    return 1
                else:
                    self.utils.print_info("i ICON NOT Found in AP row")
                    kwargs['fail_msg'] = "i ICON NOT Found in AP row"
                    self.common_validation.failed(**kwargs)
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    return -1
        self.utils.print_info("Unable to find AP : " + ap_name)
        kwargs['fail_msg'] = "Unable to find AP : " + ap_name
        self.common_validation.failed(**kwargs)
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        return -1

    def get_hover_over_details_for_wifi_capacity_anomaly_ap_level(self, ap_name, **kwargs):
        """
        - This Keyword will get the text that is displayed when the i icon is hovered over
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the ap row and hover over the i (info) icon
        - Keyword Usage:
        - ``Get Hover Over Details For Wifi Capacity Anomaly Ap Level {$AP_NAME}``

        :param ap_name: Ap name
        :return: Detail text if successful else return -1
        """

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.utils.print_info("Attempting to gather all APs from loacation")
        internal_rows = self.get_wifi_capacity_widget_location_grid_internal_rows()
        if not internal_rows:
            self.utils.print_info("Unable to get APs from location")
            kwargs['fail_msg'] = "Unable to get APs from location"
            self.common_validation.failed(**kwargs)
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return -1
        for ap_row in internal_rows:
            self.utils.print_info("Current location :" + ap_row.text)
            if ap_name in ap_row.text:
                self.utils.print_info("AP name : " + ap_name + " found")
                self.utils.print_info("Attempting to locate column containing status, i icon, and pin")
                status_icon_pin_column = self.get_wifi_capacity_widget_location_ap_status_info_pin_column(ap_row)
                if status_icon_pin_column:
                    self.utils.print_info("Able to locate column containing status, i icon, and pin")
                    self.utils.print_info("Attempting to get  i(info) icon")
                    i_icon = self.get_wifi_capacity_widget_location_ap_info_icon(status_icon_pin_column)
                    if i_icon:
                        self.utils.print_info("Hovering over the  i(info) icon")
                        self.auto_actions.move_to_element(i_icon)
                        sleep(2)
                        self.utils.print_info("Attempting to gather detail data provided by the hovering over the i(info) icon")
                        tt_content = self.get_tooltip_content()
                        if tt_content:
                            tt_text = tt_content.text
                            self.utils.print_info("Data details from the hovering :" + tt_text)
                            kwargs['pass_msg'] = "Data details from the hovering :" + tt_text
                            self.common_validation.passed(**kwargs)
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            return tt_text
                        else:
                            self.utils.print_info("Unable to gather detail data from the hovering over the i(info) icon")
                            kwargs['fail_msg'] = "Unable to gather detail data from the hovering over the i(info) icon"
                            self.common_validation.failed(**kwargs)
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            return -1
                    else:
                        self.utils.print_info("Unable to get i(info) icon")
                        kwargs['fail_msg'] = "Unable to get i(info) icon"
                        self.common_validation.failed(**kwargs)
                        self.utils.switch_to_default(CloudDriver().cloud_driver)
                        return -1
                else:
                    self.utils.print_info("Unable to locate column containing status, i icon, and pin")
                    kwargs['fail_msg'] = "Unable to locate column containing status, i icon, and pin"
                    self.common_validation.failed(**kwargs)
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    return -1
        self.utils.print_info("Unable to find AP : " + ap_name)
        kwargs['fail_msg'] = "Unable to find AP : " + ap_name
        self.common_validation.failed(**kwargs)
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        return -1

    def dislike_wifi_capacity_anomaly_location_ap(self, location_name, ap_name, feedback="Need improvement", **kwargs):
        """
        - This Keyword will click dislike button in WiFi Capacity widget specific location and access point.
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get the Location row and click AP---> Click Dislike Button
        - Keyword Usage:
        - ``Dislike WiFi Capacity Anomaly Location AP   {LOCATION_NAME}   {AP_NAME}``
        - ``Dislike WiFi Capacity Anomaly Location AP   {LOCATION_NAME}   {AP_NAME}  feedback={MSG}``

        :return: 1 if successfully clicked Dislike Button for specific Location and ap the else return -1
        """
        self.utils.print_info("Getting Location Name rows on Wi-Fi capacity")
        self.click_wifi_capacity_anomaly_location_row(location_name)
        self.screen.save_screen_shot()

        self.utils.print_info(f"Getting AP Name rows on Wi-Fi capacity Location {location_name}")
        self.click_wifi_capacity_anomaly_ap_row(ap_name)
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        self.screen.save_screen_shot()

        self.utils.print_info(f"Clicking Dislike Button for the Location {location_name} and AP {ap_name}")
        self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_ap_dislike)
        self.screen.save_screen_shot()

        self.utils.print_info("Entering feedback text")
        self.auto_actions.send_keys(self.get_wifi_capacity_widget_location_ap_dislike_send_feedback_textfield(),
                                    feedback)
        self.screen.save_screen_shot()

        self.utils.print_info(f"Clicking Dislike Feedback Button for the Location {location_name} and AP {ap_name}")
        self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_ap_dislike_send_feedback_button)
        self.screen.save_screen_shot()

        tooltip = self.get_wifi_capacity_widget_location_ap_like_tooltip().text
        self.utils.print_info("Tooltip Message displayed on UI is :", tooltip)
        self.screen.save_screen_shot()

        if "Feedback saved successfully" in tooltip:
            if self.get_wifi_capacity_widget_location_ap_dislike_button_enabled_status():
                self.utils.print_info(f"successfully Disliked the Wi-Fi capacity widget location {location_name} "
                                      f"for the ap {ap_name}")
                kwargs['pass_msg'] = f"successfully Disliked the Wi-Fi capacity widget location {location_name} " \
                                     f"for the ap {ap_name}"
                self.common_validation.passed(**kwargs)

                self.utils.print_info("Closing Detailed view")
                self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
                self.screen.save_screen_shot()

                self.utils.switch_to_default(CloudDriver().cloud_driver)
                return 1
            else:
                self.utils.print_info("Unable to Click Dislike button Icon")
                kwargs['fail_msg'] = "Unable to Click Dislike button Icon"
                self.common_validation.failed(**kwargs)
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                self.utils.print_info("Closing Detailed view")
                self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info("Unable to click Dislike button for the Wi-Fi capacity widget location "
                                  f"{location_name} with ap {ap_name}")
            kwargs['fail_msg'] = "Unable to click Dislike button for the Wi-Fi capacity widget location " \
                                 f"{location_name} with ap {ap_name}"
            self.common_validation.failed(**kwargs)
            self.utils.print_info("Closing Detailed view")
            self.auto_actions.click_reference(self.get_wifi_capacity_widget_location_detailed_view_close_button)
            self.screen.save_screen_shot()
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            return -1

    def get_wifi_capacity_detailed_view(self, location_name, **kwargs):
        """
        - This Keyword will get detailed view data from the Location at the building level
        - Flow: CoPilot--> Wi-Fi CAPACITY ---> Get detailed view data from location
        - Keyword Usage:
        - ``Get Wifi Capacity Detailed View {$Location_Name}``

        :param location_name: Location Name
        :return: detaliled_data_string if successful else return -1
        """

        fail_message = ""
        detail_view_data = '\n' + "***Building*** : " + '\n'
        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        wifi_cap_widget = self.get_wifi_capacity_widget()
        if not wifi_cap_widget:
            self.utils.switch_to_default(CloudDriver().cloud_driver)
            fail_message = "Unable to get WIFI capacty widget"
            self.utils.print_info(fail_message)
            self.common_validation.failed(**kwargs)
            return -1
        else:
            location_rows = self.get_wifi_capacity_widget_location_grid_rows_from_widget(wifi_cap_widget)
            if not location_rows:
                self.utils.switch_to_default(CloudDriver().cloud_driver)
                fail_message = "Unable to get rows from widget"
                self.utils.print_info(fail_message)
                self.common_validation.failed(**kwargs)
                return -1
            else:
                self.utils.print_info("Searching for loacation : " + location_name)
                for row in location_rows:
                    row_text_no_newline = row.text.replace('\n', ' ')
                    self.utils.print_info("Current location :" + row_text_no_newline)
                    if location_name in row_text_no_newline:
                        self.utils.print_info("Location : " + location_name + " found")
                        detail_view_data = detail_view_data + "Location ->" + row_text_no_newline
                        self.utils.print_info("Clicking on row")
                        self.auto_actions.click(row)

                        self.utils.print_info("Attempting to get overall description of the anolomy")
                        overall_desc = self.get_wifi_capacity_widget_location_ap_overall_discription()
                        if not overall_desc:
                            kwargs['fail_msg'] = "Unable to get overall description of the anolomy"
                            self.utils.print_info(fail_message)
                            self.common_validation.failed(**kwargs)
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            return -1
                        detail_view_data = detail_view_data + '\n' + "***General Description***" + '\n' + "Description->" + (overall_desc.text).replace('\n', ' ')

                        self.utils.print_info("Attempting to gather all APs from loacation")
                        internal_rows = self.get_wifi_capacity_widget_location_grid_internal_rows()
                        if not internal_rows:
                            kwargs['fail_msg'] = "Unable to get APs from location"
                            self.utils.print_info(fail_message)
                            self.common_validation.failed(**kwargs)
                            self.utils.switch_to_default(CloudDriver().cloud_driver)
                            return -1
                        else:
                            detail_view_data = detail_view_data + '\n' + "***APs*** : "
                            for ap_row in internal_rows:
                                sleep(2)
                                detail_view_data = detail_view_data + '\n' + "AP -> " + (ap_row.text).replace('\n', ' ')
                        self.utils.switch_to_default(CloudDriver().cloud_driver)
                        pass_msg = "Successfully able to get Location and Ap detailed view data"
                        kwargs['pass_msg'] = pass_msg
                        self.utils.print_info(pass_msg)
                        self.utils.print_info(detail_view_data)
                        self.common_validation.passed(**kwargs)
                        return detail_view_data

                self.utils.switch_to_default(CloudDriver().cloud_driver)
                fail_message = "Unable to find location : " + location_name
                self.utils.print_info(fail_message)
                kwargs['fail_msg'] = fail_message
                self.common_validation.failed(**kwargs)
                return -1

    def navigate_wirless_clientexp_widget_by_location(self, location_name, parameter, **kwargs):
        """
        - This Keyword will navigate to wireless client experience and click on the location {building name}
        - Flow: CoPilot--> Wireless Client Experience ---> Click the Location name
        - Keyword Usage:
        - ``Click wireless clientexp widget by location {$location_name}``

        :param ap_name: Ap name
        :return: 1 if sucessfully clicking the row else return -1
        """

        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(2)

        # Move to Wireless client experience widget
        self.auto_actions.move_to_element(self.get_wireless_connectivity_experience_widget())

        # Select the option of location/ssid/ostype from the dropdown
        self.utils.print_info("Clicking view by options.")
        self.auto_actions.click(self.get_view_by_wireless_clientexp_option())
        self.screen.save_screen_shot()
        sleep(2)
        sort_options = self.get_wireless_clientexp_widget_viewby_options()
        self.utils.print_info(f"Sorting with {parameter}")
        self.auto_actions.select_drop_down_options(sort_options, parameter)
        sleep(2)

        wireless_clientexp_widget = self.get_wireless_connectivity_experience_widget()
        if not wireless_clientexp_widget:
            self.utils.print_info("Unable to get wireless client experience widget")
            fail_message = "Unable to get wireless client experience  widget"
            self.common_validation.failed(**kwargs)
        else:
            searching_for_location_row = 1
            location_rows = self.get_wireless_client_experience_widget_location_grid_rows_from_widget(wireless_clientexp_widget)
            if not location_rows:
                self.utils.print_info("Unable to get rows from widget")
                fail_message = "Unable to get rows from widget"
                self.common_validation.failed(**kwargs)
                return_value = -1
            else:
                return_value = -1
                self.utils.print_info("Searching for location : " + location_name)
                for row in location_rows:
                    self.utils.print_info("Current location :" + row.text)
                    if location_name in row.text:
                        self.utils.print_info("Location : " + location_name + " found")
                        self.utils.print_info("Clicking on row")
                        self.auto_actions.click(row)
                        sleep(4)
                        return_value = 1

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        if return_value == -1:
            if searching_for_location_row == 1:
                fail_message = "Unable to find location : " + location_name
                self.utils.print_info(fail_message)
            kwargs['fail_msg'] = fail_message
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "Location successfully clicked to display Quality Index"
            self.common_validation.passed(**kwargs)

        return return_value

    def get_wirless_clientexp_quality_index_by_location(self, location_name, parameter="Location", durationType="Last 24 Hours", **kwargs):
        """
        - This Keyword will get the Quality index values from Wireless client experience by location and Duration Tupe
        - Flow: CoPilot--> Wireless Client Experience ---> Click the Location name
        - Keyword Usage:
        - ``Click wireless clientexp widget by location {$location_name}``

        :param location_name: location name
        :param parameter: filter type Location, SSID, OSType
        :param durationType: Last 1 hrs , Last 24 hrs
        :return: Quality index values if sucessfully clicking the row else return NA
        """
        # will navigate to wireless client experience widget and click on location
        navigation_return = self.navigate_wirless_clientexp_widget_by_location(location_name, parameter, **kwargs)

        if navigation_return == -1:
            fail_message = "Unable to navigate to wireless client experience by location : " + location_name
            self.utils.print_info(fail_message)
            kwargs['fail_msg'] = fail_message
            self.common_validation.failed(**kwargs)
        else:
            self.utils.switch_to_iframe(CloudDriver().cloud_driver)
            self.utils.print_info("Clicking wireless client experience Duration option : " + durationType)
            self.auto_actions.click(self.get_wireless_client_experience_widget_duration_handle())
            self.utils.print_info("Searching for duration option : " + durationType)

            duration_options = self.get_wireless_client_experience_widget_duration_option()
            self.utils.print_info(f"Sorting with {durationType}")
            self.auto_actions.select_drop_down_options(duration_options, durationType)
            sleep(2)

            quality_index = self.get_wireless_clientexp_quality_index().text
            self.utils.print_info(f"Quality index {quality_index}")
            self.utils.switch_to_default(CloudDriver().cloud_driver)

            return quality_index.split("/")[0]

    def navigate_wirless_clientexp_widget_by_ssid(self, ssid_name, parameter, **kwargs):
        """
        - This Keyword will navigate to wireless client experience and click on the ssid {ssid name}
        - Flow: CoPilot--> Wireless Client Experience ---> Click the SSID
        - Keyword Usage:
        - ``Click wireless clientexp widget by location {$SSID_Name}``

        :param ap_name: Ap name
        :return: 1 if sucessfully clicking the row else return -1
        """

        self.utils.print_info("Navigating to Copilot menu..")
        if not self.get_copilot_branded_image():
            self.utils.switch_to_default(CloudDriver().cloud_driver)
        self.navigator.navigate_to_copilot_menu()
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(2)

        # Move to Wireless client experience widget
        self.auto_actions.move_to_element(self.get_wireless_connectivity_experience_widget())

        # Select the option of location/ssid/ostype from the dropdown
        self.utils.print_info("Clicking view by options.")
        self.auto_actions.click(self.get_view_by_wireless_clientexp_option())
        self.screen.save_screen_shot()
        sleep(2)
        sort_options = self.get_wireless_clientexp_widget_viewby_options()
        self.utils.print_info(f"Sorting with {parameter}")
        self.auto_actions.select_drop_down_options(sort_options, parameter)
        self.screen.save_screen_shot()
        sleep(2)

        wireless_clientexp_widget = self.get_wireless_connectivity_experience_widget()
        if not wireless_clientexp_widget:
            self.utils.print_info("Unable to get wireless client experience widget")
            fail_message = "Unable to get wireless client experience  widget"
            self.common_validation.failed(**kwargs)
        else:
            searching_for_ssid_row = 1
            ssid_rows = self.get_wireless_client_experience_widget_ssid_grid_rows_from_widget(wireless_clientexp_widget)
            if not ssid_rows:
                self.utils.print_info("Unable to get rows from widget")
                fail_message = "Unable to get rows from widget"
                self.common_validation.failed(**kwargs)
                return_value = -1
            else:
                return_value = -1
                self.utils.print_info("Searching for ssid : " + ssid_name)
                for row in ssid_rows:
                    self.utils.print_info("Current ssid :" + row.text)
                    if ssid_name in row.text:
                        self.utils.print_info("SSID : " + ssid_name + " found")
                        self.utils.print_info("Clicking on row")
                        self.auto_actions.click(row)
                        sleep(4)
                        return_value = 1

        self.utils.switch_to_default(CloudDriver().cloud_driver)
        if return_value == -1:
            if searching_for_ssid_row == 1:
                fail_message = "Unable to find location : " + ssid_name
                self.utils.print_info(fail_message)
            kwargs['fail_msg'] = fail_message
            self.common_validation.failed(**kwargs)
        else:
            kwargs['pass_msg'] = "ssid successfully clicked to display Quality Index"
            self.common_validation.passed(**kwargs)

        return return_value

    def get_wirless_clientexp_quality_index_by_ssid(self, ssid_name, parameter="SSID", durationType="Last 24 Hours", **kwargs):
        """
        - This Keyword will get the Quality index values from Wireless client experience by location and Duration Tupe
        - Flow: CoPilot--> Wireless Client Experience ---> Click the ssid name
        - Keyword Usage:
        - ``Click wireless clientexp widget by location {$ssid_name}``

        :param ssid_name: ssid name
        :param parameter: filter type Location, SSID, OSType
        :param durationType: Last 1 hrs , Last 24 hrs
        :return: Quality index values if sucessfully clicking the row else return NA
        """
        # will navigate to wireless client experience widget and click on location
        navigation_return = self.navigate_wirless_clientexp_widget_by_ssid(ssid_name, parameter, **kwargs)

        if navigation_return == -1:
            fail_message = "Unable to navigate to wireless client experience by ssid : " + ssid_name
            self.utils.print_info(fail_message)
            kwargs['fail_msg'] = fail_message
            self.common_validation.failed(**kwargs)
        else:
            self.utils.switch_to_iframe(CloudDriver().cloud_driver)
            self.utils.print_info("Clicking wireless client experience Duration option : " + durationType)
            self.auto_actions.click(self.get_wireless_client_experience_widget_duration_handle())
            self.utils.print_info("Searching for duration option : " + durationType)

            duration_options = self.get_wireless_client_experience_widget_duration_option()
            self.utils.print_info(f"Sorting with {durationType}")
            self.auto_actions.select_drop_down_options(duration_options, durationType)
            sleep(2)

            quality_index = self.get_wireless_clientexp_quality_index().text
            self.utils.print_info(f"Quality index {quality_index}")
            self.utils.switch_to_default(CloudDriver().cloud_driver)

            return quality_index.split("/")[0]
