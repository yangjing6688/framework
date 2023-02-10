
from extauto.xiq.xapi.XapiBase import XapiBase


class XapiBaseConfigurationUserManagementApi(XapiBase):

	def __init__(self):
		super().__init__()

    def xapi_base_add_key_based_pcg_users(self, **kwargs):

        """
		Add users to a PCG-enabled network policy  # noqa: E501
		
		Add users to a PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.add_key_based_pcg_users(policy_id, xiq_create_key_based_pcg_users_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqCreateKeyBasedPcgUsersRequest xiq_create_key_based_pcg_users_request: The payload of add users to PCG-enabled network policy (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.add_key_based_pcg_users(**kwargs)
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

    def xapi_base_add_key_based_pcg_users_with_http_info(self, **kwargs):

        """
		Add users to a PCG-enabled network policy  # noqa: E501
		
		Add users to a PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.add_key_based_pcg_users_with_http_info(policy_id, xiq_create_key_based_pcg_users_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqCreateKeyBasedPcgUsersRequest xiq_create_key_based_pcg_users_request: The payload of add users to PCG-enabled network policy (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.add_key_based_pcg_users_with_http_info(**kwargs)
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

    def xapi_base_assign_ports(self, **kwargs):

        """
		Assign ports to devices in network policy  # noqa: E501
		
		Assign ports for devices (only support AP150W now) in a network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.assign_ports(policy_id, xiq_pcg_assign_ports_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqPcgAssignPortsRequest xiq_pcg_assign_ports_request: The payload of assign ports for devices (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqPcgAssignPortsResponse
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.assign_ports(**kwargs)
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

    def xapi_base_assign_ports_with_http_info(self, **kwargs):

        """
		Assign ports to devices in network policy  # noqa: E501
		
		Assign ports for devices (only support AP150W now) in a network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.assign_ports_with_http_info(policy_id, xiq_pcg_assign_ports_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqPcgAssignPortsRequest xiq_pcg_assign_ports_request: The payload of assign ports for devices (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqPcgAssignPortsResponse, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.assign_ports_with_http_info(**kwargs)
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

    def xapi_base_create_end_user(self, **kwargs):

        """
		Create an end user  # noqa: E501
		
		Create a new end user.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.create_end_user(xiq_create_end_user_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqCreateEndUserRequest xiq_create_end_user_request: Create end user request body (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqEndUser
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.create_end_user(**kwargs)
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

    def xapi_base_create_end_user_with_http_info(self, **kwargs):

        """
		Create an end user  # noqa: E501
		
		Create a new end user.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.create_end_user_with_http_info(xiq_create_end_user_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqCreateEndUserRequest xiq_create_end_user_request: Create end user request body (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqEndUser, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.create_end_user_with_http_info(**kwargs)
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

    def xapi_base_create_user_group(self, **kwargs):

        """
		Create user group  # noqa: E501
		
		Create a new user group.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.create_user_group(xiq_create_user_group_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqCreateUserGroupRequest xiq_create_user_group_request: Create user group request body (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqUserGroup
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.create_user_group(**kwargs)
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

    def xapi_base_create_user_group_with_http_info(self, **kwargs):

        """
		Create user group  # noqa: E501
		
		Create a new user group.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.create_user_group_with_http_info(xiq_create_user_group_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqCreateUserGroupRequest xiq_create_user_group_request: Create user group request body (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqUserGroup, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.create_user_group_with_http_info(**kwargs)
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

    def xapi_base_delete_key_based_pcg_users(self, **kwargs):

        """
		Delete users from a PCG-enabled network policy  # noqa: E501
		
		Delete users from a PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_key_based_pcg_users(policy_id, xiq_delete_key_based_pcg_users_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqDeleteKeyBasedPcgUsersRequest xiq_delete_key_based_pcg_users_request: The payload of delete Key-based PCG users request (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_key_based_pcg_users(**kwargs)
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

    def xapi_base_delete_key_based_pcg_users_with_http_info(self, **kwargs):

        """
		Delete users from a PCG-enabled network policy  # noqa: E501
		
		Delete users from a PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_key_based_pcg_users_with_http_info(policy_id, xiq_delete_key_based_pcg_users_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqDeleteKeyBasedPcgUsersRequest xiq_delete_key_based_pcg_users_request: The payload of delete Key-based PCG users request (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_key_based_pcg_users_with_http_info(**kwargs)
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

    def xapi_base_delete_pcg(self, **kwargs):

        """
		Delete Private Client Group from a network policy  # noqa: E501
		
		Delete Private Client Group settings from a network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_pcg(policy_id, ids, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param list[int] ids: The IDs of the Key-based PCG entity to be deleted from network policy (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_pcg(**kwargs)
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

    def xapi_base_delete_pcg_with_http_info(self, **kwargs):

        """
		Delete Private Client Group from a network policy  # noqa: E501
		
		Delete Private Client Group settings from a network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_pcg_with_http_info(policy_id, ids, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param list[int] ids: The IDs of the Key-based PCG entity to be deleted from network policy (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_pcg_with_http_info(**kwargs)
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

    def xapi_base_delete_ssid_user(self, **kwargs):

        """
		Delete end user by ID  # noqa: E501
		
		Delete a specific end user.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_ssid_user(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The end user ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_ssid_user(**kwargs)
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

    def xapi_base_delete_ssid_user_with_http_info(self, **kwargs):

        """
		Delete end user by ID  # noqa: E501
		
		Delete a specific end user.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_ssid_user_with_http_info(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The end user ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_ssid_user_with_http_info(**kwargs)
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

    def xapi_base_delete_user_group(self, **kwargs):

        """
		Delete user group by ID  # noqa: E501
		
		Delete the user-group for the specified ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_user_group(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The user group ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_user_group(**kwargs)
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

    def xapi_base_delete_user_group_with_http_info(self, **kwargs):

        """
		Delete user group by ID  # noqa: E501
		
		Delete the user-group for the specified ID.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.delete_user_group_with_http_info(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The user group ID (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.delete_user_group_with_http_info(**kwargs)
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

    def xapi_base_email_keys(self, **kwargs):

        """
		Send keys to users in network policy via Email  # noqa: E501
		
		Send keys to specified users in PCG-enabled network policy via Email.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.email_keys(policy_id, user_ids, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param list[int] user_ids: The user IDs (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.email_keys(**kwargs)
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

    def xapi_base_email_keys_with_http_info(self, **kwargs):

        """
		Send keys to users in network policy via Email  # noqa: E501
		
		Send keys to specified users in PCG-enabled network policy via Email.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.email_keys_with_http_info(policy_id, user_ids, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param list[int] user_ids: The user IDs (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.email_keys_with_http_info(**kwargs)
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

    def xapi_base_generate_keys(self, **kwargs):

        """
		Generate shared keys for users in network policy  # noqa: E501
		
		Generate/regenerate shared keys for specified users in a specific PCG-enable network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.generate_keys(policy_id, user_ids, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param list[int] user_ids: The user IDs (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.generate_keys(**kwargs)
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

    def xapi_base_generate_keys_with_http_info(self, **kwargs):

        """
		Generate shared keys for users in network policy  # noqa: E501
		
		Generate/regenerate shared keys for specified users in a specific PCG-enable network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.generate_keys_with_http_info(policy_id, user_ids, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param list[int] user_ids: The user IDs (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.generate_keys_with_http_info(**kwargs)
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

    def xapi_base_get_key_based_pcg_users(self, **kwargs):

        """
		Get users for a PCG-enabled network policy  # noqa: E501
		
		Get users for a specific PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.get_key_based_pcg_users(policy_id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: list[XiqKeyBasedPcgUser]
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.get_key_based_pcg_users(**kwargs)
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

    def xapi_base_get_key_based_pcg_users_with_http_info(self, **kwargs):

        """
		Get users for a PCG-enabled network policy  # noqa: E501
		
		Get users for a specific PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.get_key_based_pcg_users_with_http_info(policy_id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(list[XiqKeyBasedPcgUser], status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.get_key_based_pcg_users_with_http_info(**kwargs)
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

    def xapi_base_get_port_assignments(self, **kwargs):

        """
		Get device port assignments in network policy  # noqa: E501
		
		Get port assignments for devices (only support AP150W now) in a network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.get_port_assignments(policy_id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqGetPortAssignmentDetailsResponse
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.get_port_assignments(**kwargs)
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

    def xapi_base_get_port_assignments_with_http_info(self, **kwargs):

        """
		Get device port assignments in network policy  # noqa: E501
		
		Get port assignments for devices (only support AP150W now) in a network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.get_port_assignments_with_http_info(policy_id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqGetPortAssignmentDetailsResponse, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.get_port_assignments_with_http_info(**kwargs)
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

    def xapi_base_list_email_templates(self, **kwargs):

        """
		List Email templates  # noqa: E501
		
		List all Email notification templates.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_email_templates(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqPasswordType password_type: The password type
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: list[XiqEmailTemplate]
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_email_templates(**kwargs)
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

    def xapi_base_list_email_templates_with_http_info(self, **kwargs):

        """
		List Email templates  # noqa: E501
		
		List all Email notification templates.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_email_templates_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqPasswordType password_type: The password type
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(list[XiqEmailTemplate], status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_email_templates_with_http_info(**kwargs)
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

    def xapi_base_list_end_users(self, **kwargs):

        """
		List end users  # noqa: E501
		
		List a page of end users.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_end_users(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param list[int] user_group_ids: The user group IDs
		:param list[str] usernames: The list of username
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqEndUser
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_end_users(**kwargs)
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

    def xapi_base_list_end_users_with_http_info(self, **kwargs):

        """
		List end users  # noqa: E501
		
		List a page of end users.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_end_users_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param list[int] user_group_ids: The user group IDs
		:param list[str] usernames: The list of username
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqEndUser, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_end_users_with_http_info(**kwargs)
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

    def xapi_base_list_key_based_private_client_groups(self, **kwargs):

        """
		List Key-based Private Client Groups  # noqa: E501
		
		List all Key-based Private Client Groups.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_key_based_private_client_groups(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: list[XiqKeyBasedPcg]
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_key_based_private_client_groups(**kwargs)
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

    def xapi_base_list_key_based_private_client_groups_with_http_info(self, **kwargs):

        """
		List Key-based Private Client Groups  # noqa: E501
		
		List all Key-based Private Client Groups.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_key_based_private_client_groups_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(list[XiqKeyBasedPcg], status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_key_based_private_client_groups_with_http_info(**kwargs)
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

    def xapi_base_list_sms_templates(self, **kwargs):

        """
		List SMS templates  # noqa: E501
		
		List all SMS notification templates.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_sms_templates(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqPasswordType password_type: The password type
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: list[XiqSmsTemplate]
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_sms_templates(**kwargs)
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

    def xapi_base_list_sms_templates_with_http_info(self, **kwargs):

        """
		List SMS templates  # noqa: E501
		
		List all SMS notification templates.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_sms_templates_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqPasswordType password_type: The password type
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(list[XiqSmsTemplate], status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_sms_templates_with_http_info(**kwargs)
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

    def xapi_base_list_user_groups(self, **kwargs):

        """
		List user groups  # noqa: E501
		
		List a page of user groups.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_user_groups(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param XiqPasswordDbLocation password_db_location: The password DB location
		:param XiqPasswordType password_type: The password type
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqUserGroup
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_user_groups(**kwargs)
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

    def xapi_base_list_user_groups_with_http_info(self, **kwargs):

        """
		List user groups  # noqa: E501
		
		List a page of user groups.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_user_groups_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param XiqPasswordDbLocation password_db_location: The password DB location
		:param XiqPasswordType password_type: The password type
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqUserGroup, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.list_user_groups_with_http_info(**kwargs)
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

    def xapi_base_onboard_key_based_private_client_group(self, **kwargs):

        """
		Create Key-based PCG in network policy  # noqa: E501
		
		Create a Key-based Private Client Group for a specific network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.onboard_key_based_private_client_group(policy_id, xiq_onboard_key_based_pcg_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqOnboardKeyBasedPcgRequest xiq_onboard_key_based_pcg_request: (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.onboard_key_based_private_client_group(**kwargs)
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

    def xapi_base_onboard_key_based_private_client_group_with_http_info(self, **kwargs):

        """
		Create Key-based PCG in network policy  # noqa: E501
		
		Create a Key-based Private Client Group for a specific network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.onboard_key_based_private_client_group_with_http_info(policy_id, xiq_onboard_key_based_pcg_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqOnboardKeyBasedPcgRequest xiq_onboard_key_based_pcg_request: (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.onboard_key_based_private_client_group_with_http_info(**kwargs)
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

    def xapi_base_regenerate_end_user_password(self, **kwargs):

        """
		Regenerate a new password for the end user  # noqa: E501
		
		Update the user's password with a system generated password.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.regenerate_end_user_password(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The enduser's ID (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqRegenerateEndUserPasswordResponse
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.regenerate_end_user_password(**kwargs)
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

    def xapi_base_regenerate_end_user_password_with_http_info(self, **kwargs):

        """
		Regenerate a new password for the end user  # noqa: E501
		
		Update the user's password with a system generated password.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.regenerate_end_user_password_with_http_info(id, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The enduser's ID (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqRegenerateEndUserPasswordResponse, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.regenerate_end_user_password_with_http_info(**kwargs)
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

    def xapi_base_setup_key_based_private_client_group_network_policy(self, **kwargs):

        """
		Setup a Key-based Private Client Group  # noqa: E501
		
		Setup a Key-based Private Client Group, including network policy, user, user group, SSID, etc.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.setup_key_based_private_client_group_network_policy(xiq_init_key_based_pcg_network_policy_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqInitKeyBasedPcgNetworkPolicyRequest xiq_init_key_based_pcg_network_policy_request: The request to setup Key-based PCG network policy (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.setup_key_based_private_client_group_network_policy(**kwargs)
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

    def xapi_base_setup_key_based_private_client_group_network_policy_with_http_info(self, **kwargs):

        """
		Setup a Key-based Private Client Group  # noqa: E501
		
		Setup a Key-based Private Client Group, including network policy, user, user group, SSID, etc.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.setup_key_based_private_client_group_network_policy_with_http_info(xiq_init_key_based_pcg_network_policy_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param XiqInitKeyBasedPcgNetworkPolicyRequest xiq_init_key_based_pcg_network_policy_request: The request to setup Key-based PCG network policy (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.setup_key_based_private_client_group_network_policy_with_http_info(**kwargs)
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

    def xapi_base_update_end_user(self, **kwargs):

        """
		Update an end user  # noqa: E501
		
		Update a specific end user.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_end_user(id, xiq_update_end_user_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The end user ID (required)
		:param XiqUpdateEndUserRequest xiq_update_end_user_request: Update end user request body (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqEndUser
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.update_end_user(**kwargs)
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

    def xapi_base_update_end_user_with_http_info(self, **kwargs):

        """
		Update an end user  # noqa: E501
		
		Update a specific end user.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_end_user_with_http_info(id, xiq_update_end_user_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The end user ID (required)
		:param XiqUpdateEndUserRequest xiq_update_end_user_request: Update end user request body (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqEndUser, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.update_end_user_with_http_info(**kwargs)
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

    def xapi_base_update_key_based_pcg_users(self, **kwargs):

        """
		Replace all users in a PCG-enabled network policy  # noqa: E501
		
		Replace all users in a specific PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_key_based_pcg_users(policy_id, xiq_update_key_based_pcg_users_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqUpdateKeyBasedPcgUsersRequest xiq_update_key_based_pcg_users_request: The payload of update Key-based PCG users request (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.update_key_based_pcg_users(**kwargs)
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

    def xapi_base_update_key_based_pcg_users_with_http_info(self, **kwargs):

        """
		Replace all users in a PCG-enabled network policy  # noqa: E501
		
		Replace all users in a specific PCG-enabled network policy.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_key_based_pcg_users_with_http_info(policy_id, xiq_update_key_based_pcg_users_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int policy_id: The network policy ID (required)
		:param XiqUpdateKeyBasedPcgUsersRequest xiq_update_key_based_pcg_users_request: The payload of update Key-based PCG users request (required)
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.update_key_based_pcg_users_with_http_info(**kwargs)
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

    def xapi_base_update_user_group(self, **kwargs):

        """
		Update user group  # noqa: E501
		
		Update existing user group information.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_user_group(id, xiq_update_user_group_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The user group ID. (required)
		:param XiqUpdateUserGroupRequest xiq_update_user_group_request: Update user-group request body (required)
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: XiqUserGroup
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.update_user_group(**kwargs)
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

    def xapi_base_update_user_group_with_http_info(self, **kwargs):

        """
		Update user group  # noqa: E501
		
		Update existing user group information.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.update_user_group_with_http_info(id, xiq_update_user_group_request, async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int id: The user group ID. (required)
		:param XiqUpdateUserGroupRequest xiq_update_user_group_request: Update user-group request body (required)
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(XiqUserGroup, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationUserManagementApi(api_client)
            try:
                api_response = api_instance.update_user_group_with_http_info(**kwargs)
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

