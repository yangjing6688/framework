from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationTcpKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationTcpKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_tcp_stack(self, port_string, source_ip, netmask=None, gateway_address=None, mac_address=None,
                         vlan_id=None, **kwargs):
        """
        Keyword Arguments:
        [self] -
        [port_string] -
        [source_ip] -
        [netmask] -
        [gateway_address] -
        [mac_address] -
        [vlan_id] -  (default: None)

        create_tcp_stack
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.TCP_API, **kwargs)

        self.emulation_api.create_tcp_stack(self.current_port, source_ip, netmask, gateway_address,
                                            mac_address, vlan_id)
        self._keyword_cleanup()
