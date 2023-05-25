import os
import re
from robot.libraries.BuiltIn import BuiltIn
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.Cli import Cli
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.WirelessCWPWebElements import WirelessCWPWebElements
from extauto.common.CommonValidation import CommonValidation


class WirelessCaptiveWebPortal(WirelessCWPWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.screen = Screen()
        self.cli = Cli()
        self.auto_actions = AutoActions()
        self.custom_file_dir = os.getcwd() + '/custom_cwp_pages/'
        self.common_validation = CommonValidation()

    def _config_approver_email_domain_list(self, domain):
        """
        - check the approver domain list exist in the grid.
        - if it is not present add the approver domain list.

        :param domain: (str) domain name
        :return: 1
        """
        for row in self.get_approve_email_domain_list_rows():
            if cell := self.get_approve_email_domain_list_row_cell(row):
                if cell.text.upper() == domain.upper():
                    self.utils.print_info("Domain already exists")
                    return 1

        self.utils.print_info("Click on the domain add button")
        self.auto_actions.click_reference(self.get_approve_email_domain_list_add_button)
        sleep(2)

        self.utils.print_info(f"Enter the approve email domain:{domain}")
        self.auto_actions.send_keys(self.get_approve_email_domain_list_domain_name(), domain)

        self.utils.print_info("Click on the domain list add button")
        self.auto_actions.click_reference(self.get_approve_email_domain_list_domain_add_button)
        return 1

    def _config_cwp_ppsk_settings(self, **ppsk_settings):
        """
        - Configure cwp PPSK settings, for below two combination of cwp options
        - "Enable Self-Registration" and "Return Aerohive Private PSK"
        - need to select the "Access SSID" and "PPSK Server" under new cwp creation window

        :param ppsk_settings: (dict) cwp_ppsk setting
        :return: None
        """
        self.utils.print_info("Click on choose access ssid drop down")
        self.auto_actions.click_reference(self.get_choose_access_ssid_drop_down)
        sleep(2)

        self.utils.print_info(f"Selecting access ssid:{ppsk_settings['choose_access_ssid']}")
        self.auto_actions.select_drop_down_options(self.get_choose_access_ssid_options(), ppsk_settings['choose_access_ssid'])

        self.utils.print_info("Click choose ppsk server drop down")
        self.auto_actions.click_reference(self.get_choose_a_ppsk_server_drop_down)
        sleep(2)

        self.utils.print_info(f"Selecting ppsk server:{ppsk_settings['choose_ppsk_server']}")
        self.auto_actions.select_drop_down_options(self.get_choose_a_ppsk_server_options(), ppsk_settings['choose_ppsk_server'])

        if ppsk_settings['employee_approval'].upper() == "ENABLE":
            self.auto_actions.enable_radio_button(self.get_employee_approval_radio_button())

            self.utils.print_info("Configure Approver email domain list ")
            self._config_approver_email_domain_list(ppsk_settings['domain'])
        else:
            self.auto_actions.disable_radio_button(self.get_employee_approval_radio_button())

    def _add_self_reg_user_auth_cwp(self, **open_cwp_config):
        """
        - Adding open network cwp with "Enable Self-Registration" and "User Auth on Captive Web Portal"
        - If cwp already created select it from select window otherwise create it

        :param open_cwp_config: (dict) cwp parameters
        :return: 1 if added else -1
        """
        cwp_name = open_cwp_config.get('captive_web_portal_name')
        employee_approval = open_cwp_config.get('employee_approval')
        customize_and_preview = open_cwp_config.get('customize_and_preview')
        auth_method = open_cwp_config.get('auth_method')

        self.utils.print_info(f"Check the cwp: {cwp_name}  already exists")
        if self._select_default_captive_web_portal(cwp_name):
            return 1

        self.utils.print_info("Click on default cwp add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)
        sleep(2)

        self.utils.print_info(f"Enter cwp name:{cwp_name}")
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), cwp_name)

        if employee_approval and employee_approval.upper() == "ENABLE":
            self.auto_actions.enable_radio_button(self.get_employee_approval_radio_button())
            self.utils.print_info("Configure Approver email domain list ")
            self._config_approver_email_domain_list(open_cwp_config['domain'])
        else:
            self.auto_actions.disable_radio_button(self.get_employee_approval_radio_button())

        if customize_and_preview and customize_and_preview.upper() == "ENABLE":
            self.utils.print_info("Click on customise and preview button")
            self.auto_actions.click_reference(self.get_customise_and_preview_button)
            self.utils.print_info("Click on authentication drop down")
            self.auto_actions.click_reference(self.get_auth_method_drop_down)
            self.utils.print_info(f"select the authentication method:{auth_method}")
            self.auto_actions.select_drop_down_options(self.get_auth_method_drop_down_options(), auth_method)

        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)
        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "Update the highlighted errors below" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -1
        return 1

    def _add_self_reg_return_aerohive_ppsk_cwp(self, **open_cwp_config):
        """
        - Adding the open network cwp with "Enable Self-Registration" and "Return Aerohive Private PSK"
        - If cwp already created select it from select window otherwise create it

        :param open_cwp_config: (dict) cwp parameters
        :return: 1 if added else -1
        """
        cwp_name = open_cwp_config.get('captive_web_portal_name')
        ppsk_settings = open_cwp_config.get('ppsk_settings')

        self.utils.print_info(f"Check the cwp: {cwp_name}  already exists")
        if self._select_default_captive_web_portal(cwp_name):
            return 1

        self.utils.print_info("Click on default cwp add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)
        sleep(2)

        self.utils.print_info(f"Enter cwp name:{cwp_name}")
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), cwp_name)

        self.utils.print_info("config ppsk settings")
        self._config_cwp_ppsk_settings(**ppsk_settings)
        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "Update the highlighted errors below" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -1
        return 1

    def _select_unselect_captive_web_portal_options(self, **options):
        """
        - Select and unselect the below checkbox under captive web portal
        - User Auth on Captive Web Portal, Enable Self-Registration, Return Aerohive Private PSK, Enable UPA

        :param options: (dict) cwp options combination
        :return: True if selected else False
        """
        enable_self_reg = options.get('enable_self_reg')
        return_aerohive_private_psk = options.get('return_aerohive_private_psk')
        enable_upa = options.get('enable_upa')
        user_auth_on_captive_web_portal = options.get('user_auth_on_captive_web_portal')

        self.utils.wait_till(self.get_enable_upa, delay=2, timeout=8, is_logging_enabled=True)
        if enable_upa.upper() == "ENABLE":
            self.utils.print_info("Select the enable upa check box")
            self.auto_actions.enable_check_box(self.get_enable_upa())
        else:
            self.utils.print_info("Un select the enable upa check box")
            self.auto_actions.disable_check_box(self.get_enable_upa())

        sleep(2)
        if enable_self_reg.upper() == "ENABLE":
            self.utils.print_info("Select the enable self registration check box")
            self.auto_actions.enable_check_box(self.get_enable_self_registration())
        else:
            self.utils.print_info("un select the enable self registration check box")
            self.auto_actions.disable_check_box(self.get_enable_self_registration())

        if user_auth_on_captive_web_portal.upper() == "ENABLE":
            self.utils.print_info("Select auth on captive web portal")
            self.auto_actions.enable_check_box(self.get_user_auth_on_captive_web_portal())
        else:
            self.utils.print_info("Un select auth on captive web portal")
            self.auto_actions.disable_check_box(self.get_user_auth_on_captive_web_portal())

        if return_aerohive_private_psk.upper() == "ENABLE":
            self.utils.print_info("select Return Aerohive private psk check box")
            self.auto_actions.enable_check_box(self.get_return_aerohive_private_psk())
        else:
            self.utils.print_info("un select Return Aerohive private psk check box")
            self.auto_actions.disable_check_box(self.get_return_aerohive_private_psk())

        sleep(3)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "This combination is not supported" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return False
        return True

    def _select_social_login_type(self, social_login_type):
        """
        Select social login types ie Facebook or google or Linkedin

        :param social_login_type: (str) social_login_type
        :return: 1 selected else -1
        """
        self.utils.print_info("selecting Social Login type for cloud CWP wireless network")
        if social_login_type.upper() == "FACEBOOK":
            self.auto_actions.click_reference(self.get_cloud_cwp_social_login_type_fb)
            return 1
        elif social_login_type.upper() == "GOOGLE":
            self.auto_actions.click_reference(self.get_cloud_cwp_social_login_type_google)
            return 1
        elif social_login_type.upper() == "LINKEDIN":
            self.auto_actions.click_reference(self.get_cloud_cwp_social_login_type_linkedin)
            return 1
        else:
            return -1

    def _config_cloud_social_cwp_open_nw(self, **social_login_config):
        """
        - Config the cloud social captive web portal
        - Configure the cwp based on social type Ex: Facebook, Linkdin, Google

        :param social_login_config: (dict) configuration parameters
        :return: 1 if success else -1
        """

        social_cwp_name = social_login_config.get('cloud_cwp_name')
        social_cwp_config = social_login_config.get('social_cwp_config')

        login_type = social_cwp_config.get('social_login_type')
        restrict_access_domain = social_cwp_config.get('restrict_access')
        auth_cache_duration = social_cwp_config.get('auth_cache_duration')

        self.utils.print_info("Click on default CWP add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)
        sleep(2)

        self.utils.print_info(f"Enter CWP name: {social_cwp_name}")
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), social_cwp_name)

        self.utils.print_info(f"Selecting Social Login Type: {login_type}")
        self._select_social_login_type(login_type)

        if restrict_access_domain.upper() != "DEFAULT":
            self.utils.print_info("Enter Restrict Domain Name")
            self.auto_actions.send_keys(self.get_cloud_cwp_restrict_domain_field(), restrict_access_domain)
            sleep(2)

        if auth_cache_duration.upper() != "DEFAULT":
            self.utils.print_info("Enter Cache Duration in Minutes")
            self.auto_actions.send_keys(self.get_cloud_cwp_cache_duration_field(), auth_cache_duration)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(3)

        self.utils.print_info("Click CWP save button")
        self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)

        self.screen.save_screen_shot()
        sleep(3)

        if self.get_cwp_error_message():
            tool_tp_text = self.get_cwp_error_message().text
            if "The authentication cache duration must not exceed 30 days" in tool_tp_text:
                self.utils.print_info(f"{tool_tp_text}")

                self.utils.print_info("Click CWP Cancel button")
                self.auto_actions.click_reference(self.get_default_cwp_add_dialog_cwp_cancel_cwp_button)

                self.utils.print_info("Click Cancel wireless network button")
                self.auto_actions.click_reference(self.get_cwp_wireless_network_cancel_button)
                return -1
        return 1

    def _select_default_captive_web_portal(self, cwp_name):
        """
        Select default CWP from select menu

        :param cwp_name: (str) CWP name to select from select window
        :return: True if selected else False
        """
        self.utils.print_info("Click on default CWP select button")
        self.auto_actions.scroll_down()
        sleep(2)

        self.auto_actions.click_reference(self.get_default_cwp_select_button)
        sleep(2)

        if not self.get_default_select_window_cwp_rows():
            self.utils.print_info(f"default CWP: {cwp_name} does't exist, Please create default cwp")
            self.auto_actions.click_reference(self.get_default_cwp_select_window_cancel_button)
            sleep(2)
            return False

        for row in self.get_default_select_window_cwp_rows():
            if cwp_name.upper() in row.text.upper():
                self.auto_actions.click(self.get_default_cwp_select_window_row_select_check_box(row))
                sleep(2)
                self.auto_actions.click_reference(self.get_default_cwp_select_window_select_button)
                return True

        self.utils.print_info(f"default CWP: {cwp_name} does't exist, Please create default cwp")
        self.auto_actions.click_reference(self.get_default_cwp_select_window_cancel_button)
        sleep(2)
        return False

    def create_cloud_social_login_cwp(self, **social_cwp_profile):
        """
        - This keyword is used to create the cloud social login type CWP
        - There are two ways to call this method
        - 1. called by create_open_network_captive_web_portal
        - 2. standalone call. for this pre-condition is already navigated to the wireless network tab
        - Keyword Usage:
        - ``Create Cloud Social Login CWP  &{SOCIAL_LOGIN_CWP_PROFILE}``
        - For creation of different combination &{SOCIAL_LOGIN_CWP_PROFILE} dict refer social_login_config.robot

        :param social_cwp_profile: (dict) configuration profile
        :return: 1 if created else -1
        """
        social_login_config = social_cwp_profile.get('open_cwp_config')
        social_cwp_name = social_login_config.get('cloud_cwp_name')

        self.utils.print_info("Enable captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal())
        sleep(5)

        self.utils.print_info("Enable Cloud captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_cloud_cwp_radio_button())

        self.utils.print_info("Enable Social Login radio button")
        self.auto_actions.enable_radio_button(self.get_social_login_radio_button())

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info(f"Check the CWP: {social_cwp_name}  already exists")
        if self._select_default_captive_web_portal(social_cwp_name):
            return 1

        return self._config_cloud_social_cwp_open_nw(**social_login_config)

    def create_cloud_social_login_ege(self, **social_cwp_profile):
        """
        - This keyword is used to create the guest social login type eguest
        - There are two ways to call this method
        - 1. called by create_open_network_captive_web_portal
        - 2. standalone call. for this pre-condition is already navigated to the wireless network tab
        - Keyword Usage:
        - ``Create Cloud Social Login EGE  &{SOCIAL_LOGIN_CWP_PROFILE}``

        :param social_cwp_profile: (dict) configuration profile
        :return: 1 if created else -1
        """
        wall_garden_profile = social_cwp_profile.get('wall_garden_profile')
        social_profile_web_obj = wall_garden_profile.get('web_objs')


        self.utils.print_info("Click Walled Garden Add button")
        self.auto_actions.click_reference(self.get_walled_garden_add_button)
        sleep(5)

        self.utils.print_info("Adding Walled Garden Web Objects")
        self.auto_actions.send_keys(self.get_walled_garden_text_area(), social_profile_web_obj)

        self.utils.print_info("Click Walled Garden Text Add button")
        self.auto_actions.click_reference(self.get_walled_garden_text_add_button)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

    def _add_user_auth_on_captive_web_portal(self, **open_cwp_config):
        """
        - create the user authentication CWP
        - If CWP already created select it from select window other wise create it
        :param open_cwp_config: configuration dict
        :return:
        """
        cwp_name = open_cwp_config.get('captive_web_portal_name')
        customize_and_preview = open_cwp_config.get('customize_and_preview')
        auth_method = open_cwp_config.get('auth_method')

        self.utils.print_info(f"Check the cwp: {cwp_name}  already exists")
        if self._select_default_captive_web_portal(cwp_name):
            return 1

        self.utils.print_info("Click on default cwp add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)

        self.utils.wait_till(self.get_default_cwp_name_field, delay=2, timeout=8, is_logging_enabled=True)
        self.utils.print_info(f"Enter CWP name:{cwp_name}")
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), cwp_name)

        if customize_and_preview.upper() == "ENABLE":
            self.utils.print_info("Click on customise and preview button")
            self.auto_actions.click_reference(self.get_customise_and_preview_button)
            self.utils.print_info("Click on authentication drop down")
            self.auto_actions.click_reference(self.get_auth_method_drop_down)
            self.utils.print_info(f"select the authentication method:{auth_method}")
            self.auto_actions.select_drop_down_options(self.get_auth_method_drop_down_options(), auth_method)
        self.utils.print_info("Click Save CWP button")
        self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)

        sleep(3)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "Update the highlighted errors below" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -1
        return 1

    def _add_user_auth_return_aerohive_ppsk(self, **open_cwp_config):
        """
        - Create cwp with "User Auth on Captive Web Portal" and "Return Aerohive Private PSK" options
        - If CWP already created select it from select window otherwise create it
        :param open_cwp_config:
        :return:
        """
        cwp_name = open_cwp_config.get('captive_web_portal_name')
        import_html = open_cwp_config.get('import_html', 'Disable')

        self.utils.print_info(f"Check the cwp: {cwp_name}  already exists")
        if self._select_default_captive_web_portal(cwp_name):
            return 1

        self.utils.print_info("Click on default cwp add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)
        sleep(2)

        self.utils.print_info(f"Enter cwp name:{cwp_name}")
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), cwp_name)

        if import_html.upper() == "ENABLE":
            self.utils.print_info("click on import html button")
            self.auto_actions.click_reference(self.get_import_html_button)
            self.screen.save_screen_shot()

            if open_cwp_config.get('download_samples') == 'download':
                self.utils.print_info("click on the User-Auth-Return-PPSK-Example download link")
                if self.get_user_auth_return_ppsk_link():
                    self.auto_actions.click_reference(self.get_user_auth_return_ppsk_link)
                    self.screen.save_screen_shot()
                    # @to do Need to add the import logic just checking download the html pages
                    sleep(2)
                    self.auto_actions.click_reference(self.get_cwp_dialog_window_cancel_button)
                    self.screen.save_screen_shot()
                    return 1
                else:
                    self.utils.print_info("user auth return ppsk example link not present")
                    return -1

    def create_default_captive_web_portal(self, **cwp_config):
        """
        - This keyword is used to create the default captive web portal with below combinations
        - "User Auth on Captive Web Portal", "Enable Self-Registration", "Return Aerohive Private PSK",
          "Enable UPA"
        - There are two way to call this keyword
        - 1. called by create_open_network_captive_web_portal
        - 2. standalone, Assumption is already navigated to the wireless network tab
        - Keyword Usage:
        - ``Create Default Captive Web Portal  &{DEFAULT_CWP_CONFIG}``

        :param cwp_config: (dict) captive web portal config parameters
        :return: 1 if config success else -1
        """

        user_auth_on_captive_web_portal = cwp_config.get("user_auth_on_captive_web_portal")
        enable_self_reg = cwp_config.get("enable_self_reg")
        return_aerohive_ppsk = cwp_config.get("return_aerohive_private_psk")
        auth_with_extcldiq_service = cwp_config.get("auth_with_extcldiq_service", "Disable")

        self.utils.print_info("Enable 'Enable Captive Web Portal' radio button")
        self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal())

        self.utils.wait_till(self.get_enable_captive_web_portal_cwp_radio_button, delay=2, timeout=8, is_logging_enabled=True)
        self.utils.print_info("Enable captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal_cwp_radio_button())

        self.utils.print_info("select and unselect the various options under cwp")
        if not self._select_unselect_captive_web_portal_options(**cwp_config):
            self.utils.print_info("Please select the valid captive web portal options")
            return -1

        self.screen.save_screen_shot()
        sleep(2)

        if auth_with_extcldiq_service.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_wir_auth_with_extiq_auth_service_slider_button())
            sleep(2)

        if enable_self_reg.upper() == 'ENABLE' and return_aerohive_ppsk.upper() == "ENABLE":
            return self._add_self_reg_return_aerohive_ppsk_cwp(**cwp_config['open_cwp_config'])

        if enable_self_reg.upper() == 'ENABLE' and user_auth_on_captive_web_portal.upper() == 'ENABLE':
            return self._add_self_reg_user_auth_cwp(**cwp_config['open_cwp_config'])

        if user_auth_on_captive_web_portal.upper() == 'ENABLE' and return_aerohive_ppsk.upper() == "ENABLE":
            return self._add_user_auth_return_aerohive_ppsk(**cwp_config['open_cwp_config'])

        if user_auth_on_captive_web_portal.upper() == "ENABLE":
            return self._add_user_auth_on_captive_web_portal(**cwp_config['open_cwp_config'])

    def create_open_network_captive_web_portal(self, **cwp_profile):
        """
        - If Authentication type is open, below are ways to create the CWP
        - default captive web portal
        - This consists of below 4 options
            User Auth on Captive Web Portal
            Enable Self-Registration
            Return Aerohive Private PSK
            Enable UPA

        - cloud captive web portal
        - It consists Social Login CWP, Cloud Pin CWP
        - Based on passed cwp-profile dict create the cwp for open network
        - Assumes that already navigated to the wireless network page
        - Keyword Usage:
        - ``Create Open Network Captive Web Portal    &{CWP_PROFILE}``
        - For &{CWP_PROFILE} creation refer social_login_config.robot, cloud_pin_config.robot

        :param cwp_profile: (dict) configuration profile dictionary
        :return: 1 if created else -1
        """
        enable_cwp = cwp_profile.get('enable_cwp')
        cloud_captive_web_portal = cwp_profile.get('cloud_captive_web_portal', 'Disable')
        captive_web_portal = cwp_profile.get('captive_web_portal', 'DISABLE')
        guest_essential = cwp_profile.get('enable_ege', 'DISABLE')

        if enable_cwp and enable_cwp.upper() == "DISABLE":
            self.auto_actions.disable_radio_button(self.get_enable_captive_web_portal())
            return 1

        if cloud_captive_web_portal and cloud_captive_web_portal.upper() == "ENABLE":
            if cwp_profile['social_login'].upper() == "ENABLE":
                return self.create_cloud_social_login_cwp(**cwp_profile)

            if cwp_profile['request_pin'].upper() == 'ENABLE':
                return self.create_cloud_pin_cwp(**cwp_profile)

        if captive_web_portal and captive_web_portal.upper() == "ENABLE":
            return self.create_default_captive_web_portal(**cwp_profile)

        if guest_essential and guest_essential.upper() == "ENABLE":
            self.auto_actions.enable_radio_button(self.get_enable_extreme_guest_essentials_slide_button())
            sleep(2)
            if 'wall_garden_profile' in cwp_profile.keys():
                self.create_cloud_social_login_ege(**cwp_profile)
            return 1

    def _add_default_cwp_wireless_network(self, cwp_name):
        """
        For auth type enterprise or ppsk, add the default captive web portal

        :param cwp_name: (str) captive web portal name
        :return: 1
        """
        self.utils.print_info("Click on default CWP add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)
        sleep(2)

        self.utils.print_info("Enter CWP name:{}".format(cwp_name))
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), cwp_name)

        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Click CWP save button")
        self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "The Captive Web Portal cannot be saved because the name" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -1
        return 1

    def _add_user_authentication_on_cwp(self, cwp_name, auth_method, **kwargs):
        """
        For auth type personal(psk), add user authentication on captive web portal

        :param cwp_name: (str) captive web portal name
        :param auth_method: (str) 'PAP', 'CHAP', or 'MS-CHAP V2'
        :return: 1 if created else -1
        """
        try:
            self.utils.print_info("Click on CWP add button")
            self.auto_actions.click_reference(self.get_default_cwp_add_button)
            self.utils.wait_till(self.get_default_cwp_name_field, delay=2, timeout=6, is_logging_enabled=True)
            self.utils.print_info("Enter CWP name:{}".format(cwp_name))
            self.auto_actions.send_keys(self.get_default_cwp_name_field(), cwp_name)
            self.utils.print_info(f"Click on authentication method dropdown: {auth_method}")
            self.auto_actions.click_reference(self.get_auth_method_drop_down)
            self.auto_actions.select_drop_down_options(self.get_auth_method_drop_down_options(), auth_method)

            self.screen.save_screen_shot()
            sleep(2)
            self.utils.print_info("Click CWP save button")
            self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)

            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            for tip_text in tool_tp_text:
                if "The Captive Web Portal cannot be saved because the name" in tip_text:
                    kwargs['fail_msg'] = f"Unable to _add_user_authentication_on_cwp(): {tip_text}"
                    self.common_validation.failed(**kwargs)
                    return -1

            kwargs['pass_msg'] = "Successfully able to _add_user_authentication_on_cwp()"
            self.common_validation.passed(**kwargs)
            return 1

        except Exception as e:
            kwargs['fail_msg'] = f"Unable to _add_user_authentication_on_cwp(): {e}"
            self.common_validation.failed(**kwargs)
            return -1

    def create_ppsk_wireless_network_cwp(self, **cwp_config):
        """
        - Create captive web portal for  PPSK wireless network
        - This is called as part of PPSK wireless network creation
        - For standalone call assumes that already navigated to the wireless network page, selected the PPSK auth type
        - Keyword Usage:
        - ``Create PPSK Wireless Network CWP    &{CWP_CONFIG}``

        :param cwp_config: (dict) configuration
        :return: 1 if created else -1
        """
        enable_cwp = cwp_config.get('enable_cwp').upper()
        cwp_name = cwp_config.get('cwp_name')

        if enable_cwp.upper() == "DISABLE":
            self.auto_actions.disable_radio_button(self.get_enable_captive_web_portal())
            return 1

        self.utils.print_info("Enable captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal())
        sleep(5)

        self.utils.print_info(f"Check the CWP: {cwp_name}  already exists")
        if self._select_default_captive_web_portal(cwp_name):
            return 1
        return self._add_default_cwp_wireless_network(cwp_name)

    def create_enterprise_wireless_network_cwp(self, **cwp_config):
        """
        - Create captive web portal for enterprise wireless network
        - This is called as part of enterprise wireless network creation
        - For standalone call assumes that already navigated to the wireless network page,
          selected the enterprise auth type
        - Keyword Usage:
        - ``Create Enterprise Wireless Network Cwp    &{CWP_CONFIG}``

        :param cwp_config: (dict) configuration
        :return: 1 if created else -1
        """
        enable_cwp = cwp_config.get('enable_cwp').upper()
        cwp_name = cwp_config.get('cwp_name')

        if enable_cwp.upper() == "DISABLE":
            self.auto_actions.disable_radio_button(self.get_enable_captive_web_portal())
            return 1

        self.utils.print_info("Enable captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal())
        sleep(5)

        self.utils.print_info(f"Check the CWP: {cwp_name}  already exists")
        if self._select_default_captive_web_portal(cwp_name):
            return 1
        return self._add_default_cwp_wireless_network(cwp_name)

    def _select_customise_success_page(self, success_page):
        """
        Select the customise success page

        :param success_page: success page html
        :return:
        """
        self.utils.print_info("Click on success page drop down")
        self.auto_actions.click_reference(self.get_customise_success_page_drop_down)
        sleep(2)

        options = self.get_customise_success_page_drop_down_options()
        self.auto_actions.select_drop_down_options(options, success_page)
        return 1

    def _select_customise_login_page(self, login_page):
        """
        Select the customise login page

        :param login_page: login page html
        :return:
        """
        self.utils.print_info("Click on login page drop down")
        self.auto_actions.click_reference(self.get_customise_login_page_drop_down)
        sleep(2)

        options = self.get_customise_login_page_drop_down_option()
        self.auto_actions.select_drop_down_options(options, login_page)
        return 1

    def _manage_customise_pages(self, upload_files):
        """
        upload the customized cwp html files from xiq/functional/custom_cwp_pages folder
        example: file /xiq/functional/custom_cwp_pages/aerohive.svg

        :param upload_files: (list) absolute file path of the html pages
        :return: None
        """
        self.utils.print_info("Click on manage files upload/remove button")
        self.auto_actions.scroll_down()
        sleep(2)
        self.auto_actions.click_reference(self.get_manage_upload_remove_files)
        sleep(2)

        self.utils.print_info("Uploading the customized html files")
        for file in upload_files:
            self.utils.print_info(file)
            upload_file = self.custom_file_dir + file
            self.auto_actions.send_keys(self.get_manage_file_choose_field(), upload_file)
            sleep(1)

        self.utils.print_info("Click on customise choose files window done button")
        self.auto_actions.click_reference(self.get_manage_file_choose_done_button)
        sleep(2)

    def _select_web_file_directory(self, directory_name):
        """
        Select the customise cwp file directory

        :param directory_name:  name of the directory to create
        :return:
        """
        # @to do change the random generation of directory file once able to delete the directory from GUI

        self.utils.print_debug("Directory name ", directory_name)
        self.utils.print_info("Create Web file directory")
        directory_name = self.utils.get_random_string()
        self._create_web_file_directory(directory_name)

        self.utils.print_info("Click on web file directory drop down")
        self.auto_actions.click_reference(self.get_web_file_directory_drop_down)
        sleep(2)
        options = self.get_web_file_directory_drop_down_options()
        self.auto_actions.select_drop_down_options(options, directory_name)
        return 1

    def _create_web_file_directory(self, directory_name):
        """
        Create the web file directory to store the customized cwp pages

        :param directory_name: directory name
        :return: 1
        """
        self.utils.print_info("Click on web file directory create button")
        self.auto_actions.click_reference(self.get_create_web_file_directory)
        sleep(2)

        self.utils.print_info("Enter the directory name:{}".format(directory_name))
        self.auto_actions.send_keys(self.get_directory_name(), directory_name)

        self.utils.print_info("Click on web directory create button")
        self.auto_actions.click_reference(self.get_web_file_directory_create_button)
        sleep(2)

        self.utils.print_info("Click on web directory create done button")
        self.auto_actions.click_reference(self.get_web_file_directory_create_done_button)
        sleep(2)
        return 1

    def _config_cloud_pin_custom_cwp(self, **custom_settings):
        """
        Configure the customized captive web portal

        :param custom_settings: customised web cwp config parameters
        :return:
        """
        directory_name = custom_settings.get('directory_name')
        upload_files = custom_settings.get('upload_files')
        self.utils.print_info("Click on customize CWP radio button")
        if not self.get_customise_cwp_setting().is_selected():
            self.auto_actions.click_reference(self.get_customise_cwp_setting)
            sleep(2)

        self.auto_actions.scroll_down()
        sleep(2)

        self.utils.print_info("Select Web file directory")
        self._select_web_file_directory(directory_name)

        self.utils.print_info("Add customise CWP files")
        self._manage_customise_pages(upload_files)

        self.utils.print_info("select the login page")
        self._select_customise_login_page('index.html')

        self.utils.print_info("select the success page")
        self._select_customise_success_page('login.html')

        if self.get_failure_page_container().is_displayed():
            self.utils.print_info("For Cloud PIN Custom Pages Failure page section should not be there")
            return -1
        return 1

    def _config_daily_report_delivery_time(self, time_hour='1', time_minutes='15'):
        """
        - select the daily report delivery time based on passed time in hour, minute

        :param time_hour: time in hour to select
        :param time_minutes: time in minute to select
        :return:
        """

        self.auto_actions.click_reference(self.get_daily_report_delivery_time_hour_drop_down)
        sleep(2)

        self.utils.print_info("Select hour:{}".format(time_hour))
        options = self.get_daily_report_delivery_time_hour_options()
        self.auto_actions.select_drop_down_options(options, time_hour)

        self.auto_actions.click_reference(self.get_daily_report_delivery_time_minutes_drop_down)
        sleep(2)

        self.utils.print_info("Select minutes:{}".format(time_minutes))
        options = self.get_daily_report_delivery_time_minutes_options()
        self.auto_actions.select_drop_down_options(options, time_minutes)

    def _config_daily_report_email_addr(self, email):
        """
        Config the daily report email address field

        :param email: email address to send daily report
        :return:
        """
        self.utils.print_info("EMAIL for daily report delivery:{}".format(email))
        self.auto_actions.send_keys(self.get_email_address_daily_report_field(), email)

    def _config_pin_valid_time(self, pin_time='1 Hour'):
        """
        configure validity hour of the generated PIN

        :param pin_time: time in hour
        :return:
        """
        self.auto_actions.click_reference(self.get_valid_pin_time_drop_down)
        sleep(2)

        self.utils.print_info("PIN Valid time:{}".format(pin_time))
        options = self.get_valid_pin_time_option()
        self.auto_actions.select_drop_down_options(options, pin_time)

    def _get_report_delivery_time(self, report_time_delta):
        """
        - Read the Current Report Delivery time defined in test case level.
        - If it is not defined in test case level , get the current utc time.
        - Get the delivery report time in hour and minute

        :param report_time_delta:  time delta in minutes
        :return: hour, minute
        """
        delivery_time = BuiltIn().get_variable_value('${REPORT_DELIVERY_TIME}')
        if delivery_time:
            time_ = re.search(r'(\d+):(\d+)', delivery_time)

        else:
            cur_utc_time = self.utils.get_utc_time()
            deliver_time = self.utils.get_utc_minute_time_delta(cur_utc_time, int(report_time_delta))
            time_ = re.search(r'(\d+):(\d+)', deliver_time)

        hour = time_.group(1)
        minute = time_.group(2)
        return hour, minute

    def _add_cloud_pin_cwp(self, cloud_cwp_name, **pin_cwp_config):
        """
        - configure all the fields in cloud pin opened window

        :param pin_cwp_config: (dict) configuration parameters
        :param cloud_cwp_name: (str) CWP name
        :return: None
        """
        pin_valid_time = pin_cwp_config.get('pin_valid_time', '1 Hour')
        report_time_delta = pin_cwp_config.get('report_time_delta', '10')
        daily_report_email_id = pin_cwp_config.get('email_address_for_daily_report')
        custom_cwp_setting = pin_cwp_config.get('custom_cwp_setting')

        delivery_time_hour, delivery_time_minute = self._get_report_delivery_time(report_time_delta)

        self.utils.print_info("Click on default CWP add button")
        self.auto_actions.click_reference(self.get_default_cwp_add_button)
        sleep(2)

        self.utils.print_info(f"Enter CWP name:{cloud_cwp_name}")
        self.auto_actions.send_keys(self.get_default_cwp_name_field(), cloud_cwp_name)

        self.utils.print_info("Select the pin valid time")
        self._config_pin_valid_time(pin_valid_time)

        self.utils.print_info("Enter Daily report email address")
        self._config_daily_report_email_addr(daily_report_email_id)

        self.utils.print_info("Config Daily report time")
        self._config_daily_report_delivery_time(delivery_time_hour, delivery_time_minute)
        if custom_cwp_setting:
            return self._config_cloud_pin_custom_cwp(**custom_cwp_setting)


    @property
    def perform_cwp_save(self):
        """
        Save the captive web portal and handle the error msgs in any field

        :return: 1 if created else -1
        """
        self.utils.print_info("Click on CWP save button")
        self.auto_actions.click_reference(self.get_default_add_windows_cwp_save_cwp_button)
        self.screen.save_screen_shot()
        sleep(2)

        # Error handling
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        for tip_text in tool_tp_text:
            if "Update the highlighted errors below" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return -1
        return 1

    def create_cloud_pin_cwp(self, **cloud_pin_cwp_profile):
        """
        - This keyword is used to create cloud pin based cwp
        - there are two ways to call this keyword
        - 1. standalone, for this assumption is already navigated to the wireless network tab
        - Keyword Usage:
        - ``Create Cloud Pin CWP   &{CLOUD_PIN_CWP_PROFILE}``
        - For &{CLOUD_PIN_CWP_PROFILE}  dict creation refer cloud_pin_config.robot
        - 2. called by "create_open_network_captive_web_portal"

        :param cloud_pin_cwp_profile: (dict) configuration parameters to create cloud pin based cwp
        :return: 1 if created or selected, else -1
        """

        self.utils.print_info("Enable captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal())
        sleep(5)

        self.utils.print_info("Enable Cloud captive web portal radio button")
        self.auto_actions.enable_radio_button(self.get_cloud_cwp_radio_button())

        self.utils.print_info("Click on Request a pin radio button")
        if not self.get_request_pin_radio_button().is_selected():
            self.auto_actions.click_reference(self.get_request_pin_radio_button)
            sleep(2)
        self.screen.save_screen_shot()

        cloud_pin_cwp_config = cloud_pin_cwp_profile.get('open_cwp_config')
        cloud_pin_cwp_name = cloud_pin_cwp_config.get('cloud_cwp_name')

        if self._select_default_captive_web_portal(cloud_pin_cwp_name):
            return 1

        pin_cwp_config = cloud_pin_cwp_config.get('pin_cwp_config')
        self.utils.print_info("Add PIN Generating cloud CWP")
        if self._add_cloud_pin_cwp(cloud_pin_cwp_name, **pin_cwp_config) == -1:
            return -1

        return self.perform_cwp_save

    def edit_cloud_pin_cwp(self, **edit_config):
        """
        - Assuming that navigated up to cloud pin cwp dialog window
        - It is used to edit the already existed CWP
        - Keyword Usage:
        - ```Edit Cloud Pin CWP    ${EDIT_CONFIG}``

        :param edit_config: (dict) edit configuration parameters
        :return: 1 if success else -1
        """
        cwp_name = edit_config.get('cwp_name')
        self.utils.print_info("Click on cwp:{} edit link".format(cwp_name))
        self.auto_actions.click_reference(self.get_default_cwp_edit_link)
        sleep(2)

        pin_valid_time = edit_config.get('pin_valid_time', '1 Hour')
        report_time_delta = edit_config.get('report_time_delta', '10')
        daily_report_email_id = edit_config.get('email_address_for_daily_report')
        delivery_time = BuiltIn().get_variable_value('${REPORT_DELIVERY_TIME}')

        delivery_time_hour, delivery_time_minute = self._get_report_delivery_time(report_time_delta)

        if pin_valid_time:
            self.utils.print_info("Select the pin valid time")
            self._config_pin_valid_time(pin_valid_time)

        if daily_report_email_id:
            self.utils.print_info("Enter Daily report email address")
            self._config_daily_report_email_addr(daily_report_email_id)
        if delivery_time:
            self.utils.print_info("Config Daily report time")
            self._config_daily_report_delivery_time(delivery_time_hour, delivery_time_minute)

        if not self.perform_cwp_save == 1:
            return -1

        self.utils.print_info("Click on wireless network save button")
        self.auto_actions.click_reference(self.get_cwp_wireless_network_save_button)
        sleep(2)
        return 1

    def create_psk_wireless_network_cwp(self, **cwp_config):
        """
        - Create captive web portal for  psk wireless network
        - This is called as part of psk wireless network creation
        - For standalone call assumes that already navigated to the wireless network page, selected the psk auth type
        - Keyword Usage:
        - ``Create Psk Wireless Network CWP    &{CWP_CONFIG}``

        :param cwp_config: (dict) configuration
        :return: 1 if created else -1
        """
        enable_cwp = cwp_config.get('enable_cwp', 'DISABLE')
        user_auth_on_cwp = cwp_config.get('user_auth_on_cwp', 'DISABLE')
        enable_self_reg = cwp_config.get('enable_self_reg', 'DISABLE')
        enable_upa = cwp_config.get('enable_upa', 'ENABLE')
        cwp_name = cwp_config.get('cwp_name')
        authentication_method = cwp_config.get('authentication_method', 'CHAP')

        try:
            if enable_cwp.upper() == 'ENABLE':
                self.utils.print_info('Enable Captive Web Portal.')
                self.auto_actions.enable_radio_button(self.get_enable_captive_web_portal())
            else:
                self.utils.print_info('Disable Captive Web Portal.')
                self.auto_actions.disable_radio_button(self.get_enable_captive_web_portal())
                return 1

            self.utils.wait_till(self.get_enable_upa, delay=2, timeout=6, is_logging_enabled=True)
            if enable_upa.upper() == 'ENABLE':
                self.utils.print_info('Enable UPA.')
                self.auto_actions.enable_check_box(self.get_enable_upa())
            else:
                self.utils.print_info('Disable UPA.')
                self.auto_actions.disable_check_box(self.get_enable_upa())

            if user_auth_on_cwp.upper() == 'ENABLE':
                self.utils.print_info('Enable user auth on cwp.')
                self.auto_actions.enable_check_box(self.get_user_auth_on_captive_web_portal())
            else:
                self.utils.print_info('Disable user auth on cwp.')
                self.auto_actions.disable_check_box(self.get_user_auth_on_captive_web_portal())

            if enable_self_reg.upper() == "ENABLE":
                self.utils.print_info("Enable self registration check box")
                self.auto_actions.enable_check_box(self.get_enable_self_registration())
            else:
                self.utils.print_info("Disable self registration check box")
                self.auto_actions.disable_check_box(self.get_enable_self_registration())

            self.screen.save_screen_shot()
            sleep(2)
            self.utils.print_info(f"Check the CWP: {cwp_name}  already exists")
            if self._select_default_captive_web_portal(cwp_name):
                return 1
            else:
                if enable_upa.upper() == 'ENABLE':
                    return self._add_default_cwp_wireless_network(cwp_name)
                elif user_auth_on_cwp.upper() == 'ENABLE':
                    return self._add_user_authentication_on_cwp(cwp_name, authentication_method)
                else:
                    return -1

        except Exception as e:
            self.utils.print_info(f"Unable to create_psk_wireless_network_cwp(): {e}")
            return -1