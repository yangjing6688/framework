from tools.xapi.XapiBase import XapiBase

class XapiGlobalSettings(XapiBase):

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

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.AccountApi(api_client)
            api_response = None
            try:
                # Get VIQ Info
                api_response = api_instance.get_viq_info()
            except self.ApiException as e:
                self.utils.print_error("Exception when calling AccountApi->get_viq_info: %s\n" % e)
                raise e
        return api_response