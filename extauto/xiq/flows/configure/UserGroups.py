from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.configure.PasswdSettings import PasswdSettings
from extauto.xiq.flows.configure.ExpirationSettings import ExpirationSettings
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.UserGroupsWebElements import UserGroupsWebElements
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.xapi.configure.XapiUserGroups import XapiUserGroups
from ExtremeAutomation.Utilities.deprecated import deprecated


class UserGroups(UserGroupsWebElements):
    def __init__(self, **kwargs):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.screen = Screen()
        self.pass_settings = PasswdSettings()
        self.expiration = ExpirationSettings()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()
        self.builtin = BuiltIn()
        self.xapiUserGroups = XapiUserGroups()

    def _select_password_db_loc_type(self, password_db_loc, password_type):
        """
        - Select the password DB location and password type

        :param password_db_loc:
        :param password_type:
        :return: 1 if success
        """
        self.utils.print_info("Click on password DB location drop down")
        self.auto_actions.click_reference(self.get_password_db_loc_drop_down_button)

        self.utils.print_info(f"Selecting password DB location:{password_db_loc}")
        self.auto_actions.select_drop_down_options(self.get_password_db_loc_items(), password_db_loc)

        self.utils.print_info("Click on password DB location drop down")
        self.auto_actions.click_reference(self.get_password_type_drop_down_button)

        self.utils.print_info(f"Selecting password type:{password_type}")
        self.auto_actions.select_drop_down_options(self.get_password_type_items(), password_type)

        return 1

    def _users_text_field_error_handling(self, text_field_error_els):
        """
        - Checking the mandatory field tool tip text in single user and bulk user creation
        :param text_field_error_els: (list) text filed tool tip elements
        :return: True if no tool tip text else False
        """
        error_texts = [el.text for el in text_field_error_els if el.text]
        error_flag = False
        for text in error_texts:
            if "This field is required" in text:
                self.utils.print_info("Mandatory fields are missing in single user dialog box")
                error_flag = True
            if "This group password can" in text:
                self.utils.print_info(text)
                error_flag = True
        return error_flag

    def add_bulk_user_to_user_group(self, **user_info):
        """
        - Add bulk users to User Groups
        - Keyword Usage:
        - ``Add Bulk User To User Group    &{USER_INFO}``
        - For creating the &{USER_INFO} dict refer user_group_config.robot

        :param user_info:(dict)  buk user config parameters
        :return: True if created else False
        """
        username_prefix = user_info.get('username_prefix')
        no_of_account = user_info.get('no_of_accounts')
        email_user_account_info_to = user_info.get('email_user_account_to')

        self.utils.print_info("Click on bulk user add button")
        self.auto_actions.click_reference(self.get_bulk_user_add_button)

        self.utils.print_info(f"Enter User name prefix{username_prefix}")
        self.auto_actions.send_keys(self.get_bulk_create_users_username_prefix(), username_prefix)

        self.utils.print_info(f"Enter Number accounts:{no_of_account}")
        self.auto_actions.send_keys(self.get_bulk_create_users_number_of_accounts(), no_of_account)

        self.utils.print_info(f"Enter user account info to:{email_user_account_info_to}")
        self.auto_actions.send_keys(self.get_bulk_create_users_email_user_account_info_to(), email_user_account_info_to)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click of done button")
        self.auto_actions.click_reference(self.get_bulk_create_users_done_button)
        sleep(2)

        # Error Handling
        if error_els := self.get_bulk_user_create_text_field_error():
            if self._users_text_field_error_handling(error_els):
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.get_bulk_create_users_cancel_button)
                sleep(2)
                return False
        return True

    def add_single_user_to_user_group(self, password_db_loc, **user_info):
        """
        - Add the single user to User Groups
        - single users options are different based on password_db_loc
        - Keyword Usage:
        - ``Add Single User To User Group    ${PASSWORD_DB_LOC}    &{USER_INFO}``
        - For creating &{USER_INFO} refer user_group_config.robot

        :param user_info: (dict)  Single user config parameters
        :param password_db_loc:  it will take either local or cloud
        :return: True if created else False
        """
        self.utils.print_info("Click on user add button")
        if self.get_single_user_add_button():
            self.auto_actions.click_reference(self.get_single_user_add_button)
            sleep(2)
        else:
            self.auto_actions.click_reference(self.get_guest_mgmt_account_single_usr_add_button)
            sleep(2)

        self.utils.print_info(f"Enter the user name:{user_info['name']}")
        self.auto_actions.send_keys(self.get_single_user_name_field(), user_info['name'])

        if password_db_loc.upper() == 'LOCAL':
            self.utils.print_info(f"Enter the Email address:{user_info['email_address']}")
            self.auto_actions.send_keys(self.get_single_user_email_address_field(), user_info['email_address'])
        else:
            self.utils.print_info(f"Enter the Organization name:{user_info['organization']}")
            self.auto_actions.send_keys(self.get_single_user_org_filed(), user_info['organization'])

            self.utils.print_info(f"Enter the purpose of visit:{user_info['purpose_of_visit']}")
            self.auto_actions.send_keys(self.get_single_user_purpose_of_visit_field(), user_info['purpose_of_visit'])

            self.utils.print_info(f"Enter the Email address:{user_info['email_address']}")
            self.auto_actions.send_keys(self.get_single_user_email_address_field(), user_info['email_address'])

            country_code, number = user_info['phone_number'].split('-')

            self.utils.print_info("Click on country code drop down")
            self.auto_actions.click_reference(self.get_single_user_country_code_drop_down)

            self.utils.print_info(f"Selecting country code:{country_code}")
            self.auto_actions.select_drop_down_options(self.get_single_user_country_code_items(), country_code)

            self.utils.print_info(f"Enter the phone number:{number}")
            self.auto_actions.send_keys(self.get_single_user_phone_number(), number)

            self.utils.print_info("Select user-name type")
            self.auto_actions.click_reference(self.get_single_user_user_name_drop_down)

            self.utils.print_info(f"Select User Name type:{user_info['user_name_type']}")
            self.auto_actions.select_drop_down_options(self.get_single_user_user_name_items(),
                                                       user_info['user_name_type'])

        self.screen.save_screen_shot()
        sleep(2)

        if user_info['pass-generate'] == 'Enable':
            self.utils.print_info("Generating user password")
            self.auto_actions.click_reference(self.get_single_user_password_generate_button)
        else:
            self.utils.print_info("Enter the user password")
            self.auto_actions.send_keys(self.get_single_user_password_field(), user_info['password'])

        self.utils.print_info("Enter the user description")
        self.auto_actions.send_keys(self.get_single_user_description(), user_info['description'])

        if user_info.get('deliver_pass'):
            self.utils.print_info(f"Credential Delivery Email:{user_info['deliver_pass']}")
            self.auto_actions.enable_check_box(self.get_single_user_deliver_password_check_box())
            self.auto_actions.send_keys(self.get_single_user_deliver_password(), user_info['deliver_pass'])

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on done button")
        self.auto_actions.click_reference(self.get_single_user_create_done_button)
        sleep(2)

        if error_filed := self.get_single_user_create_text_field_error():
            if self._users_text_field_error_handling(error_filed):
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.get_single_user_create_cancel_button)
                return False
        return True

    def _add_users_to_user_group(self, user_info, password_db_loc):
        """
        - Add the users to user group based on the user-type and password db loc

        :param user_info:
        :param password_db_loc:
        :return:
        """
        if not self.get_add_user_toggle_button().is_selected():
            self.auto_actions.click_reference(self.get_add_user_toggle_button)

        if user_info['user-type'] == 'single':
            return self.add_single_user_to_user_group(password_db_loc, **user_info)

        elif user_info['user-type'] == 'bulk':
            return self.add_bulk_user_to_user_group(**user_info)

        elif user_info['user-type'] == 'multiple':
            return self.add_multiple_user_to_user_group(password_db_loc, **user_info)

    def _private_client_groups_config(self, pcg_type):
        """
        - If "Enable use for Private Client Group" check box selected
        - select the pcg_type radio button 'AP-Based', 'Key-Based'

        :param pcg_type: 'AP-Based' or 'Key-Based'
        :return:
        """
        self.utils.print_info("Select Private client groups check box")
        self.auto_actions.enable_check_box(self.get_pcg_use_checkbox())

        if pcg_type == 'AP-Based':
            self.utils.print_info("Selecting AP-Based radio button")
            self.auto_actions.click_reference(self.get_ap_based_radio_button)
        if pcg_type == 'Key-Based':
            self.utils.print_info("Selecting Key-Based radio button")
            self.auto_actions.click_reference(self.get_key_based_radio_button)

    def _configure_cloud_ppsk_setting(self, group_conf):
        """
        - If password db loc is "CLOUD" and password type is "PPSK"
        - Select the different options combination PCG Use, Enable CWP Register

        :param group_conf: (dict) configuration parameters
        :return:
        """

        if group_conf['cwp_register'] == "Enable":
            self.utils.print_info("Selecting CWP register check box")
            self.auto_actions.enable_check_box(self.get_cwp_register_checkbox())

        if group_conf['pcg_use'] == 'Enable':
            self._private_client_groups_config(group_conf['pcg-type'])

    def _configure_local_ppsk_settings(self, group_conf):
        """
        - If password db loc is "LOCAL" and password type is "PPSK"
        - select the check box based on the config dict
        :param group_conf: (dict) configuration parameters
        :return:
        """
        if group_conf['client_per_ppsk'] == 'Enable':
            self.utils.print_info("Selecting client per ppsk check box")
            self.auto_actions.enable_check_box(self.get_max_num_of_clients_per_ppsk_check_box())

            self.utils.print_info("Enter the number of clients per ppsk")
            self.utils.print_info(f"Maximum number of clients per private PSK: {group_conf['client_num']}")
            self.auto_actions.send_keys(self.get_max_num_of_clients_per_ppsk_input_field(), group_conf['client_num'])

        if group_conf['pcg_use'] == 'Enable':
            self._private_client_groups_config(group_conf['pcg-type'])

        if group_conf['ppsk_classification'] == "Enable":
            self.utils.print_info("Select PPSK Classification Use check box")
            self.auto_actions.enable_check_box(self.get_ppsk_classification_use_checkbox())

    def _select_user_group_row(self, user_group_name):
        """
        - Select the user group row

        :param user_group_name: name of the user group
        :return:
        """
        if row := self._search_user_group(user_group_name):
            self.auto_actions.click(self.get_user_group_row_cell(row, 'dgrid-selector'))
            return 1

    def _search_user_group(self, user_group_name):
        """
        - Search the user group in user group grid rows

        :param user_group_name: name of the group to search
        :return: 1 if group else None
        """
        if group_row := self.get_user_group_grid_rows():
            for row in group_row:
                if user_group_name in row.text:
                    self.utils.print_info(f"User group name exists:{user_group_name}")
                    return row
        self.utils.print_info("User Group not exists. Lets create it")

    def _config_user_group(self, group_name, **group_group_profile):
        """
        - Configure user group with passed group config dict
        :param group_name: name of the group
        :param group_group_profile: (dict) configuration dictionary
        :return:

        Flow changed in this keyword because of: APC-47809
        Does not require save button to be clicked
        """

        user_group_config = group_group_profile.get('user_group_config')
        password_settings = group_group_profile.get('passwd_settings', 'None')
        expiration_settings = group_group_profile.get('expiration_settings', 'None')
        delivery_settings = group_group_profile.get('delivery_settings', 'None')
        users_config = group_group_profile.get('users_config')
        password_db_loc = user_group_config.get('pass_db_loc', 'CLOUD')
        password_type = user_group_config.get('pass_type', 'PPSK')
        cwp_register = user_group_config.get("cwp_register")


        self.utils.print_info("Enter the user group name")
        self.auto_actions.send_keys(self.get_user_group_name_field(), group_name)

        # select the password db location
        self._select_password_db_loc_type(password_db_loc, password_type)

        if password_db_loc.upper() == "CLOUD" and password_type.upper() == "RADIUS":
            if cwp_register == 'Enable':
                self.utils.print_info("Selecting cwp register check box")
                self.auto_actions.enable_check_box(self.get_cwp_register_checkbox())

        elif password_db_loc.upper() == "LOCAL" and password_type.upper() == "RADIUS":
            self.utils.print_info("No check box to configure")

        elif password_db_loc.upper() == "LOCAL" and password_type.upper() == "PPSK":
            self._configure_local_ppsk_settings(user_group_config)

        elif password_db_loc.upper() == "CLOUD" and password_type.upper() == "PPSK":
            self._configure_cloud_ppsk_setting(user_group_config)

        self.screen.save_screen_shot()
        sleep(2)

        # password setting configuration
        if password_settings != 'None':
            self.pass_settings.config_password_settings(**password_settings)

        # Expiration setting configuration
        if expiration_settings != 'None':
            self.expiration.config_expiration_settings(**expiration_settings)

        # delivery settings
        if delivery_settings != 'None':
            pass

        # add user to user Group
        if users_config != 'None':
            if not self._add_users_to_user_group(users_config, password_db_loc):
                return -1

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_user_group_save_button():
            self.utils.print_info("clicking on user group save button")
            self.auto_actions.click_reference(self.get_user_group_save_button)
            sleep(5)

        if error_field := self.get_user_group_text_field_form_error():
            if self._user_groups_text_field_error_handling(error_field):
                return -1

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tip_text)
        for text in tool_tip_text:
            if "User Group was saved successfully." in text:
                self.utils.print_info(f"{text}")
                return 1
            if "Die Benutzergruppe" in text:
                self.utils.print_info(f"{text}")
                return 1

            if "PPSK Classification Use and PCG Use cannot be enabled at the same time" in text:
                self.builtin.fail(f"{text}")

            if "The user cannot be saved because the name" in text:
                self.builtin.fail(f"{text}. delete the users from the already attached group and re-run the test")

            if "The User Group cannot be saved because the name" in text:
                self.builtin.fail(f"{text}. delete the user group or choose different name and re-run the test")

    @deprecated('Please use the {create_user_group} keyword keywords/gui/configure/KeywordsUserGroups.py. This method can removed after 6/17/2023')
    def create_user_group(self, group_name='Demo', user_group_profile=None, **kwargs):
        return self.gui_create_user_group(group_name, user_group_profile, **kwargs)

    def gui_create_user_group(self, group_name='Demo', user_group_profile=None, **kwargs):
        """
        - Flow: Configure --> Users --> User Groups
        - Create User Groups and add users to user Groups
        - Keyword Usage
        - ``Create User Group   group_name=${GROUP_NAME}   user_group_profile=&{USER_GROUP_PROFILE}``
        - for supported combination of  &{USER_GROUP_PROFILE} creation refer  "user_group_config.robot"

        :param group_name: Name of the user group
        :param user_group_profile: (dict)  configuration parameter
        :return: 1 if created else -1
        """

        # Need to add support in XAPI for bulk user add in order to support this feature
        # if self.xapiUserGroups.is_xapi_enabled(**kwargs):
        #     return self.xapiUserGroups.xapi_create_user_group(group_name=group_name,
        #                                                         user_group_profile=user_group_profile,
        #                                                         **kwargs)

        self.utils.print_info("Navigating to the configure users")
        self.navigator.navigate_to_configure_user_groups()

        if self._search_user_group(group_name):
            self.utils.print_info(f"User group:{group_name} already exists in user group list")
            return 1

        self.utils.print_info("Click on user group add button")
        self.auto_actions.click_reference(self.get_user_group_add_button)

        return self._config_user_group(group_name, **user_group_profile)

    def _user_groups_text_field_error_handling(self, field_error_els):
        """
        Checking the tool tip text for each input text field in user groups window

        :param field_error_els: (list) list of tool tip error elements
        :return: True if no error else False
        """
        error_flag = False
        error_texts = [el.text for el in field_error_els if el.text]
        for error in error_texts:
            if "Please enter a value from 0 to 15." in error:
                self.utils.print_info("Max number of clients allowed per PPSK is 0-15 ")
                error_flag = True

            if "This field is required." in error:
                self.utils.print_info("User Group name is required")
                error_flag = True
        return error_flag

    def _perform_user_group_delete(self):
        """
        Clicking on the user group delete button
        :return:
        """
        self.utils.print_info("Click on user group delete button")
        self.auto_actions.click_reference(self.get_user_group_delete_button)

        sleep(2)
        self.utils.print_info("Click on confirmation Yes Button")
        self.auto_actions.click_reference(self.get_user_group_delete_confirm_yes_button)
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        sleep(2)
        for text in tool_tp_text:
            if "The user group cannot be removed " in text:
                self.utils.print_info("User Group is attached to the device object, can't remove user Group")
                return -1
            elif "User group was deleted successfully." in text:
                return 1
        return -1

    def delete_user_group(self, user_group_name, **kwargs):
        """
        - Flow Configure --> Users --> User Groups
        - Delete the User Groups form User Groups grid
        - Keyword Usage:
        - ``Delete User Group   ${USER_GROUP_NAME}``

        Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

        :param user_group_name: Name of the user group
        :return: 1 if deleted successfully else -1
        """

        if self.xapiUserGroups.is_xapi_enabled(**kwargs):
            return self.xapiUserGroups.xapi_delete_user_group(user_group_name=user_group_name, **kwargs)

        self.utils.print_info("Navigating to the configure users")
        self.navigator.navigate_to_configure_user_groups()

        if not self._search_user_group(user_group_name):
            self.utils.print_info("User group doesn't exists in user group list")
            return 1

        self.utils.print_info("Select Network policy row")
        self._select_user_group_row(user_group_name)
        return self._perform_user_group_delete()

    def delete_user_groups(self, *groups):
        """
        - Delete the multiple user groups form user groups grid
        - Keyword Usage:
        - ``Delete User Groups    ${GROUP_NAME1}   ${GROUP_NAME2}``

        :param groups: groups names
        :return: 1 if deleted successfully else -1
        """
        self.utils.print_info("Navigating to the configure users")
        self.navigator.navigate_to_configure_user_groups()

        self.utils.print_info("Click on full page view")
        if self.get_page_size_element():
            self.auto_actions.click_reference(self.get_page_size_element)
            sleep(3)

        group_select_flag = None
        user_group_flag = -1
        for group in groups:
            if not self._search_user_group(group):
                self.utils.print_info("User group doesn't exists in user group list")
                user_group_flag = 1
                continue
            else:
                self._select_user_group_row(group)
                group_select_flag = True
        if group_select_flag:
            return self._perform_user_group_delete()
        if user_group_flag == 1:
            return 1

    def select_wireless_user_group(self, group_name, passwd_db_loc='None', passwd_type='None'):
        """
        - Select the wireless user group from select window if it already created
        - Keyword Usage:
        - ``Select Wireless User Group   group_name=${GROUP_NAME}   passwd_db_loc=&{PASSWD_DB_LOC}
                                          passwd_type=${PASSWD_TYPE}''
        :param group_name: name of the user group
        :param passwd_db_loc: password DB location
        :param passwd_type:  Password type
        :return: True if group select else False
        """
        self.utils.print_info("Click on user group select button")
        self.auto_actions.click_reference(self.get_wireless_user_group_select_button)
        sleep(2)

        if passwd_type.upper() == "PPSK":
            if passwd_db_loc.upper() == "LOCAL":
                self.utils.print_info("Click on user group select window local tab")
                self.auto_actions.click_reference(self.get_wireless_usr_grp_select_wind_local_tab)
                sleep(5)
            if passwd_db_loc.upper() == "CLOUD":
                self.utils.print_info("Click on user group select window Cloud tab")
                self.auto_actions.click_reference(self.get_wireless_usr_grp_select_wind_cloud_tab)
                sleep(5)

        for row in self.get_wireless_user_group_select_window_group_rows():
            if group_name.upper() in row.text.upper():
                self.utils.print_info(f"Selecting the User Group: {group_name}")
                self.auto_actions.click(self.get_wireless_usr_grp_select_wind_grp_row_check_box(row))
                sleep(2)
                self.auto_actions.click_reference(self.get_wireless_usr_grp_select_wind_select_button)
                return True
        self.utils.print_info(f"User group:{group_name} not present !!!")
        self.auto_actions.click_reference(self.get_wireless_usr_grp_select_wind_cancel_button)
        return False

    def add_wireless_nw_user_group(self, group_name='Demo', user_group_profile=None):
        """
        - supports to create the user groups from wireless network page
        - there are two ways to call this keyword
        - standalone: Assumes that already navigated to the wireless network tab
        - Keyword Usage:
        - ``Add Wireless Nw User Group   ${GROUP_NAME}   &{USER_GROUP_PROFILE}``

        :param group_name: (str)  Name of the group to create
        :param user_group_profile: (dict)  Config Parameters to create the user groups refer user_groups_config for
                                           different combination of user group profile
        :return: 1 if success else -1
        """
        user_group_config = user_group_profile.get('user_group_config')
        password_db_loc = user_group_config.get('pass_db_loc', 'CLOUD')
        password_type = user_group_config.get('pass_type', 'PPSK')

        self.utils.print_info(f"Select the user group:{group_name}")
        if self.select_wireless_user_group(group_name, password_db_loc, password_type):
            return 1

        self.utils.print_info("Click on user group add button")
        self.auto_actions.click_reference(self.get_wireless_usr_group_add_button)
        return self._config_user_group(group_name, **user_group_profile)

    def add_multiple_user_to_user_group(self, password_db_loc, **user_info):
        """
        - Add the multiple user to User Group
        - multiple users options are different based on password_db_loc
        - Keyword Usage:
        - ``Add Multiple User To User Group    ${PASSWORD_DB_LOC}    &{USER_INFO}``
        - For creating &{USER_INFO} refer user_group_config.robot

        :param user_info: (dict)  Multiple user config parameters
        :param password_db_loc:  it will take either local or cloud
        :return: True if created else False
        """
        names = user_info['name'].split()
        passwords = user_info['password'].split()
        self.utils.print_info(f"Enter the passwords {passwords}")
        for num, name in enumerate(names):
            self.utils.print_info("Click on user add button")
            if self.get_single_user_add_button():
                self.auto_actions.click_reference(self.get_single_user_add_button)
                sleep(2)
            else:
                self.auto_actions.click_reference(self.get_guest_mgmt_account_single_usr_add_button)
                sleep(2)

            self.utils.print_info(f"Enter the user name:{name}")

            self.auto_actions.send_keys(self.get_single_user_name_field(), name)

            if password_db_loc.upper() == 'LOCAL':
                self.utils.print_info(f"Enter the Email address:{user_info['email_address']}")
                self.auto_actions.send_keys(self.get_single_user_email_address_field(), user_info['email_address'])
            else:
                self.utils.print_info(f"Enter the Organization name:{user_info['organization']}")
                self.auto_actions.send_keys(self.get_single_user_org_filed(), user_info['organization'])

                self.utils.print_info(f"Enter the purpose of visit:{user_info['purpose_of_visit']}")
                self.auto_actions.send_keys(self.get_single_user_purpose_of_visit_field(), user_info['purpose_of_visit'])

                self.utils.print_info(f"Enter the Email address:{user_info['email_address']}")
                self.auto_actions.send_keys(self.get_single_user_email_address_field(), user_info['email_address'])

                country_code, number = user_info['phone_number'].split('-')

                self.utils.print_info("Click on country code drop down")
                self.auto_actions.click_reference(self.get_single_user_country_code_drop_down)

                self.utils.print_info(f"Selecting country code:{country_code}")
                self.auto_actions.select_drop_down_options(self.get_single_user_country_code_items(), country_code)

                self.utils.print_info(f"Enter the phone number:{number}")
                self.auto_actions.send_keys(self.get_single_user_phone_number(), number)

                self.utils.print_info("Select user-name type")
                self.auto_actions.click_reference(self.get_single_user_user_name_drop_down)

                self.utils.print_info(f"Select User Name type:{user_info['user_name_type']}")
                self.auto_actions.select_drop_down_options(self.get_single_user_user_name_items(),
                                                           user_info['user_name_type'])

            self.screen.save_screen_shot()
            sleep(2)

            if user_info['pass-generate'] == 'Enable':
                self.utils.print_info("Generating user password")
                self.auto_actions.click_reference(self.get_single_user_password_generate_button)
            else:
                self.utils.print_info("Enter the user password")
                self.auto_actions.send_keys(self.get_single_user_password_field(), passwords[num])

            self.utils.print_info("Enter the user description")
            self.auto_actions.send_keys(self.get_single_user_description(), user_info['description'])

            if user_info.get('deliver_pass'):
                self.utils.print_info(f"Credential Delivery Email:{user_info['deliver_pass']}")
                self.auto_actions.enable_check_box(self.get_single_user_deliver_password_check_box())
                self.auto_actions.send_keys(self.get_single_user_deliver_password(), user_info['deliver_pass'])

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click on done button")
            self.auto_actions.click_reference(self.get_single_user_create_done_button)
            sleep(2)

            if error_filed := self.get_single_user_create_text_field_error():
                if self._users_text_field_error_handling(error_filed):
                    self.screen.save_screen_shot()
                    self.auto_actions.click_reference(self.get_single_user_create_cancel_button)
                    return False
        return True

    def create_add_user_to_user_group(self, user_group, user_info, **kwargs):
        """
        - Add the single user to existing User Groups
        - Keyword Usage:
        - ``Create Add User To User Group    ${user_group}    &{USER_INFO}``
        - For creating &{USER_INFO} refer user_group_config.robot

        :param user_info: (dict)  Single user config parameters
        :param user_group:  Existing User Group name to which the user will be added
        :return: 1 if created else -1
        """

        user_info = user_info.get('user_config')
        self.utils.print_info("Navigating to the configure users")

        self.navigator.navigate_to_configure_users_subtab_users()
        sleep(2)
        self.auto_actions.click_reference(self.get_add_user_button_users_sub_tab)
        sleep(2)
        self.auto_actions.click_reference(self.get_user_group_dropdown)
        sleep(2)
        self.auto_actions.select_drop_down_options(self.get_select_user_group_from_dropdown(), user_group)

        self.utils.print_info(f"Enter the user name:{user_info['name']}")
        self.auto_actions.send_keys(self.get_single_user_name_field(), user_info['name'])


        self.utils.print_info(f"Enter the Organization name:{user_info['organization']}")
        self.auto_actions.send_keys(self.get_single_user_org_filed(), user_info['organization'])

        self.utils.print_info(f"Enter the purpose of visit:{user_info['purpose_of_visit']}")
        self.auto_actions.send_keys(self.get_single_user_purpose_of_visit_field(), user_info['purpose_of_visit'])

        self.utils.print_info(f"Enter the Email address:{user_info['email_address']}")
        self.auto_actions.send_keys(self.get_single_user_email_address_field(), user_info['email_address'])

        country_code, number = user_info['phone_number'].split('-')

        self.utils.print_info("Click on country code drop down")
        self.auto_actions.click_reference(self.get_single_user_country_code_drop_down)

        self.utils.print_info(f"Selecting country code:{country_code}")
        self.auto_actions.select_drop_down_options(self.get_single_user_country_code_items(), country_code)

        self.utils.print_info(f"Enter the phone number:{number}")
        self.auto_actions.send_keys(self.get_single_user_phone_number(), number)

        self.utils.print_info("Select user-name type")
        self.auto_actions.click_reference(self.get_single_user_user_name_drop_down)

        self.utils.print_info(f"Select User Name type:{user_info['user_name_type']}")
        self.auto_actions.select_drop_down_options(self.get_single_user_user_name_items(),
                                                   user_info['user_name_type'])

        self.screen.save_screen_shot()
        sleep(2)

        if user_info['pass-generate'] == 'Enable':
            self.utils.print_info("Generating user password")
            self.auto_actions.click_reference(self.get_single_user_password_generate_button)
        else:
            self.utils.print_info("Enter the user password")
            self.auto_actions.send_keys(self.get_single_user_password_field(), user_info['password'])

        self.utils.print_info("Enter the user description")
        self.auto_actions.send_keys(self.get_single_user_description(), user_info['description'])

        if user_info.get('deliver_pass'):
            self.utils.print_info(f"Credential Delivery Email:{user_info['deliver_pass']}")
            self.auto_actions.enable_check_box(self.get_single_user_deliver_password_check_box())
            self.auto_actions.send_keys(self.get_single_user_deliver_password(), user_info['deliver_pass'])

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on done button")
        self.auto_actions.click_reference(self.get_single_user_create_done_button)
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        sleep(2)
        for text in tool_tp_text:
            if "User was saved successfully" in text:
                self.utils.print_info(f"Created User {user_info['name']} successfully")
                self.screen.save_screen_shot()
                kwargs['pass_msg'] = f"Printing all the tool tip messages:- {text}"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['fail_msg'] = "Tool Tip not showing proper message"
        self.common_validation.failed(**kwargs)
        return -2

    def delete_single_user(self, user, **kwargs):
        """
        - Delete single user from existing User Group
        - Keyword Usage:
        - ``Delete single User    ${user}``

        :param user:  username
        :return: 1 if deleted else -1
        """

        self.utils.print_info("Navigating to the configure users")
        self.navigator.navigate_to_configure_users_subtab_users()

        self.utils.print_info("Click on full page view")
        if self.get_page_size_element():
            self.auto_actions.click_reference(self.get_page_size_element)

        sleep(3)
        rows = self.get_users_subtab_user_row()
        flag =0
        for row in rows:
            if self.get_username_in_users_subtab(row).text.strip().lower() == user.lower():
                sleep(2)
                self.utils.print_info("Found User,Selecting User in Users Sub Tab")
                self.auto_actions.click(self.get_select_user_in_users_subtab(row))
                sleep(2)
                self.utils.print_info("Clicking on Delete User Button")
                self.auto_actions.click_reference(self.get_delete_user_from_users_subtab)
                sleep(2)
                self.utils.print_info("Click on confirmation Yes Button")
                self.auto_actions.click_reference(self.get_user_delete_confirm_yes_button)
                sleep(1)
                self.screen.save_screen_shot()
                sleep(2)
                flag = 1
                break

        if flag == 0:
            kwargs['fail_msg'] = f"User with name {user} not found"
            self.common_validation.failed(**kwargs)
            return -1

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        sleep(2)
        for text in tool_tp_text:
            if "users were deleted successfully" in text:
                kwargs['pass_msg'] = f"Deleted User {user} successfully Printing all the tool tip messages:- {text}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Tool Tip not showing proper message"
        self.common_validation.failed(**kwargs)
        return -2

    def edit_single_user_password(self, user, password, **kwargs):
        """
        - Edit and change password of single user from existing User Group
        - Keyword Usage:
        - ``Edit Single User Password   ${user}    ${password}``

        :param user:  username
        :param password:  password
        :return: 1 if edited else -1
        """
        self.utils.print_info("Navigating to the configure users")
        self.navigator.navigate_to_configure_users_subtab_users()

        self.utils.print_info("Click on full page view")
        if self.get_page_size_element():
            self.auto_actions.click_reference(self.get_page_size_element)

        sleep(3)
        rows = self.get_users_subtab_user_row()
        flag =0
        for row in rows:
            if self.get_username_in_users_subtab(row).text.strip().lower() == user.lower():
                sleep(2)
                self.utils.print_info("Found User,Selecting User in Users Sub Tab")
                self.auto_actions.click(self.get_select_user_in_users_subtab(row))
                sleep(2)
                self.utils.print_info("Clicking on Edit User Button")
                self.auto_actions.click_reference(self.get_edit_user_from_users_subtab)
                sleep(2)
                self.screen.save_screen_shot()
                sleep(2)
                flag = 1
                break

        if flag == 0:
            kwargs['fail_msg'] = f"User with name {user} not found"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Entering the user password")
        self.get_single_user_password_field().clear()
        sleep(1)
        self.auto_actions.send_keys(self.get_single_user_password_field(), password)
        sleep(2)
        self.auto_actions.click_reference(self.get_single_user_create_done_button)
        sleep(2)
        self.screen.save_screen_shot()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        sleep(2)
        for text in tool_tp_text:
            if "User was saved successfully" in text:
                kwargs['pass_msg'] = f"Changed Password for User {user} successfully. " \
                                     f"Printing all the tool tip messages:- {text}"
                self.common_validation.passed(**kwargs)
                return 1

        kwargs['fail_msg'] = "Tool Tip not showing proper message"
        self.common_validation.failed(**kwargs)
        return -2

    def select_wireless_user_profile(self, profile_name, **kwargs):
        """
        - Select the wireless user Profile from select window if it already created
        - Keyword Usage:
        - ``Select Wireless User Group   profile_name=${PROFILE_NAME}''
        :param Profile_name: name of the user group
        :return: True if User profile selected Successfully else False
        """
        self.utils.print_info("Click on user Profile select button")
        self.auto_actions.click_reference(self.get_wireless_user_profile_select_button)
        sleep(2)

        for row in self.get_wireless_user_profile_select_window_group_rows():
            if profile_name.upper() in row.text.upper():
                self.utils.print_info(f"Selecting the User Profile: {profile_name}")
                self.auto_actions.click(self.get_wireless_usr_profile_select_wind_grp_row_check_box(row))
                sleep(2)
                self.auto_actions.click_reference(self.get_wireless_usr_profile_select_wind_select_button)
                kwargs['pass_msg'] = "User profile selected Successfully"
                self.common_validation.passed(**kwargs)
                return True

        self.auto_actions.click_reference(self.get_wireless_usr_profile_select_wind_cancel_button)
        kwargs['fail_msg'] = f"User Profile:{profile_name} not present"
        self.common_validation.failed(**kwargs)
        return False

    def delete_all_user_groups(self, **kwargs):
        """
        - Delete all custom user groups
        - Keyword Usage:
        - ``delete_all_user_groups    IRV=True``

        :param IRV:    if False, the error will skip, otherwise, error will not skip
        :return: 1 if deleted successfully else -1
        """

        exclusive_groups = ['GA-ppsk-user-device', 'GA-ppsk-user-service', 'GA-ppsk-self-reg', 'GA-RADIUS-us']

        self.utils.print_info("Navigating to the configure users")
        if not self.navigator.navigate_to_configure_user_groups():
            kwargs['fail_msg'] = "Unable to navigate to the user group page"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Click on full page view")
        if self.get_page_size_element():
            self.auto_actions.click_reference(self.get_page_size_element)

        sleep(5)
        self.utils.print_info("Get an user group total")
        total_rows = self.get_user_group_grid_rows()
        if total_rows != None:
            if int(len(total_rows)) - 1 == len(exclusive_groups):
                self.utils.print_info("There are no custom user groups to delete")
                return 1
        else:
            kwargs['fail_msg'] = "Could not get an user group list"
            self.common_validation.failed(**kwargs)
            return -1

        try:
            self.auto_actions.click_reference(self.get_usr_group_select_all_checkbox)
            for exclusive_group in exclusive_groups:
                if not self._search_user_group(exclusive_group):
                    kwargs['fail_msg'] = "User group does not exist in the user group list "
                    self.common_validation.failed(**kwargs)
                    return -1
                else:
                    self._select_user_group_row(exclusive_group)
        except Exception:
            kwargs['fail_msg'] = "Not able to select the exclusive user group "
            self.common_validation.failed(**kwargs)
            return -1

        if self._perform_user_group_delete() == -1:
            kwargs['fail_msg'] = "Unable to delete all custom users "
            self.common_validation.failed(**kwargs)
            return -1

        return 1
