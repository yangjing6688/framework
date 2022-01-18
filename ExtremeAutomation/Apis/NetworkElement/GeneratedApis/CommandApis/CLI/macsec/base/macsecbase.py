"""
Base class for all macsec commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MacsecBase(CliBaseApi):
    def __init__(self, device):
        super(MacsecBase, self).__init__()
        self.device = device

    def enable_ca_port(self, *args, **kwargs):
        return self.base_function()

    def disable_ca_port(self, *args, **kwargs):
        return self.base_function()

    def create_ca(self, *args, **kwargs):
        return self.base_function()

    def create_ca_encrypted(self, *args, **kwargs):
        return self.base_function()

    def set_cipher_suite_128(self, *args, **kwargs):
        return self.base_function()

    def set_cipher_suite_256(self, *args, **kwargs):
        return self.base_function()

    def set_confidentiality_offset_0(self, *args, **kwargs):
        return self.base_function()

    def set_confidentiality_offset_30(self, *args, **kwargs):
        return self.base_function()

    def set_confidentiality_offset_50(self, *args, **kwargs):
        return self.base_function()

    def set_hw_mode_half_duplex_mode(self, *args, **kwargs):
        return self.base_function()

    def set_hw_mode_macsec_mode(self, *args, **kwargs):
        return self.base_function()

    def set_include_sci_enable(self, *args, **kwargs):
        return self.base_function()

    def set_include_sci_disable(self, *args, **kwargs):
        return self.base_function()

    def set_initialize_ports(self, *args, **kwargs):
        return self.base_function()

    def set_mka_actor_priority(self, *args, **kwargs):
        return self.base_function()

    def set_replay_protect(self, *args, **kwargs):
        return self.base_function()

    def set_replay_protect_disable(self, *args, **kwargs):
        return self.base_function()

    def clear_counters_all(self, *args, **kwargs):
        return self.base_function()

    def clear_counters_on_port(self, *args, **kwargs):
        return self.base_function()

    def delete_ca(self, *args, **kwargs):
        return self.base_function()

    def show(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()

    def show_port_configuration(self, *args, **kwargs):
        return self.base_function()

    def show_port_detail(self, *args, **kwargs):
        return self.base_function()

    def show_port_counters(self, *args, **kwargs):
        return self.base_function()

    def show_port_all(self, *args, **kwargs):
        return self.base_function()

    def show_port_all_config(self, *args, **kwargs):
        return self.base_function()

    def show_port_all_detail(self, *args, **kwargs):
        return self.base_function()

    def show_connectivity_association(self, *args, **kwargs):
        return self.base_function()

    def show_connectivity_association_all(self, *args, **kwargs):
        return self.base_function()
