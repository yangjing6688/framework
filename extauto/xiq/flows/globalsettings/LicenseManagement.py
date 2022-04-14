import re
from time import sleep

from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.common.Login import Login
from extauto.xiq.elements.LicenseManagementWebElements import LicenseManagementWebElements
from extauto.xiq.elements.LoginWebElements import LoginWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements


class LicenseManagement(LicenseManagementWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.navigator = Navigator()
        self.login = Login()
        self.lic_mgt_web_elements = LicenseManagementWebElements()
        self.login_web_elements = LoginWebElements()
        self.nav_web_elements = NavigatorWebElements()
        # self.driver = extauto.common.CloudDriver.cloud_driver

    def open_license_management_page(self):
        """
         - Navigates to License Management Page
         - Flow : User account image-->Global Settings--> License Management
         - Keyword Usage
          - ``Open License Management Page``

        :return: 1 if License Management page was opened, else -1
        """
        self.utils.print_info("Navigating to the License Management page..")
        if self.navigator.navigate_to_license_mgmt() == 1:
            return 1
        else:
            self.screen.save_screen_shot()
            return -1

    def is_entitlements_table_empty(self):
        """
         - Checks if the Entitlements table is empty.
         - Assumes the License Management page is already being displayed.
         - Keyword Usage
          - ``Is Entitlements Table Empty``

        :return: 1 if Entitlements Table is empty ("No records found." is displayed), else -1
        """
        ret_val = -1

        no_data_el = self.get_entitlements_no_data()
        # if no_data_el and no_data_el.is_displayed():
        if no_data_el:
            self.utils.print_info("Entitlements table is empty")
            ret_val = 1
        else:
            self.utils.print_info("Entitlements table is not empty")

        return ret_val

    def is_legacy_table_empty(self):
        """
         - Checks if the Legacy Entitlements table is empty.
         - Assumes the License Management page is already being displayed.
         - Keyword Usage
          - ``Is Legacy Table Empty``

        :return: 1 if Legacy Entitlements Table is empty ("No data" is displayed), else -1
        """
        no_data_el = self.lic_mgt_web_elements.get_legacy_no_data()
        if no_data_el and no_data_el.is_displayed():
            self.utils.print_info("Legacy Entitlements table is empty")
            return 1
        else:
            self.utils.print_info("Legacy Entitlements table is not empty")
            return -1

    def confirm_entitlements_table_contains_data(self):
        """
         - Checks if the Entitlements table contains data.
         - Assumes the License Management page is already being displayed.
         - Keyword Usage
          - ``Confirm Entitlements Table Contains Data``

        :return: 1 if Entitlements Table is not empty, else -1
        """
        if self.is_entitlements_table_empty() == 1:
            self.utils.print_info("Entitlements table does not contain data")
            self.screen.save_screen_shot()
            return -1
        else:
            self.utils.print_info("Entitlements table contains data")
            return 1

    def confirm_legacy_table_contains_data(self):
        """
         - Checks if the Legacy Entitlements table contains data.
         - Assumes the License Management page is already being displayed.
         - Keyword Usage
          - ``Confirm Legacy Table Contains Data``

        :return: 1 if Legacy Entitlements Table is not empty, else -1
        """
        if self.is_legacy_table_empty() == 1:
            self.utils.print_info("Legacy Entitlements table does not contain data")
            self.screen.save_screen_shot()
            return -1
        else:
            self.utils.print_info("Legacy Entitlements table contains data")
            return 1

    def verify_ek_in_legacy_ek_table(self, ekey):
        """
                 - Checks if legacy ek exists in the legacy ek table
                 - pass the ek as input parameter to verify the ek to be checked
                :return: 1 if ek exists , else -1
        """
        if ekey is not None:
            self.utils.switch_to_iframe_with_attr(CloudDriver().cloud_driver,'@id="iframeIdForLicenseInfo"')
            legacy_ek_elems = self.lic_mgt_web_elements.get_legacy_ek_data()
            self.utils.print_info(legacy_ek_elems)
            for ele in legacy_ek_elems:
                ek = ele.text
                self.utils.print_info(ek)
                if re.search(ekey, ek):
                    self.utils.print_info("Legacy EK exists in the legacy ek table.")
                    self.utils.switch_to_default(CloudDriver().cloud_driver)
                    return 1
                else:
                    self.utils.print_info("Legacy EK not found the the table.")
                    return -1

    def verify_contact_sales_btn_dispalyed(self):
        """
        :return: contact sales button must be displayed
        """
        cont_sales_btn = self.lic_mgt_web_elements.get_contact_sales_btn()
        if cont_sales_btn.is_displayed():
            self.utils.print_info("Contact Sales Button is displayed.")
            return 1
        else:
            self.utils.print_info("Contact Sales Button is NOT displayed.")
            return -1

    def verify_xiq_linked_to_extr_portal(self):
        """
        verify XIQ is linked to extreme portal
        :return:
        """
        unlink_extr_portal_btn = self.lic_mgt_web_elements.get_unlink_xiq_from_extr_portal_btn()
        xiq_link_status = self.lic_mgt_web_elements.get_xiq_linked_to_extreme_portal_status()
        extr_lic_portal_link = self.lic_mgt_web_elements.get_extr_licensing_portal_btn()
        if unlink_extr_portal_btn.is_displayed():
            self.utils.print_info("XIQ is linked to Extreme Portal.")
            if xiq_link_status.is_displayed():
                self.utils.print_info(xiq_link_status.text)
            else:
                self.utils.print_info("XIQ Successfully linked to a customer account msg is not displayed.")
                return -2
            if extr_lic_portal_link.is_displayed():
                self.utils.print_info("Extreme Licensing Portal link is dispalyed.")
            else:
                self.utils.print_info("Extreme Licensing Portal link is not displayed.")
                return -2
            return 1
        else:
            self.utils.print_info("XIQ is not linked to Extreme Portal.")
            return -1

    def verify_xiq_not_linked_to_extr_portal(self):
        """
        verify XIQ is not linked to extreme portal
        :return:
        """
        link_extr_portal_btn = self.lic_mgt_web_elements.get_link_to_extr_portal_btn()
        cust_partner_info = self.lic_mgt_web_elements.get_xiq_cust_partner_info()
        xiq_not_link_status = self.lic_mgt_web_elements.get_xiq_not_linked_to_extreme_portal_status()
        if link_extr_portal_btn.is_displayed():
            self.utils.print_info("XIQ is not linked to Extreme Portal button is displayed.")
            if cust_partner_info.is_displayed():
                self.utils.print_info("Tooltip Info to customers/partners is displayed.")
            else:
                self.utils.print_info("Tooltip Info to customers/partners is not displayed.")
                return -2
            if xiq_not_link_status.is_displayed():
                self.utils.print_info("XIQ is not linked to extreme portal status is displayed.")
            else:
                self.utils.print_info("XIQ not linked status is not displayed.")
                return -2
            return 1
        else:
            self.utils.print_info("Link XIQ to Extreme Portal button is not displayed.")
            return -1

    def unlink_xiq_from_extr_portal(self):
        """
            - Unlink XIQ from extreme portal
        :return: 1 if unlinked else -1
        """
        unlink_btn = self.lic_mgt_web_elements.get_unlink_xiq_from_extr_portal_btn()
        if unlink_btn.is_displayed():
            self.auto_actions.click(unlink_btn)
            self.utils.print_info("Clicked on unlink button.")
            sleep(5)
            try:
                confirm_msg = self.lic_mgt_web_elements.get_unlink_confirm_msg()
                confirm_msg_txt = confirm_msg.text
                self.utils.print_info("unlink confirm msg is displayed:", confirm_msg_txt)
                unlink_yes_btn = self.lic_mgt_web_elements.get_unlink_confirm_yes_btn()
                if unlink_yes_btn.is_displayed():
                    self.auto_actions.move_to_element(unlink_yes_btn)
                    sleep(2)
                    self.auto_actions.click(unlink_yes_btn)
                    sleep(5)
                    unlink = self.verify_xiq_not_linked_to_extr_portal()
                    if unlink == 1:
                        self.utils.print_info("Unlink is successful...")
                        return 1
                    else:
                        self.utils.print_info("Unlink NOT successful...")
                        return -1
                else:
                    self.utils.print_info("Unlink NOT successful...")
                    return -1
            except Exception as e:
                self.utils.print_info("Unlink NOT successful.")
                return -1
        else:
            self.utils.print_info("Unlink button is not visible.")
            return -1

    def initiate_link_xiq_to_extr_portal_from_lic_mgt(self, sfdc_user_type=None, sfdc_email=None, sfdc_pwd=None, shared_cuid=None):
        """
             - links XIQ to extreme SFDC portal to get gemalto licenses
             - pass the below parameters as the keyword input:
             - sfdc user type (customer or parter)
             - sfdc customer/partner login email and password
             - shared cuid if parter login is used
            :return: 1 linking is successful , else -1
        """
        self.utils.print_info("link to extr portal...")
        link_to_extr_portal_btn = self.lic_mgt_web_elements.get_link_to_extr_portal_btn()
        if link_to_extr_portal_btn.is_displayed():
            self.utils.print_info("Link to Extreme Portal button is displayed.")
            self.auto_actions.click(link_to_extr_portal_btn)
            try:
                upgrade_msg_txt = self.lic_mgt_web_elements.get_upgrade_dialog_msg().text
                self.utils.print_info("Warning msg to user before upgrade: ", upgrade_msg_txt)
                self.utils.print_info("Select Checkbox I Agree...")
                self.auto_actions.enable_check_box(self.lic_mgt_web_elements.get_upgrade_iagree_chkbox())
                sleep(3)
                self.utils.print_info("Click on Continue button to upgrade...")
                self.auto_actions.click(self.lic_mgt_web_elements.get_upgrade_continue_btn())
                sleep(10)
                self.utils.print_info("Redirected to SFDC for oauth...")
            except Exception as e:
                self.utils.print_info("No confirmation dialog is shown.")
            return 1
        else:
            self.utils.print_info("Link to Extreme Portal button is not displayed.")
            return -1

    def navigate_and_get_entitlement_counts_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Navigates to the License Management page and returns counts from the Entitlements table as a dictionary.
        - Keyword Usage:
         - ``${COUNTS}=   Navigate and Get Entitlement Counts For Feature``
         - ``${COUNTS}=   Navigate and Get Entitlement Counts For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNTS}=   Navigate and Get Entitlement Counts For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNTS}=   Navigate and Get Entitlement Counts For Feature    PRD-XIQ-NAC-S``

        :return: Returns counts from the Entitlements table as a dictionary
        """
        self.utils.print_info("Navigate to License Management page")
        self.navigator.navigate_to_license_management()
        sleep(2)

        return self.get_entitlement_counts_for_feature(feature)

    def navigate_and_get_entitlement_device_count_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Gets the entitlement "Device Count" for the specified feature.
        - Keyword Usage:
         - ``${COUNT}=   Navigate and Get Entitlement Device Count For Feature``
         - ``${COUNT}=   Navigate and Get Entitlement Device Count For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNT}=   Navigate and Get Entitlement Device Count For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNT}=   Navigate and Get Entitlement Device Count For Feature    PRD-XIQ-NAC-S``

        :param feature: feature to return the device count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S
        :return: total number of devices allotted to the specified feature
        """
        self.utils.print_info("Navigate to License Management page")
        self.navigator.navigate_to_license_management()
        sleep(2)

        return self.get_entitlement_device_count_for_feature(feature)

    def navigate_and_get_entitlement_available_count_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Gets the entitlement "Available" count for the specified feature.
        - Keyword Usage:
         - ``${COUNT}=   Navigate and Get Entitlement Available Count For Feature``
         - ``${COUNT}=   Navigate and Get Entitlement Available Count For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNT}=   Navigate and Get Entitlement Available Count For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNT}=   Navigate and Get Entitlement Available Count For Feature    PRD-XIQ-NAC-S``

        :param feature: feature to return the available count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S
        :return: total number of available licenses allotted to the specified feature
        """
        self.utils.print_info("Navigate to License Management page")
        self.navigator.navigate_to_license_management()
        sleep(2)

        return self.get_entitlement_available_count_for_feature(feature)

    def navigate_and_get_entitlement_activated_count_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Gets the entitlement "Activated" count for the specified feature.
        - Keyword Usage:
         - ``${COUNT}=   Navigate and Get Entitlement Activated Count For Feature``
         - ``${COUNT}=   Navigate and Get Entitlement Activated Count For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNT}=   Navigate and Get Entitlement Activated Count For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNT}=   Navigate and Get Entitlement Activated Count For Feature    PRD-XIQ-NAC-S``

        :param feature: feature to return the activated count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S
        :return: total number of activations allotted to the specified feature
        """
        self.utils.print_info("Navigate to License Management page")
        self.navigator.navigate_to_license_management()
        sleep(2)

        return self.get_entitlement_activated_count_for_feature(feature)

    def get_entitlement_counts_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Returns counts of the specified feature from the Entitlements table as a dictionary
        - Keyword Usage
         - ``${COUNTS}=   Get Entitlement Counts For Feature``
         - ``${COUNTS}=   Get Entitlement Counts For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNTS}=   Get Entitlement Counts For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNTS}=   Get Entitlement Counts For Feature    PRD-XIQ-NAC-S``
        :return: Returns counts for the specified feature from the Entitlements table as a dictionary
        """
        licenses = dict()
        activated_count = 0
        available_count = 0
        devices_count = 0

        rows = self.get_entitlements_rows()
        if rows:
            self.utils.print_info(f"Got {len(rows)} rows from the Entitlements table")

            for row in rows:
                feature_value = self.get_entitlements_row_feature_value(row)
                if feature_value:
                    if feature_value.text == feature:
                        self.utils.print_debug(f"{feature_value.text} matches desired feature {feature}")

                        # Calculate the count from the Available column
                        available_value = self.get_entitlements_row_available_value(row)
                        available_text = available_value.text
                        self.utils.print_debug(f"Available value is {available_text}")
                        available_count += int(available_text)

                        # Calculate the count from the Activated column
                        activated_value = self.get_entitlements_row_activated_value(row)
                        activated_text = activated_value.text
                        self.utils.print_debug(f"Activated value is {activated_text}")
                        activated_count += int(activated_text)

                        # Calculate the count from the Devices column
                        devices_value = self.get_entitlements_row_devices_value(row)
                        devices_text = devices_value.text
                        self.utils.print_debug(f"Devices value is {devices_text}")
                        devices_count += int(devices_text)

                        # We need to keep looping in case the features are split onto multiple table rows
                else:
                    self.utils.print_info(f"Could not obtain feature value for row: {row}")
        else:
            self.utils.print_info("Entitlements table is empty")

        # Now that we have looped through all table rows and calculated the totals for the feature,
        # the counts can be returned
        licenses['feature'] = feature
        licenses['available'] = available_count
        licenses['activated'] = activated_count
        licenses['devices'] = devices_count

        self.utils.print_info(f"Returning license counts: {licenses}")
        return licenses

    def get_entitlement_device_count_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Gets the entitlement "Devices" value for the specified feature.
        - Keyword Usage:
         - ``${COUNT}=   Get Entitlement Device Count For Feature``
         - ``${COUNT}=   Get Entitlement Device Count For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNT}=   Get Entitlement Device Count For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNT}=   Get Entitlement Device Count For Feature    PRD-XIQ-NAC-S``

        :param feature: feature to return the device count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S
        :return: total number of devices allotted to the specified feature
        """
        device_count = 0

        table_row_list = self.get_entitlements_rows()
        if table_row_list:
            self.utils.print_info(f"Got {len(table_row_list)} rows")
            for table_row in table_row_list:
                if table_row:
                    feature_value = self.get_entitlements_row_feature_value(table_row)
                    if feature_value:
                        self.utils.print_debug(f"{feature_value.text} matches desired feature {feature}")
                        if feature_value.text == feature:
                            devices_value = self.get_entitlements_row_devices_value(table_row)
                            devices_text = devices_value.text
                            self.utils.print_debug(f"Devices value is {devices_text}")
                            device_count += int(devices_text)
                        else:
                            self.utils.print_debug(f"{feature_value.text} does not match desired feature {feature}")
        else:
            self.utils.print_info("Entitlements table is empty")

        self.utils.print_info(f"Returning DEVICES count {device_count} for feature {feature}")
        return device_count

    def get_entitlement_available_count_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Gets the entitlement "Available" value for the specified feature.
        - Keyword Usage:
         - ``${COUNT}=   Get Entitlement Available Count For Feature``
         - ``${COUNT}=   Get Entitlement Available Count For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNT}=   Get Entitlement Available Count For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNT}=   Get Entitlement Available Count For Feature    PRD-XIQ-NAC-S``

        :param feature: feature to return the available count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S
        :return: total number of available licenses allotted to the specified feature
        """
        available_count = 0

        table_row_list = self.get_entitlements_rows()
        if table_row_list:
            self.utils.print_info(f"Got {len(table_row_list)} rows")
            for table_row in table_row_list:
                if table_row:
                    feature_value = self.get_entitlements_row_feature_value(table_row)
                    if feature_value:
                        self.utils.print_debug(f"{feature_value.text} matches desired feature {feature}")
                        if feature_value.text == feature:
                            available_value = self.get_entitlements_row_available_value(table_row)
                            available_text = available_value.text
                            self.utils.print_debug(f"Available value is {available_text}")
                            available_count += int(available_text)
                        else:
                            self.utils.print_debug(f"{feature_value.text} does not match desired feature {feature}")
        else:
            self.utils.print_info("Entitlements table is empty")

        self.utils.print_info(f"Returning AVAILABLE count {available_count} for feature {feature}")
        return available_count

    def get_entitlement_activated_count_for_feature(self, feature="PRD-XIQ-PIL-S-C"):
        """
        - Gets the entitlement "Activated" value for the specified feature.
        - Keyword Usage:
         - ``${COUNT}=   Get Entitlement Activated Count For Feature``
         - ``${COUNT}=   Get Entitlement Activated Count For Feature    PRD-XIQ-PIL-S-C``
         - ``${COUNT}=   Get Entitlement Activated Count For Feature    PRD-XIQ-NAV-S-C``
         - ``${COUNT}=   Get Entitlement Activated Count For Feature    PRD-XIQ-NAC-S``

        :param feature: feature to return the activated count for;  PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S
        :return: total number of activated licenses for the specified feature
        """
        activated_count = 0

        table_row_list = self.get_entitlements_rows()
        if table_row_list:
            self.utils.print_info(f"Got {len(table_row_list)} rows")
            for table_row in table_row_list:
                if table_row:
                    feature_value = self.get_entitlements_row_feature_value(table_row)
                    if feature_value:
                        self.utils.print_debug(f"{feature_value.text} matches desired feature {feature}")
                        if feature_value.text == feature:
                            activated_value = self.get_entitlements_row_activated_value(table_row)
                            activated_text = activated_value.text
                            self.utils.print_debug(f"Activated value is {activated_text}")
                            activated_count += int(activated_text)
                        else:
                            self.utils.print_debug(f"{feature_value.text} does not match desired feature {feature}")
        else:
            self.utils.print_info("Entitlements table is empty")

        self.utils.print_info(f"Returning ACTIVATED count {activated_count} for feature {feature}")
        return activated_count

    def wait_until_entitlement_counts_for_feature_matches(self, feature, expected_available, expected_activated, expected_devices,
                                                          retry_duration=30, retry_count=30):
        """
        - This keyword is used to wait until the entitlement counts (Available, Activated, Devices) for the specified
        - feature match the expected value.
        -
        - Keyword Usage:
         - ``Wait Until Entitlement Counts For Feature Matches    PRD-XIQ-PIL-S-C    9    1       1``
         - ``Wait Until Entitlement Counts For Feature Matches    PRD-XIQ-NAV-S-C    2    0       0``
         - ``Wait Until Entitlement Counts For Feature Matches    PRD-XIQ-NAC-S      0    1000    1000``

        :param feature: type of license entitlement to check the counts of (PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)
        :param expected_available: expected value for the "Available" column for the specified license entitlement feature
        :param expected_activated: expected value for the "Activated" column for the specified license entitlement feature
        :param expected_devices: expected value for the "Devices" column for the specified license entitlement feature
        :param retry_duration: duration between each retry
        :param retry_count: number of times to retry
        :return: 1 if counts for feature matches within time, else -1
        """

        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Device Count Check for feature {feature} - Loop: {count}")

            # Navigate away from and back to page to force a refresh of the data
            # NOTE: this can be changed to a refresh when the page supports refresh functionality
            self.navigator.navigate_to_devices()
            self.navigator.navigate_to_license_management()

            # Retrieve the counts for the specified feature
            counts_dict = self.get_entitlement_counts_for_feature(feature)
            available_count = counts_dict["available"]
            activated_count = counts_dict["activated"]
            devices_count = counts_dict["devices"]

            # Compare the counts with what is expected for the specified feature
            if available_count == int(expected_available) and \
               activated_count == int(expected_activated) and \
               devices_count == int(expected_devices):
                self.utils.print_info(f"Counts for {feature} are at the expected values:\n"
                                      f"  Available: {expected_available}\n"
                                      f"  Activated: {expected_activated}\n"
                                      f"  Devices:   {expected_devices}")
                return 1
            else:
                self.utils.print_info(f"Counts for {feature} are not at expected values.\n"
                                      f"Current values are:\n"
                                      f"  Available: {available_count}\n"
                                      f"  Activated: {activated_count}\n"
                                      f"  Devices:   {devices_count}\n"
                                      f"Expected values are:\n"
                                      f"  Available: {expected_available}\n"
                                      f"  Activated: {expected_activated}\n"
                                      f"  Devices:   {expected_devices}\n"
                                      f"Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        self.utils.print_info(f"Counts for {feature} are not at expected values. Please check.")
        self.screen.save_screen_shot()

        return -1

    def wait_until_entitlement_device_count_for_feature_matches(self, expected, feature="PRD-XIQ-PIL-S-C",
                                                                retry_duration=30, retry_count=30):
        """
        - This keyword is used to wait until the device count for the specified license entitlement matches the
        - expected value.
        -
        - Keyword Usage:
         - ``Wait Until Entitlement Device Count For Feature Matches    1``
         - ``Wait Until Entitlement Device Count For Feature Matches    0  feature=PRD-XIQ-NAV-S-C``
         - ``Wait Until Entitlement Device Count For Feature Matches    3  retry_duration=10    retry_count=12``
         - ``Wait Until Entitlement Device Count For Feature Matches    2  feature=PRD-XIQ-PIL-S-C    retry_duration=60    retry_count=5``
         - ``Wait Until Entitlement Device Count For Feature Matches    1  feature=PRD-XIQ-NAV-S-C    retry_duration=30    retry_count=10``
         - ``Wait Until Entitlement Device Count For Feature Matches    1  feature=PRD-XIQ-NAC-S      retry_duration=15    retry_count=8``

        :param expected: expected number of devices for specified license entitlement feature
        :param feature: type of license entitlement to check the device count of (e.g., PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device count for feature matches within time, else -1
        """

        device_count = 0
        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Device Count Check for feature {feature} - Loop: {count}")

            # Navigate away from and back to page to force a refresh of the data
            self.navigator.navigate_to_devices()
            self.navigator.navigate_to_license_management()

            # Check the device count for the specified feature
            device_count = self.get_entitlement_device_count_for_feature(feature)
            if device_count == int(expected):
                self.utils.print_info(f"Device count for {feature} is at expected value {expected}")
                return 1
            else:
                self.utils.print_info(f"Device count for {feature} is {device_count}, not expected value {expected}. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        self.utils.print_info(f"Device count for {feature} is {device_count}, not expected value {expected}. Please check.")
        self.screen.save_screen_shot()
        sleep(2)

        return -1

    def wait_until_entitlement_available_count_for_feature_matches(self, expected, feature="PRD-XIQ-PIL-S-C",
                                                                   retry_duration=30, retry_count=30):
        """
        - This keyword is used to wait until the available count for the specified license entitlement matches the
        - expected value.
        -
        - Keyword Usage:
         - ``Wait Until Entitlement Available Count For Feature Matches    1``
         - ``Wait Until Entitlement Available Count For Feature Matches    0  feature=PRD-XIQ-NAV-S-C``
         - ``Wait Until Entitlement Available Count For Feature Matches    3  retry_duration=10    retry_count=12``
         - ``Wait Until Entitlement Available Count For Feature Matches    2  feature=PRD-XIQ-PIL-S-C    retry_duration=60    retry_count=5``
         - ``Wait Until Entitlement Available Count For Feature Matches    1  feature=PRD-XIQ-NAV-S-C    retry_duration=30    retry_count=10``
         - ``Wait Until Entitlement Available Count For Feature Matches    1  feature=PRD-XIQ-NAC-S      retry_duration=15    retry_count=8``

        :param expected: expected number of available licenses for specified license entitlement feature
        :param feature: type of license entitlement to check the available count of (e.g., PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if available count for feature matches within time, else -1
        """

        available_count = 0
        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Available Count Check for feature {feature} - Loop: {count}")

            # Navigate away from and back to page to force a refresh of the data
            self.navigator.navigate_to_devices()
            self.navigator.navigate_to_license_management()

            # Check the available count for the specified feature
            available_count = self.get_entitlement_available_count_for_feature(feature)
            if available_count == int(expected):
                self.utils.print_info(f"Available count for {feature} is at expected value {expected}")
                return 1
            else:
                self.utils.print_info(f"Available count for {feature} is {available_count}, not expected value {expected}. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        self.utils.print_info(f"Available count for {feature} is {available_count}, not expected value {expected}. Please check.")
        self.screen.save_screen_shot()
        sleep(2)

        return -1

    def wait_until_entitlement_activated_count_for_feature_matches(self, expected, feature="PRD-XIQ-PIL-S-C",
                                                                   retry_duration=30, retry_count=30):
        """
        - This keyword is used to wait until the activated count for the specified license entitlement matches the
        - expected value.
        -
        - Keyword Usage:
         - ``Wait Until Entitlement Activated Count For Feature Matches    1``
         - ``Wait Until Entitlement Activated Count For Feature Matches    0  feature=PRD-XIQ-NAV-S-C``
         - ``Wait Until Entitlement Activated Count For Feature Matches    3  retry_duration=10    retry_count=12``
         - ``Wait Until Entitlement Activated Count For Feature Matches    2  feature=PRD-XIQ-PIL-S-C    retry_duration=60    retry_count=5``
         - ``Wait Until Entitlement Activated Count For Feature Matches    1  feature=PRD-XIQ-NAV-S-C    retry_duration=30    retry_count=10``
         - ``Wait Until Entitlement Activated Count For Feature Matches    1  feature=PRD-XIQ-NAC-S      retry_duration=15    retry_count=8``

        :param expected: expected number of activated licenses for specified license entitlement feature
        :param feature: type of license entitlement to check the activated count of (e.g., PRD-XIQ-PIL-S-C, PRD-XIQ-NAV-S-C, PRD-XIQ-NAC-S)
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if activated count for feature matches within time, else -1
        """

        activated_count = 0
        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Available Count Check for feature {feature} - Loop: {count}")

            # Navigate away from and back to page to force a refresh of the data
            self.navigator.navigate_to_devices()
            self.navigator.navigate_to_license_management()

            # Check the activated count for the specified feature
            activated_count = self.get_entitlement_activated_count_for_feature(feature)
            if activated_count == int(expected):
                self.utils.print_info(f"Activated count for {feature} is at expected value {expected}")
                return 1
            else:
                self.utils.print_info(f"Activated count for {feature} is {activated_count}, not expected value {expected}. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        self.utils.print_info(f"Activated count for {feature} is {activated_count}, not expected value {expected}. Please check.")
        self.screen.save_screen_shot()
        sleep(2)

        return -1

    def wait_until_entitlements_table_empty(self, retry_duration=30, retry_count=30):
        """
        - This keyword is used to wait until the Entitlements table is empty.
        -
        - Keyword Usage:
         - ``Wait Until Entitlements Table Empty``
         - ``Wait Until Entitlements Table Empty    retry_duration=10    retry_count=12``
         - ``Wait Until Entitlements Table Empty    retry_duration=60``
         - ``Wait Until Entitlements Table Empty    retry_count=10``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if Entitlements table is empty within time, else -1
        """

        device_count = 0
        count = 1

        while count <= retry_count:
            self.utils.print_info(f"Check for Empty Entitlements Table - Loop: {count}")

            # Navigate away from and back to page to force a refresh of the data
            self.navigator.navigate_to_devices()
            self.navigator.navigate_to_license_management()

            # Check if the Entitlements table is empty yet
            if self.is_entitlements_table_empty() == 1:
                self.utils.print_info("Entitlements table is empty")
                return 1
            else:
                self.utils.print_info(f"Entitlements table is not empty. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        self.utils.print_info("Entitlements table did not become empty within specified time. Please check.")
        self.screen.save_screen_shot()
        sleep(2)

        return -1
