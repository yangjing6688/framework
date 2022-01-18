"""
Base class for all port commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class PortBase(CliBaseApi):
    def __init__(self, device):
        super(PortBase, self).__init__()
        self.device = device

    def enable_state(self, *args, **kwargs):
        return self.base_function()

    def disable_state(self, *args, **kwargs):
        return self.base_function()

    def enable_jumbo(self, *args, **kwargs):
        return self.base_function()

    def disable_jumbo(self, *args, **kwargs):
        return self.base_function()

    def set_speed(self, *args, **kwargs):
        return self.base_function()

    def clear_speed(self, *args, **kwargs):
        return self.base_function()

    def show_all_jumbo(self, *args, **kwargs):
        return self.base_function()

    def show_alias(self, *args, **kwargs):
        return self.base_function()

    def show_admin_status(self, *args, **kwargs):
        return self.base_function()

    def show_oper_status(self, *args, **kwargs):
        return self.base_function()

    def show_mtu(self, *args, **kwargs):
        return self.base_function()

    def show_mac_address(self, *args, **kwargs):
        return self.base_function()

    def show_high_speed(self, *args, **kwargs):
        return self.base_function()

    def show_in_octets(self, *args, **kwargs):
        return self.base_function()

    def show_in_unicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_in_discard_packets(self, *args, **kwargs):
        return self.base_function()

    def show_in_error_packets(self, *args, **kwargs):
        return self.base_function()

    def show_out_octets(self, *args, **kwargs):
        return self.base_function()

    def show_out_unicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_out_discard_packets(self, *args, **kwargs):
        return self.base_function()

    def show_out_error_packets(self, *args, **kwargs):
        return self.base_function()

    def show_in_multicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_in_broadcast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_out_multicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_out_broadcast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_in_octets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_in_unicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_in_multicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_in_broadcast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_out_octets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_out_unicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_out_multicast_packets(self, *args, **kwargs):
        return self.base_function()

    def show_64_bit_out_broadcast_packets(self, *args, **kwargs):
        return self.base_function()

    def set_rate_egress_mbps(self, *args, **kwargs):
        return self.base_function()

    def set_rate_egress_gbps(self, *args, **kwargs):
        return self.base_function()

    def set_rate_egress_kbps(self, *args, **kwargs):
        return self.base_function()

    def set_rate_egress_no_limit(self, *args, **kwargs):
        return self.base_function()

    def set_rate_flood_bcast(self, *args, **kwargs):
        return self.base_function()

    def set_rate_flood_mcast(self, *args, **kwargs):
        return self.base_function()

    def set_rate_flood_unknown(self, *args, **kwargs):
        return self.base_function()

    def set_restart(self, *args, **kwargs):
        return self.base_function()

    def show_rate_limit(self, *args, **kwargs):
        return self.base_function()

    def show_advertised(self, *args, **kwargs):
        return self.base_function()

    def enable_flex_uni(self, *args, **kwargs):
        return self.base_function()

    def disable_flex_uni(self, *args, **kwargs):
        return self.base_function()

    def set_alias(self, *args, **kwargs):
        return self.base_function()

    def show_flex_uni_status(self, *args, **kwargs):
        return self.base_function()
