import re
from ExtremeAutomation.Library.Net.Address.Address import Address


class Ipv4Address(Address):
    def __init__(self, address):
        super(Ipv4Address, self).__init__(address, 4)

    def to_string(self):
        return self.to_formated_string(10, ".")

    @staticmethod
    def is_valid_ipv4(ip):
        """
        Validates IPv4 addresses.
        """
        pattern = re.compile(r"""
            ^
            (?:
              # Dotted variants:
              (?:
                # Decimal 1-255 (no leading 0's)
                [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
              |
                0x0*[0-9a-f]{1,2}  # Hexadecimal 0x0 - 0xFF (possible leading 0's)
              |
                0+[1-3]?[0-7]{0,2} # Octal 0 - 0377 (possible leading 0's)
              )
              (?:                  # Repeat 0-3 times, separated by a dot
                \.
                (?:
                  [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
                |
                  0x0*[0-9a-f]{1,2}
                |
                  0+[1-3]?[0-7]{0,2}
                )
              ){0,3}
            |
              0x0*[0-9a-f]{1,8}    # Hexadecimal notation, 0x0 - 0xffffffff
            |
              0+[0-3]?[0-7]{0,10}  # Octal notation, 0 - 037777777777
            |
              # Decimal notation, 1-4294967295:
              429496729[0-5]|42949672[0-8]\d|4294967[01]\d\d|429496[0-6]\d{3}|
              42949[0-5]\d{4}|4294[0-8]\d{5}|429[0-3]\d{6}|42[0-8]\d{7}|
              4[01]\d{8}|[1-3]\d{0,9}|[4-9]\d{0,8}
            )
            $
        """, re.VERBOSE | re.IGNORECASE)
        return pattern.match(ip) is not None

    @staticmethod
    def to_long(ip):
        if isinstance(ip, int):
            return ip
        if isinstance(ip, str):
            if Ipv4Address.is_valid_ipv4(ip):
                ip = Ipv4Address(ip)
            return int("0x" + ip.to_formated_string(16, ""), 16)
        if isinstance(ip, Ipv4Address):
            return int("0x" + ip.to_formated_string(16, ""), 16)
