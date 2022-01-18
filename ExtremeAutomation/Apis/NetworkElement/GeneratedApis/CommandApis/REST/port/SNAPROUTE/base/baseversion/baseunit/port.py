"""
All port supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.port.base.portbase import PortBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.port.SNAPROUTE.base.baseversion.baseunit.\
    portData import PortData


class Port(DeviceApi, PortBase):
    def __init__(self, device):
        super(Port, self).__init__(device)
        self.data_file = PortData()

    def enable_state(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "patch"
        data = self.data_file.enable_state_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_state(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "patch"
        data = self.data_file.disable_state_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_admin_status(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_admin_status_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_oper_status(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_oper_status_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_info_detail(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_info_detail_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_mtu(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_mtu_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_mac_address(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_mac_address_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_high_speed(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_high_speed_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_in_octets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_in_octets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_in_discard_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_in_discard_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_in_error_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_in_error_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_in_unknown_protocol_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_in_unknown_protocol_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_out_octets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_out_octets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_out_unicast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_out_unicast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_out_discard_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_out_discard_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_out_error_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_out_error_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_in_broadcast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_in_broadcast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_out_multicast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_out_multicast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_out_broadcast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_out_broadcast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_in_octets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_in_octets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_in_unicast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_in_unicast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_in_multicast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_in_multicast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_in_broadcast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_in_broadcast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_out_octets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_out_octets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_out_unicast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_out_unicast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_out_multicast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_out_multicast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_64_bit_out_broadcast_packets(self, arg_dict, **kwargs):
        uri = "public/v1/config/Port"
        request_type = "get"
        data = self.data_file.show_64_bit_out_broadcast_packets_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
