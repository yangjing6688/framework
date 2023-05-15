from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.xiq.flows.configure.WirelessCaptiveWebPortal import WirelessCaptiveWebPortal
from extauto.xiq.flows.configure.GuestAccessNetwork import GuestAccessNetwork
from extauto.xiq.flows.configure.UserGroups import UserGroups
from extauto.xiq.flows.configure.RadiusServer import RadiusServer
from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements


class WirelessNetworks:
    def __init__(self):
        self.utils = Utils()
        self.wireless_web_elements = WirelessWebElements()
        self.navigator = NavigatorWebElements()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.captive_portal = WirelessCaptiveWebPortal()
        self.radius_server = RadiusServer()
        self.guest_access = GuestAccessNetwork()
        self.user_group = UserGroups()

    def _search_wireless_network_name_in_grid(self, ssid_name):
        """
        - Search the wireless network name in the Wireless network page

        :param ssid_name: Name of the SSID
        :return: 1 if ssid row exists else -1
        """
        row = self._get_wireless_network_row(ssid_name)
        if row:
            return 1

    def _get_wireless_network_row(self, wireless_nw_name):
        """
        - Get the wireless network row

        :param wireless_nw_name:
        :return: row object
        """
        self.utils.print_info("Getting the wireless network rows")
        rows = self.wireless_web_elements.get_wireless_nw_grid_rows()
        if not rows:
            self.utils.print_info("Wireless networks are not present")
            return False
        for row in rows:
            cell = self.wireless_web_elements.get_wireless_nw_row_cell(row, 'field-name')
            if cell.text == wireless_nw_name:
                return row
        self.utils.print_info("wireless nw name not exist in wireless network page")

    def _wireless_wifi0_use_checkbox(self, status):
        """
        Select or unselect the wifi0 use check box

        :param status: Enable or Disable
        :return: None
        """
        if status == "Enable":
            self.auto_actions.enable_check_box(self.wireless_web_elements.get_wireless_wifi0_checkbox())
        else:
            self.auto_actions.disable_check_box(self.wireless_web_elements.get_wireless_wifi0_checkbox())

    def _wireless_wifi1_use_checkbox(self, status):
        """
        Select or unselect the wifi1 use check box

        :param status: Enable or Disable
        :return: None
        """
        if status == "Enable":
            self.auto_actions.enable_check_box(self.wireless_web_elements.get_wireless_wifi1_checkbox())
        else:
            self.auto_actions.disable_check_box(self.wireless_web_elements.get_wireless_wifi1_checkbox())

    def _config_enterprise_authentication_settings(self, **authentication_settings):
        """
        - Configuring enterprise authentication subsection
        - Authentication with ExtremeCloud IQ Authentication Service  option Enable-->Add User Groups
        - Authentication with ExtremeCloud IQ Authentication Service  option Disable-->Add Radius Server

        :param authentication_settings: (dict) Authentication configuring parameters
        :return: 1 if success else -1
        """
        extiq_auth_service = authentication_settings.get('auth_with_extcldiq_service')
        auth_service_slider_button = self.wireless_web_elements.get_auth_with_extiq_auth_service_slider_button()

        if extiq_auth_service.upper() == 'DISABLE':
            self.auto_actions.disable_check_box(auth_service_slider_button)
            sleep(2)

            self.utils.print_info("Configure the Radius server")
            rs_group_config = authentication_settings.get('radius_server_group_config')
            return self.radius_server.config_radius_server(**rs_group_config)

        if extiq_auth_service.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(auth_service_slider_button)
            sleep(2)

            user_group_config = authentication_settings.get('user_group_config')
            if not user_group_config == 'None':
                usr_group_name = user_group_config.get('group_name')
                group_profile = user_group_config.get('user_group_profile')
                if not group_profile == 'None':
                    self.user_group.add_wireless_nw_user_group(usr_group_name, group_profile)
                else:
                    if not self.user_group.select_wireless_user_group(usr_group_name):
                        self.utils.print_info(f"User group:{usr_group_name} not created !!!")
                        return -1
            return 1

    def _configure_wifi_interfaces_settings(self, **conf):
        """
        Select the options to enable wifi0 and wifi1 radio settings

        :param conf: configuration dictionary
        :return:
        """
        wifi0_config = conf.get('WIFI0', 'Enable')
        wifi1_config = conf.get('WIFI1', 'Enable')

        if wifi0_config == "Enable":
            self._wireless_wifi0_use_checkbox('Enable')
        else:
            self._wireless_wifi0_use_checkbox('Disable')

        if wifi1_config == "Enable":
            self._wireless_wifi1_use_checkbox('Enable')
        else:
            self._wireless_wifi1_use_checkbox('Disable')

        wifi2_config = conf.get('WIFI2', 'None')
        if not wifi2_config == 'None':
            if conf['WIFI2'] == "Enable":
                self._wireless_wifi2_use_checkbox('Enable')

                self.utils.print_info("Clicking Yes button for WiFi6 Dialog")
                self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_wifi2_checkbox_dialog_yes_button)

            else:
                self._wireless_wifi2_use_checkbox('Disable')

    def _config_key_encryption_method(self, key_management, encryption_method):
        """
        - Selecting configuration Key And Encryption Method

        :param key_management: Key Management ex: WPA2-802.1X
        :param encryption_method: key method --CCMP (AES) , TKIP
        :return: 1 if configured else -1
        """
        self.utils.print_info("Click on key-management drop down")
        self.auto_actions.click_reference(self.wireless_web_elements.get_key_management_drop_down)
        sleep(2)
        key_options = self.wireless_web_elements.get_key_management_options()
        self.auto_actions.select_drop_down_options(key_options, key_management)
        sleep(2)

        if key_management.upper() == "WPA3-802.1X":
            return 1

        self.utils.print_info("Click on encryption method drop down")
        self.auto_actions.click_reference(self.wireless_web_elements.get_encryption_method_drop_down)
        sleep(2)
        encryption_opt = self.wireless_web_elements.get_encryption_method_options()
        self.auto_actions.select_drop_down_options(encryption_opt, encryption_method)
        return 1

    def _select_wireless_network_auth_type(self, auth_type):
        """
        Select the authentication type, Ex: OPEN, WEP, PSK, PPSK, ENTERPRISE

        :param auth_type: Type of the authentication
        :return: 1 is selected else -1
        """
        self.utils.print_info("selecting Authentication type for wireless network: {}".format(auth_type))
        if auth_type.upper() == "OPEN":
            self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_open)
            return 1
        elif auth_type.upper() == "ENTERPRISE":
            self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_enterprise)
            return 1
        elif auth_type.upper() == "PSK":
            self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_personal)
            return 1
        elif auth_type.upper() == "PPSK":
            self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_ppsk)
            return 1
        elif auth_type.upper() == "ENHANCED":
            self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_enhanced)
            return 1
        else:
            return -1

    def _config_wireless_network_ssid_section(self, ssid_name, **radio_config):
        """
        Configuring wireless network ssid subsection, enabling , disabling wi-fi radio's based arguments

        :param ssid_name: name of the ssid, same name used for broadcast ssid
        :param radio_config: config dictionary to config the radio settings
        :return: True
        """
        self.utils.print_info("Enter the Wireless Networks SSID Name:{}".format(ssid_name))
        self.auto_actions.send_keys(self.wireless_web_elements.get_wireless_ssid_field(), ssid_name)
        sleep(1)

        self.utils.print_info("Enter the Wireless Networks Broadcast Name:{}".format(ssid_name))
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_broadcast_name_field)
        sleep(1)

        # select WIFI0 interfaces for Wireless Networks
        self._configure_wifi_interfaces_settings(**radio_config)
        return True

    def _config_open_wireless_network(self, **auth_profile):
        """
        - Configure open authentication network

        :param auth_profile: (dict) include auth_type, cwp_config(dict), user_group_config(dict)
        :return: 1 if created else -1
        """

        self.utils.print_info(60*'*')
        self.utils.print_info("Configuration parameters for open network")
        for key, value in auth_profile.items():
            self.utils.print_info("{}: {}".format(key, value))
        self.utils.print_info(60 * '*')

        auth_type = auth_profile.get('auth_type')
        cwp_profile = auth_profile.get('cwp_profile')
        user_group_config = auth_profile.get('user_group_config', 'None')
        user_profile_config = auth_profile.get('user_profile_config', 'None')

        self.utils.print_info("Select Authentication card menu")
        self._select_wireless_network_auth_type(auth_type)

        self.screen.save_screen_shot()
        sleep(2)

        if not self.captive_portal.create_open_network_captive_web_portal(**cwp_profile) == 1:
            self.utils.print_info("Issue in creating the captive web portal")
            return -1

        self.utils.print_info("Selecting User Profiles")
        if not user_profile_config == 'None':
            usr_profile_name = user_profile_config.get('profile_name')
            if not self.user_group.select_wireless_user_profile(usr_profile_name, ignore_failure=True):
                self.utils.print_info(f"User Profile:{usr_profile_name} not created !!!")
                return -1

        if not user_group_config == 'None':
            usr_group_name = user_group_config.get('group_name')
            group_profile = user_group_config.get('user_group_profile')
            if not group_profile == 'None':
                self.user_group.add_wireless_nw_user_group(usr_group_name, group_profile)
            else:
                if not self.user_group.select_wireless_user_group(usr_group_name):
                    self.utils.print_info(f"User group:{usr_group_name} not created !!!")
                    return -1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("click on wireless network save button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_network_save_button)
        self.screen.save_screen_shot()
        sleep(2)
        return 1

    def _config_enterprise_wireless_network(self, **auth_profile):
        """
        Configure the enterprise authentication network

        :param auth_profile: configuration dictionary to config cwp, radius server, user group
        :return: 1
        """
        self.utils.print_info(60*'*')
        self.utils.print_info("Configuration parameters for enterprise network")
        for key, value in auth_profile.items():
            self.utils.print_info("{}: {}".format(key, value))
        self.utils.print_info(60 * '*')

        key_encryption = auth_profile['key_encryption']
        cwp_profile = auth_profile['cwp_profile']
        auth_setting_profile = auth_profile['auth_settings_profile']

        # select the authentication card menu
        self.utils.print_info("Select Enterprise WPA/WPA2/WPA3 card menu")
        self._select_wireless_network_auth_type(auth_profile['auth_type'])

        self.utils.print_info("Configuring the key and encryption method")
        self._config_key_encryption_method(key_encryption['key_management'], key_encryption['encryption_method'])

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Configuring captive web portal")
        if not self.captive_portal.create_enterprise_wireless_network_cwp(**cwp_profile) == 1:
            return -1

        self.utils.print_info("Configuring Enterprise authentication network settings sub section")
        if not self._config_enterprise_authentication_settings(**auth_setting_profile) == 1:
            return -2

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("click on wireless network save button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_network_save_button)
        self.screen.save_screen_shot()
        sleep(2)
        return 1

    def _client_per_ppsk_checkbox(self, status, no_clients=0):
        """
        Enable or disable the maximum number of clients per private ppsk

        :param status: Enable or Disable
        :param no_clients: number of clients
        :return: None
        """
        if status == 'Enable':
            self.auto_actions.enable_check_box(self.wireless_web_elements.get_max_num_of_clients_per_ppsk_check_box())
            sleep(1)

            self.utils.print_info("Enter the number of clients per ppsk")
            self.auto_actions.send_keys(self.wireless_web_elements.get_max_num_of_clients_per_ppsk_input_field(),
                                        no_clients)
        else:
            self.utils.print_info("Un Select the max numb clients per ppsk check box")
            self.auto_actions.disable_check_box(self.wireless_web_elements.get_max_num_of_clients_per_ppsk_check_box())

    def _ppsk_classification_use_checkbox(self, status):
        """
        Select or unselect the PPSK classification by using checkbox

        :param status: Enable or Disable
        :return: None
        """
        if status == "Enable":
            self.auto_actions.enable_check_box(self.wireless_web_elements.get_ppsk_classification_use_checkbox())
        else:
            self.auto_actions.disable_check_box(self.wireless_web_elements.get_ppsk_classification_use_checkbox())

    def _pcg_use_check_box(self, status, pcg_type=None):
        """
        Enable of disable the pcg(Private client group) based on status

        :param status: Enable for select , Disable for unselect
        :param pcg_type: AP-Based or Key-Based
        :return: None
        """
        if status == "Enable":
            if not self.wireless_web_elements.get_pcg_use_checkbox().is_selected():
                self.utils.print_info("Clicking on PCG use check box")
                self.auto_actions.click_reference(self.wireless_web_elements.get_pcg_use_checkbox)
                if pcg_type == 'AP-Based':
                    self.utils.print_info("Selecting AP-Based radio button")
                    self.auto_actions.click_reference(self.wireless_web_elements.get_ap_based_radio_button)
                if pcg_type == 'Key-Based':
                    self.utils.print_info("Selecting Key-Based radio button")
                    self.auto_actions.click_reference(self.wireless_web_elements.get_key_based_radio_button)
        else:
            self.utils.print_info("Un selecting pcg use check box")
            if self.wireless_web_elements.get_pcg_use_checkbox().is_selected():
                self.auto_actions.click_reference(self.wireless_web_elements.get_pcg_use_checkbox)

    def _mac_bindings_per_ppsk_checkbox(self):
        """

        :return:
        """
        pass

    def _set_ppsk_configuration(self, **ppsk_config):
        """
        Enable or disable the check box, maximum number of clients per private PSK,
        Set the MAC binding numbers per private PSK, Private Client Group Options,
        PPSK Classification Options

        :param ppsk_config:
        :return:
        """
        client_per_ppsk = ppsk_config['client_per_ppsk']
        mac_binding_num_per_ppsk = ppsk_config['mac_binding_num_per_ppsk']
        pcg_use = ppsk_config['pcg_use']
        ppsk_classification = ppsk_config['ppsk_classification']

        self.utils.print_info(f"Set the maximum number of clients per private PSK:{client_per_ppsk}")
        if client_per_ppsk.upper() == "ENABLE":
            self._client_per_ppsk_checkbox('Enable', ppsk_config['num_clients'])
        else:
            self._client_per_ppsk_checkbox('Disable')

        self.utils.print_info(f"Set the MAC binding numbers per private PSK:{mac_binding_num_per_ppsk}")
        if mac_binding_num_per_ppsk.upper() == "ENABLE":
            self._mac_bindings_per_ppsk_checkbox()

        self.utils.print_info("Private Client Group Options:{}".format(pcg_use))
        if ppsk_config['pcg_use'].upper() == 'ENABLE':
            self._pcg_use_check_box('Enable', ppsk_config['pcg-type'])
        else:
            self._pcg_use_check_box('Disable')

        self.utils.print_info(f"PPSK Classification Options:{ppsk_classification}")
        if ppsk_config['ppsk_classification'].upper() == "ENABLE":
            self._ppsk_classification_use_checkbox('Enable')
        else:
            self._ppsk_classification_use_checkbox('Disable')

    def _config_private_pre_shared_key_wireless_network(self, **auth_profile):
        """
        - Configure the PPSK network

        :param auth_profile: configuration dict to configure cwp, user groups
        :return: 1
        """
        self.utils.print_info(60*'*')
        self.utils.print_info("Configuration parameters for ppsk network")
        for key, value in auth_profile.items():
            self.utils.print_info("{}: {}".format(key, value))
        self.utils.print_info(60 * '*')

        key_encryption = auth_profile.get('key_encryption')
        ppsk_config = auth_profile.get('ppsk_config')
        cwp_config = auth_profile.get('cwp_config')
        user_group_config = auth_profile.get('user_group_config', 'None')

        self.utils.print_info("Select Private Pre-Shared Key card menu")
        self._select_wireless_network_auth_type(auth_profile['auth_type'])

        key_management = key_encryption['key_management']
        encryption_method = key_encryption['encryption_method']

        self.utils.print_info(f"Configuring key management:{key_management}  encryption method:{encryption_method}")
        self._config_key_encryption_method(key_management, encryption_method)

        self.utils.print_info("Configure PPSK settings")
        self._set_ppsk_configuration(**ppsk_config)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Configuring captive web portal")
        if not self.captive_portal.create_ppsk_wireless_network_cwp(**cwp_config) == 1:
            return -1

        self.utils.print_info("Select the user group")
        if not user_group_config == 'None':
            usr_group_name = user_group_config.get('group_name')
            group_profile = user_group_config.get('user_group_profile')
            if not group_profile == 'None':
                self.user_group.add_wireless_nw_user_group(usr_group_name, group_profile)
            else:
                db_loc = user_group_config.get('db_loc')
                if not self.user_group.select_wireless_user_group(usr_group_name, db_loc, 'PPSK'):
                    self.utils.print_info(f"User group:{usr_group_name} not created !!!")
                    return -1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("click on wireless network save button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_network_save_button)
        return 1

    def _config_enhanced_open_wireless_network(self, **auth_profile):
        """
        - Configure Enhanced Open SSID Authentication Wireless Network

        :param auth_profile: (dict) Authentication profile
        :return: 1 if success else -1
        """
        self.utils.print_info(60 * '*')
        self.utils.print_info("Configuration parameters for enhanced open network")
        for key, value in auth_profile.items():
            self.utils.print_info("{}: {}".format(key, value))
        self.utils.print_info(60 * '*')

        transition_mode = auth_profile.get('transition_mode', 'Disable')
        self.utils.print_info("Select Enhanced Open SSID Authentication tab.")
        self._select_wireless_network_auth_type(auth_profile['auth_type'])

        if transition_mode.upper() == "DISABLE":
            self.utils.print_info("Disable Transition Mode for 2.4Ghz and 5Ghz.")
            self.auto_actions.disable_radio_button(self.wireless_web_elements.get_transition_mode_for_2ghz_and_5ghz())
        elif transition_mode.upper() == "ENABLE":
            self.utils.print_info("Enable Transition Mode for 2.4Ghz and 5Ghz.")
            self.auto_actions.select_radio_button(self.wireless_web_elements.get_transition_mode_for_2ghz_and_5ghz())
            self.screen.save_screen_shot()
            sleep(2)
        else:
            return -1

        self.utils.print_info("Click on wireless network save button.")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_network_save_button)
        return 1

    def _config_standard_wireless_network(self, **kwargs):
        """
        - Creating the standard wireless network

        :param kwargs: configuration variable dict
        :return: 1 if successfully created else -1
        """
        ssid = kwargs.get('ssid_name')
        radio_config = kwargs.get('ssid_profile')
        auth_profile = kwargs.get('auth_profile')

        self.utils.print_info("Click on wireless network add drop down button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_nw_add_button)
        sleep(5)

        self.utils.print_info("Configure the SSID Name , Broadcast ssid name, and radio config ")
        self._config_wireless_network_ssid_section(ssid, **radio_config)

        auth_method_config = {'OPEN': self._config_open_wireless_network,
                              'PSK': self._config_personal_wireless_network,
                              'PPSK': self._config_private_pre_shared_key_wireless_network,
                              'ENHANCED': self._config_enhanced_open_wireless_network,
                              'ENTERPRISE': self._config_enterprise_wireless_network
                              }

        # Create the wireless Network Based on authentication type
        return auth_method_config[auth_profile['auth_type'].upper()](**auth_profile)

    def create_wireless_network(self, **wireless_network_conf):
        """
        - Create Standard or Guest wireless network based on network type
        - create open, PPSK, PSK, enterprise networks based authentication types
        - Assumption is already navigated to the network policy tab
        - Keyword Usage:
        - ``Create Wireless Network   &{WIRELESS_NETWORK_CONFIG}``
        - For creation of different config dict refer wireless_networks_config.robot, private_pre_shared_key_config.robot
        - guest_access_config.robot, wpa_personal_config.robot, social_login_config.robot, cloud_pin_config.robot

        :param wireless_network_conf: configuration parameter dictionary
        :return: 1 if successfully created else -1
        """
        ssid_name = wireless_network_conf.get('ssid_name')
        network_type = wireless_network_conf.get('network_type', 'None')

        self.utils.print_info("Click on  wireless network tab tab")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_networks_tab)
        sleep(5)

        if self._search_wireless_network_name_in_grid(ssid_name):
            self.utils.print_info("Wireless network already exists")
            return -1

        if network_type.upper() == "STANDARD" or network_type == 'None':
            return self._config_standard_wireless_network(**wireless_network_conf)

    def navigate_to_standard_enterprise_network(self):
        """
        - Navigate to Standard Enterprise Wireless Network after Network Policy Edit

        :return: True if success
        """
        self.utils.print_info("Click on  wireless network tab")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_networks_tab)
        sleep(5)

        self.utils.print_info("Click on wireless network add drop down button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_nw_add_button)
        sleep(5)

        self.utils.print_info("Click on standard network add button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_standard_nw_menu)

        self.utils.print_info("Select Enterprise WPA/WPA2/WPA3 card menu")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_authtype_enterprise)

        return True

    def _config_personal_wireless_network(self, **auth_profile):
        """
        - Configure Personal SSID Authentication Wireless Network

        :param auth_profile: auth_profile include key_management, encryption_method, key_type, key_value, cwp_config
        :return: 1 if there is no error
        :param auth_profile:
        :return:
        """
        self.utils.print_info(60 * '*')
        self.utils.print_info("Configuration parameters for personal network")
        for key, value in auth_profile.items():
            self.utils.print_info("{}: {}".format(key, value))
        self.utils.print_info(60 * '*')

        key_encryption = auth_profile['key_encryption']
        cwp_config = auth_profile['cwp_config']
        user_profile_config = auth_profile.get('user_profile_config', 'None')

        self.utils.print_info("Select Personal SSID Authentication Card Menu")
        self._select_wireless_network_auth_type(auth_profile['auth_type'])

        if key_encryption['key_management'] == "WPA2-(WPA2 Personal)-PSK":
            self.utils.print_info("Configuring the key and encryption method")
            self._config_key_encryption_method(key_encryption['key_management'], key_encryption['encryption_method'])

            self.utils.print_info("Configuring the key Type and Key Value")
            self._config_personal_wpa2_key_type_value_method(key_encryption['key_type'], key_encryption['key_value'])

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Configuring captive web portal")
            cp_status = self.captive_portal.create_psk_wireless_network_cwp(**cwp_config)
            if not cp_status == 1:
                return cp_status

        if key_encryption['key_management'] == "WPA3 (SAE)":
            self.utils.print_info("Configuring key Management")
            self._config_personal_key_method(key_encryption['key_management'])

            self.utils.print_info("Configuring SAE Group from drop down")
            self.auto_actions.click_reference(self.wireless_web_elements.get_sae_group_drop_down)
            sleep(2)
            key_options = self.wireless_web_elements.get_sae_group_options()
            for opt in key_options:
                if key_encryption['sae_group'].upper() == opt.text.upper():
                    self.auto_actions.click(opt)
                    sleep(2)
                    break

            self.utils.print_info("Configuring Transition Mode Status")
            self._configure_transition_mode(key_encryption['transition_mode'])

            self.utils.print_info("Enter WPA3 Key Value Input Field")
            self.auto_actions.send_keys(self.wireless_web_elements.get_personal_wpa3_key_value_input_field(),
                                        key_encryption['key_value'])

            self.utils.print_info("Enter Anti Logging Threshold")
            self.auto_actions.send_keys(self.wireless_web_elements.get_anti_logging_threshold(),
                                        key_encryption['anti_logging_Threshold'])

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Configuring captive web portal")
            cp_status = self.captive_portal.create_psk_wireless_network_cwp(**cwp_config)
            if not cp_status == 1:
                return cp_status

        self.utils.print_info("Selecting User Profiles")
        if not user_profile_config == 'None':
            usr_profile_name = user_profile_config.get('profile_name')
            if not self.user_group.select_wireless_user_profile(usr_profile_name, ignore_failure=True):
                self.utils.print_info(f"User Profile:{usr_profile_name} not created !!!")
                return -1
        sleep(2)
        self.utils.print_info("click on wireless network save button")
        self.auto_actions.click_reference(self.wireless_web_elements.get_wireless_network_save_button)
        sleep(2)
        self.screen.save_screen_shot()
        return 1

    def _config_personal_wpa2_key_type_value_method(self, key_type, key_value):
        """
        - Configure Key type And key value for personal authentication method

        :param key_type: Key Type ex: ASCII or HEX
        :param key_value: key value -- Password String to connect Client
        :return: 1 if configured else -1
        """
        self.utils.print_info(60*'*')
        self.utils.print_info("Key Type used:{}".format(key_type))
        self.utils.print_info(60 * '*')

        self.utils.print_info("Click on WPA2 key-type drop down")
        self.auto_actions.click_reference(self.wireless_web_elements.get_personal_wpa2_key_type_drop_down)
        sleep(2)
        key_options = self.wireless_web_elements.get_personal_wpa2_key_type_options()
        for opt in key_options:
            if key_type.upper() == opt.text.upper():
                self.auto_actions.click(opt)
                sleep(2)
                break

        self.utils.print_info("Enter WPA2 Key Value Input Field")
        self.auto_actions.send_keys(self.wireless_web_elements.get_personal_wpa2_key_value_input_field(), key_value)

        return 1

    def _config_personal_key_method(self, key_management):
        """
        Configure Key Management Method

        :param key_management: Key Management ex: WPA2-802.1X
        :return: 1 if configured else -1
        """
        self.utils.print_info(60*'*')
        self.utils.print_info("Key Management used:{}".format(key_management))
        self.utils.print_info(60 * '*')

        self.utils.print_info("Click on key-management drop down")
        self.auto_actions.click_reference(self.wireless_web_elements.get_key_management_drop_down)
        sleep(2)
        key_options = self.wireless_web_elements.get_key_management_options()
        for opt in key_options:
            if key_management.upper() == opt.text.upper():
                self.auto_actions.click(opt)
                sleep(2)
                break
        return 1

    def _configure_transition_mode(self, status):
        """
        - configure Transition Mode based on status for WPA3 (SAE)

        :param status: (str) status is either enable or disable
        :return: True if Enable, False if Disable
        """
        if status.upper() == "DISABLE":
            if self.wireless_web_elements.get_transition_mode_button().is_selected():
                self.auto_actions.click_reference(self.wireless_web_elements.get_transition_mode_button)
                sleep(2)
            return False
        if status.upper() == "ENABLE":
            self.utils.print_info("Enable Transition Mode Button")
            if not self.wireless_web_elements.get_transition_mode_button().is_selected():
                self.auto_actions.click_reference(self.wireless_web_elements.get_transition_mode_button)
                sleep(10)
            return True

    def _wireless_wifi2_use_checkbox(self, status):
        """
        Select or unselect the wifi2 use check box

        :param status: Enable or Disable
        :return: None
        """
        if status == "Enable":
            self.auto_actions.enable_check_box(self.wireless_web_elements.get_wireless_wifi2_checkbox())
        else:
            self.auto_actions.disable_check_box(self.wireless_web_elements.get_wireless_wifi2_checkbox())
