
#    =========================================
#    WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py
#    DO NOT EDIT THIS FILE
#    =========================================



from tools.xapi.XapiHelper import XapiHelper


class XapiBaseOperationApi(XapiHelper):

    def __init__(self):
        super().__init__()

    def xapi_base_cancel_operation(self, **kwargs):

        """
            Cancel Long-Running Operation (LRO)  # noqa: E501
            
            When the cancelable is true in operation metadata the clients are allowed to send a cancel request to ask the backend to cancel the operation. The server makes its best effort to cancel the operation, but success is not guaranteed.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.cancel_operation(operation_id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseOperationApi.py
            
                cancel operation    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseOperationApi import XapiBaseOperationApi
            
                xapiBaseOperationApi = XapiBaseOperationApi()
                xapiBaseOperationApi.cancel_operation(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param str operation_id: The operation ID (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: None
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
            api_instance = self.extremecloudiq.OperationApi(api_client)
            try:
                api_response = api_instance.cancel_operation(**kwargs)
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

    def xapi_base_delete_operation(self, **kwargs):

        """
            Delete Long-Running Operation (LRO)  # noqa: E501
            
            The Long-Running Operation (LRO) can be deleted when the operation is done or in PENDING status.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.delete_operation(operation_id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseOperationApi.py
            
                delete operation    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseOperationApi import XapiBaseOperationApi
            
                xapiBaseOperationApi = XapiBaseOperationApi()
                xapiBaseOperationApi.delete_operation(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param str operation_id: The operation ID (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: None
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
            api_instance = self.extremecloudiq.OperationApi(api_client)
            try:
                api_response = api_instance.delete_operation(**kwargs)
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

    def xapi_base_get_operation(self, **kwargs):

        """
            Get Long-Running Operation (LRO) status and result  # noqa: E501
            
            Get the Long-Running Operation (LRO) status and result. The response will include either result or error if the operation is done.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_operation(operation_id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseOperationApi.py
            
                get operation    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseOperationApi import XapiBaseOperationApi
            
                xapiBaseOperationApi = XapiBaseOperationApi()
                xapiBaseOperationApi.get_operation(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param str operation_id: The operation ID (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqOperationObject
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
            api_instance = self.extremecloudiq.OperationApi(api_client)
            try:
                api_response = api_instance.get_operation(**kwargs)
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

