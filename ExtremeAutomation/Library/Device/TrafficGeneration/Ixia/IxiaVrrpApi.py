from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingVrrpApi import NetworkEmulatingVrrpApi


class IxiaVrrpApi(NetworkEmulatingVrrpApi):
    def __init__(self, device):
        super(IxiaVrrpApi, self).__init__(device)

    def create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, priority=200, advertise_interval_msecs=1000, version=2):
        return self.logger.log_unimplemented_method()

    def remove_vrrp_router(self, port_string, router_id, route_address):
        return self.logger.log_unimplemented_method()

    def add_vrf(self, port_string, router_id, vrf_id, backup_address, priority=150):
        return self.logger.log_unimplemented_method()

    def enable_vrf(self, port_string, router_id, vrf_id, enabled=True):
        return self.logger.log_unimplemented_method()

    def remove_vrf(self, port_string, router_id, vrf_id):
        return self.logger.log_unimplemented_method()
