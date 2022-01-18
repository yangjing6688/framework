from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingLldpApi import NetworkEmulatingLldpApi


class IxiaLldpApi(NetworkEmulatingLldpApi):
    def __init__(self, device):
        super(IxiaLldpApi, self).__init__(device)

    def create_lldp_interface(self, port_string, router_id, mac_address, chassis_mac, ttl):
        return self.logger.log_unimplemented_method()

    def remove_lldp_interface(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def enable_lldp(self, port_string, router_id, enabled=True):
        return self.logger.log_unimplemented_method()

    def start_transmit_tlv(self, port_string, router_id, tlv_name):
        return self.logger.log_unimplemented_method()

    def stop_transmit_tlv(self, port_string, router_id, tlv_name):
        return self.logger.log_unimplemented_method()
