
from extauto.xiq.xapi.XapiBase import XapiBase


class XapiBaseClientApi(XapiBase):

    def __init__(self):
        super().__init__()

    def xapi_base_get_client(self, **kwargs):

        """
        Get client info  # noqa: E501
        
        Get client detailed information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseClientApi.py
        
                get client    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseClientApi import XapiBaseClientApi
        
                xapiBaseClientApi = XapiBaseClientApi()
                xapiBaseClientApi.get_client(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The client ID (required)
        :param list[XiqClientView] views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] fields: The client fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClient
                 If the method is called asynchronously,
                 returns the request thread.
        """


        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.ClientApi(api_client)
            try:
                api_response = api_instance.get_client(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    # Make sure this isn't a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_get_client_summary(self, **kwargs):

        """
        Get client summary metrics  # noqa: E501
        
        Get number of connected wireless clients and number of detected wired clients.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_summary(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseClientApi.py
        
                get client summary    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseClientApi import XapiBaseClientApi
        
                xapiBaseClientApi = XapiBaseClientApi()
                xapiBaseClientApi.get_client_summary(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param list[int] location_ids: The location IDs
        :param list[int] device_ids: The device IDs
        :param list[int] vlans: The associate VLAN IDs
        :param list[str] user_profile_names: The user profile names
        :param list[str] ssids: The SSIDs
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClientSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """


        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.ClientApi(api_client)
            try:
                api_response = api_instance.get_client_summary(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    # Make sure this isn't a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_get_client_usage(self, **kwargs):

        """
        Get usage per client  # noqa: E501
        
        Get the client usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_usage(client_ids, start_time, end_time, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseClientApi.py
        
                get client usage    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseClientApi import XapiBaseClientApi
        
                xapiBaseClientApi = XapiBaseClientApi()
                xapiBaseClientApi.get_client_usage(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param list[int] client_ids: The client IDs (required)
        :param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970 (required)
        :param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970 (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqClientUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """


        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.ClientApi(api_client)
            try:
                api_response = api_instance.get_client_usage(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    # Make sure this isn't a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_list_active_clients(self, **kwargs):

        """
        List active clients  # noqa: E501
        
        List active clients with filters and pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_active_clients(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseClientApi.py
        
                list active clients    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseClientApi import XapiBaseClientApi
        
                xapiBaseClientApi = XapiBaseClientApi()
                xapiBaseClientApi.list_active_clients(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param list[int] location_ids: The location IDs
        :param list[int] device_ids: The device IDs
        :param list[int] vlans: The associate vlan IDs
        :param list[str] user_profile_names: The user profile names
        :param list[str] ssids: The SSIDs
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param list[XiqClientView] views: The views to return client fields (Check fields for each view at XiqClientView schema)
        :param list[XiqClientField] fields: The client fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedXiqClient
                 If the method is called asynchronously,
                 returns the request thread.
        """


        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.ClientApi(api_client)
            try:
                api_response = api_instance.list_active_clients(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = "returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = "getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    # Make sure this isn't a async call because the thread will be returned and the
                    # api_response is not None
                    if not kwargs.get('async_req', False) and api_response:
                        # Non async call, check the http return
                        self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

