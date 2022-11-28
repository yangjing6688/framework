from pprint import pprint
import time
try:
    import extremecloudiq2
    from extremecloudiq.rest import ApiException
except:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')


class Example:

    def login(self, url, username, password):
        """
           - Login to the XIQ instance and return the configuration that can be used to send other commands.

           :param url - The XIQ Instance url
           :param username - The username for the XIQ instance
           :param password - The password for the XIQ instance
           :return: api_response  This will be None if the command failed or will contain the JSON from the API call
       """
        configuration = extremecloudiq.Configuration(
            host=url,
            username=username,
            password=password
        )
        access_token = None
        with extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = extremecloudiq.AuthenticationApi(api_client)
            xiq_login_request = {"username": username,
                                 "password": password}

            try:
                # User login with username and password
                api_response = api_instance.login(xiq_login_request)
                pprint(api_response)
                configuration.access_token = api_response.access_token
            except ApiException as e:
                print("Exception when calling AuthenticationApi->login: %s\n" % e)
                raise e

        return configuration


    def get_viq_info(self, configuration):
        """
            - Get the VIQ information

            :param configuration: The configuration that was returned from the login.
            :return: api_response  This will be None if the command failed or will contain the JSON from the API call
        """

        api_response = None
        # Check that the access_token is in
        if configuration.access_token == None:
            raise "Error: access_token is None in the configuration"

        # Enter a context with an instance of the API client
        with extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = extremecloudiq.AccountApi(api_client)
            try:
                # Get VIQ Info
                api_response = api_instance.get_viq_info()
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling AccountApi->get_viq_info: %s\n" % e)
                raise e
        return api_response