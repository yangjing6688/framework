"""
Base class for all fdb commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class FdbBase(CliBaseApi):
    def __init__(self, device):
        super(FdbBase, self).__init__()
        self.device = device

    def set_agetime(self, *args, **kwargs):
        return self.base_function()

    def set_agetime_min(self, *args, **kwargs):
        return self.base_function()

    def clear_agetime(self, *args, **kwargs):
        return self.base_function()

    def enable_unicast_as_multicast(self, *args, **kwargs):
        return self.base_function()

    def disable_unicast_as_multicast(self, *args, **kwargs):
        return self.base_function()

    def clear_all(self, *args, **kwargs):
        return self.base_function()

    def clear_all_vlan(self, *args, **kwargs):
        return self.base_function()

    def clear_all_port(self, *args, **kwargs):
        return self.base_function()

    def create_entry(self, *args, **kwargs):
        return self.base_function()

    def create_multicast_entry(self, *args, **kwargs):
        return self.base_function()

    def delete_entry(self, *args, **kwargs):
        return self.base_function()

    def show_agetime(self, *args, **kwargs):
        return self.base_function()

    def show_all_entries(self, *args, **kwargs):
        return self.base_function()

    def show_entry(self, *args, **kwargs):
        return self.base_function()

    def create_blackhole_entry(self, *args, **kwargs):
        return self.base_function()

    def enable_learning_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_learning_port(self, *args, **kwargs):
        return self.base_function()

    def disable_learning_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_learning_port(self, *args, **kwargs):
        return self.base_function()

    def show_stats(self, *args, **kwargs):
        return self.base_function()

    def show_stats_port(self, *args, **kwargs):
        return self.base_function()

    def show_stats_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_stats_vlan_name(self, *args, **kwargs):
        return self.base_function()

    def show_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_name(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()

    def clear_mac_port(self, *args, **kwargs):
        return self.base_function()

    def clear_mac_port_vlan(self, *args, **kwargs):
        return self.base_function()

    def clear_dynamic_entry(self, *args, **kwargs):
        return self.base_function()

    def show_entries_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_entries_port(self, *args, **kwargs):
        return self.base_function()

    def set_agetime_conversational(self, *args, **kwargs):
        return self.base_function()

    def clear_agetime_conversational(self, *args, **kwargs):
        return self.base_function()

    def set_fdb_learn_mode_conversational(self, *args, **kwargs):
        return self.base_function()

    def clear_fdb_learn_mode(self, *args, **kwargs):
        return self.base_function()

    def clear_all_linecard(self, *args, **kwargs):
        return self.base_function()

    def clear_all_linecard_rbid(self, *args, **kwargs):
        return self.base_function()

    def enable_learning(self, *args, **kwargs):
        return self.base_function()

    def disable_learning(self, *args, **kwargs):
        return self.base_function()
