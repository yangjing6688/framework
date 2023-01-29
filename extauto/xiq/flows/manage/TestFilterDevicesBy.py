from  extauto.xiq.flows.manage.FilterManageDevices import *

class TestFilterDevicesBy():
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
        self.FilterManageDevices = FilterManageDevices()
        self.screen = Screen()
    def check_filter_device_by_network_policy_is_correct(self):
        """ Verification of the filtering of the devices by network policy
                  prequist: Require at least two onboard devices with with two different wireless networks
                  usage of test case:
                  Test1: Filter Device By network policy
                  filter device by policy
        """
        sn_list, policy_list = self.FilterManageDevices.check_available_devices()
        if sn_list == -1: return -1, policy_list
        element = self.filter_element.get_policy_filter(str(policy_list[0]))
        if not element:
            self.FilterManageDevices.expand_and_collapse_filters(self.filter_element.get_network_policy_filter_link())

        self.utils.print_info(" ----- Filter the policy  " + str(policy_list[0]) + " ----- ")
        status, error = self.filter_policy(str(policy_list[0]))
        if status == -1:
            self.utils.print_info(error)
            return -1
        status, error = self.filter_policy(str(policy_list[1]))
        if status == -1:
            self.utils.print_info(error)
            return -1
        self.FilterManageDevices.clear_all_filters()
        return str(1)

    def filter_policy(self,policy):
        """  Check the filter network policy result:device list and return the result
        """
        self.FilterManageDevices.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy')
        self.apply_filter(self.filter_element.get_applied_filter_btn())
        actual_sn_list, actual_policy_list = self.FilterManageDevices.get_column_values_from_device_page()
        self.utils.print_info(
            " **** The result after the filter *** " + str(actual_sn_list) + " " + str(actual_policy_list))
        if not actual_sn_list or not actual_policy_list or len(actual_sn_list) != 1 or len(actual_sn_list) != 1:
            return -1, "The device list does not match with the filter " + policy

        if policy != actual_policy_list[0]:
            return -1, "The device list does not match with the filter " + policy
        #self.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy', reset=False)
        self.FilterManageDevices.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy', reset=True)
        self.apply_filter(self.filter_element.get_applied_filter_btn())

        return str(1), None

    def apply_filter(self,locator):
        """  Click the ""APPLY FILTERS button to make the filter effective""
        """
        self.utils.print_info("----- Apply the filter-----")
        #self.auto_actions.click_reference(locator)
        element = self.web.get_element(locator)
        if not element: assert True == False, "Not able to find the button 'APPLY FILTERS'" + str(
            locator)
        self.utils.print_info(" Click the 'APPLY FILTERS' button")
        self.auto_actions.click(element)