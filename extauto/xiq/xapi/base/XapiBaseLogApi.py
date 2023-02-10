
from extauto.xiq.xapi.XapiBase import XapiBase


class XapiBaseLogApi(XapiBase):

	def __init__(self):
		super().__init__()

    def xapi_base_list_accounting_logs(self, **kwargs):

        """
		List accounting logs  # noqa: E501
		
		List a page of accounting logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_accounting_logs(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param str calling_station_id: The calling station ID
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqAccountingLog
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_accounting_logs(**kwargs)
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

    def xapi_base_list_accounting_logs_with_http_info(self, **kwargs):

        """
		List accounting logs  # noqa: E501
		
		List a page of accounting logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_accounting_logs_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param str calling_station_id: The calling station ID
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqAccountingLog, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_accounting_logs_with_http_info(**kwargs)
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

    def xapi_base_list_audit_logs(self, **kwargs):

        """
		List audit logs  # noqa: E501
		
		List a page of audit logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_audit_logs(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param list[XiqAuditLogCategory] categories: Audit category
		:param str username: The user login name
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqAuditLog
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_audit_logs(**kwargs)
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

    def xapi_base_list_audit_logs_with_http_info(self, **kwargs):

        """
		List audit logs  # noqa: E501
		
		List a page of audit logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_audit_logs_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param list[XiqAuditLogCategory] categories: Audit category
		:param str username: The user login name
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqAuditLog, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_audit_logs_with_http_info(**kwargs)
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

    def xapi_base_list_auth_logs(self, **kwargs):

        """
		List auth logs  # noqa: E501
		
		List a page of auth logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_auth_logs(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param str calling_station_id: The calling station ID
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqAuthLog
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_auth_logs(**kwargs)
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

    def xapi_base_list_auth_logs_with_http_info(self, **kwargs):

        """
		List auth logs  # noqa: E501
		
		List a page of auth logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_auth_logs_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param str calling_station_id: The calling station ID
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqAuthLog, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_auth_logs_with_http_info(**kwargs)
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

    def xapi_base_list_credential_logs(self, **kwargs):

        """
		List credential logs  # noqa: E501
		
		List a page of credential logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_credential_logs(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqCredentialLog
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_credential_logs(**kwargs)
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

    def xapi_base_list_credential_logs_with_http_info(self, **kwargs):

        """
		List credential logs  # noqa: E501
		
		List a page of credential logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_credential_logs_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqCredentialLog, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_credential_logs_with_http_info(**kwargs)
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

    def xapi_base_list_email_logs(self, **kwargs):

        """
		List Email logs  # noqa: E501
		
		List a page of Email logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_email_logs(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqEmailLog
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_email_logs(**kwargs)
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

    def xapi_base_list_email_logs_with_http_info(self, **kwargs):

        """
		List Email logs  # noqa: E501
		
		List a page of Email logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_email_logs_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str username: The user login name
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqEmailLog, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_email_logs_with_http_info(**kwargs)
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

    def xapi_base_list_sms_logs(self, **kwargs):

        """
		List SMS logs  # noqa: E501
		
		List a page of SMS logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_sms_logs(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str phone_number: The phone number
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqSmsLog
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_sms_logs(**kwargs)
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

    def xapi_base_list_sms_logs_with_http_info(self, **kwargs):

        """
		List SMS logs  # noqa: E501
		
		List a page of SMS logs.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_sms_logs_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param str phone_number: The phone number
		:param int start_time: The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative
		:param int end_time: The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqSmsLog, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.LogApi(api_client)
            try:
                api_response = api_instance.list_sms_logs_with_http_info(**kwargs)
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

