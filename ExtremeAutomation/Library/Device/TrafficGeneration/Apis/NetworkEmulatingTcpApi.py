# from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingTcpApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingTcpApi, self).__init__(device)

    @abc.abstractmethod
    def create_tcp_stack(self, port_string, source_ip, netmask=None, gateway_address=None, mac_address=None,
                         vlan_id=None):
        return self.logger.log_unimplemented_method()
    # tcpip config -device 1 -ipAddr 31.1.2.3 -netmask 255.255.255.0 -rtrStackIp 31.1.2.1 -macAddress 00:33:44:55:66:77

    def delete_tcp_stack(self, port_string, source_ip):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingTcpConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TCP_API = "TCP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
