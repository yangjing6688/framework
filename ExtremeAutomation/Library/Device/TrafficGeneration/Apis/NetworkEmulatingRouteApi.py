from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingRouteApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingRouteApi, self).__init__(device)
        self.route_ipv4_shortcuts = {}
        self.route_ipv6_shortcuts = {}

    @abc.abstractmethod
    def advetise_ipv4_routes(self, port_string, bridge_name, shortcut_ip, shortcut_netmask, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def enable_ipv4_shortcuts(self, port_string, bridge_name, shortcut_ip=None, shortcut_netmask='255.255.255.255'):
        return self.logger.log_unimplemented_method()

    def is_ipv4_shortcuts_enabled(self, port_string, bridge_name):
        if port_string in self.route_ipv4_shortcuts:
            if bridge_name in self.route_ipv4_shortcuts[port_string]:
                return True
        return False

    def set_ipv4_shortcuts_enabled(self, port_string, bridge_name):
        if port_string not in self.route_ipv4_shortcuts:
            self.route_ipv4_shortcuts[port_string] = []
        self.route_ipv4_shortcuts[port_string].append(bridge_name)

    @abc.abstractmethod
    def advetise_ipv6_routes(self, port_string, bridge_name, shortcut_ip, options=None):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def enable_ipv6_shortcuts(self, port_string, bridge_name, shortcut_ip=None):
        return self.logger.log_unimplemented_method()

    def is_ipv6_shortcuts_enabled(self, port_string, bridge_name):
        if port_string in self.route_ipv6_shortcuts:
            if bridge_name in self.route_ipv6_shortcuts[port_string]:
                return True
        return False

    def set_ipv6_shortcuts_enabled(self, port_string, bridge_name):
        if port_string not in self.route_ipv6_shortcuts:
            self.route_ipv6_shortcuts[port_string] = []
        self.route_ipv6_shortcuts[port_string].append(bridge_name)

    @abc.abstractmethod
    def get_all_routes_from_interface(self, port_string):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def get_routes(self, port_string, ip_address):
        return self.log_unimplemented_method()


class NetworkEmulatingRouteConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    ROUTE_API = "ROUTE_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
