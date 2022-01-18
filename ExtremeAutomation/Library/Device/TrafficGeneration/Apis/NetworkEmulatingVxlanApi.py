from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingVxlanApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingVxlanApi, self).__init__(device)

    def create_vxlan_interface_and_host(self, port_string, router_id_and_source_ip, netmask_outter,
                                        gateway_address_outter, mac_address_outter, vlan_id_outter, source_ip_inner,
                                        netmask_inner, mac_address_inner, vlan_id_inner, vxlan_vlan_id, vxlan_src_ip,
                                        vxlan_dest_ip):
        self.create_vxlan_interface(port_string, router_id_and_source_ip, netmask_outter, gateway_address_outter,
                                    mac_address_outter, vlan_id_outter)

        self.add_vxlan_host(port_string, router_id_and_source_ip, source_ip_inner, netmask_inner, mac_address_inner,
                            vlan_id_inner, vxlan_vlan_id, vxlan_src_ip, vxlan_dest_ip)

    # set vlan_id to 0 or None for untagged
    @abc.abstractmethod
    def create_vxlan_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address,
                               vlan_id):
        return self.logger.log_unimplemented_method()

    # set vlan_id to 0 or None for untagged
    @abc.abstractmethod
    def add_vxlan_host(self, port_string, router_id, inner_source_ip, netmask, mac_address, vlan_id, vxlan_vlan_id,
                       vxlan_src_ip, vxlan_dest_ip):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingVxlanConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    VXLAN_API = "VXLAN_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
