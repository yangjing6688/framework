import re
from ExtremeAutomation.Library.Utils.Lists.ObjectList import ObjectList
from ExtremeAutomation.Library.Utils.Lists.IntList import IntList
from ExtremeAutomation.Library.Net.Address.Ipv6Address import Ipv6Address


class IpV6List(ObjectList):
    """
    Example:
        ipList = IpV6List("2001:0db8-0dbf:85a3,FFFF::8a2e:0370:7334,2001:0db8-0dbf:85a3,FFFF:0000:0000:8a2e:0370:7334")
    """

    def __init__(self, ipstring):
        """
        Init function
        """
        super(IpV6List, self).__init__(ipstring)

    def parse_elements(self, str_list):
        """
        formats:
        - means a range
            example FF01:8888::0001-0003 will give you:
                FF01:8888:0000:0000:0000:0000:0000:0001,
                FF01:8888:0000:0000:0000:0000:0000:0002,
                FF01:8888:0000:0000:0000:0000:0000:0003
        ,   means a single int value in an ipv6
            example FF01,FF0A:8888::0001 will give you:
                FF01:8888:0000:0000:0000:0000:0000:0001, FF0A:8888:0000:0000:0000:0000:0000:0001
        ; means another ipv6 address or ipv6 address range when between ips
            example FF01,FF0A:8888::0001;FF01,FF0A:8888::00AA will give you:
                FF01:8888:0000:0000:0000:0000:0000:0001,
                FF0A:8888:0000:0000:0000:0000:0000:0001,
                FF0A:8888:0000:0000:0000:0000:0000:00AA
        """
        inner_array = []
        string = str_list.replace(" ", "")
        if "::" in string:
            comma_tokens = string.split(";")
            string = ""
            for elm in comma_tokens:
                if "::" in elm:
                    if elm.startswith("::"):
                        elm = "0000" + elm
                    if elm.endswith("::"):
                        elm = elm + "0000"
                    needed = 7 - elm.count(':') + 1
                    string_to_replace = ":" + ("0000:" * needed)
                    elm = elm.replace("::", string_to_replace)

                    string += elm + ";"
                string += elm + ";"
            string = string[:-1]

        p = re.compile(r'([0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+:' +
                       r'[0-9A-F,\-]+)[;]')
        comma_tokens = p.split(string)

        for elm in comma_tokens:
            if elm == '':
                continue
            subnets = elm.split(":")
            sub1 = IntList(subnets[0], 16).get_all()
            sub2 = IntList(subnets[1], 16).get_all()
            sub3 = IntList(subnets[2], 16).get_all()
            sub4 = IntList(subnets[3], 16).get_all()
            sub5 = IntList(subnets[4], 16).get_all()
            sub6 = IntList(subnets[5], 16).get_all()
            sub7 = IntList(subnets[6], 16).get_all()
            sub8 = IntList(subnets[7], 16).get_all()
            for s1 in sub1:
                for s2 in sub2:
                    for s3 in sub3:
                        for s4 in sub4:
                            for s5 in sub5:
                                for s6 in sub6:
                                    for s7 in sub7:
                                        for s8 in sub8:
                                            addy = (hex(s1)[2:].zfill(4) + ":" + hex(s2)[2:].zfill(4) + ":" +
                                                    hex(s3)[2:].zfill(4) + ":" + hex(s4)[2:].zfill(4) + ":" +
                                                    hex(s5)[2:].zfill(4) + ":" + hex(s6)[2:].zfill(4) + ":" +
                                                    hex(s7)[2:].zfill(4) + ":" + hex(s8)[2:].zfill(4))
                                            inner_array.append(addy.upper())

        return inner_array

    def get_all_ipv6address(self):
        """
        This function returns a list of all IPv6 addresses in the IPv4List.
        """
        temp = []
        for elm in self.inner_array:
            temp.append(Ipv6Address(elm))
        return temp

    def get_ipv6address(self, index):
        """
        This function returns the IPv6 address at the given index.
        """
        return Ipv6Address(self.inner_array[index])
