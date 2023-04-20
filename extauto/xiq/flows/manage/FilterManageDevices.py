from time import sleep

from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.elements.FilterManageDeviceWebElements import FilterManageDeviceWebElements
from extauto.xiq.elements.FilterManageClientsWebElements import FilterManageClientWebElements
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.manage.Tools import Tools
from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy
from extauto.xiq.flows.configure.ExpressNetworkPolicies import ExpressNetworkPolicies
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip


class FilterManageDevices():
    def __init__(self):
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

    def filter_device_by_network_policy(self):

        """ Verification of the filtering of the devices by the network policy
            prequist: Require at least two onboard APs with each policy
            Usage of test case:
            Test1: Filter Device By Policy
            filter device by policy
        """
        sn_list, policy_list = self.check_available_devices()
        self.expand_and_collapse_filters(self.filter_element.get_network_policy_filter_link())
        if sn_list == -1: return -1, policy_list

        self.utils.print_info(" ----- Filter the policy  " + str(policy_list[0]) + " ----- ")
        status, error = self.filter_policy(str(policy_list[0]))
        if status == -1:
            return -1, error
        self.select_filter_by(self.filter_element.get_policy_filter(policy_list[0]), filter_name='policy' + str(policy_list[0]))

        saved_filter_name = self.save_filter()
        self.utils.print_info(" Saved the filter name " + str(saved_filter_name))
        self.tools.wait_til_elements_avail(self.filter_element.network_policy_filter_link, 60, False)

        self.utils.print_info(" Apply the saved filter ")
        self.select_filter_by(self.filter_element.get_saved_filter_chkbox(saved_filter_name), filter_name='filter name:' + saved_filter_name, reset=True)
        self.select_filter_by(self.filter_element.get_policy_filter(str(policy_list[0])), filter_name='policy' + str(policy_list[0]), reset=True)
        self.select_filter_by(self.filter_element.get_saved_filter_chkbox(saved_filter_name), filter_name='filter name : ' + saved_filter_name)
        status, error = self.filter_policy(str(policy_list[0]))
        if status == -1:
            return -1, error

        return str(1), None

    def filter_policy(self, policy):
        self.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy')
        actual_sn_list, actual_policy_list = self.get_column_values_from_device_page()
        self.utils.print_info(" **** The result after the filter *** " + str(actual_sn_list) + " "  + str(actual_policy_list))
        if not actual_sn_list or not actual_policy_list or len(actual_sn_list) == 0 or len(actual_sn_list) == 0:
            return -1, "The device list is empty with the filter " + policy

        if policy != actual_policy_list[0]:
            return -1, "The device list does not match with the filter " + policy
        self.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy', reset=True)

        return str(1), None

    def filter_by_device_type(self, filter='default'):

        """ Verification of the filtering of the devices by the device type
            prequist: Require at least one real device and one simulated device
            Usage of test case:
            Test1: Filter Device By Device Type
            filter by device type  real device
            filter by device type  simulated device
        """
        self.utils.print_info(" -----  Filter the " + filter + " ---- ")
        total_sim_devices, total_real_devices = self.check_available_devices('device type')
        self.clear_all_filters()
        self.expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(), filter_type='device type')

        if filter in ["real device"]:
            self.select_filter_by(self.filter_element.real_device_filter_chkbox, filter_name='real device')
            sim_lst, real_lst = self.get_column_values_from_device_page("device type")
            self.utils.print_info(" **** The result after the filter *** " + 'sim device: ' + str(len(sim_lst)) + " real device: "  + str(len(real_lst)))
            if not real_lst and not sim_lst  : return -1, "The device list is empty after the filter"
            if len(sim_lst) != 0 and len(real_lst) != len(total_real_devices): return -1, " The result does not match with the real device filter"
            self.select_filter_by(self.filter_element.real_device_filter_chkbox, filter_name='real device', reset=True)

        if filter in ["simulated device"]:
            self.select_filter_by(self.filter_element.simulated_device_filter_chkbox, filter_name='simulated device')
            sim_lst, real_lst = self.get_column_values_from_device_page("device type")
            self.utils.print_info(" **** The result after the filter *** " + 'sim device: ' + str(len(sim_lst)) + " real device: "  + str(len(real_lst)))
            if not real_lst and not sim_lst: return -1, "The device list is empty after the filter "
            if len(sim_lst) != len(total_sim_devices) and len(real_lst) != 0:
                return -1, " The result does not match with the simulated device filter"
            self.select_filter_by(self.filter_element.simulated_device_filter_chkbox, filter_name='simulated device', reset=True)

        return str(1), None

    def filter_device_by_connection_state(self, ap_sn):

        """ Verification of the devices by connection state
            prequist: Require one device in connected state and one device in disconnected state
        """

        self.clear_all_filters()
        sn_list, policy_list = self.get_column_values_from_device_page()
        self.expand_and_collapse_filters(self.filter_element.get_device_state_filter_link(), filter_type='device state')
        if not sn_list or len(sn_list) == 0: return -1, "The device list is empty"
        status = self.device.get_device_status(device_serial=ap_sn)

        if status == 'green':
            self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
            sn_list, policy_list =  self.get_column_values_from_device_page()
            if ap_sn not in sn_list: return -1, " The device list does not match with the connected filter"
            self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected', reset=True)
            self.select_filter_by(self.filter_element.device_state_disconnected_filter_chkbox, filter_name='disconnected')
            sn_list, policy_list = self.get_column_values_from_device_page()
            if ap_sn in sn_list: return -1, " The device list does not match with the disconnected filter: " + str(ap_sn) + ' in ' + str(sn_list)
        else:
            self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
            sn_list, policy_list = self.get_column_values_from_device_page()
            if ap_sn in sn_list: return -1, " The device list does not match with the connected filter"
            self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected', reset=True)
            self.select_filter_by(self.filter_element.device_state_disconnected_filter_chkbox, filter_name='disconnected')
            sn_list, policy_list = self.get_column_values_from_device_page()
            if ap_sn not in sn_list: return -1, " The device list does not match with the disconnected filter: " + + str(ap_sn) + ' not in ' + str(sn_list)

        return str(1), None

    def filter_device_by_production_type(self):

        """ Verification of the filtering of the device models
            prequist: Require at least two or more APs with the different hardware models
            Usage of test case:

            Test1: Filter By Device Production Type
            filter device production type
        """
        self.clear_all_filters()
        self.expand_default_filters()
        self.expand_and_collapse_filters(self.filter_element.get_device_type_filter_link())
        models = self.get_column_values_from_device_page('product type')
        self.utils.print_info(" Check available hardware models ")
        if not models or len(models) <= 1:  return -1, "Require at least two different hardware models"

        models = list(dict.fromkeys(models))
        self.expand_and_collapse_filters(self.filter_element.get_device_prod_type_filter_link())
        self.utils.print_info(" List of models :" + str(models))
        cnt = 1
        for model in models:
            if cnt > 2: break
            self.utils.print_info(" ----- Filter For The Hardware Model " + model + " ----- ")
            status, error = self.filter_hardware_model(model)
            if status == -1:   return -1, error
            cnt = cnt + 1

        return str(1), None

    def filter_hardware_model(self, model):
        self.select_filter_by(self.filter_element.get_device_prod_type_model_filter_checkbox(model), filter_name='model ' + str(model))
        actual_models = list(dict.fromkeys(self.get_column_values_from_device_page('product type')))
        self.utils.print_info(" Validate the filter " + str(model))
        self.utils.print_info(" actual model list " + str(actual_models))
        if not actual_models: return -1, "The device list is empty with the filter model " + str(model)
        self.utils.print_info(" actual model " + str(actual_models[0]) + ' expected model ' + str(model))
        if actual_models[0] != model: return -1, "The model does not match with the filter model " + str(model) + " and actual model is " + str(actual_models)
        self.select_filter_by(self.filter_element.get_device_prod_type_model_filter_checkbox(model), filter_name='model ' + str(model), reset=True)

        return str(1), None

    def filter_device_by_function(self, filter):

        """ Verification of the filtering of the devices by function
            prequist: Require at least one AP and one Fasthpath / Hive OS switch
            Ussage of test case:
            Test1: Filter By Device Function
            filter device by function  ap model
            filter device by function  sw model
        """
        self.utils.print_info(" ----- Filter the " + filter + " ----- ")
        ap_lst, sw_lst = self.check_available_devices()
        if ap_lst == -1: return -1, sw_lst
        if filter in ['ap model']:
            self.select_filter_by(self.filter_element.device_function_access_point_filter_chkbox, filter_name='access point')
            aps, sws = self.get_column_values_from_device_page("device function")
            self.utils.print_info(" Validate the filter ")
            if not aps and len(aps) ==0: return -1, " The device list is empty after the filter"
            aps = list(dict.fromkeys(aps))
            if aps != ap_lst and  len(sws) != 0: return -1, "The device list does not match with the filter"
            self.select_filter_by(self.filter_element.device_function_access_point_filter_chkbox, filter_name='access point', reset=True)

        if filter in ['switch']:
            self.select_filter_by(self.filter_element.device_function_switch_filter_chkbox, filter_name='switch')
            aps, sws = self.get_column_values_from_device_page("device function")
            self.utils.print_info(" Validate the filter ")
            if not sws and len(sws) == 0 : return -1, " The device list is empty after the filter"
            sws = list(dict.fromkeys(sws))
            if sws != sw_lst and len(aps) != 0: return -1, "The device list does not match with the filter"
            self.select_filter_by(self.filter_element.device_function_switch_filter_chkbox, filter_name='switch',reset=True)

        return str(1), None

    def filter_device_both_unmanaged_and_managed_state(self):

        """ Verification of the devices by the device mangement state
            prequist: Require at least one or more onboard devices
            Usage of test case:
            Test1: Filter By Device Management State
            filter device by management state
        """
        sn_list, host_list = self.check_available_devices(real_device=True)
        if sn_list == -1: return -1, host_list

        self.utils.print_info(" ----- Filter The Unmanaged Device -----")
        self.expand_and_collapse_filters(self.filter_element.get_device_data_management_state_filter_link(), filter_type='management state')
        self.action_change_managed_state(sn_list[0], "unmanaged")
        self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected', reset=True)
        self.select_filter_by(self.filter_element.device_data_management_unmanaged_chkbox, filter_name='unmanaged')
        self.tools.wait_til_ap_change_status(sn_list[0], host_list[0], 180, "red")
        actual_sn_list, actual_host_list = self.get_column_values_from_device_page("management state")

        self.utils.print_info(" Validate the filter ")
        if not actual_sn_list and len(actual_sn_list) == 0 : return -1, "The device list is empty with the unmanaged filter"
        if actual_sn_list[0] != sn_list[0]: return -1, "Device does not match and the actual sn is " + actual_sn_list[0] + ' expected sn is ' + sn_list[0]

        self.utils.print_info(" ----- Filter The Managed Device -----")
        self.action_change_managed_state(sn_list[0], "managed")
        self.select_filter_by(self.filter_element.device_data_management_unmanaged_chkbox, filter_name='unmanaged',reset=True)
        self.select_filter_by(self.filter_element.device_data_management_managed_chkbox, filter_name='managed')
        self.tools.wait_til_ap_change_status(sn_list[0], host_list[0], 300, "green")

        self.utils.print_info(" Validate the filter ")
        actual_sn_list, actual_host_list = self.get_column_values_from_device_page("management state")
        if not actual_sn_list and len(actual_sn_list) == 0 : return -1, "The device list is empty with the managed filter"
        if actual_sn_list[0] != sn_list[0]: return -1, "Device does not match and the actual sn is " + actual_sn_list[0] + ' expected sn is ' + sn_list[0]

        return str(1), None

    def filter_all_devices_by_software_version(self):

        """ verification of the devices by software version
            prequist: Require at least two or more onboard different hardware devices
            usage of test case:
            Test1: Filter By Device Software Version
            filter device by software version
        """
        soft_lst = self.check_available_devices('firmware version')
        if soft_lst == -1: return -1, "error"
        self.utils.print_info(" Bwfoew Available hardware models " + str(soft_lst))
        real_modeL_lst =  self.parse_string(soft_lst)
        self.utils.print_info(" Available hardware models" + str(real_modeL_lst))
        self.expand_and_collapse_filters(self.filter_element.get_device_soft_version_link())

        for model in real_modeL_lst:
            self.utils.print_info(" ----- filter the versions ----- " + model)
            model_element = self.filter_element.get_device_soft_version_chkbox(model)
            self.select_filter_by(model_element, filter_name='firmware version')
            soft_lst = self.get_column_values_from_device_page("firmware version")
            self.utils.print_info(" Validate the filter " + str(soft_lst))
            if not soft_lst or len(soft_lst) == 0 : return -1, "The device list is empty by the filter " + model
            actual_model_lst = list(dict.fromkeys(soft_lst))
            actual_model_lst = self.parse_string(actual_model_lst)
            for actual_model in actual_model_lst:
                if actual_model != model:
                    return -1, "The device does not match with the version " + str(actual_model) + ' ' + str(model)
            self.select_filter_by(model_element, filter_name='firmware version', reset=True)

        return str(1), None

    def filter_device_with_audit_match_and_mismatch(self):

        """ Verification of the filtering of the devices by audit status
            prequist: Require at least two or more onboard devices with a different policy
            usage of test case
            Test1: Filter By Device audit status
            filter device by audit status
        """
        sn_list, policy_list = self.check_available_devices(real_device=True)
        if sn_list == -1: return -1, policy_list
        sn_list, policy_list = self.get_devices_with_network_policy(sn_list, policy_list)
        self.utils.print_info(" The available sn list : " + str(sn_list) + ' ' + str(policy_list))

        self.utils.print_info(" ------  Filter the audit match device " + str(policy_list[0]) + " ------")
        policy = ''.join([str(elem) for elem in policy_list[0]])
        self.net_policy.get_all_ssids_in_policy(policy, new_ssid=True, special_char=True)
        self.net_policy.deploy_network_policy(policy, sn_list[0], "delta")
        self.clear_all_filters()
        self.expand_and_collapse_filters(self.filter_element.get_audit_state_filter_link())
        self.select_filter_by(self.filter_element.device_audit_config_match_filter_chkbox, filter_name='match device')
        sns, policies = self.get_column_values_from_device_page()
        self.utils.print_info(" The sn list after the match filter : " + str(sn_list) + ' ' + str(policy_list))
        if not sns and len(sns) == 0: return -1, "Device list is empty after the filter"
        if sn_list[0] != sns[0]:
            return -1, "The device list does not match with the audit match filter " + sn_list[0] + ' ' + sns[0]
        self.select_filter_by(self.filter_element.device_audit_config_match_filter_chkbox, filter_name='match device', reset=True)

        self.utils.print_info(" ------ Filter the audit mismatch device " + str(policy_list[0]) + " ------")
        self.select_filter_by(self.filter_element.device_audit_config_mismatch_filter_chkbox, filter_name='mistmatch')
        sns, policies = self.get_column_values_from_device_page()
        self.utils.print_info(" The sn list after the mismatch filter : " + str(sn_list) + ' ' + str(policy_list))
        if not sns: return -1, "Device list is empty after the filter"
        if sn_list[0] == sns[0]:
            return -1, "The device list does not match with the audit mismatch filter " + sn_list[0] + ' ' + sns[0]

        return str(1), None

    def filter_device_by_ssid(self):

        """ Verification of the filtering of the devices by ssid
            prequist: Require at least two onboard devices with with two different wireless networks
            usage of test case:
            Test1: Filter Device By ssid
            filter device by ssid

            Jira: APC-39526 - The SSID list in the SSID filter does not update accordingly
        """
        sn_list, policy_list = self.check_available_devices(real_device=True, ap_type=True)
        if sn_list == -1: return -1, policy_list
        policy_ssid, ssid_name  = self.net_policy.get_all_ssids_in_policy(policy_list[0], new_ssid=False, special_char=True)
        self.utils.print_info(" ssid list  " + str(policy_ssid))
        self.clear_all_filters()
        self.expand_and_collapse_filters(self.filter_element.get_device_ssid_filter_link())

        cnt = 0
        for policy in policy_list:
            for ssid in policy_ssid[policy]:
                cnt = cnt + 1
                if cnt > 3:
                    break
                self.utils.print_info(" ------ Filter the ssid ------ " + str(ssid) + ' in the policy ' + str(policy))
                ssid_element = self.filter_element.get_device_ssid_filter_checkbox(str(ssid))
                self.select_filter_by(ssid_element, filter_name='ssid')
                self.utils.print_info(" Validate the filter ")
                sn_list, policy_list = self.get_column_values_from_device_page()
                if not policy_list or len(policy_list) == 0:
                    return -1, "The device list is empty with the ssid filter " + str(ssid)
                policy_list = list(dict.fromkeys(policy_list))
                if policy_list[0] != policy:
                    return -1, " Policy does not match " + str(policy_list[0] + ' ' + str(policy))
                self.select_filter_by(ssid_element, filter_name='ssid', reset=True)

        return str(1), None

    def filter_device_by_user_profiles(self, filter='default'):

        """ Verification of the filtering of the devices by user profiles
            prequist: Require at least one onboard devices with a network policy
            usage of test case:
            Test1: Filter By Device user profile
            filter device by user profiles  guest
            filter device by user profiles  profile
        """
        self.utils.print_info(" ----- Filter the " + filter + " -----")
        sn_list, policy_list = self.check_available_devices(real_device=True, ap_type=True)
        if sn_list == -1: return -1, policy_list

        if filter in ['guest profile']:
            #self.net_policy.delete_all_ssid_in_policy(policy_list[0])
            self.utils.print_info(" Create a new guest wireless network" )
            self.net_policy.get_all_ssids_in_policy(policy_list[0], new_ssid=True, special_char=False)
            self.clear_all_filters()
            self.expand_default_filters()
            self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected', reset=True)
            self.select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guest profile')
            actual_sns, actual_policies = self.get_column_values_from_device_page()

            self.utils.print_info(" Validate the filter ")
            if not actual_sns and not actual_policies: return -1, " The device list is empty with filter the guess profile"
            if sn_list[0] not in actual_sns: return -1, "The device " + str(sn_list[0] + " does not match in the device list " + str(actual_sns))
            self.select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guest profile', reset=True)

        if  filter in ['default profile']:
            policy_name, ssid_name = self.utils.get_random_string(), self.utils.get_random_string()
            cwp_name = self.utils.get_random_string()
            self.netExpress.create_open_auth_express_network_policy(policy_name, ssid_name, cwp_name)
            self.net_policy.deploy_network_policy(policy_name, sn_list[0], "delta")
            self.clear_all_filters()
            self.expand_default_filters()
            self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected', reset=True)
            self.select_filter_by(self.filter_element.device_default_profile_filter_chkbox, filter_name='default profile')
            actual_sns, actual_policies = self.get_column_values_from_device_page()

            self.utils.print_info(" Validate the filter ")
            if not actual_sns: return -1, " The device list is empty with the default profile filter"
            if sn_list[0] not in actual_sns: return -1, "The device " + str(sn_list[0] + " does not match in the device list " + str(actual_sns))
            self.select_filter_by(self.filter_element.device_default_profile_filter_chkbox, filter_name='default profile', reset=True)

        return str(1), None

    def filter_client_by_device_function(self, filter):

        """ Verification of the filtering of the clients based on the device function
            prequist: AP and switch need to be onboarded and need one client to switch and one client connect to AP
            Usage of test case:
            Test1: Filter Client By Device Function
            client.filter client by device function  client ap
            client.filter client by device function  client switch
            Jira: APC - 3741
        """
        self.utils.print_info(" ----- Filter the " + filter + " -----")
        if filter in ['client ap', 'client switch', 'client wireless connection type', 'client wired connection type']:
            self.clear_all_filters('client filter')
        elif filter in ['client 360 ap', 'client 360 switch', 'client 360 wireless connection type', 'client 360 wired connection type']:
            self.clear_all_filters('ml_insight filter')

        ap_conn, sw_conn = self.get_column_values_from_device_page("client connection")
        self.utils.print_info(" Check available client connections before start a filter ")
        if not ap_conn or not sw_conn or len(sw_conn) == 0 or len(ap_conn) == 0:
            return -1, "Require at least one onboard switch and one onboard AP with a wireless connection "

        if filter in ['client ap', 'client wireless connection type', 'client 360 ap', 'client 360 wireless connection type']:
            if filter in ['client ap', 'client 360 ap']:
                self.expand_and_collapse_filters(self.client_element.get_filter_client_device_function_link(), 'client')
                self.select_filter_by(self.client_element.filter_client_device_function_ap_chkbox, filter_name = filter)
            elif filter in ['client wireless connection type', 'client 360 wireless connection type']:
                self.expand_and_collapse_filters(self.client_element.get_filter_client_connection_link(), 'client')
                self.select_filter_by(self.client_element.filter_client_device_wireless_connection_chkbox,filter_name = filter)
            aps, sws = self.get_column_values_from_device_page("client connection")
            self.utils.print_info(" Validate the filter ")
            if not aps or len(aps) == 0 :
                return -1, "The client list is empty with the " + filter +  " filter"
            if len(aps) != len(ap_conn) and len(sws) !=0 :
                return -1, "The wireless connections do not match with the " + filter + " filter "

        if filter in ['client switch', 'client wired connection type', 'client 360 switch', 'client 360 wired connection type']:
            if filter in ['client switch', 'client 360 switch']:
                self.expand_and_collapse_filters(self.client_element.get_filter_client_device_function_link(), 'client')
                self.select_filter_by(self.client_element.filter_client_device_function_sw_chkbox, filter_name = filter)
            elif filter in ['client wired connection type', 'client 360 wired connection type']:
                self.expand_and_collapse_filters(self.client_element.get_filter_client_connection_link(), 'client')
                self.select_filter_by(self.client_element.filter_client_device_wired_connection_chkbox, filter_name='wired')
            aps, sws = self.get_column_values_from_device_page("client connection")
            if not sws or len(sws) == 0:
                return -1, "The client list is empty with the " + filter + " filter"
            if len(sws) != len(sw_conn) and len(aps) != 0:
                return -1, "The wired connections do not match with the " + filter + " filter "
            self.select_filter_by(self.client_element.filter_client_device_function_sw_chkbox, filter_name = filter, reset=True)

        self.expand_and_collapse_filters(self.client_element.get_filter_client_device_function_link(), 'client', True)

        return str(1), None

    def filter_client_by_os_type(self, filter):

        """ Verification of the clients based on the os type
            prequist: One or two clients should be connected via Wifi either Windows, Mac OS
            Usage of test case:
            Test1: Filter Client By OS Type
            filter client by os type
        """

        self.utils.print_info(" ----- Filter the " + filter  + "-----" )
        if filter in ['client os type']:
            self.clear_all_filters('client filter')
        elif filter in ['client 360 os type']:
            self.clear_all_filters('ml_insight filter')

        os_types_list = self.get_column_values_from_device_page("client os type")
        os_types_list = [x.lower() for x in os_types_list if x]
        self.utils.print_info("Available client OS types: " + str(os_types_list))
        self.utils.print_info(" Check available client connections ")
        if not os_types_list or len(os_types_list) == 0: return -1, "Require at least one Mac or Window client connects to a wireless"

        self.expand_and_collapse_filters(self.client_element.get_filter_client_os_type_link(), 'client')
        if 'mac' in str(os_types_list).lower():
            self.select_filter_by(self.client_element.filter_client_mac_os_type_chkbox, filter_name='mac os')
            os_types_list = self.get_column_values_from_device_page("client os type")
            self.utils.print_info(" Validate the filter ")
            os_types_list = [x.lower() for x in os_types_list if x]
            if 'mac' not in str(os_types_list).lower():  return -1,  "Mac filter does not match " + str(os_types_list)
            self.select_filter_by(self.client_element.filter_client_mac_os_type_chkbox, filter_name='mac os', reset=True)

        if 'window' in str(os_types_list).lower():
            self.select_filter_by(self.client_element.filter_client_windows_os_type_chkbox, filter_name='windows')
            os_types_list = self.get_column_values_from_device_page("client os type")
            os_types_list = [x.lower() for x in os_types_list if x]
            if 'window' not in str(os_types_list).lower(): return -1, "Windows filter does not match " + str(os_types_list)
            self.select_filter_by(self.client_element.filter_client_windows_os_type_chkbox, filter_name='windows', reset=True)
        self.expand_and_collapse_filters(self.client_element.get_filter_client_os_type_link(), 'client', collapse=True)

        return str(1), None

    def filter_client_by_ssid(self, filter):

        """ Verification of the Clients based on the SSID
            prequist: 1 Ap should be onboarded with wireless network
            Usage of test case:
            Test1: Filter Client By Client SSID
            filter client by ssid
        """
        self.utils.print_info("----- filter the " + filter + " ------ " )
        if filter in ['client ssid']:
            self.clear_all_filters('client filter')
        elif filter in ['client 360 ssid']:
            self.clear_all_filters('ml_insight filter')

        self.expand_and_collapse_filters(self.client_element.get_client_ssid_filter_link(), 'client')
        ssids = self.get_column_values_from_device_page("client ssid")
        ssids = [x for x in ssids if x]
        self.utils.print_info(" Available SSIDs " + str(ssids))
        if not ssids or len(ssids) <= 0:
            return -1, "Require at least one onboared device connecting 1 wirless network"
        ssids = list(dict.fromkeys(ssids))

        for ssid in ssids:
            ssid_element = self.client_element.get_client_ssid_filter_checkbox(str(ssid))
            self.select_filter_by(ssid_element, filter_name='ssid')
            actual_ssids = self.get_column_values_from_device_page("client ssid")
            if not actual_ssids: return -1, "The SSID list is empty with the filter " + str(ssid)
            for actual_ssid in actual_ssids:
                if str(actual_ssid) != str(ssid) : return -1 , "The SSID does not match " + str(actual_ssid) + ' ' + str(ssid)
            self.select_filter_by(ssid_element, filter_name='ssid', reset=True)

        self.expand_and_collapse_filters(self.client_element.get_client_ssid_filter_link(), 'client', collapse=True)

        return str(1), None

    def filter_client_by_user_profiles(self, ssid_name, filter='default'):
        """ Verification of the filtering of the Clients based on the SSID
            prequist: 1 Ap should be onboarded with wireless network
            Usage of test case:
            Test1: Filter Client By User Profiles
            filter client by user profiles  ${ssid_name}   client guess profile
            filter client by user profiles  ${ssid_name}   client default profile
        """

        if filter in ['client guest profile']:
            sleep(60)
            self.utils.print_info(" ------ Filter the " + filter + "-----")
            self.clear_all_filters('client filter')
            self.expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), 'client')
            self.select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guest profile')
            ssid_list = self.get_column_values_from_device_page("client ssid")
            if not ssid_list or len(ssid_list) == 0:
                return -1, " There is no wireless connection with the guess profile filter"
            if ssid_name not in ssid_list:
                return -1, " The client ssid does not match with the guest profile filter " + str(ssid_name) + ' ' + str(ssid_list)
            self.select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guess profile', reset=True)

        # if filter in ['client default profile']:
        #     self.utils.print_info("Create a standard access network for the device " + sns[1])
        #     username = self.utils.get_random_string()
        #     policy_name, ssid_name = self.netExpress.add_express_net_policy()
        #     self.usergroup.create_simple_user_in_usergroup('GA-ppsk-user-device', username, 'aerohive')
        #     self.auto_actions.scroll_up()
        #     self.net_policy.deploy_network_policy_with_delta_update(policy_name, sns[1])
        #     self.utils.print_info("Make a WIFFI connection to the ssid name is " + ssid_name2)
        #     self.cli.mac_wifi_connection(mac_station, mac_login, mac_password, ssid_name2, ssid_pass="aerohive")
        #
        #     self.utils.print_info(" ----- Filter the client for the default profile ------")
        #     self.clear_all_filters('client filter')
        #     self.expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), 'client')
        #     self.select_filter_by(self.filter_element.device_default_profile_filter_chkbox, filter_name='default profile')
        #     ssids = self.get_column_values_from_page("client ssid")
        #     if not ssids: assert True == False, " There is no wireless connection with the standard profile filter"
        #     ssids = list(set(ssids))
        #     assert ssid_name2 == ssids[0], "The ssid " + ssid_name2 + " does not match in the actual ssid list " + str(ssids[0])
        #     self.select_filter_by(self.filter_element.device_default_profile_filter_chkbox, filter_name='default profile', reset=True)
        #     self.select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guest profile')
        #     ssids = self.get_column_values_from_page("client ssid")
        #     if ssids:
        #         assert ssid_name2 != ssids[0], "The standard network should not appear with the guess profile filter"
        #     self.select_filter_by(self.filter_element.device_default_guest_profile_filter_chkbox, filter_name='guess profile', reset=True)

            self.expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), 'client', True)

        return str(1), None

    def set_device_type_filter(self, filter='All', select='true'):
        """
        Sets the device type filter to the specified value
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
            self.auto_actions.click_reference(self.filter_element.get_device_type_filter_link)

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
        """
        Sets the device connection state filter to the specified value
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
            self.auto_actions.click_reference(self.filter_element.get_device_state_filter_link)

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
            self.auto_actions.click_reference(self.filter_element.get_device_data_management_state_filter_link)

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
            self.auto_actions.click_reference(self.filter_element.get_device_function_filter_link)

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
            self.auto_actions.click_reference(self.filter_element.get_device_function_filter_link)

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
            self.auto_actions.click_reference(self.filter_element.get_device_soft_version_link)

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
            self.auto_actions.click_reference(self.filter_element.get_cloud_config_group_filter_link)

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
                self.auto_actions.click_reference(self.filter_element.get_filter_toggle_link)
        elif navigator == 'client filter':
            self.navigator.navigate_to_clients()
            if not self.client_element.get_filter_client_device_function_link().is_displayed():
                self.auto_actions.click_reference(self.filter_element.get_filter_toggle_link)
        elif navigator == 'ml_insight filter':
            self.navigator.navigate_to_client360()
            if not self.client_element.get_filter_client_device_function_link().is_displayed():
                self.auto_actions.click_reference(self.filter_element.get_filter_toggle_link)
        elif navigator == 'application':
            self.navigator.navigate_manage_application()
            self.auto_actions.click_reference(self.filter_element.get_filter_toggle_link)

        all_filters = self.filter_element.get_my_saved_filter_list()
        if all_filters:
            self.utils.print_info("Start clearing my filter ")
            for index in range(1, len(all_filters) + 1):
                self.auto_actions.click_reference(self.filter_element.get_list_del_index_filter)
                self.tools.wait_til_elements_avail(self.filter_element.dialog_yes_filter_btn, 60, False)
                self.tools.click_til_element_avail(self.filter_element.get_del_yes_btn())

        all_applied_filters = self.filter_element.get_applied_filter_list()
        if all_applied_filters:
            self.utils.print_info("start clearing the applied filters ")
            self.auto_actions.click_reference(self.filter_element.get_applied_clear_filter_link)
            sleep(3)
        self.utils.print_info("Exit --> Clear all filters ")

        return 1

    def expand_and_collapse_filters(self, element, filter_type='policy', collapse=False):
        """ expand and collapse the filter links

            :param element : link of filter
            :param filter_type: page contains the filters
            :param collapse: collapse the filter toggle when it is true
        """
        self.utils.print_info(" Start -- > Expand / collapse filters " + filter_type)
        if filter_type == 'device type':
            self.tools.wait_til_elements_avail(self.filter_element.device_type_filter_link, 30, False)
        if filter_type == 'client':
            self.tools.wait_til_elements_avail(self.client_element.filter_client_device_function_link, 30, False)
        if filter_type == 'user_profile':
            self.tools.wait_til_elements_avail(self.filter_element.get_user_profiles_filter_link, 30, False)
        sleep(5)
        self.auto_actions.click(element)
        if collapse:
            self.auto_actions.click_reference(self.filter_element.get_filter_toggle_link)
        self.utils.print_info(" Exit --> Expand / collapse filters " + filter_type)

        return 1

    def select_filter_by(self, *locators, filter_name = 'default', reset=False):
        """ expand and collapse the filter links

            :param locators : list of checkboxs
            :param reset : clear the checkbox when it is true
        """
        self.utils.print_info(" Start select filter ")
        for locator in locators:
            element = self.web.get_element(locator)
            self.utils.print_info(" Locator " + str(locator))
            if not element: assert True == False, "Not able to find a filter selection and the test aborts " + str(locator)
            if not reset:
                if not element.is_selected():
                    self.utils.print_info(" In Click filter ")
                    self.utils.print_info(" Select filter  " + filter_name)
                    self.auto_actions.click(element)
            else:
                if element.is_selected():
                    self.utils.print_info(" Unselect filter   " + filter_name)
                    self.auto_actions.click(element)

        self.utils.print_info(" Exit --> The select / unselect filter")
        return True

    def save_filter(self):

        """ create a filter and save the filter

        :param: None
        :return filter_name (name of filter)
        """

        self.utils.print_info("Start --> Save filter ")
        filter_name = self.utils.get_random_string(8)
        self.auto_actions.click_reference(self.filter_element.get_save_filter_btn)
        self.tools.wait_til_elements_avail(self.filter_element.dialog_input_filter_filename_txt, 30, False)
        self.utils.print_info(" Enter the filter saved name  " + filter_name + ' and click on Save')
        self.auto_actions.send_keys(self.filter_element.get_enter_filter_name_txt(), filter_name)
        self.auto_actions.click_reference(self.filter_element.get_dialog_save_btn)
        self.utils.print_info("Exit --> Save filter ")

        return filter_name

    def get_column_values_from_device_page(self, filter='default'):

        """ verify if the polices are assigned to all devices

            :param  grid : a list of column values on the device page
            :return list of column values
        """
        self.utils.print_info("Start --> Get the values from page ")
        list1, list2, elements = [], [], []
        sleep(20)
        if filter in ["default"]:
            return self.get_elements_text(self.filter_element.get_device_serial_list()),\
                   self.get_elements_text(self.filter_element.get_device_policy_list())
        elif filter in ['management state']:
            return self.get_elements_text(self.filter_element.get_device_serial_list()),\
                   self.get_elements_text((self.filter_element.get_all_device_hosts()))
        elif filter in ['product type']:
            return self.get_elements_text(self.filter_element.get_device_prod_type_model_list())
        elif filter in ['firmware version']:
            return  self.get_elements_text(self.filter_element.get_device_soft_version_list())
        elif filter in ['all connection states'] : return self.filter_element.get_connection_state_list()

        elif filter in ['device type', 'device function']:
            if filter == 'device type':  elements = self.filter_element.get_all_device_hosts()
            elif filter == 'device function' :  elements = self.filter_element.get_device_prod_type_model_list()

            if not elements:
                return False, False

            sleep(5)
            for element in elements:
                if filter == 'device type':
                    if element.text[:3] == "SIM" :  list1.append(element)
                    else:                           list2.append(element)
                elif filter == 'device function':
                    if element.text[:2] == "SR" :   list2.append(element.text)
                    elif element.text[:1] == "A":   list1.append(element.text)

        elif filter in ['client device function', 'client connection', 'client os type', 'client ssid']:
            sleep(5)
            if self.client_element.get_page_size_100_link().is_displayed():
                self.auto_actions.click_reference(self.client_element.get_page_size_100_link)
            if filter == 'client device function': elements = self.client_element.get_filter_client_device_list()
            elif filter == 'client connection' :   elements = self.client_element.get_filter_client_connection_list()
            elif filter == 'client os type'    :   return  self.get_elements_text(self.client_element.get_filter_client_os_type_list())
            elif filter == 'client ssid'       :   return  self.get_elements_text(self.client_element.get_filter_client_ssid_list())

            if not elements:
                return False, False

            for element in elements:
                if filter == 'client device function':
                    if element.text[:5] == 'AH-Sw': list1.append(element.text)
                    else                          : list2.append(element.text)
                elif filter == 'client connection':
                    if element.text[:8] == 'WIRELESS': list1.append(element.text)
                    else                             : list2.append(element.text)

        self.utils.print_info("Exit --> Get the values from page ")
        return list1, list2

    def get_elements_text(self, elements):
        """ get_elements_text

            :param: list of elements
            :return list of texts
        """
        ls1 = []
        if elements:
            sleep(5)
            for element in elements:
                ls1.append (element.text)
                if element.text != '':
                    self.utils.print_info("Start --> Get element text " + element.text)
            return ls1
        self.utils.print_info("Exit --> Get element text " )
        return False

    def action_change_managed_state(self, ap, state="managed"):
        """ change a managed state of ap

            :param: ap: ap's serial number
            :param: state is either managed or unmanaged
            :return True
        """
        self.utils.print_info(" Start --> the action managed state " + str(ap))
        self.device.select_device(device_serial=ap)
        self.utils.print_info(" Click on the action button  ")
        self.auto_actions.click_reference(self.device_actions.get_device_actions_button)
        self.auto_actions.move_to_element(self.device_actions.get_device_actions_change_management_status())
        self.tools.wait_til_elements_avail(self.filter_element.action_managed_device_link, 30, False)
        self.utils.print_info(" Change the managed state to  " + state)
        if state == "managed":
            self.auto_actions.click_reference(self.filter_element.get_action_managed_device)
        else:
            self.auto_actions.click_reference(self.filter_element.get_action_unmanaged_device)
        self.auto_actions.click_reference(self.filter_element.get_del_yes_btn)
        self.auto_actions.click_reference(self.filter_element.get_action_close_dialog)
        self.utils.print_info(" Exit --> the Action managed state  ")

        return 1

    def get_devices_with_network_policy(self, sns, policies ):
        sn_list, policies_list = [], []
        self.utils.print_info(" Start --> Get devices with network policies ")
        for i in range(0, len(policies)) :
            if policies[i] != '' and policies[i] not in policies_list  :
                sn_list.append(sns[i])
                policies_list.append(policies[i])
        self.utils.print_info(" Exit --> Get devices with network policies " )
        return  sn_list, policies_list

    def parse_string(self, models):

        self.utils.print_info("Start --> Parse string " + str(models))
        real_modeL_lst = []
        for model in models:
            real_modeL_lst.append(model[0:int(model.index('(')) - 1])
        self.utils.print_info(" Exit --> Parse string: " + str(real_modeL_lst))
        return real_modeL_lst

    def expand_default_filters(self):
        self.utils.print_info(" Start --> Expand the default filters ")
        element = self.filter_element.device_state_connected_filter_chkbox
        if not element:
            self.expand_and_collapse_filters(self.filter_element.get_device_state_filter_link(), filter_type='device state')
        self.select_filter_by(self.filter_element.device_state_connected_filter_chkbox, filter_name='connected')
        self.expand_and_collapse_filters(self.filter_element.get_device_function_filter_link(), filter_type='device function')
        self.expand_and_collapse_filters(self.filter_element.get_user_profile_filter_link(), filter_type='device user profile')
        self.expand_and_collapse_filters(self.filter_element.get_device_type_filter_link(), filter_type='device type')

        self.utils.print_info(" Exit --> Expand the default filters ")

        return 1

    def check_available_devices(self, filter='default', real_device= False, ap_type = False):
        self.utils.print_info(" Start --> Check available onboard devices ")
        self.clear_all_filters()
        self.expand_default_filters()

        if real_device: self.select_filter_by(self.filter_element.real_device_filter_chkbox)
        if ap_type: self.select_filter_by(self.filter_element.device_function_access_point_filter_chkbox, filter_name='access point')

        if filter == 'device type':
            self.select_filter_by(self.filter_element.real_device_filter_chkbox, self.filter_element.simulated_device_filter_chkbox,
                                  filter_name='real and simulated device')

        elif filter in ['firmware version']:
            list1 = list(dict.fromkeys(self.get_column_values_from_device_page(filter)))
            if not list1 and len(list1) == 0: return -1, " The available hardwares don't meet the requirement "
            return list1

        sn_list, policy_list = self.get_column_values_from_device_page(filter)
        if filter not in ['device type']:
            sn_list, policy_list = self.get_devices_with_network_policy(sn_list, policy_list)

        if not sn_list or not policy_list or len(sn_list) == 0 or len(policy_list) == 0:
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
        self.auto_actions.click_reference(self.filter_element.get_filter_toggle_link)
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

    def set_copilot_license_filter(self, filter='All', select='true', **kwargs):
        """
        Sets the copilot license filter to the specified value
        Usage of test case:
            Set CoPilot License Filter  All  true
            Set CoPilot License Filter  All CoPilot Eligible Devices  true
            Set CoPilot License Filter  CoPilot Active  true
            Set CoPilot License Filter  CoPilot Expired  true
            Set CoPilot License Filter  CoPilot None  true
            Set CoPilot License Filter  All  false
            Set CoPilot License Filter  All CoPilot Eligible Devices  false
            Set CoPilot License Filter  CoPilot Active  false
            Set CoPilot License Filter  CoPilot Expired  false
            Set CoPilot License Filter  CoPilot None  false

        :param filter: name of the filter to set
        :param select: indicates whether the filter check box should be selected (true) or deselected (false)
        :return: 1 if filter was set, else -1
        """
        self.utils.print_info(f" -----  Set CoPilot License By {filter} selected {select} ---- ")

        # Open the Filter panel if it is not already open
        self.open_filter_panel()

        # Expand the CoPilot License filter section if it is not yet expanded
        copilot_license_filter_collapsed = self.filter_element.get_copilot_license_filter_link_collapsed()
        if copilot_license_filter_collapsed and copilot_license_filter_collapsed.is_displayed():
            self.auto_actions.click_reference(self.filter_element.get_copilot_license_filter_link)

        # Get the check box element to toggle
        element = None
        if filter == 'All':
            element = self.filter_element.get_copilot_license_all_filter_chkbox()
        elif filter == 'All CoPilot Eligible Devices':
            element = self.filter_element.get_copilot_license_all_copilot_eligible_filter_chkbox()
        elif filter == 'CoPilot Active':
            element = self.filter_element.get_copilot_license_active_filter_chkbox()
        elif filter == 'CoPilot Expired':
            element = self.filter_element.get_copilot_license_expired_filter_chkbox()
        elif filter == 'CoPilot None':
            element = self.filter_element.get_copilot_license_none_filter_chkbox()

        # Set the desired state of the filter check box
        return self.toggle_filter_check_box(element, select)

    def apply_filters(self, **kwargs):
        """
        Clicks on "Apply Filters" button to apply any selected filters within the Devices panel
        Usage of test case:
            Apply Filters

        :return: 1 if filter was set, else -1
        """

        self.utils.print_info("Clicking on Apply Filters button")
        apply_filters = self.filter_element.get_apply_filters_btn()

        if apply_filters:
            self.auto_actions.click_reference(self.filter_element.get_apply_filters_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to click Apply Filters button")
            ret_val = -1

        return ret_val
