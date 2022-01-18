from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationVxlanKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationVxlanKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_vxlan_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address,
                               vlan_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id_and_source_ip] -
        [netmask] -
        [gateway_address] -
        [mac_address] -
        [vlan_id] -

        create_vxlan_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VXLAN_API, **kwargs)

        self.emulation_api.create_vxlan_interface(self.current_port, router_id_and_source_ip, netmask,
                                                  gateway_address, mac_address, vlan_id)
        self._keyword_cleanup()

    def add_vxlan_host(self, port_string, router_id, inner_source_ip, netmask, mac_address, vlan_id, vxlan_vlan_id,
                       vxlan_src_ip, vxlan_dest_ip, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [inner_source_ip] -
        [netmask] -
        [mac_address] -
        [vlan_id] -
        [vxlan_vlan_id] -
        [vxlan_src_ip] -
        [vxlan_dest_ip] -

        add_vxlan_host
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VXLAN_API, **kwargs)

        self.emulation_api.add_vxlan_host(self.current_port, router_id, inner_source_ip, netmask,
                                          mac_address, vlan_id, vxlan_vlan_id, vxlan_src_ip, vxlan_dest_ip)
        self._keyword_cleanup()
