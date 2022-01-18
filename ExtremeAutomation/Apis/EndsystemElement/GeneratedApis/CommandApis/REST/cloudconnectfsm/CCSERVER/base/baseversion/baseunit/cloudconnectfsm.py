"""
All cloudconnectfsm supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.REST.cloudconnectfsm.base.cloudconnectfsmbase \
    import CloudconnectfsmBase
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.REST.cloudconnectfsm.CCSERVER.base.baseversion.\
    baseunit.cloudconnectfsmData import CloudconnectfsmData


class Cloudconnectfsm(DeviceApi, CloudconnectfsmBase):
    def __init__(self, device):
        super(Cloudconnectfsm, self).__init__(device)
        self.data_file = CloudconnectfsmData()

    def add_connect_entry_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/connect"
        request_type = "post"
        data = self.data_file.add_connect_entry_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def remove_connect_entry_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/connect"
        request_type = "post"
        data = self.data_file.remove_connect_entry_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def add_upgrade_entry_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/upgrade"
        request_type = "post"
        data = self.data_file.add_upgrade_entry_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def remove_upgrade_entry_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/upgrade"
        request_type = "post"
        data = self.data_file.remove_upgrade_entry_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def add_config_entry_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/config"
        request_type = "post"
        data = self.data_file.add_config_entry_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def remove_config_entry_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/config"
        request_type = "post"
        data = self.data_file.remove_config_entry_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def add_stats_reply_for_serial(self, arg_dict, **kwargs):
        uri = "robot_config/stats"
        request_type = "post"
        data = self.data_file.add_stats_reply_for_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def allow_connect_state_timeout(self, arg_dict, **kwargs):
        uri = "robot_config/allow_timeout"
        request_type = "post"
        data = self.data_file.allow_connect_state_timeout_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def allow_upgrade_state_timeout(self, arg_dict, **kwargs):
        uri = "robot_config/allow_timeout"
        request_type = "post"
        data = self.data_file.allow_upgrade_state_timeout_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def allow_config_state_timeout(self, arg_dict, **kwargs):
        uri = "robot_config/allow_timeout"
        request_type = "post"
        data = self.data_file.allow_config_state_timeout_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_fsm_states_by_serial(self, arg_dict, **kwargs):
        uri = "robot_config/clear_fsm_states"
        request_type = "post"
        data = self.data_file.clear_fsm_states_by_serial_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def check_device_states(self, arg_dict, **kwargs):
        uri = "robot_config/device_states"
        request_type = "get"
        data = self.data_file.check_device_states_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_mgmt_ip(self, arg_dict, **kwargs):
        uri = "robot_config/get_mgmt_ip"
        request_type = "get"
        data = self.data_file.show_mgmt_ip_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_device_version(self, arg_dict, **kwargs):
        uri = "robot_config/get_device_assets"
        request_type = "get"
        data = self.data_file.show_device_version_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
