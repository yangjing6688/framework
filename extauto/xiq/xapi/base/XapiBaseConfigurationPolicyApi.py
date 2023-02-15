
from extauto.xiq.xapi.XapiBase import XapiBase


class XapiBaseConfigurationPolicyApi(XapiBase):

    def __init__(self):
        super().__init__()

    def xapi_base_attach_cwp_to_ssid(self, **kwargs):

        """
        Attach CWP to an SSID  # noqa: E501
        
        Attach CWP to an SSID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.attach_cwp_to_ssid(id, body, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                attach cwp to ssid    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.attach_cwp_to_ssid(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param int body: The CWP ID to be attached to the SSID. For CWP with only User Auth on Captive Web Portal enabled, please also attach a RADIUS server group or enable ExtremeCloud IQ Authentication Service. (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.attach_cwp_to_ssid(**kwargs)
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

    def xapi_base_attach_radius_server_group_to_ssid(self, **kwargs):

        """
        Attach radius server group to an SSID  # noqa: E501
        
        Attach radius server group to an SSID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.attach_radius_server_group_to_ssid(id, body, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                attach radius server group to ssid    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.attach_radius_server_group_to_ssid(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param int body: The radius server group ID to be attached to the SSID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.attach_radius_server_group_to_ssid(**kwargs)
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

    def xapi_base_attach_user_profile_to_ssid(self, **kwargs):

        """
        Attach user profile to an SSID  # noqa: E501
        
        Attach user profile to an SSID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.attach_user_profile_to_ssid(id, body, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                attach user profile to ssid    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.attach_user_profile_to_ssid(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param int body: The user profile ID to be attached to the SSID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.attach_user_profile_to_ssid(**kwargs)
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

    def xapi_base_change_psk_password(self, **kwargs):

        """
        Change the SSID PSK password  # noqa: E501
        
        Change the SSID PSK password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_psk_password(id, body, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                change psk password    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.change_psk_password(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param str body: The new SSID PSK password (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.change_psk_password(**kwargs)
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

    def xapi_base_create_classification_rule(self, **kwargs):

        """
        Create classification rule  # noqa: E501
        
        Create a new classification rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_classification_rule(xiq_create_classification_rule_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                create classification rule    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.create_classification_rule(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateClassificationRuleRequest xiq_create_classification_rule_request: The payload to create a new classification rule (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClassificationRule
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.create_classification_rule(**kwargs)
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

    def xapi_base_create_cloud_config_group(self, **kwargs):

        """
        Create new cloud config group  # noqa: E501
        
        Create a new cloud config group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cloud_config_group(xiq_create_cloud_config_group_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                create cloud config group    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.create_cloud_config_group(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateCloudConfigGroupRequest xiq_create_cloud_config_group_request: Create new cloud config group request body (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqCloudConfigGroup
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.create_cloud_config_group(**kwargs)
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

    def xapi_base_create_mac_oui_profile(self, **kwargs):

        """
        Create a MAC OUI profile  # noqa: E501
        
        Create a new MAC OUI profile for radio usage optimization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mac_oui_profile(xiq_create_rp_mac_oui_profile_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                create mac oui profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.create_mac_oui_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateRpMacOuiProfileRequest xiq_create_rp_mac_oui_profile_request: The request body to create new user profile. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpMacOuiProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.create_mac_oui_profile(**kwargs)
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

    def xapi_base_create_radio_profile(self, **kwargs):

        """
        Create a radio profile  # noqa: E501
        
        Create a new radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_radio_profile(xiq_create_radio_profile_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                create radio profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.create_radio_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateRadioProfileRequest xiq_create_radio_profile_request: The request body to create new user profile. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadioProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.create_radio_profile(**kwargs)
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

    def xapi_base_create_user_profile(self, **kwargs):

        """
        Create a user profile  # noqa: E501
        
        Create a new user profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_profile(xiq_create_user_profile_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                create user profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.create_user_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqCreateUserProfileRequest xiq_create_user_profile_request: The request body to create new user profile. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqUserProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.create_user_profile(**kwargs)
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

    def xapi_base_delete_classification_rule(self, **kwargs):

        """
        Delete classification rule by ID  # noqa: E501
        
        Delete an existing classification rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_classification_rule(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                delete classification rule    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.delete_classification_rule(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The classification rule ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.delete_classification_rule(**kwargs)
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

    def xapi_base_delete_cloud_config_group(self, **kwargs):

        """
        Delete a cloud config group  # noqa: E501
        
        Delete a specific cloud config group by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_cloud_config_group(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                delete cloud config group    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.delete_cloud_config_group(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The cloud config group ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.delete_cloud_config_group(**kwargs)
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

    def xapi_base_delete_co_user_profile(self, **kwargs):

        """
        Delete an user profile by ID  # noqa: E501
        
        Delete an existing user profile by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_co_user_profile(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                delete co user profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.delete_co_user_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The user profile ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.delete_co_user_profile(**kwargs)
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

    def xapi_base_delete_radio_profile(self, **kwargs):

        """
        Delete radio profile by ID  # noqa: E501
        
        Delete the existing radio profile by the profile ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_radio_profile(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                delete radio profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.delete_radio_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio profile ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.delete_radio_profile(**kwargs)
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

    def xapi_base_delete_rp_mac_oui_profile(self, **kwargs):

        """
        Delete MAC OUI profile  # noqa: E501
        
        Delete the existing MAC OUI profile for radio usage optimization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_rp_mac_oui_profile(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                delete rp mac oui profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.delete_rp_mac_oui_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The MAC OUI profile ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.delete_rp_mac_oui_profile(**kwargs)
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

    def xapi_base_disable_ssid_cwp(self, **kwargs):

        """
        Disable the CWP on the SSID  # noqa: E501
        
        Disable the CWP on the SSID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_ssid_cwp(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                disable ssid cwp    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.disable_ssid_cwp(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.disable_ssid_cwp(**kwargs)
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

    def xapi_base_enable_ssid_cwp(self, **kwargs):

        """
        Enable and attach the CWP on the SSID  # noqa: E501
        
        Enable and attach the CWP on the SSID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_ssid_cwp(id, body, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                enable ssid cwp    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.enable_ssid_cwp(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param int body: The new CWP ID.  For CWP with only User Auth on Captive Web Portal enabled, please also attach a RADIUS server group or enable ExtremeCloud IQ Authentication Service. (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.enable_ssid_cwp(**kwargs)
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

    def xapi_base_get_classification_rule(self, **kwargs):

        """
        Get a classification rule by ID  # noqa: E501
        
        Get a specific classification rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_classification_rule(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get classification rule    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_classification_rule(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The classification Rule ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClassificationRule
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_classification_rule(**kwargs)
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

    def xapi_base_get_cloud_config_group(self, **kwargs):

        """
        Get a cloud config group  # noqa: E501
        
        Get cloud config group info for the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cloud_config_group(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get cloud config group    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_cloud_config_group(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The cloud config group ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqCloudConfigGroup
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_cloud_config_group(**kwargs)
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

    def xapi_base_get_neighborhood_analysis(self, **kwargs):

        """
        Get neighborhood analysis settings  # noqa: E501
        
        Get the neighborhood analysis settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_neighborhood_analysis(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get neighborhood analysis    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_neighborhood_analysis(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The neighborhood analysis settings ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpNeighborhoodAnalysis
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_neighborhood_analysis(**kwargs)
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

    def xapi_base_get_radio_profile(self, **kwargs):

        """
        Get radio profile by ID  # noqa: E501
        
        Get radio profile details for the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radio_profile(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get radio profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_radio_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio profile ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadioProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_radio_profile(**kwargs)
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

    def xapi_base_get_rp_channel_selection(self, **kwargs):

        """
        Get channel selection settings  # noqa: E501
        
        Get the channel selection settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rp_channel_selection(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get rp channel selection    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_rp_channel_selection(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The channel selection settings ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpChannelSelection
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_rp_channel_selection(**kwargs)
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

    def xapi_base_get_rp_mac_oui_profile(self, **kwargs):

        """
        Get MAC OUI profile  # noqa: E501
        
        Get the MAC OUI profile belonging the radio optimization settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rp_mac_oui_profile(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get rp mac oui profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_rp_mac_oui_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The MAC OUI profile ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpMacOuiProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_rp_mac_oui_profile(**kwargs)
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

    def xapi_base_get_rp_miscellaneous_settings(self, **kwargs):

        """
        Get radio miscellaneous settings  # noqa: E501
        
        Get the radio miscellaneous settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rp_miscellaneous_settings(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get rp miscellaneous settings    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_rp_miscellaneous_settings(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio miscellaneous settings ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpMiscellaneousSettings
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_rp_miscellaneous_settings(**kwargs)
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

    def xapi_base_get_rp_radio_usage_optimization(self, **kwargs):

        """
        Get radio usage optimization settings  # noqa: E501
        
        Get the radio usage optimization settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rp_radio_usage_optimization(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get rp radio usage optimization    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_rp_radio_usage_optimization(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio usage optimization settings ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpRadioUsageOptimization
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_rp_radio_usage_optimization(**kwargs)
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

    def xapi_base_get_rp_sensor_scan_settings(self, **kwargs):

        """
        Get sensor scan settings  # noqa: E501
        
        Get the sensor scan settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rp_sensor_scan_settings(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get rp sensor scan settings    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_rp_sensor_scan_settings(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The sensor scan settings ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpSensorScanSettings
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_rp_sensor_scan_settings(**kwargs)
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

    def xapi_base_get_rp_wmm_qos_settings(self, **kwargs):

        """
        Get Wmm QoS settings  # noqa: E501
        
        Get the Wi-Fi Multimedia (WMM) QoS settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rp_wmm_qos_settings(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get rp wmm qos settings    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_rp_wmm_qos_settings(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio QoS settings ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpWmmQosSettings
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_rp_wmm_qos_settings(**kwargs)
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

    def xapi_base_get_user_profile(self, **kwargs):

        """
        Get user profile by ID  # noqa: E501
        
        Get user profile details for the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                get user profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.get_user_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The user profile ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqUserProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.get_user_profile(**kwargs)
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

    def xapi_base_list_classification_rules(self, **kwargs):

        """
        List classification rules  # noqa: E501
        
        List a page of classification rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_classification_rules(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list classification rules    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_classification_rules(**kwargs)
        
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
        :return: PagedXiqClassificationRule
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_classification_rules(**kwargs)
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

    def xapi_base_list_cloud_config_groups(self, **kwargs):

        """
        List clould config groups  # noqa: E501
        
        List a papge of cloud config groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cloud_config_groups(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list cloud config groups    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_cloud_config_groups(**kwargs)
        
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
        :return: PagedXiqCloudConfigGroup
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_cloud_config_groups(**kwargs)
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

    def xapi_base_list_l3_address_profiles(self, **kwargs):

        """
        List L3 address profiles  # noqa: E501
        
        List all L3 Address Profiles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_l3_address_profiles(address_type, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list l3 address profiles    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_l3_address_profiles(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param str address_type: The address type (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[XiqL3AddressProfile]
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_l3_address_profiles(**kwargs)
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

    def xapi_base_list_radio_profiles(self, **kwargs):

        """
        List radio profiles  # noqa: E501
        
        List a page of radio profiles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_radio_profiles(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list radio profiles    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_radio_profiles(**kwargs)
        
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
        :return: PagedXiqRadioProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_radio_profiles(**kwargs)
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

    def xapi_base_list_rp_mac_oui_profiles(self, **kwargs):

        """
        List MAC OUI profiles  # noqa: E501
        
        List a page of MAC OUI profiles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_rp_mac_oui_profiles(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list rp mac oui profiles    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_rp_mac_oui_profiles(**kwargs)
        
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
        :return: PagedXiqRpMacOuiProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_rp_mac_oui_profiles(**kwargs)
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

    def xapi_base_list_ssids(self, **kwargs):

        """
        List SSIDs  # noqa: E501
        
        List SSIDs with filter and pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ssids(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list ssids    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_ssids(**kwargs)
        
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
        :return: PagedXiqSsid
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_ssids(**kwargs)
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

    def xapi_base_list_user_profiles(self, **kwargs):

        """
        List user profiles  # noqa: E501
        
        List a page of user profiles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_profiles(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                list user profiles    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.list_user_profiles(**kwargs)
        
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
        :return: PagedXiqUserProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.list_user_profiles(**kwargs)
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

    def xapi_base_rename_ssid(self, **kwargs):

        """
        Rename SSID (Wireless name)  # noqa: E501
        
        Change SSID broadcast name (Wireless name).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rename_ssid(id, body, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                rename ssid    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.rename_ssid(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param str body: The new SSID name (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.rename_ssid(**kwargs)
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

    def xapi_base_set_ssid_mode_dot1x(self, **kwargs):

        """
        Change the SSID mode to 802.1x  # noqa: E501
        
        Change the SSID mode to 802.1x.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_ssid_mode_dot1x(id, xiq_set_ssid_mode_dot1x_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                set ssid mode dot1x    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.set_ssid_mode_dot1x(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param XiqSetSsidModeDot1xRequest xiq_set_ssid_mode_dot1x_request: The payload to change the SSID mode to 802.1x (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.set_ssid_mode_dot1x(**kwargs)
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

    def xapi_base_set_ssid_mode_open(self, **kwargs):

        """
        Change the SSID mode to open access  # noqa: E501
        
        Change the SSID mode to open access.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_ssid_mode_open(id, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                set ssid mode open    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.set_ssid_mode_open(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.set_ssid_mode_open(**kwargs)
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

    def xapi_base_set_ssid_mode_ppsk(self, **kwargs):

        """
        Change the SSID mode to PPSK  # noqa: E501
        
        Change the SSID mode to PPSK.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_ssid_mode_ppsk(id, xiq_set_ssid_mode_ppsk_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                set ssid mode ppsk    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.set_ssid_mode_ppsk(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param XiqSetSsidModePpskRequest xiq_set_ssid_mode_ppsk_request: The payload to change the SSID mode to PPSK (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.set_ssid_mode_ppsk(**kwargs)
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

    def xapi_base_set_ssid_mode_psk(self, **kwargs):

        """
        Change the SSID mode to PSK  # noqa: E501
        
        Change the SSID mode to PSK.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_ssid_mode_psk(id, xiq_set_ssid_mode_psk_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                set ssid mode psk    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.set_ssid_mode_psk(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param XiqSetSsidModePskRequest xiq_set_ssid_mode_psk_request: The payload to change the SSID mode to PSK (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.set_ssid_mode_psk(**kwargs)
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

    def xapi_base_set_ssid_mode_wep(self, **kwargs):

        """
        Change the SSID mode to WEP  # noqa: E501
        
        Change the SSID mode to WEP.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_ssid_mode_wep(id, xiq_set_ssid_mode_wep_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                set ssid mode wep    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.set_ssid_mode_wep(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The SSID ID (required)
        :param XiqSetSsidModeWepRequest xiq_set_ssid_mode_wep_request: The payload to change the SSID mode to WEP (required)
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.set_ssid_mode_wep(**kwargs)
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

    def xapi_base_update_classification_rule(self, **kwargs):

        """
        Update classification rule  # noqa: E501
        
        Update the exist classification rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_classification_rule(id, xiq_update_classification_rule_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update classification rule    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_classification_rule(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The classification rule ID (required)
        :param XiqUpdateClassificationRuleRequest xiq_update_classification_rule_request: The payload to update exist classification rule (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqClassificationRule
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_classification_rule(**kwargs)
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

    def xapi_base_update_cloud_config_group(self, **kwargs):

        """
        Update cloud config group information  # noqa: E501
        
        Update the cloud config group details having the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_cloud_config_group(id, xiq_update_cloud_config_group_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update cloud config group    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_cloud_config_group(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The cloud config group ID (required)
        :param XiqUpdateCloudConfigGroupRequest xiq_update_cloud_config_group_request: Update cloud config group request body (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqCloudConfigGroup
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_cloud_config_group(**kwargs)
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

    def xapi_base_update_co_user_profile(self, **kwargs):

        """
        Update user profile  # noqa: E501
        
        Update an existing user profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_co_user_profile(id, xiq_update_user_profile_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update co user profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_co_user_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The user profile ID. (required)
        :param XiqUpdateUserProfileRequest xiq_update_user_profile_request: The payload of user profile. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqUserProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_co_user_profile(**kwargs)
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

    def xapi_base_update_neighborhood_analysis(self, **kwargs):

        """
        Update neighborhood analysis settings  # noqa: E501
        
        Update the neighborhood analysis settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_neighborhood_analysis(id, xiq_update_rp_neighborhood_analysis_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update neighborhood analysis    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_neighborhood_analysis(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The neighborhood analysis settings ID. (required)
        :param XiqUpdateRpNeighborhoodAnalysisRequest xiq_update_rp_neighborhood_analysis_request: The payload of the update neighborhood analysis settings request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpNeighborhoodAnalysis
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_neighborhood_analysis(**kwargs)
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

    def xapi_base_update_radio_profile(self, **kwargs):

        """
        Update radio profile by ID  # noqa: E501
        
        Update the existing radio profile by the profile ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_radio_profile(id, xiq_update_radio_profile_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update radio profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_radio_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio profile ID. (required)
        :param XiqUpdateRadioProfileRequest xiq_update_radio_profile_request: The payload of the update radio profile request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRadioProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_radio_profile(**kwargs)
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

    def xapi_base_update_rp_channel_selection(self, **kwargs):

        """
        Update channel selection settings  # noqa: E501
        
        Update the channel selection settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rp_channel_selection(id, xiq_update_rp_channel_selection_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update rp channel selection    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_rp_channel_selection(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The channel selection settings ID. (required)
        :param XiqUpdateRpChannelSelectionRequest xiq_update_rp_channel_selection_request: The payload of the update channel selection settings request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpChannelSelection
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_rp_channel_selection(**kwargs)
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

    def xapi_base_update_rp_mac_oui_profile(self, **kwargs):

        """
        Update MAC OUI profile  # noqa: E501
        
        Update the existing MAC OUI profile for radio usage optimization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rp_mac_oui_profile(id, xiq_update_rp_mac_oui_profile_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update rp mac oui profile    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_rp_mac_oui_profile(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The MAC OUI profile ID. (required)
        :param XiqUpdateRpMacOuiProfileRequest xiq_update_rp_mac_oui_profile_request: The payload of the update MAC OUI profile request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpMacOuiProfile
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_rp_mac_oui_profile(**kwargs)
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

    def xapi_base_update_rp_miscellaneous_settings(self, **kwargs):

        """
        Update radio miscellaneous settings  # noqa: E501
        
        Update the radio miscellaneous settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rp_miscellaneous_settings(id, xiq_update_rp_miscellaneous_settings_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update rp miscellaneous settings    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_rp_miscellaneous_settings(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio miscellaneous settings ID. (required)
        :param XiqUpdateRpMiscellaneousSettingsRequest xiq_update_rp_miscellaneous_settings_request: The payload of the update radio miscellaneous settings request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpMiscellaneousSettings
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_rp_miscellaneous_settings(**kwargs)
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

    def xapi_base_update_rp_radio_usage_optimization(self, **kwargs):

        """
        Update radio usage optimization settings  # noqa: E501
        
        Update the radio usage optimization settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rp_radio_usage_optimization(id, xiq_update_rp_radio_usage_optimization_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update rp radio usage optimization    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_rp_radio_usage_optimization(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The radio usage optimization settings ID. (required)
        :param XiqUpdateRpRadioUsageOptimizationRequest xiq_update_rp_radio_usage_optimization_request: The payload of the update radio usage optimization settings request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpRadioUsageOptimization
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_rp_radio_usage_optimization(**kwargs)
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

    def xapi_base_update_rp_sensor_scan_settings(self, **kwargs):

        """
        Update sensor scan settings  # noqa: E501
        
        Update the sensor scan settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rp_sensor_scan_settings(id, xiq_update_rp_sensor_scan_settings_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update rp sensor scan settings    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_rp_sensor_scan_settings(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The sensor scan settings ID. (required)
        :param XiqUpdateRpSensorScanSettingsRequest xiq_update_rp_sensor_scan_settings_request: The payload of the update sensor scan settings request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpSensorScanSettings
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_rp_sensor_scan_settings(**kwargs)
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

    def xapi_base_update_rp_wmm_qos_settings(self, **kwargs):

        """
        Update Wmm QoS settings  # noqa: E501
        
        Update the Wi-Fi Multimedia (WMM) QoS settings belonging to a radio profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rp_wmm_qos_settings(id, xiq_update_rp_wmm_qos_settings_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library     extauto/xiq/xapi/base/XapiBaseConfigurationPolicyApi.py
        
                update rp wmm qos settings    **kwargs
            Pytest:
                from extauto.xiq.xapi.base.XapiBaseConfigurationPolicyApi import XapiBaseConfigurationPolicyApi
        
                xapiBaseConfigurationPolicyApi = XapiBaseConfigurationPolicyApi()
                xapiBaseConfigurationPolicyApi.update_rp_wmm_qos_settings(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param int id: The Wmm QoS settings ID. (required)
        :param XiqUpdateRpWmmQosSettingsRequest xiq_update_rp_wmm_qos_settings_request: The payload of the update Wmm QoS settings request. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqRpWmmQosSettings
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
            api_instance = self.extremecloudiq.ConfigurationPolicyApi(api_client)
            try:
                api_response = api_instance.update_rp_wmm_qos_settings(**kwargs)
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

