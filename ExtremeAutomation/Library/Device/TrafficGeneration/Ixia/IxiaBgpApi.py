from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingBgpApi import NetworkEmulatingBgpApi


class IxiaBgpApi(NetworkEmulatingBgpApi):
    def __init__(self, device):
        super(IxiaBgpApi, self).__init__(device)

    def create_bgp_interface(self, port_string, router_id, local_as, source_ip, netmask, gateway_address, mac_address,
                             vlan_id=None, neighbor_type=None, ip_version="IPv4", options=None):
        return self.logger.log_unimplemented_method()

    def configure_network_generator_bgp_routes_on_bgp_peer(self, bgp_interface_handle, prefix, netmask, num_routes,
                                                           origin_route_enable, origin, ip_version, options=None):
        return self.logger.log_unimplemented_method()

    def start_network_generator_bgp_emulation(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def stop_network_generator_bgp_emulation(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def restart_network_generator_bgp_emulation(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def delete_bgp_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1):
        return self.logger.log_unimplemented_method()

    def remove_bgp_router(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def configure_bgp_options(self, port_string, updateinterval=1000, maxattributes=1000, notifylogsize=256):
        return self.logger.log_unimplemented_method()

    def add_bgp_neighbor(self, port_string, router_id, ip_address, netmask, local_as):
        return self.logger.log_unimplemented_method()

    def add_bgp_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1, origin="IGP", med=0,
                      localpref=0):
        return self.logger.log_unimplemented_method()

    def delete_bpg_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1):
        return self.logger.log_unimplemented_method()

    def get_bgp_state(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def get_bgp_stats(self, port_string, router_id):
        return self.logger.log_unimplemented_method()
