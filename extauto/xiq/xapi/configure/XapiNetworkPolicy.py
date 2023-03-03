from keywords.xapi_base.XapiBaseNetworkPolicyApi import XapiBaseNetworkPolicyApi
from tools.xapi.XapiHelper import XapiHelper

class XapiNetworkPolicy(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseNetworkPolicyApi = XapiBaseNetworkPolicyApi()


    #########################################################################
    # Keyword functions
    #########################################################################

    # We will revist this once create SSID is supported on XAPI
    def xapi_create_network_policy(self, policy, wireless_profile, cli_type='AH-AP', **kwargs):
        pass

        # There is no type tyee passed in, so this method uses the NETWORK_ACCESS_AND_SWITCHING_AND_BR option for all.
        # Typs include the following:
        # 'SWITCHING_AND_BRANCH_ROUTING'
        # 'WIRELESS_ACCESS'
        # 'BRANCH_ROUTING'
        # 'NETWORK_ACCESS_AND_SWITCHING_AND_BR'
        # 'NETWORK_ACCESS_AND_SWITCHING'
        # 'SWITCHING'
        # 'NETWORK_ACCESS_AND_BRANCH_ROUTING'

        # xiq_create_network_policy_request = { "name": policy,
        #                                       "description": '',
        #                                       "type": "NETWORK_ACCESS_AND_SWITCHING_AND_BR"}
        #
        # repsonse = self.xapiBaseNetworkPolicyApi.xapi_base_create_network_policy(xiq_create_network_policy_request=xiq_create_network_policy_request)
        # if repsonse == -1:
        #     kwargs['fail_msg'] = 'Failed to create the network policy'
        #     self.common_validation.failed(**kwargs)
        #     return -1
        # else:
        #     policy_id = repsonse.id
        #
        #     # Add the SSIDs
        #     # This will be a new call to create the SSID
        #
        #     # Add the new SSID to the policy
        #     # self.xapiBaseNetworkPolicyApi.xapi_base_add_ssids_to_network_policy()
        #
        #     kwargs['pass_msg'] = 'Created the network policy'
        #     self.common_validation.passed(**kwargs)
        #     return 1

    def xapi_delete_network_polices(self, *policies, exclude_list=[], **kwargs):
        """
            This method will take a list of policy names and delete them.

        :param policies: The list of policy names to delete
        :param policies: The list of policy names to exclude from the delete
        :param kwargs:
        :return: 1 if the the network policies were deleted or if there is nothing to delete. Will return -1 if there was a failure
        """

        # get the policy based on the name
        length_policy = len(policies)
        if length_policy == 0:
            self.utils.print_warning('No policies were passed into this function to delete')
            kwargs['pass_msg'] = f'Deleted the network policy -> {policies}'
            self.common_validation.passed(**kwargs)
            return 1
        else:
            successfuly_deleted = True
            # make sure we have data
            if len(policies) != 0:
                for policy in policies[0]:
                    # Make sure we shoudn't exclude this one
                    if policy not in exclude_list:
                        policy_data = self.xapiBaseNetworkPolicyApi.xapi_base_list_network_polices(policy_names=[policy])
                        if len(policy_data) != 0:
                            repsonse = self.xapiBaseNetworkPolicyApi.xapi_base_delete_network_policy(id=policy_data.data[0].id)
                            if repsonse and repsonse == -1:
                                successfuly_deleted = False
                                self.utils.print_error(f'Failed to delete the policy {policy}')
        if successfuly_deleted != -1:
            kwargs['pass_msg'] = f'Deleted the network policy -> {policies}'
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f'Failed to deleted the network policy -> {policies}'
            self.common_validation.failed(**kwargs)
            return -1


