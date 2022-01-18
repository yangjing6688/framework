import abc
import time
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Time import current_milli_time
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class NetworkEmulatingDhcpApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingDhcpApi, self).__init__(device)

    @abc.abstractmethod
    def create_dhcp_client(self, port_string, mac_address, network_mask, vlan=-1, count=1, step=1):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def remove_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def start_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def get_dhcp_client_address(self, port_string, mac_address):
        return self.log_unimplemented_method()

    def wait_for_dhcp_client_address(self, port_string, mac_address, max_wait_ms=60000, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -
        [max_wait_ms] -
        get_dhcp_client_address
        """
        start_time = current_milli_time()
        address = "0.0.0.0"
        while address == "0.0.0.0" and (current_milli_time() - start_time) < max_wait_ms:
            try:
                address = self.get_dhcp_client_address(port_string, mac_address)
                if address == "0.0.0.0":
                    time.sleep(1)
            except Exception as e:
                self.logger.log_error(e)
                return address
        return address

    @abc.abstractmethod
    def ping_dhcp_client(self, port_string, mac_address, network_mask, destination_ip):
        return self.log_unimplemented_method()


class NetworkEmulatingDhcpConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    DHCP_API = "DHCP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
