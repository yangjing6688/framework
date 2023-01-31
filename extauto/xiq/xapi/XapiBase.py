import time
from extauto.xiq.xapi.XapiHelper import XapiHelper
from extauto.common.Utils import Utils

try:
    import extremecloudiq
    from extremecloudiq.rest import ApiException
except:
    pprint('WARNING: The library for ExtremecloudIQ cannot be loaded, please ensure this libaray is installed if you are trying to use the XAPI')


class XapiBase(object):

    def __init__(self):
        self.xapiHelper = XapiHelper()
        self.utils = Utils()
        self.extremecloudiq = extremecloudiq
        self.ApiException = ApiException

    def is_xapi_enabled(self, **kwargs):
        """
            Checks to see if the XAPI_ENABLED variable is set in kwargs or globally

            :param kwargs: Looks for XAPI_ENABLED in kwargs
            :return: True if the XAPI_ENABLED is in kwargs or set globally, false otherwise
        """
        # Check to see if the user enabled XAPI via the kwargs or globally
        if self.XapiHelper.common_validation.get_kwarg(kwargs, "XAPI_ENABLED", None) or self.xapiHelper.is_xapi_enabled():
            return True
        else:
            return False

    def valid_http_reponse(self, api_reponse):
        """
            This method will valid the http response object make sure the return code is 200 or 201
            :param api_reponse: The HTTPResponse object
            :return: True when the status is 200 or 201, throws exception otherwise
        """
        if api_reponse.status != 200 and api_reponse.status != 201:
            raise Exception(f'ERROR: valid_http_reponse -> HTTPResponse status returned failure: {api_reponse.status}')
        return True

