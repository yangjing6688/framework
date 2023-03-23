
#    =========================================
#    WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py
#    DO NOT EDIT THIS FILE
#    =========================================



from tools.xapi.XapiHelper import XapiHelper


class XapiBaseCopilotAnomaliesApi(XapiHelper):

    def __init__(self):
        super().__init__()

    def xapi_base_get_devices_by_location(self, **kwargs):

        """
            get_devices_by_location  # noqa: E501
            
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_devices_by_location(async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseCopilotAnomaliesApi.py
            
                get devices by location    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseCopilotAnomaliesApi import XapiBaseCopilotAnomaliesApi
            
                xapiBaseCopilotAnomaliesApi = XapiBaseCopilotAnomaliesApi()
                xapiBaseCopilotAnomaliesApi.get_devices_by_location(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param XiqAnomalyType anomaly_type: Anomaly type
            :param int location_id: The location id
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqAnomalyDevicesByLocationResponse
                     If the method is called asynchronously,
                     returns the request thread.

                    -1 if there is a error (fault)
        """


        # Get the configuration from the Global variables
        configuration = self.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.CopilotAnomaliesApi(api_client)
            try:
                api_response = api_instance.get_devices_by_location(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    # Make sure this is not a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.common_validation.fault(**kwargs)
                return -1

    def xapi_base_get_poe_flapping_stats(self, **kwargs):

        """
            get_poe_flapping_stats  # noqa: E501
            
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_poe_flapping_stats(anomaly_id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseCopilotAnomaliesApi.py
            
                get poe flapping stats    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseCopilotAnomaliesApi import XapiBaseCopilotAnomaliesApi
            
                xapiBaseCopilotAnomaliesApi = XapiBaseCopilotAnomaliesApi()
                xapiBaseCopilotAnomaliesApi.get_poe_flapping_stats(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param str anomaly_id: The anomaly id (required)
            :param int location_id: The location id
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqPoeFlappingStatsResponse
                     If the method is called asynchronously,
                     returns the request thread.

                    -1 if there is a error (fault)
        """


        # Get the configuration from the Global variables
        configuration = self.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.CopilotAnomaliesApi(api_client)
            try:
                api_response = api_instance.get_poe_flapping_stats(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    # Make sure this is not a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.common_validation.fault(**kwargs)
                return -1

    def xapi_base_list_anomaly_locations(self, **kwargs):

        """
            list_anomaly_locations  # noqa: E501
            
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.list_anomaly_locations(async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseCopilotAnomaliesApi.py
            
                list anomaly locations    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseCopilotAnomaliesApi import XapiBaseCopilotAnomaliesApi
            
                xapiBaseCopilotAnomaliesApi = XapiBaseCopilotAnomaliesApi()
                xapiBaseCopilotAnomaliesApi.list_anomaly_locations(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param XiqAnomalyType anomaly_type: Anomaly type
            :param int page: Page number, min = 1
            :param int limit: Number of Records, min = 1, max = 100
            :param XiqAnomalySortField sort_field: sort by field
            :param XiqSortOrder sort_order: The sorting order
            :param bool exclude_muted: exclude muted
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqCopilotPagedXiqAnomalyLocationEntity
                     If the method is called asynchronously,
                     returns the request thread.

                    -1 if there is a error (fault)
        """


        # Get the configuration from the Global variables
        configuration = self.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.CopilotAnomaliesApi(api_client)
            try:
                api_response = api_instance.list_anomaly_locations(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    # Make sure this is not a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.common_validation.fault(**kwargs)
                return -1
