from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingIgmpApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingIgmpApi, self).__init__(device)

    @abc.abstractmethod
    def create_igmp_host(self, port_string, source_ip, netmask, gateway_address, mac_address, igmp_version=2,
                         vlan_id=None, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def generate_igmp_leave(self, port_string, source_ip, multicast_address):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def generate_igmp_join(self, port_string, source_ip, multicast_address):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_igmp_host(self, port_string):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingIgmpConstants(object):
    __metaclass = Singleton

    # api reference constant for this api to get it from the device
    IGMP_API = "IGMP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
