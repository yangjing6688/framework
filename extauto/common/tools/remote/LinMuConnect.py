import subprocess
import re
from time import sleep


class LinMuConnect:
    def __init__(self):
        pass

    @property
    def _get_wlan_interface_name(self):
        """
        Get the wlan interface name, Assuming below is the output format
        phy#0
        Interface wlan0
                ifindex 3
                type managed
        wlan0 is the common name for wireless interface
        :return:
        """
        print("cmd: sudo iw dev")
        cmd_out = self.execute_commands('sudo iw dev')
        print("Output:{}".format(' '.join(cmd_out)))
        for value in cmd_out:
            if re.search(r'Interface', value.strip()):
                interface = re.search(r'(Interface )(\w+)', value).group(2)
                print("Wlan INterface is: {}".format(interface))
                return interface

    def search_network(self, ssid, interface):
        """
        This keyword search for network
        :param ssid: name of the ssid to scan
        :param interface: name of the wlan interface
        :return: 1 if success
        """
        cmd_list = ['sudo ifconfig ' + interface + ' down',
                    'sleep 2',
                    'sudo ifconfig ' + interface + ' up',
                    'sleep 10',
                    'sudo iw ' + interface + ' scan ' + ' | grep ' + ssid,
                    'sleep 5',
                    ]
        retry = 0
        while retry < 5:
            print("cmd:{}".format(";".join(cmd_list)))
            cmd_out = self.execute_commands(";".join(cmd_list))
            print("cmd_out: {}".format(cmd_out))
            if ssid in "".join(cmd_out):
                return 1
            else:
                sleep(10)
                retry += 1

    def connect_open_network(self, ssid):
        """
        Connects open authentication network
        :param ssid: name of the ssid to connect
        :return: 1 if success
        """
        _interface = self._get_wlan_interface_name
        cmd = ['sudo iw dev ' + _interface + ' connect ' + ssid]
        if not self.search_network(ssid, _interface):
            return "SSID not available in scanned list"

        print(cmd)
        self.execute_commands(cmd)
        sleep(10)
        output = self.execute_commands('iwconfig')
        connect_status = None
        for line in output:
            if "Link Quality" in line:
                connect_status = True
            print(line)
        if connect_status:
            if self.get_wi_fi_interface_ip_address:
                return 1
            if self.get_dhcp_ip:
                return 1
        return -1

    def connect_psk_network(self, ssid=None, key=None):
        """
        Connects to psk network
        :param ssid: ssid
        :param key: ssid keys
        :return: none
        """
        # Update the config file
        self.execute_commands('echo  network={ >psk.conf')
        self.execute_commands('echo  ssid=\"' + ssid + '">>psk.conf')
        self.execute_commands('echo  psk=\"' + key + '"}>>psk.conf')

    def disconnect_wi_fi(self):
        """
        Disconnects from wi-fi
        :return:
        """
        cmds = ['sudo iw dev wlan0 disconnect',
                'sleep 2',
                'pkill dhclient',
                'sleep 2',
                'pkill wpa_supplicant'
               ]
        print(";".join(cmds))
        self.execute_commands(";".join(cmds))

    def check_internet_connectivity(self):
        """
        - Check MU machine Internet connectivity with curl and Firefox detect portal
        - Keyword Usage:
        - ``MU1.Check Internet Connectivity``

        :return: 1 if Internet is available, else -1
        """
        cmd = 'curl http://detectportal.firefox.com/success.txt'
        curl_out = self._execute_commands(cmd)
        if (len(curl_out) == 1) and re.fullmatch('success', curl_out[0]):
            return 1
        else:
            return -1

    @property
    def get_dhcp_ip(self):
        """
        Gets DHCP IP
        :return:
        """
        _interface = self._get_wlan_interface_name
        dhcp_release_command = 'dhclient ' + _interface + ' -r -v'
        dhcp_command = 'dhclient ' + _interface + ' -v'
        self.execute_commands(dhcp_release_command)
        sleep(10)
        self.execute_commands(dhcp_command)
        sleep(10)
        if self.get_wi_fi_interface_ip_address:
            return True

    @property
    def get_wi_fi_interface_ip_address(self):
        """
        Gets WiFi Interface IP addresss
        :return:
        """
        _interface = self._get_wlan_interface_name

        cmd = 'ifconfig ' + _interface
        cmd_out = self.execute_commands(cmd)
        ip = None
        for line in cmd_out:
            if re.search(r'inet addr:\d+.\d+.\d+.\d+', line):
                ip = re.search(r'inet addr:\d+.\d+.\d+.\d+', line).group().split(':')[-1]
                print(ip)
                break
        return ip

    @staticmethod
    def execute_commands(cmd):
        """
        Execute command on windows command line using subprocess module
        :param cmd: command to execute
        :return: cmd_out of the command
        """
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_out = []
        for line in process.stdout:
            cmd_out.append(line.decode().strip())
        return cmd_out


if __name__ == "__main__":
    obj = LinMuConnect()
    obj.connect_psk_network("Hanamants", "SGSGS")
    obj.connect_open_network('OPEN_HS_DEMO')