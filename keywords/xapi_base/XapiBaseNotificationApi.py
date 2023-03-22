
#    =========================================
#    WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py
#    DO NOT EDIT THIS FILE
#    =========================================



from tools.xapi.XapiHelper import XapiHelper


class XapiBaseNotificationApi(XapiHelper):

    def __init__(self):
        super().__init__()

    def xapi_base_create_subscriptions(self, **kwargs):

        """
            Create webhook subscriptions  # noqa: E501
            
            Create multiple webhook subscriptions.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.create_subscriptions(xiq_create_webhook_subscription_request, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseNotificationApi.py
            
                create subscriptions    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseNotificationApi import XapiBaseNotificationApi
            
                xapiBaseNotificationApi = XapiBaseNotificationApi()
                xapiBaseNotificationApi.create_subscriptions(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param list[XiqCreateWebhookSubscriptionRequest] xiq_create_webhook_subscription_request: The payload of create multiple webhook subscriptions (required)
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
            api_instance = self.extremecloudiq.NotificationApi(api_client)
            try:
                api_response = api_instance.create_subscriptions(**kwargs)
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

    def xapi_base_delete_subscription(self, **kwargs):

        """
            Delete webhook subscription  # noqa: E501
            
            Delete an exist webhook subscription.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.delete_subscription(id, async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseNotificationApi.py
            
                delete subscription    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseNotificationApi import XapiBaseNotificationApi
            
                xapiBaseNotificationApi = XapiBaseNotificationApi()
                xapiBaseNotificationApi.delete_subscription(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param int id: The webhook subscription ID (required)
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
            api_instance = self.extremecloudiq.NotificationApi(api_client)
            try:
                api_response = api_instance.delete_subscription(**kwargs)
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

    def xapi_base_list(self, **kwargs):

        """
            List webhook subscriptions  # noqa: E501
            
            List all webhook subscriptions.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.list(async_req=True)
            >>> result = thread.get()
            
            **Note - The kwargs options are explained in the :param section below.
            These can be placed in the kwargs dict as key / values pairs or 
            passed into the function as key / value pairs as separate arguments.
            
            Robot ->
            
                Library    keywords/xapi_base/XapiBaseNotificationApi.py
            
                list    **kwargs
            
            Pytest ->
            
                from keywords.xapi_base.XapiBaseNotificationApi import XapiBaseNotificationApi
            
                xapiBaseNotificationApi = XapiBaseNotificationApi()
                xapiBaseNotificationApi.list(**kwargs)
            
            :param async_req bool: execute request asynchronously
            :param _preload_content: if False, the urllib3.HTTPResponse object will
                                     be returned without reading/decoding response
                                     data. Default is True.
            :param _request_timeout: timeout setting for this request. If one
                                     number provided, it will be total request
                                     timeout. It can also be a pair (tuple) of
                                     (connection, read) timeouts.
            :return: list[XiqWebhookSubscription]
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
            api_instance = self.extremecloudiq.NotificationApi(api_client)
            try:
                api_response = api_instance.list(**kwargs)
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

