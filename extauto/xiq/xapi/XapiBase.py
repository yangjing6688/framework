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
        # Check to see if the user enabled XAPI via the kwargs or globally
        if self.XapiHelper.common_validation.get_kwarg(kwargs, "XAPI_ENABLED", None) or self.xapiHelper.is_xapi_enabled():
            return True
        else:
            return False