from tools.xapi.XapiBase import XapiBase
from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi

class XapiGlobalSettings(XapiBase):

    def __init__(self):
        super().__init__()
        self.xapiBaseAccountApi = XapiBaseAccountApi()

    def get_viq_info(self, **kwargs):
        """
            - Get the VIQ information

            :param configuration: The configuration that was returned from the login.
            :return: api_response  This will be None if the command failed or will contain the JSON from the API call
        """

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()

        api_response = None
        # Check that the access_token is in
        if configuration.access_token == None:
            raise "Error: access_token is None in the configuration"

        try:
            # Get VIQ Info
            api_response = self.xapiBaseAccountApi.xapi_base_get_viq_info()

        except self.ApiException as e:
            self.utils.print_error("Exception when calling AccountApi->get_viq_info: %s\n" % e)
            raise e
        return api_response