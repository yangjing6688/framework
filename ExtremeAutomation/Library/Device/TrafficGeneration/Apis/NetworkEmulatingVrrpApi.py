import abc
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class NetworkEmulatingVrrpApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingVrrpApi, self).__init__(device)

    def create_and_go_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address,
                                     backup_address, vlan_id=None, priority=200, advertise_interval_msecs=1000,
                                     version=2):
        self.create_vrrp_interface(port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id,
                                   priority, advertise_interval_msecs, version)
        self.add_vrf(port_string, router_id, 1, backup_address, priority)
        self.enable_vrf(port_string, router_id, 1)

    @abc.abstractmethod
    def create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, priority=200, advertise_interval_msecs=1000, version=2):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_vrrp_router(self, port_string, router_id, route_address):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def add_vrf(self, port_string, router_id, vrf_id, backup_address, priority=150):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def enable_vrf(self, port_string, router_id, vrf_id, enabled=True):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_vrf(self, port_string, router_id, vrf_id):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingVrrpConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    VRRP_API = "VRRP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
