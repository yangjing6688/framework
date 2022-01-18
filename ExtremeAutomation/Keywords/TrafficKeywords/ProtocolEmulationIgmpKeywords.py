from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationIgmpKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationIgmpKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_igmp_host(self, port_string, source_ip, netmask, gateway_address, mac_address, igmp_version=2,
                         vlan_id=None, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]        - A dictionary of the tgen_port and tgen_name to configure.
        [source_ip]          - The source ip address of the host.
        [netmask]            - The netmask of the host.
        [gateway_address]    - The gateway IP Address of the host.
        [mac_address]        - The source MAC address of the host.
        [igmp_version]       - The IGMP Version that the host will use.
        [vlan_id]            - The VLAN ID for the host.
        [options]            - A dictionary of available options to include on the interface.

        Creates an IGMP emulated host.  (NOTE:  Only IGMPv2 is supported at this time)
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.IGMP_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_igmp_host(self.current_port, source_ip, netmask, gateway_address,
                                            mac_address, igmp_version, vlan_id, options)

        self._keyword_cleanup()

    def remove_igmp_host(self, port_string, **kwargs):
        """
        Keyword Arguments:
        [port_string]        - A dictionary of the tgen_port and tgen_name to configure.

        Removes an IGMP emulated host.  (NOTE:  Only IGMPv2 is supported at this time)
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.IGMP_API, **kwargs)

        self.emulation_api.remove_igmp_host(self.current_port, port_string)

        self._keyword_cleanup()

    def generate_igmp_join(self, port_string, source_ip, multicast_address, **kwargs):
        """
        Keyword Arguments:
        [port_string]        - A dictionary of the tgen_port and tgen_name to configure.
        [source_ip]          - The source ip address of the host.
        [multicast_address]  - The multicast IP address to join.

        Generates an igmp join for the specified multicast group.  (NOTE:  Only IGMPv2 is supported at this time)
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.IGMP_API, **kwargs)

        self.emulation_api.generate_igmp_join(self.current_port, source_ip, multicast_address)

        self._keyword_cleanup()

    def generate_igmp_leave(self, port_string, source_ip, multicast_address, **kwargs):
        """
        Keyword Arguments:
        [port_string]        - A dictionary of the tgen_port and tgen_name to configure.
        [source_ip]          - The source ip address of the host.
        [multicast_address]  - The multicast IP address to leave.

        Generates an igmp leave for the specified multicast group.  (NOTE:  Only IGMPv2 is supported at this time)
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.IGMP_API, **kwargs)

        self.emulation_api.generate_igmp_leave(self.current_port, source_ip, multicast_address)

        self._keyword_cleanup()
