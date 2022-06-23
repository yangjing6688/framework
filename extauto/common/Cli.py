import re
import sys
import time
import shlex
import pexpect
import paramiko
import subprocess
import uuid
from platform import system
from netmiko import ConnectHandler
from extauto.xiq.configs.device_commands import *
from robot.libraries.BuiltIn import BuiltIn
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend
from ExtremeAutomation.Keywords.EndsystemKeywords.EndsystemConnectionManager import EndsystemConnectionManager

from extauto.common.Utils import Utils

if "Window" not in system():
    from pexpect.pxssh import ExceptionPxssh
    from pexpect import pxssh


class Cli(object):

    def __init__(self):
        self.dut_platform = -1
        self.aerohive_default_password = 'aerohive'
        self.utils = Utils()
        self.builtin = BuiltIn()
        self.networkElementConnectionManager = NetworkElementConnectionManager()
        self.networkElementCliSend = NetworkElementCliSend()
        self.endsystemConnectionManager = EndsystemConnectionManager()

        self.net_element_types = ['VOSS', 'EXOS', 'WING-AP', 'AH-FASTPATH', 'AH-AP', 'AH-XR']
        self.end_system_types = ['MU-WINDOWS', 'MU-MAC', 'MU-LINUX', 'A3']

    def close_spawn(self, spawn, **kwargs):
        """
        - Closes a device spawn
        - Keyword Usage:
         - ``Close Spawn``

        :param spawn: device spawn
        :return: 1 if device spawn closed successfully else -1
        """

        if spawn.split('_')[1].upper() in self.net_element_types:
            self.networkElementConnectionManager.close_connection_to_network_element(spawn)
        elif spawn.split('_')[1].upper() in self.end_system_types:
            self.endsystemConnectionManager.close_connection_to_endsystem_element(spawn)
        else:
            raise Exception("Cli_Type was not found, please use on of the following type: \n" + '\n'.join(self.net_element_types) + '\n' + '\n'.join(self.end_system_types))



    def set_platform(self, platform):  # if spawn == -9:
        #     return -9
        #
        # if spawn == -1:
        #     self.utils.print_info("Device Spawn is not Opened Successfully. So Unable to Close the Spawn.")
        #     return -1
        #
        # self.utils.print_info("\nClosing Connection...")
        # try:
        #     spawn.close()
        #     return 1
        # except Exception as e:
        #     self.utils.print_info(e)
        #     return -1
        """
        - Sets the self.dut_platform with platform
        - Keyword Usage:
         - ``Set Platform  ${DEVICE_PLATFORM}``

        :param platform: DUT platform wing, identify, aerohive or linux
        :return: None
        """
        self.utils.print_info("Setting Platform to : ", platform)
        self.dut_platform = platform

    def get_platform(self):
        """
        - Gets the Device Platform and assign it to self.dut_platform.
        - Keyword Usage:
         - ``Get Platform``

        :return: platform - DUT platform wing, identify, aerohive or linux
        """
        self.utils.print_info("Returning Platform to : ", self.dut_platform)
        return self.dut_platform

    def open_ssh_spawn(self, ip, username, password, port="default"):
        """
        - This Keyword used to access device/host ssh Using IP Address,username,password and port number
        - Note :This Keyword Internally calls "open_pxssh_spawn" Keyword.So Suggest to use "open_pxssh_spawn" Keyword Directly
        - Keyword Usage:
         - ``Open SSH Spawn     ${IP}   ${USERNAME}  ${PASSWORD}``
         - ``Open SSH Spawn     ${IP}   ${USERNAME}  ${PASSWORD}   _port=22``

        :param ip: SSH spawn IP address
        :param username: User Name for ssh access
        :param password: Password for ssh access
        :param port: port number for ssh access
        :return: Device or Host SSH Spawn
        """
        if port == "default":
             return self.open_pxssh_spawn(ip, username, password, _port=22)
        else:
            self.utils.print_info("SSH Port:", port)
            return self.open_pxssh_spawn(ip, username, password, _port=int(port))

    def open_spawn(self, ip, port, username, password, cli_type, connection_method='ssh'):
        """
        - This Keyword used to access device/host Prompt Using IP Address,port number, username,password and cli_type
        # Device type:
            - VOSS
            - EXOS
            - WING-AP
            - AH-FASTPATH
            - AH-AP
            - AH-XR
        # Endsystem:
            - MU-WINDOWS
            - MU-MAC
            - MU-LINUX
            - A3
        - Keyword Usage:
         - ``Open Spawn     ${IP}   ${PORT}  ${USERNAME}  ${PASSWORD}   ${cli_type}``

        :param ip: Device IP address
        :param port: port number for spawn access
        :param username: User Name for spawn access
        :param password: Password for spawn access
        :param cli_type: Device Cli Type
        :param connection_method: The connection type, will default to ssh. (ssh, telnet, console)

        :return: Device Prompt
        """
        self.utils.print_info("=================================")
        self.utils.print_info("IP: ", ip)
        self.utils.print_info("PORT: ", port)
        self.utils.print_info("Username: ", username)
        self.utils.print_info("Password: ", password)
        self.utils.print_info("Cli Type: ", cli_type)
        self.utils.print_info("=================================")

        # Generate UUID
        device_uuid = str(uuid.uuid4()) + "_" + cli_type
        if cli_type.upper() in self.net_element_types:
            self.networkElementConnectionManager.connect_to_network_element(device_uuid, ip, username, password, connection_method, cli_type.upper(), port=port)
        elif cli_type.upper() in self.end_system_types:
            self.endsystemConnectionManager.connect_to_endsystem_element(device_uuid, ip, username, password, connection_method, cli_type.upper(), port=port)
        else:
            raise Exception("Cli_Type was not found, please use on of the following type: \n" +  '\n'.join(
                self.net_element_types) + '\n' + '\n'.join(self.end_system_types))
        # The calls to the connect_to_<device> will check the cli_type to ensure that the correct type value was passed in and will error out in the case that
        # an unknown value was passed in.
        return device_uuid


        # _out = -1
        # ssh = False
        # if port == '-1':
        #     return -9
        #
        # self.set_platform(platform)
        # self.utils.print_info("Pinging the IP : ", ip)
        #
        # # try to ping to destination
        # p_count = 0
        # while p_count < 3:
        #     _cmd = "ping -c 2 %s" % str(ip)
        #     #self.utils.print_info("CMD: ", _cmd)
        #     _out =subprocess.check_output([_cmd], shell = True)
        #     if " 0% packet loss" in str(_out):
        #         break
        #     p_count += 1
        #
        # if " 0.0% packet loss"  or " 0% packet loss"in str(_out):
        #     self.utils.print_info("Ping received successfully...")
        # else:
        #     self.utils.print_info("Unable to reach the DUT/MU")
        #     return -1
        #
        # conn_str = 'telnet ' + ip + " " + str(port)
        # if (str(port) == '22') or (str(port) == '8554'):
        #     self.utils.print_info("Opening SSH Spawn...")
        #     conn_str = 'ssh ' + username + "@" + ip + " -p " + str(port) + " -o StrictHostKeyChecking=no"
        #     self.utils.print_info("SSH conn_str: ", conn_str)
        #     ssh = True
        #     self.ssh = True
        # password_default = "admin123"
        # password_cloud_default = "symbol123"
        #
        # if platform == "win":
        #     return self.open_windows_spawn(conn_str, username, password)
        #
        # elif platform == "linux":
        #     retry_count = 0
        #     spawn = pexpect.spawnu(conn_str)
        #     spawn.logfile = sys.stdout
        #     self.utils.print_info("Connecting to Linux Host")
        #
        #     while retry_count < 10:
        #         self.utils.print_info("Loop: ", retry_count)
        #         i = spawn.expect(['login:',
        #                           'assword:',
        #                           'yes/no',
        #                           '#',
        #                           'Login incorrect',
        #                           '>',
        #                           pexpect.TIMEOUT,
        #                           pexpect.EOF], timeout=90)
        #         if i == 0:
        #             self.utils.print_info("Sending Username: ", username)
        #             spawn.sendline(username)
        #             time.sleep(2)
        #             spawn.expect('assword:', timeout=30)
        #             time.sleep(2)
        #             spawn.sendline(password)
        #             time.sleep(10)
        #             j = spawn.expect('#', timeout=60)
        #             if j == 0:
        #                 return spawn
        #             if j == 1:
        #                 self.utils.print_info("Timeout Exiting...")
        #                 continue
        #
        #         if i == 1:
        #             self.utils.print_info("SSH Detected...")
        #             spawn.sendline(password)
        #             time.sleep(5)
        #             j = spawn.expect(['#', '>'], timeout=60)
        #             if j == 0:
        #                 self.utils.print_info("Got Prompt. Returning Spawn...")
        #                 return spawn
        #
        #             if j == 1:
        #                 self.utils.print_info("Got Prompt. Returning Spawn...")
        #                 return spawn
        #
        #             if j == 2:
        #                 self.utils.print_info("Timeout Exiting...")
        #                 continue
        #
        #         if i == 2:
        #             time.sleep(1)
        #             spawn.sendline("yes")
        #             continue
        #
        #         if i == 3:
        #             time.sleep(1)
        #             return spawn
        #
        #         if i == 4:
        #             time.sleep(5)
        #
        #         if i == 5:
        #             time.sleep(5)
        #
        #         if i == 6:
        #             time.sleep(5)
        #             self.utils.print_info("pexpect.EOF, Retrying...")
        #             retry_count += 1
        #             continue
        #
        #         if i == 7:
        #             time.sleep(5)
        #             self.utils.print_info("Timeout, Retrying...")
        #             retry_count += 1
        #             continue
        #
        #         if retry_count == 10:
        #             self.utils.print_info("Unable To Access Device Console.There Is a Problem to access console port")
        #             self.screen.save_screen_shot()
        #             return -1
        #
        # elif platform == "aerohive":
        #     return self.open_aerohive_ap_spawn(ip, port, username, password, ssh, conn_str)
        #
        # elif platform == "aerohive-switch":
        #     return self.open_aerohive_switch_spawn(conn_str, username, password)
        #
        # elif platform == "aerohive-fastpath":
        #     return self.open_fastpath_switch_spawn(conn_str, username, password)
        #
        # elif platform.lower() == "voss":
        #     return self.open_voss_spawn(conn_str, username, password)
        #
        # elif platform == 'wing':
        #     return self.open_wing_ap_spawn(conn_str, username, password, ssh)
        #
        # elif platform.lower() == "exos":
        #     return self.open_exos_switch_spawn(conn_str, username, password, ssh)
        #
        # elif platform == "xiqse":
        #     return self.open_xiqse_spawn(conn_str, username, password)
        #
        # else:
        #     spawn = pexpect.spawn(conn_str, timeout=90)
        #     retry_count = 0
        #     self.utils.print_info("Connecting to Platform: ", platform)
        #     while retry_count < 10:
        #         self.utils.print_info("Loop : ", retry_count)
        #         if platform == "identifi":
        #             spawn.logfile = sys.stdout
        #             spawn.sendline("\r")
        #         else:
        #             spawn.sendline("\r")
        #
        #         """ pattern matches """
        #         i = spawn.expect(['## Booting',
        #                           'Welcome.',
        #                           'Please press Enter to activate this console.',
        #                           'Login incorrect',
        #                           'login:',
        #                           ' #'
        #                           '#',
        #                           '\>',
        #                           pexpect.TIMEOUT], timeout=60)
        #
        #         if i == 0:
        #             retry_count += 1
        #             self.utils.print_info("Booting...")
        #             time.sleep(5)
        #
        #         elif i == 1:
        #             retry_count += 1
        #             self.utils.print_info("Got Welcome... DUT is still booting")
        #             time.sleep(10)
        #
        #         elif i == 2:
        #             retry_count += 1
        #             self.utils.print_info("Continue")
        #
        #         elif i == 3:
        #             retry_count += 1
        #             time.sleep(65)
        #             self.utils.print_info("Continue")
        #
        #         elif i == 4:
        #             retry_count += 1
        #             self.utils.print_info("Got login: prompt..")
        #             self.utils.print_info("Sending Username : ", username)
        #             spawn.sendline(username)
        #             spawn.expect("Password:")
        #             time.sleep(1)
        #             self.utils.print_info("Sending Password: ", password)
        #             if password == "none":
        #                 self.utils.print_info("No Password. Sending a CR: ")
        #                 spawn.sendline("\r")
        #             else:
        #                 spawn.sendline(password)
        #
        #             j = spawn.expect(["System is currently using the factory default login credentials",
        #                               "Login incorrect",
        #                               "\>",
        #                               "\#"
        #                               ], timeout=60)
        #             """ i = spawn.expect(["Enter new password:","Login incorrect", "failed", ], timeout=60) """
        #             if j == 0:
        #                 self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
        #                 spawn.sendline(password_cloud_default)
        #                 spawn.expect('Confirm new password:')
        #
        #                 self.utils.print_info("Confirming Cloud Default Password : ", password_cloud_default)
        #                 spawn.sendline(password_cloud_default)
        #                 spawn.expect('>')
        #                 spawn.sendline('en')
        #                 spawn.expect('#')
        #             if j == 1:
        #                 spawn.sendline(username)
        #                 spawn.expect("assword:")
        #                 self.utils.print_info("Sending Factory Default Password : ", password_default)
        #
        #                 if password_default != -1:
        #                     spawn.sendline(password_default)
        #                 else:
        #                     spawn.sendline(password)
        #
        #                 k = spawn.expect(["Enter new password:",
        #                                   "Login incorrect", '>'])
        #                 if k == 0:
        #                     self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
        #                     spawn.sendline(password_cloud_default)
        #                     spawn.expect('Confirm new password:')
        #
        #                     self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
        #                     spawn.sendline(password_cloud_default)
        #                     spawn.expect('>')
        #                     spawn.sendline('en')
        #                     spawn.expect('#')
        #                 if k == 1:
        #                     self.utils.print_info("\n\nPlease try with valid login credentials...Exiting")
        #                     return -2
        #                 if k == 2:
        #                     self.utils.print_info("\n\nDefault password got changed... Please check")
        #                     exit(0)
        #             if j == 2:
        #                 spawn.sendline('en')
        #                 m = spawn.expect(["\#", "\:"], timeout=30)
        #                 if m == 1:
        #                     self.utils.print_info("Wrong > found.. Continuing..")
        #                     password_default = -1
        #                     continue
        #                 if m == 0:
        #                     self.utils.print_info("Found the prompt...")
        #                     break
        #             if j == 3:
        #                 pass
        #
        #         elif i == 6:
        #             retry_count += 1
        #             self.utils.print_info("Already Logged in")
        #             spawn.sendline('\r')
        #
        #             spawn.sendline('show version')
        #             time.sleep(2)
        #             break
        #
        #         elif i == 5:
        #             pass
        #
        #         elif i == 7:
        #             spawn.sendline('en')
        #             n = spawn.expect(["\#", "\:"], timeout=30)
        #             if n == 1:
        #                 self.utils.print_info("Wrong > found.. Continuing..")
        #                 password_default = -1
        #                 continue
        #             if n == 0:
        #                 self.utils.print_info("Found the prompt...")
        #                 break
        #         elif i == 8:
        #             self.utils.print_info("Killing the Lantronix Port...")
        #             lantronix_ip = 'telnet ' + ip
        #             lspawn = pexpect.spawn(lantronix_ip)
        #
        #             lspawn.logfile = sys.stdout
        #             retry_count = 0
        #             m = lspawn.expect(["ETS8P", "\>"], timeout=30)
        #             if m == 0:
        #                 self.utils.print_info("OLD Lantronix")
        #                 self.utils.print_info("Killing the tunnel on port : ", port)
        #                 lspawn.sendline("su" + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect(">")
        #
        #                 lspawn.sendline("su" + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect(">")
        #
        #                 lspawn.sendline("system" + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect(">>")
        #
        #                 lspawn.sendline("lo po " + str(int(port) % 2000) + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect(">>")
        #
        #                 lspawn.close()
        #                 retry_count = 0
        #
        #             if m == 1:
        #                 self.utils.print_info("NEW Lantronix")
        #                 self.utils.print_info("Killing the tunnel on port : ", port)
        #                 lspawn.sendline("enable" + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect("#")
        #
        #                 lspawn.sendline("tunnel " + str(int(port) % 10000) + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect("#")
        #
        #                 lspawn.sendline("accept" + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect("#")
        #
        #                 lspawn.sendline("kill connection" + '\r')
        #                 time.sleep(2)
        #                 lspawn.expect("#")
        #
        #                 lspawn.close()
        #
        #                 self.utils.print_info("Re-opening the spawn")
        #                 spawn = pexpect.spawn(conn_str)
        #                 spawn.logfile = sys.stdout
        #                 retry_count = 0
        #             continue
        #         else:
        #             self.utils.print_info("Retrying...")
        #         retry_count += 1
        #
        # self.utils.print_info("Returning spawn...")
        # return spawn

    def open_aerohive_switch_spawn(self, conn_str, username, password):
        """
        - This Keyword used to access Aerohive Switch Spawn Using Connection String, user name and password
        - Keyword Usage:
         - ``Open Aerohive Switch Spawn     ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``


        :param conn_str: Connection String ie telnet <ip>  <Port>
        :param username: User Name for spawn access
        :param password: Password for spawn access
        :return: Device Spawn to execute CLI commands
        """
        self.utils.print_info("Platform set to Aerohive Switch...")
        retry_count = 0
        spawn = -1
        while retry_count < 10:
            spawn = pexpect.spawn(conn_str, encoding='utf-8', codec_errors='ignore')
            time.sleep(5)
            spawn.sendline("\r")

            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['login:',
                              'User:',
                              'Password:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                self.utils.print_info("Sending Password: ", password)
                spawn.expect('Password:', timeout=30)
                time.sleep(5)
                spawn.sendline(password)
                time.sleep(2)
                j = spawn.expect('#', timeout=60)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 1:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                self.utils.print_info("Sending Password: ", password)
                spawn.expect('Password:', timeout=30)
                time.sleep(5)
                spawn.sendline(password)
                time.sleep(2)
                j = spawn.expect('>', timeout=60)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 2:
                self.utils.print_info("SSH Detected...")
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 3:
                time.sleep(1)
                spawn.sendline("yes")
                continue

            if i == 4:
                time.sleep(1)
                return spawn

            if i == 5:
                time.sleep(5)

            if i == 6:
                spawn.sendline("en")

            if i == 7:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")

            if i == 8:
                self.utils.print_info("Timeout, Retrying after 30 seconds...")
                time.sleep(30)
                spawn.sendline("\r")

            retry_count += 1
        return spawn

    def open_fastpath_switch_spawn(self, conn_str, username, password):
        """
        - This Keyword used to access Aerohive Fastpath Switch Spawn Using Connection String, user name and password
        - Keyword Usage:
         - ``Open Fastpath Switch Spawn     ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``

        :param conn_str: Connection String ie telnet <ip>  <Port>
        :param username: User Name for spawn access
        :param password: Password for spawn access
        :return: Device Spawn to execute CLI commands
        """
        self.utils.print_info("Platform set to Aerohive Switch...")
        retry_count = 0
        spawn = -1
        while retry_count < 10:
            spawn = pexpect.spawn(conn_str, encoding='utf-8', codec_errors='ignore')
            time.sleep(5)
            spawn.sendline("\r")

            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['User:',
                              'Password:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                self.utils.print_info("Sending Password: ", password)
                spawn.expect('Password:', timeout=30)
                time.sleep(5)
                spawn.sendline(password)
                time.sleep(2)
                j = spawn.expect('>', timeout=60)
                if j == 0:
                    spawn.sendline('en')
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 1:
                self.utils.print_info("SSH Detected...")
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 2:
                time.sleep(1)
                spawn.sendline("yes")
                continue

            if i == 3:
                time.sleep(1)
                return spawn

            if i == 4:
                time.sleep(5)

            if i == 5:
                spawn.sendline("en")

            if i == 6:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")

            if i == 7:
                time.sleep(5)
                self.utils.print_info("Timeout, Retrying...")
                spawn.sendline("\r")

            retry_count += 1
        return spawn

    def open_aerohive_ap_spawn(self, ip, port, username, password, ssh, conn_str):
        """
        - This Keyword used to access Aerohive AP Spawn Using IP, Port,user name and password and Connection String
        - Keyword Usage:
         - ``Open Aerohive AP Spawn     ${IP}  ${PORT}  ${USERNAME}  ${PASSWORD}``
         - ``Open Aerohive AP Spawn     ${IP}  ${PORT}  ${USERNAME}  ${PASSWORD}   ssh  ${CONNECTION_STRING}``


        :param ip: IP Address of Aerohive AP
        :param port: Port Number of Aerohive AP
        :param username: User Name of Aerohive AP
        :param password: Password of Aerohive AP
        :param ssh: to set ssh flag is true
        :param conn_str: Connection String of Aerohive AP with IP and port string combination
        :return: Device Spawn
        """
        self.utils.print_info("Platform set to Aerohive AP...")

        if ssh is True:
            self.utils.print_info("SSH Detected...")
            return self.open_pxssh_spawn(ip, username, password)

        self.utils.print_info("conn_str: ", conn_str)
        retry_count = 0
        spawn = -1
        while retry_count < 5:
            spawn = pexpect.spawn(conn_str, encoding='utf-8', codec_errors='ignore')
            time.sleep(5)
            if not ssh:
                spawn.sendline("\r")
            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['login:',
                              'assword:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                time.sleep(2)
                self.utils.print_info("Sending Password: ", password)
                spawn.expect('assword:', timeout=30)
                time.sleep(2)
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', 'login:'], timeout=30)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Sending Username: ", username)
                    spawn.sendline(username)
                    time.sleep(2)
                    self.utils.print_info("Sending Default Password: ", password)
                    spawn.sendline(self.aerohive_default_password)
                    time.sleep(2)
                    spawn.expect('#')
                    return spawn
                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 1:
                self.utils.print_info("SSH Detected...")
                self.utils.print_info("Sending Password: ", password)
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 2:
                time.sleep(1)
                spawn.sendline("yes")

            if i == 3:
                time.sleep(1)
                return spawn

            if i == 4:
                time.sleep(5)

            if i == 5:
                time.sleep(5)

            if i == 6:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")

            if i == 7:
                time.sleep(30)
                self.utils.print_info("Timeout, Retrying...")
                spawn.sendline("\r")

            retry_count += 1
            if retry_count == 5:
                self.utils.print_info("Unable To Access Device Console.There Is a Problem to access console port")
                return -1
        return spawn

    def open_wing_ap_spawn(self, conn_str, username, password, ssh):
        """
        - This Keyword used to access Wing AP Spawn Using Connection String,user name and password.
        - Keyword Usage:
         - ``Open Wing AP Spawn     ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``
         - ``Open Wing AP Spawn      ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}  ssh``


        :param conn_str: Connection String of Wing AP with IP and port string combination
        :param username: User Name of Wing AP
        :param password: Password of Wing AP
        :param ssh: to set ssh flag is true

        :return: Wing Device Spawn
        """
        self.utils.print_info("Platform set to WiNG AP...")
        self.utils.print_info("conn_str: ", conn_str)
        retry_count = 0
        spawn = -1
        while retry_count < 10:
            spawn = pexpect.spawn(conn_str, encoding='utf-8', codec_errors='ignore')
            time.sleep(5)
            if not ssh:
                spawn.sendline("\r")
            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['login:',
                              'assword:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                time.sleep(2)
                spawn.expect('assword:', timeout=30)
                time.sleep(2)
                spawn.sendline(password)
                time.sleep(10)
                j = spawn.expect('#', timeout=60)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 1:
                self.utils.print_info("SSH Detected...")
                self.utils.print_info("Sending Password: ", password)
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 2:
                time.sleep(1)
                spawn.sendline("yes")

            if i == 3:
                time.sleep(1)
                return spawn

            if i == 4:
                time.sleep(5)

            if i == 5:
                time.sleep(5)

            if i == 6:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")

            if i == 7:
                time.sleep(5)
                self.utils.print_info("Timeout, Retrying...")
                spawn.sendline("\r")

            retry_count += 1
        return spawn

    def open_windows_spawn(self, conn_str, username, password):
        """
        - This Keyword used to access Windows Host Spawn Using Connection String, user name and password
        - Keyword Usage:
         - ``Open Windows Spawn     ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``

        :param conn_str: Connection String of Windows Host with IP and port string combination
        :param username: User Name of Windows host to access
        :param password: Password of Windows host to access

        :return: Windows host Spawn
        """
        spawn = pexpect.spawn(conn_str)
        spawn.logfile = sys.stdout
        time.sleep(5)
        self.utils.print_info("Connecting to Windows Host")
        retry_count = 0
        while retry_count < 10:
            i = spawn.expect([':', pexpect.EOF, pexpect.TIMEOUT], timeout=20)
            if i == 0:
                self.utils.print_info("Sending Username : ", username)
                spawn.send(username + "\r")
                time.sleep(5)
                self.utils.print_info("Sending Password : ", password)
                spawn.expect('assword:', timeout=20)
                time.sleep(5)
                spawn.send(password + "\r")
                time.sleep(5)
                spawn.send("\r\n")
                time.sleep(5)
                try:
                    j = spawn.expect('>', timeout=20)
                except Exception as e:
                    self.utils.print_info(e)
                    # in case connect with a ssh server on window machine
                    j = spawn.expect('$', timeout=20)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")

            if i == 1:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")
                continue

            if i == 2:
                time.sleep(5)
                self.utils.print_info("Timeout, Retrying...")
                continue

            retry_count += 1
            if retry_count == 10:
                self.utils.print_info("Unable To Access Device Console.There Is a Problem to access console port")
                return -1
        return spawn

    def send_command_to_ap1(self, command):
        """
        - This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor
        - Keyword Usage:
         - ``Send Command To AP1     ${COMMAND}``

        :param command: CLI command to be execute on AP1

        :return: CLI Command Output
        """
        ip = self.utils.get_config_value("AP1_CONSOLE_IP")
        port = self.utils.get_config_value("AP1_CONSOLE_PORT")
        username = self.utils.get_config_value("AP1_USERNAME")
        password = self.utils.get_config_value("AP1_PASSWORD")
        platform = self.utils.get_config_value("AP1_PLATFORM")

        self.utils.print_info("AP1 IP         : ", ip)
        self.utils.print_info("AP1 Port       : ", port)
        self.utils.print_info("AP1 Username   : ", username)
        self.utils.print_info("AP1 Password   : ", password)
        self.utils.print_info("AP1 Platform   : ", platform)

        _spawn = self.open_spawn(ip, port, username, password, platform)
        if _spawn:
            output = self.send(_spawn, command)
            self.close_spawn(_spawn)
            return output

    def send(self, spawn, line, expect_match="default", time_out="default", platform="default", **kwargs):
        """
        - This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor
        - Default timeout is 90 seconds
        - Keyword Usage:
         - ``Send   ${SPAWN}        ${COMMAND}``

        :param spawn: Device Spawn to execute command
        :param line: CLI command to be execute
        :param expect_match: Expected Prompt Match
        :param time_out: Timeout value
        :param platform: Device/Host Platform (Not needed anymore)
        Optional Arguments (kwargs):
        :param wait_for_prompt: If set to True, keyword will move on without waiting for the device prompt to return. This is often used in cli commands that have follow-up questions or outputs that do not contain the prompt. Default is False.
        :param check_initial_prompt: If set to False, keyword will not check for prompt before issuing a command to agent. Default is True.
        :param expect_error: This will cause a keyword to fail unless an error is seen in the commands output. This is disabled by default.
        :param wait_for and interval: This function executes a wait for validation. It checks the result of the passed parse function every (The time in seconds between each status check of the keyword function) until it matches the expected result or <max_wait> seconds have passed.
        :param max_wait: The amount of time in seconds the keyword should wait before it is considered a failure.
        :param ignore_error: This adds errors to the devices error checker to ignore for the given keyword.
        :param ignore_cli_feedback: If set to True CLI feedback is ignored. This is set to False by default. This will ignore any errors that may be returned from running this keyword. This could be used to make sure the device is in a clean state before a test will begin. In some cases the keyword would execute with and without errors but the user doesn't want to report on the errors that may be returned.
        :param prompt:  This accepts a prompt constant (which can be found in NetworkElementConstants).
                        It tells the device which prompt it should sent the command from.
        :param prompt_args:  This accepts either a string or list of strings which should contain
                             any arguments required by the prompt handler to change prompt.
        :param confirmation_phrases:  This accepts either a string or list of strings which contain any
                                      outputs that require a response.
        :param confirmation_args:  This accepts a string or list of strings to send in response to the
                                   received confirmation phrase.
        :return: CLI Command Output
        """

        # Speical prompts
        prompt = "#"
        if platform == 'adsp':
            kwargs['prompt'] = "$"
            self.utils.print_info("Prompt set to $")
        if platform == "win":
            kwargs['prompt'] = ">"
            self.utils.print_info("Prompt set to >")
        if platform == 'xiqse':
            kwargs['prompt'] = "$"
            self.utils.print_info("Prompt set to $")

        # Args
        output = ''
        if expect_match != 'default':
            kwargs['expect_error'] = True
        if time_out != 'default':
            kwargs['max_wait'] = time_out
        result = self.networkElementCliSend.send_cmd(spawn, line, **kwargs)
        try:
            output = str(result[0].return_text)
        except Exception as e:
            self.utils.print_info("Keyword had an error: " + str(e))
        return output




        # if spawn == -9:
        #     return -9
        #
        # prompt = "#"
        # if platform == 'adsp':
        #     prompt = "$"
        #     self.utils.print_info("Prompt set to $")
        # if platform == "win":
        #     prompt = ">"
        #     self.utils.print_info("Prompt set to >")
        # if platform == 'xiqse':
        #     prompt = "$"
        #     self.utils.print_info("Prompt set to $")
        #
        # if spawn == -1:
        #    self.utils.print_info("Device Spawn is not Opened Successfully. So Unable to Send Command.")
        #    return -1
        #
        #
        # self.utils.print_info("Sending Command : " + "\n======================================\n" + line)
        # if expect_match == "default":
        #     self.utils.print_debug("Expected Match: default")
        #     line = line.strip()
        #     spawn.sendline(line)
        #     # self.utils.print_info("----------------")
        #     # self.utils.print_info(spawn.before + spawn.after)
        #     # self.utils.print_info("----------------")
        #     if self.dut_platform == "win":
        #         spawn.sendline("\r\n")
        #         prompt = ">"
        #         self.utils.print_info("Prompt set to >")
        #
        #     time.sleep(5)
        #     output1 = ""
        #     output2 = spawn.read_nonblocking(size=10000)
        #     if line == "exit":
        #         return output1 + output2
        #
        #     if time_out == "default":
        #         self.utils.print_debug("Time Out: default")
        #         retry_count = 0
        #         while retry_count < 6:
        #             self.utils.print_info("Loop: ", retry_count)
        #             spawn.sendline("\r")
        #             i = spawn.expect([prompt, pexpect.EOF, pexpect.TIMEOUT], timeout=90)
        #             if i == 0:
        #                 self.utils.print_info("Breaking the Loop")
        #                 break
        #             if i == 2:
        #                 output = str(spawn.before) + str(spawn.after)
        #                 self.utils.print_info("OUTPUT : ", output)
        #                 self.utils.print_info("Timeout... Retrying")
        #                 time.sleep(5)
        #             if i == 3:
        #                 break
        #             else:
        #                 retry_count += 1
        #     else:
        #         self.utils.print_info("Expecting prompt in : ", int(time_out))
        #         spawn.expect("#", timeout=int(time_out))
        #         output1 = str(spawn.before) + str(spawn.after)
        # else:
        #     spawn.sendline(line)
        #     if platform == "win":
        #         spawn.sendline("\r\n")
        #     time.sleep(2)
        #     output1 = ''
        #     output2 = spawn.read_nonblocking(size=5000)
        #     self.utils.print_info("EXPECTING MATCH : ", expect_match)
        #     # if time_out == "default":
        #     #    spawn.expect(expect_match)
        #     # else:
        #     #    spawn.expect(expect_match, timeout=int(time_out))
        #     #    output1 = str(spawn.before) + str(spawn.after)
        #
        # self.utils.print_info("OUTPUT :\n======================================")
        #
        # try:
        #     cli_output = str(output1) + str(output2)
        #     self.utils.print_info("", cli_output)
        #     return cli_output
        # except TypeError:
        #     self.utils.print_info("", str(output1))
        #     self.utils.print_info("", str(output2))

    def ping_from(self, destination, count=3):
        """
        - This method pings from the script host to the destination.
        - default count is 3
        - Keyword Usage:
         - ``Ping From     ${DESTINATION_IP}``
         - ``Ping From     ${DESTINATION_IP}  count=10``

        :param destination: IP or host name
        :param count: Number of ping requests. Default is 3
        :return: returns 1 if 0 packet loss else -1
        """

        self.utils.print_info("Pinging to : ", destination)
        output = subprocess.run([" ping ", str(destination), " -c " + str(count)])
        self.utils.print_info("OUTPUT DATA:", output)

        if "100% packet loss" in output:
            return -1
        elif " 0% packet loss" in output:
            return 1
        elif "% packet loss" in output:
            return 1
        else:
            return -1

    def ping_from_spawn(self, _spawn, destination, count=3):
        """
        - This method pings from the spawn to the destination.
        - default count is 3
        - Keyword Usage:
         - ``Ping From Spawn   ${SPAWN}  ${DESTINATION_IP}``
         - ``Ping From Spawn   ${SPAWN}  ${DESTINATION_IP}   count=10``

        :param _spawn: spawn of DUT/host from where ping should start
        :param destination: IP or host name
        :param count: Number of ping requests. Default is 3
        :return: returns 1 if 0 packet loss else -1
        """

        self.utils.print_info("Pinging to : ", destination)
        output = self.send(_spawn, "ping " + str(destination) + " -c " + str(count))
        self.utils.print_info("OUTPUT DATA:", output)

        if "100% packet loss" in output:
            return -1
        elif " 0% packet loss" in output:
            return 1
        elif "% packet loss" in output:
            return 1
        else:
            return -1

    def httping_from(self, _spawn, destination, count=3, timeout=5):
        """
        - This method pings from the spawn to the destination.
        - default count is 3
        - Keyword Usage:
         - ``Httping From   ${SPAWN}  ${DESTINATION_IP}``
         - ``Httping From   ${SPAWN}  ${DESTINATION_IP}   count=10``
         - ``Httping From   ${SPAWN}  ${DESTINATION_IP}   count=10   timeout=10``

        :param _spawn: spawn of DUT/host from where ping should start
        :param destination: IP or host name
        :param count: Number of ping requests. Default is 3
        :param timeout: Timeout for the HTTP ping. Default is 5 seconds
        :return: returns 1 if 0 packet loss else -1
        """

        output = self.send(
            _spawn, "httping " + str(destination) + " -c " + str(count) + " -t " + str(timeout), "#", str(60))
        if "100.00% failed" in output:
            return 0
        elif " 0.00% failed" in output:
            return 1
        else:
            return -1

    def send_commands(self, spawn, commands_list):
        """
        - Sends multiple commands separated by a ","
        - Keyword Usage:
         - ``Send Commands   ${SPAWN}  ${COMMAND_LIST}``

        :param spawn: spawn of DUT/host
        :param commands_list: list of DUT/Lunux commands separated by comma
        :return: output of the command
        """
        self.utils.print_info("Sending Commands List: ", commands_list)

        command_list = commands_list.split(",")
        output_end = ""

        for command in command_list:
            self.utils.print_info("Sending command: ", command)
            command = command.strip()
            output1 = self.send(spawn, command)
            time.sleep(2)
            output_end += output1

        return output_end

    def exec_shell_command(self, exec_shell_command):
        """
        - Executes a shell command
        - Keyword Usage:
         - ``Exec Shell Command  ${SHELL_COMMAND}``

        :param exec_shell_command: Any shell command
        :return: output of the command
        """

        self.utils.print_info("Command: ", exec_shell_command)
        args = shlex.split(exec_shell_command)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = p.stdout.read()
        return result

    def open_pxssh_spawn(self, host, username, password, _port=22, prompt_reset=False,
                         disable_strict_host_key_checking=False, sync_multiplier=5):
        """
        - Opens a pxssh spawn
        - Keyword Usage:
         - ``Openpxssh Spawn  ${HOST_NAME}  ${USER_NAME}  ${PASSWORD}``
         - ``Openpxssh Spawn  ${HOST_NAME}  ${USER_NAME}  ${PASSWORD}   disable_strict_host_key_checking=True``

        :param host: IP or host name
        :param username: username of host
        :param password: password of host
        :param _port: port number
        :param prompt_reset: prompt reset boolean
        :param disable_strict_host_key_checking : Either True/False .Based on these two flags it will Changes
                                          strict_host_key_checking value of ssh_config on server.
                                          By default(False) server will check ssh key of the device on remote host.
        :param sync_multiplier: sync_multiplier
        :return: returns 1 if 0 packet loss else -1
        """
        try:
            self.utils.print_info("Host        : ", host)
            self.utils.print_info("Username    : ", username)
            self.utils.print_info("Password    : ", password)
            self.utils.print_info("Port        : ", _port)
            self.utils.print_info("PromptReset : ", prompt_reset)
            self.utils.print_info("Sync Multi  : ", sync_multiplier)

            if disable_strict_host_key_checking:
                self.utils.print_info("Disabling SSH key Checking for Remote Device/Host On Server")
                pxssh_spawn = pxssh.pxssh(options={"StrictHostKeyChecking": "no", "UserKnownHostsFile": "/dev/null"})
            else:
                pxssh_spawn = pxssh.pxssh()

            if pxssh_spawn.login(host, username, password, port=_port, auto_prompt_reset=prompt_reset, original_prompt=r"[#$>]", sync_multiplier=sync_multiplier):
                pxssh_spawn.logfile = None
                self.utils.print_info("SSH session login successful")
                self.utils.print_info(pxssh_spawn.before)
                return pxssh_spawn
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def close_pxssh_spawn(self, pxssh_spawn):
        """
        - Closes a pxssh spawn
        - Keyword Usage:
         - ``Close Pxssh Spawn  ${PXSSH_SPAWN}``
        :param pxssh_spawn: pxssh spawn to close
        :return: -1 in case of error else 1
        """

        self.utils.print_info("Closing PXSSH spawn")
        try:
            pxssh_spawn.logout()
            return 1
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def send_pxssh(self, pxssh_spawn, command, timeout=3, expected_output=None):
        """
        - Sends a command to pxssh spawn
        - Default Timeout value is 3 seconds
        - Keyword Usage:
         - ``Send Pxssh  ${PXSSH_SPAWN}  ${COMMAND}``
         - ``Send Pxssh  ${PXSSH_SPAWN}  ${COMMAND}  ${TIMEOUT}=10``

        :param pxssh_spawn: pxssh spawn
        :param command: command to send
        :param timeout: timeout to get the output
        :param expected_output: expected output to match
        :return: -1 in case of error else pxssh spawn
        """

        try:
            aa = pxssh_spawn.sendline(command)
            if expected_output:
                pxssh_spawn.expect(expected_output)
            else:
                pxssh_spawn.prompt(timeout=timeout)
            self.utils.print_info("spawn.before: ", pxssh_spawn.before)
            self.utils.print_info("-----------------------------------")
            self.utils.print_info("spawn.after: ", pxssh_spawn.after)
            time.sleep(1)
            if expected_output:
                return pxssh_spawn.after.decode("utf-8", errors="ignore")
            return pxssh_spawn.before.decode("utf-8", errors="ignore")
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_ssh_spawn(self, **kwargs):
        """
        - Creating spawn object, This will work only for extreme wing
        - Keyword Usage:
         - ``netmiko ssh spawn  ${SPAWN_DICTIONARY_PARAMETERS}``

        :param kwargs: host, username, password
        :return: returns spawn else the exception
        """
        extreme = {'device_type': 'extreme_wing'}
        extreme['host'] = self.host=kwargs.get('host')
        extreme['username'] = self.host=kwargs.get('username')
        extreme['password'] = self.host=kwargs.get('password')
        try:
            spawn = ConnectHandler(**extreme)
            spawn.find_prompt()
            return spawn
        except Exception as e:
            self.utils.print_info("Exception caught while creating sapwan is: ", str(e))

    def netmiko_send_en_command(self, spawn, command):
        """
        - Sending command to spawn obj(specifically show commands of wings)
        - Keyword Usage:
         - ``Netmiko Send En Command  ${SPAWN}  ${COMMAND}``

        :param spawn: netmiko spawn
        :param command: command to send
        :return: -1 in case of error else output of command
        """
        # Enable the prompt
        try:
            spawn.enable()
            output = spawn.send_command(command)
            self.utils.print_info("{} output is {}".format(command, output))
            return output
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_send_cfg_cmd(self, spawn, config_commands):
        """
        - Send the commands for configuring
        - Keyword Usage:
         - ``Netmiko Send Cfg Cmd  ${SPAWN}  ${COMMANDS_LIST}``

        :param spawn: netmiko spawn
        :param config_commands: command to send
        :return: -1 in case of error else output of command
        """
        try:
            spawn.enable()
            output = spawn.send_config_set(config_commands)
            self.utils.print_info("Configuration:\n {}".format(output))
            return output
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_send_timing_command(self, spawn, cmd):
        """
        - Sends command to spawn
        - Keyword Usage:
         - ``netmiko send timing command  ${SPAWN}  ${COMMAND}``

        :param spawn: netmiko spawn
        :param cmd: command
        :return: output of command if successful else -1
        """
        try:
            # send_command_timing as the router prompt is not returned
            self.utils.print_info("Sending command: ", cmd)
            output = spawn.send_command_timing(cmd, strip_command=False, strip_prompt=False)
            if "confirm" in output:
                    output += spawn.send_command_timing(
                        "\n", strip_command=False, strip_prompt=False
            )
            return output
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_close(self, spawn):
        """
        - Closes a netmiko spawn
        - Keyword Usage:
         - ``Netmiko Close``

        :param spawn: netmiko spawn
        :return: -1 in case of error else 1
        """
        try:
            spawn.disconnect()
            return 1
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def open_paramiko_ssh_spawn(self, host, username, password, port=22):
        """
        - Creating ssh spawn object
        - Keyword Usage:
         - ``Open Paramiko SSH Spawn   ${HOST}  ${USERNAME}  ${PASSWORD}``

        :param host: IP or host name of DUT
        :param username: username to access Spawn
        :param password: password to access Spawn
        :return: returns spawn else -1
        """
        try:
            spawn = paramiko.SSHClient()
            # Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.
            spawn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            spawn.load_system_host_keys()
            spawn.connect(str(host), port, username=str(username), password=str(password))
            return spawn
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def send_paramiko_cmd(self, spawn, cmd, timeout=10):
        """
        - Execute the commands on ssh spawn
        - Keyword Usage:
         - ``Send Paramiko Cmd   ${SPAWN}  ${COMMAND}``
         - ``Send Paramiko Cmd   ${SPAWN}  ${COMMAND}  timeout=${TIMEOUT_VALUE}``

        :param spawn: Paramiko spawn
        :param cmd: command to send
        :param timeout: command timeout
        :return: -1 in case of error else output of command
        """
        try:
            stdin, stdout, stderr = spawn.exec_command(cmd, timeout=timeout)
            output = stdout.read().decode('ascii').strip("\n")
            self.utils.print_info("cmd: {}".format(cmd))
            self.utils.print_info("Output: {}".format(output))
            return output
        except paramiko.SSHException:
            self.utils.print_info("Failed to execute the command")

    def close_paramiko_spawn(self, spawn):
        """
        - Closes paramiko spawn object
        - Keyword Usage:
         - ``Close Paramiko Spawn   ${SPAWN}``

        :param spawn: paramiko spawn
        :return: returns -1 if there is any exception
        """
        self.utils.print_info("Closing paramiko spawn")
        try:
            spawn.close()
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def get_thput_value(self, ip, cli_spawn, server_spawn):
        """
        - Get the throughput value from and to air
        - Keyword Usage:
          - ``Get Thput Value   ${IP}    ${CLI_SPAWN}   ${SERVER_SPAWN}``

        :param ip: IP address
        :param cli_spawn: CLI Spawn
        :param server_spawn: Server Spawn
        :return: server command output
        """
        cli_cmd = 'iperf -c ' + ip + ' -i 1 -u  -b 20m -t 10'
        srvr_cmd = 'iperf -s -i 1 -u  &'

        self.utils.print_info("client_cmd:{}".format(cli_cmd))
        self.utils.print_info("Server_cmd:{}".format(srvr_cmd))

        _, stdout, _ = server_spawn.exec_command(srvr_cmd, timeout=200)
        cli_spawn.exec_command(cli_cmd, timeout=200)

        time.sleep(60)
        server_spawn.exec_command('TASKKILL /IM iperf.exe /F', timeout=200)
        server_spawn.exec_command('killall iperf', timeout=200)

        cli_spawn.exec_command('killall iperf', timeout=200)
        cli_spawn.exec_command('TASKKILL /IM iperf.exe /F', timeout=200)

        return stdout.readlines()
    
    def close_netmiko_spawn(self, spawn):
        """
        - Closing netmiko spawn object
        - Keyword Usage:
         - ``Close Netmiko Spawn   ${SPAWN}``

        :param spawn: netmiko spawn
        :return: returns -1 if there is any exception
        """
        self.utils.print_info("Closing netmiko spawn")
        try:
            spawn.disconnect()
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def open_wing_spawn(self, host, username, password):
        """
        - Open Wing spawn object using PXSSH
        - Keyword Usage:
         - ``Open Wing Spawn   ${HOST}  ${USERNAME}  ${PASSWORD}``

        :param host: IP/Host of WING AP
        :param username: username
        :param password: Password
        :return: Wing Device Spawn
        """
        wing_spawn = pxssh.pxssh()
        if not wing_spawn.login(host, username, password, auto_prompt_reset=False):
            self.utils.print_info("SSH session failed on login.")
            print (str(wing_spawn))
        else:
            self.utils.print_info("SSH session login successful")
            self.utils.print_info(wing_spawn.before)
            return wing_spawn

    def send_wing_cmd(self, pxssh_spawn, command):
        """
        - This method will send a command to the Wing spawn Object
        - Keyword Usage:
         - ``Send Wing Cmd   ${SPAWN}  ${COMMAND}``

        :param pxssh_spawn: spawn
        :param command: command to send
        :return: returns the output if success else -1
        """
        try:
            aa = pxssh_spawn.sendline(command)
            pexpect.pty_spawn.SpawnBase.buffer = ""
            self.utils.print_info("-----------------------------------")
            self.utils.print_info("spawn.before: ", pxssh_spawn.before)
            self.utils.print_info("-----------------------------------")
            self.utils.print_debug("spawn.after: ", pxssh_spawn.after)
            time.sleep(1)
            return pxssh_spawn.before
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def get_ap_version(self, spawn=None):
        """
        - This method returns the AP HiveOs version
        - Keyword Usage:
         - ``Get AP Version``

        :param spawn: spawn to AP
        :return: returns the version if success else -1
        """
        #output = self.send_command_to_ap1('show version | include Version')
        self.utils.print_info("Getting AP Version")
        output = self.send(spawn, 'show version | include Version')
        try:
            self.utils.print_info("AP Version: ", output)
            ap_version = re.search('HiveOS (.*) build', output).group(1)
            return ap_version
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def capwap_ap_on_off(self, ip, usr, passwd, mode):
        """
        - This Keyword will enable/disable capwap mode
        - Keyword Usage:
         - ``Capwap AP On Off``

        :param ip: IP Address of AP
        :param usr: user name
        :param passwd: Password
        :param mode: Either on/off
        :return: None
        """

        self.conn = self.open_spawn(ip, 22, usr, passwd, 'aerohive')
        if mode == 'off':
            self.send(self.conn, AP_CAPWAP_OFF, time_out="default", platform="aerohive")
        else:
            self.send(self.conn, AP_CAPWAP_ON, time_out="default", platform="aerohive")
        self.close_spawn(self.conn)

        
    def mac_wifi_connection(self, ip, usr, passwd, ssid, ssid_pass='badpassword20*rd', wifi_port='en1', mode='pass',
                            ntimes=1):
        """
        - This Keyword will establish WiFi Connection in MAC PC/Laptop
        - Keyword Usage:
         - ``mac_wifi_connection  ${IP}  ${USERNAME}  {PASSWORD}  ${SSID}``
         - ``mac_wifi_connection  ${IP}  ${USERNAME}  {PASSWORD}  ${SSID}  ssid_pass=${SSID_PASSWORD}``

        :param ip: IP Address of MAC book
        :param usr: username of MAC book
        :param passwd: Password of MAC book
        :param ssid: WiFI SSID
        :param ssid_pass:  ssid Password
        :param wifi_port: WiFi interface
        :param mode: WiFi Mode
        :param ntimes: No.of times to try to establish the WiFi Connections
        :return:  None
        """

        self.conn = self.open_paramiko_ssh_spawn(ip, usr, passwd)
        self.send_paramiko_cmd(self.conn, TURN_ON_OFF_WIFI_INTERFACE + wifi_port + ' ON', 30)

        cnt = -1
        for i in range(1, 5):
            self.utils.print_info( " ***** Number of attempts ", str(i))
            time.sleep(20)
            listSSIDs = str(self.send_paramiko_cmd(self.conn, SCAN_FOR_LIST_WIFI, 300))
            cnt = self.utils.check_match(listSSIDs, ssid)
            if cnt == 1:
                self.utils.print_info('ssid ' + ssid + ' is found')
                break

        if cnt != 1: return -1, "Not able to find the SSID"

        cn1 = False
        if mode == 'pass':
            rc = self.send_paramiko_cmd(self.conn, CONNECT_TO_WIFI + wifi_port + ' ' + ssid + ' ' + ssid_pass, 30)
            self.utils.print_info("RC is ---------" + str(rc))
            if self.utils.check_match(rc, 'Failed to join') == 1   : return -1,  " Fail to Join "
            if self.utils.check_match(rc, 'not find network') == 1 : return -1,  " Could not find network " + str(ssid)
            if self.utils.check_match(rc, 'Exception') == 1        : return -1,  " Fail with an Exception"
            if self.utils.check_match(rc, 'Error') == 1            : return -1,  " There is an Error "

            self.utils.print_info('Connect successfully!')
        else:
            for i in range(1, ntimes):
                self.utils.print_info(str(i) + ' attempt(s)')
                rc = self.send_paramiko_cmd(self.conn, CONNECT_TO_WIFI + wifi_port + ' ' + ssid + ' ' + ssid_pass, 40)
        self.close_spawn(self.conn)

        return str(1), None


    def get_mac_hostname(self, ip, userid, passwd):
        """
        - This keyword will get the Host Name of Mac book
        - Keyword Usage:
         - ``Get MAC Hostname  ${IP}  ${USERNAME}  {PASSWORD}``

        :param ip: IP Address of MAC book
        :param userid:  username of MAC book
        :param passwd: Password of MAC book
        :return: Host Name of mac book
        """
        conn = self.open_paramiko_ssh_spawn(ip, userid, passwd)
        hostname = self.send_paramiko_cmd(conn, 'hostname')
        self.close_spawn(conn)
        return hostname

    def open_exos_switch_spawn(self, conn_str, username, password, ssh):
        """
        - This keyword will Open EXOS Switch spawn object
        - Keyword Usage:
         - ``Open Exos Switch Spawn   ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``
         - ``Open Exos Switch Spawn   ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}  {SSH_FLAG}``

        :param host: IP/Host of EXOS Switch
        :param username: username of EXOS Switch
        :param password: Password of EXOS Switch
        :return: EXOS Switch Device Spawn
        """
        self.utils.print_info("Platform set to EXOS Switch...")
        self.utils.print_info("conn_str: ", conn_str)
        retry_count = 0
        spawn = -1
        while retry_count < 10:
            spawn = pexpect.spawn(conn_str, encoding='utf-8', codec_errors='ignore')

            time.sleep(5)
            if not ssh:
                spawn.sendline("\r")
            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['login:',
                              'assword:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              'Authentication',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                time.sleep(2)
                self.utils.print_info("Sending Password: ", password)
                spawn.expect('assword:', timeout=30)
                time.sleep(2)
                if password == "":
                    self.utils.print_info("Password is :  None")
                    spawn.sendline('\r')
                else:
                    spawn.sendline(password)
                time.sleep(10)
                j = spawn.expect('#', timeout=60)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            elif i == 1:
                self.utils.print_info("SSH Detected...")
                self.utils.print_info("Sending Password: ", password)
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            elif i == 2:
                if i == 3:
                    time.sleep(1)
                    return spawn

                if i == 4:
                    time.sleep(5)

                if i == 5:
                    time.sleep(5)

                if i == 6:
                    self.utils.print_info("Looks like Device rebooted just now... ")
                    spawn.sendline('\r')

                if i == 7:
                    time.sleep(5)
                    self.utils.print_info("pexpect.EOF, Retrying...")

                if i == 8:
                    time.sleep(5)
                    self.utils.print_info("Timeout, Retrying...")
                    spawn.sendline("\r")

                retry_count += 1
                return spawn
                time.sleep(1)
                spawn.sendline("yes")

            elif i == 3:
               time.sleep(1)
               return spawn

            else:
                self.utils.print_info("Retrying...")
            retry_count += 1

        return spawn

    def wait_for_cli_output(self, spawn, cmd, expected_output, retry_duration=30, retry_count=10):
        """
        - This Keyword will Helps to Wait till getting expected output based on retry duration
        - Retry duration by default 30 seconds
        - Retry Count by default 10
        - Keyword Usage:
         - ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}``
         - ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60``
         - ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60  ${COUNT}=15``

        :param spawn: Device Spawn
        :param cmd: Command to Execute
        :param expected_output: Expected CLI Output
        :param retry_duration: Retry Duration in seconds
        :param retry_count: Retry Count
        :return: 1 if Getting the expected output else -1
        """
        count = 1
        while count <= retry_count:
            _output = self.send(spawn, cmd)
            if expected_output in _output:
                self.utils.print_info("Got the expected output")
                return 1
            else:
                self.utils.print_info("Waiting for: ", retry_duration, " Seconds")
                time.sleep(retry_duration)
            count += 1
        self.utils.print_info("Unable to get the expected output. Please check.")
        return -1

    def clear_ssh_host_key(self):
        """
        - This keyword will clear the SSH key
        - Keyword Usage:
         - ``clear ssh host key``

        :return: None
        """

        # 'ssh-keygen -f "/home/automation/.ssh/known_hosts" -R "10.234.178.60"'
        pass

    def open_voss_spawn(self, conn_str, username, password):
        """
        - This keyword will Open VOSS Switch spawn object
        - Keyword Usage:
         - ``Open Voss Spawn   ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``

        :param conn_str: Connection String
        :param username: username of VOSS Switch
        :param password: Password of VOSS Switch
        :return: Voss Switch Spawn
        """
        spawn = pexpect.spawn(conn_str, timeout=90)
        retry_count = 0
        self.utils.print_info("Connecting to VOSS")
        while retry_count < 10:
            self.utils.print_info("Loop : ", retry_count)

            """ first thing we need to do is to enter a return to get to the login prompt """
            spawn.sendline("\r")

            """ pattern matches """
            i = spawn.expect(['## Booting',
                              'Welcome.',
                              'Please press Enter to activate this console.',
                              'Login incorrect',
                              'Login:',
                              'assword:',
                              ' #'
                              '#',
                              '\>',
                              pexpect.TIMEOUT], timeout=60)

            if i == 0:
                retry_count += 1
                self.utils.print_info("Booting...")
                time.sleep(5)

            elif i == 1:
                retry_count += 1
                self.utils.print_info("Got Welcome... DUT is still booting")
                time.sleep(10)

            elif i == 2:
                retry_count += 1
                self.utils.print_info("Continue")

            elif i == 3:
                retry_count += 1
                time.sleep(65)
                self.utils.print_info("Continue")

            elif i == 4 or i == 5:
                retry_count += 1
                if i == 4:
                    self.utils.print_info("Got Login: prompt..")
                    self.utils.print_info("Sending Username: ", username)
                    spawn.sendline(username)
                    spawn.expect("Password:")
                    time.sleep(1)
                self.utils.print_info("Sending Password: ", password)
                if password == "none":
                    self.utils.print_info("No Password. Sending a CR: ")
                    spawn.sendline("\r")
                else:
                    spawn.sendline(password)

                j = spawn.expect(["System is currently using the factory default login credentials",
                                  "Login incorrect",
                                  "\>",
                                  "\#"
                                  ], timeout=60)
                """ i = spawn.expect(["Enter new password:","Login incorrect", "failed", ], timeout=60) """
                if j == 0:
                    self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
                    spawn.sendline(password_cloud_default)
                    spawn.expect('Confirm new password:')

                    self.utils.print_info("Confirming Cloud Default Password : ", password_cloud_default)
                    spawn.sendline(password_cloud_default)
                    spawn.expect('>')
                    spawn.sendline('en')
                    spawn.expect('#')
                if j == 1:
                    spawn.sendline(username)
                    spawn.expect("assword:")
                    self.utils.print_info("Sending Factory Default Password : ", password_default)

                    if password_default != -1:
                        spawn.sendline(password_default)
                    else:
                        spawn.sendline(password)

                    k = spawn.expect(["Enter new password:",
                                      "Login incorrect", '>'])
                    if k == 0:
                        self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
                        spawn.sendline(password_cloud_default)
                        spawn.expect('Confirm new password:')

                        self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
                        spawn.sendline(password_cloud_default)
                        spawn.expect('>')
                        spawn.sendline('en')
                        spawn.expect('#')
                    if k == 1:
                        self.utils.print_info("\n\nPlease try with valid login credentials...Exiting")
                        return -2
                    if k == 2:
                        self.utils.print_info("\n\nDefault password got changed... Please check")
                        exit(0)
                if j == 2:
                    spawn.sendline('en')
                    m = spawn.expect(["\#", "\:"], timeout=30)
                    if m == 1:
                        self.utils.print_info("Wrong > found.. Continuing..")
                        password_default = -1
                        continue
                    if m == 0:
                        self.utils.print_info("Found the prompt...")
                        break
                if j == 3:
                    pass

            elif i == 6:
                pass

            elif i == 7:
                retry_count += 1
                self.utils.print_info("Already Logged in")
                spawn.sendline('\r')

                spawn.sendline('show version')
                time.sleep(2)
                break

            elif i == 8:
                spawn.sendline('en')
                n = spawn.expect(["\#", "\:"], timeout=30)
                if n == 1:
                    self.utils.print_info("Wrong prompt found.. Continuing..")
                    password_default = -1
                    continue
                if n == 0:
                    self.utils.print_info("Found the prompt...")
                    break

            else:
                self.utils.print_info("Retrying...")

        return spawn

    def open_xiqse_spawn(self, conn_str, username, password):
        """
        - This keyword will Open XIQ SE spawn object
        - Keyword Usage:
         - ``open xiqse spawn   ${CONNECTION_STRING}  ${USERNAME}  ${PASSWORD}``

        :param conn_str: Connection String
        :param username: username of xiqse
        :param password: Password of xiqse
        :return: xiqse Spawn
        """

        self.utils.print_info(f"Connect string: {conn_str}")
        spawn = pexpect.spawn(conn_str, timeout=90)
        retry_count = 0
        self.utils.print_info("Connecting to ExtremeCloud IQ - Site Engine")

        time.sleep(5)
        while retry_count < 10:
            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['login as:',
                              'assword:',
                              'yes/no',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            self.utils.print_debug(f"SPAWN.EXPECT INDEX IS {i}")
            if i == 0:
                self.utils.print_info(f"Sending Username: {username}")
                spawn.sendline(username)
                time.sleep(2)
                spawn.expect('assword:', timeout=30)
                time.sleep(2)
                self.utils.print_info(f"Sending Password: {password}")
                spawn.sendline(password)
                time.sleep(10)
                j = spawn.expect('$', timeout=60)
                if j == 0:
                    self.utils.print_info("Got expected prompt '$'... Returning Spawn")
                    return spawn
                else:
                    self.utils.print_info("Timeout - did not receive expected prompt '$'...")
                    continue

            if i == 1:
                self.utils.print_info(f"Sending Password: {password}")
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect('$', timeout=60)
                if j == 0:
                    self.utils.print_info("Got expected prompt '$'... Returning Spawn")
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout - did not receive expected prompt '$'...")
                    continue

            if i == 2:
                time.sleep(1)
                self.utils.print_info("Got yes/no prompt - sending 'yes'")
                spawn.sendline("yes")
                continue

            if i == 3:
                time.sleep(5)
                self.utils.print_info("pexpect.TIMEOUT, Retrying...")
                retry_count += 1
                continue

            if i == 4:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")
                retry_count += 1
                continue

        return spawn

    def reboot_switch(self, spawn, expected_output, option):
        """
        -This Keyword will reboot the switch
        - Keyword Usage:
         - ``Reboot Switch   ${SPAWN}  ${EXPECTED_OUTPUT}  ${OPTION}``

        :param spawn: Switch Spawn
        :param expected_output: Expected Output
        :param option: Option
        :return: 1 if Switch Rebooted Successfully else -1
        """
        spawn.sendline('reboot')
        time.sleep(2)
        try:
            spawn.expect(expected_output, timeout=30)
            spawn.sendline(option)
            spawn.expect('login', timeout=300)
            return 1
        except Exception as e:
            self.utils.print_info("Unable to send the reboot command")
            return -1

    def download_firmware_on_exos(self, spawn, image_url, vr_name, time_out=1000):
        """
        This method downloads the firmware on EXOS Switch

        :param spawn:       spawn to exos switch
        :param image_url:   image location url to load exos switch with.
        :param vr_name:     vr_name on exos switch
        :return: returns output 
        """
        dnld_cmd = f'download url {image_url} vr {vr_name}'
        self.utils.print_info("Sending download cli is   ", dnld_cmd)
        spawn.sendline(dnld_cmd)

        i = spawn.expect(['Do you want to continue with download and remove existing files from internal-memory?',
                          'Do you want to install image after downloading?',
                          'y - yes, n - no',
                          pexpect.TIMEOUT,
                          pexpect.EOF], timeout=200)

        if i == 0:
            time.sleep(2)
            output = str(spawn.before) + str(spawn.after)
            self.utils.print_info("OUTPUT : ", output)
            spawn.sendline("yes")
            time.sleep(5)

            j = spawn.expect(['Do you want to install image after downloading',
                              'y - yes, n - no',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=200)
            if j == 0 or j == 1:
                time.sleep(2)
                output = str(spawn.before) + str(spawn.after)
                self.utils.print_info("OUTPUT : ", output)
                spawn.sendline("yes")
                time.sleep(5)

        if i == 1 or i == 2:
            time.sleep(2)
            output = str(spawn.before) + str(spawn.after)
            self.utils.print_info("OUTPUT : ", output)
            spawn.sendline("yes")
            time.sleep(5)

        self.utils.print_info("Expecting prompt in : ", int(time_out))
        spawn.expect("#", timeout=int(time_out))
        output = str(spawn.before) + str(spawn.after)

        return output

    def enable_disable_iqagent_on_exos(self, spawn, operation):
        """
        This method disables or enables IQAgent on EXOS Switch based on operation input
        - Keyword Usage:
         - ``Enable Disable IQAgent on Exos   ${SPAWN}  disable``

        :param spawn:       spawn to exos switch
        :param operation:   perform IQAgent disable or enable.
        :return: returns output
        """
        if operation == "enable":
            self.utils.print_info("Sending IQAgent enable command to Device")
            spawn.sendline('enable iqagent')
        elif operation == "disable":
            self.utils.print_info("Sending IQAgent disable command to Device")
            spawn.sendline('disable iqagent')
        else:
            self.utils.print_info("Incorrect input..")

        i = spawn.expect(['Do you want to continue?',
                          pexpect.TIMEOUT,
                          pexpect.EOF], timeout=30)

        if i == 0:
            time.sleep(2)
            output = str(spawn.before) + str(spawn.after)
            self.utils.print_info("OUTPUT : ", output)
            spawn.sendline("yes")
            time.sleep(5)

        try:
            spawn.expect("#", timeout=20)
            output = str(spawn.before) + str(spawn.after)
            self.utils.print_info("OUTPUT : ", output)
            return 1
        except Exception as e:
            self.utils.print_info("Unable to execute command..")
            output = str(spawn.before) + str(spawn.after)
            self.utils.print_info("OUTPUT : ", output)
            return -1

    def send_line_and_wait(self, spawn,line, wait = 60):
        """
        - This Keyword used to gets the output from CLI
        - Default timeout is 90 seconds
        - Keyword Usage:
         - ``Send line and_wait   ${SPAWN}   ${LINE}     ${COMMAND}``
        :param spawn: Device Spawn to execute command
        :param line: CLI command to be execute
        :param wait: Collect the information in a certain time
        :return: CLI Command Output; else -1
        """
        line = line.strip()
        if spawn == None or spawn == 0:
            self.utils.print_info("No information about spawn")
            return -1
        spawn.sendline(line)
        time.sleep(wait)
        output2 = spawn.read_nonblocking(size=10000)
        if isinstance(output2, bytes):
            return output2.decode()
        else:
            return output2

    def configure_device_to_connect_to_cloud(self, device_make, ip, port, username, password, platform, server_name,
                                             vr='VR-Default', retry_count=10):
        """
        - This Keyword will configure necessary configuration in the Device to Connect to Cloud
        - Keyword Usage:
         - ``Configure Device To Connect To Cloud   ${DEVICE_MAKE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}
                                                    ${PLATFORM}  ${SERVER_NAME}``

        :param device_make: Device Make
        :param ip: Console IP Address of the Device
        :param port: Console Port
        :param username: username to access console
        :param password: Password to access console
        :param platform: device Platform example: aerohive,aerohive-switch,aerohive-fastpath,exos,voss,wing,xiqse etc
        :param server_name: Cloud Server Name to connect the device
        :param vr : VR configuration Option for EXOS device. options: VR-Default and VR-Mgmt
        :param retry_count: Retry count to check device connection status with capwap server
        :return: 1 id device successfully connected with capwap server else -1
        """
        _spawn = self.open_spawn(ip, port, username, password, platform)

        if _spawn != -1:
            if 'AEROHIVE' in device_make.upper():
                self.send(_spawn, f'capwap client server name {server_name}')
                self.send(_spawn, f'capwap client default-server-name {server_name}')
                self.send(_spawn, f'capwap client server backup name {server_name}')
                self.send(_spawn, f'no capwap client enable')
                self.send(_spawn, f'capwap client enable')
                self.send(_spawn, f'save config')
                count = 1
                while count <= retry_count:
                    self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: ", count)
                    time.sleep(10)
                    output = self.send(_spawn, f'show capwap client | include "RUN state"')

                    if 'Connected securely to the CAPWAP server' in output:
                        self.close_spawn(_spawn)
                        self.utils.print_info(f"Device Successfully Connected to {server_name}")
                        return 1
                    count +=1

                self.builtin.fail(msg=f"Device is Not Connected Successfully With CAPWAP Server : {server_name}")

            if 'EXOS' in device_make.upper():
                self.send(_spawn, f'configure iqagent server ipaddress {server_name}')
                self.send(_spawn, f'configure iqagent server vr {vr}')
                count = 1
                while count <= retry_count:
                    self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: ", count)
                    time.sleep(10)
                    output = self.send(_spawn, f'show iqagent | include "XIQ Address"')
                    output1 = self.send(_spawn, f'show iqagent | include "Status"')

                    if server_name in output and 'CONNECTED TO XIQ' in output1:
                        self.close_spawn(_spawn)
                        self.utils.print_info(f"Device Successfully Connected to {server_name}")
                        return 1
                    count +=1

                self.builtin.fail(msg=f"Device is Not Connected Successfully With Cloud Server {server_name} ")

            if 'VOSS' in device_make.upper():
                self.send(_spawn, f'enable')
                self.send(_spawn, f'configure terminal')
                self.send(_spawn, f'application')
                self.send(_spawn, f'no iqagent enable')
                self.send(_spawn, f'iqagent server {server_name}')
                self.send(_spawn, f'iqagent enable')
                self.send(_spawn, f'end')

                count = 1
                while count <= retry_count:
                    self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: ", count)
                    time.sleep(10)

                    output1 = self.send(_spawn, f'show application iqagent | include "Server Address"')
                    output2 = self.send(_spawn, f'show application iqagent status | include "Connection Status"')

                    if server_name in output1 and 'Connected' in output2:
                        self.close_spawn(_spawn)
                        self.utils.print_info(f"Device Successfully Connected to {server_name}")
                        return 1
                    count += 1

                self.builtin.fail(msg=f"Device is Not Connected Successfully With Cloud Server {server_name} ")
        else:
            self.builtin.fail(msg="Failed to Open The Spawn to Device.So Exiting the Testcase")
            return -1
    def downgrade_iqagent_voss(self, ip, port, username, password, platform):

        _spawn = self.open_spawn(ip, port, username, password, platform)

        if _spawn != -1:
            if 'VOSS' in platform:
                self.send(_spawn, f'enable')
                output=self.send(_spawn, f'ls /intflash/rc.0')
                if '  rc.0 ' in output:
                    self.utils.print_info("rc.0 file found in the device")
                else:
                    self.utils.print_info("Couldn't able to locate rc.0 file")
                    self.close_spawn(_spawn)
                    return -1
                self.send(_spawn, f'dbg enable')
                self.send(_spawn, f'config t')
                self.send(_spawn, f'application')
                output_version=self.send(_spawn, f'show application iqagent | include "Agent Version"')
                self.send(_spawn, f'no iqagent enable')
                self.send(_spawn, f'software iqagent reinstall')
                self.send(_spawn, f'iqagent enable')
                output_new_version=self.send(_spawn, f'show application iqagent | include "Agent Version"')
                self.close_spawn(_spawn)

    def  downgrade_iqagent_exos(self, ip, port, username, password, platform,url_image):

        _spawn = self.open_spawn(ip, port, username, password, platform)

        if _spawn != -1:
            if 'EXOS' in platform:
                self.send(_spawn, f'show iqagent | include Version')
                self.send(_spawn, url_image, expect_match='Do you want to install image after downloading? (y - yes, n - no, <cr> - cancel)')
                self.send(_spawn, f'yes')
                time.sleep(10)
                self.send(_spawn, f'show iqagent | include Version')
                self.close_spawn(_spawn)


        else:
            self.builtin.fail(msg="Failed to Open The Spawn to Device.So Exiting the Testcase")
            return -1

    def disconnect_device_from_cloud(self, device_make, ip, port, username, password, platform, retry_count=10):
        """
        - This Keyword Disconnect Device From Cloud
        - Keyword Usage:
         - ``Configure Device To Connect To Cloud   ${DEVICE_MAKE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}
                                                    ${PLATFORM}``

        :param device_make: Device Make
        :param ip: Console IP Address of the Device
        :param port: Console Port
        :param username: username to access console
        :param password: Password to access console
        :param platform: device Platform example: aerohive,aerohive-switch,aerohive-fastpath,exos,voss,wing,xiqse etc
        :param retry_count: Retry count to check device connection status with Cloud server
        :return: 1 id device successfully disconnected with cloud server else -1
        """
        _spawn = self.open_spawn(ip, port, username, password, platform)

        if _spawn != -1:
            if 'AEROHIVE' in device_make.upper():
                self.send(_spawn, f'no capwap client server name')
                self.send(_spawn, f'no capwap client default-server-name')
                self.send(_spawn, f'no capwap client server backup name')
                self.send(_spawn, f'no capwap client enable')
                self.send(_spawn, f'save config')
                count = 1
                while count <= retry_count:
                    self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: ", count)
                    time.sleep(10)
                    output = self.send(_spawn, f'show capwap client | include "RUN state"')

                    if 'Connected securely to the CAPWAP server' not in output:
                        self.close_spawn(_spawn)
                        self.utils.print_info(f"Device Successfully Disconnected from CAPWAP server")
                        return 1
                    count += 1

                self.builtin.fail(msg=f"Device is not Disconnected Successfully With CAPWAP Server")

            if 'EXOS' in device_make.upper():
                self.send(_spawn, f'disable iqagent', expect_match='Do you want to continue? (y/N)')
                self.send(_spawn, f'yes')
                count = 1
                while count <= retry_count:
                    self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: ", count)
                    time.sleep(10)
                    output = self.send(_spawn, f'show iqagent | include "Status"')

                    if 'CONNECTED TO XIQ' not in output:
                        self.close_spawn(_spawn)
                        self.utils.print_info(f"Device Successfully Disconnected From Cloud server")
                        return 1
                    count += 1

                self.builtin.fail(msg=f"Device is Not Disconnected Successfully From Cloud Server")

            if 'VOSS' in device_make.upper():
                self.send(_spawn, f'enable')
                self.send(_spawn, f'configure terminal')
                self.send(_spawn, f'application')
                self.send(_spawn, f'no iqagent enable')
                self.send(_spawn, f'no iqagent server')
                self.send(_spawn, f'end')

                count = 1
                while count <= retry_count:
                    self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: ", count)
                    time.sleep(10)

                    output = self.send(_spawn, f'show application iqagent status | include "Connection Status"')

                    if 'Disconnected' in output:
                        self.close_spawn(_spawn)
                        self.utils.print_info(f"Device Successfully Disconnected from Cloud server")
                        return 1
                    count += 1

                self.builtin.fail(msg=f"Device is Not Disconnected Successfully From Cloud Server")
        else:
            self.builtin.fail(msg="Failed to Open The Spawn to Device.So Exiting the Testcase")
            return -1

if __name__ == '__main__':
    from pytest_testconfig import *
    config['${TEST_NAME}'] = 'bob'
    tCli = Cli()
    #sID = tCli.open_pxssh_spawn('10.69.61.101', 'extreme', 'extreme', 22, prompt_reset=False,
    #                     disable_strict_host_key_checking=False, sync_multiplier=5)
    conn_str = "ssh extreme@10.69.61.101"
    username = 'extreme'
    password = 'extreme'
    sID = tCli.open_windows_spawn(conn_str, username, password)