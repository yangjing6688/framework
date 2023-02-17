
from tools.xapi.XapiBase import XapiBase


class XapiBaseConfigurationAuthenticationApi(XapiBase):

    def __init__(self):
        super().__init__()

    def xapi_base_create_external_radius_server(self, **kwargs):

        """
        Create external RADIUS server configuration  # noqa: E501
        
        Create a new external RADIUS server configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_external_radius_server(xiq_create_external_radius_server_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                create external radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.create_external_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateExternalRadiusServerRequest xiq_create_external_radius_server_request: Use the payload configuration to create a new external RADIUS server (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqExternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.create_external_radius_server(**kwargs)
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

    def xapi_base_create_internal_radius_server(self, **kwargs):

        """
        Create internal RADIUS server configuration  # noqa: E501
        
        Create a new internal RADIUS server configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_internal_radius_server(xiq_create_internal_radius_server_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                create internal radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.create_internal_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateInternalRadiusServerRequest xiq_create_internal_radius_server_request: Use the payload configuration to create a new internal RADIUS server (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqInternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.create_internal_radius_server(**kwargs)
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

    def xapi_base_create_ldap_server(self, **kwargs):

        """
        Create LDAP server  # noqa: E501
        
        Create a new LDAP server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ldap_server(xiq_create_ldap_server_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                create ldap server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.create_ldap_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateLdapServerRequest xiq_create_ldap_server_request: The body of create LDAP server API (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqLdapServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.create_ldap_server(**kwargs)
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

    def xapi_base_create_radius_client_object(self, **kwargs):

        """
        Create RADIUS client object configuration  # noqa: E501
        
        Create a new RADIUS client object configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_radius_client_object(xiq_create_radius_client_object_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                create radius client object    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.create_radius_client_object(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateRadiusClientObjectRequest xiq_create_radius_client_object_request: Use the payload configuration to create a new RADIUS client object (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadiusClientObject
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.create_radius_client_object(**kwargs)
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

    def xapi_base_create_radius_proxy(self, **kwargs):

        """
        Create RADIUS proxy configuration  # noqa: E501
        
        Create a new RADIUS proxy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_radius_proxy(xiq_create_radius_proxy_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                create radius proxy    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.create_radius_proxy(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateRadiusProxyRequest xiq_create_radius_proxy_request: The body of create RADIUS proxy API (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadiusProxy
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.create_radius_proxy(**kwargs)
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

    def xapi_base_delete_external_radius_server(self, **kwargs):

        """
        Delete external RADIUS server configuration  # noqa: E501
        
        Delete an existing external RADIUS server configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_external_radius_server(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                delete external radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.delete_external_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The external RADIUS server ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.delete_external_radius_server(**kwargs)
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

    def xapi_base_delete_internal_radius_server(self, **kwargs):

        """
        Delete internal RADIUS server configuration  # noqa: E501
        
        Delete an existing internal RADIUS server configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_internal_radius_server(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                delete internal radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.delete_internal_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The internal RADIUS server ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.delete_internal_radius_server(**kwargs)
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

    def xapi_base_delete_ldap_server(self, **kwargs):

        """
        Delete a LDAP server  # noqa: E501
        
        Delete a specific LDAP server by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ldap_server(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                delete ldap server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.delete_ldap_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The LDAP server ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.delete_ldap_server(**kwargs)
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

    def xapi_base_delete_radius_client_object(self, **kwargs):

        """
        Delete a RADIUS client object configuration  # noqa: E501
        
        Delete an existing RADIUS client object configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_radius_client_object(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                delete radius client object    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.delete_radius_client_object(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The RADIUS client object ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.delete_radius_client_object(**kwargs)
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

    def xapi_base_delete_radius_proxy(self, **kwargs):

        """
        Delete the RADIUS proxy configuration  # noqa: E501
        
        Delete an existing RADIUS proxy configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_radius_proxy(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                delete radius proxy    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.delete_radius_proxy(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The RADIUS proxy ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.delete_radius_proxy(**kwargs)
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

    def xapi_base_get_external_radius_server(self, **kwargs):

        """
        Get external RADIUS server by ID  # noqa: E501
        
        Get detailed configuration for a specific external RADIUS server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_external_radius_server(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                get external radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.get_external_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The ID for external RADIUS server (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqExternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.get_external_radius_server(**kwargs)
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

    def xapi_base_get_internal_radius_server(self, **kwargs):

        """
        Get internal RADIUS server by ID  # noqa: E501
        
        Get detailed configuration for internal RADIUS server by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_internal_radius_server(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                get internal radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.get_internal_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The ID for internal RADIUS server (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqInternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.get_internal_radius_server(**kwargs)
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

    def xapi_base_get_ldap_server(self, **kwargs):

        """
        Get LDAP server by ID  # noqa: E501
        
        Get a specific LDAP server by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ldap_server(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                get ldap server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.get_ldap_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The LDAP server  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqLdapServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.get_ldap_server(**kwargs)
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

    def xapi_base_get_radius_client_object(self, **kwargs):

        """
        Get RADIUS client object by ID  # noqa: E501
        
        Get detailed configuration for a specific RADIUS client object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radius_client_object(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                get radius client object    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.get_radius_client_object(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The ID of RADIUS client object (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadiusClientObject
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.get_radius_client_object(**kwargs)
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

    def xapi_base_get_radius_proxy(self, **kwargs):

        """
        Get the RADIUS proxy configuration  # noqa: E501
        
        Get an existing RADIUS proxy configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radius_proxy(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                get radius proxy    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.get_radius_proxy(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The RADIUS proxy ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadiusProxy
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.get_radius_proxy(**kwargs)
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

    def xapi_base_list_active_directory_servers(self, **kwargs):

        """
        List active directory servers  # noqa: E501
        
        List a page of active directory servers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_active_directory_servers(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list active directory servers    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_active_directory_servers(**kwargs)
        
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
        :return: PagedXiqActiveDirectoryServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_active_directory_servers(**kwargs)
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

    def xapi_base_list_captive_web_portals(self, **kwargs):

        """
        List captive web portals  # noqa: E501
        
        List a page of Captive Web Portals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_captive_web_portals(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list captive web portals    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_captive_web_portals(**kwargs)
        
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
        :return: PagedXiqCwp
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_captive_web_portals(**kwargs)
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

    def xapi_base_list_external_radius_servers(self, **kwargs):

        """
        List external RADIUS servers  # noqa: E501
        
        List a page of external RADIUS server configurations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_external_radius_servers(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list external radius servers    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_external_radius_servers(**kwargs)
        
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
        :return: PagedXiqExternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_external_radius_servers(**kwargs)
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

    def xapi_base_list_internal_radius_devices(self, **kwargs):

        """
        List all internal RADIUS devices  # noqa: E501
        
        List all internal RADIUS devices fields.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_internal_radius_devices(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list internal radius devices    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_internal_radius_devices(**kwargs)
        
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
        :return: PagedXiqInternalRadiusDevice
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_internal_radius_devices(**kwargs)
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

    def xapi_base_list_internal_radius_servers(self, **kwargs):

        """
        List all internal RADIUS servers  # noqa: E501
        
        List all internal RADIUS servers configurations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_internal_radius_servers(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list internal radius servers    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_internal_radius_servers(**kwargs)
        
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
        :return: PagedXiqInternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_internal_radius_servers(**kwargs)
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

    def xapi_base_list_ldap_servers(self, **kwargs):

        """
        List LDAP servers  # noqa: E501
        
        List a page of LDAP servers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ldap_servers(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list ldap servers    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_ldap_servers(**kwargs)
        
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
        :return: PagedXiqLdapServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_ldap_servers(**kwargs)
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

    def xapi_base_list_radius_client_objects(self, **kwargs):

        """
        List RADIUS client objects  # noqa: E501
        
        List a page of RADIUS client object configurations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_radius_client_objects(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list radius client objects    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_radius_client_objects(**kwargs)
        
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
        :return: PagedXiqRadiusClientObject
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_radius_client_objects(**kwargs)
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

    def xapi_base_list_radius_proxies(self, **kwargs):

        """
        List RADIUS proxies  # noqa: E501
        
        List a page of RADIUS proxy configurations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_radius_proxies(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list radius proxies    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_radius_proxies(**kwargs)
        
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
        :return: PagedXiqRadiusProxy
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_radius_proxies(**kwargs)
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

    def xapi_base_list_radius_proxy_devices(self, **kwargs):

        """
        List Radius proxy devices  # noqa: E501
        
        List devices for Radius Proxy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_radius_proxy_devices(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                list radius proxy devices    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.list_radius_proxy_devices(**kwargs)
        
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
        :return: PagedXiqInternalRadiusDevice
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.list_radius_proxy_devices(**kwargs)
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

    def xapi_base_update_external_radius_server(self, **kwargs):

        """
        Update external RADIUS server configuration  # noqa: E501
        
        Update external RADIUS server configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_external_radius_server(id, xiq_update_external_radius_server_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                update external radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.update_external_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The external RADIUS server ID. (required)
        :param XiqUpdateExternalRadiusServerRequest xiq_update_external_radius_server_request: The payload to update the external RADIUS server (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.update_external_radius_server(**kwargs)
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

    def xapi_base_update_internal_radius_server(self, **kwargs):

        """
        Update internal RADIUS server configuration  # noqa: E501
        
        Update internal RADIUS server configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_internal_radius_server(id, xiq_update_internal_radius_server_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                update internal radius server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.update_internal_radius_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The internal RADIUS server ID (required)
        :param XiqUpdateInternalRadiusServerRequest xiq_update_internal_radius_server_request: The payload to update the internal RADIUS server (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqInternalRadiusServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.update_internal_radius_server(**kwargs)
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

    def xapi_base_update_ldap_server(self, **kwargs):

        """
        Update LDAP server configuration  # noqa: E501
        
        Update configuration for a specific LDAP server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ldap_server(id, xiq_update_ldap_server_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                update ldap server    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.update_ldap_server(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The LDAP server ID. (required)
        :param XiqUpdateLdapServerRequest xiq_update_ldap_server_request: The body of update LDAP server API (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqLdapServer
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.update_ldap_server(**kwargs)
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

    def xapi_base_update_radius_client_object(self, **kwargs):

        """
        Update RADIUS client object configuration  # noqa: E501
        
        Update RADIUS client object configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_radius_client_object(id, xiq_update_radius_client_object_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                update radius client object    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.update_radius_client_object(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The RADIUS client object ID. (required)
        :param XiqUpdateRadiusClientObjectRequest xiq_update_radius_client_object_request: The payload to update the RADIUS client object (required)
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.update_radius_client_object(**kwargs)
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

    def xapi_base_update_radius_proxy(self, **kwargs):

        """
        Update RADIUS proxy configuration  # noqa: E501
        
        Update RADIUS proxy configuration by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_radius_proxy(id, xiq_update_radius_proxy_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseConfigurationAuthenticationApi.py
        
                update radius proxy    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseConfigurationAuthenticationApi import XapiBaseConfigurationAuthenticationApi
        
                xapiBaseConfigurationAuthenticationApi = XapiBaseConfigurationAuthenticationApi()
                xapiBaseConfigurationAuthenticationApi.update_radius_proxy(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The RADIUS proxy ID (required)
        :param XiqUpdateRadiusProxyRequest xiq_update_radius_proxy_request: The body of update RADIUS proxy API (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadiusProxy
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
            api_instance = self.extremecloudiq.ConfigurationAuthenticationApi(api_client)
            try:
                api_response = api_instance.update_radius_proxy(**kwargs)
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

