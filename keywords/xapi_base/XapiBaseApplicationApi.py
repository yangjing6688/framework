
from tools.xapi.XapiBase import XapiBase


class XapiBaseApplicationApi(XapiBase):

    def __init__(self):
        super().__init__()

    def xapi_base_list_application_top_clients_usage(self, **kwargs):

        """
        List the TopN clients for a application  # noqa: E501
        
        List the TopN clients by usage for a specific application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_application_top_clients_usage(id, n, start_time, end_time, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseApplicationApi.py
        
                list application top clients usage    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseApplicationApi import XapiBaseApplicationApi
        
                xapiBaseApplicationApi = XapiBaseApplicationApi()
                xapiBaseApplicationApi.list_application_top_clients_usage(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The application ID (required)
        :param int n: The TopN number (required)
        :param int start_time: The start time for querying top client usage of application (required)
        :param int end_time: The end time for querying top application usage of application (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqApplicationTopClientsUsage]
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
            api_instance = self.extremecloudiq.ApplicationApi(api_client)
            try:
                api_response = api_instance.list_application_top_clients_usage(**kwargs)
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

    def xapi_base_list_applications(self, **kwargs):

        """
        List the applications  # noqa: E501
        
        List a page of applications by filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_applications(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseApplicationApi.py
        
                list applications    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseApplicationApi import XapiBaseApplicationApi
        
                xapiBaseApplicationApi = XapiBaseApplicationApi()
                xapiBaseApplicationApi.list_applications(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int page: Page number, min = 1
        :param int limit: Page Size, min = 1, max = 100
        :param str name: Application Name
        :param XiqApplicationDetectionProtocol detection_protocol: Application Detection Protocol, only for custom Application
        :param XiqApplicationDetectionType detection_type: Application Detection Type, only for custom Application
        :param bool predefined: Flag to filter predefined or custom Application
        :param XiqApplicationSortField sort_field: The sort field
        :param XiqSortOrder order: The sort order (ascending by default)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedXiqApplication
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
            api_instance = self.extremecloudiq.ApplicationApi(api_client)
            try:
                api_response = api_instance.list_applications(**kwargs)
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

    def xapi_base_list_top_applications_usage(self, **kwargs):

        """
        List the TopN applications  # noqa: E501
        
        List the TopN applications by usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_top_applications_usage(n, start_time, end_time, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseApplicationApi.py
        
                list top applications usage    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseApplicationApi import XapiBaseApplicationApi
        
                xapiBaseApplicationApi = XapiBaseApplicationApi()
                xapiBaseApplicationApi.list_top_applications_usage(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int n: The TopN number (required)
        :param int start_time: The start time for querying top application usage (required)
        :param int end_time: The end time for querying top application usage (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqTopApplicationsUsage]
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
            api_instance = self.extremecloudiq.ApplicationApi(api_client)
            try:
                api_response = api_instance.list_top_applications_usage(**kwargs)
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

