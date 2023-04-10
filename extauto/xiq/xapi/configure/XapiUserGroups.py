from keywords.xapi_base.XapiBaseConfigurationUserManagementApi import XapiBaseConfigurationUserManagementApi
from tools.xapi.XapiHelper import XapiHelper
# from extremecloudiq.models.xiq_user_group import XiqUserGroup
# from extremecloudiq.models.xiq_end_user import XiqEndUser
# from ExtremeAutomation.Library.Utils.DotDict import DotDict
# import time

class XapiUserGroups(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseConfigurationUserManagementApi = XapiBaseConfigurationUserManagementApi()



    def xapi_create_user_group(self, group_name='Demo', user_group_profile=None, **kwargs):

        pass  # This need to support bulk user add
        # """
        #      Will craate the user group based on the parameters that are passed in.
        #
        # :param group_name: The name of the user group
        # :param user_group_profile: See JSON format above
        # :param kwargs:
        # :return: 1 on success and -1 on failure
        # """
        #
        # if user_group_profile == None:
        #     kwargs['fail_msg'] = 'You must provide the user_group_profile argument to this keyword'
        #     self.common_validation.fault(**kwargs)
        #     return -1
        #
        # # Let's see if the group is already created
        # find_response = self.xapi_find_user_group(group_name, ignore_failure=True)
        # if find_response != -1:
        #     # We found the user group, let's try and delete it
        #     self.xapi_delete_user_group(group_name)
        #
        # default_password_settings = {
        #                                 "enable_letters": True,
        #                                 "enable_numbers": True,
        #                                 "enable_special_characters": True,
        #                                 "password_concat_string": "",
        #                                 "psk_generation_method": "PASSWORD_ONLY",
        #                                 "password_character_types": "INCLUDE_ALL_CHARACTER_TYPE_ENABLED",
        #                                 "password_length": 8
        #                             }
        # default_expiration_settings = {
        #                                 "expiration_type": "NEVER_EXPIRE",
        #                                 "valid_during_dates": {
        #                                     "start_date_time": {
        #                                         "day_of_month": 0,
        #                                         "month": 0,
        #                                         "year": 0,
        #                                         "hour_of_day": 0,
        #                                         "minute_of_hour": 0
        #                                     },
        #                                     "end_date_time": {
        #                                         "day_of_month": 0,
        #                                         "month": 0,
        #                                         "year": 0,
        #                                         "hour_of_day": 0,
        #                                         "minute_of_hour": 0
        #                                     },
        #                                     "time_zone": ""
        #                                 },
        #                                 "valid_for_time_period": {
        #                                     "valid_time_period_after": "ID_CREATION",
        #                                     "after_id_creation_settings": {
        #                                         "valid_time_period": 20,
        #                                         "valid_time_period_unit": "MINUTE"
        #                                     },
        #                                     "after_first_login_settings": {
        #                                         "valid_time_period": 20,
        #                                         "valid_time_period_unit": "MINUTE",
        #                                         "first_login_within": 20,
        #                                         "first_login_within_unit": "MINUTE"
        #                                     }
        #                                 },
        #                                 "valid_daily": {
        #                                     "daily_start_hour": 0,
        #                                     "daily_start_minute": 0,
        #                                     "daily_end_hour": 0,
        #                                     "daily_end_minute": 0
        #                                 },
        #                                 "expiration_action": "SHOW_MESSAGE",
        #                                 "post_expiration_action": {
        #                                     "enable_credentials_renewal": True,
        #                                     "enable_delete_immediately": True,
        #                                     "delete_after_value": 0,
        #                                     "delete_after_unit": "MINUTE"
        #                                 }
        #                             }
        # default_delivery_settings = {
        #                                 "email_template_id": 0,
        #                                 "sms_template_id": 0
        #                             }
        # default_ssid = []
        #
        # users_config = user_group_profile.get('users_config')
        # password_settings = user_group_profile.get('passwd_settings', default_password_settings)
        # expiration_settings = user_group_profile.get('expiration_settings', default_expiration_settings)
        # delivery_settings = user_group_profile.get('delivery_settings', default_delivery_settings)
        # client_per_ppsk = user_group_profile.get("client_per_ppsk", False)
        # pcg_use = user_group_profile.get("pcg_use", False)
        # client_num = user_group_profile.get("client_num", 0)
        # pcg_type = user_group_profile.get("pcg-type", "AP_BASED")
        #
        # # Part of the user_group_config
        # user_group_config = user_group_profile.get('user_group_config', None)
        # if user_group_config == None:
        #     kwargs['fail_msg'] = 'You must provide the user_group_profile[\'user_group_config\'] argument to this keyword'
        #     self.common_validation.fault(**kwargs)
        #     return -1
        # password_db_loc = user_group_config.get('pass_db_loc', 'CLOUD')
        # password_type = user_group_config.get('pass_type', 'PPSK')
        # cwp_register = user_group_config.get("cwp_register", False)
        #
        # # Correct the data if needed
        # if isinstance(password_settings, str) and password_settings.lower() == 'none':
        #     password_settings = default_password_settings
        #
        # if isinstance(expiration_settings, str) and expiration_settings.lower() == 'none':
        #     expiration_settings = default_expiration_settings
        #
        # if isinstance(delivery_settings, str) and delivery_settings.lower() == 'none':
        #     delivery_settings = default_delivery_settings
        #
        # xiqUserGroup = XiqUserGroup(id=1,
        #                             create_time=time.time(),
        #                             update_time=time.time(),
        #                             org_id=None,
        #                             name=group_name,
        #                             description="Framwork xapi_create_user_group generated user group",
        #                             predefined=False,
        #                             password_db_location=password_db_loc,
        #                             password_type=password_type,
        #                             pcg_use_only=self.convert_enable_disable_to_bool(pcg_use),
        #                             pcg_type=pcg_type,
        #                             ppsk_use_only=self.convert_enable_disable_to_bool(client_per_ppsk),
        #                             enable_cwp_reg=self.convert_enable_disable_to_bool(cwp_register),
        #                             password_settings=password_settings,
        #                             expiration_settings=expiration_settings,
        #                             delivery_settings=delivery_settings,
        #                             user_count=client_num,
        #                             ssids=default_ssid,
        #                             local_vars_configuration=None)
        #
        # try:
        #     # Create the group
        #     response = self.xapiBaseConfigurationUserManagementApi.xapi_base_create_user_group(xiq_create_user_group_request=xiqUserGroup, _preload_content=False)
        #     # Validate the reponse
        #     self.valid_http_response(response)
        #     # Conver the raw response to an object
        #     user_group_data =  self.convert_preload_content_data_to_object(response.data)
        #     # Get the user group ID
        #     user_group_id = user_group_data.id
        #     base_user_template = {
        #                           "user_group_id": user_group_id,
        #                           "name": "",
        #                           "user_name": "",
        #                           "organization": "",
        #                           "visit_purpose": "",
        #                           "description": "",
        #                           "email_address": "",
        #                           "phone_number": "",
        #                           "password": "",
        #                           "email_password_delivery": '',
        #                           "sms_password_delivery": ""
        #                         }
        #
        #     # add user to user Group
        #     if users_config != 'None':
        #         # Add in full user details
        #         if users_config.get('user-type', '') == 'single':
        #             new_user = DotDict(base_user_template)
        #             new_user.name = users_config.get('name', 'default_name')
        #             new_user.user_name = users_config.get('name', 'default_name')
        #             new_user.organization = users_config.get('organization', '')
        #             new_user.visit_purpose = users_config.get('purpose_of_visit', '')
        #             new_user.email_address = users_config.get('email_address', '')
        #             new_user.phone_number = phone_number = users_config.get('phone_number', '')
        #             new_user.description = users_config.get('description', 'Created with the Automation Framework')
        #
        #             if not user_info.get('pass-generate','') == 'Enable':
        #                 new_user.password = users_config.get('password', '')
        #
        #             if user_info.get('deliver_pass', None):
        #                 new_user.email_password_delivery = users_config.get('deliver_pass', '')
        #
        #             response = self.xapiBaseConfigurationUserManagementApi.xapi_base_create_end_user(xiq_create_end_user_request=new_user, _preload_content=False)
        #             # Validate the reponse
        #             self.valid_http_response(response)
        #
        #         # Mostly blank users, but username is added
        #         elif users_config.get('user-type', '') == 'bulk':
        #             number_of_accounts = int(users_config.get('no_of_accounts', '0'))
        #             for account_number in range(0, number_of_accounts):
        #                 # 'email_user_account_to' Is this a new feature?
        #                 username_prefix = users_config.get('username_prefix', "user_")
        #                 new_user = DotDict(base_user_template)
        #                 new_user.name = f'{username_prefix}{account_number+1}'
        #                 new_user.user_name = f'{username_prefix}{account_number+1}'
        #                 if email_address := users_config.get('email_user_account_to', None):
        #                     new_user.email_password_delivery = email_address
        #                 else:
        #                     kwargs['fail_msg'] = f' "email_user_account_to" can\'t be None for user: -> {new_user.user_name}'
        #                     self.common_validation.fault(**kwargs)
        #                     return -1
        #                 response = self.xapiBaseConfigurationUserManagementApi.xapi_base_create_end_user(xiq_create_end_user_request=new_user, _preload_content=False)
        #                 # Validate the reponse
        #                 self.valid_http_response(response)
        #
        #         # Same user details, but username / password are different
        #         elif users_config.get('user-type', '') == 'multiple':
        #             names = users_config.get('name', "").split()
        #             passwords = users_config.get('password', "").split()
        #             if isinstaceof(names, array) and \
        #                 isinstaceof(passwords, array) and \
        #                 len(names) == len(passwords):
        #                 for name, password in zip(names, passwords):
        #                     new_user = DotDict(base_user_template)
        #                     new_user.name = name
        #                     new_user.user_name = name
        #                     new_user.organization = users_config.get('organization', '')
        #                     new_user.visit_purpose = users_config.get('purpose_of_visit', '')
        #                     new_user.email_address = users_config.get('email_address', '')
        #                     new_user.phone_number = phone_number = users_config.get('phone_number', '')
        #                     new_user.description = users_config.get('description',
        #                                                             'Created with the Automation Framework')
        #                     new_user.password = password
        #                     if user_info.get('deliver_pass', None):
        #                         new_user.email_password_delivery = users_config.get('deliver_pass', '')
        #
        #                     response = self.xapiBaseConfigurationUserManagementApi.xapi_base_create_end_user(
        #                         xiq_create_end_user_request=new_user, _preload_content=False)
        #                     # Validate the reponse
        #                     self.valid_http_response(response)
        #         else:
        #             kwargs['fail_msg'] = f'Failed the users_config {users_config} missing the user-type'
        #             self.common_validation.fault(**kwargs)
        #             return -1
        #
        # except Exception as e:
        #     kwargs['fail_msg'] = f'Failed to create the user group -> {group_name} -> {e}'
        #     self.common_validation.fault(**kwargs)
        #     return -1
        #
        # # If we got here without any errors, we should be good
        # kwargs['pass_msg'] = f'Added users and group {group_name}'
        # self.common_validation.passed(**kwargs)
        # return 1



    def xapi_delete_user_group(self, user_group_name, **kwargs):
        """
            Will search for the user group and if found, delete it.

        :param user_group_name: The user group name (string)
        :return: 1 when the user group was deleted or nothing was found, otherwise -1 on error
        """
        try:
            user_group_list_preload = self.xapiBaseConfigurationUserManagementApi.xapi_base_list_user_groups(limit=100, _preload_content=False)
            user_group_list = self.convert_preload_content_data_to_object(user_group_list_preload.data)
            for user_group in user_group_list.data:
                if user_group_name == user_group.name:
                    response = self.xapiBaseConfigurationUserManagementApi.xapi_base_delete_user_group(id=user_group.id)
                    if response == -1:
                        kwargs['fail_msg'] = f'Failed to delete the user group {user_group_name}'
                        self.common_validation.failed(**kwargs)
                        return -1
            kwargs['pass_msg'] = f'Deleted the user group -> {user_group_name}'
            self.common_validation.passed(**kwargs)
            return 1
        except Exception as e:
            kwargs['fail_msg'] = f'Failed to delete the user group {user_group_name} Exception: {e}'
            self.common_validation.fault(**kwargs)
            return -1

    def xapi_find_user_group(self, user_group_name, **kwargs):
        """
            Will search for the user group and if found it will return it

        :param user_group_name: The user group name (string)
        :return: user group information when the user group was found, otherwise -1 on error or not found
        """
        try:
            user_group_list_preload = self.xapiBaseConfigurationUserManagementApi.xapi_base_list_user_groups(
                limit=100, _preload_content=False)
            user_group_list = self.convertPreloadContentDataToObject(user_group_list_preload.data)
            for user_group in user_group_list.data:
                if user_group_name == user_group.name:
                    kwargs['pass_msg'] = f'Found the user group -> {user_group_name}'
                    self.common_validation.passed(**kwargs)
                    return user_group

            kwargs['fail_msg'] = f'Failed to find the user group {user_group_name}'
            self.common_validation.failed(**kwargs)
            return -1
        except Exception as e:
            kwargs['fail_msg'] = f'Failed to find the user group {user_group_name} Exception: {e}'
            self.common_validation.fault(**kwargs)
            return -1

