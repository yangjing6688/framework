
#    =========================================
#    WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py
#    DO NOT EDIT THIS FILE
#    =========================================



from tools.xapi.XapiHelper import XapiHelper


class XapiBaseConfigurationBasicApi(XapiHelper):

    def __init__(self):
        super().__init__()

    def xapi_base_create_vlan_profile(self, **kwargs):

        """
            Create VLAN profile  # noqa: E501
            
            Create a new VLAN profile.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.create_vlan_profile(xiq_create_vlan_profile_request, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseConfigurationBasicApi.py
            
                create vlan profile    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
            
                xapiBaseConfigurationBasicApi = XapiBaseConfigurationBasicApi()
                xapiBaseConfigurationBasicApi.create_vlan_profile(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param XiqCreateVlanProfileRequest xiq_create_vlan_profile_request: The payload to create new VLAN profile (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqVlanProfile
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
            api_instance = self.extremecloudiq.ConfigurationBasicApi(api_client)
            try:
                api_response = api_instance.create_vlan_profile(**kwargs)
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

    def xapi_base_delete_vlan_profile(self, **kwargs):

        """
            Delete a VLAN profile  # noqa: E501
            
            Delete a specific VLAN profile by ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.delete_vlan_profile(id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseConfigurationBasicApi.py
            
                delete vlan profile    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
            
                xapiBaseConfigurationBasicApi = XapiBaseConfigurationBasicApi()
                xapiBaseConfigurationBasicApi.delete_vlan_profile(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param int id: The VLAN profile ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationBasicApi(api_client)
            try:
                api_response = api_instance.delete_vlan_profile(**kwargs)
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

    def xapi_base_delete_vlan_profiles(self, **kwargs):

        """
            [LRO] Delete VLAN profiles  # noqa: E501
            
            Delete VLAN profiles.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.delete_vlan_profiles(xiq_vlan_profile_filter, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseConfigurationBasicApi.py
            
                delete vlan profiles    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
            
                xapiBaseConfigurationBasicApi = XapiBaseConfigurationBasicApi()
                xapiBaseConfigurationBasicApi.delete_vlan_profiles(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param XiqVlanProfileFilter xiq_vlan_profile_filter: (required)
            :param bool _async: Whether to enable async mode
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
            api_instance = self.extremecloudiq.ConfigurationBasicApi(api_client)
            try:
                api_response = api_instance.delete_vlan_profiles(**kwargs)
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

    def xapi_base_get_vlan_profile(self, **kwargs):

        """
            Get a VLAN profile  # noqa: E501
            
            Get a specific VLAN profile by ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.get_vlan_profile(id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseConfigurationBasicApi.py
            
                get vlan profile    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
            
                xapiBaseConfigurationBasicApi = XapiBaseConfigurationBasicApi()
                xapiBaseConfigurationBasicApi.get_vlan_profile(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param int id: The VLAN profile ID (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqVlanProfile
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
            api_instance = self.extremecloudiq.ConfigurationBasicApi(api_client)
            try:
                api_response = api_instance.get_vlan_profile(**kwargs)
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

    def xapi_base_list_vlan_profiles(self, **kwargs):

        """
            List VLAN profiles  # noqa: E501
            
            Get a page of VLAN profiles.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.list_vlan_profiles(async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseConfigurationBasicApi.py
            
                list vlan profiles    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
            
                xapiBaseConfigurationBasicApi = XapiBaseConfigurationBasicApi()
                xapiBaseConfigurationBasicApi.list_vlan_profiles(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param int page: Page number, min = 1
            :param int limit: Page Size, min = 1, max = 100
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: PagedXiqVlanProfile
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
            api_instance = self.extremecloudiq.ConfigurationBasicApi(api_client)
            try:
                api_response = api_instance.list_vlan_profiles(**kwargs)
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

    def xapi_base_update_vlan_profile(self, **kwargs):

        """
            Update a VLAN profile  # noqa: E501
            
            Update a specific VLAN profile.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.update_vlan_profile(id, xiq_update_vlan_profile_request, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseConfigurationBasicApi.py
            
                update vlan profile    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseConfigurationBasicApi import XapiBaseConfigurationBasicApi
            
                xapiBaseConfigurationBasicApi = XapiBaseConfigurationBasicApi()
                xapiBaseConfigurationBasicApi.update_vlan_profile(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param int id: The VLAN profile ID. (required)
            :param XiqUpdateVlanProfileRequest xiq_update_vlan_profile_request: The payload to update VLAN profile (required)
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: XiqVlanProfile
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
            api_instance = self.extremecloudiq.ConfigurationBasicApi(api_client)
            try:
                api_response = api_instance.update_vlan_profile(**kwargs)
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

