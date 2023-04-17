from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
from tools.xapi.XapiHelper import XapiHelper
import json


class XapiVlan(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapi_base_config_api = XapiBaseConfigurationBasicApi()

    def xapi_create_vlan(self, payload, **kwargs):
        """
            - Get the VIQ information

            :param configuration: The configuration that was returned from the login.
            :return: api_response  This will be None if the command failed or will contain the JSON from the API call
        """
        data = json.loads(json.dumps(payload))
        # Get the configuration from the Global varibles
        configuration = self.get_xapi_configuration()

        api_response = None
        # Check that the access_token is in
        if configuration.access_token == None:
            raise "Error: access_token is None in the configuration"

        try:
            # Get VIQ Info (_preload_content=False)
            api_http_response = self.xapi_base_config_api.xapi_base_create_vlan_profile(xiq_create_vlan_profile_request=data,_preload_content=False)
            api_response = json.loads(api_http_response.data)

        except self.ApiException as e:
            self.utils.print_error("Exception when calling AccountApi->get_viq_info: %s\n" % e)
            raise e
        #api_response_dict = vars(api_response)
        return api_response