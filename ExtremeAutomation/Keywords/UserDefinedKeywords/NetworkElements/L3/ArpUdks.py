from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementArpGenKeywords import NetworkElementArpGenKeywords


class ArpUdks():
    def __init__(self) -> None:
        self.networkElementArpGenKeywords = NetworkElementArpGenKeywords()

    def Add_ARP_Entry_and_Verify_it_was_Added(self, netelem_name, ip, mac, interface=None, **kwargs):
        """  Creates_an_ARP_entry_and_verify_it_was_created. (EXOS_does_not_support_specifying_an_interface) """
        if interface is None:
            self.networkElementArpGenKeywords.arp_create_entry(netelem_name, ip, mac, **kwargs)
        else:
            self.networkElementArpGenKeywords.arp_create_entry_interface(netelem_name, ip, mac, interface, **kwargs)
        self.networkElementArpGenKeywords.arp_verify_entry_exists(netelem_name, ip, mac, interface, **kwargs)

    def Remove_ARP_Entry_and_verify_it_was_Removed(self, netelem_name, ip, mac, interface=None, **kwargs):
        """  Delete_an_ARP_entry_and_verify_it_was_deleted. (EXOS_does_not_support_specifying_an_interface) """
        self.networkElementArpGenKeywords.arp_delete_entry(netelem_name, ip, ignore_cli_feedback=True)
        self.networkElementArpGenKeywords.arp_verify_entry_does_not_exist(netelem_name, ip, mac, interface, **kwargs)
