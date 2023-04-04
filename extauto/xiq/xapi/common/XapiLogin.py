from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
from keywords.xapi_base.XapiBaseAuthenticationApi import XapiBaseAuthenticationApi
from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi
from tools.xapi.XapiHelper import XapiHelper

class XapiLogin(XapiHelper):

    def __init__(self):
        super().__init__()
        self.xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
        self.xapiBaseAuthenticationApi = XapiBaseAuthenticationApi()
        self.xapiBaseAccountApi = XapiBaseAccountApi()


    def login(self, username, password, **kwargs):
        """
           - Login to the XIQ instance and return the configuration that can be used to send other commands.

           :param url - The XIQ Instance url
           :param username - The username for the XIQ instance
           :param password - The password for the XIQ instance
           :return: 1 if success or -1 if failure
       """

        # Login information
        xapi_url = self.get_xapi_url()
        
        # Check for https
        if not xapi_url.lower().startswith(('http://', 'https://')):
            xapi_url = f'https://{xapi_url}'
        self.utils.print_info(f'Using XAPI URL: {xapi_url}')
        
        if xapi_url:
            configuration = self.xapiBaseAuthenticationApi.extremecloudiq.Configuration(
                host=xapi_url,
                username=username,
                password=password
            )
            # Set the base configuration
            self.set_xapi_configuration(configuration)

            xiq_login_request = {"username": username,
                                 "password": password}

            try:
                api_response = self.xapiBaseAuthenticationApi.xapi_base_login(xiq_login_request=xiq_login_request)
                if api_response != -1:
                    configuration.access_token = api_response.access_token
                    # Set the configuration with the token
                    self.set_xapi_configuration(configuration)
                else:
                    kwargs['fail_msg'] = "Error when calling AuthenticationApi->login"
                    self.common_validation.failed(**kwargs)
                    return -1

                # Get the new configuration Object and generate a new token
                xiq_generate_api_token_request = {"description": "Token for Automation Test",
                                                  "expire_time": None, "permissions": []}
                api_response = self.xapiBaseAuthorizationApi.xapi_base_generate_api_token(xiq_generate_api_token_request=xiq_generate_api_token_request)
                if api_response != -1:
                    configuration.access_token = api_response.access_token
                    # Set the configuration with the new token
                    self.set_xapi_configuration(configuration)
                    kwargs['pass_msg'] = 'User was logged in and token was generated'
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = 'Token was not generated'
                    self.common_validation.failed(**kwargs)
                    return -1
            except Exception:
                kwargs['fail_msg'] = 'Token was not generated'
                self.common_validation.failed(**kwargs)
                return -1


    def logout(self,  **kwargs):
        """
           - logout of the XIQ instance and return
           :return: 1 if success or -1 if failure
        """
        auth = self.xapiBaseAuthenticationApi.xapi_base_logout()
        if auth != -1:
            configuration = self.get_xapi_configuration()
            configuration.access_token = None
            self.xapiBaseAuthenticationApi.set_xapi_configuration(configuration)
            kwargs['pass_msg'] = 'User was logged out'
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = 'Failed to log out user'
            self.common_validation.failed(**kwargs)
            return -1

    def xapi_capture_data_center_name(self, **kwargs):
        """
            Get the XIQ instance name
        :param kwargs: kwargs
        :return: XIQ instance name or 'Unknown' if there was an error
        """
        api_response = self.xapiBaseAccountApi.xapi_base_get_home_account()
        if api_response != -1:
            kwargs['pass_msg'] = f'Got data center name: {api_response.name}'
            self.common_validation.passed(**kwargs)
            return api_response.name
        else:
            kwargs['fail_msg'] = 'Failed to get data center name'
            self.common_validation.failed(**kwargs)

    # def xapi_capture_xiq_version(self, **kwargs):
    #     """
    #         Get the XIQ instance version
    #     :param kwargs: kwargs
    #     :return: XIQ instance version
    #     """
    #     # get the xapi URL from the global variables
    #     xapi_url = self.get_xapi_url()
    #
    #     configuration = self.get_xapi_configuration()
    #     with self.xapiBaseAuthenticationApi.extremecloudiq.ApiClient(configuration) as api_client:
    #         # Create an instance of the API class
    #         api_instance = self.xapiBaseAuthenticationApi.extremecloudiq.AccountApi(api_client)
    #
    #         try:
    #             # get the data
    #             api_response = api_instance.get_home_account()
    #             self.utils.print_info(api_response)
    #             return 1
    #         except self.ApiException as e:
    #             self.utils.print_error("Exception when calling AuthenticationApi->login: %s\n" % e)
    #     self.common_validation.failed(**kwargs)
    #     return -1

