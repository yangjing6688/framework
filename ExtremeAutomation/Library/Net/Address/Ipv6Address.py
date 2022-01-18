import re
import ipaddress  # pip install ipaddress
from ExtremeAutomation.Library.Net.Address.Address import Address


class Ipv6Address(Address):
    def __init__(self, address):
        super(Ipv6Address, self).__init__(address, 16)

    def to_string(self, collapsed=False):
        ipv6_addr = self.to_formated_string(16, "")
        if collapsed:
            ipv6_addr = ipaddress.ip_address(ipv6_addr)
        return str(ipv6_addr)

    def to_formated_string(self, string_format, delim):
        ret_string = "".join(str(hex(x)[2:]).zfill(2) for x in list(reversed(self.pkt_bytes)))
        return ':'.join([ret_string[i:i + 4] for i in range(0, len(ret_string), 4)])

    def parse_address(self, address):
        if isinstance(address, str) and address.startswith("0x"):
            address = address[2:]
        if not isinstance(address, int) and "::" in address:
            if address.endswith(":"):
                address += "0"
            if address.startswith(":"):
                address = "0" + address
            byteCount = 9 - len(address.split(":"))
            address = address.replace("::", ":0" * byteCount + ":")
        if isinstance(address, int):  # treat it as an integer
            hex_string = str(hex(address)).upper()[2:].zfill(self.length * 2)
            self.parse_address(hex_string)
        elif ":" in address:  # probably a mac address
            parts = address.split(':')
            index = self.length - 1
            for part in parts:
                part = str(part).zfill(4)
                self.pkt_bytes[index] = int((int(part, 16) & 0x0FF00) >> 8)
                self.pkt_bytes[index - 1] = int(int(part, 16) & 0x00FF)
                index -= 2
        elif len(address) == self.length * 2:  # probably hex string
            parts = Address.split_hex(address).split(" ")
            index = self.length - 1
            for part in parts:
                self.pkt_bytes[index] = int(part, 16)
                index -= 1

    @staticmethod
    def is_valid_ipv6(ip):
        """
        Validates IPv6 addresses.
        """
        pattern = re.compile(r"""
            ^
            \s*                         # Leading whitespace
            (?!.*::.*::)                # Only a single whildcard allowed
            (?:(?!:)|:(?=:))            # Colon iff it would be part of a wildcard
            (?:                         # Repeat 6 times:
                [0-9a-f]{0,4}           #   A group of at most four hexadecimal digits
                (?:(?<=::)|(?<!::):)    #   Colon unless preceeded by wildcard
            ){6}                        #
            (?:                         # Either
                [0-9a-f]{0,4}           #   Another group
                (?:(?<=::)|(?<!::):)    #   Colon unless preceeded by wildcard
                [0-9a-f]{0,4}           #   Last group
                (?: (?<=::)             #   Colon iff preceeded by exacly one colon
                 |  (?<!:)              #
                 |  (?<=:) (?<!::) :    #
                 )                      # OR
             |                          #   A v4 address with NO leading zeros
                (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)
                (?: \.
                    (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)
                ){3}
            )
            \s*                         # Trailing whitespace
            $
        """, re.VERBOSE | re.IGNORECASE | re.DOTALL)
        return pattern.match(ip) is not None

    @staticmethod
    def to_long_upper(ip):
        if isinstance(ip, str):
            if Ipv6Address.is_valid_ipv6(ip):
                ip = Ipv6Address(ip)
        ip = ip.to_formated_string(16, "").replace(":", "")
        return int("0x" + ip[:16], 16)

    @staticmethod
    def to_long_lower(ip):
        if isinstance(ip, str):
            if Ipv6Address.is_valid_ipv6(ip):
                ip = Ipv6Address(ip)
        ip = ip.to_formated_string(16, "").replace(":", "")
        return int("0x" + ip[16:], 16)
