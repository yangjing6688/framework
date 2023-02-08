from pprint import pprint
from extauto.xiq.xapi.XapiHelper import XapiHelper

try:
    import extremecloudiq
    from extremecloudiq.rest import ApiException
except Exception:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')


class XapiGlobalSettings:

    def __init__(self):
        self.xapiHelper = XapiHelper()

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
        with extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = extremecloudiq.AccountApi(api_client)
            try:
                # Get VIQ Info
                api_response = api_instance.get_viq_info()
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling AccountApi->get_viq_info: %s\n" % e)
                raise e
        return api_response