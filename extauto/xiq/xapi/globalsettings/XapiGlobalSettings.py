from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi
from keywords.xapi_base.XapiBaseLogApi import XapiBaseLogApi
from tools.xapi.XapiHelper import XapiHelper
import time

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


    def xapi_get_authentication_logs_details(self, search_string, search_filter=None, **kwargs):
        """
            - Filter the logs based on the Filter arguments Allowed Filters are: Client or user name
            - Gets all authentication details from the row
            - Flow : User account image-->Global Settings--> Authentication Logs
            - Keyword Usage
            - ``Get Authentication Logs Details   ${SEARCH_STRING}    ${SEARCH_FILTER}``

            :param search_filter:  filter string
            :param search_string:  row search string - columns in the json
            :return: authentication details dict
        """

        # Get the configuration from the Global varibles
        configuration = self.get_xapi_configuration()
        api_response = None
        # Check that the access_token is in
        if configuration.access_token == None:
            raise "Error: access_token is None in the configuration"

        search_filtered_data = []
        try:
            # assume last 15 mintutes for start time (logs)
            CONSTANT_SECONDS = 900  # time  in seconds (900 seconds = 15 min)
            current_time = int(time.time())
            time_before_15_min = current_time - CONSTANT_SECONDS
            api_raw_response = self.xapiBaseLogApi.xapi_base_list_auth_logs(_preload_content=False, start_time=time_before_15_min, limit=100)
            api_reponse = self.convert_preload_content_data_to_object(api_raw_response)
            # Search the data (userName or Mac)
            if search_filter:
                for record in api_reponse.data:
                    if record.username == search_filter or record.called_station_id == search_filter:
                        search_filtered_data.append(record)

            else: # The full data set (no search data was passed in)
                search_filtered_data = api_reponse.data

            # Filter the data
            filtered_data = []
            for record in search_filtered_data:
                # Search all keys for the search_string
                values_found = [value for value, record_value in record.items() if record_value == search_string]
                if len(values_found) > 0:
                    filtered_data.append(record)

            # Let's normalize the data
            normalized_data = []
            normalized_template = {
                'userName': '',
                'ssid': '',
                'authType': '',
                'callingStationId': '',
                'authdate' : ''
            }
            for record in filtered_data:
                new_record = normalized_template.copy()
                new_record['userName'] = record.username
                new_record['ssid'] = record.ssid
                new_record['authType'] = record.auth_type
                new_record['callingStationId'] = record.called_station_id
                new_record['authdate'] = record.auth_date
                normalized_data.append(new_record)

            return normalized_data

        except self.ApiException as e:
            self.utils.print_error("Exception when calling AccountApi->get_viq_info: %s\n" % e)
            raise e
        return api_response