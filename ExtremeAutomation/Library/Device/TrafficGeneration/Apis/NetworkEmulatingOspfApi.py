from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingOspfApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingOspfApi, self).__init__(device)

    @abc.abstractmethod
    def create_ospf_interface(self, port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, link_type="broadcast", area_type="extcapable", passive=False, prio="1",
                              cost="1", trans_delay="40", hello_int="10", dead_int="40", retrans_int="5",
                              wait_time="40"):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step, age, ls_type="AS_EXTERNAL",
                       adv_rtr="0.0.0.0", forward_address="0.0.0.0", cost=1, costype="type1_external", ex_route_tag=1):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def delete_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_ospf_router(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def set_ospf_router_enabled(self, port_string, router_id, enable=True):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_ospf_state(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_ospf_lsas(self, port_string, router_id, lsa, receive_router):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_ospf_stats(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id,
                    attached_router_ip):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id,
                       attached_router_ip):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_stub_network(self, port_string, router_id, ip_address, netmask):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_stub_network(self, port_string, router_id, ip_address, netmask):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingOspfConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    OSPF_API = "OSPF_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
