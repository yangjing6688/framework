from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimiotuserdevicesConstants import \
    GimiotuserdevicesConstants


class UiGimIOTUserDevicesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimIOTUserDevicesKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_IOT_USER_DEVICES
        self.command_const = GimiotuserdevicesConstants()

    def gim_dev_add_device(self, element_name, device_mac, device_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_mac]  -  Random mac address
        [device_name] -  Name of the Device

        This keyword is used for adding device with random mac address and device name
        """
        args = {"device_mac": device_mac,
                "device_name": device_name,
                }

        return self.execute_keyword(element_name, args, self.command_const.DEV_ADD_MAC_DEVICES, **kwargs)

    def gim_dev_select_device_type(self, element_name, ot_name, device_grp_name, device_type_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_grp_name] -    Device Group Name
        [ot_name] - OT name from drop down.

        This keyword is used for selecting device and sub type from drop down using provisioner login.
        """
        args = {"ot_name": ot_name,
                "device_grp_name": device_grp_name,
                "device_type_name": device_type_name
                }

        return self.execute_keyword(element_name, args, self.command_const.DEV_SELECT_DEVICE_TYPE, **kwargs)

    def gim_dev_verify_devices_added(self, element_name, device_mac, device_name, device_type, device_subtype,
                                     device_source, device_enabled, device_asset_type, device_ot, device_prv, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_mac] -  Device MAC
        [device_name] -   Device Name
        [device_type] -   Device Type
        [device_subtype] - Device subtype.
        [device_source] - Source
        [device_enabled] - Enabled or not
        [device_asset_type] - Asset type
        [device_ot] - OT of the device
        [device_prv] - Provisioner name

        This keyword is used for verifying devices added under device section from both admin and provisioner login.
        """
        args = {
            "device_mac": device_mac,
            "device_name": device_name,
            "device_type": device_type,
            "device_subtype": device_subtype,
            "device_source": device_source,
            "device_enabled": device_enabled,
            "device_asset_type": device_asset_type,
            "device_ot": device_ot,
            "device_prv": device_prv
        }

        return self.execute_keyword(element_name, args, self.command_const.DEV_VERIFY_DEVICE_ADDED, **kwargs)

    def gim_dev_create_device_using_self_provisioner(self, element_name, device_grp_name, device_type_name, de_mac,
                                                     **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_grp_name] -   Device group name
        [device_type_name] -  Device type
        [de_mac]: Device MAC

        This keyword is used for creating device and sub type from drop down from self provisioners.
        """
        args = {
            "device_grp_name": device_grp_name,
            "device_type_name": device_type_name,
            "de_mac": de_mac
        }

        return self.execute_keyword(element_name, args, self.command_const.DEV_CREATE_DEVICE_USING_SELF_PROVISIONER,
                                    **kwargs)

    def gim_dev_de_select_device_type(self, element_name, device_type_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_type_name] -  Device type

        This keyword is used for creating device and sub type from drop down from self provisioners.
        """
        args = {
            "device_type_name": device_type_name,
        }
        return self.execute_keyword(element_name, args, self.command_const.DEV_DE_SELECT_DEVICE_TYPE, **kwargs)

    def gim_dev_verify_only_selected_device_type_in_drop_down(self, element_name, device_type_name, summary, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_type_name]:  Device type

        This keyword is used for verifying the existence of device types from the device type drop down
        """
        args = {
            "device_type_name": device_type_name,
            "summary": summary
        }
        return self.execute_keyword(element_name, args, self.command_const.
                                    DEV_VERIFY_ONLY_SELECTED_DEVICE_TYPE_IN_DROP_DOWN, **kwargs)

    def gim_dev_verify_default_selected_device_types(self, element_name, device_type_name, summary, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_type_name] -  is used for verifying device type name from summary tab.
        [summary] - Summary of the device type

        This keyword is used for verifying the default selected device types
        """
        args = {
            "device_type_name": device_type_name,
            "summary": summary
        }

        return self.execute_keyword(element_name, args, self.command_const.DEV_VERIFY_DEFAULT_SELECTED_DEVICE_TYPES,
                                    **kwargs)

    def gim_dev_create_dev_validate_acc_validity(self, element_name, de_otname, device_mac, de_name, time,
                                                 change_no_change, change_time, error_no_error, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [de_otname] - OT name
        [device_mac] - Device MAC address
        [de_name] - Device Name
        [time] - Time
        [change_nochan] - Change or no change
        [change_time] - Change time
        [error_no_error] - Error no error

        This keyword is used to to validate device Account while creating
        """
        args = {"de_otname": de_otname,
                "device_mac": device_mac,
                "de_name": de_name,
                "time": time,
                "change_nochan": change_no_change,
                "change_time": change_time,
                "error_no_error": error_no_error
                }

        return self.execute_keyword(element_name, args, self.command_const.DEV_CREATE_DEV_VALIDATE_ACC_VALIDITY,
                                    **kwargs)

    def gim_dev_locale_register_devices(self, element_name, locale_name, with_authenticator, prv_un, prv_pwd,
                                        dev_mac, device_grp_name, device_type_name, click_ok, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [locale_name] - Name of the locale
        [with_authenticator] - Provisioner authenticator required?, if needed provide 'yes_with_authenticator'
        [prv_un] - Provisioner user name
        [prv_pwd] - provisioner password
        [dev_mac] - MAC address
        [device_grp_name] - Device group name
        [device_type_name] - Device type
        [click_ok] - if click on ok button, provide 'yes_click_ok'

        This keyword is used to enter the data while registering devices for localization
        """
        args = {"locale_name": locale_name,
                "with_authenticator": with_authenticator,
                "prv_un": prv_un,
                "prv_pwd": prv_pwd,
                "dev_mac": dev_mac,
                "device_grp_name": device_grp_name,
                "device_type_name": device_type_name,
                "click_ok": click_ok
                }

        return self.execute_keyword(element_name, args, self.command_const.DEV_LOCALE_REGISTER_DEVICES,
                                    **kwargs)

    def gim_dev_locale_error_success_validation(self, element_name, locale_selection, locale_name, submit,
                                                title_error, body_text, body_text_content, ok_button, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [locale_selection] -  If locale selection required, then add 'yes_locale_selection'
        [locale_name] - Name of the Locale
        [submit] - Submit button
        [title_error] - Title Error
        [body_text] - If body text validation required, then add 'yes_body text' validation
        [body_text_content] - Body Text Content
        [ok_button] - click on ok_button

        Validates the Success text after submit.
        """
        args = {"locale_selection": locale_selection,
                "locale_name": locale_name,
                "submit": submit,
                "title_error": title_error,
                "body_text": body_text,
                "body_text_content": body_text_content,
                "ok_button": ok_button
                }

        return self.execute_keyword(element_name, args, self.command_const.DEV_LOCALE_ERROR_SUCCESS_VALIDATION,
                                    **kwargs)

    def gim_dev_create_accessible_to_prov_options(self, element_name, de_otname, de_mac, name_yes_or_no, de_name,
                                                  source_option, static_source_value, error_or_no, device_limit,
                                                  source_yes_or_no, change_source, source_changed_name, asset,
                                                  asset_change, asset_change_type, dtg_option, dt_option,
                                                  admin_comment, admin_comment_value, doe_enable_disable, doe_option,
                                                  account_activation_type, acc_exp, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [de_otname] - Onboarding Template that needs to be selected from the dropdown.
        [de_mac] - MAC Address of the Device
        [name_yes_or_no] - Specifies whether Name should be entered or not
        [de_name] - Name of the Device
        [source_option] - validates the behavior for either of the following Source Options
                                a. Auto
                                b. Static
        [static_source_value] - Validates the Source value input by Provisioner.
        [error_or_no] - To handle the error conditions.
        [device_limit] - Number of Devices allowed to create per provisioner.
        [source_yes_or_no] - Validates the behavior when the Source is enabled and disabled.
        [change_source] - Specifies whether to change the source name or not.
        [source_changed_name] - Specifies to which name, Source needs to be changed.
        [asset] - Validates the behavior when Asset is enabled/disabled.
        [asset_change] - Specifies whether to change the asset type from device creation page.
        [asset_change_type] - To which type, asset needs to be changed between Permanent and Temporary.
        [dtg_option] - Device Type group needs to be included or not with the following options.
                        a. Mandatory
                        b. Optional
        [dt_option] - Device Type needs to be included or not with the following Options.
                        a. Mandatory
                        b. Optional
        [admin_comment] - Validates the change in Device creation page, if the admin comment is included.
        [admin_comment_value] - Validates the Admin Comment's value.
        [doe_enable_disable] - Validates the change in Device creation page,when the Delete on Expire is Enable/Disable.
        [doe_option] - Validates the Device Creation page for the following Delete on Expire Options.
                        a. Delete on Expire
                        b. Do Not Delete on Expire
        [account_activation_type] - Validates the change in Device creation page, for the following Account Activation
                                    options.
                                           a. TimeBased
                                           b. First Login
        [acc_exp] - Validates the change in Device creation page, is the account expiration is enabled/disabled.

        Validates the options available for provisioner and creates a device.
        """
        args = {"de_otname": de_otname,
                "de_mac": de_mac,
                "name_yes_or_no": name_yes_or_no,
                "de_name": de_name,
                "source_option": source_option,
                "static_source_value": static_source_value,
                "error_or_no": error_or_no,
                "device_limit": device_limit,
                "source_yes_or_no": source_yes_or_no,
                "change_source": change_source,
                "source_changed_name": source_changed_name,
                "asset": asset,
                "asset_change": asset_change,
                "asset_change_type": asset_change_type,
                "dtg_option": dtg_option,
                "dt_option": dt_option,
                "admin_comment": admin_comment,
                "admin_comment_value": admin_comment_value,
                "doe_enable_disable": doe_enable_disable,
                "doe_option": doe_option,
                "account_activation_type": account_activation_type,
                "acc_exp": acc_exp
                }

        return self.execute_keyword(element_name, args, self.command_const.DEV_CREATE_ACCESSIBLE_TO_PROV_OPTIONS,
                                    **kwargs)
