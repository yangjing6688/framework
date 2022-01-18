from ExtremeAutomation.Library.Net.Address.Address import Address
import re


class EnetAddress(Address):
    def __init__(self, address):
        super(EnetAddress, self).__init__(address, 6)

    def to_string(self):
        return self.to_formated_string(16, ":")

    def equals(self, other_mac, mask=None):
        o1 = EnetAddress.to_long(self)
        o2 = EnetAddress.to_long(other_mac)
        if mask:
            oMask = EnetAddress.to_long(mask)
        else:
            oMask = 0
        oMask = ~oMask
        return (o1 & oMask) == (o2 & oMask)

    @staticmethod
    def to_long(mac):
        if not isinstance(mac, EnetAddress):
            mac = EnetAddress(mac)
        return int(mac.to_formated_string(16, ""), 16)

    @staticmethod
    def is_valid_enet(ip):
        """
        Validates IPv4 addresses.
        """
        pattern = re.compile(r'^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$', re.VERBOSE | re.IGNORECASE)
        return pattern.match(ip) is not None
