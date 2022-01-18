from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc


class NetworkEmulatingSpbmApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingSpbmApi, self).__init__(device)

    # eth2, 'edgeA', "00:00:00:0c:0a:01", 4051, 4502, "c02000000000", "00:00:00:0e:0a:0f", 10,

    @abc.abstractmethod
    def create_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                              pnode_id, spb_instance, cost, options=None):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def set_isis_globals(self, hello_interval=9, isi_multiplier=3, retrans_lsp_interval=5, options=None):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def set_bridge_enabled(self, enable=True):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def set_multicast_enabled(self, enable=True):
        return self.log_unimplemented_method()

    def create_and_go_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                                     pnode_id, spb_instance, cost, enable=True, options=None):
        """
        If you are adding more than one bridge, don't use this method. call create as many times as you need and then
        set the globals and enable. Results might not be right if you don't.
        :param port_string:
        :param bridge_name:
        :param mac_addr:
        :param vlan_id:
        :param svlan_id:
        :param area:
        :param sys_id:
        :param pnode_id:
        :param spb_instance:
        :param cost:
        :param enable:
        :param options:
        :return:
        """
        self.create_isis_interface(port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                                   pnode_id, spb_instance, cost, options)
        self.set_isis_globals()
        if enable:
            self.set_bridge_enabled()

    def create_and_go_isis_interface_dvr_leaf(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                                              pnode_id, spb_instance, cost, dvr_domain=-1, enable=True, options=None):
        if not options:
            options = {}
        options['dvrMode'] = "LEAF"
        if dvr_domain != -1:
            options['dvrDomain'] = str(dvr_domain)
        return self.create_and_go_isis_interface(port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                                                 pnode_id, spb_instance, cost, enable, options)

    def create_and_go_isis_interface_dvr_controller(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area,
                                                    sys_id, pnode_id, spb_instance, cost, dvr_domain=-1, enable=True,
                                                    options=None):
        if not options:
            options = {}
        options['dvrMode'] = "CONTROLLER"
        if dvr_domain != -1:
            options['dvrDomain'] = str(dvr_domain)
        return self.create_and_go_isis_interface(port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                                                 pnode_id, spb_instance, cost, enable, options)

    @abc.abstractmethod
    def create_isis_ipv4_route_stack(self, port_string, bridge_name, create_stack, starting_ip, netmask, gateway_ip,
                                     num_routes, cost, step, options=None):
        return self.log_unimplemented_method()


class NetworkEmulatingSpbmConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    SBP_API = "SBP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
