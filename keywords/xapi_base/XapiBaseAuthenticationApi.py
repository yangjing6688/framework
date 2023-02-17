
from tools.xapi.XapiBase import XapiBase


class XapiBaseAuthenticationApi(XapiBase):

    def __init__(self):
        super().__init__()

    def xapi_base_login(self, **kwargs):

        """
        User login with username and password  # noqa: E501
        
        Get access token via username and password authentication. The client must present Bearer token to access the protected API endpoints.The Bearer token should be present in the "Authorization" request header field and use the "Bearer" HTTP authentication scheme to transmit the access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login(xiq_login_request, async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseAuthenticationApi.py
        
                login    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseAuthenticationApi import XapiBaseAuthenticationApi
        
                xapiBaseAuthenticationApi = XapiBaseAuthenticationApi()
                xapiBaseAuthenticationApi.login(**kwargs)
        
        :param async_req bool: execute request asynchronously
        :param XiqLoginRequest xiq_login_request: Login request body (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XiqLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """


        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()
        api_response = None

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.AuthenticationApi(api_client)
            try:
                api_response = api_instance.login(**kwargs)
                self.xapiHelper.common_validation.passed(**kwargs)
                return api_response

            except self.ApiException as e:
                kwargs['fail_msg'] = f"ApiException : {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

    def xapi_base_logout(self, **kwargs):

        """
        User logout (Revoke the current access token)  # noqa: E501
        
        User logout, the current access token will be revoked and the following access with the same token will be immediately denied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout(async_req=True)
        >>> result = thread.get()
        
            Robot:
                Library    keywords/xapi_base/XapiBaseAuthenticationApi.py
        
                logout    **kwargs
            Pytest:
                from keywords.xapi_base.XapiBaseAuthenticationApi import XapiBaseAuthenticationApi
        
                xapiBaseAuthenticationApi = XapiBaseAuthenticationApi()
                xapiBaseAuthenticationApi.logout(**kwargs)
        
        :param async_req bool: execute request asynchronously
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
            api_instance = self.extremecloudiq.AuthenticationApi(api_client)
            try:
                api_response = api_instance.logout(**kwargs)
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

