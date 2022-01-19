import re
from extauto.common.Utils import Utils
from extauto.common.Cli import Cli


class Tshark:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()


    def tshark_capture(self, spawn, wlan_int, ch_num, bssid,count=1000):
        """
        :param spawn:
        :param wlan_int:
		:param ch_num:
		:param bssid:
        :param count:
        :return:
        """
        self.utils.print_info("Configuring MU as sniffer ")

        self.cli.send(spawn, "ifconfig " + str(wlan_int) + " down")
        self.cli.send(spawn, "iwconfig " + str(wlan_int) + " mode moniter")
        self.cli.send(spawn, "iwconfig " + str(wlan_int) + " channel " + ch_num)
        self.cli.send(spawn, " ifconfig " + str(wlan_int) + " up ")
        self.cli.send(spawn, "iwconfig " + str(wlan_int) + " channel " + ch_num)

        self.utils.print_info("Tshark capturing on interface : ", wlan_int)
        self.cli.send(spawn, "tshark -i " + str(wlan_int) + " -w" + " p1.pcap " + "-c " + str(count))
        command = "tshark -r " + "p1.pcap " + "-Y " + "\"wlan.addr == " + str(bssid) +"\"" + " -V | grep freq" + " --color=never"

        output = self.cli.send(spawn, command)
        self.utils.print_info("OUTPUT:", output)

        if "Channel frequency" not in output:
            return -1
        else:
            ch_freq = re.search(r'Channel frequency: (\d+)', output)
            self.utils.print_info("channel frequency is ", ch_freq.group(1))
            print ("channel frequency is", ch_freq.group(1))
            if ch_freq.group(1) == '5180':
                    return 1
            elif ch_freq.group(1) == '2412':
                    return 2
