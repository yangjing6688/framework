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
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend
from ExtremeAutomation.Keywords.EndsystemKeywords.EndsystemConnectionManager import EndsystemConnectionManager
from ExtremeAutomation.Utilities.deprecated import deprecated


from extauto.common.Utils import Utils
from extauto.common.CommonValidation import CommonValidation

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
        self.commonValidation = CommonValidation()
        self.net_element_types = ['VOSS', 'EXOS', 'WING-AP', 'AH-FASTPATH', 'AH-AP', 'AH-XR']
        self.end_system_types = ['MU-WINDOWS', 'MU-MAC', 'MU-LINUX', 'A3']

    def close_spawn(self, spawn, **kwargs):
        """
        - Closes a device spawn
        - Keyword Usage:
         - ``Close Spawn``

        :param spawn: device spawn
        :return: 1 if the connection is closed.  Note: an error will be raised if the connection fails to close
        """

        if spawn.split('_')[1].upper() in self.net_element_types:
            self.networkElementConnectionManager.close_connection_to_network_element(spawn)
        elif spawn.split('_')[1].upper() in self.end_system_types:
            self.endsystemConnectionManager.close_connection_to_endsystem_element(spawn)
        else:
            raise Exception("Cli_Type was not found, please use on of the following type: \n" + '\n'.join(self.net_element_types) + '\n' + '\n'.join(self.end_system_types))

        return 1

    def open_spawn(self, ip, port, username, password, cli_type, connection_method='ssh', disable_strict_host_key_checking=False, **kwargs):
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
        :param disable_strict_host_key_checking: Used to enable or disable strict host key checking
        :return: Device Prompt
        """
        self.utils.print_info(f"=================================")
        self.utils.print_info(f"IP: {ip}")
        self.utils.print_info(f"PORT: {port}")
        self.utils.print_info(f"Username: {username}")
        self.utils.print_info(f"Password: {password}")
        self.utils.print_info(f"Cli Type: {cli_type}")
        self.utils.print_info(f"Connection Method: {connection_method}")
        self.utils.print_info(f"Disable Strict Host Key Checking: {disable_strict_host_key_checking}")
        self.utils.print_info(f"=================================")

        # Generate UUID
        device_uuid = str(uuid.uuid4()) + "_" + cli_type

        if cli_type.upper() in self.net_element_types:
            self.networkElementConnectionManager.connect_to_network_element(device_uuid, ip, username, password, connection_method, cli_type.upper(), port=port, disable_strict_host_key_checking=disable_strict_host_key_checking, **kwargs)

        elif cli_type.upper() in self.end_system_types:
            self.endsystemConnectionManager.connect_to_endsystem_element(device_uuid, ip, username, password, connection_method, cli_type.upper(), port=port, **kwargs)
        else:
            raise Exception("Cli_Type was not found, please use on of the following type: \n" +  '\n'.join(
                self.net_element_types) + '\n' + '\n'.join(self.end_system_types))
        # The calls to the connect_to_<device> will check the cli_type to ensure that the correct type value was passed in and will error out in the case that
        # an unknown value was passed in.
        return device_uuid

    def send(self, spawn, line, expect_match="default", time_out="default", platform="default", **kwargs):
        """
        - This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor
        - Default timeout is 60 seconds
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
        self.utils.print_info(f"Sending command to device: {spawn}: {line}")
        result = self.networkElementCliSend.send_cmd(spawn, line, **kwargs)
        try:
            output = str(result[0].return_text)
            self.utils.print_info(f"Got response to commandf from device {spawn}: {output}")
        except Exception as e:
            self.utils.print_info("Keyword had an error: " + str(e))
        return output

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

    @deprecated("Please use the open_spawn keyword")
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

    @deprecated("Please use the close_spawn keyword")
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

    @deprecated("Please use the send keyword")
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
        for i in range(1, 6):
            self.utils.print_info( " ***** Number of attempts ", str(i))
            time.sleep(30)
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

    def clear_ssh_host_key(self):
        """
        - This keyword will clear the SSH key
        - Keyword Usage:
         - ``clear ssh host key``

        :return: None
        """

        # 'ssh-keygen -f "/home/automation/.ssh/known_hosts" -R "10.234.178.60"'
        pass

    # This needs to be fixed in order to use the new spawn
    # def reboot_switch(self, spawn, expected_output, option):
    #     """
    #     -This Keyword will reboot the switch
    #     - Keyword Usage:
    #      - ``Reboot Switch   ${SPAWN}  ${EXPECTED_OUTPUT}  ${OPTION}``
    #
    #     :param spawn: Switch Spawn
    #     :param expected_output: Expected Output
    #     :param option: Option
    #     :return: 1 if Switch Rebooted Successfully else -1
    #     """
    #     spawn.sendline('reboot')
    #     time.sleep(2)
    #     try:
    #         spawn.expect(expected_output, timeout=30)
    #         spawn.sendline(option)
    #         spawn.expect('login', timeout=300)
    #         return 1
    #     except Exception as e:
    #         self.utils.print_info("Unable to send the reboot command")
    #         return -1

    # This needs to be fixed in order to use the new spawn
    # def download_firmware_on_exos(self, spawn, image_url, vr_name, time_out=1000):
    #     """
    #     This method downloads the firmware on EXOS Switch
    #
    #     :param spawn:       spawn to exos switch
    #     :param image_url:   image location url to load exos switch with.
    #     :param vr_name:     vr_name on exos switch
    #     :return: returns output
    #     """
    #     dnld_cmd = f'download url {image_url} vr {vr_name}'
    #     self.utils.print_info("Sending download cli is   ", dnld_cmd)
    #     spawn.sendline(dnld_cmd)
    #
    #     i = spawn.expect(['Do you want to continue with download and remove existing files from internal-memory?',
    #                       'Do you want to install image after downloading?',
    #                       'y - yes, n - no',
    #                       pexpect.TIMEOUT,
    #                       pexpect.EOF], timeout=200)
    #
    #     if i == 0:
    #         time.sleep(2)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         spawn.sendline("yes")
    #         time.sleep(5)
    #
    #         j = spawn.expect(['Do you want to install image after downloading',
    #                           'y - yes, n - no',
    #                           pexpect.TIMEOUT,
    #                           pexpect.EOF], timeout=200)
    #         if j == 0 or j == 1:
    #             time.sleep(2)
    #             output = str(spawn.before) + str(spawn.after)
    #             self.utils.print_info("OUTPUT : ", output)
    #             spawn.sendline("yes")
    #             time.sleep(5)
    #
    #     if i == 1 or i == 2:
    #         time.sleep(2)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         spawn.sendline("yes")
    #         time.sleep(5)
    #
    #     self.utils.print_info("Expecting prompt in : ", int(time_out))
    #     spawn.expect("#", timeout=int(time_out))
    #     output = str(spawn.before) + str(spawn.after)
    #
    #     return output

    # This needs to be fixed in order to use the new spawn
    # def enable_disable_iqagent_on_exos(self, spawn, operation):
    #     """
    #     This method disables or enables IQAgent on EXOS Switch based on operation input
    #     - Keyword Usage:
    #      - ``Enable Disable IQAgent on Exos   ${SPAWN}  disable``
    #
    #     :param spawn:       spawn to exos switch
    #     :param operation:   perform IQAgent disable or enable.
    #     :return: returns output
    #     """
    #     if operation == "enable":
    #         self.utils.print_info("Sending IQAgent enable command to Device")
    #         spawn.sendline('enable iqagent')
    #     elif operation == "disable":
    #         self.utils.print_info("Sending IQAgent disable command to Device")
    #         spawn.sendline('disable iqagent')
    #     else:
    #         self.utils.print_info("Incorrect input..")
    #
    #     i = spawn.expect(['Do you want to continue?',
    #                       pexpect.TIMEOUT,
    #                       pexpect.EOF], timeout=30)
    #
    #     if i == 0:
    #         time.sleep(2)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         spawn.sendline("yes")
    #         time.sleep(5)
    #
    #     try:
    #         spawn.expect("#", timeout=20)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         return 1
    #     except Exception as e:
    #         self.utils.print_info("Unable to execute command..")
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         return -1

    def configure_device_to_connect_to_cloud(self, cli_type, ip, port, username, password, server_name,
                                             connection_type='ssh', vr='VR-Default', retry_count=10):
        """
        - This Keyword will configure necessary configuration in the Device to Connect to Cloud
        - Keyword Usage:
         - ``Configure Device To Connect To Cloud   ${CLI_TYPE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}  ${SERVER_NAME}``

        :param cli_type: Device Cli Type
        :param ip: Console IP Address of the Device
        :param port: Console Port
        :param username: username to access console
        :param password: Password to access console
        :param server_name: Cloud Server Name to connect the device
        :param connection_type: The connection type, will default to ssh. (ssh, telnet, console)
        :param vr : VR configuration Option for EXOS device. options: VR-Default and VR-Mgmt
        :param retry_count: Retry count to check device connection status with capwap server
        :return: 1 id device successfully connected with capwap server else -1
        On July 26 2022, it was decide to disable the verification steps for the following reason
        Depending on the order of configuration in a test case the verification check will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud
        As of July 26, 2022, this method never return a "-1" it would only return a "1"
        if the verification check passed. Since I took out the verification I am blindly
        return "1".
        """

        _spawn = self.open_spawn(ip, port, username, password, cli_type, connection_type)

        if NetworkElementConstants.OS_AHFASTPATH in cli_type.upper() or \
           NetworkElementConstants.OS_AHXR in cli_type.upper():
            self.send(_spawn, f'do Hivemanager address {server_name}')
            self.send(_spawn, f'do Application stop hiveagent')
            self.send(_spawn, f'do Application start hiveagent')
            """
            July 26, 2022
            Depending on the order of configuration this step will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud this step will fail
            It was decided to take out the verification steps from this method for now.
            We should create a verify method if the user does desire that functionality
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: ", count)
                time.sleep(10)
                hm_status = self.send(_spawn, f'do show hivemanager status | include Status')
                hm_address = self.send(_spawn, f'do show hivemanager address')

                if 'CONNECTED TO HIVEMANAGER' in hm_status and server_name in hm_address:
                    self.close_spawn(_spawn)
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1
            """
        elif NetworkElementConstants.OS_AHAP in cli_type.upper():
            self.send(_spawn, f'capwap client server name {server_name}')
            self.send(_spawn, f'capwap client default-server-name {server_name}')
            self.send(_spawn, f'capwap client server backup name {server_name}')
            self.send(_spawn, f'no capwap client enable')
            self.send(_spawn, f'capwap client enable')
            self.send(_spawn, f'save config')
            """
            July 26, 2022
            Depending on the order of configuration this step will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud this step will fail
            It was decided to take out the verification steps from this method for now.
            We should create a verify method if the user does desire that functionality
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
            """
        elif NetworkElementConstants.OS_EXOS in cli_type.upper():
            self.send(_spawn, f'configure iqagent server ipaddress {server_name}')
            self.send(_spawn, f'configure iqagent server vr {vr}')
            """
            July 26, 2022
            Depending on the order of configuration this step will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud this step will fail
            It was decided to take out the verification steps from this method for now.
            We should create a verify method if the user does desire that functionality
            
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
            """

        elif NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.send(_spawn, f'enable')
            self.send(_spawn, f'configure terminal')
            self.send(_spawn, f'application')
            self.send(_spawn, f'no iqagent enable')
            self.send(_spawn, f'iqagent server {server_name}')
            self.send(_spawn, f'iqagent enable')
            self.send(_spawn, f'end')

            """
            July 26, 2022
            Depending on the order of configuration this step will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud this step will fail
            It was decided to take out the verification steps from this method for now.
            We should create a verify method if the user does desire that functionality
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
            """
        elif NetworkElementConstants.OS_WING in cli_type.upper():
            self.send(_spawn, f'en')
            self.send(_spawn, f'config')
            self.send(_spawn, f'virtual-controller')
            self.send(_spawn, f'show adoption status')
            # Delete the policy
            self.send(_spawn, f'no nsight-policy xiq', ignore_cli_feedback=True)
            self.send(_spawn, f'commit write memory')
            # Create the new policy
            self.send(_spawn, f'nsight-policy xiq')
            self.send(_spawn, f'server host {server_name} https enforce-verification poll-work-queue')
            self.send(_spawn, f'commit write memory')
            self.send(_spawn, f'rf-domain default')
            self.send(_spawn, f'use nsight-policy xiq')
            self.send(_spawn, f'commit write memory')
            # show run nsight-policy ECIQ
        return 1

    def wait_for_configure_device_to_connect_to_cloud(self, cli_type, ip, port, username, password, server_name,
                                                     connection_type='ssh', vr='VR-Default', retry_count=10, retry_duration=30):
        """
        - This Keyword will configure necessary configuration in the Device to Connect to Cloud
        - Keyword Usage:
         - ``Configure Device To Connect To Cloud   ${CLI_TYPE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}  ${SERVER_NAME}``

        :param cli_type: Device Cli Type
        :param ip: Console IP Address of the Device
        :param port: Console Port
        :param username: username to access console
        :param password: Password to access console
        :param server_name: Cloud Server Name to connect the device
        :param connection_type: The connection type, will default to ssh. (ssh, telnet, console)
        :param vr : VR configuration Option for EXOS device. options: VR-Default and VR-Mgmt
        :param retry_count: Retry count to check device connection status with capwap server
        :return: 1 id device successfully connected with capwap server else -1
        On July 26 2022, it was decide to disable the verification steps for the following reason
        Depending on the order of configuration in a test case the verification check will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud
        As of July 26, 2022, this method never return a "-1" it would only return a "1"
        if the verification check passed. Since I took out the verification I am blindly
        return "1".
        """

        _spawn = self.open_spawn(ip, port, username, password, cli_type, connection_type)

        if NetworkElementConstants.OS_AHFASTPATH in cli_type.upper() or \
                NetworkElementConstants.OS_AHXR in cli_type.upper():
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: ", count)
                time.sleep(retry_duration)
                hm_status = self.send(_spawn, f'do show hivemanager status | include Status')
                hm_address = self.send(_spawn, f'do show hivemanager address')

                if 'CONNECTED TO HIVEMANAGER' in hm_status and server_name in hm_address:
                    self.close_spawn(_spawn)
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1
        elif NetworkElementConstants.OS_AHAP in cli_type.upper():
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

        elif NetworkElementConstants.OS_EXOS in cli_type.upper():
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

        elif NetworkElementConstants.OS_VOSS in cli_type.upper():
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
        return 1

    def downgrade_iqagent(self, ip, port, username, password, cli_type, **kwargs):
        """
               - This Keyword will downgrade iqagent
               - Keyword Usage:
                - ``Downgrade Iqagent  ${IP}   ${PORT}      ${USERNAME}       ${PASSWORD}        ${PLATFORM}

               :param ip: IP Address of the Device
               :param port: Port
               :param username: username to access console
               :param password: Password to access console
               :param cli_type: Device Cli Type
               :param url_image: image for exos device
               :return: 1 commands successfully configured  else -1
               """
        if cli_type.upper()=='VOSS':
            return self.downgrade_iqagent_voss(ip, port, username, password, cli_type, **kwargs)
        elif cli_type.upper()=='EXOS':
            count = 0
            retries = 6
            results = -1
            while count < retries:
                try:
                    results = self.downgrade_iqagent_exos(ip, port, username, password, cli_type, **kwargs)
                    break
                except Exception as e:
                    self.utils.print_info(f"Unable to downgrade IQAgent {e}, waiting 30 seconds and trying again...")
                    time.sleep(30)
                    count = count + 1
            return results
        else:
            self.utils.print_info(f"cli_type: {cli_type} doesn't need to be downgraded and isn't supported")
            return 1

    def downgrade_iqagent_voss(self, ip, port, username, password, cli_type, **kwargs):
        _spawn = self.open_spawn(ip, port, username, password, cli_type)
        if NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.send(_spawn, f'enable')
            # output=self.send(_spawn, f'ls /intflash/rc.0')
            # if '  rc.0 ' in output:
            #     self.utils.print_info("rc.0 file found in the device")
            # else:
            #     self.utils.print_info("Couldn't able to locate rc.0 file")
            #     self.close_spawn(_spawn)
            #     return -1
            self.send(_spawn, f'dbg enable')
            self.send(_spawn, f'config t')
            self.send(_spawn, f'application')
            output_version=self.send(_spawn, f'show application iqagent | include "Agent Version"')
            self.send(_spawn, f'no iqagent enable')
            self.send(_spawn, f'software iqagent reinstall')
            self.send(_spawn, f'iqagent enable')
            output_new_version=self.send(_spawn, f'show application iqagent | include "Agent Version"')
            self.close_spawn(_spawn)
            return 1
        else:
            self.builtin.fail(msg="Failed to Open The Spawn to Device. So Exiting the Testcase")
            return -1


    def downgrade_iqagent_exos(self, ip, port, username, password, cli_type, **kwargs):
        returnCode = -1
        _spawn = self.open_spawn(ip, port, username, password, cli_type)
        try:
            current_version = self.send(_spawn, f'show iqagent | include Version')
            current_version = current_version.split()[1]
            base_version = self.send(_spawn, f'show process iqagent  | include iqagent')
            base_version = base_version.split()[1]
            # Adjust the verison down to 3 numbers
            parts = base_version.split('.')
            if len(parts) > 3:
                base_version = f'{parts[0]}.{parts[1]}.{parts[2]}'

            if current_version != base_version:
                system_type = self.send(_spawn, f'show switch | include "System Type"')
                system_type = system_type.split()[2]
                self.utils.print_info(f"Getting the device type for EXOS: {system_type}")
                exos_device_type = None
                if '5320' in system_type or '5420' in system_type or '5520' in system_type:
                    exos_device_type = 'summit_arm'
                    self.utils.print_info(f'Found device type for {system_type} as {exos_device_type}')
                elif '440' in system_type or '450' in system_type or '460' in system_type:
                    exos_device_type = 'summitX'
                    self.utils.print_info(f'Found device type for {system_type} as {exos_device_type}')
                elif '435' in system_type:
                    exos_device_type = 'summitlite_arm'
                    self.utils.print_info(f'Found device type for {system_type} as {exos_device_type}')
                elif '465' in system_type or '5720' in system_type:
                    exos_device_type = 'onie'
                    self.utils.print_info(f'Found device type for {system_type} as {exos_device_type}')
                else:
                    self.utils.print_error(f'Failed to get the correct device type for {system_type}')
                    kwargs['fail_msg'] = f'Failed to get the correct device type for {system_type}'

                if exos_device_type:
                    self.utils.print_info(f"Downgrading iqagent {current_version} to base version {base_version}")
                    url_image = f'http://engartifacts1.extremenetworks.com:8081/artifactory/xos-iqagent-local-release/xmods/{base_version}/{exos_device_type}-iqagent-{base_version}.xmod'
                    self.utils.print_info(f"Sending URL: {url_image}")
                    self.send(_spawn, f'download url {url_image}', \
                              confirmation_phrases='Do you want to install image after downloading? (y - yes, n - no, <cr> - cancel)', \
                              confirmation_args='yes')

                    # Wait for the output to return downgraded version to a max of 60 seconds
                    max_tries = 60
                    count = 0

                    # Sleep for 20 seconds to allow for the download to complete
                    time.sleep(20)

                    new_version = ''
                    while 'Version' not in new_version:
                        if count == max_tries:
                            break
                        time.sleep(1)
                        new_version = self.send(_spawn, f'show iqagent | include Version')
                        count = count + 1
                    try:
                        new_version = new_version.split()[1]
                        if new_version == base_version:
                            returnCode = 1
                        else:
                            self.utils.print_error(f"Downgrading iqagent {current_version} to base version {base_version} failed!")
                            kwargs['fail_msg'] = f"Downgrading iqagent {current_version} to base version {base_version} failed!"
                    except:
                        self.utils.print_error(f"Downgrading iqagent {current_version} to base version {base_version} failed! new_version: {new_version}")
                        kwargs['pass_msg'] = f"Downgrading iqagent {current_version} to base version {base_version} failed! new_version: {new_version}"
            else:
                # We should be good as we are running the base version
                returnCode = 1
        except Exception as e :
            raise e
        finally:
            self.close_spawn(_spawn)
        self.commonValidation.validate(returnCode, 1, **kwargs)
        return returnCode

        # show iqagent - get version
        # show process iqagent - get version
        # Compare versions
        # downgrade
        # X435 - download image 10.51.1.154 summitlite_arm-iqagent-0.5.40.xmod
        # X465 (and 5720, but the minimum used should be 0.5.61) - download image 10.51.1.154 onie-iqagent-0.5.40.xmod
        # Other X4xx (440, 450, 460) - download image 10.51.1.154 summitX-iqagent-0.5.40.xmod
        # 5320,5420,5520 - download image 10.51.1.154 summit_arm-iqagent-0.5.40.xmod
        # show system | include Type
        #       System Type:      5520-24T-SwitchEngine
        #

        # if NetworkElementConstants.OS_EXOS in cli_type.upper():
        #     self.send(_spawn, f'show iqagent | include Version')
        #     self.send(_spawn, url_image, \
        #               confirmation_phrases='Do you want to install image after downloading? (y - yes, n - no, <cr> - cancel)', \
        #               confirmation_args='yes')
        #     time.sleep(10)
        #     self.send(_spawn, f'show iqagent | include Version')
        #     self.close_spawn(_spawn)
        #     return 1
        # else:
        #     self.builtin.fail(msg="Failed to Open The Spawn to Device. So Exiting the Testcase")
        #     return -1

    def disconnect_device_from_cloud(self, cli_type, ip, port, username, password, retry_count=10):
        """
        - This Keyword Disconnect Device From Cloud
        - Keyword Usage:
         - ``disconnect device from cloud  ${CLI_TYPE}  ${CONSOLE_IP}  ${PORT}  ${USERNAME}  ${PASSWORD}``

        :param cli_type: The cli type
        :param ip: Console IP Address of the Device
        :param port: Console Port
        :param username: username to access console
        :param password: Password to access console
        :param retry_count: Retry count to check device connection status with Cloud server
        :return: 1 id device successfully disconnected with cloud server else -1
        """
        _spawn = self.open_spawn(ip, port, username, password, cli_type)

        if NetworkElementConstants.OS_AHFASTPATH in cli_type.upper() or \
           NetworkElementConstants.OS_AHXR in cli_type.upper():
            self.send(_spawn, f'no Hivemanager address {server_name}')
            self.send(_spawn, f'Application stop hiveagent')
            self.send(_spawn, f'Application start hiveagent')
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: ", count)
                time.sleep(10)
                hm_status = self.send(_spawn, f'show hivemanager status | include Status')
                if 'CONNECTED TO HIVEMANAGER' not in hm_status:
                    self.close_spawn(_spawn)
                    self.utils.print_info(f"Device Successfully Disconnected from CAPWAP server")
                    return 1
                count += 1

            self.builtin.fail(msg=f"Device is not Disconnected Successfully With CAPWAP Server")

        elif NetworkElementConstants.OS_AHAP in cli_type.upper():
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

        elif NetworkElementConstants.OS_EXOS in cli_type.upper():
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

        elif NetworkElementConstants.OS_VOSS in cli_type.upper():
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

    def open_spawn_and_wait_for_cli_output(self, ip_dest, username, password, port, cmd, expected_output, os , retry_duration=30, retry_count=10):
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
        conn_str = 'telnet ' + ip_dest + " " + str(port)
        if os.lower() == 'exos':
            spawn = self.open_exos_switch_spawn(conn_str,username, password, False)
        elif os.lower() == 'voss':
            spawn = self.open_voss_spawn(conn_str, username, password, False)
        else:
            return -1
        if spawn == -1:
            return -1
        if os.lower() == 'exos':
            pass
        elif os.lower() == 'voss':
            self.send(spawn, "enable")
            self.send(spawn, "config t")
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
