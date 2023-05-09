from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi
from keywords.xapi_base.XapiBaseLogApi import XapiBaseLogApi
from tools.xapi.XapiHelper import XapiHelper
import time
import re
from datetime import datetime
from datetime import timedelta
from extauto.common.CommonValidation import CommonValidation


class XapiGlobalSettings(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseAccountApi = XapiBaseAccountApi()
        self.xapiBaseLogApi = XapiBaseLogApi()
        self.common_validation = CommonValidation()

    def xapi_get_viq_id(self, **kwargs):
        """
            - Gets the VIQ ID

            :return: returns the VIQ ID if success. return "" if not success.
        """
        try:
            json_response = self.get_viq_info(**kwargs)
            viq_id = json_response.owner_id
            return str(viq_id)

        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword xapi_get_viq_id Error: {e}"
            self.common_validation.fault(**kwargs)
            return ""
          

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

            :param search_filter:  filter string (if this is a datetime format then it will be used to search for the auth_date or timestamp for the last 5 minutes)
            :param search_string:  row search string - columns in the json
            :return: authentication details dict
        """

        normalized_template = {
            'reply': '',
            'userName': '',
            'ssid': '',
            'authType': '',
            'callingStationId': '',
            'calledStationId': '',
            'mgmtMacAddress': '',
            'authdate': '',
            'timestamp': '',
            'rejectReason': '',
            'nasIdentifier': '',
        }

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
            time_before_15_min = (current_time - CONSTANT_SECONDS) * 1000
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
                # Regular expression to check the date time format
                pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
                search_string_date = bool(len(re.findall(pattern, search_string)) > 0)
                if (search_string_date):
                    self.utils.print_info("Search String is a date time format")

                    # Search the data (auth_date or timestamp)
                    # Here we need to make sure that the date time is checked for plus or minus 5 minutes
                    not_found = True
                    time_minute_difference = -10
                    # This should be the local time zone
                    auth_date_string = datetime.fromtimestamp(record.auth_date / 1000.0).strftime('%Y-%m-%d %H:%M')
                    timestamp_string = datetime.fromtimestamp(record.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M')
                    while not_found:
                        new_date_time = datetime.strptime(search_string, '%Y-%m-%d %H:%M')
                        adjusted_date_time = new_date_time - timedelta(minutes=time_minute_difference)
                        adjusted_date_time_string = adjusted_date_time.strftime('%Y-%m-%d %H:%M')
                        self.utils.print_info(f"(auth_date_string: {auth_date_string} or timestamp_string: {timestamp_string}) == search_string: {search_string}")
                        if auth_date_string == adjusted_date_time_string or timestamp_string == adjusted_date_time_string:
                            filtered_data.append(record)
                            not_found = False
                        else:
                            time_minute_difference += 1
                            if time_minute_difference > 10: # 10 minutes
                                self.utils.print_info(f"Could not find the date time: {search_string} minus {time_minute_difference} minutes")
                                not_found = False
                else: # Check all of the key for the values
                    self.utils.print_info("Search String is not a date time format, search all of the keys")
                    values_found = [value for value, record_value in record.items() if record_value == search_string]
                    if len(values_found) > 0:
                        filtered_data.append(record)

            # Let's normalize the data
            for record in filtered_data:
                # Return the 1st record in the list
                new_record = normalized_template.copy()
                if record.reply == 'Access-Accept':
                    normalized_template['reply'] = 'auth-logs-accept'
                else:
                    normalized_template['reply'] = record.reply
                normalized_template['userName'] = record.username
                normalized_template['ssid'] = record.ssid
                normalized_template['authType'] = record.auth_type
                normalized_template['callingStationId'] = record.calling_station_id
                normalized_template['calledStationId'] = record.called_station_id
                normalized_template['authdate'] = record.auth_date
                normalized_template['timestamp'] = record.timestamp
                normalized_template['mgmtMacAddress'] = record.mgmt_mac_address
                normalized_template['rejectReason'] = record.reject_reason
                normalized_template['nasIdentifier'] = record.nas_identifier
                self.utils.print_info(f"Normalized Data Found: {normalized_template}")
                return normalized_template

            # Empty
            self.utils.print_info("No data found")
            return normalized_template

        except self.ApiException as e:
            self.utils.print_error("Exception when calling AccountApi->get_viq_info: %s\n" % e)
            raise e