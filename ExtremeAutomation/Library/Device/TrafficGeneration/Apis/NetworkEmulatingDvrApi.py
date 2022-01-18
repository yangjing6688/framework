from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Logger.Logger import Logger
import abc


class NetworkEmulatingDvrApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingDvrApi, self).__init__(device)

    @abc.abstractmethod
    def get_all_dvr_enties(self, bridge_name):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def add_dvr_gateway(self, bridge_name, l3_isid, l2_isid, cmac, mask_length, gateway, vlan_ip_interface):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def delete_dvr_gateway(self, bridge_name, l3_isid, l2_isid, gateway):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def verify_dvr_gateway(self, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length, gateway, options=None):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def add_dvr_route(self, bridge_name, l3_isid, l2_isid, cmac, mask_length, network_address, next_hop, domain_id):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def delete_dvr_route(self, bridge_name, l3_isid, l2_isid, cmac, mask_length, network_address):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def verify_dvr_route(self, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length, network_address, domain_id,
                         ctrl=1, cost=1, options=None):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def add_dvr_multicast(self, bridge_name, l3_isid, l2_isid, multicast_config, igmp_version):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def delete_dvr_multicast(self, bridge_name, l3_isid, l2_isid):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def verify_dvr_multicast(self, bridge_name, l3_isid, l2_isid, multicast_config, igmp_version=2,
                             igmp_query_interval=0, igmp_query_max_response=0, igmp_robust_value=0,
                             igmp_member_query_interval=0, igmp_ext_compatibility_mode_enable=16777215):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def create_dvr_gw_endpoint(self, bridge_name, l3_sid, starting_ip, mac_address, gateway):
        return self.log_unimplemented_method()

    @abc.abstractmethod
    def verify_dvr_member(self, bridge_name, bmac, domain_id, role, domain_isid, code):
        return self.log_unimplemented_method()


class NetworkEmulatingDvrConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    DVR_API = "DVR_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class DvrHost(object):
    def __init__(self):
        self.host = None
        self.dvr_gateways = []
        self.dvr_multicast_tlv = []
        self.dvr_routes = []
        self.dvr_member = []
        self.logger = Logger()

    def process_jets_info(self, _str):
        index = _str.index('[')
        self.host = _str[:index]
        _str = _str[index:]
        _str = _str.replace("]", "").replace("[", "")._strip()
        members = _str.split(",")
        for m in members:
            m = m.strip()
            if m.startswith("DvrLearnedIpv4GatewayTlv"):
                d = DvrGateway()
                d.process_jets(m)
                self.dvr_gateways.append(d)
            elif m.startswith("DvrLearnedMulticastConfigTlv"):
                d = DvrMulticastTlv()
                d.process_jets(m)
                self.dvr_multicast_tlv.append(d)
                pass
            elif m.startswith("DvrLearnedIpv4RouteTlv"):
                d = DvrRoute()
                d.process_jets(m)
                self.dvr_routes.append(d)
                pass
            elif m.startswith("DvrLearnedMemberTlv"):
                d = DvrMember()
                d.process_jets(m)
                self.dvr_member.append(d)
                pass
            else:
                self.logger.log_info("not accounted for " + m)

    def __str__(self):
        rt_str = self.host
        if len(self.dvr_gateways) > 0:
            rt_str += "\n\tDVR Gateways"
            index = 0
            for m in self.dvr_gateways:
                index += 1
                rt_str += "\n\t\t" + str(index) + ") " + str(m)
        if len(self.dvr_multicast_tlv) > 0:
            rt_str += "\n\tDVR Multicast"
            index = 0
            for m in self.dvr_multicast_tlv:
                index += 1
                rt_str += "\n\t\t" + str(index) + ") " + str(m)
        if len(self.dvr_routes) > 0:
            rt_str += "\n\tDVR Routes"
            index = 0
            for m in self.dvr_routes:
                index += 1
                rt_str += "\n\t\t" + str(index) + ") " + str(m)
        if len(self.dvr_member) > 0:
            rt_str += "\n\tDVR Members"
            index = 0
            for m in self.dvr_member:
                index += 1
                rt_str += "\n\t\t" + str(index) + ") " + str(m)
        return rt_str


class DvrGateway(object):
    def __init__(self):
        self.l3_isid = None
        self.l2_isid = None
        self.gateway_address = None
        self.mask_length = None
        self.bmac = None
        self.vrf = None
        self.cmac = None

    def process_jets(self, _str):
        parts = _str.split(":")
        self.l3_isid = parts[1]
        self.l2_isid = parts[2]
        self.gateway_address = parts[3]
        self.mask_length = parts[4]
        self.bmac = ":".join(parts[5:11])
        # self.vrf = parts[12]
        self.cmac = ":".join(parts[12:18])

    def __str__(self):

        return str(self.l3_isid) + \
            str(self.l2_isid) + \
            str(self.gateway_address) + \
            str(self.mask_length) +  \
            str(self.bmac) + str(self.vrf) + str(self.cmac)


class DvrMulticastTlv(object):
    def __init__(self):
        self.l3_isid = None
        self.l2_isid = None
        self.gateway_address = None
        self.mask_length = None
        self.bmac = None
        self.vrf = None
        self.cmac = None

    def process_jets(self, _str):
        # these need to be parsed correctly. this i just the DvrGateway parsing.
        parts = _str.split(":")
        self.l3_isid = parts[1]
        self.l2_isid = parts[2]
        self.gateway_address = parts[3]
        self.mask_length = parts[4]
        self.bmac = ":".join(parts[5:11])
        # self.vrf = parts[12]
        self.cmac = ":".join(parts[12:18])

    def __str__(self):
        return str(self.l3_isid) + \
            str(self.l2_isid) + \
            str(self.gateway_address) + \
            str(self.mask_length) +  \
            str(self.bmac) + str(self.vrf) + str(self.cmac)


class DvrRoute(object):
    def __init__(self):
        self.l3_isid = None
        self.l2_isid = None
        self.gateway_address = None
        self.mask_length = None
        self.bmac = None
        self.vrf = None
        self.cmac = None

    def process_jets(self, _str):
        # these need to be parsed correctly. this i just the DvrGateway parsing.
        parts = _str.split(":")
        self.l3_isid = parts[1]
        self.l2_isid = parts[2]
        self.gateway_address = parts[3]
        self.mask_length = parts[4]
        self.bmac = ":".join(parts[5:11])
        # self.vrf = parts[12]
        self.cmac = ":".join(parts[12:18])

    def __str__(self):

        return str(self.l3_isid) + \
            str(self.l2_isid) + \
            str(self.gateway_address) + \
            str(self.mask_length) +  \
            str(self.bmac) + str(self.vrf) + str(self.cmac)


class DvrMember(object):
    def __init__(self):
        self.l3_isid = None
        self.l2_isid = None
        self.gateway_address = None
        self.mask_length = None
        self.bmac = None
        self.vrf = None
        self.cmac = None

    def process_jets(self, _str):
        # these need to be parsed correctly. this i just the DvrGateway parsing.
        parts = _str.split(":")
        self.l3_isid = parts[1]
        self.l2_isid = parts[2]
        self.gateway_address = parts[3]
        self.mask_length = parts[4]
        self.bmac = ":".join(parts[5:11])
        # self.vrf = parts[12]
        self.cmac = ":".join(parts[12:18])

    def __str__(self):

        return str(self.l3_isid) + \
            str(self.l2_isid) + \
            str(self.gateway_address) + \
            str(self.mask_length) +  \
            str(self.bmac) + str(self.vrf) + str(self.cmac)
