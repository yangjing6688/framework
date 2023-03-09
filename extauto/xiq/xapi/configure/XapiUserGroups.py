from keywords.xapi_base.XapiBaseConfigurationUserManagementApi import XapiBaseConfigurationUserManagementApi
from tools.xapi.XapiHelper import XapiHelper
from extremecloudiq.models.xiq_user_group import XiqUserGroup
import time

class XapiUserGroups(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseConfigurationUserManagementApi = XapiBaseConfigurationUserManagementApi()



    def xapi_create_user_group(self, group_name='Demo', user_group_profile=None, **kwargs):
        """
             Will craate the user group based on the parameters that are passed in.

        :param group_name: The name of the user group
        :param user_group_profile: See JSON format above
        :param kwargs:
        :return: 1 on success and -1 on failure
        """

        if user_group_profile == None:
            kwargs['fail_msg'] = 'You must provide the user_group_profile argument to this keyword'
            self.common_validation.fault(**kwargs)
            return -1

        default_password_settings = {
                                        "enable_letters": True,
                                        "enable_numbers": True,
                                        "enable_special_characters": True,
                                        "password_concat_string": "string",
                                        "psk_generation_method": "PASSWORD_ONLY",
                                        "password_character_types": "INCLUDE_ALL_CHARACTER_TYPE_ENABLED",
                                        "password_length": 8
                                    }
        default_expiration_settings = {
                                        "expiration_type": "NEVER_EXPIRE",
                                        "valid_during_dates": {
                                            "start_date_time": {
                                                "day_of_month": 0,
                                                "month": 0,
                                                "year": 0,
                                                "hour_of_day": 0,
                                                "minute_of_hour": 0
                                            },
                                            "end_date_time": {
                                                "day_of_month": 0,
                                                "month": 0,
                                                "year": 0,
                                                "hour_of_day": 0,
                                                "minute_of_hour": 0
                                            },
                                            "time_zone": "string"
                                        },
                                        "valid_for_time_period": {
                                            "valid_time_period_after": "ID_CREATION",
                                            "after_id_creation_settings": {
                                                "valid_time_period": 20,
                                                "valid_time_period_unit": "MINUTE"
                                            },
                                            "after_first_login_settings": {
                                                "valid_time_period": 20,
                                                "valid_time_period_unit": "MINUTE",
                                                "first_login_within": 20,
                                                "first_login_within_unit": "MINUTE"
                                            }
                                        },
                                        "valid_daily": {
                                            "daily_start_hour": 0,
                                            "daily_start_minute": 0,
                                            "daily_end_hour": 0,
                                            "daily_end_minute": 0
                                        },
                                        "expiration_action": "SHOW_MESSAGE",
                                        "post_expiration_action": {
                                            "enable_credentials_renewal": True,
                                            "enable_delete_immediately": True,
                                            "delete_after_value": 0,
                                            "delete_after_unit": "MINUTE"
                                        }
                                    }
        default_delivery_settings = {
                                        "email_template_id": 0,
                                        "sms_template_id": 0
                                    }
        default_ssid = []

        users_config = user_group_profile.get('users_config')
        password_settings = user_group_profile.get('passwd_settings', default_password_settings)
        expiration_settings = user_group_profile.get('expiration_settings', default_expiration_settings)
        delivery_settings = user_group_profile.get('delivery_settings', default_delivery_settings)
        client_per_ppsk = user_group_profile.get("client_per_ppsk", False)
        pcg_use = user_group_profile.get("pcg_use", False)
        client_num = user_group_profile.get("client_num", 0)
        pcg_type = user_group_profile.get("pcg-type", "AP_BASED")

        # Part of the user_group_config
        user_group_config = user_group_profile.get('user_group_config', None)
        if user_group_config == None:
            kwargs['fail_msg'] = 'You must provide the user_group_profile[\'user_group_config\'] argument to this keyword'
            self.common_validation.fault(**kwargs)
            return -1
        password_db_loc = user_group_config.get('pass_db_loc', 'CLOUD')
        password_type = user_group_config.get('pass_type', 'PPSK')
        cwp_register = user_group_config.get("cwp_register", False)

        # Correct the data if needed
        if isinstance(password_settings, str) and password_settings.lower() == 'none':
            password_settings = default_password_settings

        if isinstance(expiration_settings, str) and expiration_settings.lower() == 'none':
            expiration_settings = default_expiration_settings

        if isinstance(delivery_settings, str) and delivery_settings.lower() == 'none':
            delivery_settings = default_delivery_settings

        xiqUserGroup = XiqUserGroup(id=1,
                                    create_time=time.time(),
                                    update_time=time.time(),
                                    org_id=None,
                                    name=group_name,
                                    description="Framwork xapi_create_user_group generated user group",
                                    predefined=False,
                                    password_db_location=password_db_loc,
                                    password_type=password_type,
                                    pcg_use_only=self.convertEnableDisableToBool(pcg_use),
                                    pcg_type=pcg_type,
                                    ppsk_use_only=self.convertEnableDisableToBool(client_per_ppsk),
                                    enable_cwp_reg=self.convertEnableDisableToBool(cwp_register),
                                    password_settings=password_settings,
                                    expiration_settings=expiration_settings,
                                    delivery_settings=delivery_settings,
                                    user_count=0,
                                    ssids=default_ssid,
                                    local_vars_configuration=None)

        try:
            # Create the group
            response = self.xapiBaseConfigurationUserManagementApi.xapi_base_create_user_group(xiq_create_user_group_request=xiqUserGroup, _preload_content=False)
            # Validate the reponse
            self.valid_http_response(response)
            # Conver the raw response to an object
            user_group_data =  self.convertPreloadContentDataToObject(response.data)
            # Get the user group ID
            user_group_id = user_group_data.id
            # Next add all of the users to the group
            base_user_template = {
                                  "user_group_id": user_group_id,
                                  "name": "",
                                  "user_name": "",
                                  "organization": "",
                                  "visit_purpose": "",
                                  "description": "",
                                  "email_address": "",
                                  "phone_number": "",
                                  "password": "",
                                  "email_password_delivery": "",
                                  "sms_password_delivery": ""
                                }

        except Exception as e:
            kwargs['fail_msg'] = f'Failed to create the user group -> {group_name} -> {e}'
            self.common_validation.fault(**kwargs)
            return -1



    def xapi_delete_user_group(self, user_group_name, **kwargs):
        """
            Will search for the user group and if found, delete it.

        :param user_group_name: The user group name (string)
        :return: 1 when the user group was deleted or nothing was found, otherwise -1 on error
        """
        try:
            user_group_list_preload = self.xapiBaseConfigurationUserManagementApi.xapi_base_list_user_groups(limit=100, _preload_content=False)
            user_group_list = self.convertPreloadContentDataToObject(user_group_list_preload.data)
            for user_group in user_group_list.data:
                if user_group_name == user_group.name:
                    response = self.xapiBaseConfigurationUserManagementApi.xapi_base_delete_user_group(id=user_group.id)
                    if response == -1:
                        kwargs['fail_msg'] = f'Failed to delete the user group {user_group_name}'
                        self.common_validation.failed(**kwargs)
                        return -1
            kwargs['pass_msg'] = f'Deleted the network policy -> {policies}'
            self.common_validation.passed(**kwargs)
            return 1
        except Exception as e:
            kwargs['fail_msg'] = f'Failed to delete the user group {user_group_name} Exception: {e}'
            self.common_validation.fault(**kwargs)
            return -1

