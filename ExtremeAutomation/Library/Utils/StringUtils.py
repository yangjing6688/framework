import re
import sys
import traceback
import json
import codecs
import hashlib
import binascii
import datetime
import ipaddress
from ast import literal_eval
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.Ipv6Address import Ipv6Address
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
from ExtremeAutomation.Keywords.FailureException import FailureException


class StringUtils(object):
    @staticmethod
    def normalize_value(ip, format_type):
        """Converts an IP address to the standard format for Keyword usage."""
        if isinstance(ip, str) and "Not Set" in ip:
            return ip
        if format_type == PacketConstants.BOOLEAN:
            if isinstance(ip, str):
                return bool(ip)
            return ip
        try:
            if format_type == PacketConstants.IPV4_ADDRESS:
                return Ipv4Address(ip).to_string()
            if format_type == PacketConstants.IPV6_ADDRESS:
                return Ipv6Address(ip).to_string()
            if format_type == PacketConstants.ENET_ADDRESS:
                return EnetAddress(ip).to_string()
        except ValueError:
            return ip
        if format_type == PacketConstants.HEX_STRING:
            return StringUtils.place_character_every_n_characters(ip.replace(".", "").replace(":", "").replace(" ", ""),
                                                                  " ", 2)
        if format_type == PacketConstants.ASCII_STRING:
            return StringUtils.place_character_every_n_characters(binascii.hexlify(ip), " ", 2)
        if format_type == PacketConstants.INTEGER:
            if isinstance(ip, int):
                return ip
            if ip.startswith("0x"):
                ip = ip[2:]
                if ip == '':
                    ip = '0'
                return int(ip.replace(" ", "").upper(), 16)
            else:
                return int(ip)
        return ip

    @staticmethod
    def replace_all_regex(removelist, replace_with, source):
        """Uses regular expressions to replace a list of values with the supplied value."""
        return re.sub(r'' + removelist + '', replace_with, source)

    @staticmethod
    def place_character_every_n_characters(string, delim, length):
        """Adds the given delimiter every <length> in the string."""
        return delim.join(string[i:i + length] for i in range(0, len(string), length))

    @staticmethod
    def normalize_mac(macs, delimiter=":", three_block=False):
        """
        Accepts a mac string or a list of mac strings.

        Each valid mac is converted to ##x##x##x##x##x## format, where x is the provided delimiter.

        Unless the three_block flag is set to True. Then the format is ####x####x####, again where
        x is the delimiter.

        For EXOS all alphabetical hex characters are set to lower case.

        Any non valid macs (non-hex character, too many characters, etc) are returned as they were originally passed.
        """
        macs = ListUtils.convert_to_list(macs)

        normalized_macs = []

        three_block = StringUtils.string_to_boolean(three_block)

        for mac in macs:
            standard_mac = ""
            mac_list = []

            if mac.startswith("0x"):
                raw_hex = mac[2::]
                if not three_block:
                    normalized_macs.append(delimiter.join(raw_hex[i:i + 2] for i in range(0, len(raw_hex), 2)))
                else:
                    normalized_macs.append(delimiter.join(raw_hex[i:i + 4] for i in range(0, len(raw_hex), 4)))
            else:
                for i in range(len(mac)):
                    if StringUtils.__ishex(mac[i]):
                        standard_mac += mac[i]
                if len(standard_mac) == 12:
                    if not three_block:
                        for i in range(0, len(standard_mac), 2):
                            mac_list.append(standard_mac[i: i + 2])
                            if i != 10:
                                mac_list.append(delimiter)
                    else:
                        for i in range(0, len(standard_mac), 4):
                            mac_list.append(standard_mac[i: i + 4])
                            if i != 8:
                                mac_list.append(delimiter)
                    normalized_macs.append("".join(mac_list).upper())
                else:
                    normalized_macs.append(mac)
        return normalized_macs if len(normalized_macs) > 1 else normalized_macs[0]

    @staticmethod
    def normalize_mac_lowercase(mac, delimiter=":", three_block=False):
        """
        Takes any mac and returns it in ##x##x##x##x##x## format, where x is the provided delimiter.

        Unless the three_block flag is set to True. Then the format is ####x####x####, again where
        x is the delimiter.

        For EXOS all alphabetical hex characters are set to lower case.
        """
        from ExtremeAutomation.Library.Logger.Logger import Logger
        standard_mac = ""
        mac_list = []

        if isinstance(three_block, str):
            three_block = True if three_block.lower() == "true" else False

        for i in range(len(mac)):
            if StringUtils.__ishex(mac[i]):
                standard_mac += mac[i]
        if len(standard_mac) == 12:
            if not three_block:
                for i in range(0, len(standard_mac), 2):
                    mac_list.append(standard_mac[i: i + 2])
                    if i != 10:
                        mac_list.append(delimiter)
            else:
                for i in range(0, len(standard_mac), 4):
                    mac_list.append(standard_mac[i: i + 4])
                    if i != 8:
                        mac_list.append(delimiter)
            return "".join(mac_list).lower()
        else:
            Logger().log_error(mac + " is an invalid MAC address.")
            return mac

    @staticmethod
    def __ishex(c):
        """Helper function for normalize mac. Checks if a given char is a valid hexadecimal character."""
        if c.isdigit():
            return True
        c = c.lower()
        if re.search("[a-f]", c):
            return True
        else:
            return False

    @staticmethod
    def exos_vlan_string(vlans, vman=False):
        """
        Takes an EXOS vlan integer and converts it into the following format.
        vlans = 123, output = VLAN_0123. Can be a single string or list of strings.
        vlan = 12, output = VLAN_0012

        If vlans is a list then a list of converted vlan strings will be returned. If vlans is a single string
        a string with the converted VLAN will be returned.
        """
        if vlans is None:
            return None
        vlans = ListUtils.convert_to_list(vlans)

        exos_vlan_strings = []
        vlan_prefix = "VLAN_" if not vman else "VMAN_"

        for vlan in vlans:
            if vlan.isdigit():
                if int(vlan) == 1:
                    exos_vlan_strings.append("Default")
                else:
                    exos_vlan_strings.append(vlan_prefix + ("0" * (4 - len(vlan)) + str(vlan)))
            else:
                exos_vlan_strings.append(vlan)

        return exos_vlan_strings if len(exos_vlan_strings) > 1 else exos_vlan_strings[0]

    @staticmethod
    def isw_vlan_string(vlan):
        """
        Takes an EXOS vlan interger and converts it into the following format.
        vlan = 123, output = VLAN_0123
        vlan = 12, output = VLAN_0012
        """
        if vlan.isdigit():
            if int(vlan) != 1:
                return "VLAN" + ("0" * (4 - len(vlan)) + str(vlan))
            else:
                return "Default"
        return vlan

    @staticmethod
    def expand_voss_vlan_string(compressed_vlan):
        """
        Takes a compressed VOSS VLAN string and expands each VLAN id into a list.
        For example:  '100-102,105'  converts to: ['100', '101', '102', '105'].
        """
        x = [ss.split('-') for ss in compressed_vlan.split(',')]
        x = [range(int(i[0]), int(i[1]) + 1) if len(i) == 2 else i for i in x]
        return [str(item) for sublist in x for item in sublist]

    @staticmethod
    def eos_interface(iface, prefix="vlan"):
        """
        Converts the interface number to an EOS interface string.

        Ex:
        iface = 1 returns 'vlan.0.1'
        """
        if iface is not None:
            iface = ListUtils.convert_to_list(iface)
            int_list = []
            for i in iface:
                int_list.append(prefix + ".0." + i)

            return int_list if len(int_list) > 1 else int_list[0]

        return None

    @staticmethod
    def exos_loopback_interface(ifaces):
        """
        Converts the interface number to an EXOS loopback name.

        Ex:
        iface = 1 returns 'LO1'
        """
        ifaces = ListUtils.convert_to_list(ifaces)
        converted_ifaces = ["L0" + i if i.isdigit() else i for i in ifaces]

        return converted_ifaces if len(converted_ifaces) > 1 else converted_ifaces[0]

    @staticmethod
    def exos_tunnel_interface(iface):
        """
        Converts the interface number to an EXOS tunnel name.

        Ex:
        iface = 1 returns 'TUN1'
        """
        if iface is not None:
            iface = ListUtils.convert_to_list(iface)
            int_list = []
            for i in iface:
                if i.isdigit():
                    int_list.append("TUN" + i)
                else:
                    int_list.append(i)

            return int_list if len(int_list) > 1 else int_list[0]

        return None

    @staticmethod
    def exos_format_instance(sids):
        """Returns the msti in EXOS format."""
        return ["s" + i for i in sids] if isinstance(sids, list) else "s" + sids

    @staticmethod
    def format_json_output(output):
        """
        If the output is from JSON we convert it from a string to a dictionary.
        Otherwise the output is left as a string.
        """
        if isinstance(output, str):
            try:
                string_output = output.replace(":false", ":False")
                string_output = string_output.replace(":true", ":True")
                string_output = literal_eval(string_output)
                return string_output
            except ValueError:
                try:
                    output = json.loads(output)
                except ValueError:
                    pass
            except SyntaxError:
                pass
        return output

    @staticmethod
    def prefix_len(netmask):
        """This function takes an IP address mask and returns the prefix length."""
        netmask = ListUtils.convert_to_list(netmask)

        netmask_list = []
        try:
            for i in netmask:
                binary_str = ''
                i = i.split('.')
                for octet in i:
                    # Magic
                    binary_str += bin(int(octet))[2:].zfill(8)
                netmask_list.append(str(len(binary_str.rstrip('0'))))
        except ValueError:
            netmask_list = netmask

        return netmask_list if len(netmask_list) > 1 else netmask_list[0]

    @staticmethod
    def mask_from_prefix(cidr):
        """This function takes a prefix length and returns the netmask."""
        cidr = ListUtils.convert_to_list(cidr)

        cidr_list = []
        for i in cidr:
            mask = [0, 0, 0, 0]
            i = int(i)
            for num in range(i):
                mask[num // 8] += + (1 << (7 - num % 8))
            cidr_list.append(".".join(map(str, mask)))

        return cidr_list if len(cidr_list) > 1 else cidr_list[0]

    @staticmethod
    def normalize_list(list_string):
        """
        This functions takes a list of integers in any format and returns them in a python list.
        For example {1,2,3}, (1, 2, 3), or 1, 2, 3 would all be converted to [1, 2, 3].
        """
        if not isinstance(list_string, list):
            new_list_string = ""

            for char in list_string:
                if char.isdigit() or char == ",":
                    new_list_string += char

            normal_list = new_list_string.split(",")

            return normal_list
        else:
            # String is already a list.
            # Convert each index to an integer and return the list.
            int_list = [int(i) for i in list_string]

            return int_list

    @staticmethod
    def normalize_exos_ports(ports_string, as_list=False):
        """Returns a normalized string or list of EXOS ports."""
        formatted_ports_string = ""

        if isinstance(ports_string, list):
            ports_string = ",".join(ports_string)

        for c in ports_string:
            if c.isdigit():
                formatted_ports_string += c
            elif c == "," or c == ":":
                formatted_ports_string += c

        if as_list:
            return formatted_ports_string.split(",")
        return formatted_ports_string

    @staticmethod
    def range_to_list(range_string):
        """
        This function takes a range string value such as "5,7-10,4" and returns a list of int values
        representing the entire list [4,5,7,8,9,10]
        """
        range_string = range_string.split(",")
        final_set = set()
        for item in range_string:
            if "-" in item:
                range_val = item.split("-")
                if int(range_val[0]) < int(range_val[1]):
                    range_list = range(int(range_val[0]), int(range_val[1]) + 1)
                    for num in range_list:
                        final_set.add(num)
                else:
                    raise FailureException("Invalid range specified.")
            else:
                final_set.add(int(item))
        final_set = sorted(list(final_set))
        return final_set

    @staticmethod
    def string_to_boolean(boolean_string, default=True):
        """
        Converts boolean strings to a python boolean.
        Example "True" and "true" would be converted to True.
        The default option is used to set the boolean value when the passed string
        does not contain "True", "true", "False", or "false".

        """
        if str(type(boolean_string)) == "<type 'unicode'>":
            boolean_string = boolean_string.encode('utf8')

        if isinstance(boolean_string, str):
            if boolean_string.lower() == "true":
                boolean = True
            elif boolean_string.lower() == "false":
                boolean = False
            else:
                boolean = default
        elif isinstance(boolean_string, bool):
            boolean = boolean_string
        else:
            boolean = default

        return boolean

    @staticmethod
    def expand_ipv6_address(ipv6_addr, leading_zeroes=True):
        """
        Returns a full length IPv6 address from a shortened address.

        Ex:
        2001::1 expands to 2001:0:0:0:0:0:0:1
        """
        ipv6_addr = Ipv6Address(ipv6_addr).to_string()

        if leading_zeroes:
            return ipv6_addr
        else:
            expanded_ipv6_addr = ipv6_addr.split(":")
            for i in range(len(expanded_ipv6_addr)):
                new_block = ""
                for index, c in enumerate(expanded_ipv6_addr[i]):
                    if index == 0:
                        new_block = expanded_ipv6_addr[i]
                    elif index == len(expanded_ipv6_addr[i]) - 1:
                        expanded_ipv6_addr[i] = c
                        break

                    if c == "0":
                        new_block = new_block[1::]
                    else:
                        expanded_ipv6_addr[i] = new_block
                        break
            return ":".join(expanded_ipv6_addr)

    @staticmethod
    def collapse_ipv6_address(ipv6_addr):
        """
        Returns a shortened IPv6 address from a full length address.

        Ex:
        2001:0:0:0:0:0:0:1 shortens to 2001::1
        """
        return Ipv6Address(ipv6_addr).to_string(collapsed=True)

    @staticmethod
    def rzfill(string, length):
        """Pads a given string to make it the set length."""
        return ((string[::-1]).zfill(length))[::-1]

    @staticmethod
    def pretty_print_dict(json_string):
        """Returns a formatted string representation of the given JSON dictionary."""
        return json.dumps(json_string, sort_keys=True, indent=4)

    @staticmethod
    def create_mac_hash(txt, length=10):
        """This creates a MAC length hash from any string."""
        _hash = hashlib.md5()
        _hash.update(txt)
        hex_string = _hash.hexdigest()[:length]
        return "00" + str(hex_string)

    @staticmethod
    def _is_mac(string):
        """Verifies whether or not the given string is a valid MAC address."""
        if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", string.lower()):
            return True
        else:
            return False

    @staticmethod
    def mac_to_dec(mac_string):
        """
        This function takes a mac address in the form of xx:xx:xx:xx:xx:xx and converts it to dotted decimal form.
        For example 00:33:44:55:66:ac would be converted to 0.51.68.85.102.172.
        """
        return ".".join(str(x) for x in [int(x, 16) for x in mac_string.split(':')])

    @staticmethod
    def mac_to_dec_with_len(mac_string):
        """
        This function takes a mac address in the form of xx:xx:xx:xx:xx:xx and converts it to dotted decimal form
        with the length identifier of 6.
        For example 00:33:44:55:66:ac would be converted to 6.0.51.68.85.102.172.
        """
        return "6." + ".".join(str(x) for x in [int(x, 16) for x in mac_string.split(':')])

    @staticmethod
    def dec_to_mac(dec_string):
        """
        This function takes a decimal mac address in the form of d+.d+.d+.d+.d+.d+ and converts it to hex.
        For example 0.51.68.85.102.172 would be converted to 00:33:44:55:66:ac.
        """
        return ":".join(str(x) for x in ["{:02x}".format(int(x)) for x in dec_string.split('.')])

    @staticmethod
    def ipv4_to_dec(ip_string):
        """
        This function takes an ipv4 address in the form of xx:xx:xx:xx and converts it to dotted decimal form.
        For example ac:03:40:02 would be converted to 172.3.64.2.
        """
        return ".".join(str(x) for x in [int(x, 16) for x in ip_string.split(':')])

    @staticmethod
    def ipv6_to_dec(ip_string):
        """
        This function takes an ip address in the form of xxxx:xxxx:xxxx and converts it to dotted decimal form.
        For example 2005:9876::1 would be converted to 32.5.152.118.0.0.0.0.0.0.0.0.0.0.0.1.
        """
        if "::" in ip_string:
            ip_string = ipaddress.ip_address(ip_string).exploded
            ip_string = ':'.join(a + b for a, b in zip(ip_string.replace(":", "")[::2],
                                                       ip_string.replace(":", "")[1::2]))
            return ".".join(str(x) for x in [int(x, 16) for x in ip_string.split(':')])
        elif ":" in ip_string:
            ip_string = ':'.join(
                a + b for a, b in zip(ip_string.replace(":", "")[::2], ip_string.replace(":", "")[1::2]))
            return ".".join(str(x) for x in [int(x, 16) for x in ip_string.split(':')])
        else:
            return ip_string

    @staticmethod
    def ipv4_to_dec_with_len(ip_string):
        """
        This function takes an IP address in the form of xx:xx:xx:xx and converts it to dotted decimal form
        with the ip address type of 1 for ipv4 and length identifier of 4 and(RFC 4001).
        For example af:40:03:96 would be converted to 1.4.175.64.3.150.
        """
        return "1.4." + ".".join(str(x) for x in [int(x, 16) for x in ip_string.split(':')])

    @staticmethod
    def ipv6_to_dec_with_len(ip_string):
        """
        This function takes an ip address in the form of xxxx:xxxx:xxxx and converts it to dotted decimal form
        with the ip address type of 2 for ipv6 and length identifier of 16 (RFC 4001).
        For example 2005:9876::1 would be converted to 2.16.32.5.152.118.0.0.0.0.0.0.0.0.0.0.0.1.
        """
        if "::" in ip_string:
            ip_string = ipaddress.ip_address(ip_string).exploded
            ip_string = ':'.join(a + b for a, b in zip(ip_string.replace(":", "")[::2],
                                                       ip_string.replace(":", "")[1::2]))
            return "2.16." + ".".join(str(x) for x in [int(x, 16) for x in ip_string.split(':')])
        elif ":" in ip_string:
            ip_string = ':'.join(
                a + b for a, b in zip(ip_string.replace(":", "")[::2], ip_string.replace(":", "")[1::2]))
            return "2.16." + ".".join(str(x) for x in [int(x, 16) for x in ip_string.split(':')])
        else:
            return ip_string

    @staticmethod
    def dec_to_hex_ipv4(dec_string):
        """
        This function takes a decimal ipv4 address in the form of d+.d+.d+.d+ and converts it to hex.
        For example 192.168.10.5 would be converted to c0:a8:0a:05.
        """
        return ":".join(str(x) for x in ["{:02x}".format(int(x)) for x in dec_string.split('.')])

    @staticmethod
    def split_every_n(n, s):
        """
        Splits a string every n'th character.
        Example: split_every_n(4, '0fa000140020') returns: ['0fa0', '0014', '0020']
        """
        return [s[i:i + n] for i in range(0, len(s), n)]

    @staticmethod
    def replace_multiple_spaces_in_string(string):
        """
        This function take a string that can have multiple spaces between words as shown below
          "02:00:41:ff:ff:ff  4051      00bb.0000.4100   VSP4001           1/10             2000"
        and changes it to a string containing only one space between words:
         "02:00:41:ff:ff:ff 4051 00bb.0000.4100 VSP4001 1/10 2000"
        Caution:  This also replaces CRs, LFs, and Tabs.
        """
        return re.sub(r'\s+', ' ', string)

    @staticmethod
    def hex_str_to_dotted_decimal(hex_str):
        """
        This function takes a hex string in the form of "49.00.00", "49:00:00", "490000", or "0x490000"
        and converts it to a dotted decimal string
        Example: hex_to_dotted_decimal("49.00.00") returns: "73.0.0".
        """
        if hex_str.startswith("0x"):
            hex_str = hex_str[2::]
        ma = hex_str.replace('.', '').replace(":", '')
        ma = [ma[i:i + 2] for i in range(0, len(ma), 2)]
        return ".".join(str(x) for x in [int(x, 16) for x in ":".join(ma).split(':')])

    @staticmethod
    def hex_str_to_dotted_decimal_with_len(hex_str):
        """
        This function takes a hex string in the form of "49.00.00", "49:00:00", "490000", or "0x490000"
        and converts it to a dotted decimal string with the length identifier as the first decimal.
        Example: hex_to_dotted_decimal_with_len("49.00.00") returns: "3.73.0.0".
        """
        if hex_str.startswith("0x"):
            hex_str = hex_str[2::]
        ma = hex_str.replace('.', '').replace(":", '')
        ma = [ma[i:i + 2] for i in range(0, len(ma), 2)]
        length = len(ma)
        ma = ".".join(str(x) for x in [int(x, 16) for x in ":".join(ma).split(':')])
        return str(length) + '.' + ma

    @staticmethod
    def hex_str_to_int(s):
        """
        Converts a hex string to an integer string.
        Example: hex_str_to_int('0x0fa0') ==> '4000'
                 hex_str_to_int('fa0') ==> '4000'
        """
        if s.startswith("0x"):
            s = s[2::]

        if len(s) % 2 != 0:
            s = "0" + s
        try:
            i = int(s, 16)
            if i >= 2 ** 23:
                i -= 2 ** 24
            return str(i)
        except ValueError:
            return s

    @staticmethod
    def hex_str_to_ipv4_list(s):
        """Converts a hex string to a decimal IPv4 address list."""
        ip_list = []
        while len(s) > 0:
            ip_list.append(StringUtils.hex_str_to_dotted_decimal(s[:8]))
            s = s[8:]
        return ip_list

    @staticmethod
    def hex_str_to_ipv6_list(s):
        """Converts a hex string to an IPv6 address."""
        ip_list = []
        while len(s) > 0:
            # this needs to be changed to :
            ip_list.append(StringUtils.hex_str_to_dotted_decimal(s[:32]))
            s = s[32:]
        return ip_list

    @staticmethod
    def int_to_hex_str(i, add_0x=True, hex_min_size="1"):
        """
        Converts an integer string to a hex string.
        Example: int_to_hex_str('4000') ==> '0xfa0'
                 int_to_hex_str('4000', True) ==> '0xfa0'

        If minimum size of 2 octets (or 4 nibbles) is needed;
        Example: int_to_hex_str('4000', True, '2') ==> '0x0fa0'

        Examples for output to not use the 0x prefix:
        int_to_hex_str('4000', False) ==> 'fa0'
        int_to_hex_str('4000', False, '2') ==> '0fa0'
        """
        if add_0x:
            if hex_min_size == "1":
                return '0x' + str('%02x' % ((int(i) + 2 ** 24) % 2 ** 24))
            elif hex_min_size == "2":
                return '0x' + str('%04x' % ((int(i) + 2 ** 24) % 2 ** 24))
            else:
                return ValueError("Minimum size of the hex string only can be 1 or 2")
        else:
            if hex_min_size == "1":
                return str('%02x' % ((int(i) + 2 ** 24) % 2 ** 24))
            elif hex_min_size == "2":
                return str('%04x' % ((int(i) + 2 ** 24) % 2 ** 24))
            else:
                return ValueError("Minimum size of the hex string only can be 1 or 2")

    @staticmethod
    def insert_dot_every_four_characters(hex_string):
        """
        Inserts a dot for every fourth character in a hex string.
        Example: insert_dot_every_four_characters('0x0fa000140020') returns: '0fa0.0014.0020'
        """
        if hex_string.startswith("0x"):
            hex_string = hex_string[2::]
        return '.'.join(hex_string[i:i + 4] for i in range(0, len(hex_string), 4))

    @staticmethod
    def exos_port_list_to_ports(hex_string):
        """
        This function takes a port list address and converts it to the actual port number.
        For example 0x00440000000000000000000000000000 would be converted to 10 and 14.
        """
        if len(hex_string) > 34:
            my_string = bin(int(hex_string, base=16))[2:].zfill((len(hex_string) - 2) * 4 + 1)
            p = [i for i, x in enumerate(my_string) if x == "1"]
            new = []
            for x in p:
                if (x > 0) and (x < 129):
                    new.append('1:' + str(x))
                elif (x > 128) and (x < 257):
                    new.append('2:' + str(x - 128))
                elif (x > 256) and (x < 385):
                    new.append('3:' + str(x - 256))
                elif (x > 384) and (x < 513):
                    new.append('4:' + str(x - 384))
                elif (x > 512) and (x < 641):
                    new.append('5:' + str(x - 512))
                elif (x > 640) and (x < 769):
                    new.append('6:' + str(x - 640))
                elif (x > 768) and (x < 897):
                    new.append('7:' + str(x - 768))
                elif (x > 896) and (x < 1025):
                    new.append('8:' + str(x - 896))
                elif (x > 1024) and (x < 1153):
                    new.append('9:' + str(x - 1024))
                elif (x > 1152) and (x < 1281):
                    new.append('10:' + str(x - 1152))
        else:
            my_string = bin(int(hex_string, base=16))[2:].zfill((len(hex_string) - 2) * 4 + 1)
            p = [i for i, x in enumerate(my_string) if x == "1"]
            new = []
            for x in p:
                if (x > 0) and (x < 129):
                    new.append(str(x))

        return '\r\n'.join(str(x) for x in new)

    @staticmethod
    def dec_to_ascii(dec_string):
        """
        This function takes a decimal string in the form of d+.d+.d+.d+.d+.d+ and converts it to ascii.
        For example 109.99.109.103.114 would be converted to mcmgr.
        """
        return "".join(str(x) for x in [chr(int(x)) for x in dec_string.split('.')])

    @staticmethod
    def ascii_to_dec(ascii_string):
        """
        This function takes an ascii string in the form of abc and converts it to a dotted decimal string.
        For example lacp would be converted to 108.97.99.112.
        """
        return ".".join(str(x) for x in [ord(str(x)) for x in ascii_string])

    @staticmethod
    def ascii_to_dec_with_len(ascii_string):
        """
        This function takes an ascii string in the form of abc and converts it to a dotted decimal string along with
        the length identifier at as the first decimal.
        For example lacp would be converted to 4.108.97.99.112.
        """
        dec_string = ".".join(str(x) for x in [ord(str(x)) for x in ascii_string])
        length = len(ascii_string)
        return str(length) + '.' + dec_string

    @staticmethod
    def hex_string_to_octet_string(hex_string):
        """
        This function takes a hex string formed as 0x0a3410a2, 0a3410a2, or a3410a2 and decodes it to an octet string.
        It also handles any : or . characters if they are present.
        For example 0a3410a2 would be converted to \x0a\x34\x10\xa2.
        """
        hex_decoder = codecs.getdecoder("hex_codec")

        hex_string = hex_string.replace(".", "").replace(":", "")
        if hex_string.startswith("0x"):
            hex_string = hex_string[2::]
        if len(hex_string) % 2 != 0:
            hex_string = "0" + hex_string

        return hex_decoder(hex_string)[0]

    @staticmethod
    def normalize_hex_string_to_0x_hex_expression(hex_string):
        """
        This function takes a hex string formed as 0a3410a2, a3410a2 and normalizes it to a hex string with a 0x prefix.
        It also handles any : or . characters if they are present.
        For example 0a.34.10a2 would be converted to "0x0a3410a2
        """
        hex_string = hex_string.replace(".", "").replace(":", "")
        if hex_string.startswith("0x"):
            hex_string = hex_string[2::]
        if len(hex_string) % 2 != 0:
            hex_string = "0" + hex_string

        return "0x" + hex_string.lower()

    @staticmethod
    def hex_string_to_bit_string(hex_string):
        """
        This function takes a hex string formed as 0x0a3410a2, 0a3410a2, or a3410a2 and converts it to a bit string.
        It also handles any : or . characters if they are present.
        For example 0a3410a2 would be converted to '1010001101000001000010100010'.
        """
        hex_string = hex_string.replace(".", "").replace(":", "")
        if hex_string.startswith("0x"):
            hex_string = hex_string[2::]
        if len(hex_string) % 2 != 0:
            hex_string = "0" + hex_string

        return bin(int(hex_string, base=16)).lstrip('0b')

    @staticmethod
    def ipaddr_to_pure_hex(addr, leading_zeroes=True):
        """
        This function takes either ipv4 or ipv6 address and converts it into a pure hex string.
        For example 10.10.10.5  would be converted to 0x0a0a0a05.
        """
        if ':' in addr:
            ipv6_addr = Ipv6Address(addr).to_string()

            if leading_zeroes:
                return '0x' + ipv6_addr.replace(':', '')
            else:
                expanded_ipv6_addr = ipv6_addr.split(":")
                for i in range(len(expanded_ipv6_addr)):
                    new_block = ""
                    for index, c in enumerate(expanded_ipv6_addr[i]):
                        if index == 0:
                            new_block = expanded_ipv6_addr[i]
                        elif index == len(expanded_ipv6_addr[i]) - 1:
                            expanded_ipv6_addr[i] = c
                            break

                        if c == "0":
                            new_block = new_block[1::]
                        else:
                            expanded_ipv6_addr[i] = new_block
                            break
                return '0x' + ":".join(expanded_ipv6_addr).replace(':', '')
        elif '.' in addr:
            return '0x' + ":".join(str(x) for x in ["{:02x}".format(int(x)) for x in addr.split('.')]).replace(':', '')
        else:
            return addr

    @staticmethod
    def hex_string_to_bytes(hex_string):
        """
        This function takes a hex string ("00AABBCC") and returns a non displayable string

        Ex. ([0x00, 0xAA, 0xBB, 0xCC])
        """
        bytes_string = StringUtils.place_character_every_n_characters(hex_string.replace(".", "").replace(":", "").
                                                                      replace(" ", ""), " ", 2)
        bytes_array = bytes_string.split(" ")
        byte_string = ""
        for byte in bytes_array:
            char_string = binascii.a2b_hex(byte)
            byte_string += char_string
        return byte_string

    @staticmethod
    def octet_string_to_date_and_time(octet_string):
        """
        This function takes an octet string representing the date and time and converts it to human readable form.
        For example 0x07e10b0f0e201300 would be converted to 11/15/17 14:32:19.
        """
        if len(octet_string) > 17 < 25:
            dts = octet_string.replace('0x', '')
            y = int(dts[:4], 16)
            mon = int(dts[4:6], 16)
            d = int(dts[6:8], 16)
            h = int(dts[8:10], 16)
            m = int(dts[10:12], 16)
            s = int(dts[12:14], 16)
            result = str(mon) + '/' + str(d) + '/' + str(str(y)[2:4]) + ' ' + str(h) + ':' + str(m) + ':' + str(s)
            return result
        else:
            return 'Error Date and Time String Used is Not Suitable.'

    @staticmethod
    def voss_portnum_only(ports):
        """
        This function take a VOSS port string, ex: "giabitEthernet 1/1", and returns only the port number.
        If passed just a port number, it will return back the port as-is.
        """
        ports = ListUtils.convert_to_list(ports)
        port_list = []
        for port in ports:
            port_list.append(port.split()[1] if " " in port else port)

        return port_list if len(port_list) > 1 else str(port_list[0])

    @staticmethod
    def voss_porttype_only(ports):
        """
        This function take a VOSS port string, ex: "giabitEthernet 1/1", and returns only the port type.
        If passed a non-VOSS port string, it will return back the port as-is.
        """
        ports = ListUtils.convert_to_list(ports)
        port_list = []
        for port in ports:
            port_list.append(port.split()[0] if " " in port else port)

        return port_list if len(port_list) > 1 else str(port_list[0])

    @staticmethod
    def get_slot_from_port_string(ports):
        """
        This function take a port string, ex: "gigabitEthernet 2/3",  "2/3", or "2:3" and returns only the slot number.
        If passed a port number like "3" which is typical of a non-stacked/non-slot system,
        it will return the slot number as 1.
        """
        ports = ListUtils.convert_to_list(ports)
        slot_list = []

        for port in ports:
            port = port.replace(":", "/")
            if "/" in port:
                slot_list.append(port.split()[1].split("/")[0] if " " in port else port.split("/")[0])
                return slot_list[0]
            else:
                return "1"

    @staticmethod
    def exception_to_string():
        """Re-formats the exception(s) to a simple string."""
        exc_type, exc_value, exc_traceback = sys.exc_info()
        rt_string = ""
        exc_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for l in exc_list:
            rt_string += str(l) + "\n"
        return rt_string

    @staticmethod
    def convert_seconds_to_elapsed_time(seconds):
        """
        This function takes a digit expressing a value of seconds and converts it to a human readable elapsed time.
        Example 1: convert_seconds_to_elapsed_time("79075") returns: "21:57:55".
        Example 2: convert_seconds_to_elapsed_time("87763") returns  "1d 0:22:43"
        """
        if seconds.isdigit():
            seconds = int(seconds)
            return str(datetime.timedelta(seconds=seconds)).replace("ay,", "").replace(" d", "d")
        else:
            return seconds

    @staticmethod
    def convert_elapsed_time_to_seconds(elapsed_time):
        """
        This function takes a days, hours, minutes, seconds expression in the form of "21:57:55" or "1d 00:22:43"
        and converts it to seconds.
        Example 1: convert_elapsed_time_to_seconds("21:57:55") returns: "79075".
        Example 2: convert_elapsed_time_to_seconds("1d:00:22:43") returns: "87763".
        """
        if ":" in elapsed_time:
            if "d" not in elapsed_time:
                h, m, s = [int(i) for i in elapsed_time.split(':')]
                return str(3600 * h + 60 * m + s)
            else:
                elapsed_time = elapsed_time.replace("d", "")
                d, h, m, s = [int(i) for i in elapsed_time.split(':')]
                return str(86400 * d + 3600 * h + 60 * m + s)
        else:
            return elapsed_time

    @staticmethod
    def convert_seconds_to_milliseconds(seconds):
        """
        This function takes a digit expressing a value in seconds and converts it to a millisecond value.
        Example: convert_seconds_to_milliseconds("9") returns: "9000".
        """
        if seconds.isdigit():
            return str(int(seconds) * 1000)
        else:
            return seconds

    @staticmethod
    def convert_milliseconds_to_seconds(milliseconds):
        """
        This function takes a digit expressing a value in milliseconds and converts it to a second value.
        Example: convert_milliseconds_to_seconds("9000") returns: "9".
        """
        if milliseconds.isdigit():
            return str(int(milliseconds) // 1000)
        else:
            return milliseconds


StringUtilsConstants = PacketConstants()
