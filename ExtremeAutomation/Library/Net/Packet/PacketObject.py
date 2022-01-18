import copy
from collections import deque
from ExtremeAutomation.Library.Logger.Logger import Logger


class PacketObject(object):
    logger = Logger()

    def __init__(self):
        self.__packet_composite = dict()
        self.__packet_tags = deque()
        pass

    def clone(self, packet):
        self._PacketObject__packet_composite = copy.deepcopy(packet._PacketObject__packet_composite)

    # def set__packet_composite (self, _packet_composite):
    #     self.__packet_composite = _packet_composite
    #
    # def get__packet_composite (self):
    #     return self.__packet_composite
    #
    # def set__packet_tags (self, _packet_tags):
    #     self.__packet_tags = _packet_tags
    #
    # def get__packet_tags (self):
    #     return self.__packet_tags

    def set_packet_component(self, composite_name, component_name, comp):
        if composite_name not in self.__packet_composite.keys():
            self.__packet_composite[composite_name] = dict()
        self.__packet_composite[composite_name][component_name] = comp

    def get_packet_component(self, composite_name, component_name):
        if composite_name not in self.__packet_composite.keys():
            return "Header Not Set"
        if component_name not in self.__packet_composite[composite_name].keys():
            return "Field Not Set"
        return self.__packet_composite[composite_name][component_name]

    def remove_packet_composite(self, composite_name):
        if composite_name in self._PacketObject__packet_composite:
            del self._PacketObject__packet_composite[composite_name]

    def set_packet_composite(self, composite_name):
        if composite_name in self.__packet_composite.keys():
            return "already contains " + composite_name
            pass
        self.__packet_composite[composite_name] = dict()

    def get_packet_composite(self, composite_name):
        if composite_name not in self.__packet_composite.keys():
            return "Header Not Set"
        return self.__packet_composite[composite_name]

    def register_packet_tag(self, pkt_type):
        if pkt_type not in self.__packet_tags:
            self.__packet_tags.append(pkt_type)

    def get_packet_tags(self):
        return self.__packet_tags

    def remove_packet_tag(self, pkt_type):
        if pkt_type in self._PacketObject__packet_tags:
            del self._PacketObject__packet_tags[pkt_type]

    def get_all_packet_fields(self):
        return self.__packet_composite

    @staticmethod
    def log_debug(msg):
        PacketObject.logger.log_debug(msg)

    @staticmethod
    def log_info(msg):
        PacketObject.logger.log_info(msg)

    @staticmethod
    def log_error(msg):
        PacketObject.logger.log_error(msg)

    def __str__(self):
        return "Packet Headers: " + '\n\t'.join('{}{}'.format(key, val) for
                                                key, val in sorted(self.__packet_composite.items())) + \
               "\nPacket Tags:    " + str(self.__packet_tags)


class PacketConstants:
    def __init__(self):
        pass

    PRINT_FLAG_EVERYTHING = "everything"
    PRINT_FLAG_ERRORS = "errors only"
    PRINT_FLAG_NONE = "none"

    PACKET_HEADER_L1_ETHERNET = "PACKET_HEADER_L1_ETHERNET"
    PACKET_HEADER_L2_ETHERNET_II_TYPE = "PACKET_HEADER_L2_ETHERNET_II_TYPE"
    PACKET_HEADER_L2_ETHERNET_TAGGED = "PACKET_HEADER_L2_ETHERNET_TAGGED"
    PACKET_HEADER_L2_ETHERNET_VLAN_STACK = "PACKET_HEADER_L2_ETHERNET_VLAN_STACK"
    PACKET_HEADER_L3_ENCAPSULATED = "PACKET_HEADER_L3_ENCAPSULATED"
    PACKET_HEADER_L3_MPLSENCAPSULATED = "PACKET_HEADER_L3_MPLSENCAPSULATED"
    PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE = "PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE"
    PACKET_HEADER_L3_IPV4 = "PACKET_HEADER_L3_IPV4"
    PACKET_HEADER_L3_IPV6 = "PACKET_HEADER_L3_IPV6"
    PACKET_HEADER_L3_MPLS = "PACKET_HEADER_L3_MPLS"
    PACKET_HEADER_L3_ARP = "PACKET_HEADER_L3_ARP"
    PACKET_HEADER_L3_DBSYNCDVR = "PACKET_HEADER_L3_DBSYNCDVR"
    PACKET_HEADER_L3_ISIS = "PACKET_HEADER_L3_ISIS"
    PACKET_HEADER_L3_BPDU = "PACKET_HEADER_L3_BPDU"
    PACKET_HEADER_L3_MSTP = "PACKET_HEADER_L3_MSTP"
    PACKET_HEADER_L3_SPANNINGTREE = "PACKET_HEADER_L3_SPANNINGTREE"
    PACKET_HEADER_L4_TCP = "PACKET_HEADER_L4_TCP"
    PACKET_HEADER_L4_UDP = "PACKET_HEADER_L4_UDP"
    PACKET_HEADER_L4_OSPF = "PACKET_HEADER_L4_OSPF"
    PACKET_HEADER_L4_IGMP = "PACKET_HEADER_L4_IGMP"
    PACKET_HEADER_L4_ICMP = "PACKET_HEADER_L4_ICMP"
    PACKET_HEADER_L4_PIM = "PACKET_HEADER_L4_PIM"
    PACKET_HEADER_L3_VRRP = "PACKET_HEADER_L3_VRRP"

    PACKET_HEADER_L5_GRE = "PACKET_HEADER_L5_GRE"
    PACKET_HEADER_L3_ERSPANIII = "PACKET_HEADER_L3_ERSPANIII"
    PACKET_HEADER_L3_ERSPAN = "PACKET_HEADER_L3_ERSPAN"

    PACKET_HEADER_L2_SNAP = "PACKET_HEADER_L2_SNAP"

    PACKET_HEADER_L2_LLC = "PACKET_HEADER_L2_LLC"
    PACKET_HEADER_L3_IPX = "PACKET_HEADER_L3_IPX"

    PACKET_HEADER_L3_LLDP = "PACKET_HEADER_L3_LLDP"
    PACKET_HEADER_L3_RADIUS = "PACKET_HEADER_L3_RADIUS"
    PACKET_HEADER_L5_VXLAN = "PACKET_HEADER_L5_VXLAN"

    PACKET_HEADER_L4_ISIS_HELLOPDU = "PACKET_HEADER_L4_ISIS_HELLOPDU"
    PACKET_HEADER_L4_ISIS_LSP = "PACKET_HEADER_L4_ISIS_LSP"
    PACKET_HEADER_L4_ISIS_SNP = "PACKET_HEADER_L4_ISIS_SNP"
    PACKET_HEADER_L4_CSNPDBSYNCDVR = "PACKET_HEADER_L4_CSNPDBSYNCDVR"
    PACKET_HEADER_L4_DBPDBSYNCDVR = "PACKET_HEADER_L4_DBPDBSYNCDVR"

    PACKET_HEADER_L4_OSPF_HELLO = "PACKET_HEADER_L4_OSPF_HELLO"
    PACKET_HEADER_L4_OSPF_DBDESCRIPTION = "PACKET_HEADER_L4_OSPF_DBDESCRIPTION"
    PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST = "PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST"
    PACKET_HEADER_L4_OSPF_LINKSTATEUPDATE = "PACKET_HEADER_L4_OSPF_LINKSTATEUPDATE"
    PACKET_HEADER_L4_OSPF_LINKSTATEACKNOWLEDGE = "PACKET_HEADER_L4_OSPF_LINKSTATEACKNOWLEDGE"

    PACKET_HEADER_L5_BGP = "PACKET_HEADER_L5_BGP"
    PACKET_HEADER_L5_BGPOPENMESSAGE = "PACKET_HEADER_L5_BGPOPENMESSAGE"
    PACKET_HEADER_L3_BGPKEEPALIVE = "PACKET_HEADER_L3_BGPKEEPALIVE"

    PACKET_HEADER_L3_SYSLOG = "PACKET_HEADER_L3_SYSLOG"

    PACKET_HEADER_L5_RIP = "PACKET_HEADER_L5_RIP"
    PACKET_HEADER_L5_RIPNG = "PACKET_HEADER_L5_RIPNG"

    PACKET_HEADER_L5_DNS = "PACKET_HEADER_L3_DNS"

    PACKET_HEADER_L5_BOOTP = "PACKET_HEADER_L5_BOOTP"

    IPV4_ADDRESS = "IPV4_ADDRESS"
    IPV6_ADDRESS = "IPV6_ADDRESS"
    ENET_ADDRESS = "ENET_ADDRESS"
    INTEGER = "INTEGER"
    HEX_STRING = "HEX_STRING"
    ASCII_STRING = "ASCII_STRING"
    BOOLEAN = "BOOLEAN"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class PacketTagConstants:
    def __init__(self):
        pass

    TAG_TCP = "TCP"
    TAG_UDP = "UDP"
    TAG_VRRP = "VRRP"
    TAG_OSPF = "OSPF"
    TAG_RIP = "RIP"
    TAG_RIPNG = "TAG_RIPNG"
    TAG_IPV4 = "IPV4"
    TAG_IPV6 = "IPV6"
    TAG_MPLS = "MPLS"
    TAG_MLD = "MLD"
    TAG_MLD_V2 = "MLDV2"
    TAG_DVMRP = "DVMRP"
    TAG_BOOTP = "BOOTP"
    TAG_DHCP = "DHCP"
    TAG_PIM = "TAG_PIM"
    TAG_PIM_JOIN_PRUNE = "PIMJOINPRUNE"
    TAG_PIM_BOOTSTRAP = "PIMBOOTSTRAP"
    TAG_PROVIDERBACKBONEBRIDGE = "TAG_PROVIDERBACKBONEBRIDGE"
    TAG_PIM_ASSERT = "PIMASSERT"
    TAG_PIM_CANIDATE = "PIMCANIDATE"
    TAG_PIM_GRAFT_ACK_MESSAGE = "PIMGRAFTACKMESSAGE"
    TAG_PIM_GRAFT_MESSAGE = "PIMGRAFTMESSAGE"
    TAG_PIM_REGISTER_STOP_MESSAGE = "PIMREGISTERSTOP"
    TAG_PIM_REGISTER_MESSAGE = "PIMREGISTER"
    TAG_MPLSENCAPSULATED = "TAG_MPLSENCAPSULATED"
    TAG_PIM_HELLO = "PIMHELLO"
    TAG_PIM_V2 = "PIMV2"
    TAG_DNS = "DNS"
    TAG_IPX = "IPX"
    TAG_LLC = "LLC"
    TAG_QTAGGED = "TAGGED"
    TAG_VLAN_STACK = "VLANSTACK"
    TAG_VXLAN = "VXLAN"
    TAG_ARP = "ARP"
    TAG_DBSYNCDVR = "TAG_DBSYNCDVR"
    TAG_DBPDBSYNCDVR = "TAG_DBPDBSYNCDVR"
    TAG_CSNPDBSYNCDVR = "TAG_CSNPDBSYNCDVR"
    TAG_RARP = "RARP"
    TAG_ICMP = "ICMP"
    TAG_ICMP_V6 = "ICMPV6"
    TAG_IGMP = "IGMP"
    TAG_SAP = "SAP"
    TAG_SNAP = "SNAP"
    TAG_ENET2 = "Ethernet2"
    TAG_ETHER = "Ether"
    TAG_BPDU = "BPDU"
    TAG_RAW = "RAW"
    TAG_ETHER_ENCAP = "ENCAPSULATED"
    TAG_IPV4_IPV4_ENCAP = "IPV4IPV4ENCAPSULATED"
    TAG_IPV4_IPV6_ENCAP = "IPV4IPV6ENCAPSULATED"
    TAG_IPV6_ENCAP = "IPV6ENCAPSULATED"
    TAG_ISIS = "ISIS"
    TAG_LSP = "LSP"
    TAG_SNP = "SNP"
    TAG_HELLOPDU = "HELLOPDU"
    TAG_PAUSE_CONTROL = "PAUSECONTROL"
    TAG_NEIGHBOR_DISCOVERY = "NEIGHBORDISCOVERY"
    TAG_SPANNINGTREE = "TAG_SPANNINGTREE"
    TAG_MSTP = "TAG_MSTP"
    TAG_RSTP = "TAG_RSTP"
    TAG_MSTP = "TAG_BPDU"
    TAG_BOOTP = "TAG_BOOTP"
    TAG_LLDP = "TAG_LLDP"
    TAG_RADIUS = "TAG_RADIUS"
    TAG_GRE = "TAG_GRE"
    TAG_ENCAPSULATED = "TAG_ENCAPSULATED"
    TAG_ERSPAN = "TAG_ERSPAN"
    TAG_ERSPANIII = "TAG_ERSPANIII"
    TAG_OSPF_HELLO = "TAG_OSPF_HELLO"
    TAG_OSPF_DBDESCRIPTION = "TAG_OSPF_DBDESCRIPTION"
    TAG_OSPF_LINKSTATEREQUEST = "TAG_OSPF_LINKSTATEREQUEST"
    TAG_OSPF_LINKSTATEUPDATE = "TAG_OSPF_LINKSTATEUPDATE"
    TAG_OSPF_LINKSTATEACKNOWLEDGE = "TAG_OSPF_LINKSTATEACKNOWLEDGE"
    TAG_BGP = "TAG_BGP"
    TAG_BGPOPENMESSAGE = "TAG_BGPOPENMESSAGE"
    TAG_BGPKEEPALIVE = "TAG_BGPKEEPALIVE"
    TAG_SYSLOG = "TAG_SYSLOG"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class PacketHeaderDynamicFieldLogic(object):
    MATCH_ALL = "MATCH_ALL"
    MATCH_ONE = "MATCH_ONE"
    MATCH_ONLY = "MATCH_ONLY"
    MATCH_NONE = "MATCH_NONE"

    def __init__(self):
        self.pkt_type = self.MATCH_ALL
        self.order_matters = True
        pass

    def set_match_type(self, pkt_type):
        self.pkt_type = pkt_type

    def get_match_type(self):
        return self.pkt_type

    def is_order_matters(self):
        return self.order_matters

    def set_order_matters(self, val):
        self.order_matters = val

    def compare_packet_fields(self, expected, actual, print_results=False, print_failures=False):
        num_dynamic_entries_expected = self.get_compare_number(expected)
        num_dynamic_entries_actual = self.get_compare_number(actual)
        index_dynamic = 0
        results = []
        result = False
        while index_dynamic < num_dynamic_entries_expected:
            index_dynamic += 1
            results.append(self.compare_entry(expected, actual, index_dynamic, self.is_order_matters(), print_results,
                                              print_failures))
        # now filter based on self.get_match_type()
        mt = self.get_match_type()
        if mt == self.MATCH_ALL:
            result = True
            for res in results:
                result &= result
        elif mt == self.MATCH_ONE:
            result = True
            for res in results:
                result |= result
        elif mt == self.MATCH_ONLY:
            result = True
            for res in results:
                result &= result
            result &= (num_dynamic_entries_expected == num_dynamic_entries_actual)
        elif mt == self.MATCH_NONE:
            result = True
            for res in results:
                result |= result
            result = not result
        return result

    def compare_entry(self, expected, actual, index, order, print_results=False, print_failures=False):
        num_vlans = self.get_compare_number(actual)
        if order:
            results = False
            # check actual.get_vlan_protocol_id(index_dynamic), actual.get_vlan_id(index_dynamic),
            # actual.get_vlan_tci(index_dynamic)
            # vs fields_value if match
            results = self.compare_dynamic_fields(expected, actual, index, index)
            return results
        else:
            # check index = (0-vlan_num) actual.get_vlan_protocol_id(index), actual.get_vlan_id(index),
            # actual.get_vlan_tci(index)
            # vs fields_value until match
            index_actual_vlans = 0
            results = False
            while index_actual_vlans < num_vlans and not results:
                index_actual_vlans += 1
                # check actual.get_vlan_protocol_id(index_dynamic), actual.get_vlan_id(index_dynamic),
                # actual.get_vlan_tci(index_dynamic)
                # vs fields_value if match
                results |= self.compare_dynamic_fields(expected, actual, index, index_actual_vlans)
            return results
            pass

    def __str__(self):
        return "Match Type:" + str(self.get_match_type()) +\
            " Ordering matters:" + str(self.is_order_matters())
