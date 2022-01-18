from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementNdGenKeywords import NetworkElementNdGenKeywords


class NdUdks():
    def __init__(self) -> None:
        self.networkElementNdGenKeywords = NetworkElementNdGenKeywords()

    def Add_ND_Entry_and_Verify_it_was_Added(self, netelem_name,  ipv6,  mac, interface=1, ports=None, **kwargs):
        self.networkElementNdGenKeywords.nd_set_v6_neighbor(netelem_name, ipv6, mac, interface, ports, **kwargs)
        self.networkElementNdGenKeywords.nd_verify_neighbor_entry(netelem_name, ipv6, mac, interface, **kwargs)

    def Remove_ND_Entry_and_Verify_it_was_Removed(self, netelem_name,  ipv6, mac, interface=None, **kwargs):
        self.networkElementNdGenKeywords.nd_clear_v6_neighbor(netelem_name, ipv6, interface, **kwargs)
        self.networkElementNdGenKeywords.nd_verify_neighbor_entry_does_not_exist(netelem_name, ipv6, mac, interface, **kwargs)
