from keywords.xapi_base.XapiBaseNetworkPolicyApi import XapiBaseNetworkPolicyApi
from keywords.xapi_base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
from keywords.xapi_base.XapiBaseConfigurationDeploymentApi import XapiBaseConfigurationDeploymentApi
from extauto.xiq.xapi.manage.XapiDevices import XapiDevices
import time

from tools.xapi.XapiHelper import XapiHelper

class XapiNetworkPolicy(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseNetworkPolicyApi = XapiBaseNetworkPolicyApi()
        self.xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
        self.xapiBaseConfigurationDeploymentApi = XapiBaseConfigurationDeploymentApi()
        self.xapiDevices = XapiDevices()


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
                        policy_data = self.xapiBaseNetworkPolicyApi.xapi_base_list_network_polices(policy_names=[policy], limit=100)
                        if len(policy_data.data) != 0:
                            repsonse = self.xapiBaseNetworkPolicyApi.xapi_base_delete_network_policy(id=policy_data.data[0].id)
                            if repsonse == -1:
                                successfuly_deleted = False
                                self.utils.print_error(f'Failed to delete the policy {policy}')
        if successfuly_deleted:
            kwargs['pass_msg'] = f'Deleted the network policy -> {policies}'
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = f'Failed to deleted the network policy -> {policies}'
            self.common_validation.failed(**kwargs)
            return -1


    def xapi_delete_ssids(self, *ssids, **kwargs):
        """
            The XAPI will be used to delete the SSID names (list) that was passed in

        :param ssids: The list of ssids names to delete
        :param kwargs:
        :return: 1 if the the network ssids were deleted or if there is nothing to delete. Will return -1 if there was a failure
        """
        pass # Need XAPI SSID support to complete the code below

        # length_ssid = len(ssids)
        # if length_ssid == 0:
        #     self.utils.print_warning('No SSIDs were passed into this function to delete')
        #     kwargs['pass_msg'] = f'Deleted the ssid -> {ssids}'
        #     self.common_validation.passed(**kwargs)
        #     return 1
        # else:
        #     successfuly_deleted = True
        #     for look_for_ssid_name in ssids:
        #         ssid_list = self.xapiBaseConfigurationPolicyApi.xapi_base_list_ssids()
        #         for ssid in ssid_list.data:
        #             if ssid.name == look_for_ssid_name:
        #
        #                 Delete the ssid (not implemented yet)
        #                 repsonse = self.xapiBaseNetworkPolicyApi.xapi_base_delete_ssids_from_network_policy(id=policy.id,
        #                                                                                                     request_body=[
        #                                                                                                         ssid.id])
        #                 if repsonse == -1:
        #                     successfuly_deleted = False
        #                     self.utils.print_error(f'Failed to delete the SSID {ssid.name}')
        #                 break
        #
        #     if successfuly_deleted:
        #         kwargs['pass_msg'] = f'Deleted the SSID -> {ssids}'
        #         self.common_validation.passed(**kwargs)
        #         return 1
        #     else:
        #         kwargs['fail_msg'] = f'Failed to deleted the ssid -> {ssids}'
        #         self.common_validation.failed(**kwargs)
        #         return -1

    def xapi_get_policy(self, policy_name, **kwargs):
        """
           This helper function will get the policy given the policy name

           :param: policy_name - The policy name
           :return: The device JSON or -1 if an error occured
        """
        # Get the configuration from the Global varibles
        configuration = self.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        try:
            api_response = None
            api_response = self.xapiBaseNetworkPolicyApi.xapi_base_list_network_polices(policy_names=[policy_name])
            return api_response

        except Exception as e:
            kwargs['fail_msg'] = f"Exception when calling DeviceApi->list_devices: {e}"
            self.common_validation.fault(**kwargs)
            return -1

    def xapi_deploy_network_policy_with_delta_update(self, policy_name, device_serial, update_type):
        """
            This will deploy the nextwork policy to the devices that were selected (delta)

        :param policy_name: The policy name
        :param device_serial: The devices that were selected
        :param update_type: The update type [complete or delta]
        :return: 1 for success or -1 for failure
        """
        return self.xapi_deploy_network_policy_with_complete_update(self, policy_name, device_serial, update_type)

    def xapi_deploy_network_policy_with_complete_update(self, policy_name, device_serial, update_type, next_reboot=False, **kwargs):
        """
            This will deploy the nextwork policy to the devices that were selected

        :param policy_name: The policy name
        :param device_serial: The devices that were selected
        :param update_type: The update type [complete or delta]
        :param next_reboot: Do the update on the next reboot
        :return: 1 for success or -1 for failure
        """
        update_type_value = True # Complete
        if update_type == 'delta':
            update_type_value = False

        # Get the device ID
        device = self.xapiDevices.xapi_get_device(device_serial=device_serial)
        if len(device['data']) == 0:
            kwargs['fail_msg'] = f'Failed to get the device ID from the serial number: {device_serial}'
            self.common_validation.failed(**kwargs)
            return -1

        device_id = device['data'][0]['id']
        deployment = {
                      "devices": {
                        "ids": [
                            device_id
                        ]
                      },
                      "policy": {
                        "enable_complete_configuration_update": update_type_value,
                        "firmware_upgrade_policy": {
                          "enable_enforce_upgrade": True,
                          "enable_distributed_upgrade": True
                        },
                        "firmware_activate_option": {
                          "enable_activate_at_next_reboot": next_reboot,
                          "activation_delay_seconds": 0,
                          "activation_time": 0
                        }
                      }
                    }
        try:
            # Do the deployment
            deployment_reponse_preload = self.xapiBaseConfigurationDeploymentApi.xapi_base_deploy_config(xiq_deployment_request=deployment, _preload_content=False)
            # Get the status
            finished = False
            count = 0
            max_count = 600 # 10 minutes
            while not finished:
                deployment_status_reponse = self.xapiBaseConfigurationDeploymentApi.xapi_base_get_deploy_status(device_ids=[device_id], _preload_content=False)
                deployment_data = self.convert_preload_content_data_to_object(deployment_status_reponse.data)
                data = deployment_data[str(device_id)]
                finished = data.finished
                if not finished:
                    if count % 10 == 0: # only print this message every 10 times
                        self.utils.print_info(f"Device serial: {device_serial}, Status: {data.current_step_message}, Completed: {finished}")
                    time.sleep(1)
                    if count >= max_count:
                        kwargs['fail_msg'] = f'Failed to completed the deployment -> Device serial: {device_serial}, Status: {data.current_step_message}, Completed: {finished}" '
                        self.common_validation.failed(**kwargs)
                else:
                    self.utils.print_info(f"Device serial: {device_serial}, Deployment Sucessful: {data.is_finished_successful}, Completed: {finished}")
                    if not data.is_finished_successful:
                        kwargs['fail_msg'] = f'Failed to completed the deployment with status: {data.is_finished_successful}"'
                        self.common_validation.failed(**kwargs)
                        return -1

                count = count +1
        except Exception as e:
            kwargs['fail_msg'] = f'Failed to completed the deployment with exception {e}'
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = 'The deployment is completed'
        self.common_validation.passed(**kwargs)
        return 1

