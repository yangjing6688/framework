
from extauto.xiq.xapi.XapiBase import XapiBase


class XapiBaseConfigurationCertificateApi(XapiBase):

	def __init__(self):
		super().__init__()

    def xapi_base_list_certificates(self, **kwargs):

        """
		List certificates  # noqa: E501
		
		List a page of certificates.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_certificates(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param XiqCertificateType cert_type: The certificate type
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: PagedXiqCertificate
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
            api_instance = self.extremecloudiq.ConfigurationCertificateApi(api_client)
            try:
                api_response = api_instance.list_certificates(**kwargs)
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

    def xapi_base_list_certificates_with_http_info(self, **kwargs):

        """
		List certificates  # noqa: E501
		
		List a page of certificates.  # noqa: E501
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please pass async_req=True
		>>> thread = api.list_certificates_with_http_info(async_req=True)
		>>> result = thread.get()
		
		:param async_req bool: execute request asynchronously
		:param int page: Page number, min = 1
		:param int limit: Page Size, min = 1, max = 100
		:param XiqCertificateType cert_type: The certificate type
		:param _return_http_data_only: response data without head status code
		                               and headers
		:param _preload_content: if False, the urllib3.HTTPResponse object will
		                         be returned without reading/decoding response
		                         data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
		                         number provided, it will be total request
		                         timeout. It can also be a pair (tuple) of
		                         (connection, read) timeouts.
		:return: tuple(PagedXiqCertificate, status_code(int), headers(HTTPHeaderDict))
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
            api_instance = self.extremecloudiq.ConfigurationCertificateApi(api_client)
            try:
                api_response = api_instance.list_certificates_with_http_info(**kwargs)
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

