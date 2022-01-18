from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingRipApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingRipApi, self).__init__(device)

    @abc.abstractmethod
    def create_rip_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address, vlan_id,
                             mode="R1", refresh_time=30):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_rip_route(self, port_string, router_id, first_ip, netmask="0.0.0.0", next_hop="0.0.0.0", metric=1,
                      num_routes=1, step=1):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def delete_rip_route(self, port_string, router_id, first_ip, netmask="0.0.0.0", num_routes=1, step=1):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_rip_router(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def rip_config(self, port_string, tx_delay):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_rip_stats(self, port_string, router_id):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingRipConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    RIP_API = "RIP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
