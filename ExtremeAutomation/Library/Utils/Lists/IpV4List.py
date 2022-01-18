import re
from ExtremeAutomation.Library.Utils.Lists.IntList import IntList
from ExtremeAutomation.Library.Utils.Lists.ObjectList import ObjectList
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address


class IpV4List(ObjectList):
    """
    Example: ipList = IpV4List("1.1.1-2,4.1, 3.3.3.3;4.4.4-10.4")
             ipList = IpV4List("1.1.1-2,4;7,7;3-6.1, 3.3.3.3;4.4.4-10.4")
    """

    def __init__(self, ipstring):
        """
        Init function
        """
        super(IpV4List, self).__init__(ipstring)

    def parse_elements(self, str_list):
        """
        formats:
        - or : means a range
            example 1.1.1-2.3-4 will give you:
                1.1.1.3, 1.1.1.4, 1.1.2.3, 1.1.2.4
        , or ;  means a single int value in an ip
            example 1.1.1;6.3,8 will give you:
                1.1.1.3, 1.1.1.8, 1.1.6.3, 1.1.6.8
        , or ; means another ip address or ip address range when between ips
            example 192.168.1.1,1.1.1-2.3-4;2.2.2.2-4 will give you:
                192.168.1.1, 1.1.1.3, 1.1.1.8, 1.1.6.3, 1.1.6.8, 2.2.2.2, 2.2.2.3, 2.2.2.4
        """
        inner_array = []
        string = str_list.replace(" ", "")
        string = string.replace(":", "-")
        p = re.compile(r'([0-9,;\-]+\.[0-9,;\-]+\.[0-9,;\-]+\.[0-9,;\-]+)[,;]')
        comma_tokens = p.split(string)

        for elm in comma_tokens:
            if elm == '':
                continue
            subnets = elm.split(".")
            sub1 = IntList(subnets[0]).get_all()
            sub2 = IntList(subnets[1]).get_all()
            sub3 = IntList(subnets[2]).get_all()
            sub4 = IntList(subnets[3]).get_all()
            for s1 in sub1:
                for s2 in sub2:
                    for s3 in sub3:
                        for s4 in sub4:
                            addy = str(s1) + "." + str(s2) + "." + str(s3) + "." + str(s4)
                            inner_array.append(addy)

        return inner_array

    def get_all_ipv4address(self):
        """
        This function returns a list of all IP addresses in the IPv4List.
        """
        temp = []
        for elm in self.inner_array:
            temp.append(Ipv4Address(elm))
        return temp

    def get_ipv4address(self, index):
        """
        This function returns the IP address at the given index.
        """
        return Ipv4Address(self.inner_array[index])
