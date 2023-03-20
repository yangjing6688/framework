
#	=========================================
#	WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py
#	DO NOT EDIT THIS FILE
#	=========================================



from tools.xapi.XapiHelper import XapiHelper


class XapiBaseConfigurationDeploymentApi(XapiHelper):

    def __init__(self):
        super().__init__()

    def xapi_base_deploy_config(self, **kwargs):

        """
        Push configuration and upgrade firmware  # noqa: E501
        
        Push configuration and upgrade firmware to the target devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deploy_config(xiq_deployment_request, async_req=True)
        >>> result = thread.get()
        
        **Note: The kwargs options are explained in the :param section below.
        These can be placed in the kwargs dict as key / values pairs or 
        passed into the function as key / value pairs as separate arguments.
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationDeploymentApi.py
        
                deploy config    **kwargs
        
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationDeploymentApi import XapiBaseConfigurationDeploymentApi
        
                xapiBaseConfigurationDeploymentApi = XapiBaseConfigurationDeploymentApi()
                xapiBaseConfigurationDeploymentApi.deploy_config(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqDeploymentRequest xiq_deployment_request: The device deploy configuration (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqDeploymentResponse
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
            api_instance = self.extremecloudiq.ConfigurationDeploymentApi(api_client)
            try:
                api_response = api_instance.deploy_config(**kwargs)
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
                    # Make sure this isn't a async call because the thread will be returned and the
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

    def xapi_base_get_deploy_overview(self, **kwargs):

        """
        Get configuration deployment overview  # noqa: E501
        
        Get configuration deployment status overview.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deploy_overview(async_req=True)
        >>> result = thread.get()
        
        **Note: The kwargs options are explained in the :param section below.
        These can be placed in the kwargs dict as key / values pairs or 
        passed into the function as key / value pairs as separate arguments.
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationDeploymentApi.py
        
                get deploy overview    **kwargs
        
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationDeploymentApi import XapiBaseConfigurationDeploymentApi
        
                xapiBaseConfigurationDeploymentApi = XapiBaseConfigurationDeploymentApi()
                xapiBaseConfigurationDeploymentApi.get_deploy_overview(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqDeploymentOverview
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
            api_instance = self.extremecloudiq.ConfigurationDeploymentApi(api_client)
            try:
                api_response = api_instance.get_deploy_overview(**kwargs)
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
                    # Make sure this isn't a async call because the thread will be returned and the
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

    def xapi_base_get_deploy_status(self, **kwargs):

        """
        Get configuration deployment status  # noqa: E501
        
        Get configuration deployment status for the target devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deploy_status(device_ids, async_req=True)
        >>> result = thread.get()
        
        **Note: The kwargs options are explained in the :param section below.
        These can be placed in the kwargs dict as key / values pairs or 
        passed into the function as key / value pairs as separate arguments.
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationDeploymentApi.py
        
                get deploy status    **kwargs
        
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationDeploymentApi import XapiBaseConfigurationDeploymentApi
        
                xapiBaseConfigurationDeploymentApi = XapiBaseConfigurationDeploymentApi()
                xapiBaseConfigurationDeploymentApi.get_deploy_status(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param list[int] device_ids: The target device IDs (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: dict(str, XiqDeploymentStatus)
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
            api_instance = self.extremecloudiq.ConfigurationDeploymentApi(api_client)
            try:
                api_response = api_instance.get_deploy_status(**kwargs)
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
                    # Make sure this isn't a async call because the thread will be returned and the
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

