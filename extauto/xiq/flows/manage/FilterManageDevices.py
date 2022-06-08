from extauto.xiq.elements.FilterManageDeviceWebElements import *
from extauto.xiq.elements.FilterManageClientsWebElements import *
from extauto.xiq.elements.DeviceActions import *
from extauto.xiq.flows.manage.Devices import *
from extauto.xiq.flows.manage.Tools import Tools
from extauto.xiq.flows.configure.NetworkPolicy import *
from extauto.xiq.flows.configure.WirelessNetworks import *
from extauto.xiq.flows.configure.UserGroups import *
from extauto.xiq.flows.configure.ExpressNetworkPolicies import *
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.common.Screen import Screen
import extauto.common.CloudDriver


class FilterManageDevices():
    def __init__(self):
        global driver
        self.utils          = Utils()
        self.navigator      = Navigator()
        self.auto_actions   = AutoActions()
        self.web            = WebElementHandler()
        self.filter_element = FilterManageDeviceWebElements()
        self.tools          = Tools()
        self.device_actions = DeviceActions()
        self.device         = Devices()
        self.net_policy     = NetworkPolicy()
        self.client_element = FilterManageClientWebElements()
        self.netExpress     = ExpressNetworkPolicies()
        self.screen = Screen()
        self.driver = extauto.common.CloudDriver.cloud_driver

    def filter_device_by_network_policy(self):

        """ filtering of the devices by a network policy

            prequist: Require at least two onboard APs with each policy
            Usage:
                    filter device by network policy
            :return:  return 1 for successful otherwise -1 with an error
        """

        self.clear_all_filters()
        self.clear_column_filter()
        self._select_filter_by(self.filter_element.real_device_filter_chkbox)
        self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        sn_list, policy_list = self._get_column_values_from_device_page()
        self.utils.print_info("Available device list with the policies " + str(policy_list) + ' ' + str(sn_list))
        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        self._expand_and_collapse_filters(self.filter_element.get_network_policy_filter_link(),
                                          self.filter_element.get_all_policy_filter())

        if sn_list == -1 or len(sn_list) < 2 or policy_list == -1 or len(policy_list) < 2:
            return -1, "Device requires to have a policy"
        self.clear_all_filters()
        for policy in policy_list:
            self.utils.print_info(" ----- Filter the policy  " + str(policy) + " ----- ")
            self.auto_actions.scroll_up()
            self._select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy')
            actual_sn_list, actual_policy_list = self._get_column_values_from_device_page()
            if not actual_sn_list or not actual_policy_list or len(actual_sn_list) == 0 or len(actual_sn_list) == 0:
                return -1, "Filter does not match with the filter " + policy

            if policy != actual_policy_list[0]:
                return -1, "Filter does not match with the filter " + policy
            self._select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy', reset=True)

        return 1, None

    def filter_by_device_type(self, filter='default'):

        """ Filtering of the devices by a device type
            prequist: Require at least one real device and one simulated device
            :param:   filter: filter type
            :return:  return 1 for successful otherwise -1 with an error

            Usage:
                filter by device type   real
                filter by device type   simulate
        """

        self.utils.print_info(" -----  Filter the " + filter + " ---- ")
        self.clear_all_filters()
        self._expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(), filter_type='device type')

        if filter in ["real"]:
            self._select_filter_by(self.filter_element.real_device_filter_chkbox, filter_name='real device')
            sim_lst, real_lst = self._get_column_values_from_device_page("device type")
            if not real_lst and not sim_lst:
                return -1, "The device list is empty with the real device filter "
            if len(sim_lst) != 0 or len(real_lst) == 0:
                return -1, " The device list does not match with the real device filter "
            self._select_filter_by(self.filter_element.real_device_filter_chkbox, filter_name='real device', reset=True)

        if filter in ["simulate"]:
            self._select_filter_by(self.filter_element.simulated_device_filter_chkbox, filter_name='simulated device')
            sim_lst, real_lst = self._get_column_values_from_device_page("device type")
            if not real_lst and not sim_lst:
                return -1, "The device list is empty with the simulated device filter "
            if len(sim_lst) == 0 or len(real_lst) != 0:
                return -1, " The device list does not match with the simulated device filter"

        return 1, None

    def filter_device_by_connection_state(self, ap_sn):

        """ Filtering of the devices by a connection state
            prequist: Require one device connected and one device is disconnected
            :param:   ap_n: ap serial no
            :return:  return 1 for successful otherwise -1 with an error

            Usage :
                 filter_device_by_connection_state    ${AP1_SERIAL}
        """

        self.clear_all_filters()
        self.clear_column_filter()
        sn_list, policy_list = self._get_column_values_from_device_page()
        self._expand_and_collapse_filters(self.filter_element.get_device_state_filter_link(),
                                          self.filter_element.get_state_connected_filter_chkbox(),
                                          filter_type='device state')
        if not sn_list or len(sn_list) == 0: return -1, "The device list is empty"
        status = self.device.get_ap_status(ap_sn)
        if status == 'green':
            self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
            self.auto_actions.click(self.filter_element.get_filter_toggle_link())
            sn_list, policy_list = self._get_column_values_from_device_page()

            self.utils.print_info(" The avaialble sn list " + str(sn_list))
            if ap_sn not in sn_list: return -1, " The device list does not match with the connected filter"
            self.auto_actions.click(self.filter_element.get_filter_toggle_link())
            self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected',
                                   reset=True)
            self._select_filter_by(self.filter_element.device_state_disconnected_filter_chkbox,
                                   filter_name='disconnected')

            self.auto_actions.click(self.filter_element.get_filter_toggle_link())
            sn_list, policy_list = self._get_column_values_from_device_page()

            if not sn_list or ap_sn in sn_list:
                return -1, " The device list does not match with the disconnected filter: "
        else:
            return -1, "The AP device needs to be connected " + str(ap_sn)

        return 1, None

    def filter_device_by_production_type(self):

        """ Verification of the filtering of the device models
            prequist: Require at least two or more APs with the different hardware models
            :return :  return 1 for successful otherwise -1 with an error

            Usage of test case:
                   filter device production type
        """

        self.clear_all_filters()
        self.expand_default_filters()
        self._expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(),
                                          self.filter_element.get_all_device_types_filter_chkbox())
        models = self._get_column_values_from_device_page('product type')
        if not models or len(models) <= 1:
            return -1, "Require at least two different hardware models"
        models = list(dict.fromkeys(models))

        try:
            models.remove("ATOM")
        except:
            self.utils.print_info(" There is no simulate device")

        self._expand_and_collapse_filters(self.filter_element.get_device_prod_type_filter_link(),
                                          self.filter_element.get_all_device_types_filter_chkbox())
        self.utils.print_info(" List of models :" + str(models))
        for model in models:
            self.utils.print_info(" ----- Filter For The Hardware Model " + model + " ----- ")
            model = model[:2] + "_" + model[2:]
            self._select_filter_by(self.filter_element.get_device_prod_type_model_filter_checkbox(model),
                                   filter_name='model ' + str(model))
            actual_models = list(dict.fromkeys(self._get_column_values_from_device_page('product type')))

            if not actual_models:
                return -1, "The device list is empty with the filter model " + str(model)
            actual_model = actual_models[0]
            actual_model = actual_model[:2] + "_" + actual_model[2:]
            if actual_model != model:
                return -1, "The model does not match with the filter model "
            self._select_filter_by(self.filter_element.get_device_prod_type_model_filter_checkbox(model),
                                   filter_name='model ' + str(model), reset=True)

        return 1, None

    def filter_device_by_function(self, filter):

        """ Filtering of the devices by the device function
            prequist: Require at least one AP and one Fasthpath / Hive OS switch
            :param :  filter: filter type
            :return:  return 1 for successful otherwise -1 with an error

            Ussage:
                   filter device by function  ap
                   filter device by function  sw
        """

        self.utils.print_info(" ----- Filter the " + filter + " ----- ")
        ap_lst, sw_lst = self._check_available_devices("device function")
        if ap_lst == -1 or sw_lst == -1:
            return -1, "Require at lease one AP and one Aerohive switch"

        if filter in ['ap']:
            self._select_filter_by(self.filter_element.device_function_access_point_filter_chkbox,
                                   filter_name='access point')
            aps, sws = self._get_column_values_from_device_page("device function")
            if not aps and len(aps) == 0:
                return -1, " The device list is empty with the AP filter"
            aps = list(dict.fromkeys(aps))
            if aps != ap_lst and len(sws) != 0:
                return -1, "The device list does not match with the ap filter"

        if filter in ['switch']:
            self._select_filter_by(self.filter_element.device_function_switch_filter_chkbox, filter_name='switch')
            aps, sws = self._get_column_values_from_device_page("device function")
            if not sws and len(sws) == 0: return -1, " The device list is empty with the switch filter"
            sws = list(dict.fromkeys(sws))
            if sws != sw_lst and len(aps) != 0: return -1, "The device list does not match with the switch filter"

        return 1, None

    def filter_device_by_unmanaged_and_managed_state(self):

        """ Filtering of the devices by the unmanaged_and_managed_state
            prequist: Require at least one or more onboard devices
            :return:  return 1 for successful otherwise -1 with an error

            Usage:
                       filter_device_by_unmanaged_and_managed_state
        """

        sn_list, host_list = self._check_available_devices(filter='management state', real_device=True)
        if sn_list == -1:
            return -1, host_list

        self.utils.print_info(" ----- Filter The Unmanaged Device -----")
        self._expand_and_collapse_filters(self.filter_element.get_device_data_management_state_filter_link(),
                                          filter_type='management state')
        self._action_change_managed_state(sn_list[0], "unmanaged")
        self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected',
                               reset=True)
        self._select_filter_by(self.filter_element.device_data_management_unmanaged_chkbox, filter_name='unmanaged')
        self.tools.wait_til_ap_change_status(sn_list[0], host_list[0], 180, "red")
        actual_sn_list, actual_host_list = self._get_column_values_from_device_page("management state")

        if not actual_sn_list and len(actual_sn_list) == 0:
            return -1, "The device list is empty with the unmanaged filter"
        if actual_sn_list[0] != sn_list[0]:
            return -1, "The device list does not match with the unmanaged state"

        self.utils.print_info(" ----- Filter The Managed Device -----")
        self._action_change_managed_state(sn_list[0], "managed")
        self._select_filter_by(self.filter_element.device_data_management_unmanaged_chkbox, filter_name='unmanaged',
                               reset=True)
        self._select_filter_by(self.filter_element.device_data_management_managed_chkbox, filter_name='managed')
        self.tools.wait_til_ap_change_status(sn_list[0], host_list[0], 300, "green")
        actual_sn_list, actual_host_list = self._get_column_values_from_device_page("management state")

        if not actual_sn_list and len(actual_sn_list) == 0:
            return -1, "The device list is empty with the managed filter"
        if actual_sn_list[0] != sn_list[0]:
            return -1, "The device list is empty with the managed filter"

        return 1, None

    def filter_all_devices_by_software_version(self):

        """ Filtering of the devices by the software version
            prequist: Require at least two or more onboard different hardware devices
            :return:  return 1 for successful otherwise -1 with an error

            Usage:
                filter_all_devices_by_software_version
        """

        soft_lst = self._check_available_devices('firmware version')
        if soft_lst == -1:
            return -1, "Device list is empty"
        self.utils.print_info(" soft_lst " + str(soft_lst))
        real_modeL_lst = self._parse_string(soft_lst)
        self._expand_and_collapse_filters(self.filter_element.get_device_soft_version_link())

        for model in real_modeL_lst:
            self.utils.print_info(" ----- filter the versions ----- " + model)
            model_element = self.filter_element.get_device_soft_version_chkbox(model)
            self._select_filter_by(model_element, filter_name='firmware version')
            soft_lst = self._get_column_values_from_device_page("firmware version")

            if not soft_lst or len(soft_lst) == 0:
                return -1, "The device list is empty with the filter " + model
            actual_model_lst = list(dict.fromkeys(soft_lst))
            actual_model_lst = self._parse_string(actual_model_lst)
            for actual_model in actual_model_lst:
                if actual_model != model:
                    return -1, "The device does not match with the version " + str(actual_model) + ' ' + str(model)
            self._select_filter_by(model_element, filter_name='firmware version', reset=True)

        return 1, None

    def filter_device_by_ssid(self):

        """ Filtering of the devices by ssid
            prequist: Require at least two onboard devices with with two different wireless networks
            :return: return 1 for successful otherwise -1 with an error

            Usage:
                 filter device by ssid
        """
        self.clear_all_filters()
        self.clear_column_filter()
        self._select_filter_by(self.filter_element.real_device_filter_chkbox)
        self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
        self._select_filter_by(self.filter_element.device_function_access_point_filter_chkbox,
                               filter_name='access point')
        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        sn_list, policy_list = self._get_column_values_from_device_page()
        self.utils.print_info(str(policy_list) + ' ' + str(sn_list))
        if policy_list == -1:
            return -1, "No devices has assigned any policy"

        policy_ssid, ssid_name = self.net_policy.get_all_ssids_in_policy(policy_list[0], new_ssid=True,
                                                                             special_char=True)
        if policy_ssid == None:
            return -1, "Device has no ssid"

        self.clear_all_filters()
        self._expand_and_collapse_filters(self.filter_element.get_device_ssid_filter_link())
        for ssid in policy_ssid[policy_list[0]]:
            self.utils.print_info(
                " ------ Filter the ssid ------ " + str(ssid) + ' in the policy ' + str(policy_list[0]))
            ssid_element = self.filter_element.get_device_ssid_filter_checkbox(str(ssid))
            self._select_filter_by(ssid_element, filter_name='ssid')
            act_sn_list, act_policy_list = self._get_column_values_from_device_page()
            if not act_policy_list or len(act_policy_list) == 0: return -1, "SSID does not match"

            act_policy_list = list(dict.fromkeys(act_policy_list))
            if policy_list[0] not in act_policy_list: return -1, "SSID does not match"
            self._select_filter_by(ssid_element, filter_name='ssid', reset=True)

        return 1, ssid_name

    def filter_device_with_audit_match_and_mismatch(self, policy=None, serial=None):

        """ Filtering of the devices by audit status
            prequist: Require at least one or more onboard devices with a different policy
            :param    policy: policy name
            :param    serial: ap serial nu,,ber
            :return   return 1 if succesful and ssid name

            usage:
                 filter_device_with_audit_match_and_mismatch  policy=ppsk  serial=033449555
        """

        self.clear_all_filters()
        self.clear_column_filter()
        ssid_list, ssid_name = self.net_policy.get_all_ssids_in_policy(policy, new_ssid=True, special_char=False)
        self.utils.print_info(" Policy name contains this list of ssids " + str(policy) + ' ' + str(ssid_list))
        self.navigator.navigate_to_devices()
        sleep(5)

        self.utils.print_info(f"Select ap row with serial {serial}")
        if not self.device.select_device(serial):
            self.utils.print_info(f"ap {serial} is not present in the grid")
            return -1, "ap is not present in the grid"
        sleep(2)
        self.device._assign_network_policy(policy)

        self.utils.print_info(" ------  Filter the audit match device " + policy + " ------")
        self._select_filter_by(self.filter_element.device_audit_config_match_filter_chkbox, filter_name='match device')
        sns, policies = self._get_column_values_from_device_page()
        self.utils.print_info(" list of policies with the audit match filter : " + str(sns) + ' ' + str(policies))

        if not policy or policy not in policies or serial not in sns:
            return -1, "The audit does not match"
        self._select_filter_by(self.filter_element.device_audit_config_match_filter_chkbox, filter_name='match device',
                               reset=True)

        self.utils.print_info(" ------  Filter the audit mismatch device " + policy + " ------")
        self._select_filter_by(self.filter_element.device_audit_config_mismatch_filter_chkbox, filter_name='mistmatch')
        self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected',
                               reset=True)
        self._select_filter_by(self.filter_element.real_device_filter_chkbox, filter_name='real device', reset=True)
        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        sns, policies = self._get_column_values_from_device_page()
        self.utils.print_info(
            " list of policies with the the audit mismatch filter : " + str(sns) + ' ' + str(policies))

        if policy in policies or serial in sns:
            return -1, ssid_name

        return 1, ssid_name

    def filter_device_by_user_profiles(self, filter='default', serial=None, **policies):

        """ Filtering of the devices by user profiles
            prequist: Require at least one onboard devices with a network policy
            :param: serial: ap serial
            :param: policies: list of policies
            :return: return 1 if succesful and ssid name

            usage :
                       filter device by user profiles  guest
                       filter device by user profiles  profile
        """
        self.utils.print_info(" ----- Filter the " + filter + " -----")
        policy1 = policies.get('policy1')
        policy2 = policies.get('policy2')
        self.utils.print_info("Policy1 " + policy1 + " policy2 " + policy2)

        if filter in ['guest']:
            self.net_policy.delete_all_ssid_in_policy(policy1)
            self.utils.print_info(" Create a new guest wireless network")
            ssid_list, ssid_name = self.net_policy.get_all_ssids_in_policy(policy1, new_ssid=True,
                                                                           special_char=False)
            self.clear_all_filters()
            self.expand_default_filters()
            self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected',
                                   reset=True)
            self._select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox,
                                   filter_name='guest profile')

            actual_sns, actual_policies = self._get_column_values_from_device_page()
            if not actual_sns and not actual_policies: return -1, ssid_name
            if serial not in actual_sns: return -1, ssid_name

            return 1, ssid_name

        if filter in ['default']:
            ssid_name, cwp_name = self.utils.get_random_string(), self.utils.get_random_string()
            self.netExpress.create_open_auth_express_network_policy(policy2, ssid_name, cwp_name)
            self.navigator.navigate_to_devices()
            sleep(5)

            self.utils.print_info(f"Select ap row with serial {serial}")
            if not self.device.select_device(serial):
                self.utils.print_info(f"ap {serial} is not present in the grid")
                return -1, "ap is not present in the grid"
            sleep(2)
            self.device._assign_network_policy(policy2)
            self.clear_all_filters()
            self.expand_default_filters()
            self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected',
                                   reset=True)
            self._select_filter_by(self.filter_element.device_default_profile_filter_chkbox,
                                   filter_name='default profile')
            actual_sns, actual_policies = self._get_column_values_from_device_page()
            if not actual_sns and not actual_policies:
                return -1, "Default profile filter does not match"
            if serial not in actual_sns:
                return -1, "Default profile filter does not match"

            if not self.device.select_device(serial):
                self.utils.print_info(f"Switch {serial} is not present in the grid")
                return -1, "ap is not present in the grid"
            sleep(2)

            self.utils.print_info("Policy1 " + policy1 + " policy2 " + policy2)
            self.device._assign_network_policy(policy1)

            return 1, ssid_name

    def filter_client_by_device_function(self, filter):

        """ Filtering of the clients based on the device function
            prequist: AP and switch need to be onboarded and need one client to switch and one client connect to AP
                Usage:
                        filter_client_by_device_function  ap
                        filter_client_by_device_function  switch

            Jira: APC - 3741
        """

        if filter in ['ap', 'switch', 'wireless_connection', 'wired_connection']:
            self.clear_all_filters('client filter')
        elif filter in ['360_ap', '360_switch', '360_wireless_connection', '360_wired_connection']:
            self.clear_all_filters('ml_insight filter')

        if filter in ['ap', 'wireless_connection', '360_ap', '360_wireless_connection']:
            if filter in ['ap', '360_ap']:
                self._expand_and_collapse_filters(self.client_element.get_filter_client_device_function_link(),
                                                  'client')
                self._select_filter_by(self.client_element.filter_client_device_function_ap_chkbox, filter_name=filter)

            elif filter in ['wireless_connection', '360_wireless_connection']:
                self._expand_and_collapse_filters(self.client_element.get_filter_client_connection_link(), 'client')
                self._select_filter_by(self.client_element.filter_client_device_wireless_connection_chkbox,
                                       filter_name=filter)

            aps, sws = self._get_column_values_from_device_page("client connection")
            self.utils.print_info(" aps and sws  " + str(aps) + ' ' + str(sws))
            self.utils.print_info(" Validate the filter ")
            if len(aps) == 0 or not aps or len(sws) != 0:
                return -1, "The wireless connections do not match with the " + filter + " filter "
            self._select_filter_by(self.client_element.filter_client_device_function_ap_chkbox, filter_name=filter,
                                   reset=True)

        if filter in ['switch', '360_switch', 'wired_connection', '360_wired_connection']:
            if filter in ['switch', '360_switch']:
                self._expand_and_collapse_filters(self.client_element.get_filter_client_device_function_link(),
                                                  'client')
                self._select_filter_by(self.client_element.filter_client_device_function_sw_chkbox, filter_name=filter)

            elif filter in ['wired_connection', '360_wired_connection']:
                self._expand_and_collapse_filters(self.client_element.get_filter_client_connection_link(), 'client')
                self._select_filter_by(self.client_element.filter_client_device_wired_connection_chkbox,
                                       filter_name='wired')

            aps, sws = self._get_column_values_from_device_page("client connection")
            if not sws or len(sws) == 0 or len(aps) != 0:
                return -1, "The wired connections do not match with the " + filter + " filter "

        return 1, None

    def filter_client_by_os_type(self, filter):

        """ Filtering of the clients based on the OS type
            prequist: One or two clients should be connected via Wifi either Windows, Mac OS
            Usage:
                       filter client by os type
        """

        self.utils.print_info(" ----- Filter the " + filter + "-----")
        if filter in ['os']:
            self.clear_all_filters('client filter')
        elif filter in ['360_os']:
            self.clear_all_filters('ml_insight filter')

        os_types_list = self._get_column_values_from_device_page("client os type")
        os_types_list = [x.lower() for x in os_types_list if x]
        self.utils.print_info("Available client OS types: " + str(os_types_list))
        if not os_types_list or len(os_types_list) == 0:
            return -1, "Require at least one Mac or Window client connects to a wireless"

        self._expand_and_collapse_filters(self.client_element.get_filter_client_os_type_link(), 'client')
        if 'mac' in str(os_types_list).lower():
            self._select_filter_by(self.client_element.filter_client_mac_os_type_chkbox, filter_name='mac os')
            os_types_list = self._get_column_values_from_device_page("client os type")
            self.utils.print_info(" Validate the filter ")
            os_types_list = [x.lower() for x in os_types_list if x]
            if 'mac' not in str(os_types_list).lower():
                return -1, "Mac filter does not match " + str(os_types_list)
            self._select_filter_by(self.client_element.filter_client_mac_os_type_chkbox, filter_name='mac os',
                                   reset=True)

        if 'window' in str(os_types_list).lower():
            self._select_filter_by(self.client_element.filter_client_windows_os_type_chkbox, filter_name='windows')
            os_types_list = self._get_column_values_from_device_page("client os type")
            os_types_list = [x.lower() for x in os_types_list if x]
            if 'window' not in str(os_types_list).lower():
                return -1, "Windows filter does not match " + str(os_types_list)
            self._select_filter_by(self.client_element.filter_client_windows_os_type_chkbox, filter_name='windows',
                                   reset=True)
        self._expand_and_collapse_filters(self.client_element.get_filter_client_os_type_link(), 'client', collapse=True)

        return 1, None

    def filter_client_by_ssid(self, filter):

        """ Filtering of the clients based on the SSID
            prequist: 1 Ap should be onboarded with wireless network
            Usage:
                     filter client by ssid  ssid
                     filter client by ssid  360_ssid

        """
        self.utils.print_info("----- filter the " + filter + " ------ ")
        if filter in ['ssid']:
            self.clear_all_filters('client filter')
        elif filter in ['360_ssid']:
            self.clear_all_filters('ml_insight filter')

        self._expand_and_collapse_filters(self.client_element.get_client_ssid_filter_link(), 'client')
        ssids = self._get_column_values_from_device_page("client ssid")
        ssids = [x for x in ssids if x]
        self.utils.print_info(" Available SSIDs " + str(ssids))
        if not ssids or len(ssids) <= 0:
            return -1, "Require at least one onboared device connecting 1 wirless network"
        ssids = list(dict.fromkeys(ssids))

        count = 1
        for ssid in ssids:
            ssid_element = self.client_element.get_client_ssid_filter_checkbox(str(ssid))
            self._select_filter_by(ssid_element, filter_name='ssid')
            actual_ssids = self._get_column_values_from_device_page("client ssid")
            if not actual_ssids: return -1, "The SSID list is empty with the filter " + str(ssid)
            for actual_ssid in actual_ssids:
                if str(actual_ssid) != str(ssid): return -1, "The SSID does not match " + str(actual_ssid) + ' ' + str(
                    ssid)
            self._select_filter_by(ssid_element, filter_name='ssid', reset=True)
            if count == 1: break

        self._expand_and_collapse_filters(self.client_element.get_client_ssid_filter_link(), 'client', collapse=True)

        return 1, None

    def filter_client_by_user_profiles(self, ssid_name, filter='default'):
        """ Filtering of the Clients based on the user_profiles
            Usage :
                filter client by user profiles  ${ssid_name}   guess profile
                filter client by user profiles  ${ssid_name}   default profile
        """

        if filter in ['guest profile']:
            sleep(60)
            self.utils.print_info(" ------ Filter the " + filter + "-----")
            self.clear_all_filters('client filter')
            self._expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), 'client')
            self._select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox,
                                   filter_name='guest profile')
            ssid_list = self._get_column_values_from_device_page("client ssid")
            if not ssid_list or len(ssid_list) == 0:
                return -1, " There is no wireless connection with the guess profile filter"
            if ssid_name not in ssid_list:
                return -1, " The client ssid does not match with the guest profile filter " + str(
                    ssid_name) + ' ' + str(ssid_list)
            self._select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox,
                                   filter_name='guess profile', reset=True)

            self._expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), 'client', True)

        return 1, None

    def location_action_type(self, location='default', type='search'):
        """ This keyword search a location in the filter list
            :param : location: name of location, building, floor
            :param : type: either select, unselect, search
            :param : negative: True: location matches

            Usage of test case:
                      Test1: Filter a location
                        location action type     location=auto_location_01    type=select location
                        location action type     location=auto_location_01    type=search location
                        location action type     location=auto_location_01    type=unselect location
                        location action type     location=auto_location_01    type=select save filter
        """

        self.utils.print_info(" Search a location " + location)
        self._expand_and_collapse_filters(self.filter_element.get_locations_link(), self.filter_element.get_all_policy_filter())
        self.auto_actions.scroll_up()
        sleep(5)
        if type == 'search location':
            self.auto_actions.send_keys(self.filter_element.get_location_search_input(), location)
            if self.web.get_element(self.filter_element.get_locations_filter(location)) != None:
                self.auto_actions.click(self.web.get_element(self.filter_element.get_locations_filter(location)))
            else:
                return 1, None
        elif type in ['select location', 'click']:
            if not self.auto_actions.click(self.web.get_element(self.filter_element.get_locations_filter(location))):
                self.auto_actions.click(self.web.get_element(self.filter_element.get_locations_filter(location)))
        elif type in ['unselect location']:
            if self.web.get_element(self.filter_element.get_locations_filter(location)).is_selected():
                #self.auto_actions.click(self.web.get_element(self.filter_element.get_locations_filter(location)))
                self.driver.execute_script("arguments[0].click();", self.web.get_element(self.filter_element.get_locations_filter(location)))
            self.auto_actions.click(self.filter_element.get_apply_filter_button())

            if self.web.get_element(self.filter_element.get_locations_filter(location)).is_selected():
                return -1, "Can not unselect the location"
            else:
                return 1, None

        elif type in ['select save filter']:
            locator_save_filter = self.filter_element.get_locations_filter(location)
            self.auto_actions.click(self.web.get_element(locator_save_filter))
            self.driver.execute_script("arguments[0].click();", self.web.get_element(locator_save_filter))
            if not self.web.get_element(locator_save_filter).is_selected():
                return -1, "Can not select a save filter"
            else:
                return 1, None

        self.auto_actions.click(self.filter_element.get_apply_filter_button())
        if not self.web.get_element(self.filter_element.get_locations_filter(location)).is_selected():
            return -1, "Can not select the location"
        else:
            return 1, None


    def verify_device_location(self, *devices, negative=False):
        """ This keyword verifies the devices associating the location
            :param : *devices: list of devices associating the location
            :param : negative: True: a device should not exist

            Usage of test case:
                verify_device_location   ${sn1}  ${sn2}

        """

        self.utils.print_info(" Validate a device associating with the location " + str(devices))
        self.clear_column_filter()
        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        sn_list, policy_list = self._get_column_values_from_device_page()
        self.utils.print_info(" sn list " + str(sn_list) + ' ' + str(policy_list))

        for device in devices:
            self.utils.print_info(" Validate the device location " + device)
            if not negative:
                if sn_list is None or not sn_list:
                    return -1, "device does not match"
                else:
                    if device not in sn_list: return -1, "device does not match"
            else:
                if sn_list is None or not sn_list: return str(1), None
                if device in sn_list: return -1, "device does not match"

        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        return 1, None

    def set_device_type_filter(self, filter='All', select='true'):
        """ Sets the device type filter to the specified value
            Usage of test case:
                Set Device Type Filter  All  true
                Set Device Type Filter  Plan Devices  true
                Set Device Type Filter  Real Devices  true
                Set Device Type Filter  Simulated Devices  true
                Set Device Type Filter  All  false
                Set Device Type Filter  Plan Devices  false
                Set Device Type Filter  Real Devices  false
                Set Device Type Filter  Simulated Devices  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Device Type By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Device Types filter section if it is not yet expanded
        device_type_filter_collapsed = self.filter_element.get_device_type_filter_link_collapsed()
        if device_type_filter_collapsed and device_type_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_device_type_filter_link())

        # Get the check box element to toggle
        element = None
        if filter == 'All':
            element = self.filter_element.get_all_device_types_filter_chkbox()
        elif filter == 'Plan Devices':
            element = self.filter_element.get_plan_device_filter_chkbox()
        elif filter == 'Real Devices':
            element = self.filter_element.get_real_device_filter_chkbox()
        elif filter == 'Simulated Devices':
            element = self.filter_element.get_simulated_device_filter_chkbox()

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def set_device_connection_state_filter(self, filter='All', select='true'):
        """ Sets the device connection state filter to the specified value
            Usage of test case:
                Set Device Connection State Filter  All  true
                Set Device Connection State Filter  Connected  true
                Set Device Connection State Filter  Disconnected  true
                Set Device Connection State Filter  Pre-Provisioned  true
                Set Device Connection State Filter  All  false
                Set Device Connection State Filter  Connected  false
                Set Device Connection State Filter  Disconnected  false
                Set Device Connection State Filter  Pre-Provisioned  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Device Connection State By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Device Connection State filter section if it is not yet expanded
        connection_state_filter_collapsed = self.filter_element.get_device_state_filter_link_collapsed()
        if connection_state_filter_collapsed and connection_state_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_device_state_filter_link())

        # Get the check box element to toggle
        element = None
        if filter == 'All':
            element = self.filter_element.get_device_state_all_filter_chkbox()
        elif filter == 'Connected':
            element = self.filter_element.get_state_connected_filter_chkbox()
        elif filter == 'Disconnected':
            element = self.filter_element.get_state_disconnected_filter_chkbox()
        elif filter == 'Pre-Provisioned':
            element = self.filter_element.get_state_preprovisioned_filter_chkbox()

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def set_device_management_state_filter(self, filter='All', select='true'):
        """ Sets the device management state filter to the specified value
            Usage of test case:
                Set Device Management State Filter  All  true
                Set Device Management State Filter  Managed  true
                Set Device Management State Filter  New  true
                Set Device Management State Filter  Setting Up  true
                Set Device Management State Filter  Unmanaged  true
                Set Device Management State Filter  All  false
                Set Device Management State Filter  Managed  false
                Set Device Management State Filter  New  false
                Set Device Management State Filter  Setting Up  false
                Set Device Management State Filter  Unmanaged  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Device Management State By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Device Management State filter section if it is not yet expanded
        mgmt_state_filter_collapsed = self.filter_element.get_device_data_management_state_filter_link_collapsed()
        if mgmt_state_filter_collapsed and mgmt_state_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_device_data_management_state_filter_link())

        # Get the check box element to toggle
        element = None
        if filter == 'All':
            element = self.filter_element.get_device_management_all_state_chkbox()
        elif filter == 'Managed':
            element = self.filter_element.get_device_management_managed_state_chkbox()
        elif filter == 'New':
            element = self.filter_element.get_device_management_new_state_chkbox()
        elif filter == 'Setting Up':
            element = self.filter_element.get_device_management_setting_up_state_chkbox()
        elif filter == 'Unmanaged':
            element = self.filter_element.get_device_management_unmanaged_state_chkbox()

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def set_device_function_filter(self, filter='All', select='true'):
        """ Sets the device function filter to the specified value
            Usage of test case:
                Set Device Function Filter  All  true
                Set Device Function Filter  Switch  true
                Set Device Function Filter  XIQSE  true
                Set Device Function Filter  All  false
                Set Device Function Filter  Switch  false
                Set Device Function Filter  XIQSE  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Device Function By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Device Function filter section if it is not yet expanded
        func_filter_collapsed = self.filter_element.get_device_function_filter_link_collapsed()
        if func_filter_collapsed and func_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_device_function_filter_link())

        # Get the check box element to toggle
        element = None
        if filter == 'All':
            element = self.filter_element.get_device_function_all_chkbox()
        elif filter == 'Switch':
            element = self.filter_element.get_device_function_switch_chkbox()
        elif filter == 'XIQSE':
            element = self.filter_element.get_device_function_xiqse_chkbox()

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def set_device_product_type_filter(self, filter='All', select='true'):
        """ Sets the device product type filter to the specified value
            Usage of test case:
                Set Device Product Type Filter  All  true
                Set Device Product Type Filter  X460_G2_48t_10_G4  true
                Set Device Product Type Filter  XIQ_SE  true
                Set Device Product Type Filter  All  false
                Set Device Product Type Filter  X460_G2_48t_10_G4  false
                Set Device Product Type Filter  XIQ_SE  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Device Product Type By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Device Product Type filter section if it is not yet expanded
        prod_filter_collapsed = self.filter_element.get_device_function_filter_link_collapsed()
        if prod_filter_collapsed and prod_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_device_function_filter_link())

        # Get the check box element to toggle
        element = None
        if filter == "All":
            element = self.filter_element.get_device_prod_type_all_filter_checkbox()
        else:
            cb_locator = self.filter_element.get_device_prod_type_model_filter_checkbox(filter)
            if cb_locator:
                element = self.web.get_element(cb_locator)

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def set_device_software_version_filter(self, filter='All', select='true', exact_match='true'):
        """ Sets the device software version filter to the specified value
            Usage of test case:
                Set Device Software Version Filter  All  true
                Set Device Software Version Filter  21.4.10.6  true
                Set Device Software Version Filter  All  false
                Set Device Software Version Filter  30.7.11-patch1-23  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Device Software Version By {filter} exact {exact_match} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Device Software Version filter section if it is not yet expanded
        soft_ver_filter_collapsed = self.filter_element.get_device_soft_version_link_collapsed()
        if soft_ver_filter_collapsed and soft_ver_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_device_soft_version_link())

        # Get the check box element to toggle
        element = None
        if filter == "All":
            element = self.filter_element.get_device_soft_version_all_chkbox()
        else:
            if exact_match == "true":
                cb_locator = self.filter_element.get_device_soft_version_chkbox(filter)
            else:
                cb_locator = self.filter_element.get_device_soft_version_chkbox_contains(filter)
            if cb_locator:
                element = self.web.get_element(cb_locator)

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def set_cloud_config_groups_filter(self, filter='All', select='true'):
        """ Sets the cloud config groups filter to the specified value
            Usage of test case:
                Set Cloud Config Groups Filter  All  true
                Set Cloud Config Groups Filter  Model_AP_410C  true
                Set Cloud Config Groups Filter  All  false
                Set Cloud Config Groups Filter  Model_AP_410C  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set Cloud Config Group By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the Cloud Config Group filter section if it is not yet expanded
        ccg_filter_collapsed = self.filter_element.get_cloud_config_group_filter_link_collapsed()
        if ccg_filter_collapsed and ccg_filter_collapsed.is_displayed():
            self.auto_actions.click(self.filter_element.get_cloud_config_group_filter_link())

        # Get the check box element to toggle
        element = None
        if filter == "All":
            element = self.filter_element.get_cloud_config_group_all_checkbox()
        else:
            cb_locator = self.filter_element.get_cloud_config_group_checkbox(filter)
            if cb_locator:
                element = self.web.get_element(cb_locator)

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def toggle_filter_check_box(self, element, select='true'):
        """ Toggles the filter check box to have the specified selection state

        :param element: check box to toggle
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        ret_val = 1

        # Click the check box if it is not already in the desired state
        if element:
            self.auto_actions.move_to_element(element)
            if select == 'true':
                self.utils.print_info("Selecting filter check box")
                self.auto_actions.enable_check_box(element)
            else:
                self.utils.print_info("Deselecting filter check box")
                self.auto_actions.disable_check_box(element)
        else:
            self.utils.print_info("Unable to locate filter check box")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def open_filter_panel(self):
        """ Opens the filter panel if it isn't already open
        """
        ret_val = -1
        filter_by_title = self.filter_element.get_filter_by_title()
        if filter_by_title:
            if not filter_by_title.is_displayed():
                filter_toggle = self.filter_element.get_filter_toggle_link()
                if filter_toggle:
                    self.auto_actions.click(filter_toggle)
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to click filter icon to open filter panel")
            else:
                self.utils.print_info("Filter panel already open")
                ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Filter By' title element")

        return ret_val

    def close_filter_panel(self):
        """ Closes the filter panel if it is open
        """
        ret_val = -1
        filter_by_title = self.filter_element.get_filter_by_title()
        if filter_by_title:
            if filter_by_title.is_displayed():
                filter_toggle = self.filter_element.get_filter_toggle_link()
                if filter_toggle:
                    self.auto_actions.click(filter_toggle)
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to click filter icon to close filter panel")
            else:
                self.utils.print_info("Filter panel already closed")
                ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Filter By' title element")

        return ret_val


    #========================
    # supported functions
    def clear_all_filters(self, navigator='device filter'):
        """ Clearing all applied and saved filters
            :param navigator: navigator to a filtered page
        """

        self.utils.print_info("Start --> Clear all filters ")
        if navigator == 'device filter':
            self.navigator.navigate_to_devices()
            if not self.filter_element.get_device_type_filter_link().is_displayed():
                self.utils.print_info("Expand the filter toggle ")
                self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        elif navigator == 'client filter':
            self.navigator.navigate_to_clients()
            if not self.client_element.get_filter_client_device_function_link().is_displayed():
                self.auto_actions.click(self.filter_element.get_filter_toggle_link())
            if self.client_element.get_page_size_100_link():
                self.auto_actions.click(self.client_element.get_page_size_100_link())
        elif navigator == 'ml_insight filter':
            self.navigator.navigate_to_client360()
            if not self.client_element.get_filter_client_device_function_link().is_displayed():
                self.auto_actions.click(self.filter_element.get_filter_toggle_link())
            if self.client_element.get_page_size_100_link():
                self.auto_actions.click(self.client_element.get_page_size_100_link())
        elif navigator == 'application filter':
            self.navigator.navigate_manage_application()
            if not self.client_element.get_filter_client_device_function_link().is_displayed():
                self.auto_actions.click(self.filter_element.get_filter_toggle_link())

        all_filters = self.filter_element.get_my_saved_filter_list()
        if all_filters:
            self.utils.print_info("Start clearing my filter ")
            sleep(5)
            for index in range(1, len(all_filters) + 1):
                self.auto_actions.click(self.filter_element.get_list_del_index_filter())
                self.tools.wait_til_elements_avail(self.filter_element.dialog_yes_filter_btn, 60, False)
                self.tools.click_til_element_avail(self.filter_element.get_del_yes_btn())
                sleep(2)

        all_applied_filters = self.filter_element.get_applied_filter_list()
        if all_applied_filters:
            self.utils.print_info("start clearing the applied filters ")
            self.auto_actions.click(self.filter_element.get_applied_clear_filter_link())
            sleep(3)

        return 1

    def _expand_and_collapse_filters(self, element, inner_element='default', filter_type='policy', collapse=False):
        """ expand and collapse the filter links
            :param element : link of filter
            :param filter_type: page contains the filters
            :param collapse: collapse the filter toggle when it is true
        """

        sleep(5)
        self.utils.print_info(" Start -- > Expand / collapse filters " + filter_type)
        if filter_type == 'device type':
            self.tools.wait_til_elements_avail(self.filter_element.device_type_filter_link, 30, False)
        if filter_type == 'client':
            self.tools.wait_til_elements_avail(self.client_element.filter_client_device_function_link, 30, False)

        if inner_element != 'default':
            if inner_element == None:
                self.auto_actions.click(element)

        if collapse:
            self.auto_actions.click(self.filter_element.get_filter_toggle_link())

        return 1

    def _select_filter_by(self, *locators, filter_name='default', reset=False):
        """ Select and unselect the filter checkboxes
            :param locators : list of checkboxs
            :param reset : clear the checkbox when it is true
        """

        sleep(5)
        try:
            for locator in locators:
                element = self.web.get_element(locator)
                if not element: return False, "Not able to find a filter selection and the test aborts " + str(locator)
                if not reset:
                    if not element.is_selected():
                        self.utils.print_info(" Select filter  " + filter_name)
                        self.utils.print_info(" element.text   " + element.text)
                        self.auto_actions.click(element)
                else:
                    if element.is_selected():
                        self.utils.print_info(" Unselect filter   " + filter_name)
                        self.auto_actions.click(element)
            self.auto_actions.click(self.filter_element.get_apply_filter_button())
        except:
            return False, None

        return True, None

    def save_filter(self):

        """ create a filter and save the filter
        :param: None
        :return filter_name (name of filter)
        """

        self.utils.print_info("Start --> Save filter ")
        filter_name = self.utils.get_random_string(8)
        self.auto_actions.click(self.filter_element.get_save_filter_btn())
        self.tools.wait_til_elements_avail(self.filter_element.dialog_input_filter_filename_txt, 30, False)
        self.utils.print_info(" Enter the filter saved name  " + filter_name + ' and click on Save')
        self.auto_actions.send_keys(self.filter_element.get_enter_filter_name_txt(), filter_name)
        self.auto_actions.click(self.filter_element.get_dialog_save_btn())

        return filter_name

    def clear_applied_filters(self, single_del=False):

        self.utils.print_info("Start --> Clear applied filters ")
        if not single_del:
            count = self.filter_element.get_applied_filter_list()
            if count == None or not count: return 1, "No filters to clear"
            else : count = len(count)
        else:
            count = 1

        try:
            for i in range(count):
                 self.auto_actions.click(self.filter_element.get_applied_filter_del_x_button())
        except:
                return -1, "Not able to click"
        return 1, None

    def clear_location_search(self):
        self.utils.print_info("Clear Location Filter ")

        try:
            self.auto_actions.click(self.filter_element.get_location_clear_icon())
        except:
            return -1, "Not able to clear the location search"

        return 1, None

    def clear_my_filters(self):
        self.utils.print_info("Start clearing my filter ")
        try:
            all_filters = self.filter_element.get_my_saved_filter_list()

            for index in range(1, len(all_filters) + 1):
                self.auto_actions.click(self.filter_element.get_list_del_index_filter())
                self.tools.wait_til_elements_avail(self.filter_element.dialog_yes_filter_btn, 60, False)
                self.tools.click_til_element_avail(self.filter_element.get_del_yes_btn())
                sleep(2)
        except:
            return -1, "Not able to clear my filters"

        return 1

    def _get_column_values_from_device_page(self, filter='default'):

        """ verify if the polices are assigned to all devices
            :param  grid : a list of column values on the device page
            :return list of column values
        """
        self.utils.print_info("Start --> Get the values from page ")
        list1, list2, elements = [], [], []
        sleep(10)
        if filter in ["default"]:
            return self._get_elements_text(self.filter_element.get_device_serial_list()), \
                   self._get_elements_text(self.filter_element.get_device_policy_list())


        elif filter in ['management state']:
            return self._get_elements_text(self.filter_element.get_device_serial_list()), \
                   self._get_elements_text((self.filter_element.get_all_device_hosts()))
        elif filter in ['product type']:
            return self._get_elements_text(self.filter_element.get_device_prod_type_model_list())
        elif filter in ['firmware version']:
            return self._get_elements_text(self.filter_element.get_device_soft_version_list())
        elif filter in ['all connection states']:
            return self.filter_element.get_connection_state_list()

        elif filter in ['device type', 'device function']:
            if filter == 'device type':
                elements = self.filter_element.get_all_device_hosts()
            elif filter == 'device function':
                elements = self.filter_element.get_device_prod_type_model_list()

            if elements == None or not elements:
                return False, False

            for element in elements:
                if filter == 'device type':
                    if element.text[:3] == "SIM":
                        list1.append(element)
                    else:
                        list2.append(element)
                elif filter == 'device function':
                    if element.text[:2] == "SR":
                        list2.append(element.text)
                    elif element.text[:1] == "A":
                        list1.append(element.text)

        elif filter in ['client device function', 'client connection', 'client os type', 'client ssid',
                        'application connection']:
            if filter == 'client device function':
                elements = self.client_element.get_filter_client_device_list()
            elif filter == 'client connection':
                elements = self.client_element.get_filter_client_connection_list()
            elif filter == 'client os type':
                return self._get_elements_text(self.client_element.get_filter_client_os_type_list())
            elif filter == 'client ssid':
                return self._get_elements_text(self.client_element.get_filter_client_ssid_list())
            elif filter == 'application connection':
                return self.client_element.get_application_connect_table_list()

            if not elements:
                return False, False

            for element in elements:
                if filter == 'client device function':
                    if element.text[:5] == 'AH-Sw':
                        list1.append(element.text)
                    else:
                        list2.append(element.text)
                elif filter == 'client connection':
                    if "WIRELESS" in element.text == 'WIRELESS':
                        list1.append(element.text)
                    else:
                        list2.append(element.text)
        return list1, list2

    def _get_elements_text(self, elements):
        """ get_elements_text
            :param: list of elements
            :return list of texts
        """
        ls1 = []
        if elements:
            sleep(5)
            for element in elements:
                ls1.append(element.text)
                self.utils.print_info("Get the text " + element.text)
            return ls1

        return False

    def _action_change_managed_state(self, ap, state="managed"):
        """ change a managed state of ap
            :param: ap: ap's serial number
            :param: state is either managed or unmanaged
            :return True
        """
        self.utils.print_info(" Start --> the action managed state " + str(ap))
        self.device.select_ap(ap)
        self.utils.print_info(" Click on the action button  ")
        self.auto_actions.click(self.device_actions.get_device_actions_button())
        self.auto_actions.click(self.device_actions.get_device_actions_change_management_status())
        self.tools.wait_til_elements_avail(self.filter_element.action_managed_device_link, 30, False)
        self.utils.print_info(" Change the managed state to  " + state)
        if state == "managed":
            self.auto_actions.click(self.filter_element.get_action_managed_device())
        else:
            self.auto_actions.click(self.filter_element.get_action_unmanaged_device())
        self.auto_actions.click(self.filter_element.get_del_yes_btn())
        self.auto_actions.click(self.filter_element.get_action_close_dialog())
        self.utils.print_info(" Exit --> the Action managed state  ")

        return 1

    def _get_devices_with_network_policy(self, sns, policies):
        sn_list, policies_list = [], []
        self.utils.print_info(" Start --> Get devices with network policies ")
        for i in range(0, len(policies)):
            if policies[i] != '' and policies[i] not in policies_list:
                sn_list.append(sns[i])
                policies_list.append(policies[i])
        self.utils.print_info(" Exit --> Get devices with network policies ")
        return sn_list, policies_list

    def clear_column_filter(self):
        """ this function resets the column filter
        """

        self.utils.print_info("Start --> Reset to the default filters ")
        try:
            self.auto_actions.click(self.filter_element.get_col_filter_pkr_link())
            self.auto_actions.click(self.filter_element.get_clear_filter_button())
        except:
            return -1, "Not able to clear"

        return 1

    def _parse_string(self, models):

        self.utils.print_info("Start --> Parse string " + str(models))
        real_modeL_lst = []
        for model in models:
            rc = int(model.find("("))
            if rc != -1:
                real_modeL_lst.append(model[0:int(model.index('(')) - 1])
            else:
                real_modeL_lst.append(model)

        return real_modeL_lst

    def expand_default_filters(self):
        self.utils.print_info(" Start --> Expand the default filters ")
        self.auto_actions.scroll_down()
        self._expand_and_collapse_filters(self.filter_element.get_device_state_filter_link(),
                                          self.filter_element.get_state_connected_filter_chkbox(),
                                          filter_type='device state')
        self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
        self._expand_and_collapse_filters(self.filter_element.get_device_function_filter_link(),
                                          self.filter_element.get_device_function_access_point_chkbox(),
                                          filter_type='device function')
        self._expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(),
                                          self.filter_element.get_user_profile_default_guest_filter_chkbox(),
                                          filter_type='device user profile')
        self._expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(),
                                          self.filter_element.get_real_device_filter_chkbox(),
                                          filter_type='device type')

        self.utils.print_info(" Exit --> Expand the default filters ")

        return 1

    def verify_save_filter(self, filter="saved filter", expected_count=1):
        self.utils.print_info("Verify the saved filter " + str(expected_count))

        if filter == "saved filter":
            count = self.filter_element.get_save_filter_list()
            if int(expected_count) == 0:
                if not count: return str(1), None
                else:  return -1, "Save filter does not match"
            else:
                if len(count) == int(expected_count):  return str(1), None
                else:  return -1, "Save filter does not match"
        else:
            element = self.filter_element.get_save_filter_scroll_bar()
            if int(expected_count) == 0:
                if element.is_displayed(): return -1, "Scroll bar appears"
                else: return str(1), None
            else:
                if not element.is_displayed(): return -1, "Scroll bar does not appear"
                else: return str(1), None

    def verify_applied_filter_list(self, expected_count=0, is_more_btn=False, negative=False):
        self.utils.print_info("Verify the applied filter list ")

        if not self.filter_element.get_device_type_filter_link().is_displayed():
            self.utils.print_info("Expand the filter toggle ")
            self.auto_actions.click(self.filter_element.get_filter_toggle_link())

        if is_more_btn:
           try:
                self.utils.print_info("Click the more link ")
                self.auto_actions.click(self.filter_element.get_applied_filter_more_link())
           except:
                return -1, "Not able to Click on the More button"

        sleep(5)
        count = self.filter_element.get_applied_filter_list()

        if not expected_count:
           if count: return -1, "Applied filter list does not matches"
        else:
           if len(count) != expected_count: return -1, "Applied filter list does not match"

        return str(1), None

    def verify_applied_name_filter(self, *filters, is_more_btn=False, negative=False):
        self.utils.print_info("verify name applied filter " + str(negative))
        sleep(5)

        if not self.filter_element.get_device_type_filter_link().is_displayed():
            self.utils.print_info("Expand the filter toggle ")
            self.auto_actions.click(self.filter_element.get_filter_toggle_link())

        if is_more_btn:
            self.utils.print_info("Click on the more link ")
            self.auto_actions.click(self.filter_element.get_applied_filter_more_link())
        elements = self.filter_element.get_applied_filter_list()

        filter_list = []
        if elements:
            for element in elements:
                filter_list.append(element.text)
        self.utils.print_info("applied filter list " + str(filter_list))

        if not negative:
            if elements is None or not elements: return -1, "Applied filter list is empty"
            for filter in filters:
                if filter not in filter_list:  return -1, "Filter list does not match"
        else:
            if elements is None or not elements: return str(1), None
            for filter in filters:
                if filter in filter_list:  return -1, "Filter list does not match"

        return 1, None

    def Enable_all_filter_list(self, filter):
        self.utils.print_info("Enable_all_filter_list " + str(filter))
        if filter == "device type":
            self._expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(), self.filter_element.get_all_device_types_filter_chkbox())
            self._select_filter_by(self.filter_element.all_device_types_filter_chkbox, filter_name='All Product Type')
        else:
            pass

        return

    def expand_all_filters(self):
        """ Expand all filter chekboxe

        """
        self.utils.print_info(" Start --> Expand all filters ")
        self.auto_actions.scroll_down()
        self._expand_and_collapse_filters(self.filter_element.get_device_state_filter_link(), self.filter_element.get_state_connected_filter_chkbox(), filter_type='device state')
        self._select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
        self._select_filter_by(self.filter_element.device_state_disconnected_filter_chkbox, filter_name='disconnected')

        self._expand_and_collapse_filters(self.filter_element.get_device_function_filter_link(), self.filter_element.get_device_function_access_point_chkbox(), filter_type='device function')
        self._select_filter_by(self.filter_element.device_function_access_point_filter_chkbox, filter_name='access point')
        self._select_filter_by(self.filter_element.device_function_switch_filter_chkbox, filter_name='switch')

        self._expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), self.filter_element.get_user_profile_default_guest_filter_chkbox(), filter_type='device user profile')
        self._select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guest profile')
        self._select_filter_by(self.filter_element.device_default_profile_filter_chkbox, filter_name='default profile')

        self._expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(), self.filter_element.get_real_device_filter_chkbox(), filter_type='device type')
        self._select_filter_by(self.filter_element.real_device_filter_chkbox, filter_name='real device')
        self._select_filter_by(self.filter_element.simulated_device_filter_chkbox, filter_name='simulated device')

        self.utils.print_info(" Exit --> Expand all filters ")

        return 1

    def _check_available_devices(self, filter='default', real_device=False, ap_type=False):

        """ verify if the polices are assigned to all devices
                :param  filter :     filter type
                :param  real_device: boolean
                :param  ap_type:     boolean

                :return list of column values
        """

        self.utils.print_info(" Start --> Check available onboard devices ")
        self.clear_all_filters()
        self.clear_column_filter()
        self.expand_default_filters()

        if real_device: self._select_filter_by(self.filter_element.real_device_filter_chkbox)
        if ap_type: self._select_filter_by(self.filter_element.device_function_access_point_filter_chkbox,
                                           filter_name='access point')

        if filter == 'device type':
            self._select_filter_by(self.filter_element.real_device_filter_chkbox,
                                   self.filter_element.simulated_device_filter_chkbox,
                                   filter_name='real and simulated device')

        if filter in ['firmware version']:
            list1 = list(dict.fromkeys(self._get_column_values_from_device_page(filter)))
            if not list1 and len(list1) == 0:
                return -1, " The available hardwares don't meet the requirement "
            return list1

        sn_list, policy_list = self._get_column_values_from_device_page(filter)
        if not sn_list or not policy_list or len(sn_list) == 0 or len(policy_list) == 0:
            return -1, " The available hardwares don't meet the requirement "

        if filter not in ['device type', 'device function']:
            sn_list, policy_list = self._get_devices_with_network_policy(sn_list, policy_list)

        if not sn_list or not policy_list or len(sn_list) == 0 or len(policy_list) <= 0:
            return -1, " The available hardwares don't meet the requirement "

        self.utils.print_info(" Exit --> Check available onboard devices ")

        return sn_list, policy_list

    def user_profile_filter_error(self, user_profile=None):
        """
        - Checks for error after selecting user profile which is not assigned to any device, ie, it should not throw error "can not get the required device list"
        :param user_profile: name of the user profile
        :return: 1 if successful
        """
        self.navigator.navigate_to_devices()
        self.utils.print_info("Clicking on filter")
        sleep(5)
        self.utils.print_info(self.filter_element.get_filter_toggle_link())
        self.auto_actions.click(self.filter_element.get_filter_toggle_link())
        sleep(10)
        self.utils.print_info("getting user profile grid")
        eles = self.filter_element.get_user_profile_grid()
        for ele in eles:
            self.utils.print_info("value: ", ele.text)
            if user_profile == ele.text:
                # element = self.filter_element.get_user_check_box(ele)
                # self.utils.print_info("the element is : ", ele)
                sleep(5)
                val = ele.find_element_by_tag_name("input")
                sleep(10)
                if val:
                    # self.utils.print_info("checked val is ", val)
                    self.auto_actions.click(val)
                else:
                    self.utils.print_info("element not visible ")

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for value in tool_tp_text:
            if "can not get the required device list" in value.lower():
                self.utils.print_info(value)
                return -1
        return 1
