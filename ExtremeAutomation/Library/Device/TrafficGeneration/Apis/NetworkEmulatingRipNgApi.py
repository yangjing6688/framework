from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingRipNgApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingRipNgApi, self).__init__(device)

    @abc.abstractmethod
    def create_ripng_interface(self, port_string, router_id_and_source_ip, prefix_length, mac_address, vlan_id=None,
                               mode="R1", refresh_time=30):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_ripng_route(self, port_string, router_id, first_ip, next_hop="0:0:0:0:0:0:0:0", prefix_length=64, metric=1,
                        num_routes=1, step=1):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def delete_ripng_route(self, port_string, router_id, first_ip, next_hop="0:0:0:0:0:0:0:0", prefix_length=64,
                           num_routes=1, step=1):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_ripng_router(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def ripng_config(self, port_string, tx_delay):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_ripng_stats(self, port_string, router_id):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingRipNgConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    RIPNG_API = "RIPNG_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
