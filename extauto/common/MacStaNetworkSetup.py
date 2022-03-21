import time
import re
from extauto.common.Cli import Cli
from extauto.common.Utils import Utils

class MacStaNetworkSetup(object):
    def __init__(self):
        self.Cli               = Cli()
        self.utils             = Utils()
        self.spawn             = None
        self.wifi_interface    = 'en1'
        self.userkeychain_path = '/Users/admin/Library/Keychains/login.keychain'
        self.syskeychain_path  = '/Library/Keychains/System.keychain'

    def open_mac_sta(self, ip, user, password="aerohive"):
        """
        - Creating ssh spawn object
        - Keyword Usage:
        - ``Open Mac Sta   ${HOST}  ${USERNAME}  ${PASSWORD}``

        :param host: IP or host name of DUT
        :param username: username to access Spawn
        :param password: password to access Spawn
        :return: returns spawn else -1
        """
        self.spawn = self.Cli.open_paramiko_ssh_spawn(ip, user, password)
        return self.spawn

    def close_mac_sta(self):
        """
        - Closes Mac Station spawn object
        - Keyword Usage:
         - ``Close Mac Sta    ${SPAWN}``
        """
        self.Cli.close_paramiko_spawn(self.spawn)

    def send_mac_sta(self, cmd, timeout=10):
        """
        - Execute the commands on ssh spawn
        - Keyword Usage:
         - ``Send Paramiko Cmd   ${SPAWN}  ${COMMAND}``
         - ``Send Paramiko Cmd   ${SPAWN}  ${COMMAND}  timeout=${TIMEOUT_VALUE}``

        :param cmd: command to send
        :param timeout: command timeout
        :return: -1 in case of error else output of command
        """
        self.Cli.send_paramiko_cmd(self.spawn, cmd, 10)

    def sta_connect_to_wpa2_aes_psk_ssid(self, ssid, key='Aerohive123', **kwargs):
        """connect to wpa2 _aes_psk ssid.

        :param str ssid: the ssid to be connected
        :param str key : the key of the ssid
        :returns: return true or alert failed

        Example::


        | sta_connect_to_wpa2_aes_psk_ssid | yourssid | yourpassword |

         For negative test

        | sta_connect_to_wpa2_aes_psk_ssid |yourssid | yourpassword | negative = True|

         when there are no need to get ip

        |sta_connect_to_wpa2_aes_psk_ssid  | yourssid | yourpassword|  dhcpcheck = False|
        """
        negative = kwargs.get('negative', False)
        dhcpcheck = kwargs.get('dhcpcheck', True)
        dhcpcheck = self._parse_bool_item(dhcpcheck)
        negative = self._parse_bool_item(negative)
        self._reset_wifi_interface()
        if not negative:
            scan_result = self._sta_loop_check_ssid(ssid)
            if not scan_result:
                raise AssertionError("Can not scan thst  ssid please check!")
        join_cmd = 'networksetup -setairportnetwork ' + self.wifi_interface + " " + "\"" + ssid + "\"" + " " + key
        result = self._connect_to_ssid(join_cmd, ssid, negative, dhcpcheck)
        ReturnResult = self._get_return_result(result, negative)
        return ReturnResult

    def sta_get_wifi_interface(self):
        """
        - Return the device name of wifi interface

        :returns: device name or error

        Example::

        | ${wifi_interface}= | sta_get_wifi_interface |
        """

        out = self.Cli.send_paramiko_cmd(self.spawn, 'networksetup -listallhardwareports | grep -i -A3 wi-fi')
        m = re.search("Device:\s+([\w]+)", out)
        if m:
            return m.group(1)
        else:
            raise NotFoundKeyword("Can not get ip address for interface \'" + self.wifi_interface + "\'.")

    def sta_remove_preferred_network(self, wifi_interface):
        """
        - Remove preferred networt setting on station.
        """
        self.wifi_interface = self.sta_get_wifi_interface()
        out = self.Cli.send_paramiko_cmd(self.spawn, 'networksetup -removeallpreferredwirelessnetworks ' + wifi_interface)
        if 'Unable to commit systemconfig database' in out:
            self.utils.print_info("Please log into client as root")
            return 0
        else:
            self.utils.print_info("Successfully remove preferred wireless networks list")
            return 1

    def sta_check_ssid(self, ssid):
        out = self.Cli.send_paramiko_cmd(self.spawn, 'airport -s \"' + ssid + '\"', timeout=60)
        lines = out.split('\n')
        for line in lines:
            m = re.search(r"No networks found", line)
            if m:
                return False

        return True

    def _parse_bool_item(self, item):
        if isinstance(item, str):
            if item.upper() == 'TRUE':
                return True
            elif item.upper() == 'FALSE':
                return False
            else:
                raise ValueError("input string invaid,just support ture or false!")
        elif isinstance(item, bool):
            return item
        raise ValueError("input value  type error!")

    def _reset_wifi_interface(self):
        interface = self.sta_get_wifi_interface()
        self.wifi_interface = interface
        self.Cli.send_paramiko_cmd(self.spawn, 'wl up')
        time.sleep(1)
        self.Cli.send_paramiko_cmd(self.spawn, 'networksetup -setairportpower ' + interface + ' off')
        self.Cli.send_paramiko_cmd(self.spawn, 'networksetup -setairportpower ' + interface + ' on')
        time.sleep(10)
        self.sta_remove_preferred_network(self.wifi_interface)
        self.Cli.send_paramiko_cmd(self.spawn, 'wl disassoc')
        self.Cli.send_paramiko_cmd(self.spawn, "networksetup -setnetworkserviceenabled Wi-Fi on")

    def _sta_loop_check_ssid(self, ssid, looptimes=5):
        scan_loop = 0
        while scan_loop < looptimes:
            if self.sta_check_ssid(ssid):
                return True
            else:
                time.sleep(6)
                scan_loop += 1
        return False

    def _connect_to_ssid(self, join_cmd, ssid, negative, dhcpcheck):
        self.Cli.send_paramiko_cmd(self.spawn, join_cmd, timeout=110)
        time.sleep(1)
        scan_loop = 1
        if negative:
            loop_cnt_wlstatus = 2
        else:
            loop_cnt_wlstatus = 10
        loop_cnt_ip_route = 5
        connect_flag = "False"
        auth_flag = "False"
        flag = 'False'
        while scan_loop < loop_cnt_wlstatus and connect_flag == "False":
            self.Cli.send_paramiko_cmd(self.spawn, join_cmd, timeout=60)
            output = self.Cli.send_paramiko_cmd(self.spawn, 'networksetup -getairportnetwork ' + self.wifi_interface)
            if re.search(ssid, output, re.IGNORECASE):
                connect_flag = "True"
            else:
                time.sleep(5)
                scan_loop += 1

        # add by Tony to check whether station get ip address
        # modified  by Fran to use ipconfig to get ip
        scan_loop = 1
        ver = self.__get_os_version()
        while scan_loop < loop_cnt_ip_route and connect_flag == "True" and auth_flag == "False" and dhcpcheck is True:
            if ver < 100905:
                wifi_output = self.Cli.send_paramiko_cmd(self.spawn, 'ifconfig ' + self.wifi_interface)
                if re.search("inet\s+[\d.]+\s+netmask", wifi_output, re.IGNORECASE) and "inet 169" not in wifi_output:
                    auth_flag = "True"
                else:
                    time.sleep(14)
                    scan_loop += 1
            else:
                wifi_output = self.Cli.send_paramiko_cmd(self.spawn, 'ipconfig getpacket ' + self.wifi_interface)
                if re.search("yiaddr =\s+[\d.]+", wifi_output, re.IGNORECASE) and (
                re.search("giaddr =\s+[\d.]+", wifi_output, re.IGNORECASE)):
                    auth_flag = "True"
                else:
                    time.sleep(14)
                    scan_loop += 1
        if dhcpcheck is not True:
            auth_flag = "True"
        if (connect_flag == 'True') and (auth_flag == 'True'):
            flag = 'True'

        return (flag)

    def __get_os_version(self):
        """
        retrive mac os version number, convert the version to integer,
        return the integer of the version
        """
        out = self.Cli.send_paramiko_cmd(self.spawn, '/usr/bin/sw_vers')
        ver = re.search('ProductVersion:\s+([\d.]+).*', out)
        ver_val = 0
        if ver != None:
            ver_str = ver.group(1)
            ver_lst = ver_str.split('.')
            ver_val = int(ver_lst[0]) * 10000 + int(ver_lst[1]) * 100
            if len(ver_lst) > 2:
                ver_val = ver_val + int(ver_lst[2])
        return ver_val

    def _get_return_result(self, connect_flag, negative):
        if connect_flag == "False":
            if  negative is False:
                raise AssertionError('Failed to join ')
            else:
                return(True)
        else:
            if  negative is False:
                return(True)
            else:
                 raise AssertionError('should not join ')


from robot.errors import RobotError
from robot import utils

class ExtremeExceptions(RobotError):
    """Used for communicating failures in test execution."""

    def __init__(self, message):
        if '\r\n' in message:
            message = message.replace('\r\n', '\n')
        RobotError.__init__(self, self._format_message(utils.cut_long_message(message)))

    def _format_message(self, messages):
        messages = 'AeroLibrary failures occurred: \n' + messages
        return messages

class InvalidAHCli(ExtremeExceptions):
    pass

class InvalidParameter(ExtremeExceptions):
    pass

class NotFoundKeyword(ExtremeExceptions):
    pass
