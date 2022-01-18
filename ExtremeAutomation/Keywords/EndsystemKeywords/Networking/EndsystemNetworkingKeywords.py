from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.NetworkingConstants \
    import NetworkingConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.NetworkingConstants \
    import NetworkingConstants as CommandConstants


class EndsystemNetworkingKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemNetworkingKeywords, self).__init__()
        self.api_const = self.constants.API_NETWORKING
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    def connect_to_wireless_network(self, device_name, ssid, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ssid] - The ssid of the wireless network being connected to.

        This keyword will connect to the wireless network with the SSID provided.

        * Currently this keyword is only supported on windows and a netsh profile must already exist.
        If the ability to connect to wireless networks without a netsh profile is needed additional
        functionality will need to be added.
        """
        args = {"ssid": ssid}

        return self.execute_keyword(device_name, args, self.cmd_const.CONNECT_TO_WIRELESS_NETWORK, **kwargs)

    def disconnect_from_wireless_network(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        This keyword will disconnect from the wireless network.
        """
        return self.execute_keyword(device_name, {}, self.cmd_const.DISCONNECT_FROM_WIRELESS_NETWORK, **kwargs)

    def verify_endsys_wireless_network_connected(self, device_name, ssid, **kwargs):
        """
        [device_name] - The device the keyword should be run against.
        [ssid] - The SSID of the wireless network the end system should be connected to.

        Verifies that the end system is connected to the specified wireless network.
        """
        args = {"ssid": ssid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_WIRELESS_NETWORK,
                                           self.parse_const.CHECK_WIRELESS_NETWORK_CONNECTED, True,
                                           "End system {device_name} was connected to SSID {ssid}.",
                                           "End system {device_name} was NOT connected to SSID {ssid}.",
                                           wait_for=True, **kwargs)

    def verify_endsys_wireless_network_disconnected(self, device_name, **kwargs):
        """
        [device_name] - The device the keyword should be run against.

        Verifies that the end system is not connected to any wireless network.
        """
        return self.execute_verify_keyword(device_name, {}, self.cmd_const.SHOW_WIRELESS_NETWORK,
                                           self.parse_const.CHECK_WIRELESS_NETWORK_DISCONNECTED, True,
                                           "End system {device_name} is not connected to a wireless network.",
                                           "End system {device_name} IS CONNECTED to a wireless network.",
                                           wait_for=True, **kwargs)
