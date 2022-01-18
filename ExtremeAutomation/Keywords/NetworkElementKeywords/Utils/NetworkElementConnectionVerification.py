from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import \
    TrafficStreamConfigurationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketTypeConstants import PacketTypeConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementPortGenKeywords import NetworkElementPortGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementFdbGenKeywords import NetworkElementFdbGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementLldpGenKeywords import NetworkElementLldpGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementVlanGenKeywords import NetworkElementVlanGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementListUtils import NetworkElementListUtils
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Library.Utils.NetworkElementUtils import NetworkElementUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils


class NetworkElementConnectionVerification(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementConnectionVerification, self).__init__()

        try:
            self.variables = RobotUtils.get_variables(no_decoration=True)
            self.netelems = NetworkElementUtils.get_device_names_from_variables(self.variables, "netelem")
        except Exception:
            self.logger.log_info("Connection Verification cannot be used outside of a robot / pytest run.")

        self.tgen_stream = TrafficStreamConfigurationKeywords()
        self.tgen_pkt = TrafficPacketCreationKeywords()
        self.portc = NetworkElementPortGenKeywords()
        self.nlu = NetworkElementListUtils()
        self.vlan = NetworkElementVlanGenKeywords()
        self.lldp = NetworkElementLldpGenKeywords()
        self.fdb = NetworkElementFdbGenKeywords()

    def verify_all_netelem_tgen_connections(self, vlan, **kwargs):
        """
        Keyword Arguments:
        [vlan] - The VLAN to use for connection verification.

        Verifies the connection port for all tgen ports.
        """
        self._init_keyword(**kwargs)
        not_found = []

        for netelem in self.netelems:
            device_name = self.variables[netelem]['name']
            netelem_tgen_portlist = self.variables[netelem]["tgen"]

            for tgen_port in netelem_tgen_portlist:
                host = netelem_tgen_portlist[tgen_port]["intnet"]
                host_hash = StringUtils.create_mac_hash(host)
                smac = StringUtils.normalize_mac(host_hash)
                port = netelem_tgen_portlist[tgen_port]["ifname"]

                try:
                    self.fdb.fdb_entry_should_exist(device_name, smac, vlan, port, wait_for=True, max_wait=20,
                                                    log_keyword=False)
                    self.logger.log_info("Port " + port + " is connected correctly.")
                except FailureException:
                    not_found.append("Port " + port + " is NOT connected correctly.")

        if not_found:
            all_found = False
            fail_string = "\n".join(not_found)
        else:
            all_found = True
            fail_string = None
        kw_result = KeywordResult("All Network Elements", all_found, "All TGen connections found", fail_string, None)
        return self._keyword_cleanup([kw_result])

    def verify_all_netelem_isl_connections(self, **kwargs):
        """
        Keyword Arguments:

        Verifies all Network Element ISL connection ports.
        """
        self._init_keyword(**kwargs)
        no_neighbor = []

        isl_dict = {}
        for netelem in self.netelems:
            isl_dict[netelem] = {}
            isl_ports = self.variables[netelem]["isl"]

            for port in isl_ports:
                ifname = isl_ports[port]["ifname"]
                intnet = isl_ports[port]["intnet"]
                isl_dict[netelem][port] = [ifname, intnet]

        for netelem_name in isl_dict:
            other_netelems = dict(isl_dict)
            other_netelems.pop(netelem_name)

            for port in isl_dict[netelem_name]:
                lan_found = False
                ifname = isl_dict[netelem_name][port][0]
                lan_segment = isl_dict[netelem_name][port][1]

                for neighbor in other_netelems:
                    for neighbor_port in isl_dict[neighbor]:
                        if lan_segment.lower() == isl_dict[neighbor][neighbor_port][1].lower():
                            lan_found = True
                            try:
                                self.lldp.verify_lldp_remote_port(self.variables[netelem_name]["name"], ifname,
                                                                  isl_dict[neighbor][neighbor_port][0], wait_for=True,
                                                                  max_wait=20, interval=5)
                            except FailureException:
                                no_neighbor.append("The ISL port connection between " +
                                                   self.variables[netelem_name]["name"] + " " + ifname +
                                                   " and remote port " + self.variables[neighbor]["name"] + " " +
                                                   isl_dict[neighbor][neighbor_port][0] +
                                                   " was not found!")
                            break

                    if lan_found:
                        break
                if not lan_found:
                    no_neighbor.append("No neighbor port was found for " + self.variables[netelem_name]["name"] + " " +
                                       ifname + " with intnet " + lan_segment + "!")
        if no_neighbor:
            neighbors_found = False
            fail_string = "\n".join(no_neighbor)
        else:
            neighbors_found = True
            fail_string = None
        kw_result = KeywordResult("All Network Elements", neighbors_found,
                                  "All ISL connections found.", fail_string, None)
        return self._keyword_cleanup([kw_result])

    def create_tgen_connection_verification_packets(self, **kwargs):
        """
        Keyword Arguments:

        Creates the packets sent by the Traffic Generator.
        """
        self._init_keyword(**kwargs)

        for netelem in self.netelems:
            portname_list = self.variables["tgen_ports"][netelem]

            for port in portname_list:
                port_dict = {"tgen_name": portname_list[port]["tgen_name"], "ifname": portname_list[port]["ifname"]}
                packet_name = str(netelem) + "_" + str(port)
                host = portname_list[port]["intnet"]
                host_hash = StringUtils.create_mac_hash(host)
                smac = StringUtils.normalize_mac(host_hash)

                self.tgen_pkt.create_packet(packet_name, PacketTypeConstants.ETH2_PACKET)
                self.tgen_pkt.set_ethernet2(packet_name, "00:11:22:33:22:11", smac)
                self.tgen_stream.configure_stream_packet(port_dict, "1", packet_name)
                self.tgen_stream.configure_stream_mode_continuous(port_dict, "1")
                self.tgen_stream.add_stream_to_port(port_dict, "1")

    def enable_and_configure_all_netelem_ports(self, vlan_id, **kwargs):
        """
        Keyword Arguments:
        [vlan_id] - The VLAN to use for connection verification.

        Enables and adds all Network Element ports to the selected VLAN.
        """
        self._init_keyword(**kwargs)
        netelem_nums = self.nlu.create_list_of_network_elements()

        for netelem_num in netelem_nums:
            netelem_name = self.variables[netelem_num]["name"]
            tgen_ports = self.nlu.create_list_of_netelem_tgen_ports(netelem_num)
            isl_ports = self.nlu.create_list_of_netelem_isl_ports(netelem_num)
            self.lldp.enable_lldp_transmission_and_reception_on_port(netelem_name, isl_ports)
            self.lldp.configure_lldp_tx_interval(netelem_name, "5")
            self.portc.configure_port_enable(netelem_name, tgen_ports)
            self.portc.configure_port_enable(netelem_name, isl_ports)
            self.portc.port_should_be_operational(netelem_name, tgen_ports, wait_for=True, max_wait=300, interval=5)
            self.vlan.create_vlan(netelem_name, vlan_id)
            self.vlan.add_port_to_untagged_egress(netelem_name, vlan_id, tgen_ports)
            self.vlan.configure_port_pvid(netelem_name, tgen_ports, vlan_id)

    def disable_and_cleanup_all_netelem_ports(self, vlan_id, **kwargs):
        """
        Keyword Arguments:
        [vlan_id] - The VLAN ID used for connection verification.

        Removes the selected VLAN and disables all Network Element ports.
        """
        self._init_keyword(**kwargs)
        netelem_nums = self.nlu.create_list_of_network_elements()

        for netelem_num in netelem_nums:
            netelem_name = self.variables[netelem_num]["name"]
            tgen_ports = self.nlu.create_list_of_netelem_tgen_ports(netelem_num)
            isl_ports = self.nlu.create_list_of_netelem_isl_ports(netelem_num)
            self.lldp.disable_lldp_transmission_and_reception_on_port(netelem_name, isl_ports)
            self.lldp.configure_lldp_tx_interval(netelem_name, "30")
            self.portc.configure_port_disable(netelem_name, tgen_ports)
            self.portc.configure_port_disable(netelem_name, isl_ports)
            self.portc.port_should_be_disabled(netelem_name, tgen_ports)
            self.portc.port_should_be_disabled(netelem_name, isl_ports)
            self.vlan.remove_port_from_vlan_egress(netelem_name, vlan_id, tgen_ports)
            self.vlan.configure_port_pvid(netelem_name, tgen_ports, "1")
            self.vlan.remove_vlan(netelem_name, vlan_id)
