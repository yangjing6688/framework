"""
All autopeering supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.autopeering.base.autopeeringbase import \
    AutopeeringBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.autopeering.EXOS.base.baseversion.baseunit.\
    autopeeringData import AutopeeringData


class Autopeering(DeviceApi, AutopeeringBase):
    def __init__(self, device):
        super(Autopeering, self).__init__(device)
        self.data_file = AutopeeringData()

    def set_anycast_mac(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "patch"
        data = self.data_file.set_anycast_mac_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_anycast_mac_and_id(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "patch"
        data = self.data_file.set_anycast_mac_and_id_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_anycast_mac_and_route_target(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "patch"
        data = self.data_file.set_anycast_mac_and_route_target_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_anycast_mac(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "patch"
        data = self.data_file.clear_anycast_mac_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_anycast_mac_and_id(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "patch"
        data = self.data_file.clear_anycast_mac_and_id_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_anycast_mac_and_route_target(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "patch"
        data = self.data_file.clear_anycast_mac_and_route_target_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_host_address_host_vrf_static_route_network_static_route_next_hop(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts"
        request_type = "patch"
        data = self.data_file.set_host_address_host_vrf_static_route_network_static_route_next_hop_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_all_hosts(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts"
        request_type = "put"
        data = self.data_file.clear_all_hosts_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_host(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts/host={0},{1}".format(arg_dict['host_address'],
                                                                                               arg_dict['host_vrf'])
        request_type = "delete"
        data = self.data_file.clear_host_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_static_route_from_host(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts/host={0},{1}/static-routes/static-route={2}{3}".format(arg_dict['host_address'],
                                                                                                                                 arg_dict['host_vrf'],
                                                                                                                                 arg_dict['static_route_ip'],
                                                                                                                                 arg_dict['mask_value'])
        request_type = "delete"
        data = self.data_file.clear_static_route_from_host_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/services"
        request_type = "patch"
        data = self.data_file.set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_host_static_route(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts/host={0},{1}".format(arg_dict['host_address'],
                                                                                               arg_dict['host_vrf'])
        request_type = "patch"
        data = self.data_file.set_host_static_route_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_all_services(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/services"
        request_type = "put"
        data = self.data_file.clear_all_services_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_service(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/services/service={0}".format(arg_dict['nsi'])
        request_type = "delete"
        data = self.data_file.clear_service_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_global(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering"
        request_type = "get"
        data = self.data_file.show_global_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_hosts(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts"
        request_type = "get"
        data = self.data_file.show_hosts_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_host_static_routes(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/hosts/host={0},{1}/static-routes/".format(arg_dict['host_address'],
                                                                                                              arg_dict['host_vrf'])
        request_type = "get"
        data = self.data_file.show_host_static_routes_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_service(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/services/service={0}".format(arg_dict['nsi'])
        request_type = "get"
        data = self.data_file.show_service_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_all_services(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/extreme-auto-peering:auto-peering/services/"
        request_type = "get"
        data = self.data_file.show_all_services_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
