import time
from extauto.xiq.xapi.XapiBase import XapiBase

class XapiLogin(XapiBase):

    def login(self, username, password, **kwargs):
        """
           - Login to the XIQ instance and return the configuration that can be used to send other commands.

           :param url - The XIQ Instance url
           :param username - The username for the XIQ instance
           :param password - The password for the XIQ instance
           :return: 1 if success or -1 if failure
       """
        return_code = -1

        # get the xapi URL from the global variables
        xapi_url = self.xapiHelper.get_xapi_url()

        # Login information
        configuration = self.extremecloudiq.Configuration(
            host=xapi_url,
            username=username,
            password=password
        )
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.AuthenticationApi(api_client)

            xiq_login_request = {"username": username,
                                 "password": password}

            try:
                # User login with username and password
                api_response = api_instance.login(xiq_login_request)
                self.utils.print_info(api_response)
                configuration.access_token = api_response.access_token
                self.xapiHelper.set_xapi_configuration(configuration)
            except self.ApiException as e:
                self.utils.print_info("Exception when calling AuthenticationApi->login: %s\n" % e)
                self.xapiHelper.common_validation.failed(**kwargs)
                return -1

        # Get the new configuration Object and generate a new token
        configuration = self.xapiHelper.get_xapi_configuration()
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.AuthorizationApi(api_client)
            xiq_generate_api_token_request = {"description": "Token for Automation Test",
                                              "expire_time": None, "permissions": []}
            try:
                # Generate new API token
                api_response = api_instance.generate_api_token(xiq_generate_api_token_request)
                self.utils.print_info(api_response)
                configuration.access_token = api_response.access_token
                self.xapiHelper.set_xapi_configuration(configuration)
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1
            except self.ApiException as e:
                self.utils.print_error("Exception when calling AuthorizationApi->generate_api_token: %s\n" % e)

        self.xapiHelper.common_validation.failed(**kwargs)
        return -1

    def logout(self,  **kwargs):
        """
           - logout of the XIQ instance and return
           :return: 1 if success or -1 if failure
        """
        return_code = -1

        # get the xapi URL from the global variables
        xapi_url = self.xapiHelper.get_xapi_url()

        configuration = self.xapiHelper.get_xapi_configuration()
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.AuthenticationApi(api_client)

            try:
                # logout
                api_response = api_instance.logout()
                self.utils.print_info(api_response)
                configuration.access_token = None
                self.xapiHelper.set_xapi_configuration(configuration)
                self.xapiHelper.common_validation.passed(**kwargs)
                return 1
            except self.ApiException as e:
                self.utils.print_error("Exception when calling AuthenticationApi->login: %s\n" % e)

        self.xapiHelper.common_validation.failed(**kwargs)
        return -1