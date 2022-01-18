import re
from ExtremeAutomation.Library.Utils.Lists.ObjectList import ObjectList
from ExtremeAutomation.Library.Utils.Lists.IntList import IntList
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress


class EnetAddressList(ObjectList):
    """
    Example: ipList = EnetAddressList("01:22:33-35,66:44:55:66")
             ipList = EnetAddressList("01:22:33-35,66:44:55:66;FF:EE:FF:11-22,EE-FF:23:23")
    """

    def __init__(self, ipstring):
        """
        Init function
        """
        super(EnetAddressList, self).__init__(ipstring)

    def parse_elements(self, str_list):
        """
        formats:
        - means a range
            example 00:44:55:66-67:88:88 will give you:
                00:44:55:66:88:88, 00:44:55:67:88:88
        , means a single int value in a mac
            example 00:44:55:66,99:88:88 will give you:
                00:44:55:66:88:88, 00:44:55:99:88:88
        , or ; means another mac address or mac address range when between macs
            example 00:44:55:66:88:88,00:11:22:33:44:55;00:11:22:33,35:44:66 will give you:
                00:44:55:66:88:88, 00:11:22:33:44:55, 00:11:22:33:44:66, 00:11:22:35:44:66
        """
        inner_array = []
        string = str_list.replace(" ", "")
        p = re.compile(r'([0-9A-F,;\-]+:[0-9A-F,;\-]+:[0-9A-F,;\-]+:[0-9A-F,;\-]+:[0-9A-F,;\-]+:[0-9A-F,;\-]+)[,;]')
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
            for s1 in sub1:
                for s2 in sub2:
                    for s3 in sub3:
                        for s4 in sub4:
                            for s5 in sub5:
                                for s6 in sub6:
                                    addy = (hex(s1)[2:].zfill(2) + ":" + hex(s2)[2:].zfill(2) + ":" +
                                            hex(s3)[2:].zfill(2) + ":" + hex(s4)[2:].zfill(2) + ":" +
                                            hex(s5)[2:].zfill(2) + ":" + hex(s6)[2:].zfill(2))
                                    inner_array.append(addy.upper())

        return inner_array

    def get_all_enetaddress(self):
        """
        This function returns a list of all MAC addresses in the EnetAddressList.
        """
        temp = []
        for elm in self.inner_array:
            temp.append(EnetAddress(elm))
        return temp

    def get_enetaddress(self, index):
        """
        This function returns the MAC address at the given index.
        """
        return EnetAddress(self.inner_array[index])
