
from extauto.xiq.xapi.XapiBase import XapiBase


class XapiBaseNetworkPolicyApi(XapiBase):

	def __init__(self):
		super().__init__()

    def xapi_base_add_ssids_to_network_policy(self, **kwargs):

        """
		Add SSIDs to a network policy  # noqa: E501
		
		Add SSIDs to a specific network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.add_ssids_to_network_policy(id, request_body, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param list[int] request_body: The SSID ids to be added to the network policy (required)
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.add_ssids_to_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_add_ssids_to_network_policy_with_http_info(self, **kwargs):

        """
		Add SSIDs to a network policy  # noqa: E501
		
		Add SSIDs to a specific network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.add_ssids_to_network_policy_with_http_info(id, request_body, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param list[int] request_body: The SSID ids to be added to the network policy (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.add_ssids_to_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_create_network_policy(self, **kwargs):

        """
		Create network policy  # noqa: E501
		
		Create a new network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.create_network_policy(xiq_create_network_policy_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqCreateNetworkPolicyRequest xiq_create_network_policy_request: The body of create network policy API (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqNetworkPolicy
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.create_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_create_network_policy_with_http_info(self, **kwargs):

        """
		Create network policy  # noqa: E501
		
		Create a new network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.create_network_policy_with_http_info(xiq_create_network_policy_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqCreateNetworkPolicyRequest xiq_create_network_policy_request: The body of create network policy API (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqNetworkPolicy, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.create_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_delete_network_policy(self, **kwargs):

        """
		Delete the network policy  # noqa: E501
		
		Delete an existing network policy by ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_network_policy(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.delete_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_delete_network_policy_with_http_info(self, **kwargs):

        """
		Delete the network policy  # noqa: E501
		
		Delete an existing network policy by ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_network_policy_with_http_info(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.delete_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_delete_ssids_from_network_policy(self, **kwargs):

        """
		Removes SSIDs from the network policy  # noqa: E501
		
		Removing multiple SSIDs from the network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_ssids_from_network_policy(id, request_body, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param list[int] request_body: The SSID ids to be removed from the network policy (required)
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.delete_ssids_from_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_delete_ssids_from_network_policy_with_http_info(self, **kwargs):

        """
		Removes SSIDs from the network policy  # noqa: E501
		
		Removing multiple SSIDs from the network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_ssids_from_network_policy_with_http_info(id, request_body, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param list[int] request_body: The SSID ids to be removed from the network policy (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.delete_ssids_from_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_get_network_policy(self, **kwargs):

        """
		Get the network policy  # noqa: E501
		
		Get an existing network policy by ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.get_network_policy(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqNetworkPolicy
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.get_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_get_network_policy_with_http_info(self, **kwargs):

        """
		Get the network policy  # noqa: E501
		
		Get an existing network policy by ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.get_network_policy_with_http_info(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqNetworkPolicy, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.get_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_list_network_polices(self, **kwargs):

        """
		List network policies  # noqa: E501
		
		List a page of network policies.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_network_polices(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param list[str] policy_names: The list of policy names
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqNetworkPolicy
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.list_network_polices(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_list_network_polices_with_http_info(self, **kwargs):

        """
		List network policies  # noqa: E501
		
		List a page of network policies.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_network_polices_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param list[str] policy_names: The list of policy names
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqNetworkPolicy, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.list_network_polices_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_list_ssids_by_network_policy(self, **kwargs):

        """
		List SSIDs for a network policy  # noqa: E501
		
		List a page of SSIDs for a specific network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_ssids_by_network_policy(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.list_ssids_by_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_list_ssids_by_network_policy_with_http_info(self, **kwargs):

        """
		List SSIDs for a network policy  # noqa: E501
		
		List a page of SSIDs for a specific network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_ssids_by_network_policy_with_http_info(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqSsid, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.list_ssids_by_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_update_network_policy(self, **kwargs):

        """
		Update the network policy  # noqa: E501
		
		Update network policy by ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_network_policy(id, xiq_update_network_policy_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param XiqUpdateNetworkPolicyRequest xiq_update_network_policy_request: The body of update network policy API (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqNetworkPolicy
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.update_network_policy(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_update_network_policy_with_http_info(self, **kwargs):

        """
		Update the network policy  # noqa: E501
		
		Update network policy by ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_network_policy_with_http_info(id, xiq_update_network_policy_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The network policy ID (required)
		:param XiqUpdateNetworkPolicyRequest xiq_update_network_policy_request: The body of update network policy API (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqNetworkPolicy, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.NetworkPolicyApi(api_client)
            try:
                api_response = api_instance.update_network_policy_with_http_info(**kwargs)
                # If the _async is True, we will use the Long Runnning Operation methods
                if kwargs.get('_async', False):
                    operation_id = self.getLongRunningOperationId(api_response)
                    returnValue = self.getAsyncLongRunningOperation(operation_id)
                    if returnValue:
                        kwargs['pass_msg'] = f"returned: {returnValue}"
                        self.xapiHelper.common_validation.passed(**kwargs)
                        return returnValue
                    else:
                        kwargs['fail_msg'] = f"getAsyncLongRunningOperation failed to return SUCCESS"
                        self.xapiHelper.common_validation.failed(**kwargs)
                        return -1
                else:
                    self.valid_http_response(api_response)
                    self.xapiHelper.common_validation.passed(**kwargs)
                    return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

