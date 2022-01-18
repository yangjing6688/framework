from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingEndstationApi(TrafficGenerationApi):
    """
    init function
    meshost create local_host2 -type LOCAL_TLS -macAddr 00:00:00:ff:ff:02 -ipAddr 10.10.10.12 -vlanId 100 -intf 4
        -isid 999 -mask 255.0.0.0
    """

    def __init__(self, device):
        super(NetworkEmulatingEndstationApi, self).__init__(device)

    # eth2, 'edgeA', "00:00:00:0c:0a:01", 4051, 4502, "c02000000000", "00:00:00:0e:0a:0f", 10,

    @abc.abstractmethod
    # meshost create local_host2 -type LOCAL_TLS -macAddr 00:00:00:ff:ff:02 -ipAddr 10.10.10.12 -vlanId 100 -intf 4
    #   -isid 999 -mask 255.0.0.0
    def create_isis_interface(self, port_string, endstation_name, mac_addr, ip_addr, vlan_id, is_id, mask,
                              options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_isis_endpoint(self, bridge_name, basename, isid_id, uni_bmac, cvlan, cvlan_priority, endpoint_mac,
                             endpoint_ip, endpoint_mask, num_eps, bvlan, plsb_instance, l3isid, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_routed_l2vsn_ipv4_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_mask,
                                          endpoint_gateway, endpoint_mac, num_eps=1, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_l2vsn_ipv4_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_mask, endpoint_mac,
                                   num_eps=1, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_routed_l2vsn_ipv6_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_prefix_length,
                                          endpoint_mac, num_eps=1, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_l2vsn_ipv6_endpoint(self, bridge_name, basename, isid_id, endpoint_ip, endpoint_prefix_length,
                                   endpoint_mac, num_eps=1, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_l3vsn_ipv4_endpoint(self, bridge_name, basename, isid_id, starting_ip, endpoint_ip, endpoint_mask,
                                   num_eps=1, num_routes=1, cost=1, step=1, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def create_l3vsn_ipv6_endpoint(self, bridge_name, basename, isid_id, starting_ip, endpoint_ip, prefix_length,
                                   num_eps=1, num_routes=1, cost=1, step=1, options=None):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingEndstationConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    END_STATION_API = "END_STATION_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
