from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
import xiq.flows.common.ToolTipCapture as tool_tip
from xiq.flows.common.Navigator import Navigator
from xiq.elements.AdvOnboardWebElements import AdvOnboardWebElements


class AdvOnboard(AdvOnboardWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.navigator = Navigator()

    def _got_to_advanced_onboard_tab(self):
        """
        - This method is used to navigate to the device advanced on board tab
        - Flow:
         - Manage --> Devices --> Click on Device Add Button(+) --> Advanced Onboarding
        :return:
        """
        self.navigator.navigate_to_devices()
        self.utils.print_info("Clicking on ADD button...")
        self.auto_actions.click(self.get_devices_add_button())

        self.utils.print_info("Selecting Advanced On boarding Menu")
        self.auto_actions.click(self.get_adv_onboard_add_menu_item())

    def _got_to_next_tab(self):
        """
        - This method is used to click on the next tab
        :return:
        """
        self.utils.print_info("Click on next button....")
        self.auto_actions.click(self.get_onboard_next_button())
        sleep(5)

    def _do_skip_action(self):
        """
        - This method is used to click on the skip button
        :return:
        """
        self.utils.print_info("Click on skip button....")
        self.auto_actions.click(self.get_onboard_skip_button())
        sleep(5)

    def _add_device(self, device_type=None, device_model=None, device_serials=None):
        """
        - This keyword is used to add the real and simulated devices

        :param device_type: type of the device i.e real or simulated
        :param device_model: model of the device ex:AP1130, EXTREME-AEROHIVE, EXOS, VOSS
        :param device_serials: device serial number with comma separated
        :return: True if added else fals
        """
        if device_type.lower() == "real":
            self._add_real_devices(device_model, device_serials)
        elif device_type.lower() == "simulated":
            self._add_simulated_device(device_model)

        self.screen.save_screen_shot()
        sleep(2)

        self._got_to_next_tab()
        if self.get_adv_onboard_form_error():
            for el in self.get_adv_onboard_form_error():
                if "Value should be a 14-character" in el.text:
                    self.utils.print_info(f"Error message:{el.text}")
                    return False

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tip_text)
        for tip_text in tool_tip_text:
            if "failed to onboard" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return False
            elif "Please provide a csv or enter device numbers in text fields" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return False
            elif "successfully onboarded" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return True

        return True

    def _add_simulated_device(self, device_model):
        """
        - This method is used to add the simulated device
        :param device_model:  model of the device ex:AP550, XR200P
        :return: True if successfully added else False
        """
        self.utils.print_info("Click on simulated device radio button")
        self.auto_actions.click(self.get_add_dev_dev_type_sim())

        self.utils.print_info("Click on simulated device drop down")
        self.auto_actions.click(self.get_simulated_device_drop_down())

        self.utils.print_info(f"select device:{device_model}")
        self.auto_actions.select_drop_down_options(self.get_simulated_device_drop_down_opts(), device_model)

    def _add_real_devices(self, device_model, device_serials):
        """
        - This method adds the device based on device and serial numbers

        :param device_model: device name i.e Extreme-Aerohive, Exos, Voss
        :param device_serials: comma separated device serial numbers to add
        :return:
        - True if successfully on boarded the device
        - False if any error message while adding the device
        """

        self.utils.print_info("Clicking on real device radio button")
        self.auto_actions.click(self.get_real_devices_radio_button())

        if device_model.upper() == "EXTREME-AEROHIVE":
            self.utils.print_info("Click on Extreme-Aerohive device tab")
            self.auto_actions.click(self.get_extreme_aerohive_device_tab())

            self.utils.print_info("Entering Extreme-Aerphive device serial numbers")
            self.auto_actions.send_keys(self.get_adv_onboard_serial_text_area(), device_serials)

        elif device_model.upper() == "EXOS":
            self.utils.print_info("Click on EXOS device tab")
            self.auto_actions.click(self.get_exos_device_tab())

            self.utils.print_info("Entering Exos device serial numbers")
            self.auto_actions.send_keys(self.get_exos_serial_text_area(), device_serials)

        elif device_model.upper() == "VOSS":
            self.utils.print_info("Click on Voss device tab")
            self.auto_actions.click(self.get_voss_device_tab())

            self.utils.print_info("Entering Voss device serial numbers")
            self.auto_actions.send_keys(self.get_add_dev_voss_sl_num_textarea(), device_serials)

    def _select_ap_rows_in_location_grid(self, device_serial):
        """
        - This method selects AP row in Manage->Devices based on device's serial number
        :param device_serial: serial number of device
        :return:
        - True if successfully found the device row from list
        - False if no device is found in list
        """
        self.utils.print_info("Get AP rows from grid")
        ap_rows = self.get_assign_loc_ap_grid_rows()
        for row in ap_rows:
            if device_serial in row.text:
                self.utils.print_info("click on device row check box")
                self.auto_actions.click(self.get_assign_loc_ap_grid_checkbox(row))
                return True

    def _assign_location_to_access_point(self, device_serial, **location):
        """
        - This method is used to select location tree node
        :param device_serial: serial number of device to which location is assigned
        :param location : location string on where the device has to be assigned.
        :return:
        """
        self.utils.print_info("Click on access points tab")

        if self.get_assign_loc_ap_button():
            self.auto_actions.click(self.get_assign_loc_ap_button())
        else:
            self.auto_actions.click(self.get_assign_loc_ap_button1())

        if not self._select_ap_rows_in_location_grid(device_serial):
            self.utils.print_info(f"Ap with SN {device_serial} not present in location grid")
            return False
        return self._assign_locations_to_devices(**location)

    def _open_tree_nodes(self, nodes, search_string):
        """
        - This method is used click on the location and country node open icon button
        :param nodes: nodes web elements
        :param search_string: node name to open the icon
        :return: True
        """
        for node in nodes:
            if search_string in node.text:
                attr = node.get_attribute("class")
                if "level-open" in attr:
                    return True
                else:
                    self.utils.print_info("Click on location node open icon")
                    self.auto_actions.click(self.get_location_node_open_icon(node))
                    return True

    def _assign_floor_to_device(self, floor_els, floor):
        """
        - This method assign floor to the device
        :param floor_els:
        :param floor:
        :return: True if assigned else False
        """
        for el in floor_els:
            if floor in el.text:
                self.utils.print_info(f"Clicking on the floor {floor}")
                self.auto_actions.click(el)
                return True

    def _assign_locations_to_devices(self, **location_config):
        """
        - This is the common method for all type of device
        - This method is used to select location tree node

        :param location_config:
        :return: True if assigned else False
        """
        loc_node = location_config.get('loc_node')
        country_node = location_config.get('country_node')
        building_node = location_config.get('building_node')
        floor_node = location_config.get('floor_node')

        self.utils.print_info("click on the assign location button")
        self.auto_actions.click(self.get_assign_loc_button())

        self.utils.print_info("Click on country node open icon")
        country_nodes = self.get_location_nodes()
        if not self._open_tree_nodes(country_nodes, country_node):
            self.utils.print_info(f"Country node {country_node} is not present...")
            return False

        self.utils.print_info("Click on building node open icon")
        build_nodes = self.get_building_nodes()
        if not self._open_tree_nodes(build_nodes, building_node):
            self.utils.print_info(f"Building node {building_node} not present")
            return False

        self.utils.print_info("Select the floor to assign device")
        floor_nodes = self.get_floor_nodes()
        if not self._assign_floor_to_device(floor_nodes, floor_node):
            self.utils.print_info(f"Floor node {floor_node} not present")
            return False

        self.utils.print_info("Click on location assign button")
        self.auto_actions.click(self.get_assign_loc_assign_button())
        sleep(2)

        return True

    def _assign_location(self, search_string, device_type, location):
        """
        - For assigning location need to select the device row in assign location page
        - Then click on assign location button to select the device location

        :param search_string: device row search string in location row grid
        :param location: location config dict
        :param device_type: Type of the device ie. Access Points, Switches, Routers, VPN Gateway
        :return:
        """
        if not location:
            self._got_to_next_tab()
            return True

        self.utils.print_info("Assigning the location to the device......................")
        if device_type.upper() == "ACCESS POINTS":
            if not self._assign_location_to_access_point(search_string, **location):
                return False

        elif device_type.upper() == "SWITCHES":
            self.utils.print_info("Click on switches tab")
            self.auto_actions.click(self.get_assign_loc_switch_button())

        elif device_type.upper() == "ROUTERS":
            self.utils.print_info("Click on routers tab")
            self.auto_actions.click(self.get_assign_loc_router_button())

        elif device_type.upper() == "VPN GATEWAY":
            self.utils.print_info("Click on access points tab")
            self.auto_actions.click(self.get_assign_loc_vpn_gateway())

        self.screen.save_screen_shot()
        sleep(2)

        self._got_to_next_tab()
        return True

    def _assign_branch_id(self, branch_id):
        # @to do
        if not branch_id:
            self._got_to_next_tab()
            return True

    def _create_network_policy(self, policy_config):
        """
        - This method is used to create the network policy
        - If the existing network policy passed, select the existing network policy from the drop down.

        :param policy_config: configuration dictionary to create the network policy
        :return:
        """
        if not policy_config:
            self._do_skip_action()
            return True

        policy_name = policy_config.get('policy_name')
        internal_nw_type = policy_config.get('internal_nw_type', 'None')
        guest_acc_nw_type = policy_config.get('guest_acc_nw_type', 'None')
        existing_nw_policy = policy_config.get('existing_nw_policy', 'None')

        if existing_nw_policy.lower() == 'enable':
            self.utils.print_info("Select existing network policy radio button..")
            self.auto_actions.select_radio_button(self.get_create_nw_policy_use_existing_policy())
            sleep(2)
            self.utils.print_info(f"Selecting existing network policy:{policy_name} from drop down")
            self.auto_actions.click(self.get_create_nw_policy_use_existing_policy_dropdown())
            sleep(2)

            if not self.auto_actions.select_drop_down_options(self.get_create_nw_policy_use_existing_policy_list(), policy_name):
                self.utils.print_info(f"Network policy name:{policy_name} does not exists in drop down options")
                return False
        else:
            self.utils.print_info("Select Create a new network policy radio button")
            self.auto_actions.select_radio_button(self.get_create_nw_policy_new_policy_radio_button())

            self.utils.print_info(f"Enter network policy name:{policy_name}")
            self.auto_actions.send_keys(self.get_create_nw_policy_new_policy_name_input(), policy_name)

            if internal_nw_type == "Enable":
                self.utils.print_info("Enabling internal ssid network")
                self.auto_actions.enable_check_box(self.get_create_nw_policy_type_internal_check_box())
            else:
                self.utils.print_info("Disabling internal ssid network")
                self.auto_actions.disable_check_box(self.get_create_nw_policy_type_internal_check_box())

            if guest_acc_nw_type == "Enable":
                self.utils.print_info("Enabling guest ssid network")
                self.auto_actions.enable_check_box(self.get_create_nw_policy_type_guest_check_box())
            else:
                self.utils.print_info("Disabling guest ssid network")
                self.auto_actions.disable_check_box(self.get_create_nw_policy_type_guest_check_box())

        self.screen.save_screen_shot()
        sleep(2)

        self._got_to_next_tab()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for tip_text in tool_tp_text:
            if "The data is not valid" in tip_text:
                self.utils.print_info("Network policy of same name already exists")
                self.utils.print_info(f"{tip_text}")
                return False
        return True

    def _config_internal_secure_network(self, **config):
        """
        - This method is used to configure the internal secure network with different options
        :param config:
        :return:
        """
        create_credentials = config.get('create_credentials', 'None')
        create_global_password = config.get('create_global_password', 'None')
        users_enters_credentials = config.get('users_enters_credentials', 'None')

        if create_global_password.upper() == "ENABLE":
            global_passwd = config.get('global_passwd')
            self.utils.print_info("Selecting Create global password (PSK) credentials for users to log in to the network radio button")
            self.auto_actions.select_radio_button(self.get_internal_ssid_psk_radio_btn())

            self.utils.print_info(f"Entering the global password:{global_passwd}")
            self.auto_actions.send_keys(self.get_internal_ssid_psk_password(), global_passwd)

        elif create_credentials.upper() == "ENABLE":
            pass

        elif users_enters_credentials.upper() == "ENABLE":
            pass

    def _configure_internal_ssid(self, internal_ssid_config):
        """
        - This method is used to config the Internal SSID section
        - There are two internal networks to configure
         - Secure Network
         - Unsecured Network
        - Secured Network has 3 options
         - Create credentials (PPSK) for users to log in to your network
         - Create global password (PSK) credentials for users to log in to the network.
         - Users enter their credentials to log in to the network.
        - Unsecured (Open) Network has below option
         - Users can access the network without logging in.

        :param internal_ssid_config: internal ssid configuration dictionary
        :return: True if configured successfully else -1
        """
        if not internal_ssid_config:
            self._got_to_next_tab()
            return True

        internal_ssid_name = internal_ssid_config.get('internal_ssid_name')
        network_type = internal_ssid_config.get('network_type')

        self.utils.print_info(f"Entering internal SSID name:{internal_ssid_name}")
        self.auto_actions.send_keys(self.get_conf_internal_ssid_name(), internal_ssid_name)

        if network_type.upper() == "SECURE":
            self.utils.print_info("Selecting the secure network radio button")
            self.auto_actions.select_radio_button(self.get_internal_ssid_secure_nw_radio_btn())
            self._config_internal_secure_network(**internal_ssid_config)

        elif network_type.upper() == "UNSECURE":
            self.utils.print_info("Selecting un secured network radio button")
            self.auto_actions.select_radio_button(self.get_internal_ssid_unsecure_nw_radio_btn())

            self.utils.print_info("Select Users can access the network without logging in radio button")
            self.auto_actions.select_radio_button(self.get_internal_ssid_open_nw_open_access_radio_btn())

        self.screen.save_screen_shot()
        sleep(2)

        self._got_to_next_tab()
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for tip_text in tool_tp_text:
            if "The SSID Profile cannot be saved because the" in tip_text:
                self.utils.print_info(f"{tip_text}")
                return False

        return True

    def _configure_guest_ssid(self, guest_ssid_config):
        """
        - This method is used to configure the Guest Network SSID

        :param guest_ssid_config: Guest SSID configuration dict
        :return: True if configured successfully else -1
        """
        if not guest_ssid_config:
            self._got_to_next_tab()
            return True

        guest_ssid_name = guest_ssid_config.get("guest_ssid_name")
        network_type = guest_ssid_config.get("network_type")

        self.utils.print_info(f"Entering guest SSID name:{guest_ssid_name}")
        self.auto_actions.send_keys(self.get_guest_ssid_name(), guest_ssid_name)

        if network_type.upper() == "UNSECURE":
            guest_access_without_login = guest_ssid_config.get('guest_access_without_login')
            self.auto_actions.select_radio_button(self.get_guest_ssid_unsecured_nw_radio_btn())

            if guest_access_without_login.upper() == "ENABLE":
                self.utils.print_info("Enabling Users can access the network without logging in radio button")
                self.auto_actions.select_radio_button(self.get_guest_ssid_guest_access_without_login_radio_btn())

        elif network_type.upper() == "UNSECURE":
            pass

        self.screen.save_screen_shot()
        sleep(2)

        self._got_to_next_tab()
        return True

    def _configure_network_steps(self, nw_policy_config, internal_ssid, guest_ssid):
        """
        - This method handles the Step4(CREATE NETWORK POLICY), Step5(CONFIGURE INTERNAL SSID) Step6(CONFIGURE GUEST SSID)
        - Step4,5 and 6 are interrelated ie handling in this method

        :param nw_policy_config: network policy config dict
        :param internal_ssid: internal ssid config dict
        :param guest_ssid: guest ssid config dict
        :return: True if created network policy successfully else -1
        """
        self.utils.print_info(f"Network Policy Config:{nw_policy_config}")
        self.utils.print_info(f"Internal SSID Config:{internal_ssid}")
        self.utils.print_info(f"Guest SSID Config:{guest_ssid}")

        if not nw_policy_config:
            self._do_skip_action()
            return True

        internal_nw_type = nw_policy_config.get('internal_nw_type', 'None')
        guest_acc_nw_type = nw_policy_config.get('guest_acc_nw_type', 'None')
        existing_nw_policy = nw_policy_config.get('existing_nw_policy', 'None')

        if not self._create_network_policy(nw_policy_config):
            self.utils.print_info("Failed to create network policy")
            return False

        if existing_nw_policy.lower() == 'enable':
            self.utils.print_info("if existing network is selected, internal network and guest network steps should skip")
            return True

        if internal_nw_type.lower() == "enable":
            if not self._configure_internal_ssid(internal_ssid):
                self.utils.print_info("Failed to configure internal SSID")
                return False

        if guest_acc_nw_type.lower() == "enable":
            if not self._configure_guest_ssid(guest_ssid):
                self.utils.print_info("Failed to configure Guest SSID")
                return False
        return True

    def advance_onboard_access_point(self, device_detail=None, location=None, branch_id=None, nw_policy=None,
                                     internal_ssid=None, guest_ssid=None):
        """
        - This keyword is used to advance onboard the access point
        - This keyword is used to onboard both simulated and real devices
        - Flow:
         - Navigate to Manage --> Devices --> Add(+) -->Advance Onboarding
        - Keyword Usage:
         - ``Advance Onboard Access Point    device_detail=&{DEVICE_DETAIL1}   location=&{LOCATION01}    nw_policy=&{NW_POLICY01}   internal_ssid=&{INTERNAL_SSID1_CONFIG}  guest_ssid=&{GUEST_SSID1_CONFIG}``

        :param device_detail: device detail is the dictionary Ex:
        - &{DEVICE_DETAIL1}    device_type=real         device_model=Extreme-Aerohive    device_sn=06301908310568
        - &{DEVICE_DETAIL2}    device_type=simulated    device_model=AP550

        :param location: location is the dict parameter Ex:
        - &{LOCATION01}    loc_node=auto_location_01   country_node=San Jose    building_node=building_01     floor_node=floor_01

        :param branch_id: branch id argument not required for access point

        :param nw_policy: network policy is the dict parameter Ex:
        - &{NW_POLICY01}      policy_name=AUTO_ADVANCE_TEST    internal_nw_type=Enable     guest_acc_nw_type=Enable
        - &{NW_POLICY01}      policy_name=AUTO_ADVANCE_TEST    internal_nw_type=Disable    guest_acc_nw_type=Enable
        - &{NW_POLICY01}      policy_name=AUTO_ADVANCE_TEST    internal_nw_type=Enable     guest_acc_nw_type=Disable
        - &{NW_POLICY03}      policy_name=OPEN_AUTO            existing_nw_policy=enable

        :param internal_ssid: internal ssid dict parameters Ex:
        - &{INTERNAL_SSID1_CONFIG}   internal_ssid_name=AUTO_TEST    network_type=Secure    create_global_password=Enable    global_passwd=Extreme@123

        :param guest_ssid: guest ssid dict parameters Ex:
        - &{GUEST_SSID1_CONFIG}    guest_ssid_name=AUTO_GUEST        network_type=Unsecure   guest_access_without_login=Enable
        :return:
        - 1 If successfully on boarded
        - -1 failed in ADD DEVICES Step
        - -2 Failed in ASSIGN LOCATION Step
        - -3 Failed in ASSIGN BRANCH ID Step
        - -4 Failed in CREATE NETWORK POLICY step
        """
        self.utils.print_info("Navigate to advance on board tab")
        self._got_to_advanced_onboard_tab()

        device_type = device_detail.get('device_type')
        device_model = device_detail.get('device_model')
        device_sn = device_detail.get('device_sn')

        search_string = device_sn
        if device_type == 'simulated':
            search_string = device_model

        self.utils.print_info("Adding the device")
        if not self._add_device(device_type, device_model, device_sn):
            self.utils.print_info("Failed to add the device in adding device step")
            return -1

        if not self._assign_location(search_string, 'access points', location):
            self.utils.print_info("Failed assign the location to device")
            return -2

        if not self._assign_branch_id(branch_id):
            self.utils.print_info("Failed assign the location to device")
            return -3

        if not self._configure_network_steps(nw_policy, internal_ssid, guest_ssid):
            self.utils.print_info("Failed to configure the network policy")
            return -4

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on advance on board finish button")
        self.auto_actions.click(self.get_onboard_finish_button())
        return 1
