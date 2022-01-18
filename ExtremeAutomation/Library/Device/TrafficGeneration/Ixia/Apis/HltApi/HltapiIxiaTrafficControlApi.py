from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficControlApi import TrafficControlApi, TrafficControlConstants

"""
    This is the API class for the command: traffic_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaTrafficControlApi(TrafficControlApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaTrafficControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_control
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficControlConstants.TRAFFIC_CONTROL_API)
        api.traffic_control(dummyDict)
    """
    def traffic_control(self, argdictionary):
        return super(IxiaTrafficControlApi, self).traffic_control(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    supportedIxiaHltapiCommands = {TrafficControlConstants.ACTION_CMD, TrafficControlConstants.PORT_HANDLE_CMD}
