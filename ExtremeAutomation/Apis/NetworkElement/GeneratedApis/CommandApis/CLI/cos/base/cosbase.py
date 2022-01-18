"""
Base class for all cos commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class CosBase(CliBaseApi):
    def __init__(self, device):
        super(CosBase, self).__init__()
        self.device = device

    def create_qos_profile(self, *args, **kwargs):
        return self.base_function()

    def delete_qos_profile(self, *args, **kwargs):
        return self.base_function()

    def create_port_group(self, *args, **kwargs):
        return self.base_function()

    def delete_port_group(self, *args, **kwargs):
        return self.base_function()

    def set_port_group_port(self, *args, **kwargs):
        return self.base_function()

    def set_txq_settings(self, *args, **kwargs):
        return self.base_function()

    def set_txq_settings_cos_under_seven(self, *args, **kwargs):
        return self.base_function()

    def set_irl_settings(self, *args, **kwargs):
        return self.base_function()

    def set_irl_settings_cos_under_seven(self, *args, **kwargs):
        return self.base_function()

    def set_port_resource_irl(self, *args, **kwargs):
        return self.base_function()

    def set_orl_settings(self, *args, **kwargs):
        return self.base_function()

    def set_orl_settings_cos_under_seven(self, *args, **kwargs):
        return self.base_function()

    def set_dot1p_type(self, *args, **kwargs):
        return self.base_function()

    def set_dot1p_type_only(self, *args, **kwargs):
        return self.base_function()

    def set_dot1p_port_type(self, *args, **kwargs):
        return self.base_function()

    def set_qos_scheduler(self, *args, **kwargs):
        return self.base_function()

    def set_txq_weights(self, *args, **kwargs):
        return self.base_function()

    def set_tos_settings(self, *args, **kwargs):
        return self.base_function()

    def set_tos_settings_cos_under_seven(self, *args, **kwargs):
        return self.base_function()

    def set_priority_settings(self, *args, **kwargs):
        return self.base_function()

    def set_priority_settings_cos_under_seven(self, *args, **kwargs):
        return self.base_function()

    def set_diff_serve_replacement(self, *args, **kwargs):
        return self.base_function()

    def clear_index(self, *args, **kwargs):
        return self.base_function()

    def clear_irl(self, *args, **kwargs):
        return self.base_function()

    def set_txq_shaping(self, *args, **kwargs):
        return self.base_function()

    def clear_txq_shaping(self, *args, **kwargs):
        return self.base_function()

    def set_port_priority(self, *args, **kwargs):
        return self.base_function()

    def set_port_qos_profile(self, *args, **kwargs):
        return self.base_function()

    def show_qos_profile(self, *args, **kwargs):
        return self.base_function()

    def show_port_qos_profile(self, *args, **kwargs):
        return self.base_function()

    def show_txq_port_group(self, *args, **kwargs):
        return self.base_function()

    def show_irl_port_group(self, *args, **kwargs):
        return self.base_function()

    def show_txq_port_group_specific(self, *args, **kwargs):
        return self.base_function()

    def show_irl_port_group_specific(self, *args, **kwargs):
        return self.base_function()

    def show_txq_wfq_weights(self, *args, **kwargs):
        return self.base_function()

    def show_irl_wfq_weights(self, *args, **kwargs):
        return self.base_function()

    def show_txq_port_resource_specific(self, *args, **kwargs):
        return self.base_function()

    def show_irl_port_resource_specific(self, *args, **kwargs):
        return self.base_function()

    def show_qos_scheduler(self, *args, **kwargs):
        return self.base_function()

    def show_settings(self, *args, **kwargs):
        return self.base_function()

    def show_port_priority(self, *args, **kwargs):
        return self.base_function()

    def show_port_info_detail(self, *args, **kwargs):
        return self.base_function()

    def enable_state(self, *args, **kwargs):
        return self.base_function()

    def disable_state(self, *args, **kwargs):
        return self.base_function()

    def set_txq_reference(self, *args, **kwargs):
        return self.base_function()

    def clear_txq_settings(self, *args, **kwargs):
        return self.base_function()

    def set_irl_reference(self, *args, **kwargs):
        return self.base_function()

    def clear_irl_settings(self, *args, **kwargs):
        return self.base_function()

    def set_orl_reference(self, *args, **kwargs):
        return self.base_function()

    def set_port_resource_orl(self, *args, **kwargs):
        return self.base_function()

    def clear_orl_settings(self, *args, **kwargs):
        return self.base_function()

    def clear_tos_settings(self, *args, **kwargs):
        return self.base_function()

    def clear_flood_ctrl_settings(self, *args, **kwargs):
        return self.base_function()

    def clear_all_config(self, *args, **kwargs):
        return self.base_function()

    def show_txq_port_resource(self, *args, **kwargs):
        return self.base_function()

    def show_irl_port_resource(self, *args, **kwargs):
        return self.base_function()

    def show_orl_port_resource(self, *args, **kwargs):
        return self.base_function()

    def show_txq_reference(self, *args, **kwargs):
        return self.base_function()

    def show_irl_reference(self, *args, **kwargs):
        return self.base_function()

    def show_orl_reference(self, *args, **kwargs):
        return self.base_function()

    def show_state(self, *args, **kwargs):
        return self.base_function()
