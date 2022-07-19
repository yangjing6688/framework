from extauto.xiq.flows.manage.Devices import *
from extauto.xiq.flows.common.Navigator import *
from extauto.xiq.elements.AutoprovisionWebElements import *
from extauto.common.CommonValidation import CommonValidation


class AutoProvisioning:
    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.devices = Devices()
        self.app_web_elements = AutoprovisionWebElements()
        self.screen = Screen()
        self.common_validation = CommonValidation()

    def auto_provision_basic_settings(self, policy_name, country_code=None, **auto_provision_profile):
        """
        - This keyword creates auto provision basic settings
        - Keyword Usage:
         - ``Auto Provision Basic Settings    ${APP_POLICY_NAME}    ${AP_COUNTRY}    &{APP_CONFIG_DICTIONARY}``

        :param policy_name: app policy name
        :param country_code: country code
        :param auto_provision_profile: policy_name, device_function, device_model, service_tags, ip sub networks,
        - network_policy,country_code

        :return: 1 if success else -1
        """
        self.navigator.navigate_to_auto_provision()
        sleep(5)

        self.utils.print_info("Clicking on add button")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_add_button())

        device_function = auto_provision_profile.get('device_function')
        dev_model = auto_provision_profile.get('device_model')
        network_policy = auto_provision_profile.get('network_policy')

        self.utils.print_info("Entering Auto Provisioning policy name: ", policy_name)
        self.auto_actions.send_keys(self.app_web_elements.get_auto_provisioning_name(), policy_name)

        self.utils.print_info("Selecting Device Function: ", device_function)
        self.choose_auto_provision_device_function(device_function)
        sleep(3)

        self.utils.print_info("Selecting Device Function: ", device_function)
        self.choose_auto_provision_device_model(dev_model, device_function)
        sleep(3)

        self.utils.print_info("Selecting Network Policy: ", network_policy)
        self.choose_auto_provision_network_policy(network_policy)
        sleep(3)

        self.auto_actions.scroll_down()
        sleep(3)

        if "AP" in device_function:
            # country_code = auto_provision_profile.get('country_code')
            if self.choose_auto_provision_country_code(country_code):
                sleep(3)
                self.screen.save_screen_shot()
                return 1
            else:
                self.utils.print_info("Unable to select country code for AP model")
                return -1
        else:
            self.screen.save_screen_shot()
            return 1

    def auto_provision_advanced_settings(self, **advance_setting):
        """
        - This keyword creates auto provision advanced settings
        - Keyword Usage:
         - ``Auto Provision Advanced Settings   &{APP_CONFIG_DICTIONARY}``

        :param: upload_firmware,upload_configuration,reboot,Firmware_version
        :return: None
        """

        reboot = advance_setting.get('reboot')
        upload_firmware = advance_setting.get('upload_firmware')
        upload_configuration = advance_setting.get('upload_configuration')
        firmware_version = advance_setting.get('Firmware_version')

        self.auto_actions.scroll_down()
        self.utils.print_info("scroll down")

        if reboot == "Enable":
            self.utils.print_info("Enabling Reboot After Uploading")
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_enable_Reboot())

        if upload_firmware == "Enable":
            self.utils.print_info("Enabling Upload Device Firmware")
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_enable_upload_auth())
            sleep(3)
            if firmware_version == "golden_version":
                self.auto_actions.click(self.app_web_elements.get_auto_provisioning_Upload_Auth_golden_version())
            else:
                self.auto_actions.click(self.app_web_elements.get_auto_provisioning_Upload_Auth_latest_version())

        if upload_configuration == "Enable":
            self.utils.print_info("Enabling Upload Configuration Automatically")
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_enable_Upload_Auto())
            sleep(3)
            self.screen.save_screen_shot()

    def auto_provision_device_credential(self, **device_credential):
        """
        - This keyword adds auto provision device credentials if status is enabled on device_credential dictionary
        - Keyword Usage:
         - ``Auto Provision Device Credential  &{DEVICE_CREDENTIAL_DICTIONARY}``

        :param: device credentials dict : device_credential,root_admin_name,root_admin_password,read_only_admin_name,
                read_only_admin_password
        :return: None
        """
        device_credential_val = device_credential.get('device_credential')
        root_admin_name = device_credential.get('root_admin_name')
        root_admin_password = device_credential.get('root_admin_password')
        read_only_admin_name = device_credential.get('read_only_admin_name')
        read_only_admin_password = device_credential.get('read_only_admin_password')

        if device_credential_val == "Enable":
            self.utils.print_info("Enabling Device Credential")
            sleep(2)
            self.auto_actions.send_keys(
                self.app_web_elements.get_app_device_credential_root_admin_name(), root_admin_name)
            self.auto_actions.send_keys(
                self.app_web_elements.get_app_device_credential_root_admin_password(), root_admin_password)
            self.auto_actions.send_keys(
                self.app_web_elements.get_app_device_credential_readonly_admin_name(), read_only_admin_name)
            self.auto_actions.send_keys(
                self.app_web_elements.get_app_device_credential_readonly_admin_password(), read_only_admin_password)

    def auto_provision_capwap_configurations(self, **capwap_configuration):
        """
        - This keyword creates auto provision CAPWAP configuration
        - Keyword Usage:
         - ``Auto Provision capwap configurations &{CAPWAP_CONFIGURATION_DICTIONARY}``

        :param: capwap_configuration: CAPWAP configuration values
        :return: None
        """
        primary_capwap = capwap_configuration.get('primary_CAPWAP')
        capwap_credential = capwap_configuration.get('CAPWAP_credential')
        primary_hostname = capwap_configuration.get('primary_hostname')
        primary_name = capwap_configuration.get('primary_name')
        primary_ip_addr = capwap_configuration.get('primary_ip_addr')

        if capwap_credential == "Enable":
            self.utils.print_info("Enabling CAPWAP Configurations")
            sleep(2)
            if primary_capwap == "default":

                if primary_hostname == "default":
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_ip_addr())
                    sleep(3)
                    self.auto_actions.send_keys(
                        self.app_web_elements.get_app_capwap_add_ip_name(), primary_name)
                    self.auto_actions.send_keys(
                        self.app_web_elements.get_app_capwap_add_ip_IPaddr(), primary_ip_addr)
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_save_button())
                    sleep(2)
                else:
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_hostname())
                    sleep(3)
                    self.auto_actions.send_keys(
                        self.app_web_elements.get_app_capwap_add_hostname_name(), primary_name)
                    self.auto_actions.send_keys(
                        self.app_web_elements.get_app_capwap_add_hostname_hostname(), primary_hostname)
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_save_button())
                    sleep(2)
            else:
                self.auto_actions.send_keys(self.app_web_elements.get_app_capwap_primary_server_input(), primary_capwap)

            backup_name = capwap_configuration.get('backup_name')
            backup_ip_addr = capwap_configuration.get('backup_ip_addr')
            backup_hostname = capwap_configuration.get('backup_hostname')
            backup_capwap  = capwap_configuration.get('backup_CAPWAP')
            passphrase = capwap_configuration.get('passphrase')
            if backup_capwap == "default":

                if backup_hostname == "default":

                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_ip_addr())
                    sleep(5)
                    self.auto_actions.send_keys(self.app_web_elements.get_app_capwap_add_ip_name(), backup_name)
                    self.auto_actions.send_keys(self.app_web_elements.get_app_capwap_add_ip_IPaddr(), backup_ip_addr)
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_save_button())
                    sleep(2)
                else:
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_hostname())
                    sleep(5)
                    self.auto_actions.send_keys(self.app_web_elements.get_app_capwap_add_hostname_name(), backup_name)
                    self.auto_actions.send_keys(
                        self.app_web_elements.get_app_capwap_add_hostname_hostname(), backup_hostname)
                    self.auto_actions.click(self.app_web_elements.get_app_capwap_add_save_button())
                    sleep(2)
            else:
                self.auto_actions.send_keys(self.app_web_elements.get_app_capwap_primary_server_input(), backup_capwap)

            if passphrase != "default":
                self.auto_actions.send_keys(self.app_web_elements.get_app_capwap_shared_key_passphrase(), passphrase)

    def save_and_enable_auto_provision_policy(self, policy_name):
        """
        - This keyword saves and enables auto provision profile
        - Keyword Usage:
         - ``Save and Enable Auto Provision Policy   ${APP_POLICY_NAME}``

        :param: policy_name : auto provision policy name
        :return: None
        """
        # policy_name = autoprov_profile.get('policy_name')

        self.utils.print_info("Clicking On Save Button")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_save_button())
        self.screen.save_screen_shot()
        sleep(5)
        self.auto_provision_enable_policy_row(policy_name)
        self.screen.save_screen_shot()

    def auto_provision_enable_policy_row(self, policy_name):
        """
        - Enables a auto provision policy
        - Keyword Usage:
         - ``Auto Provision Enable Policy Row   ${APP_POLICY_NAME}``

        :param: auto provision policy name which is to be searched
        :return: None
        """
        self.utils.print_info("Enabling Policy: ", policy_name)
        for row in self.app_web_elements.get_auto_provision_grid_rows():
            if policy_name in row.text:
                self.auto_actions.click(self.app_web_elements.get_auto_provision_enable(row))
                sleep(2)
                self.screen.save_screen_shot()
                return

    def choose_auto_provision_network_policy(self, network_policy):
        """
        - This keyword chooses auto provision network policy
        - Keyword Usage
         - ``Choose Auto Provision Network Policy   ${NETWORK_POLICY_NAME}``

        :param: network policy : Network Policy Name to be apply for autoprovision policy
        :return: None
        """
        sleep(3)
        self.utils.print_info("Clicking on Network Policy")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_network_policy())
        sleep(5)
        net_results = self.app_web_elements.get_auto_provisioning_network_policy_list()
        for net_result in net_results:
            val = net_result.text
            if val == network_policy:
                self.utils.print_info("Network Policy Match Found")
                self.auto_actions.click(net_result)
                self.screen.save_screen_shot()
                break

    def verify_auto_provision_policy_update(self, serial, country_code='NA', **auto_provision_policy):
        """
        - This keyword verifies if the device is updated with auto configuration policy
        - Keyword Usage
         - ``verify auto provision_policy_update   ${NETWORK_POLICY_NAME}``

        :param: serial : serial number of device
        :param: auto_provision_policy: (Config Dict) device_function(AP or Switch), network_policy_name
        :return: 1 Auto Provision Policy Update Successful else -1
        """
        device_function = auto_provision_policy.get('device_function')
        # country_code = auto_provision_policy.get('country_code')
        network_policy = auto_provision_policy.get('network_policy')

        self.devices.refresh_devices_page()
        sleep(3)

        row = self.devices.get_manage_device_row(serial)
        self.utils.print_info("RoW Data: ", self.devices.format_row(row.text))

        self.utils.print_info("Verifying Network Policy: ", network_policy)

        if "AP" in device_function:
            self.utils.print_info("Verifying device type AP")
            #if network_policy in row.text and country_code in row.text:
            if network_policy in row.text:
                self.screen.save_screen_shot()
                return 1
            else:
                self.screen.save_screen_shot()
                return -1

        if "Extreme Networks SR22xx / SR23xx Switches" in device_function:
            self.utils.print_info("Verifying device type Switch")
            if network_policy in row.text:
                self.screen.save_screen_shot()
                return 1
            else:
                self.screen.save_screen_shot()
                return -1

    def enter_auto_provision_policy_name(self, policy_name):
        """
        - This keyword uses to configure Auto Provisioning Policy Name
        - Keyword Usage
         - ``Enter Auto Provision Policy Name   ${APP_NAME}``

        :param: policy_name : Auto Provisioning Policy Name
        :return: None
        """
        sleep(3)
        self.utils.print_info("Entering Name")
        self.auto_actions.send_keys(self.app_web_elements.get_auto_provisioning_name(), policy_name)

    def choose_auto_provision_device_function(self, device_function):
        """
        - This keyword chooses auto provision device function
        - Keyword Usage
         - ``Choose Auto Provision Device Function   ${DEVICE_FUNCTION}``

        :param: device_function : device function to be selected
        :return: 1 if Device Function Selected Successfully else -1
        """
        sleep(3)
        self.utils.print_info("Clicking on Device Function drop down")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_device_function())
        results = self.app_web_elements.get_auto_provisioning_device_function_list()
        if results:
            for result in results:
                if device_function in result.text:
                    self.utils.print_info("Device Function Match Found")
                    self.auto_actions.click(result)
                    self.screen.save_screen_shot()
                    return 1
        else:
            self.utils.print_info(f" Not able to find auto provision device function dropdown items ")
            self.screen.save_screen_shot()
            return -1

    def choose_auto_provision_device_model(self, dev_model, device_function):
        """
        - This keyword chooses auto provision device model
        - Keyword Usage
         - ``Choose Auto Provision Device Model   ${DEVICE_PLATFORM}   ${DEVICE_FUNCTION}``

        :param: device model : Device Platform
        :param: device function : Device Function Name ie AP,Switches
        :return:None
        """
        sleep(3)
        self.utils.print_info("Clicking on Device Model")
        if device_function == "AP":
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_device_model())
        elif device_function == "Extreme Networks SR22xx / SR23xx Switches":
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_device_model_dropdown_switch_SR22_23())
        elif device_function == "Extreme Networks SR20xx / SR21xx Switches":
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_device_model_dropdown_switch_SR20_21())
        else:
            self.auto_actions.click(self.app_web_elements.get_auto_provisioning_device_model_dropdown_switch_dell())
        sleep(3)

        results = self.app_web_elements.get_auto_provisioning_device_model_dropdown_list()
        if results:
            for result in results:
                val = result.text
                if val == dev_model:
                    self.utils.print_info("Device Model Match Found")
                    self.auto_actions.click(result)
                    self.screen.save_screen_shot()
                    break
        else:
            self.utils.print_info(f" Not able to find auto provision device model dropdown items ")
            return -1

    def choose_auto_provision_country_code(self, country_code):
        """
        - This keyword chooses auto provision country
        - Keyword Usage
         - ``Choose Auto Provision Country Code   ${COUNTRY_CODE}``
        :param: country_code : Country Code to Configure for Auto Provisioning Policy
        :return: 1 if Country Code Successfully configured else -1
        """
        self.utils.print_info("Clicking on Country Code dropdown")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_country_code())
        self.screen.save_screen_shot()
        sleep(5)

        countries = self.app_web_elements.get_auto_provisioning_country_code_list()
        if countries:
            for country in countries:
                self.utils.print_debug("country: ", country.text)
                if country_code in country.text:
                    self.auto_actions.click(country)
                    self.utils.print_info("Selected country: ", country_code)
                    self.screen.save_screen_shot()
                    return 1
        else:
            self.utils.print_info(f" Not able to find auto provision country dropdown items ")
            self.screen.save_screen_shot()
            return -1

    def delete_auto_provisioning_policy(self, policy_name):
        """
        - Delete a Auto Provisioning Policy
        - Keyword Usage
         - ``Delete Auto Provisioning Policy   ${APP_NAME}``

        :param policy_name: Auto Provisioning policy Name
        :return: 1 if successfully deleted Auto Provisioning Policy else -1
        """
        self.navigator.navigate_to_auto_provision()
        sleep(3)

        self.utils.print_info("Deleting Auto Provisioning Policy: ", policy_name)
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_button())
        sleep(2)

        if self.search_auto_provisioning_policy(policy_name) == 1:
            for row in self.app_web_elements.get_auto_provision_grid_rows():
                if policy_name in row.text:
                    self.utils.print_info("Selecting Policy row checkbox")
                    self.auto_actions.click(self.app_web_elements.get_auto_provisioning_check_box(row))
                    sleep(2)

                    self.utils.print_info("Clicking Delete button...")
                    self.auto_actions.click(self.app_web_elements.get_auto_provisioning_delete_button())
                    sleep(2)

                    self.utils.print_info("Confirming delete")
                    self.auto_actions.click(self.app_web_elements.get_auto_provisioning_alert_yes())
                    self.utils.print_info("Deleted Auto Provisioning Policy: ", policy_name)
                    return 1
        else:
            self.utils.print_info("Unable to delete Auto Provisioning Policy: ", policy_name)
            return -1

    def delete_all_auto_provision_policies(self, **kwargs):
        """
        - Delete all Auto Provisioning Policies
        - Keyword Usage
         - ``Delete All Auto Provision Policies``

        :return: 1 if successfully deleted All Auto Provisioning Policies else -1
        """

        self.navigator.navigate_to_auto_provision()
        sleep(3)

        cur_count = self.get_auto_provision_policy_count()
        if cur_count == 0:
            kwargs['pass_msg'] = "No Auto Provision Policy is present"
            self.common_validation.validate(1, 1, **kwargs)
            return 1

        header = self.app_web_elements.get_auto_provisioning_grid_header()
        self.utils.print_info("Selecting all Policies")

        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_select_all_check_box())
        sleep(2)

        self.utils.print_info("Clicking Delete button...")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_delete_button())
        sleep(2)

        self.utils.print_info("Confirming delete")
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_alert_yes())
        sleep(5)

        new_count = self.get_auto_provision_policy_count()
        if new_count == 0:
            kwargs['pass_msg'] = "Successfully Deleted all the Policies"
            self.common_validation.validate(1, 1, **kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to Deleted all the Policies"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1

    def search_auto_provisioning_policy(self, policy_name):
        """
        - Search a Auto Provisioning Policy
        - Keyword Usage
         - ``Search Auto Provisioning Policy   ${APP_NAME}``

        :param policy_name: Auto Provision Policy
        :return: 1 if Auto Provision Policy found On Grid else -1
        """
        self.navigator.navigate_configure_common_objects()
        sleep(3)

        self.utils.print_info("Searching Auto Provisioning Policy: ", policy_name)
        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_button())
        sleep(2)
        rows = self.app_web_elements.get_auto_provision_grid_rows()
        self.utils.print_info("Rows: ", rows)

        if rows:
            for row in rows:
                if policy_name in row.text:
                    self.utils.print_info("Found Auto Provisioning Policy: ", policy_name)
                    self.screen.save_screen_shot()
                    return 1

        self.utils.print_info("Unable to find Auto Provisioning Policy: ", policy_name)
        self.screen.save_screen_shot()

        return -1

    def goto_auto_provisioning_policy(self):
        """
        - navigates to auto provisioning policy page
        - Keyword Usage
         - ``Goto Auto Provisioning Policy``

        :return: 1 if Navigate to Auto Provisioning Policy Successful else None
        """
        self.navigator.navigate_configure_common_objects()
        sleep(3)

        self.auto_actions.click(self.app_web_elements.get_auto_provisioning_button())
        sleep(2)
        return 1

    def get_auto_provision_policy_count(self):
        """
        - Returns the count of auto provision policies
        - Keyword Usage
         - ``Get Auto Provision Policy Count``

        :return: number of auto provision policies
        """
        rows = self.app_web_elements.get_auto_provision_grid_rows()
        if rows:
            rows_count = len(rows)
            self.utils.print_info("Number of Auto Provisioning Policies: ", rows_count)
            return rows_count
        else:
            self.utils.print_info("Number of Auto Provisioning Policies: 0")
            return 0
