"""
Base class for all port SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class PortBase(SnmpBaseApi):
    def __init__(self, device):
        super(PortBase, self).__init__()
        self.device = device

    def enable_state(self, *args, **kwargs):
        return self.base_function()

    def disable_state(self, *args, **kwargs):
        return self.base_function()

    def set_alias(self, *args, **kwargs):
        return self.base_function()

    def show_names(self, *args, **kwargs):
        return self.base_function()

    def show_alias(self, *args, **kwargs):
        return self.base_function()

    def show_admin_status(self, *args, **kwargs):
        return self.base_function()

    def show_oper_status(self, *args, **kwargs):
        return self.base_function()

    def show_info_detail(self, *args, **kwargs):
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

    def show_in_unknown_protocol_packets(self, *args, **kwargs):
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

    def show_dot1d_ifindex(self, *args, **kwargs):
        return self.base_function()

    def enable_flex_uni(self, *args, **kwargs):
        return self.base_function()

    def disable_flex_uni(self, *args, **kwargs):
        return self.base_function()

    def show_flex_uni_status(self, *args, **kwargs):
        return self.base_function()
