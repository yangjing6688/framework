from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.DemoConstants import DemoConstants \
    as CommandConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.DemoConstants import DemoConstants \
    as ParseConstants


class GIMDemoKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(GIMDemoKeywords, self).__init__()
        self.api_const = self.constants.API_DEMO
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    def verify_guest_onboarding_template(self, device_name, user, onboarding_template, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [host_address] - The host address to be pinged.
        [count] - The number of pings to send.  Setting the default to 1 if not specified.

        Pings a host once by default.  The number of pings to be sent can be changed.
        """
        args = {'user': user,
                "onboarding_template": onboarding_template
                }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.GET_GUEST_USER_DATA,
                                           self.parse_const.VERIFY_GUEST_ONBOARDING_TEMPLATE, True,
                                           "Onbarding templace is equal to given value",
                                           "Onbarding templace is NOT equal to given value",
                                           **kwargs)
