import re
from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from robot.libraries.BuiltIn import BuiltIn
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.GlobalSettingWebElements import GlobalSettingWebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.xapi.globalsettings.XapiGlobalSettings import XapiGlobalSettings


class GlobalSetting(GlobalSettingWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.navigate = Navigator()
        self.builtin = BuiltIn()
        self.devices_web_elements = DevicesWebElements()
        self.common_validation = CommonValidation()
        self.xapiGlobalSettings = XapiGlobalSettings()

    def get_authentication_logs_row(self, search_string):
        """
        - Get the Authentication Logs from Global Settings Page
        - Flow : User account image-->Global Settings--> Authentication Logs
        - Keyword Usage
        - ``Get Authentication Logs Row   ${SEARCH_STRING}``

        :param search_string:  it should be anything which is searched on the row cell
                               example search_string be like user_name, auth_type,client etc
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting authentication logs rows")
        sleep(5)
        rows = self.get_authentication_logs_grid_rows()
        if not rows:
            self.utils.print_info("Authentication Logs rows are not available in the page")
            return False
        try:
            for row in rows:
                row_text = row.text.lower()
                row_inner_text = row.get_attribute("innerText").lower()
                search_string_lower = search_string.lower()
                self.utils.print_info(f"Authentication Logs row text: {row_text} / {row_inner_text} = {search_string}")
                if search_string_lower in row_text or search_string_lower in row_inner_text:
                    self.utils.print_info("Authentication Logs row found")
                    return row
        except Exception as e:
            self.utils.print_error("Exception when getting the row element: %s\n" % e)
            raise e


    def get_accounting_logs_row(self, search_string):
        """
        - Get the Accounting Logs from Global Settings Page
        - Flow : User account image-->Global Settings--> Accounting Logs
        - Keyword Usage
        - ``Get Accounting Logs Row   ${SEARCH_STRING}``

        :param search_string: it should be anything which is searched on the row cell
                              example search_string be like user_name, auth_type,client etc
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting Accounting logs rows")
        rows = self.get_authentication_logs_grid_rows()
        if not rows:
            self.utils.print_info("Accounting Logs rows are not available in the page")
            return False
        for row in rows:
            if search_string in row.text:
                return row

    def get_authentication_logs_details(self, search_string, search_filter=None, **kwargs):
        """
        - Filter the logs based on the Filter arguments Allowed Filters are: Client or user name
        - Gets all authentication details from the row will try up to ten minutes to get the correct row
        - Flow : User account image-->Global Settings--> Authentication Logs
        - Keyword Usage
        - ``Get Authentication Logs Details   ${SEARCH_STRING}    ${SEARCH_FILTER``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param search_string:  row search
        :param search_filter:  filter string - i.e client mac or user name
        :return: authentication details dict
        """

        row_data = None
        max_time = 600
        counter = 0
        if self.xapiGlobalSettings.is_xapi_enabled(**kwargs):
            while(row_data is None or counter > max_time):
                row_data = self.xapiGlobalSettings.xapi_get_authentication_logs_details(search_string=search_string, search_filter=search_filter, **kwargs)
                if row_data is not None:
                    return row_data
                else:
                    self.utils.print_info("Row data is None, retrying...")
                    counter += 1
                    sleep(1)
            return row_data



        while (row_data is None or counter > max_time):
            self.utils.print_info("Navigate to Global Settings-->Authentication Logs")
            self.navigate.navigate_to_authentication_logs()
            sleep(5)
            if close_icon := self.get_authentication_logs_unknown_error_close_icon():
                if close_icon.is_displayed():
                    self.utils.print_info("Click close icon")
                    self.auto_actions.click_reference(self.get_authentication_logs_unknown_error_close_icon)
                    sleep(2)

            if search_filter:
                self.utils.print_info("Search grid based on search_filter in Auth logs")
                self.utils.print_info("Entering search_string  ", search_filter)
                self.auto_actions.send_keys(self.get_authentication_logs_search_text_field(),
                                            search_filter)
                self.screen.save_screen_shot()
                sleep(2)


            if view_log := self.get_authentication_logs_view_all_pages_button():
                if view_log.is_displayed():
                    self.utils.print_info("Click Full pages button")
                    self.auto_actions.click_reference(self.get_authentication_logs_view_all_pages_button)
                    sleep(2)

            auth_logs_dict = {}
            auth_logs_row = self.get_authentication_logs_row(search_string)

            if auth_logs_row is not None:
                self.utils.print_info("Authentication Logs row found")
                break;
            else:
                counter += 1
                self.utils.print_info("Row data is None, retrying...")
                self.navigate.navigate_to_devices()
                sleep(60)

        self.screen.save_screen_shot()
        if auth_logs_row:
            cells = self.get_authentication_logs_row_cells(auth_logs_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]

                    if label == 'reply':
                        auth_cell = self.get_authentication_logs_auth_status_cell(cell)
                        auth_logs_dict[label] = auth_cell.get_attribute("class").split()[-1]
                        self.screen.save_screen_shot()
                    else:
                        auth_logs_dict[label] = cell.text
            self.utils.print_info("******************Authentication log details************************")
            for key, value in auth_logs_dict.items():
                self.utils.print_info(f"{key}:{value}")
        # else:
        #     self.utils.print_info("No logs found.. Sleep for 60secs and checking again..")
        #     sleep(60)
        #     self.navigate.navigate_to_devices()
        #     self.navigate.navigate_to_authentication_logs()
        #     self.auto_actions.send_keys(self.get_authentication_logs_search_text_field(),
        #                                 search_filter)
        #     sleep(2)
        #     auth_logs_row = self.get_authentication_logs_row(search_string)
        #     self.screen.save_screen_shot()
        #
        #     if auth_logs_row:
        #         cells = self.get_authentication_logs_row_cells(auth_logs_row)
        #         for cell in cells:
        #             if re.search(r'field-\w*', cell.get_attribute("class")):
        #                 label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
        #
        #                 if label == 'reply':
        #                     auth_cell = self.get_authentication_logs_auth_status_cell(cell)
        #                     auth_logs_dict[label] = auth_cell.get_attribute("class").split()[-1]
        #                     self.screen.save_screen_shot()
        #                 else:
        #                     auth_logs_dict[label] = cell.text
        #         self.utils.print_info("******************Authentication log details************************")
        #         for key, value in auth_logs_dict.items():
        #             self.utils.print_info(f"{key}:{value}")

        return auth_logs_dict

    def get_authentication_logs_username(self, search_string):
        """
        - Get the username Field on authentication Logs grid
        - Flow : User account image-->Global Settings--> Authentication Logs
        - Keyword Usage
        - ``Get Authentication Logs Username   ${SEARCH_STRING}``

        :param search_string: Row Search String i.e client mac or user name
        :return: Authentication Logs User Name Field Text
        """
        device_details = self.get_authentication_logs_details(search_string)
        if device_details:
            return device_details['userName']

    def get_authentication_logs_ssid(self, search_string):
        """
        - Get the ssid Field on authentication Logs grid
        - Keyword Usage
        - ``Get Authentication Logs SSID   ${SEARCH_STRING}``

        :param search_string: Row Search String i.e client mac or user name
        :return: Authentication Logs SSID Field Text
        """
        device_details = self.get_authentication_logs_details(search_string)
        if device_details:
            return device_details['ssid']

    def get_authentication_logs_auth_method(self, search_string):
        """
        - Get the Authentication method Field on authentication Logs grid
        - Flow : User account image-->Global Settings--> Authentication Logs
        - Keyword Usage
        - ``Get Authentication Logs Auth Method   ${SEARCH_STRING}``

        :param search_string: Row Search String i.e client mac or user name
        :return: Authentication Logs Authentication Method Field Text
        """
        device_details = self.get_authentication_logs_details(search_string)
        if device_details:
            return device_details['authType']

    def get_authentication_logs_client_detail(self, search_string):
        """
        - Get the Client Details on authentication Logs grid
        - Keyword Usage
        - ``Get Authentication Logs Client Detail   ${SEARCH_STRING}``

        :param search_string: Row Search String i.e client mac or user name
        :return: Authentication Logs callingStationId Field Text
        """
        device_details = self.get_authentication_logs_details(search_string)
        if device_details:
            return device_details['callingStationId']

    def get_authentication_logs_date(self, search_string):
        """
        - Get the date Field on authentication Logs grid
        - Flow : User account image-->Global Settings--> Authentication Logs
        - Keyword Usage
        - ``Get Authentication Logs Date   ${SEARCH_STRING}``

        :param search_string: Row Search String i.e client mac or user name
        :return: Authentication Logs AuthDate Field Text
        """
        device_details = self.get_authentication_logs_details(search_string)
        if device_details:
            return device_details['authdate']

    def create_organization(self, organization_name, colour_name="Default", **kwargs):
        """
        - This Keyword Uses To Create Organization
        - Flow : User account image-->Global Settings--> Organization
        - Keyword Usage
        - ``Create Organization   ${ORGANIZATION_NAME}  ${ORGANIZATION_COLOUR}``

        :param organization_name: Name of the Organization
        :param colour_name: Organization Colour
        :return: 1 If Organization Created Successfully else None
        """
        self.utils.print_info("Navigating to the global settings--->organization")
        self.navigate.navigate_to_accounts_organization_page()

        self.utils.print_info("Click Add button")
        self.auto_actions.click_reference(self.get_global_settings_account_organizations_add_button)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering Organization name: ", organization_name)
        self.auto_actions.send_keys(self.get_global_settings_account_organization_name_inputfield(), organization_name)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click colour scroll down box")
        self.auto_actions.click_reference(self.get_organization_drop_down_button)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Select Colour for Organization")
        org_colour_items = self.get_organization_drop_down_items()
        for item in org_colour_items:
            if colour_name.upper() in item.text.upper():
                self.utils.print_info("Selecting Colour from drop down")
                self.auto_actions.click(item)
                self.screen.save_screen_shot()
                sleep(2)
                break

        self.utils.print_info("Click Add button")
        self.auto_actions.click_reference(self.get_global_settings_account_organizations_save_button)
        kwargs['pass_msg'] = "Successfully created organization"
        self.common_validation.passed(**kwargs)
        return 1

    def search_organization_name(self, organization_name, **kwargs):
        """
        - Search the Organization Name From Global Settings Page
        - Flow : User account image-->Global Settings--> Organization
        - Keyword Usage
        - ``Search Organization Name   ${ORGANIZATION_NAME}``

        :param  organization_name: Name of the Organization
        :return: 1 If Organization found on Grid else -1
        """
        self.utils.print_info("Navigating to the global settings--->organization")
        self.navigate.navigate_to_accounts_organization_page()
        self.screen.save_screen_shot()

        sleep(5)
        self.utils.print_info("Getting organization rows")
        rows = self.get_organization_grid_rows()
        sleep(5)

        if not rows:
            self.utils.print_info("organization name rows are not available in the page")
            return False
        else:
            self.utils.print_info("Organization Name rows found")

        sleep(5)
        for row in rows:
            if row.is_displayed():
                self.utils.print_info("ROW: ", row.text)
                cell = self.get_organization_grid_rows_cells(row)
                if not cell:
                    pass
                if organization_name in cell.text:
                    self.utils.print_info("'search_organization_name()' -> organization name found in the page")
                    return 1
                else:
                    self.utils.print_info("'search_organization_name()' -> organization name not found in the page")
                    return -1
        self.utils.print_info("'search_organization_name()' -> Organization not found on Grid")
        return -1

    def enable_account_hiq(self, **kwargs):
        """
        - Enable MSP Feature in the Account
        - Flow : User account image-->Global Settings--> Account Details--> Enable HIQ Button
        - Keyword Usage
        - ``Enable Account HIQ``

        :return: 1 If HIQ Enabled Successfully in the Account else -1
        """
        self.utils.print_info("Navigating to the global settings--->Account details")
        self.navigate.navigate_to_account_details_page()

        self.utils.print_info("Enable HIQ")
        hiq_status = self.get_global_settings_account_enable_hiq_status()
        self.utils.print_info("HIQ button Disabled Status:", hiq_status)

        if str(hiq_status) == "False":
            self.utils.print_info("Click Enabling HIQ button")
            self.auto_actions.click_reference(self.get_global_settings_account_enable_hiq_button)
            sleep(2)

            self.utils.print_info("Click Enabling HIQ confirm button")
            self.auto_actions.click_reference(self.get_global_settings_account_enable_hiq_confirm_button)
            sleep(2)

            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info("Tooltip Text After enabling HIQ:", tool_tp_text)

            if "The process has been started. You will be logged out momentarily." in tool_tp_text:
                kwargs['pass_msg'] = "Automatic Logout Happening on Account after enabling HIQ"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Automatic Logout Not Happening on Account after enabling HIQ"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['pass_msg'] = "HIQ Feature Already Enabled in the Account"
            self.common_validation.passed(**kwargs)
            return 1

    def get_accounting_logs_details(self, search_string, search_filter=None):
        """
        - Filter the logs based on the Filter arguments Allowed Filters are: Client or user name
        - Get accounts detailed logs from the row
        - Flow : User account image-->Global Settings--> Accounting Logs
        - Keyword Usage:
        - ``Get Accounting Logs Details   ${SEARCH_STRING}   ${SEARCH_FILTER}``

        :param search_filter: String to filter the accounting log rows
        :param search_string: String to search the row
        :return: Accounting Logs dict
        """
        self.utils.print_info("Navigate to Global Settings-->Accounting Logs")
        self.navigate.navigate_to_accounting_logs()
        sleep(5)

        if close_icon := self.get_authentication_logs_unknown_error_close_icon():
            if close_icon.is_displayed():
                self.utils.print_info("Click close icon")
                self.auto_actions.click_reference(self.get_authentication_logs_unknown_error_close_icon)
                sleep(2)

        if search_filter:
            self.utils.print_info("Search grid based on search_filter in Accounting logs")
            self.utils.print_info("Entering search_string  ", search_filter)
            self.auto_actions.send_keys(self.get_authentication_logs_search_text_field(), search_filter)
            self.screen.save_screen_shot()
            sleep(2)

        if view_log := self.get_authentication_logs_view_all_pages_button():
            if view_log.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.get_authentication_logs_view_all_pages_button)
                sleep(2)

        acct_logs_dict = {}
        acct_logs_row = self.get_accounting_logs_row(search_string)
        if acct_logs_row:
            cells = self.get_authentication_logs_row_cells(acct_logs_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    if label == 'reply':
                        auth_cell = self.get_authentication_logs_auth_status_cell(cell)
                        acct_logs_dict[label] = auth_cell.get_attribute("class").split()[-1]
                        self.screen.save_screen_shot()
                    else:
                        acct_logs_dict[label] = cell.text

            self.utils.print_info("******************accounting log details************************")
            for key, value in acct_logs_dict.items():
                self.utils.print_info(f"{key}:{value}")

            return acct_logs_dict

    def change_device_password(self, password, **kwargs):
        """
        - Change the Device Password String on Global Settings-->Device Management Page.
        - Flow : User account image-->Global Settings--> Device Management Settings
        - Keyword Usage:
        - ``Change Device password   ${LANGUAGE}``

        :param password: Password String
        :return: 1 if XIQ Account Language Changed Successfully else -1
        """
        try:
            self.navigate.navigate_to_global_settings_page()
            sleep(5)

            self.utils.print_info("Selecting Device Management Settings...")
            self.auto_actions.click_reference(self.get_device_management_settings_menu)
            sleep(5)

            self.utils.print_info("Entering password")
            self.auto_actions.send_keys(self.get_device_management_settings_password(), password)
            sleep(1)

            self.utils.print_info("Confirming password")
            self.auto_actions.send_keys(self.get_device_management_settings_password_confirm(), password)
            sleep(1)

            self.utils.print_info("Clicking Show Password checkbox...")
            self.auto_actions.click_reference(self.get_device_management_settings_show_password_checkbox)
            sleep(1)

            self.screen.save_screen_shot()
            self.utils.print_info("Saving the changes...")
            self.auto_actions.click_reference(self.get_device_management_settings_save_button)
            sleep(5)
            kwargs['pass_msg'] = "XIQ Account Password Changed Successfully"
            self.common_validation.passed(**kwargs)
            return 1
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "unsuccessfully Changed XIQ Account Language  "
            self.common_validation.fault(**kwargs)
            return -1

    def change_xiq_account_language(self, language, **kwargs):
        """
        - Change the language of the account
        - Flow : User account image-->Global Settings--> Account Details--> Select Language-->Apply
        - Keyword Usage:
        - ``Change Xiq Account Language   ${LANGUAGE}``

        :param language: Language Name ie English
        :return: 1 if XIQ Account Language Changed Successfully else -1
        """
        self.utils.print_info("Navigating to the global settings--->Account details")
        self.navigate.navigate_to_account_details_page()

        self.utils.print_info("Click on the select language drop down")
        self.auto_actions.click_reference(self.get_account_select_language_drop_down)
        sleep(2)

        self.utils.print_info("select the language")
        self.auto_actions.select_drop_down_options(self.get_account_select_language_drop_down_options(), language)

        self.utils.print_info("Click on the apply button")
        self.auto_actions.click_reference(self.get_account_language_apply_button)
        sleep(10)
        kwargs['pass_msg'] = "XIQ Account Language Changed Successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def change_xiq_account_time_zone(self, time_zone="(GMT) UTC", **kwargs):
        """
        - Change the time zone of the account
        - Flow : User account image-->Global Settings--> Account Details--> Select Time Zone-->Apply
        - Keyword Usage:
        - ``Change XIQ Account Time Zone   ${TIMEZONE}``

        :param time_zone: Time zone to select e.g., UTC, EST5EDT, etc
        :return: 1 if XIQ Account Time Zone was changed successfully, else -1
        """
        self.utils.print_info("Navigating to the global settings--->Account details")
        self.navigate.navigate_to_account_details_page()

        self.utils.print_info("Click on the Time Zone drop down")
        self.auto_actions.click_reference(self.get_account_time_zone_drop_down)
        sleep(2)

        self.utils.print_info("Select the time zone '" + time_zone + "'")
        options = self.get_account_time_zone_drop_down_options()
        self.auto_actions.select_drop_down_options(options, time_zone)

        self.utils.print_info("Click the apply button")
        self.auto_actions.click_reference(self.get_account_time_zone_apply_button)
        sleep(10)
        kwargs['pass_msg'] = "XIQ Account Time Zone Changed Successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def enable_ssh_availability(self, **kwargs):
        """
        - Enabling SSH availability in Global Settings Page
        - Flow : User account icon-->Global Settings--> VIQ Management
        - Keyword Usage
        - ``Enable SSH Availability``

        :return: 1 after successfully enabling SSH
        """

        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.utils.print_info("Now checking for SSH availability")
        self.screen.save_screen_shot()
        if not self.get_ssh_availability_option_status().is_selected():
            self.utils.print_info("Enabling SSH Availability..")
            self.auto_actions.click_reference(self.get_ssh_availability_option_status)
            sleep(1)
            self.screen.save_screen_shot()
        else:
            self.utils.print_info("SSH Availability Button already enabled...")
            sleep(2)
            self.screen.save_screen_shot()
        kwargs['pass_msg'] = "Successfully enabling ssh"
        self.common_validation.passed(**kwargs)
        return 1

    def disable_ssh_availability(self, **kwargs):
        """
        - Disabling SSH availability in Global Settings Page
        - Flow : User account icon-->Global Settings--> VIQ Management
        - Keyword Usage
        - ``Disable SSH Availability``

        :return: 1 after successfully disabling SSH
        """

        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.utils.print_info("Now checking for SSH availability")

        if self.get_ssh_availability_option_status().is_selected():
            self.utils.print_info("Disabling SSH Availability..")
            self.auto_actions.click_reference(self.get_ssh_availability_option_status)
            sleep(1)
            self.screen.save_screen_shot()
        else:
            self.utils.print_info("SSH Availability Button already disabled...")
            sleep(2)
            self.screen.save_screen_shot()
        kwargs['pass_msg'] = "Successfully disabling ssh"
        self.common_validation.passed(**kwargs)
        return 1

    def get_api_access_token_details(self, search_string):
        """
        - This key word is used to get the token details i.e access token, refresh token, expiry time
        - Flow:
        - Global Settings --> API Token Management
        - Keyword Usage:
        - ``Get API Access Token Details  ${SEARCH_STRING}``

        :param search_string: Search string is the access token generated from the curl command
        :return: access token row detail dict
        """
        access_token_dtls = {}
        self.navigate.navigate_to_api_token_mngment()
        sleep(20)  # this delay is required to load the API tokens rows

        self.screen.save_screen_shot()
        sleep(2)

        for row in self.get_api_access_token_rows():
            if search_string in row.text:
                cells = self.get_api_access_token_row_cells(row)
                access_token_dtls['Access Token'] = cells[3].text
                access_token_dtls['Expiration'] = cells[6].text
                access_token_dtls['Refresh Token'] = cells[7].text
                return access_token_dtls

        self.builtin.fail("Generated Access token is not present in API Token Management page")
        self.utils.print_info("Generated Access token is not present in API Token Management")
        return -1

    def delete_api_access_tokens(self):
        """
        - This keyword is used to delete the all generated access tokens
        - Flow: Global Settings --> API Token Management --> Select all rows --> Delete
        - Keyword Usage:
        - ``Delete Api Access Tokens```

        :return: None
        """
        self.navigate.navigate_to_api_token_mngment()
        sleep(20)  # this delay is required to load the API tokens rows

        self.utils.print_info("Select the all API Token rows")
        self.auto_actions.click_reference(self.get_api_access_tokens_select_check_box)

        sleep(2)
        self.utils.print_info("Click on API Access Tokens delete button")
        self.auto_actions.click_reference(self.get_api_access_tokens_delete_button)

        sleep(2)
        self.utils.print_info("clicking on confirm Yes button")
        self.auto_actions.click_reference(self.get_api_access_tokens_delete_cnfm_button)

        sleep(2)
        self.screen.save_screen_shot()

    def backup_viq_data(self):
        """
        - This Keyword will Backup the current VIQ Data
        - Flow : User account icon-->Global Settings--> VIQ Management ---> Backup Now
        - Keyword Usage:
        - `` Backup VIQ Data ``

        :return: 1 after successfully Backup the VIQ data else -1
        """
        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Backup Now Button")
        self.auto_actions.click_reference(self.get_viq_backup_now_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Backup Confirm Button")
        self.auto_actions.click_reference(self.get_viq_backup_confirm_button)
        sleep(2)
        self.screen.save_screen_shot()

        """
        x = datetime.datetime.now()
        approximate_backup_time1 = x + datetime.timedelta(0, 12)
        approximate_backup_time = approximate_backup_time1.strftime("%Y-%m-%d %H:%M")
        self.utils.print_info("Approximate Backup Time is:", approximate_backup_time)
        sleep(10)

        self.navigate.navigate_to_devices()
        sleep(2)

        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        last_backup_time = self.get_viq_last_backup_time_textfield().text
        self.utils.print_info("Last Backup Time is:", last_backup_time)

        self.screen.save_screen_shot()
        sleep(2)

        if approximate_backup_time in last_backup_time:
            self.utils.print_info("VIQ Backup Data Operation is Successfully Completed")
            return 1
        else:
            self.utils.print_info("VIQ Backup Data Operation is Not Successfully Completed")
            return -1
        """

        self.utils.print_info("BackUp VIQ operation is successful")
        return 1

    def reset_viq_data(self):
        """
        - This Keyword will Delete the VIQ Data
        - Flow : User account icon-->Global Settings--> VIQ Management ---> Reset VIQ
        - Keyword Usage:
        - `` Reset VIQ ``

        :return: 1 after successfully Resetting VIQ data else -1
        """
        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Reset VIQ Button")
        self.auto_actions.click_reference(self.get_viq_delete_data_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Reset VIQ Confirm Button")
        self.auto_actions.click_reference(self.get_reset_viq_confirm_button)
        sleep(2)
        self.screen.save_screen_shot()

        """
        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info("Tooltip Text After Doing Delete VIQ is:", tool_tp_text)

        if "The operation was successful." in tool_tp_text:
            self.utils.print_info("VIQ Delete Data Operation is Successfully Completed")
            return 1
        else:
            self.utils.print_info("VIQ Delete Data Operation is Not Successfully Completed")
            return -1
        """

        self.utils.print_info("Reset VIQ operation is successful")
        return 1

    def get_audit_logs_details(self, category, search_string, **kwargs):
        """
        - Get the audit log rows based on category and search_string provided
        - Flow : User account image-->Global Settings--> Audit Logs
        - Keyword Usage
        - ``Get Audit Logs Details   ${CATEGORY}    ${SEARCH_STRING}``

        :param category:  Category field(Eg: ADMIN, MONITORING)
        :param search_string:  Search string(Eg: Delete, Reset, Reboot)
        :return: 1 if search string found in logs else -1
        """
        self.utils.print_info("Navigate to Global Settings-->Audit Logs")
        self.navigate.navigate_to_audit_logs_menu()
        sleep(5)
        self.utils.print_info("Adding sleep for the audit logs to get updated")
        sleep(10)
        self.auto_actions.click_reference(self.get_audit_logs_view_all_pages_button)
        sleep(5)

        audit_logs_dict = {}
        audit_logs_row = self.get_audit_logs_row(category, search_string)
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Getting audit log Details...")
        if audit_logs_row:
            self.utils.print_info("audit_logs_row :", audit_logs_row)
            cells = self.get_authentication_logs_row_cells(audit_logs_row)
            for cell in cells:
                if re.search(r'field-\w*', cell.get_attribute("class")):
                    label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                    self.utils.print_debug("label : ", label)
                    self.utils.print_debug("cell.text : ", cell.text)
                    audit_logs_dict[label] = cell.text
            self.utils.print_info("******************Audit log details************************")
            for key, value in audit_logs_dict.items():
                self.utils.print_info(f"{key}:{value}")
            kwargs['pass_msg'] = "Successfully search string found in logs"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Audit logs not Found for given search strings"
            self.common_validation.failed(**kwargs)
            return -1

    def _sort_audit_log_columns(self, field, direction):
        """
        - sort the audit log grid column to ascending or descending direction based on the field name

        :param field: column header field name
        :param direction: ascending or descending
        :return: True if sorted based on the direction else False
        """
        # make the column to be visible in the GUI by dragging it to column 8
        if not self.devices_web_elements.get_devices_column_header_cell(field).is_displayed():
            source_el = self.devices_web_elements.get_devices_column_header_cell(field)
            target_el = self.devices_web_elements.get_device_grid_column7()
            self.auto_actions.drag_and_drop_element(source_el, target_el)
            sleep(10)

        click_count = 3
        while click_count > 0:
            self.utils.print_info("Clicking the column header")
            self.auto_actions.click(self.devices_web_elements.get_devices_column_header_cell(field))
            sleep(2)

            sorting_attr = self.devices_web_elements.get_device_column_header_sorting_attr(field)
            if direction.upper() == "ASCENDING":
                if "dgrid-sort-up" in sorting_attr:
                    return True
            if direction.upper() == "DESCENDING":
                if "dgrid-sort-down" in sorting_attr:
                    return True
            click_count -= 1
        self.utils.print_info(f"unable to sort the {field}")
        return False

    def get_audit_logs_row(self, category, search_string):
        """
        - Get the Audit log row with provided search arguments
        - Assumes that Already in Audit logs page
        - Keyword Usage
        - ``Get Audit Logs Row    ${CATEGORY}       ${SEARCH_STRING}``
        - Example of Keyword Usage
        - ``Get Audit Logs Row    MONITORING      Reset device ${AP1_NAME}``

        :param category: Category of Audit log, eg: ADMIN,CONFIG,MONITORING
        :param search_string:  it should be anything which is searched on the row cell
                               eg: Reset device ${AP1_NAME}, Added device, Deleted
        :return: row element if row exists else return -1
        """

        self.utils.print_info("Sorting the Audit logs with timestamp in order to get latest logs ")
        if self._sort_audit_log_columns('field-timeStamp', 'descending'):

            self.utils.print_info("Getting Audit logs rows")
            rows = self.get_authentication_logs_grid_rows()
            sleep(2)
            if not rows:
                self.utils.print_info("Audit Logs rows are not available in the page")
                return False
            self.utils.print_info("Searching with category : ", category, " and Search string : ", search_string)
            for row in rows:
                if re.search(rf'.*{category}.*{search_string}.*', row.text):
                    self.utils.print_info("Row with search string found in Audit logs")
                    self.utils.print_info("ROW --> ", row.text)
                    return row
            return False

    def set_vertical(self, industry_type, **kwargs):
        """
        - This Keyword will set Industry type on xiq side
        - Flow : User account icon-->Global Settings--> Account Details ---> Industry
        - Keyword Usage:
        - `` Reset VIQ ``

        :return: 1 after successfully Resetting VIQ data else -1
        """
        self.utils.print_info("Navigating to the global settings--->Account details")
        self.navigate.navigate_to_account_details_page()

        self.utils.print_info("Click on the Industry drop down")
        self.auto_actions.click_reference(self.get_industry_drop_down_button)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("select the Industry")
        self.auto_actions.select_drop_down_options(self.get_account_industry_drop_down_options(), industry_type)
        sleep(2)
        self.screen.save_screen_shot()

        self.utils.print_info("Click on the apply button")
        self.auto_actions.click_reference(self.get_industry_apply_button)
        sleep(10)
        kwargs['pass_msg'] = "Successfully Resetting VIQ data"
        self.common_validation.passed(**kwargs)
        return 1

    def export_viq(self, **kwargs):
        """
        - This Keyword will Export the current VIQ Data
        - Flow : User account icon-->Global Settings--> VIQ Management ---> Export VIQ
        - Keyword Usage:
        - `` Export VIQ ``

        :return: 1 after successfully exporting the VIQ data else -1
        """
        self.utils.switch_to_default(self.auto_actions.driver)
        sleep(5)
        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Export VIQ Button")
        self.auto_actions.click_reference(self.get_viq_export_button)
        sleep(5)
        self.utils.print_info("Switch to Export Now Tab")
        self.auto_actions.driver.switch_to.window(self.auto_actions.driver.window_handles[1])
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Export Now Button")
        self.auto_actions.click_reference(self.get_viq_export_now_button())
        sleep(2)

        self.utils.print_info("Clicking Yes Button")
        self.auto_actions.click_reference(self.get_viq_export_yes_button)
        sleep(30)

        self.utils.print_info("Clicking OK")
        self.auto_actions.click_reference(self.get_viq_export_ok_button)
        sleep(20)
        self.utils.print_info("Switch to normal tab")
        self.auto_actions.driver.switch_to.window(self.auto_actions.driver.window_handles[0])
        sleep(2)

        self.navigate.navigate_to_devices()
        sleep(2)

        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        export_viq_status_success = self.get_export_status_textfield_success().text
        export_viq_status_fail = self.get_export_status_textfield_fail().text

        if "Succeeded" in export_viq_status_success:
            kwargs['pass_msg'] = f"VIQ Export Is : {export_viq_status_success}"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"VIQ Export Is : {export_viq_status_fail}"
            self.common_validation.failed(**kwargs)
            return -1

    def set_opt_out_copilot_beta(self, option, **kwargs):
        """
        - Enable/Disable Opt out of Copilot BETA
        - Flow : User account image-->Global Settings--> Account Details--> Opt-out of copilot BETA
        - Keyword Usage
        - ``Set Opt Out Copilot BETA     ${OPTION}``

        :param option: option to enable/disable Opt out of Copilot BETA
        :return: 1 If setting opt_out of Copilot BETA is Successful
        """
        self.utils.print_info("Navigating to the global settings--->Account details")
        self.navigate.navigate_to_account_details_page()

        self.utils.print_info(f"Setting Opt-out of Copilot BETA to {option}")

        self.auto_actions.move_to_element(self.get_opt_out_copilot_beta_status())
        self.screen.save_screen_shot()
        sleep(2)

        if option.lower() == "enable":
            if not self.get_opt_out_copilot_beta_status().is_selected():
                self.utils.print_info("Enabling..")
                self.auto_actions.click_reference(self.get_opt_out_copilot_beta_status)
                sleep(1)
                self.screen.save_screen_shot()
            else:
                self.utils.print_info("Option already enabled...")

        if option.lower() == "disable":
            if not self.get_opt_out_copilot_beta_status().is_selected():
                self.utils.print_info("Option already disabled")
            else:
                self.utils.print_info("Disabling...")
                self.auto_actions.click_reference(self.get_opt_out_copilot_beta_status)
                sleep(1)
                self.screen.save_screen_shot()
        kwargs['pass_msg'] = "Successfully setting opt_out of Copilot BETA"
        self.common_validation.passed(**kwargs)
        return 1

    def get_opt_out_status_copilot_beta(self):
        """
        - Get Opt out of Copilot beta status
        - Flow : User account image-->Global Settings--> Account Details--> Opt-out of Copilot BETA
        - Keyword Usage
        - ``Get Opt Out Status Copilot BETA``

        :return: Current status(Enable/Disable) of opt-out Copilot BETA
        """
        self.utils.print_info("Navigating to the global settings--->Account details")
        self.navigate.navigate_to_account_details_page()

        self.utils.print_info("Getting Opt-out of Copilot beta status")

        self.auto_actions.move_to_element(self.get_opt_out_copilot_beta_status())
        self.screen.save_screen_shot()
        sleep(2)

        if not self.get_opt_out_copilot_beta_status().is_selected():
            return "Disable"
        else:
            return "Enable"

    def get_supplemental_cli_option(self, option, **kwargs):
        """
        - This Keyword will Enable/Disable Supplemental CLI in Global Settings
        - Flow : User account image-->Global Settings--> VIQ Management
        - Keyword Usage
        - ``Get supplemental cli option     ${OPTION}``

        :param option: Choose an option for supplemental CLI "enable"\"disable"
        :return: 1 If setting option Supplemental_cli is Successful
        """
        self.utils.print_info("Navigating to the global settings--->VIQ Management")
        self.navigate.navigate_to_viq_management_page()

        self.utils.print_info("Setting Supplemental CLI to {}".format(option))
        if option.lower() == "enable":
            if not self.get_supplemental_cli_option_status().is_selected():
                self.utils.print_info("Enabling..")
                self.auto_actions.click_reference(self.get_supplemental_cli_option_status)
                sleep(1)
            else:
                self.utils.print_info("Option already enabled...")
        elif option.lower() == "disable":
            if not self.get_supplemental_cli_option_status().is_selected():
                self.utils.print_info("Option already disabled")
            else:
                self.utils.print_info("Disabling...")
                self.auto_actions.click_reference(self.get_supplemental_cli_option_status)
                sleep(1)
        else:
            kwargs['fail_msg'] = "Failed setting option Supplemental_cli"
            self.common_validation.failed(**kwargs)
            return -1
        kwargs['pass_msg'] = "Successfully setting option Supplemental_cli"
        self.common_validation.passed(**kwargs)
        return 1

    def change_device_management_settings(self, option, **kwargs):
        """
        - This Keyword will Enable/Disable device management settings for devices that support this feature.
        - Flow : User account image-->Global Settings--> Device Management Settings
        - Keyword Usage
        - ``Change device management settings     ${OPTION} ''

        :param option: Choose an option for Device management settings :"enable"\"disable"
        :return: 1 If changing device management settings is Successful
        """
        self.utils.print_info("Navigating to the global settings---> Device Management Settings")
        self.navigate.navigate_to_device_management_settings()
        sleep(5)
        settings_successfully_changed = False
        did_not_change_settings = False
        self.utils.print_info(f"Changing Device management settings to:{option}")
        if option.lower() == "enable":
            if not self.get_device_management_settings_status().is_selected():
                self.utils.print_info("Enabling..")
                self.auto_actions.click_reference(self.get_device_management_settings_status)
                self.utils.print_info("Saving option")
                self.auto_actions.click_reference(self.get_device_management_settings_save_button)
                sleep(1)
                settings_successfully_changed = True
            else:
                self.utils.print_info("Option already enabled...")
                did_not_change_settings = True
        if option.lower() == "disable":
            if not self.get_device_management_settings_status().is_selected():
                self.utils.print_info("Option already disabled")
                did_not_change_settings = True
            else:
                self.utils.print_info("Disabling...")
                self.auto_actions.click_reference(self.get_device_management_settings_status)
                self.utils.print_info("Saving option")
                self.auto_actions.click_reference(self.get_device_management_settings_save_button)
                sleep(1)
                settings_successfully_changed = True

        if did_not_change_settings:
            kwargs['pass_msg'] = f"Did not Changing Device management settings to '{option}' since it was already set to that value"
            self.common_validation.passed(**kwargs)
            return 1
        elif settings_successfully_changed:
            kwargs['pass_msg'] = f"Successfully change device management settings to '{option}'"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f"Could not successfully change device management settings to '{option}'"
            self.common_validation.failed(**kwargs)
            return -1

    def check_audit_log(self, date_start, description, rows_number='20', **kwargs):
        """
        This function checks if a log is present into audit log

        :param date_start: Starting date for search
        :param description: Expected log description
        :param rows_number: number of logs displayed into table
        :return: 1 if the log was found ; else -1
        """

        user_button = self.devices_web_elements.get_user_button()
        if user_button:
            self.utils.print_info("User button was found ")
            self.auto_actions.move_to_element(user_button)
        else:
            kwargs['fail_msg'] = "User button was not found"
            self.common_validation.failed(**kwargs)
            return -1

        global_settings = self.devices_web_elements.get_global_settings()
        if global_settings:
            self.utils.print_info("global_settings was found ")
            self.auto_actions.click(global_settings)
        else:
            kwargs['fail_msg'] = "global_setting was not found"
            self.common_validation.failed(**kwargs)
            return -1
        sleep(5)
        audit_button = self.devices_web_elements.get_audit_button()
        if audit_button:
            self.utils.print_info("audit_button was found ")
            self.auto_actions.click(audit_button)
        else:
            kwargs['fail_msg'] = "audit_button was not found"
            self.common_validation.failed(**kwargs)
            return -1

        number_of_rows = self.devices_web_elements.get_number_of_rows()
        if number_of_rows:
            for el in number_of_rows:
                self.utils.print_info("check", el.text)
                if rows_number == el.text:
                    self.utils.print_info("click_on", el.text)
                    self.auto_actions.click(el)
                    sleep(2)
                    break
                else:
                    pass
        else:
            kwargs['fail_msg'] = "Failed extracting number of rows"
            self.common_validation.failed(**kwargs)
            return -1

        sort_time_stamp1 = self.devices_web_elements.get_sort_time_stamp()
        if sort_time_stamp1:
            self.utils.print_info("Clicking on sort time ")
            self.auto_actions.click(sort_time_stamp1)
        else:
            self.utils.print_info("Clicking on sort time  not found ")
            pass
        sleep(2)
        sort_time_stamp = self.devices_web_elements.get_sort_time_stamp()
        self.utils.print_info(sort_time_stamp.get_attribute("class"))
        if sort_time_stamp:
            if 'dgrid-sort-down' in sort_time_stamp.get_attribute("class"):
                self.utils.print_info("am ajuns aici 1 ")
                pass
            elif 'dgrid-sort-up' in sort_time_stamp.get_attribute("class"):
                self.utils.print_info("am ajuns aici 2 ")
                self.auto_actions.click(sort_time_stamp)
            else:
                self.utils.print_info("am ajuns aici 3 ")
        else:
            self.utils.print_info("am ajuns aici 4 ")
        sleep(2)
        audit_rows = self.devices_web_elements.get_audit_rows()
        self.utils.print_info("LEN ", len(audit_rows))
        if audit_rows:
            self.utils.print_info("audit_rows was found ")
            cnt = 0
            for el in audit_rows:
                time_stamp = self.devices_web_elements.get_audit_time_stamp(el)
                if time_stamp:
                    self.utils.print_debug("Time_stamp for last log is : ", time_stamp.text)
                    if self.utils.convert_string_to_date(time_stamp.text) > self.utils.convert_string_to_date(
                            date_start):
                        field_description_more_button = self.devices_web_elements.get_field_description_more_button(el)
                        if field_description_more_button:
                            self.utils.print_info("'More' button button was found on row")
                            self.auto_actions.click(field_description_more_button)
                            sleep(5)
                            more_row_description_elements = self.devices_web_elements.get_more_row_description()
                            if more_row_description_elements:
                                more_row_description = more_row_description_elements[
                                    len(more_row_description_elements) - 1]
                                if more_row_description:
                                    self.utils.print_info("This is the log description", more_row_description.text)
                                    if description in more_row_description.text:
                                        self.utils.print_info("This is the log description", more_row_description.text)
                                        sleep(5)
                                        close_more_el = self.devices_web_elements.get_more_row_description_close()
                                        if close_more_el:
                                            close_more = close_more_el[len(close_more_el) - 1]
                                            if close_more:
                                                self.utils.print_info("Click on close")
                                                self.auto_actions.click(close_more)
                                                self.screen.save_screen_shot()
                                            else:
                                                kwargs['fail_msg'] = "Failed clicking on close"
                                                self.common_validation.failed(**kwargs)
                                                return -1
                                        kwargs['pass_msg'] = "Successfully  clicking on  close button"
                                        self.common_validation.passed(**kwargs)
                                        return 1
                                    else:
                                        pass
                                    sleep(5)
                                else:
                                    self.utils.print_info("Description element not found")
                                close_more_el = self.devices_web_elements.get_more_row_description_close()
                                if close_more_el:
                                    close_more = close_more_el[len(close_more_el) - 1]
                                    if close_more:
                                        self.utils.print_info("Click on close")
                                        self.auto_actions.click(close_more)
                                        self.screen.save_screen_shot()
                                    else:
                                        kwargs['fail_msg'] = "Failed clicking on close button"
                                        self.common_validation.failed(**kwargs)
                                        return -1
                        else:
                            field_description = self.devices_web_elements.get_field_description(el)
                            if field_description:
                                if description in field_description.text:
                                    kwargs['pass_msg'] = "Log was found in audit log"
                                    self.common_validation.passed(**kwargs)
                                    return 1
                                else:
                                    pass
                            else:
                                kwargs['fail_msg'] = "Field Description not found"
                                self.common_validation.failed(**kwargs)
                                return -1
                    else:
                        pass
                else:
                    kwargs['fail_msg'] = "time_stamp was not found"
                    self.common_validation.failed(**kwargs)
                    return -1
                cnt = cnt + 1
        else:
            kwargs['fail_msg'] = "Failed determinate audit row"
            self.common_validation.failed(**kwargs)
            return -1
        kwargs['fail_msg'] = "The log was not found . return -1"
        self.common_validation.failed(**kwargs)
        return -1

    def enable_copilot_feature_for_this_viq(self, **kwargs):
        """
        - Enabling CoPilot Feature in Global Settings Page
        - Flow : User account icon-->Global Settings--> VIQ Management
        - Keyword Usage
        - ``Enable CoPilot feature for this VIQ``

        :return: 1 after successfully enabling CoPilot feature, else -1
        """

        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.utils.print_info("Now checking for Enable CoPilot feature for this VIQ")
        self.screen.save_screen_shot()
        if not self.get_enable_copilot_feature_option_status().is_selected():
            self.utils.print_info("Enabling CoPilot feature..")
            self.auto_actions.click_reference(self.get_enable_copilot_feature_option_status)
            sleep(2)
            self.screen.save_screen_shot()
            if self.devices_web_elements.get_ui_banner_warning_message():
                banner_warning_text = self.devices_web_elements.get_ui_banner_warning_message().text
                if banner_warning_text:
                    self.utils.print_info(f"Warning Message: {banner_warning_text}")
                    self.auto_actions.click_reference(self.devices_web_elements.get_ui_banner_warning_close_button)
                    self.screen.save_screen_shot()
                    kwargs['fail_msg'] = f"{banner_warning_text}"
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            self.utils.print_info("Enable CoPilot feature for this VIQ button already enabled...")
            sleep(2)
            self.screen.save_screen_shot()

        return 1

    def disable_copilot_feature_for_this_viq(self):
        """
        - Disabling CoPilot Feature in Global Settings Page
        - Flow : User account icon-->Global Settings--> VIQ Management
        - Keyword Usage
        - ``Disable CoPilot feature for this VIQ``

        :return: 1 after successfully disabling CoPilot feature
        """

        self.navigate.navigate_to_viq_management_page()
        sleep(2)

        self.utils.print_info("Now checking for Enable CoPilot feature for this VIQ")
        self.screen.save_screen_shot()
        if self.get_enable_copilot_feature_option_status().is_selected():
            self.utils.print_info("Disabling CoPilot feature..")
            self.auto_actions.click_reference(self.get_enable_copilot_feature_option_status)
            sleep(2)
            self.screen.save_screen_shot()
        else:
            self.utils.print_info("Enable CoPilot feature for this VIQ button already disabled...")
            sleep(2)
            self.screen.save_screen_shot()

        return 1
