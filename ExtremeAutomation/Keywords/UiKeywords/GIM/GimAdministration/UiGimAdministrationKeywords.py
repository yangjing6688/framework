from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimadministrationConstants \
    import GimadministrationConstants


class UiGimAdministrationKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimAdministrationKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_ADMINISTRATION
        self.command_const = GimadministrationConstants()

    def gim_admin_pref_add_locale(self, element_name, flag_name, click_only_add, set_as_default, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against
        [flag_name] - Name of the flag
        [click_only_add] - clicks only add button from locale
        [set_as_default] - set as default, if needed provide 'yes_set_as_default'

        Adds the Locales under Preferences tab
        """
        args = {"flag_name": flag_name,
                "click_only_add": click_only_add,
                "set_as_default": set_as_default}

        return self.execute_keyword(element_name, args, self.command_const.ADMIN_PREF_ADD_LOCALE, **kwargs)

    def gim_admin_pref_del_locale(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Deletes all added Locales under Preferences tab
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ADMIN_PREF_DEL_LOCALE, **kwargs)

    def gim_admin_add_nac_appliance(self, element_name, nac_ip, xmc_un, xmc_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [nac_ip] - IP address of NAC
        [xmc_un] - Username of XMC
        [xmc_pwd] - Password of XMC

        Adding nac appliance in gim administration
        """
        args = {"nac_ip": nac_ip,
                "xmc_un": xmc_un,
                "xmc_pwd": xmc_pwd}

        return self.execute_keyword(element_name, args, self.command_const.ADMIN_ADD_NAC_APPLIANCE, **kwargs)

    def gim_admin_test_connection_nac_appliance_connection(self, element_name, entire_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [enter_text] - ip of the NAC

        To check GIM-NAC connection
        """
        args = {"entire_text": entire_text}

        return self.execute_keyword(element_name, args, self.command_const.
                                    GIM_ADMIN_TEST_CONNECTION_NAC_APPLIANCE_CONNECTION, **kwargs)

    def gim_admin_restore_default_nac_appliance_configuration(self, element_name, nac_ip, nac_ip2, xmc_un, xmc_pwd,
                                                              restore_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [nac_ip] - Primary NAC IP
        [nac_ip2] - Secondary NAC IP
        [xmc_un] - XMC user name
        [xmc_pwd] - XMC password
        [restore_text] - Restore Text

        Adding nac appliance in gim administration
        """
        args = {"nac_ip": nac_ip,
                "nac_ip2": nac_ip2,
                "xmc_un": xmc_un,
                "xmc_pwd": xmc_pwd,
                "restore_text": restore_text}

        return self.execute_keyword(element_name, args,
                                    self.command_const.GIM_ADMIN_RESTORE_DEFAULT_NAC_APPLIANCE_CONFIGURATION,
                                    **kwargs)

    def gim_admin_secondary_nac_appliance_configuration(self, element_name, nac_ip2, xmc_un, xmc_pwd, failed_text,
                                                        **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [nac_ip2] - Secondary NAC IP
        [xmc_un] - XMC user name
        [xmc_pwd] - XMC password
        [failed_text] - Failed Text

        Adding nac appliance in gim administration
        """
        args = {"nac_ip2": nac_ip2,
                "xmc_un": xmc_un,
                "xmc_pwd": xmc_pwd,
                "failed_text": failed_text}

        return self.execute_keyword(element_name, args,
                                    self.command_const.GIM_ADMIN_SECONDARY_NAC_APPLIANCE_CONFIGURATION, **kwargs)

    def gim_admin_add_radius(self, element_name, rad_port, rad_timeout, gim_secret, save, restore_to_defaults,
                             restore_rad_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [rad_port] - RADIUS port
        [rad_timeout] - RADIUS Timeout
        [gim_secret] - RADIUS secret
        [save] - Save or not
        [restore_to_defaults] - Restore to defaults
        [restore_rad_text] - Text after restore display

        Adding Radius shared secret ket  in gim administration
        """
        args = {"rad_port": rad_port,
                "rad_timeout": rad_timeout,
                "gim_secret": gim_secret,
                "save": save,
                "restore_to_defaults": restore_to_defaults,
                "restore_rad_text": restore_rad_text}

        return self.execute_keyword(element_name, args, self.command_const.ADMIN_ADD_RADIUS, **kwargs)

    def gim_administration_default_page_validation(self, element_name, troubleshooting_tab, notification_tab, ace_tab,
                                                   certificates_tab, back_restore_tab, preferences_tab,
                                                   account_tab, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [troubleshooting_tab] - Tab of Troubleshooting
        [notification_tab] - Tab of Notification
        [ace_tab] - Tab of Access Control Engine
        [certificates_tab] - Tab of Certificate
        [back_restore_tab] - Tabs of back up and restore
        [preferences_tab] - Tab of Preferences
        [account_tab] - Tab of Account

        This keyword is used for validating Administration default page
        """
        args = {"troubleshooting_tab": troubleshooting_tab,
                "notification_tab": notification_tab,
                "ace_tab": ace_tab,
                "certificates_tab": certificates_tab,
                "back_restore_tab": back_restore_tab,
                "preferences_tab": preferences_tab,
                "account_tab": account_tab}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMINISTRATION_DEFAULT_PAGE_VALIDATION,
                                    **kwargs)

    def gim_ace_page_validation(self, element_name, engine_tab, radius_tab, cert_tab, lic_tab, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [engine_tab] - Tab of Access Control engine
        [radius_tab]- Tab of RADIUS
        [cert_tab]- Tab of certificate
        [lic_tab]- Tab of License

        This keyword is used to validate Access Control Engine tab
        """
        args = {"engine_tab": engine_tab,
                "radius_tab": radius_tab,
                "cert_tab": cert_tab,
                "lic_tab": lic_tab}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ACE_PAGE_VALIDATION, **kwargs)

    def gim_admin_ace_tabs_page_validation(self, element_name, primary_engine, second_nac_engine, note, port,
                                           xmc_admin_username, xmc_admin_password, ace_status, save_button,
                                           test_button, restore_button, port_value, xmc_un, xmc_pwd, nac_ip,
                                           **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [nac_ip]: Primary NAC-Ipaddress
        [xmc_un] - Username of XMC
        [xmc_pwd] - Password of XMC
        [xmc_admin_username]- Username of XMC
        [xmc_admin_password]- Password of XMC
        [primary_engine]-Primary NAC-Ipaddress
        [second_nac_engine]- Secondary NAC -Ip-address
        [note]-Note: Secondary Engine must be in the same Engine Group as Primary Engine
        [port]-NAC port-8444
        [ace-status]- NAC connection Status
        [test_button]-Testing the NAC connectivity status
        [save-button]- Saves the ACE configuration
        [restore_button]- Restoring the Engine detail configuration.

        This keyword is used to validate Engine details under Access Control Engine

        """
        args = {"primary_engine": primary_engine,
                "second_nac_engine": second_nac_engine,
                "note": note,
                "port": port,
                "xmc_admin_username": xmc_admin_username,
                "xmc_admin_password": xmc_admin_password,
                "ace_status": ace_status,
                "save_button": save_button,
                "test_button": test_button,
                "restore_button": restore_button,
                "port_value": port_value,
                "xmc_un": xmc_un,
                "xmc_pwd": xmc_pwd,
                "nac_ip": nac_ip}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_ACE_TABS_PAGE_VALIDATION,
                                    **kwargs)

    def gim_admin_ace_radius_page_validation(self, element_name, radius_port, radius_port_value, radius_shared_secret,
                                             secret, radius_timeout, timeout_note, radius_note, save_button,
                                             restore_button, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [radius_port]- RADIUS Port
        [radius_port_value]-1812
        [radius_shared_secret]- RADIUS Shared Secret key
        [secret]-Shared Secret option
        [radius_timeout]- RADIUS connection timeout
        [timeout_note]-The IP address of the RADIUS service will be automatically retrieved.
                        Authentication request will be retried up to 3 times.
        [radius_note]-Note: In Engine Group, you must have a Guest & IoT Manager server record with the IP address
                    of the server that hosts Guest & IoT Manager. Provisioners cannot login without server record.
        [save_button]- Saving RADIUS configuration
        [restore_button]- Restoring the RADIUS configuration

        This keyword is used to validate RADIUS Page
        """
        args = {"radius_port": radius_port,
                "radius_port_value": radius_port_value,
                "radius_shared_secret": radius_shared_secret,
                "secret": secret,
                "radius_timeout": radius_timeout,
                "timeout_note": timeout_note,
                "radius_note": radius_note,
                "save_button": save_button,
                "restore_button": restore_button}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_ACE_RADIUS_PAGE_VALIDATION,
                                    **kwargs)

    def gim_admin_license_validation(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        This keyword is used to validate the License status
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_LICENSE_VALIDATION, **kwargs)

    def gim_admin_notification_page_validation(self, element_name, email_tab, sms_tab, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [email_tab]-   Guest User receives the notifications as email or SMS.
        [sms_tab]- SMS gateways and SMS providers - TAB consists of SMS gateways and SMS provider details

        This keyword is used to validate Notification TAB
        """
        args = {"email_tab": email_tab,
                "sms_tab": sms_tab}

        return self.execute_keyword(element_name, args,
                                    self.command_const.GIM_ADMIN_NOTIFICATION_PAGE_VALIDATION, **kwargs)

    def gim_admin_email_notification(self, element_name, from_address, email_server, email_notification, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [from_address]- Email Notification -Admn Email Address
        [email_server]- SMTP server Ip-address
        [email_notification] Enable Email Notification

        This keyword is used to enabling and restore Email Notification
        """
        args = {"from_address": from_address,
                "email_server": email_server,
                "email_notification": email_notification}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_EMAIL_NOTIFICATION, **kwargs)

    def gim_admin_email_page_validation(self, element_name, enable_notification, email_address, email_server,
                                        email_security, email_port, email_user_authentication, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [enable_notification]-Enable Sending of Email Notification
        [email_address]- Administrator email address for sending Guest user notification
        [email_server]- SMTP server ip-address
        [email_security]- SMTP -security level
        [email_port]- SMTP port --25
        [email_user_authentication]- Test user authentication

        This keyword is used to validate Email Notification page
        """
        args = {"enable_notification": enable_notification,
                "email_address": email_address,
                "email_server": email_server,
                "email_security": email_security,
                "email_port": email_port,
                "email_user_authentication": email_user_authentication}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_EMAIL_PAGE_VALIDATION, **kwargs)

    def gim_admin_test_email_notification(self, element_name, to_address, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [to_address]- To address of Email

        This keyword is used to test the given email address for sending.
        """
        args = {"to_address": to_address}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_TEST_EMAIL_NOTIFICATION, **kwargs)

    def gim_admin_validating_sms_gateways(self, element_name, phone_carrier, add_or_edit, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [phone_carrier]- Name of the phone carrier
        [add_or_edit]- Add or Edit validation

        This keyword is used to validate SMS tab page validation
        """
        args = {"phone_carrier": phone_carrier,
                "add_or_edit": add_or_edit}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_VALIDATING_SMS_GATEWAYS, **kwargs)

    def gim_admin_add_sms_gateway(self, element_name, phone_carrier, phone_gateway, pn_option, save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [phone_carrier]- Name of the SMS gateway
        [phone_gateway]- SMS gateway
        [pn_option]- Selecting Phone Number Category
        [save]- Saving the SMS gateway
        [sms]- SMS Provider

        This keyword is used to SMS gateways.
        """
        args = {"phone_carrier": phone_carrier,
                "phone_gateway": phone_gateway,
                "pn_option": pn_option,
                "save": save}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_ADD_SMS_GATEWAY, **kwargs)

    def gim_admin_change_sms_default_gateway(self, element_name, phone_carrier, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [phone_carrier]- Name of the SMS gateway

        This keyword is used to change sms default gateway
        """
        args = {"phone_carrier": phone_carrier}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_CHANGE_SMS_DEFAULT_GATEWAY,
                                    **kwargs)

    def gim_admin_delete_sms_gateway(self, element_name, phone_carrier, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [phone_carrier]- Name of the SMS gateway

        This keyword is used to delete sms
        """
        args = {"phone_carrier": phone_carrier}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_DELETE_SMS_GATEWAY, **kwargs)

    def gim_admin_add_sms_provider(self, element_name, phone_carrier, api_type, add_edit_delete, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [[phone_carrier]- Name of the SMS gateway
        [api_type]- Selecting REST or HTTP api type  for SMS provider
        [add_edit_delete] - Select Add, Edit and Delete buttons from SMS provider

        This keyword is used to Add, Delete and Edit custom SMS provider
        """
        args = {"phone_carrier": phone_carrier,
                "api_type": api_type,
                "add_edit_delete": add_edit_delete}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_ADD_SMS_PROVIDER, **kwargs)

    def gim_admin_account_settings_validation(self, element_name, admin_name, change_pwd, current_pwd, new_pwd,
                                              confirm_pwd, idle_timeout, idle_timevalue, idle_timeout_outlook,
                                              idle_outlook_value, account_note, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [admin_name]- Administrator Login username
        [change_pwd]- Changing the Default login password
        [current_pwd]- Current Admin Login password -admin
        [new_pwd]- Provide New admin login password ( Alpha, numeric, Special characters)
        [confirm_pwd]- Confirm new password
        [idle_timeout]- Admin Login page idle timeout
        [idle_timevalue]- Admin login page time value default 30 mins
        [idle_timeout_outlook]- Outlook Timeout value
        [Account_note]-Note: Existing sessions will need to be restarted for this change to take effect.
                            Idle timeout setting is for both Administrator and Provisioner

        This keyword is used to add engine details
        """
        args = {"admin_name": admin_name,
                "change_pwd": change_pwd,
                "current_pwd": current_pwd,
                "new_pwd": new_pwd,
                "confirm_pwd": confirm_pwd,
                "idle_timeout": idle_timeout,
                "idle_timevalue": idle_timevalue,
                "idle_timeout_outlook": idle_timeout_outlook,
                "idle_outlook_value": idle_outlook_value,
                "account_note": account_note}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_ACCOUNT_SETTINGS_VALIDATION,
                                    **kwargs)

    def gim_admin_edit_delete_sms_gateway(self, element_name, phone_carrier, phone_gateway, pn_option, action, save,
                                          **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [phone_carrier]- Name of the SMS Carrier, Ex:bell
        [phone_gateway]- Carrier/SMS gateway, Ex: tmobile.com
        [pn_option]- Selecting Phone Number Category from drop down
        [action] - Specify the type of action, edit or delete
        [save]- Saving the SMS gateway

        This keyword is used to edit or delete sms
        """
        args = {"phone_carrier": phone_carrier,
                "phone_gateway": phone_gateway,
                "pn_option": pn_option,
                "action": action,
                "save": save}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_EDIT_DELETE_SMS_GATEWAY, **kwargs)

    def gim_admin_sms_gateway_should_not_exist(self, element_name, phone_carrier, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [phone_carrier]- Name of the phone carrier

        This keyword is used to validate deleted SMS should not exist
        """
        args = {"phone_carrier": phone_carrier}

        return self.execute_keyword(element_name, args, self.command_const.GIM_ADMIN_SMS_GATEWAY_SHOULD_NOT_EXIST,
                                    **kwargs)
