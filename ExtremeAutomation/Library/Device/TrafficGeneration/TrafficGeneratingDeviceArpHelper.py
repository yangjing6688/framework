import abc
import time
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.Time import current_milli_time
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxRouteIxTclHalApi import IxRouteIxTclHalConstants


class TrafficGeneratingDeviceArpHelper(object, metaclass=abc.ABCMeta):
    def __init__(self, device):
        self.dev = device
        self.logger = Logger()

    @abc.abstractmethod
    def configure_arp(self, port_string, start_ip, start_mac, num_addresses, gateway_address,
                      mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                      arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                      netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        pass

    @abc.abstractmethod
    def ping(self, port_string, source_ip, destination_ip, timeout_secs=30, ping_count=3):
        pass

    @abc.abstractmethod
    def configure_neighbor_discovery(self, port_string, start_ipv6, start_mac, num_addresses, gateway_address,
                                     mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                                     arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                                     netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        pass

    def wait_for_ping(self, port_string, source_ip, destination_ip, max_wait_ms=60000):
        start_time = current_milli_time()
        res = False
        while not res and (current_milli_time() - start_time) < max_wait_ms:
            res = self.ping(port_string, source_ip, destination_ip, 3, ping_count=1)
            if not res:
                time.sleep(0.7)
        return res
