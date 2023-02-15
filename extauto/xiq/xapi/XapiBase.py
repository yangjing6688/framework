import json
from time import sleep
import pprint
from extauto.xiq.xapi.XapiHelper import XapiHelper
from extauto.common.Utils import Utils

try:
    import extremecloudiq
    from extremecloudiq.rest import ApiException
except Exception:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')


class XapiBase(object):

    def __init__(self):
        self.xapiHelper = XapiHelper()
        self.utils = Utils()
        self.extremecloudiq = extremecloudiq
        self.ApiException = ApiException

    def is_xapi_enabled(self, **kwargs):
        """
            Checks to see if the XAPI_ENABLE variable is set in kwargs or globally

            :param kwargs: Looks for XAPI_ENABLE in kwargs
            :return: True if the XAPI_ENABLE is in kwargs or set globally, false otherwise
        """
        # Check to see if the user enabled XAPI via the kwargs or globally
        if self.XapiHelper.common_validation.get_kwarg(kwargs, "XAPI_ENABLE", None) or self.xapiHelper.is_xapi_enabled():
            return True
        else:
            return False

    def print_http_response(self, http_response):
        """
            Prints the http repsonse for the object that is passed in
        :param http_response: http repsonse object
        :return: None
        """
        try:
            self.utils.print_info("http_response: " + json.dumps(json.loads(http_response.data), indent=4, separators=(',', ': ')))
        except Exception:
            pass

    def valid_http_response(self, api_response):
        """
            This method will valid the http response object make sure the return code is 200 or 201
            :param api_response: The HTTPResponse object
            :return: True when the status is 200 or 201, throws exception otherwise
        """
        self.print_http_response(api_response)
        # if the api_response is None
        if not api_response:
            raise Exception(
                'ERROR: valid_http_response -> HTTPResponse is None')
        # Make sure we have a status to check
        elif 'status' in api_response.__dict__.keys():
            # we do, so check to make sure we got a 200 or 201
            if api_response.status != 200 and api_response.status != 201:
                raise Exception(f'ERROR: valid_http_response -> HTTPResponse status returned failure: {api_response.status}')
        return True

    def getLongRunningOperationId(self, response):
        id = response.headers['Location'].split('/')[-1]
        return id

    def getAsyncLongRunningOperation(self, operation_id, **kwargs):
        """
            This method will poll the operation untit it has completed
        :param operation_id: When calling keywords with the async_req=True, this will be the operation id that is returned
        :return: The completed operation json, or None for an error
        """

        # Get the configuration from the Global varibles
        configuration = self.xapiHelper.get_xapi_configuration()

        # Check that the access_token is in
        if configuration.access_token == None:
            raise Exception("Error: access_token is None in the configuration")

        # Enter a context with an instance of the API client
        with self.extremecloudiq.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = self.extremecloudiq.OperationApi(api_client)

            try:
                # get operation status
                operation_object = api_instance.get_operation(operation_id)
                while operation_object.metadata.status != 'SUCCEEDED':
                    self.utils.print_info(f'Operation {operation_id} has not completed [SUCCEEDED], sleep for 10 seconds and try again')
                    sleep(10)
                    operation_object = api_instance.get_operation(operation_id)
                return operation_object.response
            except Exception as e:
                kwargs['fail_msg'] = f"Exception when calling DeviceApi->onboard_devices: {e}"
                self.xapiHelper.common_validation.failed(**kwargs)
                return None

