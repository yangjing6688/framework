import re
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Library.ParsingHelper.ParserWrapper import ParserWrapper
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass


class NetworkElementSnmpUtils(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSnmpUtils, self).__init__()
        self.pw = ParserWrapper()
        self.logger = Logger()

    # ##################################################################################################################
    #   General Dictionary Data Utils   ################################################################################
    # ##################################################################################################################
    def create_and_store_interface_index_name_dictionaries(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The end system device that the keyword runs on.

        Creates two dictionaries. One uses interface index as a key and interface name as a value.
        The other uses interface name as a key and interface index as a value.
        Example for use:
        print if_index_to_if_name["1015"]
        Returns 15
        print if_name_to_if_index["15"]
        Returns 1015
        In a stacked unit:
        print if_name_to_if_index["2:15"]
        Returns 2015

        Dictionary Arguments:
        """
        args = {}

        self.execute_verify_keyword(device_name, args, "show_port_names", "create_interface_dictionaries", True,
                                    "Interface dictionaries created.",
                                    "Interface dictionaries not created.",
                                    command_api_const=self.constants.API_PORT,
                                    parse_api_const=self.constants.API_PORT,
                                    **kwargs)

    def get_port_index_from_name(self, device_name, ports):
        """
        Arguments:
        [device_name] - The Network Element to execute the keyword against.
        [ports]       - The port(s) name to be translated to index.

        Returns a list of the converted port indices, or a string if only a single port.
        """
        import re
        port_index = self.value_storage.get_value(device_name, "port_name_index")

        if port_index is None:
            return ""

        ports = ListUtils.convert_to_list(ports)
        port_list = []
        for port in ports:
            if port_index is not None:
                port = port.lower()
                prt_num = re.sub(r"\s", "", re.sub(r"[a-z]", "", port))
                index = port_index.get(prt_num, None)
                if index is not None:
                    port_list.append(index)

        if len(port_list) != 0:
            return port_list if len(port_list) > 1 else port_list[0]
        else:
            raise FailureException("Port(s) " + str(ports) + " not found in OID index list.")

    def create_and_store_interface_index_dot1d_port_dictionaries(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The end system device that the keyword runs on.

        Creates two dictionaries. One uses interface index as a key and dot1d port id as a value.
        The other uses dot1d port id as a key and interface index as a value.
        Example for use:
        print if_index_to_dot1d_id["1015"]
        Returns 5
        print dot1d_id_to_if_index["5"]
        Returns 1015

        Dictionary Arguments:
        """
        args = {}

        self.execute_verify_keyword(device_name, args, "show_dot1d_port_ifindex", "create_dot1d_dictionaries",
                                    True,
                                    "dot1d dictionaries created.",
                                    "dot1d dictionaries not created.",
                                    command_api_const=self.constants.API_PORT,
                                    parse_api_const=self.constants.API_PORT,
                                    **kwargs)

    def get_dot1d_id_from_interface_index(self, device_name, ports):
        """
        Keyword Arguments:
        [device_name] - The Network Element to execute the keyword against.
        [ports]       - The port if index to be translated to the dot1d id.

        Returns a list of the converted dot1d ids, or a string if only a single port.
        """
        dot1d_id = self.value_storage.get_value(device_name, "port_index_dot1d_id")

        if dot1d_id is None:
            return ""

        ports = ListUtils.convert_to_list(ports)
        port_list = []
        for port in ports:
            if dot1d_id is not None:
                index = dot1d_id.get(port, None)
                if index is not None:
                    port_list.append(index)

        if len(port_list) != 0:
            return port_list if len(port_list) > 1 else port_list[0]
        else:
            raise FailureException("Port(s) " + str(ports) + " not found in OID index list.")

    # ##################################################################################################################
    #   Host Monitor Utils   ###########################################################################################
    # ##################################################################################################################
    @staticmethod
    def create_slot_process_string(slots, process_name):
        """
        Keyword Arguments:
        [slots]        - The blade/slot in the chassis.
        [process_name] - The name to give the new process.
        """
        ListUtils.convert_to_list(slots)
        result_list = [i + '.' + StringUtils.ascii_to_dec(process_name) for i in slots]

        return result_list if len(result_list) > 1 else result_list[0]

    # ##################################################################################################################
    #   MLT Utils   ####################################################################################################
    # ##################################################################################################################
    def get_mlt_logical_index(self, device_name, mlt_id, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The unique numeric identifier representing the MLT.

        Gets the logical MLT ID.
        Applies only to VOSS.
        """
        args = {"mlt_id": mlt_id}

        values = self.execute_keyword(device_name, args, "show_mlt_id_logical_index",
                                      command_api_const=self.constants.API_MLT, **kwargs)
        output = values[0].cmd_obj.return_text
        if len(output.split()) >= 3:
            value = output.split()[2]
        else:
            self.logger.log_error("Invalid MLT output for 'show_mlt_id_logical_index'!")
            value = mlt_id
        return value

    def get_voss_mlt_ports(self, device_name, mlt_id, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The unique numeric identifier representing the MLT(VOSS Only).

        Gets the entire hex string representing the current port list of the MLT.
        This keyword only applies to VOSS.
        """
        args = {"mlt_id": mlt_id}

        values = self.execute_keyword(device_name, args, "show_mlt_port_members",
                                      command_api_const=self.constants.API_MLT, **kwargs)

        return values['output'].split()[2]

    # ##################################################################################################################
    #   VLAN Utils  ####################################################################################################
    # ##################################################################################################################
    def get_voss_vlan_ports(self, device_name, vlan, port, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [vlan]         - The unique numeric VLAN ID (VOSS Only).

        Gets the entire hex string representing the current port list of the VLAN.
        This keyword only applies to VOSS.
        """
        args = {"vlan": vlan,
                "port": port,
                "oid_index": vlan}

        values = self.execute_keyword(device_name, args, "show_vlan_members_port",
                                      command_api_const=self.constants.API_VLAN, **kwargs)

        return values['output'].split()[2]

    def get_voss_vlan_if_index(self, vlan_id):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword should be run against.
        [vlan_id]          - The VLAN ID.

        Gets the interface index from the VLAN ID.
        Applies only to VOSS.
        """
        if vlan_id.isdigit():
            return str(int(vlan_id) + 2048)
        else:
            self.logger.log_error(vlan_id + " is not a number!")
            return vlan_id

    # ##################################################################################################################
    #   ACL Utils   ####################################################################################################
    # ##################################################################################################################
    def get_voss_acl_vlans(self, device_name, acl_id, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).

        Gets the entire hex string representing the current vlan list of the ACL.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id}

        values = self.execute_keyword(device_name, args, "show_acl_vlans",
                                      command_api_const=self.constants.API_ACL, **kwargs)

        return values['output'].split()[2]

    def get_voss_acl_ports(self, device_name, acl_id, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).

        Gets the entire hex string representing the current port list of the ACL.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id}

        values = self.execute_keyword(device_name, args, "show_acl_ports",
                                      command_api_const=self.constants.API_ACL, **kwargs)

        return values['output'].split()[2]

    @staticmethod
    def get_voss_acl_type(voss_acl_type):
        """
        Keyword Arguments:
        [voss_acl_type] - ACL Type.

        VOSS ACL Type.  The ACL type in VOSS defines how it is applied.
        """
        if voss_acl_type.lower() == "invlan":
            return "1"
        elif voss_acl_type.lower() == "outvlan":
            return "2"
        elif voss_acl_type.lower() == "inport":
            return "3"
        elif voss_acl_type.lower() == "outport":
            return "4"
        else:
            raise ValueError(voss_acl_type + " is not a valid VOSS ACL type.")

    def get_voss_acl_action(self, action):
        """
        Keyword Arguments:
        [action] - The ACL action to take.

        VOSS default ACL action. Indicates the action to be taken one an ACL or ACE.
        """
        if action.lower() == "permit":
            return "2"
        elif action.lower() == "deny":
            return "1"
        else:
            self.logger.log_error(action + " is not a valid VOSS ACL action.")

    # ##################################################################################################################
    #   SNMP Config Utils   ############################################################################################
    # ##################################################################################################################
    @staticmethod
    def get_voss_security_level(voss_cmd_sec_level):
        """
        Keyword Arguments:
        [voss_cmd_sec_level] - Command security level.

        VOSS Security levels used in the CLI group/access table command.
        """
        if voss_cmd_sec_level.lower() == "noauthnopriv":
            return "no-auth-no-priv"
        elif voss_cmd_sec_level.lower() == "authnopriv":
            return "auth-no-priv"
        elif voss_cmd_sec_level.lower() == "authpriv":
            return "auth-priv"
        else:
            raise ValueError(voss_cmd_sec_level.lower + " is not a valid VOSS security level command type.")

    # ##################################################################################################################
    #   IS-IS, SPBM, and IP Utils for VOSS  ############################################################################
    # ##################################################################################################################
    @staticmethod
    def set_voss_spbvlan_list(pri_vlan, sec_vlan):
        """
        Keyword Arguments:
        [pri_vlan] - The primary SPB VLAN.
        [sec_vlan] - The secondary SPB VLAN.

        Set value in VOSS SPBM VLAN list.
        """
        s_bits = "0" * 4100
        if pri_vlan == '':
            pri_vlan = '0'
        if sec_vlan == '':
            sec_vlan = '0'
        m_bits = list(s_bits)
        m_bits[int(pri_vlan) + 3] = '1'
        m_bits[int(sec_vlan) + 3] = '1'
        m_bits[0] = '1'
        new_bits = "".join(m_bits)
        final_hex = "0x%x" % int(new_bits, 2)

        temp = list(final_hex)
        temp.pop(2)
        final_hex = ''.join(temp)

        return StringUtils.hex_string_to_octet_string(final_hex)

    @staticmethod
    def set_voss_isis_logical_interface_vlans(pri_vlan, sec_vlan):
        """
        Keyword Arguments:
        [pri_vlan] - The primary ISIS interface VLAN.
        [sec_vlan] - The secondary ISIS interface VLAN.

        Set value in VOSS LOGICAL VLAN list.
        """
        s_bits = "0" * 4100
        if pri_vlan == '':
            pri_vlan = '0'
        if sec_vlan == '':
            sec_vlan = '0'
        m_bits = list(s_bits)
        m_bits[int(pri_vlan) + 3] = '1'
        m_bits[int(sec_vlan) + 3] = '1'
        m_bits[0] = '1'
        new_bits = "".join(m_bits)
        final_hex = "0x%x" % int(new_bits, 2)

        temp = list(final_hex)
        temp.pop(2)
        final_hex = ''.join(temp)

        return StringUtils.hex_string_to_octet_string(final_hex)

    def get_isis_circuit(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Gets the next sequential isis ID.
        Applies only to VOSS.
        """
        args = {"oid_index": "0"}

        values = self.execute_keyword(device_name, args, "show_isis_circuit",
                                      command_api_const=self.constants.API_ISIS,
                                      **kwargs)

        return values['output'].split()[2]

    def get_interface_isis_id(self, device_name, interface_index, **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword should be run against.
        [interface_index]  - The interface index.

        Gets the IS-IS circuit ID from the interface index.
        Applies only to VOSS.
        """
        args = {"interface_index": interface_index}

        values = self.execute_keyword(device_name, args, "show_isis_circuit_interfaces",
                                      command_api_const=self.constants.API_ISIS, **kwargs)
        values = values["output"]

        if "experimental" in values:
            values = values.replace("SNMPv2-SMI::experimental.37.1.3.2.1.2.", "")
            return self.pw.get_exact_value_by_offset(values, interface_index, 0)
        else:
            return "0"

    @staticmethod
    def isis_circuit_auth_type(auth_type):
        """
        Keyword Arguments:
        [auth_type] - The isis circuit's authentication type.

        Defines Fabric Attach Element Type.
        """
        auth_type = auth_type.lower()
        a_type = {"none": "0",
                  "simple": "1",
                  "hmac-md5": "2",
                  "hmac-sha-256": "3"}

        try:
            return a_type[auth_type]
        except KeyError:
            raise ValueError(auth_type + " is not a valid IS-IS Hello authentication type value.")

    @staticmethod
    def isis_adj_state(i_state):
        """
        Keyword Arguments:
        [i_state] - The ISIS adjacency state.

        Defines IS-IS IS adjacency state.
        """
        i_state = i_state.lower()
        i_adj_state = {"down": "1",
                       "init": "2",
                       "up": "3",
                       "failed": "4"}

        try:
            return i_adj_state[i_state]
        except KeyError:
            raise ValueError(i_state + " is not a valid IS-IS adjacency state.")

    @staticmethod
    def get_isis_logical_interface_index(isis_logical_id):
        """
        Keyword Arguments:
        [isis_logical_id] - The ISIS logical interface index ID.

        Calculates the interface index for use in an IS-IS logical interface.
        """
        if isis_logical_id.isdigit():
            return str(int(isis_logical_id) + 1599)
        else:
            raise ValueError(isis_logical_id + " is not a number.")

    @staticmethod
    def get_loopback_index(loopback_id):
        """
        Keyword Arguments:
        [loopback_id] - The interface id for the ISIS loopback interface.

        Calculates the interface index for use in a circuit-less (loopback) interface in VOSS.
        """
        if loopback_id.isdigit():
            return str(int(loopback_id) + 1343)
        else:
            Logger().log_error(loopback_id + " is not a number.")
            return loopback_id

    def get_logical_index_for_cli_show(self, device_name, isis_id, **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword should be run against.
        [isis_id]          - The ID of the IS-IS logical interface.

        Gets the correct IS-IS table identifier used by the CLI when showing data for logical interfaces.
        Applies only to VOSS.

        Note:
        In the VOSS CLI show commands for IS-IS the logical interfaces are identified by the name
        instead of the ID if the name is present.
        """
        args = {"isis_id": isis_id}

        values = self.execute_keyword(device_name, args, "show_isis_logical_interface",
                                      command_api_const=self.constants.API_ISIS, **kwargs)
        values = values["output"]

        if "experimental" not in values:
            name = self.pw.get_exact_value_by_offset(values, isis_id, 1)
            if name != "--":
                return name
            else:
                pri_vid = self.pw.get_exact_value_by_offset(values, isis_id, 4)
                if pri_vid == "--":
                    tunnel_ip = self.pw.get_exact_value_by_offset(values, isis_id, 5)
                    return tunnel_ip
                else:
                    g = re.findall(r'\(([^)]+)', pri_vid)
                    return g[0]
        else:
            return "0"

    # ##################################################################################################################
    #   CFM Utils   ####################################################################################################
    # ##################################################################################################################
    def get_domain_index(self, device_name, md_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword should be run against.
        [md_name]          - The MD name.

        Gets the maintenance domain index from the md name.
        Applies only to VOSS.
        """
        args = {"md_name": md_name}

        values = self.execute_keyword(device_name, args, "show_cfm_domain_name",
                                      command_api_const=self.constants.API_CFM, **kwargs)
        values = values["output"]

        if "enterprises" in values:
            values = values.replace("SNMPv2-SMI::enterprises.2272.1.69.1.1.2.", "")
            return self.pw.get_exact_value_by_offset(values, md_name, 0)
        else:
            return "0"

    def get_association_index(self, device_name, ma_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword should be run against.
        [ma_name]          - The MA name.

        Gets the maintenance association index from the ma name.
        Applies only to VOSS.
        """
        args = {"ma_name": ma_name}

        values = self.execute_keyword(device_name, args, "show_cfm_association_name",
                                      command_api_const=self.constants.API_CFM, **kwargs)
        values = values["output"]

        if "enterprises" in values:
            values = values.replace("SNMPv2-SMI::enterprises.2272.1.69.2.1.4.", "")
            return self.pw.get_exact_value_by_offset(values, ma_name, 0)
        else:
            return "0"

    # ##################################################################################################################
    #   Port and VLAN Utils   ##########################################################################################
    # ##################################################################################################################
    @staticmethod
    def set_voss_port_list(get_val, port_index, add_or_delete):
        """
        Keyword Arguments:
        [get_val]       - The value to add or delete.
        [port_index]    - The port-index for the port being configured.
        [add_or_delete] - Defines whether to add or remove the entry.

        Set value in VOSS port list. add_or_delete '1' = add, '0' = delete.
        """
        if get_val.startswith("0x"):
            get_val = get_val[2:]

            if len(get_val) < 9:
                s_bits = "0" * 704
            else:
                get_val = list(get_val)
                get_val[0] = '8'
                get_val = "".join(get_val)

                ss_bits = bin(int(get_val, 16))
                ss_bits = ss_bits[2:]
                s_bits = ss_bits.ljust(704, '0')
            if port_index == '':
                port_index = '0'
            m_bits = list(s_bits)
            m_bits[int(port_index)] = add_or_delete
            if m_bits[0] == '0':
                m_bits[0] = '1'
            new_bits = "".join(m_bits)
            final_hex = "0x%x" % int(new_bits, 2)

            return StringUtils.hex_string_to_octet_string(final_hex)

    @staticmethod
    def set_voss_vlan_list(get_val, vlan, add_or_delete):
        """
        Keyword Arguments:
        [get_val]       - The value to add or delete.
        [vlan]          - The VLAN being configured.
        [add_or_delete] - Defines whether to add or remove the entry.

        Set value in VOSS VLAN list. add_or_delete '1' = add, '0' = delete.
        """
        if get_val.startswith("0x"):
            final_hex = ""
            new = '%04x' % int(vlan)
            if add_or_delete == '1':
                final_hex = get_val + str(new)
            elif add_or_delete == '0':
                final_hex = get_val.replace(str(new), '')
            return StringUtils.hex_string_to_octet_string(final_hex)

    # ##################################################################################################################
    #   RADIUS Utils   #################################################################################################
    # ##################################################################################################################
    @staticmethod
    def vos_radius_server_instance_for_cli(addr):
        """
        Keyword Arguments:
        [addr] - Address for which to generate VOSS server instance.

        Create a VOSS RADIUS server instance identifier for use with CLI user authentication using an IP address.
        """
        addr_string = StringUtils.ipaddr_to_pure_hex(addr)[2:]
        if len(addr_string) < 9:
            formatted_string = ':'.join(a + b for a, b in zip(addr_string[::2], addr_string[1::2]))
            return StringUtils.ipv4_to_dec_with_len(formatted_string) + "." + "1"
        else:
            return StringUtils.ipv6_to_dec_with_len(addr_string) + "." + "1"

    # ##################################################################################################################
    #   IP Address Utils   #############################################################################################
    # ##################################################################################################################
    @staticmethod
    def ip_to_inet_address(addr):
        """
        Keyword Arguments:
        [addr] - The IP address to convert.

        Formats an IP address according to the InetAddress definition described in RFC 4001.
        In basic terms, converts an IP address to a raw octet string for setting an IP address.
        """
        if len(addr) < 7:
            raise FailureException("IP address " + addr + " is not a valid IP address.")
        else:
            hex_str = StringUtils.ipaddr_to_pure_hex(addr)
            return StringUtils.hex_string_to_octet_string(hex_str)

    @staticmethod
    def inet_address_type(inet_addr_type):
        """
        Keyword Arguments:
        [inet_addr_type] - The address type of the inet address.

        Defines InetAddressType definition described in RFC 4001.
        """
        if inet_addr_type.lower() == "unknown":
            return "0"
        elif inet_addr_type.lower() == "ipv4":
            return "1"
        elif inet_addr_type.lower() == "ipv6":
            return "2"
        elif inet_addr_type.lower() == "ipv4z":
            return "3"
        elif inet_addr_type.lower() == "ipv6z":
            return "4"
        elif inet_addr_type.lower() == "dns":
            return "16"
        else:
            raise ValueError(inet_addr_type + " is not a valid InetAddressType.")

    # ##################################################################################################################
    #   DNS Utils   ####################################################################################################
    # ##################################################################################################################
    @staticmethod
    def voss_dns_server_order(pri_sec_or_ter):
        """
        Keyword Arguments:
        [pri_sec_or_ter] - The DNS server order.

        Defines the VOSS DNS server designated order.
        """
        if pri_sec_or_ter.lower() == "primary":
            return "0"
        elif pri_sec_or_ter.lower() == "secondary":
            return "1"
        elif pri_sec_or_ter.lower() == "tertiary":
            return "2"
        else:
            Logger().log_error(pri_sec_or_ter + " is not a valid VOSS DNS server order designation.")
            return pri_sec_or_ter

    # ##################################################################################################################
    #   POE Utils   ####################################################################################################
    # ##################################################################################################################
    @staticmethod
    def poe_priority(priority):
        """
        Keyword Arguments:
        [priority] - The PoE priority value.

        Defines the power over ethernet priority.
        """
        if priority.lower() == "critical":
            return "1"
        elif priority.lower() == "high":
            return "2"
        elif priority.lower() == "low":
            return "3"
        else:
            raise ValueError(priority + " is not a valid power over ethernet priority value.")

    @staticmethod
    def poe_detect_type(detect_type):
        """
        Keyword Arguments:
        [detect_type] - The PoE detection type.

        Defines the power over ethernet detection type.
        """
        if detect_type.lower() == "802.3af":
            return "1"
        elif detect_type.lower() == "802.3af and legacy":
            return "2"
        elif detect_type.lower() == "802.3at":
            return "3"
        elif detect_type.lower() == "802.3at and legacy":
            return "4"
        else:
            raise ValueError(detect_type + " is not a valid power over ethernet detection type.")

    @staticmethod
    def poe_detect_status(detect_status):
        """
        Keyword Arguments:
        [detect_status] - The PoE detection status.

        Defines the POE port detection status.
        """
        if detect_status.lower() == "disabled":
            return "1"
        elif detect_status.lower() == "searching":
            return "2"
        elif detect_status.lower() == "delivering-power":
            return "3"
        elif detect_status.lower() == "fault":
            return "4"
        elif detect_status.lower() == "test":
            return "5"
        elif detect_status.lower() == "other-fault":
            return "6"
        else:
            raise ValueError(detect_status + " is not a valid power over ethernet detection status.")

    @staticmethod
    def poe_power_classification(power_class):
        """
        Keyword Arguments:
        [power_class] - The PoE power classification.

        Defines the POE port power classification.
        """
        if power_class.lower() == "class0":
            return "1"
        elif power_class.lower() == "class1":
            return "2"
        elif power_class() == "class2":
            return "3"
        elif power_class() == "class3":
            return "4"
        elif power_class() == "class4":
            return "5"
        else:
            raise ValueError(power_class + " is not a valid power over ethernet power classification.")

    # ##################################################################################################################
    #   FA Utils   ####################################################################################################
    # ##################################################################################################################
    @staticmethod
    def fa_element_type(element_type):
        """
        Keyword Arguments:
        [element_type] - The Fabric Attach element type.

        Defines Fabric Attach Element Type.
        """
        element_type = element_type.lower()
        fa_type = {"other": "1",
                   "server": "2",
                   "proxy": "3",
                   "servernoauth": "4",
                   "proxynoauth": "5",
                   "clientwaptype1": "6",
                   "clientwaptype2": "7",
                   "clientswitch": "8",
                   "clientrouter": "9",
                   "clientipphone": "10",
                   "clientipcamera": "11",
                   "clientipvideo": "12",
                   "clientsecuritydev": "13",
                   "clientvirtswitch": "14",
                   "clientsrvrendpt": "15"}

        try:
            return fa_type[element_type]
        except KeyError:
            Logger().log_error(element_type + " is not a valid Fabric Attach element type value.")
            return element_type

    @staticmethod
    def fa_element_state(element_state):
        """
        Keyword Arguments:
        [element_state] - The Fabric Attach element state.

        Defines Fabric Element State.
        """
        if element_state.lower() == "t":
            return "0"
        elif element_state.lower() == "u":
            return "1"
        elif element_state.lower() == "d":
            return "2"
        elif element_state.lower() == "s":
            return "3"
        elif element_state.lower() == "v":
            return "4"
        else:
            raise ValueError(element_state + " is not a valid Fabric Attach element state.")

    def fa_element_assign_auth_status(self, element_assign_auth_status):
        """
        Keyword Arguments:
        [element_assign_auth_status] - The Fabric Attach element's assign auth status.

        Defines Fabric Attach Assignment Authentication Status.
        """
        if element_assign_auth_status.lower() == "ap":
            return "1"
        elif element_assign_auth_status.lower() == "af":
            return "2"
        elif element_assign_auth_status.lower() == "na":
            return "3"
        elif element_assign_auth_status.lower() == "n":
            return "4"
        else:
            self.logger.log_error(element_assign_auth_status +
                                  " is not a valid Fabric Attach assignment authentication status.")

    @staticmethod
    def fa_element_auth_status(element_auth_status):
        """
        Keyword Arguments:
        [element_auth_status] - The Fabric Attach element's auth status.

        Defines Fabric Attach Authentication Operational Status.
        """
        if element_auth_status.lower() == "ap":
            return "1"
        elif element_auth_status.lower() == "af":
            return "2"
        elif element_auth_status.lower() == "na":
            return "3"
        elif element_auth_status.lower() == "n":
            return "4"
        else:
            Logger().log_error(element_auth_status + " is not a valid Fabric Attach authentication status.")
            return element_auth_status

    def fa_element_assign_oper_auth_status(self, element_assign_oper_auth_status):
        """
        Keyword Arguments:
        [element_assign_oper_auth_status] - The Fabric Attach element's assign auth operational status.

        Defines Fabric Attach Authentication Operational Status.
        """
        if element_assign_oper_auth_status.lower() == "none":
            return "1"
        elif element_assign_oper_auth_status.lower() == "successnoauth":
            return "2"
        elif element_assign_oper_auth_status.lower() == "successauth":
            return "3"
        elif element_assign_oper_auth_status.lower() == "failmismatchedkeys":
            return "4"
        elif element_assign_oper_auth_status.lower() == "faillocalauthremotenoauth":
            return "5"
        elif element_assign_oper_auth_status.lower() == "faillocalnoauthremoteauth":
            return "6"
        else:
            self.logger.log_error(element_assign_oper_auth_status +
                                  " is not a valid Fabric Attach assignment operational authentication status.")

    @staticmethod
    def fa_element_oper_auth_status(element_oper_auth_status):
        """
        Keyword Arguments:
        [element_oper_auth_status] - The Fabric Attach element's auth operational status.

        Defines Fabric Attach Assignment Authentication Operational Status.
        """
        if element_oper_auth_status.lower() == "none":
            return "1"
        elif element_oper_auth_status.lower() == "successnoauth":
            return "2"
        elif element_oper_auth_status.lower() == "successauth":
            return "3"
        elif element_oper_auth_status.lower() == "failmismatchedkeys":
            return "4"
        elif element_oper_auth_status.lower() == "faillocalauthremotenoauth":
            return "5"
        elif element_oper_auth_status.lower() == "faillocalnoauthremoteauth":
            return "6"
        else:
            Logger().log_error(element_oper_auth_status +
                               " is not a valid Fabric Attach operational authentication status.")
            return element_oper_auth_status

    @staticmethod
    def fa_assign_state(assign_state):
        """
        Keyword Arguments:
        [assign_state] - The Fabric Attach assign state.

        Defines Fabric Attach State information for the VLAN <-> I-SID Assignment.
        """
        if assign_state.lower() == "other":
            return "1"
        elif assign_state.lower() == "pending":
            return "2"
        elif assign_state.lower() == "active":
            return "3"
        elif assign_state.lower() == "rejected":
            return "4"
        else:
            raise ValueError(assign_state + " is not a valid Fabric Attach assignment state value.")

    def fa_assign_origin(self, assign_origin):
        """
        Keyword Arguments:
        [assign_origin] - The Fabric Attach assign origin.

        Defines Fabric Attach Origin information for the VLAN <-> I-SID Assignment.
        """
        if assign_origin.lower() == "other":
            return "1"
        elif assign_origin.lower() == "proxy":
            return "2"
        elif assign_origin.lower() == "client":
            return "3"
        elif assign_origin.lower() == "radiusclient":
            return "4"
        elif assign_origin.lower() == "zerotouchclient":
            return "5"
        else:
            raise self.logger.log_error(assign_origin + " is not a valid Fabric Attach assignment origin value.")

    @staticmethod
    def fa_zero_touch_client(client_name):
        """
        Keyword Arguments:
        [client_name] - The Fabric Attach ZTP client.

        Defines Fabric Attach Zero Touch well-known (standard) origin client names.
        """
        client_name = client_name.lower()
        fa_zero_touch_client_name = {"wap-type1": "6",
                                     "wap-type2": "7",
                                     "switch": "8",
                                     "router": "9",
                                     "phone": "10",
                                     "camera": "11",
                                     "video": "12",
                                     "security-device": "13",
                                     "virtual-switch": "14",
                                     "srvr-endpt": "15",
                                     "ona-sdn": "16",
                                     "ona-spb-over-ip": "17"}

        try:
            return fa_zero_touch_client_name[client_name]
        except KeyError:
            Logger().log_error(client_name + " is not a valid Fabric Attach zero touch client name value.")
            return client_name

    def isid_type(self, i_type):
        """
        Keyword Arguments:
        [i_type] - The ISIS ID type.

        Defines Fabric Attach I-SID type of service on an interface.
        """
        i_type = i_type.lower()
        isid_interface_type = {"elan_trans": "1",
                               "elan": "2",
                               "etree": "3",
                               "l2vsn": "4"}

        try:
            return isid_interface_type[i_type]
        except KeyError:
            self.logger.log_error(i_type + " is not a valid Fabric Attach I-SID type of service value.")

    def isid_origin(self, i_origin):
        """
        Keyword Arguments:
        [i_origin] - The ISIS ID origin.

        Defines Fabric Attach I-SID origin of service on an interface.
        """
        i_origin = i_origin.lower()
        isid_interface_origin = {"config": "1",
                                 "disc_local": "2",
                                 "disc_remote": "3",
                                 "management": "4",
                                 "disc_both": "5",
                                 "spbm": "6",
                                 "mgmt_disc_local": "7",
                                 "mgmt_disc_remote": "8",
                                 "mgmt_disc_both": "9"}

        try:
            return isid_interface_origin[i_origin]
        except KeyError:
            self.logger.log_error(i_origin + " is not a valid Fabric Attach I-SID origin service value.")

    # ##################################################################################################################
    #   System object ID Utility   #####################################################################################
    # ##################################################################################################################
    # Dictionary Items of all Supported Network Element Systems.
    systems = {"SNMPv2-SMI::enterprises.1916.2.93": "summitVer2Stack",
               "SNMPv2-SMI::enterprises.1916.2.172": "summitX440-8t",
               "SNMPv2-SMI::enterprises.1916.2.173": "summitX440-8p",
               "SNMPv2-SMI::enterprises.1916.2.174": "summitX440-24t",
               "SNMPv2-SMI::enterprises.1916.2.175": "summitX440-24p",
               "SNMPv2-SMI::enterprises.1916.2.176": "summitX440-48t",
               "SNMPv2-SMI::enterprises.1916.2.177": "summitX440-48p",
               "SNMPv2-SMI::enterprises.1916.2.178": "summitX440-24t-10G",
               "SNMPv2-SMI::enterprises.1916.2.179": "summitX440-24p-10G",
               "SNMPv2-SMI::enterprises.1916.2.180": "summitX440-48t-10G",
               "SNMPv2-SMI::enterprises.1916.2.181": "summitX440-48p-10G",
               "SNMPv2-SMI::enterprises.1916.2.182": "ags100-24t",
               "SNMPv2-SMI::enterprises.1916.2.183": "ags150-24p",
               "SNMPv2-SMI::enterprises.1916.2.184": "summitX670v-48t",
               "SNMPv2-SMI::enterprises.1916.2.185": "summitX440-L2-24t",
               "SNMPv2-SMI::enterprises.1916.2.186": "summitX440-L2-48t",
               "SNMPv2-SMI::enterprises.1916.2.187": "e4g-200-12x",
               "SNMPv2-SMI::enterprises.1916.2.188": "summitX440-24x",
               "SNMPv2-SMI::enterprises.1916.2.189": "summitX440-24x-10g",
               "SNMPv2-SMI::enterprises.1916.2.190": "summitX430-24t",
               "SNMPv2-SMI::enterprises.1916.2.191": "summitX430-48t",
               "SNMPv2-SMI::enterprises.1916.2.192": "summitX440-24tdc",
               "SNMPv2-SMI::enterprises.1916.2.193": "summitX440-48tdc",
               "SNMPv2-SMI::enterprises.1916.2.194": "summitX770-32q",
               "SNMPv2-SMI::enterprises.1916.2.195": "summitX670G2-48x-4q",
               "SNMPv2-SMI::enterprises.1916.2.196": "summitX670G2-72x",
               "SNMPv2-SMI::enterprises.1916.2.197": "summitX460G2-24t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.198": "summitX460G2-24p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.199": "summitX460G2-24x-10G4",
               "SNMPv2-SMI::enterprises.1916.2.200": "summitX460G2-48t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.201": "summitX460G2-48p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.202": "summitX460G2-48x-10G4",
               "SNMPv2-SMI::enterprises.1916.2.203": "summitX430-8p",
               "SNMPv2-SMI::enterprises.1916.2.204": "summitX430-24p",
               "SNMPv2-SMI::enterprises.1916.2.205": "aviatCtr-8440",
               "SNMPv2-SMI::enterprises.1916.2.206": "summitX450G2-24t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.207": "summitX450G2-24p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.208": "summitX450G2-48t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.209": "summitX450G2-48p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.210": "summitX450G2-24t-G4",
               "SNMPv2-SMI::enterprises.1916.2.211": "summitX450G2-24p-G4",
               "SNMPv2-SMI::enterprises.1916.2.212": "summitX450G2-48t-G4",
               "SNMPv2-SMI::enterprises.1916.2.213": "summitX450G2-48p-G4",
               "SNMPv2-SMI::enterprises.1916.2.214": "summitX460G2-24t-G4",
               "SNMPv2-SMI::enterprises.1916.2.215": "summitX460G2-24p-G4",
               "SNMPv2-SMI::enterprises.1916.2.216": "summitX460G2-48t-G4",
               "SNMPv2-SMI::enterprises.1916.2.217": "summitX460G2-48p-G4 ",
               "SNMPv2-SMI::enterprises.1916.2.218": "oneC-A-600",
               "SNMPv2-SMI::enterprises.1916.2.219": "oneC-V",
               "SNMPv2-SMI::enterprises.1916.2.220": "summitX440G2-48p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.221": "summitX440G2-48t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.222": "summitX440G2-48t-10G4-DC",
               "SNMPv2-SMI::enterprises.1916.2.223": "summitX440G2-24p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.224": "summitX440G2-24t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.225": "summitX440G2-24t-10G4-DC",
               "SNMPv2-SMI::enterprises.1916.2.226": "summitX440G2-24x-10G4",
               "SNMPv2-SMI::enterprises.1916.2.227": "summitX440G2-12p-10G4",
               "SNMPv2-SMI::enterprises.1916.2.228": "summitX440G2-12t-10G4",
               "SNMPv2-SMI::enterprises.1916.2.229": "summitX440G2-12t8fx-G4",
               "SNMPv2-SMI::enterprises.1916.2.230": "summitX440G2-24t-G4",
               "SNMPv2-SMI::enterprises.1916.2.231": "summitX440G2-24fx-G4",
               "SNMPv2-SMI::enterprises.1916.2.232": "summitX620-16T",
               "SNMPv2-SMI::enterprises.1916.2.233": "summitX620-16P",
               "SNMPv2-SMI::enterprises.1916.2.234": "summitX620-16X",
               "SNMPv2-SMI::enterprises.1916.2.235": "summitX620-8T-2X",
               "SNMPv2-SMI::enterprises.1916.2.236": "summitX620-10X",
               "SNMPv2-SMI::enterprises.1916.2.237": "summitX870-32C",
               "SNMPv2-SMI::enterprises.1916.2.238": "summitX870-96X-8C",
               "SNMPv2-SMI::enterprises.1916.2.239": "ecos",
               "SNMPv2-SMI::enterprises.1916.2.240": "isw-4P-2-G2",
               "SNMPv2-SMI::enterprises.1916.2.241": "isw-8P-G4",
               "SNMPv2-SMI::enterprises.1916.2.242": "isw-4GP-2G-G2",
               "SNMPv2-SMI::enterprises.1916.2.243": "isw-8GP-G4",
               "SNMPv2-SMI::enterprises.1916.2.244": "x560-48mp-10GE4-100GE2",
               "SNMPv2-SMI::enterprises.1916.2.245": "x560-48mt-10GE4-100GE2",
               "SNMPv2-SMI::enterprises.1916.2.246": "x560-24mp-10GE4-100GE2",
               "SNMPv2-SMI::enterprises.1916.2.247": "x690-48t-4q-2c",
               "SNMPv2-SMI::enterprises.1916.2.248": "x690-48x-4q-2c",
               "SNMPv2-SMI::enterprises.1916.2.249": "extremeSNSxNSSxA",
               "SNMPv2-SMI::enterprises.1916.2.250": "extremeNSxAx20",
               "SNMPv2-SMI::enterprises.1916.2.251": "extremeNACxAx20",
               "SNMPv2-SMI::enterprises.1916.2.252": "extremeIAxV",
               "SNMPv2-SMI::enterprises.1916.2.253": "extremeIAxAx20",
               "SNMPv2-SMI::enterprises.1916.2.254": "extremeIAxAx300",
               "SNMPv2-SMI::enterprises.1916.2.255": "extremePVxV",
               "SNMPv2-SMI::enterprises.1916.2.256": "extremePVxAx300",
               "SNMPv2-SMI::enterprises.1916.2.257": "summitX460-G2-16mp-32p-10GE4",
               "SNMPv2-SMI::enterprises.1916.2.258": "summitX460G2-24p-24hp",
               "SNMPv2-SMI::enterprises.1916.2.259": "summitX460G2-24t-24ht",
               "SNMPv2-SMI::enterprises.1916.2.260": "extreme210-12t-GE2",
               "SNMPv2-SMI::enterprises.1916.2.261": "extreme210-12p-GE2",
               "SNMPv2-SMI::enterprises.1916.2.262": "extreme210-24t-GE2",
               "SNMPv2-SMI::enterprises.1916.2.263": "extreme210-24p-GE2",
               "SNMPv2-SMI::enterprises.1916.2.264": "extreme210-48t-GE4",
               "SNMPv2-SMI::enterprises.1916.2.265": "extreme210-48p-GE4",
               "SNMPv2-SMI::enterprises.1916.2.266": "extreme220-12t-10GE2",
               "SNMPv2-SMI::enterprises.1916.2.267": "extreme220-12p-10GE2",
               "SNMPv2-SMI::enterprises.1916.2.268": "extreme220-24t-10GE2",
               "SNMPv2-SMI::enterprises.1916.2.269": "extreme220-24p-10GE2",
               "SNMPv2-SMI::enterprises.1916.2.270": "extreme220-48t-10GE4",
               "SNMPv2-SMI::enterprises.1916.2.271": "extreme220-48p-10GE4",
               "SNMPv2-SMI::enterprises.1916.2.272": "extreme240-8mt-16t-10GE4",
               "SNMPv2-SMI::enterprises.1916.2.273": "extreme240-8mp-16p-10GE4",
               "SNMPv2-SMI::enterprises.1916.2.274": "extreme240-32t-16mt-10GE6",
               "SNMPv2-SMI::enterprises.1916.2.275": "extreme240-32p-16mp-10GE6",
               "SNMPv2-SMI::enterprises.1916.2.276": "extreme825-48v-6c",
               "SNMPv2-SMI::enterprises.1916.2.277": "extremeNMSxAx25",
               "SNMPv2-SMI::enterprises.1916.2.278": "extremeNMSxAx305",
               "SNMPv2-SMI::enterprises.1916.2.279": "extremeIAxAx25",
               "SNMPv2-SMI::enterprises.1916.2.280": "extremeIAxAx305",
               "SNMPv2-SMI::enterprises.1916.2.281": "extremePVxAx305",
               "SNMPv2-SMI::enterprises.1916.2.282": "extremeEMPx35",
               "SNMPv2-SMI::enterprises.1916.2.283": "extremeEMPx5310",
               "SNMPv2-SMI::enterprises.1916.2.284": "extremeEMPxV",
               "SNMPv2-SMI::enterprises.1916.2.286": "xtremeWhitebox",
               "SNMPv2-SMI::enterprises.1916.2.291": "vm386EXOS",
               "SNMPv2-SMI::enterprises.1916.2.292": "extremeNMSxV",
               "SNMPv2-SMI::enterprises.1916.2.293": "extremeSSxIxA",
               "SNMPv2-SMI::enterprises.1916.2.294": "extremeESEx2000",
               "SNMPv2-SMI::enterprises.2272.201": "rcVSP9012",
               "SNMPv2-SMI::enterprises.2272.202": "rcVSP4850GTS",
               "SNMPv2-SMI::enterprises.2272.203": "rcVSP4850GTSPWRPLUS",
               "SNMPv2-SMI::enterprises.2272.204": "rcVSP9010",
               "SNMPv2-SMI::enterprises.2272.205": "rcVSP8284XSQ",
               "SNMPv2-SMI::enterprises.2272.206": "rcVSP4450GSXPWRPLUS",
               "SNMPv2-SMI::enterprises.2272.207": "rcVSP4450GTXHTPWRPLUS",
               "SNMPv2-SMI::enterprises.2272.208": "rcVSP8404",
               "SNMPv2-SMI::enterprises.2272.209": "rcVSP7254XSQ",
               "SNMPv2-SMI::enterprises.2272.210": "rcVSP7254XTQ",
               "SNMPv2-SMI::enterprises.2272.211": "rcVSP4450GSX",
               "SNMPv2-SMI::enterprises.2272.212": "rcVSP8608"
               }
