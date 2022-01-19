from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from xiq.flows.configure.GuestPasswdSetting import GuestPasswdSetting
import xiq.flows.common.ToolTipCapture as tool_tip
from xiq.elements.GuestAccessNetworkWebElements import GuestAccessNetworkWebElements


class GuestAccessNetwork(GuestAccessNetworkWebElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.passwd_settings = GuestPasswdSetting()
        self.screen = Screen()

    def _config_ssid_fields(self, ssid):
        """
        Enter the SSID and broadcast ssid
        :param SSID:
        :return:
        """
        self.utils.print_info("Entering SSID Name:{}".format(ssid))
        self.auto_actions.send_keys(self.get_ssid_name_field(), ssid)

        self.utils.print_info("Entering Broadcast SSID name:{}".format(ssid))
        self.auto_actions.click(self.get_ssid_broadcost_name_field())
        sleep(2)

    def _add_employee_approval_domain(self, domain):
        """
        Adding Guest Access Approve Email Domain List
        :param domain:
        :return:
        """
        self.utils.print_info("Clicking on the employee approval button")
        self.auto_actions.click(self.get_add_employee_approval_button())
        sleep(2)

        self.utils.print_info("Entering domain name:{}".format(domain))
        self.auto_actions.send_keys(self.get_domain_name(), domain)

        self.utils.print_info("Click on domain add button")
        self.auto_actions.click(self.get_domain_name_add_button())
        sleep(2)

        self.screen.save_screen_shot()
        self.utils.print_info("Click on employee approval done button")
        self.auto_actions.click(self.get_employee_approval_domain_name_done_button())
        sleep(2)
        return 1

    def _add_user_groups(self, **group):
        """
        Add the user group
        :param group: group config dict
        :return:
        """
        group_name = group.get('group_name')
        passwd_settings = group.get('passwd_settings')
        expiration_settings = group.get('expiration_settings')
        delivery_settings = group.get('delivery_settings')

        if self._select_user_group(group_name):
            return 1

        self.utils.print_info("Click on group create one")
        self.auto_actions.click(self.get_user_group_create())
        sleep(2)

        self.utils.print_info("Entering the group name:{}".format(group_name))
        self.auto_actions.send_keys(self.get_user_group_name(), group_name)
        self.screen.save_screen_shot()
        if passwd_settings:
            self.passwd_settings.config_password_settings(**passwd_settings)
        if expiration_settings:
            pass
        if delivery_settings:
            pass

        self.screen.save_screen_shot()
        self.utils.print_info("Click on groups save button")
        self.auto_actions.click(self.get_user_group_save_button())
        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "The User Group cannot be saved because the name" in value:
                self.utils.print_info("User group name:{} already exists".format(group_name))
                return -1
        return 1

    def _select_user_group(self, group_name):
        """
        Select the user group
        :param group_name:
        :return:
        """
        self.utils.print_info("Selecting the user group:{}".format(group_name))
        select_elem = self.get_user_group_drop_down()
        if self.auto_actions.select_options(select_elem, group_name, 'visible_text'):
            return True

    def _config_guest_self_register_sign_in(self, **config):
        """
        - Config unsecured Auth network with "Guests can self-register,
        - then sign in option in unsecured network" option
        :param config: configuration dict
        :return:
        """

        self.utils.print_info("Selecting Guests can self-register, then sign in radio button")
        if self.get_guest_self_register_sign_in_radio_button():
            self.auto_actions.click(self.get_guest_self_register_sign_in_radio_button())
            sleep(2)

        self.screen.save_screen_shot()
        cwp_config = config.get('cwp_config')
        user_groups = config.get('user_groups')
        empl_approval_domain = config.get('empl_approval_domain')

        self.utils.print_info("Configuring Captive Web Portal")
        self._guest_access_cwp_config(**cwp_config)

        self.utils.print_info("Configuring the User Group")
        self._add_user_groups(**user_groups)

        self.utils.print_info("Configuring the Employee Approval")
        self._add_employee_approval_domain(empl_approval_domain)
        return 1

    def _guest_access_cwp_config(self, **cwp_config):
        """
        Customize Captive Web Portal configuration
        :param cwp_config: dict
        :return:
        """
        cwp_name = cwp_config.get('cwp_name')
        upa = cwp_config.get('upa')
        success_page = cwp_config.get('success_page')
        landing_page = cwp_config.get('landing_page')

        self.utils.print_info("Click on Customized captive web portal")
        self.auto_actions.click(self.get_customized_cwp())
        sleep(2)

        self.utils.print_info(f"Enter the captive web portal name:{cwp_name}")
        self.auto_actions.send_keys(self.get_cwp_name_field(), cwp_name)

        if upa:
            self.auto_actions.click(self.get_user_policy_acceptance_slide_bar())
            sleep(2)
        if success_page:
            self.auto_actions.click(self.get_success_page_slide_bar())
            sleep(2)

        if landing_page:
            self.auto_actions.click(self.get_cwp_landing_page_side_bar())
            sleep(2)
        self.screen.save_screen_shot()
        self.utils.print_info("Click on customize CWP done button")
        self.auto_actions.click(self.get_cwp_done_button())
        sleep(2)
        return 1

    def _config_guest_access_usr_policy_bf_accessing_nw(self, **config):
        """
        Config unsecured Auth network with "Guests accept the use policy before accessing the network" option
        :param config: config dict
        :return:
        """
        cwp_config = config.get('cwp_config')

        self.utils.print_info("Selecting Guests accept the use policy before accessing the network radio button")
        if self.get_guest_access_usr_policy_bf_accessing_nw():
            self.auto_actions.click(self.get_guest_access_usr_policy_bf_accessing_nw())
            self.screen.save_screen_shot()
            sleep(2)
        self._guest_access_cwp_config(**cwp_config)
        return 1

    def _configure_unsecured_network(self, **unsecure_config):
        """
        Configure Unsecured (Open) Network
        :param unsecure_config: configuration dictionary
        :return:
        """
        self.utils.print_info("***************************************************")
        self.utils.print_info("Configuration parameters of unsecured Network")
        for key, value in unsecure_config.items():
            self.utils.print_info("{}:{}".format(key, value))
        self.utils.print_info("***************************************************")

        if not self.get_guest_access_nw_without_login_radio_button():
            self.utils.print_info("Selecting Unsecured(Open) Network")
            self.auto_actions.click(self.get_unsecured_network_radio_button())
            sleep(2)

        guest_access_nw_without_login = unsecure_config.get('guest_access_nw_without_login', 'Disable')
        if guest_access_nw_without_login.upper() == "ENABLE":
            self.utils.print_info("Selecting guest access network without login radio button")
            self.auto_actions.click(self.get_guest_access_nw_without_login_radio_button())
            self.screen.save_screen_shot()
            sleep(2)
            return 1

        guest_accept_user_policy_bf_access_nw = unsecure_config.get('guest_accept_user_policy_bf_access_nw', 'Disable')
        if guest_accept_user_policy_bf_access_nw.upper() == "ENABLE":
            return self._config_guest_access_usr_policy_bf_accessing_nw(**unsecure_config)

        guest_self_register_sign_in = unsecure_config.get('guest_self_register_sign_in', 'Disable')
        if guest_self_register_sign_in.upper() == 'ENABLE':
            return self._config_guest_self_register_sign_in(**unsecure_config)

    def _config_secure_global_passwd_credentials_to_guests(self, **config):
        """
        Create Secured Auth NetworkCreate with "global password (PSK) credentials for your guests
        to log in to your network."
        :param config: configuration dict
        :return:
        """
        self.utils.print_info(config)
        self.utils.print_info("Enable global password (PSK) credentials for your guests options")
        if not self.get_global_passwd_cred_for_guest_to_login().is_selected():
            self.auto_actions.click(self.get_global_passwd_cred_for_guest_to_login())
            sleep(2)

        self.screen.save_screen_shot()
        enable_cwp = config.get('enable_cwp', 'Disable')
        cwp_config = config.get('cwp_config')
        if enable_cwp.upper() == 'ENABLE':
            self.utils.print_info("Enable captive web portal")
            self.auto_actions.click(self.get_enable_cwp_check_box())
            sleep(2)
            self._guest_access_cwp_config(**cwp_config)

        password = config.get('password',)
        self.utils.print_info("Entering PSK Password:{}".format(password))
        self.auto_actions.send_keys(self.get_psk_password(), password)
        self.screen.save_screen_shot()
        return 1

    def _config_secure_guest_self_reg_signin(self, **config):
        """
        Create Secured Auth Network, Create with  "Guests can self-register, then sign in.
        As an option, an employee can approve"
        :param config: Configuration dict
        :return:
        """
        self.utils.print_info("Enable guests self register sign in radio button")
        if not self.get_guests_self_reg_sign_in_employee_approve().is_selected():
            self.auto_actions.click(self.get_guests_self_reg_sign_in_employee_approve())
            sleep(2)
        self.screen.save_screen_shot()
        self.utils.print_info("Configure the captive web portal")
        cwp_config = config.get('cwp_config')
        self._guest_access_cwp_config(**cwp_config)

        guest_self_reg_ssid = config.get('guest_self_reg_ssid')
        self.utils.print_info("Entering guest self register ssid:{}".format(guest_self_reg_ssid))
        self.auto_actions.send_keys(self.get_guest_self_registration_ssid(), guest_self_reg_ssid)
        sleep(2)

        employee_approval_domain = config.get('empl_approval_domain')
        self._add_employee_approval_domain(employee_approval_domain)

        user_groups = config.get('user_groups')
        self.utils.print_info("Configuring the user group")
        self.utils.print_info(user_groups)
        self._add_user_groups(**user_groups)

        return 1

    def _mac_binding_numbers_per_ppsk(self, status, mac_binding_num):
        """
        Enable or disable the Set the MAC binding numbers per private PSK option
        :param status:
        :param mac_binding_num:
        :return:
        """
        if status.upper() == 'ENABLE':
            self.utils.print_info("Enabling Set the MAC binding numbers per private PSK option")
            if not self.get_mac_binding_num_per_ppsk().is_selected():
                self.auto_actions.click(self.get_mac_binding_num_per_ppsk())
                sleep(2)

            self.utils.print_info("Enter MAC binding numbers per private PSK:{}".format(mac_binding_num))
            self.auto_actions.send_keys(self.get_mac_binding_number(), mac_binding_num)
            sleep(2)
        else:
            if self.get_mac_binding_num_per_ppsk().is_selected():
                self.auto_actions.click(self.get_mac_binding_num_per_ppsk())
                sleep(2)
        return 1

    def _config_max_numb_clients_per_ppsk(self, status, num_clients):
        """
        Enable or disable the Set the maximum number of clients per private PSK options based on status,
        set the maximum number of clients per PPSK
        :param status:
        :param num_clients:
        :return:
        """
        if status.upper() == 'ENABLE':
            self.utils.print_info("Enabling maximum number of clients per private PSK option")
            if not self.get_max_num_clients_per_ppsk().is_selected():
                self.auto_actions.click(self.get_max_num_clients_per_ppsk())
                sleep(2)
            self.utils.print_info("Enter the max number of clients per PPSK:{}".format(num_clients))
            self.auto_actions.send_keys(self.get_max_clients_per_ppsk(), num_clients)
            sleep(2)
        else:
            if self.get_max_num_clients_per_ppsk().is_selected():
                self.auto_actions.click(self.get_max_num_clients_per_ppsk())
                sleep(2)
        return 1

    def _config_guest_credentials_to_login(self, **config):
        """
        Create Secured Auth Network with "credentials for guests to log in to your network."
        :param config: configuration dict
        :return:
        """
        self.utils.print_info("Click on Create credentials for guests to log in to your network Radio button")
        if not self.get_create_guest_credentials_to_login_nw().is_selected():
            self.auto_actions.click(self.get_create_guest_credentials_to_login_nw())
            sleep(2)

        self.screen.save_screen_shot()
        # configuring values
        config_options = config.get('create_guest_credentials_to_login_config')
        max_num_clients_per_ppsk = config_options.get('max_num_clients_per_ppsk')
        num_clients = config_options.get('num_clients')
        mac_binding_num_per_ppsk = config_options.get('mac_binding_num_per_ppsk')
        mac_binding_number = config_options.get('mac_binding_number')
        ppsk_server = config_options.get('ppsk_server')
        auth_db = config_options.get('auth_db')
        user_groups = config_options.get('user_groups')

        self.utils.print_info("Set the maximum number of clients per private PSK")
        self._config_max_numb_clients_per_ppsk(max_num_clients_per_ppsk, num_clients)

        self.utils.print_info("Set the MAC binding numbers per private PSK")
        self._mac_binding_numbers_per_ppsk(mac_binding_num_per_ppsk, mac_binding_number)

        self.utils.print_info("Select the authentication db type:{}".format(auth_db))
        self.auto_actions.center_element(self.get_auth_db_drop_down())
        aut_db_drop_down = self.get_auth_db_drop_down()
        self.auto_actions.select_options(aut_db_drop_down, auth_db, 'visible_text')

        self.utils.print_info("Configure the user groups")
        self._add_user_groups(**user_groups)
        self.screen.save_screen_shot()

        # @to do create bulk users
        return 1

    def _configure_secured_network(self, **secure_nw_config):
        """
        Configure the secured network based on the passed arguments
        :param secure_nw_config:
        :return:
        """
        self.utils.print_info("***************************************************")
        self.utils.print_info("Configuration parameters of secured Network")
        for key, value in secure_nw_config.items():
            self.utils.print_info("{}:{}".format(key, value))
        self.utils.print_info("***************************************************")

        self.utils.print_info("Selecting the Secure Network")
        self.auto_actions.click(self.get_secured_network_radio_button())
        sleep(2)

        create_guest_credentials_to_login = secure_nw_config.get('create_guest_credentials_to_login', 'Disable')
        if create_guest_credentials_to_login.upper() == 'ENABLE':
            return self._config_guest_credentials_to_login(**secure_nw_config)

        guest_self_reg_signin = secure_nw_config.get('guest_self_reg_signin', 'Disable')
        if guest_self_reg_signin.upper() == 'ENABLE':
            return self._config_secure_guest_self_reg_signin(**secure_nw_config)

        global_passwd_credentials_to_guests = secure_nw_config.get('global_passwd_credentials_to_guests', 'Disable')
        if global_passwd_credentials_to_guests.upper() == 'ENABLE':
            return self._config_secure_global_passwd_credentials_to_guests(**secure_nw_config)

    def create_guest_access_network(self, **config):
        """
        - Create secure and unsecure guest networks
        - Assuming navigated to Configure-->Network Policies-->Wireless Networks
        - Keyword Usage:
         - ``Create Guest Access Network     &{CONFIG}``
         - For creation of &{CONFIG} refer guest_access_config.robot

        :param config: configuration parameter dict
        :return: 1 if created else -1
        """
        guest_auth_type = config.get('guest_auth_type')
        ssid_name = config.get("ssid_name", 'Guest')
        guest_auth_config = config.get('guest_auth_config')

        self.utils.print_info("Click on wireless network add drop down button")
        self.auto_actions.click(self.get_wireless_nw_add_button())
        sleep(5)

        self.utils.print_info("Click on Guest Access Network menu item")
        self.auto_actions.click(self.get_guest_access_nw_menu_item())
        sleep(2)

        self.utils.print_info("Configure SSID and Broadcast SSID name")
        self._config_ssid_fields(ssid_name)

        if guest_auth_type.upper() == "UNSECURE":
            self._configure_unsecured_network(**guest_auth_config)

        if guest_auth_type.upper() == "SECURE":
            self._configure_secured_network(**guest_auth_config)

        sleep(2)
        self.utils.print_info("Clicking on Guest access save button")
        self.auto_actions.click(self.get_guest_access_network_save_button())
        sleep(5)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on Guest access network go to deploy button")
        self.auto_actions.click(self.get_guest_network_go_to_deploy_button())
        sleep(5)
        return 1
