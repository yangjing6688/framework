"""
Base class for all poe SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class PoeBase(SnmpBaseApi):
    def __init__(self, device):
        super(PoeBase, self).__init__()
        self.device = device

    def enable_port(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def set_power_usage_threshold(self, *args, **kwargs):
        return self.base_function()

    def set_port_power_limit(self, *args, **kwargs):
        return self.base_function()

    def set_port_power_priority(self, *args, **kwargs):
        return self.base_function()

    def set_port_detect_type(self, *args, **kwargs):
        return self.base_function()

    def show_power_usage_threshold(self, *args, **kwargs):
        return self.base_function()

    def show_port_status(self, *args, **kwargs):
        return self.base_function()

    def show_port_measurements(self, *args, **kwargs):
        return self.base_function()

    def show_port_power_limit(self, *args, **kwargs):
        return self.base_function()

    def show_port_power_priority(self, *args, **kwargs):
        return self.base_function()

    def show_port_detection_status(self, *args, **kwargs):
        return self.base_function()

    def show_port_power_classification(self, *args, **kwargs):
        return self.base_function()

    def show_global_status(self, *args, **kwargs):
        return self.base_function()

    def show_port_power_pairs(self, *args, **kwargs):
        return self.base_function()

    def show_port_detect_type(self, *args, **kwargs):
        return self.base_function()
