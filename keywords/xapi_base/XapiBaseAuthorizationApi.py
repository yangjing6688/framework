
#    =========================================
#    WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py
#    DO NOT EDIT THIS FILE
#    =========================================



from tools.xapi.XapiHelper import XapiHelper


class XapiBaseAuthorizationApi(XapiHelper):

    def __init__(self):
        super().__init__()

    def xapi_base_check_permissions(self, **kwargs):

        """
            Check permissions  # noqa: E501
            
            Get required permissions for given HTTP request.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.check_permissions(xiq_check_permission_request, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseAuthorizationApi.py
            
                check permissions    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
            
                xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
                xapiBaseAuthorizationApi.check_permissions(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param XiqCheckPermissionRequest xiq_check_permission_request: (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqCheckPermissionResponse
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
            api_instance = self.extremecloudiq.AuthorizationApi(api_client)
            try:
                api_response = api_instance.check_permissions(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
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

    def xapi_base_generate_api_token(self, **kwargs):

        """
            Generate new API token  # noqa: E501
            
            Generate a new API token with given permissions and expiration time.  The available permission list can be found via 'GET /auth/permissions' endpoint.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.generate_api_token(xiq_generate_api_token_request, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseAuthorizationApi.py
            
                generate api token    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
            
                xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
                xapiBaseAuthorizationApi.generate_api_token(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param XiqGenerateApiTokenRequest xiq_generate_api_token_request: Generate API token request body (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqGenerateApiTokenResponse
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
            api_instance = self.extremecloudiq.AuthorizationApi(api_client)
            try:
                api_response = api_instance.generate_api_token(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
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

    def xapi_base_get_current_api_token_info(self, **kwargs):

        """
            Get current API token details  # noqa: E501
            
            Introspect current API token and get detail information.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_current_api_token_info(async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseAuthorizationApi.py
            
                get current api token info    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
            
                xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
                xapiBaseAuthorizationApi.get_current_api_token_info(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqApiTokenInfo
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
            api_instance = self.extremecloudiq.AuthorizationApi(api_client)
            try:
                api_response = api_instance.get_current_api_token_info(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
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

    def xapi_base_list_permissions(self, **kwargs):

        """
            Get permissions for current login user  # noqa: E501
            
            Get permissions for current login user, which are allowed for generating new API tokens.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.list_permissions(async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseAuthorizationApi.py
            
                list permissions    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
            
                xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
                xapiBaseAuthorizationApi.list_permissions(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: str
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
            api_instance = self.extremecloudiq.AuthorizationApi(api_client)
            try:
                api_response = api_instance.list_permissions(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
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

    def xapi_base_validate_api_token(self, **kwargs):

        """
            Validate API token  # noqa: E501
            
            Validate JWT format API token  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.validate_api_token(body, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseAuthorizationApi.py
            
                validate api token    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
            
                xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
                xapiBaseAuthorizationApi.validate_api_token(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param str body: (required)
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
            api_instance = self.extremecloudiq.AuthorizationApi(api_client)
            try:
                api_response = api_instance.validate_api_token(**kwargs)
                # If the _async is True, we will use the Long Running Operation methods
                if kwargs.get('_async', False):
                    # Get the ID
                    operation_id = self.getLongRunningOperationId(api_response)
                    # Query the ID until completed
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
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

