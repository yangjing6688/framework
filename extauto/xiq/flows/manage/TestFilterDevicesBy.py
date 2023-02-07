from  extauto.xiq.flows.manage.FilterManageDevices import FilterManageDevices
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.WebElementHandler import WebElementHandler
from extauto.xiq.elements.FilterManageDeviceWebElements import FilterManageDeviceWebElements

class TestFilterDevicesBy():
    def __init__(self):
        self.utils          = Utils()
        self.auto_actions   = AutoActions()
        self.web            = WebElementHandler()
        self.filter_element = FilterManageDeviceWebElements()
        self.FilterManageDevices = FilterManageDevices()
    def check_filter_device_by_network_policy_is_correct(self):
        """ Verification of the filtering of the devices by network policy
                  pre-conditions: Require at least two onboard devices with with two different wireless network policys
                  usage of test case:
                  ${CHECK_RESULT}=        check filter device by network policy is correct
                  Should Be Equal As Integers    ${CHECK_RESULT}        1
                  Test1: Filter Device By network policy,for example,device1 is assigned policy1,device2 is assigned policy2
                  filter device1 by policy1 and filter device2 by policy2
                  Return valuesAer: "1" means filter successfully,"-1" means filter failed
        """
        sn_list, policy_list = self.FilterManageDevices.check_available_devices()
        if sn_list == -1: return -1, policy_list
        element = self.filter_element.get_policy_filter(str(policy_list[0]))
        if not element:
            self.FilterManageDevices.expand_and_collapse_filters(self.filter_element.get_network_policy_filter_link())

        self.utils.print_info(" ----- Filter the policy  " + str(policy_list[0]) + " ----- ")
        status, error = self.filter_policy(str(policy_list[0]))
        if status == -1:
            kwargs['fail_msg'] = error
            self.common_validation.failed(**kwargs)
            return -1
        status, error = self.filter_policy(str(policy_list[1]))
        if status == -1:
            kwargs['fail_msg'] = error
            self.common_validation.failed(**kwargs)
            return -1
        self.FilterManageDevices.clear_all_filters()
        return str(1)

    def filter_policy(self,policy):
        """  Check the filter network policy result:device list and return the result
             parameter:policy is the name of network-policy
             result:
                   -1 means filter device by the network-policy failed,the error message need to be returned as well.
                   1 means filter device by the network-policy successfully,if it's successful,the error message should be none
             example:
             status, error = self.filter_policy(policyName)
        """
        self.FilterManageDevices.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy')
        self.apply_filter(self.filter_element.get_applied_filter_btn())
        actual_sn_list, actual_policy_list = self.FilterManageDevices.get_column_values_from_device_page()
        self.utils.print_info(
            " **** The result after the filter *** " + str(actual_sn_list) + " " + str(actual_policy_list))
        if not actual_sn_list or not actual_policy_list or len(actual_sn_list) != 1 or len(actual_sn_list) != 1:
            kwargs['fail_msg'] = "The device list does not match with the filter " + policy
            self.common_validation.failed(**kwargs)
            return -1, kwargs['fail_msg']

        if policy != actual_policy_list[0]:
            kwargs['fail_msg'] = "The device list does not match with the filter " + policy
            self.common_validation.failed(**kwargs)
            return -1, kwargs['fail_msg']
        self.FilterManageDevices.select_filter_by(self.filter_element.get_policy_filter(policy), filter_name='policy', reset=True)
        self.apply_filter(self.filter_element.get_applied_filter_btn())

        return 1, None

    def apply_filter(self,locator):
        """  Click the ""APPLY FILTERS button to make the filter effective""
        """
        self.utils.print_info("----- Apply the filter-----")
        element = self.web.get_element(locator)
        if not element:
            kwargs['fail_msg'] = "Not able to find the button 'APPLY FILTERS'" + str(locator)
            self.common_validation.failed(**kwargs)
        self.utils.print_info(" Click the 'APPLY FILTERS' button")
        self.auto_actions.click(element)