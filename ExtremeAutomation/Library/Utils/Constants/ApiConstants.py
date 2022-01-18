from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement

netelem = NetworkElement("os", "platform", "unit", "version")
link = netelem.get_api("api")


class ApiConstants(object):
    def __getattribute__(self, item):
        val = super(ApiConstants, self).__getattribute__(item)

        return val["constant"] if isinstance(val, dict) else val

    def __init__(self):
        self.link = link
