from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi
from keywords.xapi_base.XapiBaseLogApi import XapiBaseLogApi
from tools.xapi.XapiHelper import XapiHelper

class XapiGlobalSettings(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseAccountApi = XapiBaseAccountApi()
        self.xapiBaseLogApi = XapiBaseLogApi()

    def get_viq_info(self, **kwargs):
        """
            - Get the VIQ information

            :param configuration: The configuration that was returned from the login.
            :return: api_response  This will be None if the command failed or will contain the JSON from the API call
        """

        # Get the configuration from the Global varibles
        configuration = self.get_xapi_configuration()

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


    def xapi_get_authentication_logs_details(self, search_string, search_filter=None):
        """
            - Filter the logs based on the Filter arguments Allowed Filters are: Client or user name
            - Gets all authentication details from the row
            - Flow : User account image-->Global Settings--> Authentication Logs
            - Keyword Usage
            - ``Get Authentication Logs Details   ${SEARCH_STRING}    ${SEARCH_FILTER``

            :param search_filter:  filter string - There is no UI filtering, so this isn't used
            :param search_string:  row search string - client mac or user name (search the username or mgmt_mac_address) columns in the json
            :return: authentication details dict
        """

        # Get the configuration from the Global varibles
        configuration = self.get_xapi_configuration()

        api_response = None
        # Check that the access_token is in
        if configuration.access_token == None:
            raise "Error: access_token is None in the configuration"

        try:
            # Get VIQ Info
            api_raw_response = self.xapiBaseLogApi.xapi_base_list_auth_logs(_preload_content=False)


        except self.ApiException as e:
            self.utils.print_error("Exception when calling AccountApi->get_viq_info: %s\n" % e)
            raise e
        return api_response