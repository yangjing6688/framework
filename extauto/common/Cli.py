import re
import shlex
# import pexpect
import paramiko
import subprocess
import uuid
from platform import system
from time import sleep, time

from robot.libraries.BuiltIn import BuiltIn

from extauto.common.CommonValidation import CommonValidation
from extauto.common.Utils import Utils
from extauto.xiq.configs.device_commands import (
    AP_CAPWAP_OFF,
    AP_CAPWAP_ON,
    MAC_GET_WIFI_INTERFACE_NAME,
    MAC_TURN_ON_OFF_WIFI_INTERFACE,
    MAC_SCAN_FOR_LIST_WIFI,
    MAC_CONNECT_TO_WIFI,
    MAC_CHECK_WIFI_CONNECTION,
    MAC_IPV4_ADDRESS_FILTER,
    IFCONFIG
)
from ExtremeAutomation.Keywords.EndsystemKeywords.EndsystemConnectionManager import EndsystemConnectionManager
from datetime import datetime, timedelta
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementLacpGenKeywords import \
    NetworkElementLacpGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementMltGenKeywords import \
    NetworkElementMltGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementSpanningtreeGenKeywords import \
    NetworkElementSpanningtreeGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementVlanGenKeywords import \
    NetworkElementVlanGenKeywords
from itertools import islice
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Utilities.deprecated import deprecated

if "Window" not in system():
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
        self.networkElementMltGenKeywords = NetworkElementMltGenKeywords()
        self.networkElementLacpGenKeywords = NetworkElementLacpGenKeywords()
        self.networkElementSpanningtreeGenKeywords = NetworkElementSpanningtreeGenKeywords()
        self.networkElementVlanGenKeywords = NetworkElementVlanGenKeywords()

    def close_spawn(self, spawn, pxssh=False, **kwargs):
        """
        - Closes a device spawn
        - Keyword Usage:
        - ``Close Spawn``
        :param spawn: device spawn
        :return: 1 if the connection is closed.  Note: an error will be raised if the connection fails to close
        """

        if pxssh:
            return self.__close_pxssh_spawn(spawn)
        else:
            if spawn.split('_')[1].upper() in self.net_element_types:
                self.networkElementConnectionManager.close_connection_to_network_element(spawn)
            elif spawn.split('_')[1].upper() in self.end_system_types:
                self.endsystemConnectionManager.close_connection_to_endsystem_element(spawn)
            else:
                raise Exception("Cli_Type was not found, please use on of the following type: \n" + '\n'.join(self.net_element_types) + '\n' + '\n'.join(self.end_system_types))

        return 1

    def open_spawn(self, ip, port, username, password, cli_type, connection_method='ssh', pxssh=False,
                   pxssh_prompt_reset=False, pxssh_disable_strict_host_key_checking=False,
                   pxssh_sync_multiplier=5, **kwargs):
        """
        - This Keyword used to access device/host Prompt Using IP Address,port number, username,password and cli_type
        - Device type:
        -   VOSS
        -   EXOS
        -   WING-AP
        -   AH-FASTPATH
        -   AH-AP
        -   AH-XR
        - Endsystem:
        -   MU-WINDOWS
        -   MU-MAC
        -   MU-LINUX
        -   A3
        - Keyword Usage:
        -  ``Open Spawn     ${IP}   ${PORT}  ${USERNAME}  ${PASSWORD}   ${cli_type}``
        -  ``Open Spawn     ${IP}   ${PORT}  ${USERNAME}  ${PASSWORD}   ${cli_type}  pxssh=True``
        :param ip: Device IP address
        :param port: port number for spawn access
        :param username: User Name for spawn access
        :param password: Password for spawn access
        :param cli_type: Device Cli Type
        :param connection_method: The connection type, will default to ssh. (ssh, telnet, console)
        :param disable_strict_host_key_checking: Used to enable or disable strict host key checking
        :return: Device Prompt
        """
        self.utils.print_info("=================================")
        self.utils.print_info(f"IP: {ip}")
        self.utils.print_info(f"PORT: {port}")
        self.utils.print_info(f"Username: {username}")
        self.utils.print_info(f"Password: {password}")
        self.utils.print_info(f"Cli Type: {cli_type}")
        self.utils.print_info(f"Connection Method: {connection_method}")
        if pxssh:
            self.utils.print_info(f"pxssh: {pxssh}")
            self.utils.print_info(f"pxssh prompt reset: {pxssh_prompt_reset}")
            self.utils.print_info(f"pxssh disable strict host key checking: {pxssh_disable_strict_host_key_checking}")
            self.utils.print_info(f"pxssh sync multiplier: {pxssh_sync_multiplier}")
        self.utils.print_info("=================================")

        # Generate UUID
        device_uuid = str(uuid.uuid4()) + "_" + cli_type

        if pxssh:
            device_uuid = self.__open_pxssh_spawn(ip, username, password, port, prompt_reset=pxssh_prompt_reset,
                                           disable_strict_host_key_checking=pxssh_disable_strict_host_key_checking,
                                           sync_multiplier=pxssh_sync_multiplier)
        else:
            if cli_type.upper() in self.net_element_types:
                self.networkElementConnectionManager.connect_to_network_element(device_uuid, ip, username, password, connection_method, cli_type.upper(), port=port, **kwargs)

            elif cli_type.upper() in self.end_system_types:
                self.endsystemConnectionManager.connect_to_endsystem_element(device_uuid, ip, username, password, connection_method, cli_type.upper(), port=port, **kwargs)
            else:
                raise Exception("Cli_Type was not found, please use on of the following type: \n" +  '\n'.join(
                    self.net_element_types) + '\n' + '\n'.join(self.end_system_types))
        # The calls to the connect_to_<device> will check the cli_type to ensure that the correct type value was passed in and will error out in the case that
        # an unknown value was passed in.
        return device_uuid

    def send(self, spawn, line, expect_match="default", time_out="default", platform="default", pxssh=False,
             pxssh_timeout=3, pxssh_expected_output=None, **kwargs):
        """
        - This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor
        - Default timeout is 60 seconds
        - Keyword Usage:
        -  ``Send   ${SPAWN}        ${COMMAND}``
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
        :param ignore_cli_feedback: If set to True CLI feedback is ignored. This is set to False by default. This will ignore any errors that may be returned from running this keyword. This could be used to make sure the device is in a clean state before a test will begin. In some cases the keyword would execute with and without errors but the user doesn't want to report on the errors that may be returned
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

        if pxssh:
            output = self.__send_pxssh(spawn, line, pxssh_timeout, pxssh_expected_output)
        else:
            result = self.networkElementCliSend.send_cmd(spawn, line, **kwargs)
            try:
                output = str(result[0].return_text)
                self.utils.print_info(f"Got response to command from device {spawn}: {output}")
            except Exception as e:
                self.utils.print_info("Keyword had an error: " + str(e))
        return output

    def ping_from(self, destination, count=3):
        """
        - This method pings from the script host to the destination.
        - default count is 3
        - Keyword Usage:
        -  ``Ping From     ${DESTINATION_IP}``
        -  ``Ping From     ${DESTINATION_IP}  count=10``
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
        -  ``Ping From Spawn   ${SPAWN}  ${DESTINATION_IP}``
        -  ``Ping From Spawn   ${SPAWN}  ${DESTINATION_IP}   count=10``
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
        -  ``Httping From   ${SPAWN}  ${DESTINATION_IP}``
        -  ``Httping From   ${SPAWN}  ${DESTINATION_IP}   count=10``
        -  ``Httping From   ${SPAWN}  ${DESTINATION_IP}   count=10   timeout=10``
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
        -  ``Send Commands   ${SPAWN}  ${COMMAND_LIST}``
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
            sleep(2)
            output_end += output1

        return output_end

    def exec_shell_command(self, exec_shell_command):
        """
        - Executes a shell command
        - Keyword Usage:
        -  ``Exec Shell Command  ${SHELL_COMMAND}``
        :param exec_shell_command: Any shell command
        :return: output of the command
        """

        self.utils.print_info("Command: ", exec_shell_command)
        args = shlex.split(exec_shell_command)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = p.stdout.read()
        return result

    @deprecated("Please use the open_spawn keyword with pxssh=True")
    def open_pxssh_spawn(self, host, username, password, _port=22, prompt_reset=False,
                         disable_strict_host_key_checking=False, sync_multiplier=5):
        """
        - Opens a pxssh spawn
        - Keyword Usage:
        -  ``Openpxssh Spawn  ${HOST_NAME}  ${USER_NAME}  ${PASSWORD}``
        -  ``Openpxssh Spawn  ${HOST_NAME}  ${USER_NAME}  ${PASSWORD}   disable_strict_host_key_checking=True``
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

        return self.__open_pxssh_spawn(host, username, password, _port=_port, prompt_reset=prompt_reset,
                         disable_strict_host_key_checking=disable_strict_host_key_checking, sync_multiplier=sync_multiplier)

    def __open_pxssh_spawn(self, host, username, password, _port=22, prompt_reset=False,
                         disable_strict_host_key_checking=False, sync_multiplier=5):
        """
        - Opens a pxssh spawn
        - Keyword Usage:
        -  ``Openpxssh Spawn  ${HOST_NAME}  ${USER_NAME}  ${PASSWORD}``
        -  ``Openpxssh Spawn  ${HOST_NAME}  ${USER_NAME}  ${PASSWORD}   disable_strict_host_key_checking=True``
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

    @deprecated("Please use the close_spawn keyword with pxssh=True")
    def close_pxssh_spawn(self, pxssh_spawn):
        """
        - Closes a pxssh spawn
        - Keyword Usage:
        -  ``Close Pxssh Spawn  ${PXSSH_SPAWN}``
        :param pxssh_spawn: pxssh spawn to close
        :return: -1 in case of error else 1
        """
        return self.__close_pxssh_spawn(pxssh_spawn)

    def __close_pxssh_spawn(self, pxssh_spawn):
        """
        - Closes a pxssh spawn
        - Keyword Usage:
        -  ``Close Pxssh Spawn  ${PXSSH_SPAWN}``
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

    @deprecated("Please use the send keyword with pxssh=True")
    def send_pxssh(self, pxssh_spawn, command, timeout=3, expected_output=None):
        return self.__send_pxssh(pxssh_spawn, command, timeout=timeout, expected_output=expected_output)

    def __send_pxssh(self, pxssh_spawn, command, timeout=3, expected_output=None):
        """
        - Sends a command to pxssh spawn
        - Default Timeout value is 3 seconds
        - Keyword Usage:
        -  ``Send Pxssh  ${PXSSH_SPAWN}  ${COMMAND}``
        -  ``Send Pxssh  ${PXSSH_SPAWN}  ${COMMAND}  ${TIMEOUT}=10``
        :param pxssh_spawn: pxssh spawn
        :param command: command to send
        :param timeout: timeout to get the output
        :param expected_output: expected output to match
        :return: -1 in case of error else pxssh spawn
        """

        try:
            pxssh_spawn.sendline(command)
            if expected_output:
                pxssh_spawn.expect(expected_output)
            else:
                pxssh_spawn.prompt(timeout=timeout)
            self.utils.print_info("spawn.before: ", pxssh_spawn.before)
            self.utils.print_info("-----------------------------------")
            self.utils.print_info("spawn.after: ", pxssh_spawn.after)
            sleep(1)
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
        -  ``Open Paramiko SSH Spawn   ${HOST}  ${USERNAME}  ${PASSWORD}``
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

    def send_commands_with_comma(self, spawn, command):
        """
            Sends the full command without separating the ","
                :param spawn: spawn of DUT/host
                :param commands_list: list of DUT/Lunux command
                :return: output of the command
        """
        self.utils.print_info("Sending Commands List: ", command)
        output1 = self.send(spawn, command)
        self.utils.print_info("output is: ", output1)
        return output1

    def send_paramiko_cmd(self, spawn, cmd, timeout=10):
        """
        - Execute the commands on ssh spawn
        - Keyword Usage:
        -  ``Send Paramiko Cmd   ${SPAWN}  ${COMMAND}``
        -  ``Send Paramiko Cmd   ${SPAWN}  ${COMMAND}  timeout=${TIMEOUT_VALUE}``
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
        -  ``Close Paramiko Spawn   ${SPAWN}``
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
        -  ``Get Thput Value   ${IP}    ${CLI_SPAWN}   ${SERVER_SPAWN}``
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

        sleep(60)
        server_spawn.exec_command('TASKKILL /IM iperf.exe /F', timeout=200)
        server_spawn.exec_command('killall iperf', timeout=200)

        cli_spawn.exec_command('killall iperf', timeout=200)
        cli_spawn.exec_command('TASKKILL /IM iperf.exe /F', timeout=200)

        return stdout.readlines()

    def close_netmiko_spawn(self, spawn):
        """
        - Closing netmiko spawn object
        - Keyword Usage:
        -  ``Close Netmiko Spawn   ${SPAWN}``
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
        -  ``Get AP Version``
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

    def get_device_interface_ipv4_addr(self, spawn=None, cli_type='AH-AP', device_interface='mgt0', **kwargs):
        """
        - This method returns device interface ipv4 address based on cli type
        - Keyword Usage:
        - ``Get Device Interface IPv4 Addr    ${SPAWN}  ${CLI_TYPE}  ${Interface_name}``
        :param spawn: spawn to device
        :param cli_type: Currently this function just support AH-AP cli type, others cli types can be developed in the future
        :param device_interface: Such as mgt0, eth0
        :return: returns the interface ipv4 address if success else -1
        """
        if cli_type.upper() == 'AH-AP':
            self.utils.print_info(f"Getting AP {device_interface} IPv4 address")
            output = self.send(spawn, f'show interface {device_interface} | in "IP addr"')
            try:
                self.utils.print_info(f"AP {device_interface} IPv4 info: ", output)
                ipv4_addr = re.search(r"((?:[0-9]{1,3}\.){3}[0-9]{1,3})", output).group(1)
                self.utils.print_info(f"{device_interface} IPv4 address is: {ipv4_addr}")
                return ipv4_addr
            except Exception as e:
                self.utils.print_info(e)
                kwargs['fail_msg'] = "^-- unknown keyword or invalid input"
                self.commonValidation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info(f"The {cli_type} type is NOT supported currently")
            kwargs['fail_msg'] = f"The {cli_type} type is NOT supported currently"
            self.commonValidation.failed(**kwargs)
            return -1

    def capwap_ap_on_off(self, ip, usr, passwd, mode):
        """
        - This Keyword will enable/disable capwap mode
        - Keyword Usage:
        -  ``Capwap AP On Off``
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


    def mac_wifi_connection(self, ip, usr, passwd, ssid, ssid_pass='badpassword20*rd', mode='pass', ntimes=1):

        """
        - This Keyword will establish WiFi Connection in MAC PC/Laptop
        - Keyword Usage:
        -  ``mac_wifi_connection  ${IP}  ${USERNAME}  {PASSWORD}  ${SSID}``
        -  ``mac_wifi_connection  ${IP}  ${USERNAME}  {PASSWORD}  ${SSID}  ssid_pass=${SSID_PASSWORD}``
        :param ip: IP Address of MAC book
        :param usr: username of MAC book
        :param passwd: Password of MAC book
        :param ssid: WiFI SSID
        :param ssid_pass:  ssid Password
        :param mode: WiFi Mode
        :param ntimes: No.of times to try to establish the WiFi Connections
        :return:  connection successfully return 1 else return -1
        """

        conn = self.open_paramiko_ssh_spawn(ip, usr, passwd)
        wifi_port = self.send_paramiko_cmd(conn, MAC_GET_WIFI_INTERFACE_NAME, 10)
        self.send_paramiko_cmd(conn, MAC_TURN_ON_OFF_WIFI_INTERFACE + wifi_port + ' OFF', 30)
        self.send_paramiko_cmd(conn, MAC_TURN_ON_OFF_WIFI_INTERFACE + wifi_port + ' ON', 30)

        cnt = -1
        for i in range(1, 6):
            self.utils.print_info(" ***** Number of attempts ", str(i))
            sleep(30)
            listSSIDs = str(self.send_paramiko_cmd(conn, MAC_SCAN_FOR_LIST_WIFI, 300))
            cnt = 1 if ssid in listSSIDs else -1
            self.utils.print_info(f"The ssid match cnt is {cnt}.\n The searched ssid is {ssid}")
            if cnt == 1:
                self.utils.print_info('ssid ' + ssid + ' is found')
                break

        if cnt != 1:
            self.utils.print_info("Not able to find the SSID")
            return -1

        cn1 = False
        try_cnt = 0
        if mode == 'pass':
            while not cn1:
                rc = self.send_paramiko_cmd(conn, MAC_CONNECT_TO_WIFI + wifi_port + ' ' + ssid + ' ' + ssid_pass, 30)
                self.utils.print_info("RC is ---------" + str(rc))
                if 'Failed to join' in rc: return -1,  " Fail to Join "
                if 'not find network' in rc: return -1,  " Could not find network " + str(ssid)
                if 'Exception' in rc: return -1,  " Fail with an Exception"
                if 'Error' in rc: return -1,  " There is an Error "
                check_wifi_connection = self.send_paramiko_cmd(conn, MAC_CHECK_WIFI_CONNECTION + wifi_port, 10)
                self.utils.print_info(f"WiFi Network status: {check_wifi_connection}")
                if ssid in check_wifi_connection:
                    self.utils.print_info('Connect successfully!')
                    self.close_paramiko_spawn(conn)
                    cn1 = True
                    return 1
                else:
                    try_cnt += 1
                    self.utils.print_info(f"WiFi client doesn't connect to {ssid}, {try_cnt} attempt(s)")
                    if try_cnt == 10:
                        self.utils.print_info(f"Max attempt(s) {try_cnt}, still can NOT make client to connect to SSID: {ssid}")
                        self.close_paramiko_spawn(conn)
                        return -1

    def get_mac_hostname(self, ip, userid, passwd):
        """
        - This keyword will get the Host Name of Mac book
        - Keyword Usage:
        -  ``Get MAC Hostname  ${IP}  ${USERNAME}  {PASSWORD}``
        :param ip: IP Address of MAC book
        :param userid:  username of MAC book
        :param passwd: Password of MAC book
        :return: Host Name of mac book
        """
        conn = self.open_paramiko_ssh_spawn(ip, userid, passwd)
        hostname = self.send_paramiko_cmd(conn, 'hostname')
        self.close_spawn(conn)
        return hostname

    def get_mac_wifi_ipv4_addr(self, ip, userid, passwd):
        """
        - This keyword will get the wifi ipv4 address of Mac book
        - Keyword Usage:
         - ``Get MAC Wifi IPv4 Addr    ${IP}    ${USERNAME}    {PASSWORD}``
        :param ip: IP Address of MAC book
        :param userid:  username of MAC book
        :param passwd: Password of MAC book
        :return: wifi ipv4 address of mac book
        """
        conn = self.open_paramiko_ssh_spawn(ip, userid, passwd)
        wifi_port = self.send_paramiko_cmd(conn, MAC_GET_WIFI_INTERFACE_NAME, 10)
        mac_client_get_ipv4_addr = False
        try_cnt = 0
        while not mac_client_get_ipv4_addr:
            self.utils.print_info("Check if Mac client get IPv4 address")
            wifi_ip_detail = self.send_paramiko_cmd(conn, IFCONFIG + wifi_port)
            self.utils.print_info(f"Detail info for ifconfig {wifi_port}: \n{wifi_ip_detail}")
            wifi_ipv4 = self.send_paramiko_cmd(conn, IFCONFIG + wifi_port + MAC_IPV4_ADDRESS_FILTER)
            self.utils.print_info(f"mac wifi ipv4 address: {wifi_ipv4}")
            if not wifi_ipv4:
                try_cnt += 1
                self.utils.print_info(f"Mac client is NOT got IPV4 address: {wifi_ipv4} so far, {try_cnt} attempts to check IPV4 address")
                if try_cnt == 10:
                    self.utils.print_info(f"Max {try_cnt} attempts to check IPv4 address, still not got address: {wifi_ipv4}")
                    self.close_paramiko_spawn(conn)
                    return False
                sleep(2)
            else:
                if '169.254.' in wifi_ipv4 or 'options=201' in wifi_ipv4:
                    try_cnt += 1
                    self.utils.print_info(f"Mac client got invalid IPv4 address: {wifi_ipv4}, {try_cnt} attempts to check IPV4 address")
                    if try_cnt == 10:
                        self.utils.print_info(f"Max {try_cnt} attempts to check IPv4 address, still get invalid address: {wifi_ipv4}")
                        self.close_paramiko_spawn(conn)
                        return False
                    sleep(2)
                else:
                    mac_client_get_ipv4_addr = True
                    self.close_paramiko_spawn(conn)
        if mac_client_get_ipv4_addr:
            self.utils.print_info(f"Mac client got IPv4 address: {wifi_ipv4}")
            return wifi_ipv4

    def clear_ssh_host_key(self):
        """
        - This keyword will clear the SSH key
        - Keyword Usage:
        -  ``clear ssh host key``
        :return: None
        """

        # 'ssh-keygen -f "/home/automation/.ssh/known_hosts" -R "10.234.178.60"'
        pass

    # This needs to be fixed in order to use the new spawn
    # def reboot_switch(self, spawn, expected_output, option):
    #     """
    #     - This Keyword will reboot the switch
    #     - Keyword Usage:
    #     -  ``Reboot Switch   ${SPAWN}  ${EXPECTED_OUTPUT}  ${OPTION}``
    #
    #     :param spawn: Switch Spawn
    #     :param expected_output: Expected Output
    #     :param option: Option
    #     :return: 1 if Switch Rebooted Successfully else -1
    #     """
    #     spawn.sendline('reboot')
    #     sleep(2)
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
    #         sleep(2)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         spawn.sendline("yes")
    #         sleep(5)
    #
    #         j = spawn.expect(['Do you want to install image after downloading',
    #                           'y - yes, n - no',
    #                           pexpect.TIMEOUT,
    #                           pexpect.EOF], timeout=200)
    #         if j == 0 or j == 1:
    #             sleep(2)
    #             output = str(spawn.before) + str(spawn.after)
    #             self.utils.print_info("OUTPUT : ", output)
    #             spawn.sendline("yes")
    #             sleep(5)
    #
    #     if i == 1 or i == 2:
    #         sleep(2)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         spawn.sendline("yes")
    #         sleep(5)
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
    #     -  ``Enable Disable IQAgent on Exos   ${SPAWN}  disable``
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
    #         sleep(2)
    #         output = str(spawn.before) + str(spawn.after)
    #         self.utils.print_info("OUTPUT : ", output)
    #         spawn.sendline("yes")
    #         sleep(5)
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

    def configure_device_to_connect_to_cloud(self, cli_type, server_name, connection, vr='VR-Default', retry_count=10):
        """
        - This Keyword will configure necessary configuration in the Device to Connect to Cloud
        - Keyword Usage:
        -  ``Configure Device To Connect To Cloud   ${CLI_TYPE}   ${SERVER_NAME}  ${CONNECTION}``
        :param cli_type: Device Cli Type
        :param connection: The open connection
        :param server_name: Cloud Server Name to connect the device
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

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845 CLI Support for iqagent
        if NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.send(connection, f'do hivemanager address {server_name}')

        elif NetworkElementConstants.OS_AHXR in cli_type.upper():
            self.send(connection, 'no capwap client enable')
            self.send(connection, f'capwap client server name {server_name}')
            self.send(connection, f'capwap client default-server-name {server_name}')
            self.send(connection, f'capwap client server backup name {server_name}')
            self.send(connection, 'capwap client enable')
            self.send(connection, 'save config')

        elif NetworkElementConstants.OS_AHAP in cli_type.upper():
            self.send(connection, 'no capwap client enable')
            self.send(connection, f'capwap client server name {server_name}')
            self.send(connection, f'capwap client default-server-name {server_name}')
            self.send(connection, f'capwap client server backup name {server_name}')
            self.send(connection, 'capwap client enable')
            self.send(connection, 'save config')

        elif NetworkElementConstants.OS_EXOS in cli_type.upper():
            self.send(connection, f'configure iqagent server ipaddress {server_name}')
            self.send(connection, f'configure iqagent server vr {vr}')
            self.send(connection, 'enable iqagent')

        elif NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.send(connection, 'enable')
            self.send(connection, 'configure terminal')
            self.send(connection, 'application')
            self.send(connection, 'no iqagent enable')
            self.send(connection, f'iqagent server {server_name}')
            self.send(connection, 'iqagent enable')
            self.send(connection, 'end')

        elif NetworkElementConstants.OS_WING in cli_type.upper():
            self.send(connection, 'en')
            self.send(connection, 'self')
            self.send(connection, 'virtual-controller')
            self.send(connection, 'show adoption status')
            self.send(connection, 'end')
            self.send(connection, 'en')
            self.send(connection, 'config')
            # Delete the policy
            self.send(connection, 'no nsight-policy xiq', ignore_cli_feedback=True)
            self.send(connection, 'commit write memory')
            # Create the new policy
            self.send(connection, 'nsight-policy xiq')
            self.send(connection, f'server host {server_name} https enforce-verification poll-work-queue')
            self.send(connection, 'commit write memory')
            self.send(connection, 'rf-domain default')
            self.send(connection, 'use nsight-policy xiq')
            self.send(connection, 'commit write memory')
            # show run nsight-policy ECIQ
        return 1

    def wait_for_configure_device_to_connect_to_cloud(self, cli_type, server_name, connection, retry_count=10, retry_duration=30):
        """
        - This Keyword will configure necessary configuration in the Device to Connect to Cloud
        - Keyword Usage:
        -  ``Configure Device To Connect To Cloud   ${CLI_TYPE}   ${SERVER_NAME}  ${CONNECTION}``
        :param cli_type: Device Cli Type
        :param server_name: Cloud Server Name to connect the device
        :param connection: The open connection
        :param retry_count: Retry count to check device connection status with capwap server
        :return: 1 if device successfully connected with capwap server else -1
        On July 26 2022, it was decide to disable the verification steps for the following reason
        Depending on the order of configuration in a test case the verification check will fail.
            As an example:
            configure_device_to_connect_to_cloud, then onboard device to the cloud
        As of July 26, 2022, this method never return a "-1" it would only return a "1"
        if the verification check passed. Since I took out the verification I am blindly
        return "1".
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845 CLI Support for iqagent
        if NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: {count}")
                sleep(retry_duration)
                hm_status = self.send(connection, 'show hivemanager status | include Status')
                hm_address = self.send(connection, 'show hivemanager address')

                if 'CONNECTED TO HIVEMANAGER' in hm_status and server_name in hm_address:
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1
        elif NetworkElementConstants.OS_AHXR in cli_type.upper():
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: {count}")
                sleep(10)
                capwap_status = self.send(connection, 'show capwap client | include "RUN state"')
                capwap_server = self.send(connection, f'show capwap client | include "{server_name}"')

                if 'Connected securely to the CAPWAP server' in capwap_status and server_name in capwap_server:
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1
        elif NetworkElementConstants.OS_AHAP in cli_type.upper():
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: {count}")
                sleep(10)
                output = self.send(connection, 'show capwap client | include "RUN state"')

                if 'Connected securely to the CAPWAP server' in output:
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1

            self.builtin.fail(msg=f"Device is Not Connected Successfully With CAPWAP Server : {server_name}")

        elif NetworkElementConstants.OS_EXOS in cli_type.upper():
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: {count}")
                sleep(10)
                output = self.send(connection, 'show iqagent | include "XIQ Address"')
                output1 = self.send(connection, 'show iqagent | include "Status"')

                if server_name in output and 'CONNECTED TO XIQ' in output1:
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1

            self.builtin.fail(msg=f"Device is Not Connected Successfully With Cloud Server {server_name} ")

        elif NetworkElementConstants.OS_VOSS in cli_type.upper():
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: {count}")
                sleep(10)

                output1 = self.send(connection, 'show application iqagent | include "Server Address"')
                output2 = self.send(connection, 'show application iqagent status | include "Connection Status"')

                if server_name in output1 and 'Connected' in output2:
                    self.utils.print_info(f"Device Successfully Connected to {server_name}")
                    return 1
                count += 1

            self.builtin.fail(msg=f"Device is Not Connected Successfully With Cloud Server {server_name} ")
        return -1

    def downgrade_iqagent(self, cli_type, connection, **kwargs):
        """
        - This Keyword will downgrade iqagent
        - Keyword Usage:
        -  ``Downgrade Iqagent       ${CLI_TYPE}     ${CONNECTION}
       :param cli_type: Device Cli Type
       :param connection: The open connection
       :return: 1 commands successfully configured  else -1
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845 CLI Support for iqagent
        if cli_type.upper() == 'VOSS':
            return self.downgrade_iqagent_voss(cli_type, connection, **kwargs)
        elif cli_type.upper() == 'EXOS':
            count = 0
            retries = 6
            results = -1
            while count < retries:
                try:
                    results = self.downgrade_iqagent_exos(cli_type, connection, **kwargs)
                    break
                except Exception as e:
                    self.utils.print_info(f"Unable to downgrade IQAgent {e}, waiting 30 seconds and trying again...")
                    sleep(30)
                    count = count + 1
            return results
        else:
            self.utils.print_info(f"cli_type: {cli_type} doesn't need to be downgraded and isn't supported")
            return 1

    def downgrade_iqagent_voss(self, cli_type, connection, **kwargs):
        """
        - This Keyword will downgrade iqagent for VOSS devices
        - Keyword Usage:
        -  ``downgrade iqagent voss     ${CLI_TYPE}  ${CONNECTION}``
        :param cli_type: The cli type
        :param connection: The open connection
        :return:  1 if commands successfully configured else -1
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845 CLI Support for iqagent
        if NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.send(connection, 'enable')
            self.send(connection, 'config t')
            self.send(connection, 'application')
            self.send(connection, 'show application iqagent | include "Agent Version"')
            self.send(connection, 'no iqagent enable')
            self.send(connection, 'software iqagent reinstall')
            self.send(connection, 'iqagent enable')
            self.send(connection, 'show application iqagent | include "Agent Version"')
            return 1
        else:
            kwargs['fail_msg'] = "Failed to downgrade IQAgent "
            self.commonValidation.failed(**kwargs)
            return -1

    def downgrade_iqagent_exos(self, cli_type, connection, **kwargs):
        """
        - This Keyword will downgrade iqagent for EXOS devices
        - Keyword Usage:
        -  ``downgrade iqagent exos    ${CLI_TYPE}  ${CONNECTION}``
        :param cli_type: The cli type
        :param connection: The open connection
        :return:  1 if commands successfully configured else -1
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845 CLI Support for iqagent
        returnCode = -1
        try:
            # Make sure the iqagent is enabled
            self.send(connection, 'enable iqagent')
            current_version = self.send(connection, 'show iqagent | include Version')
            # Output:
            #   Version                             0.6.6
            #   * (CIT_32.2.0.401) 5520-24T-SwitchEngine.3 # '
            current_version = current_version.replace("Version",'').split()[0]
            base_version = self.send(connection, 'show process iqagent  | include Slot-1.iqagent')
            if 'iqagent' in base_version:
                # Output:
                #   Slot-1 iqagent          0.5.42.1    0    Ready        Tue Sep 20 13:02:14 2022  Vital
                #   * Slot-1 Stack.12 #
                base_version = base_version.replace("Slot-1 iqagent",'').split()[0]
            else:
                base_version = self.send(connection, 'show process iqagent  | include iqagent')
                # Output:
                #   iqagent          0.6.6.1     0    Ready        Fri Sep  2 13:26:44 2022  Vital
                #   * (CIT_32.2.0.401) 5520-24T-SwitchEngine.3 # '
                base_version = base_version.replace("iqagent",'').split()[0]
            # Adjust the verison down to 3 numbers
            parts = base_version.split('.')
            if len(parts) > 3:
                base_version = f'{parts[0]}.{parts[1]}.{parts[2]}'

            if current_version != base_version:
                vr = self.send(connection, 'show iqagent | include Active.VR')
                # Output:
                # X465-48W.3 # show iqagent | include Active\ VR
                # Active VR                           VR-Default
                vr = vr.replace("Active VR", '').split()[0]
                if len(vr)> 0 and vr != 'None':
                    vrString = f' vr {vr}'
                else:
                    vrString = ' vr vr-mgmt'
                system_type = self.send(connection, 'show switch | include "System Type"')
                # Output:
                # System Type:      5520-24T-SwitchEngine
                # * (CIT_32.2.0.401) 5520-24T-SwitchEngine.3 # '
                system_type = system_type.replace("System Type:",'').split()[0]
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
                    self.send(connection, f'download url {url_image}{vrString}',
                              confirmation_phrases='Do you want to install image after downloading? (y - yes, n - no, <cr> - cancel)',
                              confirmation_args='yes')

                    # Wait for the output to return downgraded version to a max of 60 seconds
                    max_tries = 60
                    count = 0

                    # Sleep for 20 seconds to allow for the download to complete
                    sleep(20)

                    new_version = ''
                    while 'Version' not in new_version:
                        if count == max_tries:
                            break
                        sleep(1)
                        new_version = self.send(connection, 'show iqagent | include Version')
                        count = count + 1
                    try:
                        new_version = new_version.split()[1]
                        if new_version == base_version:
                            returnCode = 1
                        else:
                            self.utils.print_error(f"Downgrading iqagent {current_version} to base version {base_version} failed!")
                            kwargs['fail_msg'] = f"Downgrading iqagent {current_version} to base version {base_version} failed!"
                    except Exception:
                        self.utils.print_error(f"Downgrading iqagent {current_version} to base version {base_version} failed! new_version: {new_version}")
                        kwargs['pass_msg'] = f"Downgrading iqagent {current_version} to base version {base_version} failed! new_version: {new_version}"
            else:
                # We should be good as we are running the base version
                returnCode = 1
        except Exception as e:
            raise e

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
        #     self.send(_spawn, 'show iqagent | include Version')
        #     self.send(_spawn, url_image, \
        #               confirmation_phrases='Do you want to install image after downloading? (y - yes, n - no, <cr> - cancel)', \
        #               confirmation_args='yes')
        #     sleep(10)
        #     self.send(_spawn, 'show iqagent | include Version')
        #     self.close_spawn(_spawn)
        #     return 1
        # else:
        #     self.builtin.fail(msg="Failed to Open The Spawn to Device. So Exiting the Testcase")
        #     return -1

    def disconnect_device_from_cloud(self, cli_type, connection, retry_count=10):
        """
        - This Keyword Disconnect Device From Cloud
        - Keyword Usage:
        -  ``disconnect device from cloud  ${CLI_TYPE}  ${CONNECTION}``
        :param cli_type: The cli type
        :param connection: The open connection
        :param retry_count: Retry count to check device connection status with Cloud server
        :return: 1 id device successfully disconnected with cloud server else -1
        """
        if NetworkElementConstants.OS_AHXR in cli_type.upper():
            self.send(connection, 'no capwap client server name')
            self.send(connection, 'no capwap client default-server-name')
            self.send(connection, 'no capwap client server backup name')
            self.send(connection, 'no capwap client vhm-name')
            self.send(connection, 'no capwap client enable')
            self.send(connection, 'save config')
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: {count}")
                sleep(10)
                hm_status = self.send(connection, 'show capwap client | include RUN')
                if 'RUN State' not in hm_status: # the RUN state will not be in the output, only the DISCOVERY state will be shown
                    self.utils.print_info("Device Successfully Disconnected from CAPWAP server")
                    return 1
                count += 1

            self.builtin.fail(msg="Device is not Disconnected Successfully With CAPWAP Server")

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.send(connection, 'do no Hivemanager address ')
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: {count}")
                sleep(10)
                hm_status = self.send(connection, 'show hivemanager status | include Status')
                self.utils.print_info(f"hm_status:, {hm_status}")

                if 'CONNECTED TO HIVEMANAGER' not in hm_status:
                    self.utils.print_info("Device Successfully Disconnected from CAPWAP server")
                    return 1
                count += 1

            self.builtin.fail(msg="Device is not Disconnected Successfully With CAPWAP Server")

        elif NetworkElementConstants.OS_AHAP in cli_type.upper():
            self.send(connection, 'no capwap client server name')
            self.send(connection, 'no capwap client default-server-name')
            self.send(connection, 'no capwap client server backup name')
            self.send(connection, 'no capwap client vhm-name')
            self.send(connection, 'no capwap client enable')
            self.send(connection, 'save config')
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying CAPWAP Server Connection Status On Device- Loop: {count}")
                sleep(10)
                output = self.send(connection, 'show capwap client | include "RUN state"')

                if 'Connected securely to the CAPWAP server' not in output:
                    self.utils.print_info("Device Successfully Disconnected from CAPWAP server")
                    return 1
                count += 1

            self.builtin.fail(msg="Device is not Disconnected Successfully With CAPWAP Server")

        elif NetworkElementConstants.OS_EXOS in cli_type.upper():
            self.send(connection, 'configure iqagent server ipaddress none')
            self.send(connection, 'configure iqagent server vr none')
            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: {count}")
                sleep(10)
                output = self.send(connection, 'show iqagent | include "Status"')

                if 'CONNECTED TO XIQ' not in output:
                    self.utils.print_info("Device Successfully Disconnected From Cloud server")
                    return 1
                count += 1

            self.builtin.fail(msg="Device is Not Disconnected Successfully From Cloud Server")

        elif NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.send(connection, 'enable')
            self.send(connection, 'configure terminal')
            self.send(connection, 'application')
            self.send(connection, 'no iqagent enable')
            self.send(connection, 'default iqagent server')
            self.send(connection, 'end')

            count = 1
            while count <= retry_count:
                self.utils.print_info(f"Verifying Server Connection Status On Device- Loop: {count}")
                sleep(10)

                output = self.send(connection, 'show application iqagent status | include "Connection Status"')

                if 'Disconnected' in output:
                    self.utils.print_info("Device Successfully Disconnected from Cloud server")
                    return 1
                count += 1

            self.builtin.fail(msg="Device is Not Disconnected Successfully From Cloud Server")

        elif NetworkElementConstants.OS_WING in cli_type.upper():
            # These commands fail internally if there is a failure sending them
            self.send(connection, 'en')
            self.send(connection, 'config')
            # Delete the policy
            self.send(connection, 'no nsight-policy xiq', ignore_cli_feedback=True)
            self.send(connection, 'commit write memory')
            return 1
        return -1

    def wait_for_cli_output(self, spawn, cmd, expected_output, retry_duration=30, retry_count=10):
        """
        - This Keyword will Helps to Wait till getting expected output based on retry duration
        - Retry duration by default 30 seconds
        - Retry Count by default 10
        - Keyword Usage:
        -  ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}``
        -  ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60``
        -  ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60  ${COUNT}=15``
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
                sleep(retry_duration)
            count += 1
        self.utils.print_info("Unable to get the expected output. Please check.")
        return -1

    def enable_debug_mode_iqagent(self, ip, username, password, cli_type, port=22, disable_strict_host_key_checking=False, **kwargs):
        """
        - This Keyword enables debug mode for IQagent for VOSS/EXOS
        - Keyword Usage:
        -  ``Enable Debug Mode Iqagent   ${IP}  ${PORT}  ${USERNAME}  ${PASSWORD}  ${CLI_TYPE}``
        :param ip: IP Address of the Device
        :param port: Port
        :param username: username to access console
        :param password: Password to access console
        :param cli_type: device Platform example: exos,voss
        :return: _spawn Device Prompt without '#' if function call is successful else -1
        """

        if cli_type.lower() not in ["exos", "voss"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1

        spawn = self.__open_pxssh_spawn(ip, username, password, disable_strict_host_key_checking=disable_strict_host_key_checking, _port=port)

        if spawn == -1:
            kwargs["fail_msg"] = "Failed to Open The Spawn to Device.So Exiting the Testcase"
            self.commonValidation.fault(**kwargs)
            return -1
        
        if 'EXOS' in cli_type.upper():
            self.send_pxssh(spawn, 'disable cli paging')
            self.send_pxssh(spawn, 'debug iqagent show log hive-agent tail')

        elif 'VOSS' in cli_type.upper():
            self.send_pxssh(spawn, 'enable')
            self.send_pxssh(spawn, 'configure terminal')
            self.send_pxssh(spawn, 'trace level 261 3')
            self.send_pxssh(spawn, 'trace screen enable')

        kwargs["pass_msg"] = f"Successfully opened a spawn to '{ip}' and enabled iqagent debug mode."
        self.commonValidation.passed(**kwargs)
        return spawn

    def send_line_and_wait(self, spawn, line, wait=60):
        """
        - This Keyword used to gets the output from CLI
        - Default timeout is 90 seconds
        - Keyword Usage:
        -  ``Send line and_wait   ${SPAWN}   ${LINE}     ${COMMAND}``
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
        sleep(wait)
        output2 = spawn.read_nonblocking(size=100000000)
        if isinstance(output2, bytes):
            return output2.decode()
        else:
            return output2

    def get_ports_from_dut(self, dut, **kwargs):
        """
        - This Keyword gets ports for EXOS and VOSS from CLI
        :param dut:
        :return: CLI Command Output
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842 Add CLI support for all ports
        self.close_connection_with_error_handling(dut)
        self.networkElementConnectionManager.connect_to_network_element_name(dut.name)
        output = None
        if dut.cli_type.upper() == "EXOS":
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging', max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports info', max_wait=10, interval=2)[
                0].return_text
            output = re.findall(r"\r\n(\d+)\s+", output)

        elif dut.cli_type.upper() == "VOSS":
            output = \
                self.networkElementCliSend.send_cmd(dut.name, "show int gig int | no-more", max_wait=10,
                                                    interval=2)[
                    0].return_text
            output = re.findall(r"\r\n(\d+/\d+)\s+", output)

        self.close_connection_with_error_handling(dut)
        if not output:
            kwargs["fail_msg"] = "get_ports_from_dut() failed. "
            self.commonValidation.failed(**kwargs)
        kwargs['pass_msg'] = f"Ports from dut: {output}"
        self.commonValidation.passed(**kwargs)
        return output

    def get_port_list_from_dut_without_not_present_ports(self, dut, **kwargs):
        """
        - This Keyword gets ports for EXOS and VOSS from CLI and than remove "not present" ports
        :param dut: the dut, e.g. tb.dut1
        :return: CLI Command Output
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842 Add CLI support for all ports
        if dut.cli_type.upper() == "VOSS":

            sleep(10)
            self.networkElementCliSend.send_cmd(dut.name, 'enable',
                                 max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show int gig int | no-more',
                                          max_wait=10, interval=2)

            p = re.compile(r'^\d+\/\d+', re.M)
            match_port = re.findall(p, output[0].return_text)
            self.utils.print_info(f"{match_port}")

            # remove elements with two /
            p2 = re.compile(r'\d+\/\d+\/\d+', re.M)
            filtered = [port for port in match_port if not p2.match(port)]
            kwargs['pass_msg'] = f"Ports from VOSS without 'elements with two /': {filtered}"
            self.commonValidation.passed(**kwargs)
            return filtered

        elif dut.cli_type.upper() == "EXOS":

            sleep(10)
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                 max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports info',
                                          max_wait=20, interval=5)
            p = re.compile(r'^\d+:\d+', re.M)
            match_port = re.findall(p, output[0].return_text)
            is_stack = True
            if len(match_port) == 0:
                is_stack = False
                p = re.compile(r'^\d+', re.M)
                match_port = re.findall(p, output[0].return_text)

            # Remove "not present" ports
            if is_stack:
                p_notPresent = re.compile(r'^\d+:\d+.*NotPresent.*$', re.M)
            else:
                p_notPresent = re.compile(r'^\d+.*NotPresent.*$', re.M)
            parsed_info = re.findall(p_notPresent, output[0].return_text)

            for port in parsed_info:
                port_num = re.findall(p, port)
                match_port.remove(port_num[0])
            kwargs['pass_msg'] = f"Ports from EXOS without 'not present' ports: {match_port}"
            self.commonValidation.passed(**kwargs)
            return match_port

    def set_lldp(self, dut, ports, action="enable", **kwargs):
        """
         - This keyword will set lldp on VOSS and EXOS in CLI
        :return:
        """
        self.close_connection_with_error_handling(dut)
        self.networkElementConnectionManager.connect_to_network_element_name(dut.name)

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2838 CDP Support
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2839 LLDP Support for VOSS
        if dut.cli_type.upper() == "EXOS":
            if action == "enable":
                self.networkElementCliSend.send_cmd(dut.name, 'enable cdp ports all', max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, 'enable edp ports all', max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, 'enable lldp ports all', max_wait=10, interval=2)
            elif action == "disable":
                self.networkElementCliSend.send_cmd(dut.name, 'disable cdp ports all', max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, 'disable edp ports all', max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, 'disable lldp ports all', max_wait=10, interval=2)

        elif dut.cli_type.upper() == "VOSS":
            self.networkElementCliSend.send_cmd(dut.name, "enable", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "configure terminal", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(
                dut.name, f"interface gigabitEthernet {ports[0]}-{ports[-1]}", max_wait=10, interval=2)
            cmd_action = f"lldp port {ports[0]}-{ports[-1]} cdp enable"
            if action == "enable":
                self.networkElementCliSend.send_cmd(dut.name, "no auto-sense enable", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, "no fa enable", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, cmd_action, max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, "fa enable", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(dut.name, "auto-sense enable", max_wait=10, interval=2)
            elif action == "disable":
                self.networkElementCliSend.send_cmd(dut.name, "no " + cmd_action, max_wait=10, interval=2)

        self.close_connection_with_error_handling(dut)
        kwargs['pass_msg'] = "set_lldp() keyword passed."
        self.commonValidation.passed(**kwargs)

    def bounce_IQAgent(self, dut, xiq_ip_address=None, connect_to_dut=True, disconnect_from_dut=True, wait=True,
                       xiq=None, **kwargs):
        """
         - This keyword will bounce IQAgent for VOSS and EXOS in CLI
        :return:
        """

        if connect_to_dut:
            self.close_connection_with_error_handling(dut)
            self.networkElementConnectionManager.connect_to_network_element_name(dut.name)

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845 CLI Support for iqagent
        if dut.cli_type.upper() == "EXOS":
            self.networkElementCliSend.send_cmd(dut.name, 'disable iqagent', max_wait=10, interval=2,
                                                confirmation_phrases='Do you want to continue?',
                                                confirmation_args='Yes')
            if xiq_ip_address:
                self.networkElementCliSend.send_cmd(
                    dut.name, f"configure iqagent server ipaddress {xiq_ip_address}", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'enable iqagent', max_wait=10, interval=2)

        elif dut.cli_type.upper() == "VOSS":
            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'configure terminal', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'application', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'no iqagent enable', max_wait=10, interval=2)
            if xiq_ip_address:
                self.networkElementCliSend.send_cmd(
                    dut.name, f'iqagent server {xiq_ip_address}', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'iqagent enable', max_wait=10, interval=2)

        if disconnect_from_dut:
            self.close_connection_with_error_handling(dut)
            kwargs['pass_msg'] = "bounce_IQAgent() keyword passed."
            self.commonValidation.passed(**kwargs)
        if wait and xiq is not None:
            xiq.xflowscommonDevices.wait_until_device_online(dut.serial)
            kwargs['pass_msg'] = "bounce_IQAgent() keyword passed. Successfully waited until device online."
            self.commonValidation.passed(**kwargs)

    def get_the_number_of_ports_from_cli(self, dut, **kwargs):
        """
         - This keyword gets the number of ports for EXOS and VOSS from CLI
        :return: the number of ports
        """
        self.close_connection_with_error_handling(dut)
        self.networkElementConnectionManager.connect_to_network_element_name(dut.name)

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842 Add CLI support for all ports
        if dut.cli_type.upper() == "VOSS":

            self.networkElementCliSend.send_cmd(dut.name, 'enable',
                                                max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show int gig int | no-more',
                                                         max_wait=10, interval=2)
            p = re.compile(r'^\d+\/\d+\/?\d*', re.M)
            match_port = re.findall(p, output[0].return_text)
            self.utils.print_info(f"{match_port}")
            no_ports = len(match_port)
            no_ports = int(no_ports)

        elif dut.cli_type.upper() == "EXOS":
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                                max_wait=10)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports vlan',
                                                         max_wait=10)
            output = output[0].return_text
            match_port = re.findall(r'(\d+)\s+\w+', output)
            no_ports = len(match_port)
            no_ports = int(no_ports)

        self.utils.print_info(f'Number of ports for this switch is {no_ports}')
        self.close_connection_with_error_handling(dut)
        kwargs['pass_msg'] = f'Number of ports for this switch is {no_ports}'
        self.commonValidation.passed(**kwargs)
        return no_ports

    def verify_vlan_config_on_switch(self, onboarded_switch, port_vlan_mapping, logger, **kwargs):
        """
         - This keyword will verify vlan config on switch in CLI
        :return: Device ports speed dictionary
        """
        self.close_connection_with_error_handling(onboarded_switch)
        self.networkElementConnectionManager.connect_to_network_element_name(onboarded_switch.name)

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2869
        logger.info("Wait 120 seconds for the configuration of the ports to update on the dut")

        start_time = time()
        while time() - start_time < 120:

            if onboarded_switch.cli_type.upper() == "EXOS":
                try:
                    for port, vlan in port_vlan_mapping.items():
                        output = self.networkElementCliSend.send_cmd(onboarded_switch.name, f'show vlan ports {port}',
                                                      max_wait=10, interval=2)[0].return_text
                        assert re.search(fr"\r\nVLAN_{str(vlan).zfill(4)}\s+{vlan}\s+", output)
                except Exception as exc:
                    logger.info(f"Sleep 10s...\n{repr(exc)}")
                    sleep(10)
                else:
                    logger.info("Configuration successfully updated on the dut")
                    break

            elif onboarded_switch.cli_type.upper() == "VOSS":
                try:
                    output = self.networkElementCliSend.send_cmd(onboarded_switch.name, 'show vlan members',
                                                  max_wait=10, interval=2)[0].return_text

                    for port, vlan in port_vlan_mapping.items():
                        assert re.search(fr"\r\n{vlan}\s+{port}\s+", output)

                except Exception as exc:
                    logger.info(f"Sleep 10s...\n{repr(exc)}")
                    sleep(10)
                else:
                    logger.info("Configuration successfully updated on the dut")
                    break
        else:
            raise AssertionError("The configuration did not update on the dut after 120 seconds")

        self.close_connection_with_error_handling(onboarded_switch)
        kwargs['pass_msg'] = 'verify_vlan_config_on_switch() keyword passed'
        self.commonValidation.passed(**kwargs)

    def no_channel_enable_on_all_ports(self, onboarded_switch, **kwargs):
        """
         - This keyword sends 'no channelize enable' on all ports in CLI
        :return:
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842 Add CLI support for all ports
        output = self.networkElementCliSend.send_cmd(onboarded_switch.name, 'show interface GigabitEthernet channelize',
                                      max_wait=10,
                                      interval=2)[0].return_text
        match_port = re.findall(r"(\d+)\/(\d+)\s+(false|true)\s+[a-zA-Z0-9]+", output)

        for port in match_port:
            if port[2] == "true":
                command = "interface GigabitEthernet " + port[0] + "/" + port[1] + "/1"
                self.networkElementCliSend.send_cmd(onboarded_switch.name, command)
                self.networkElementCliSend.send_cmd(onboarded_switch.name, 'no channelize enable',
                                     confirmation_phrases='Do you wish to continue (y/n) ?',
                                     confirmation_args='y')
        kwargs['pass_msg'] = 'no_channel_enable_on_all_ports() passed'
        self.commonValidation.passed(**kwargs)

    def get_device_port_status(self, networkElementCliSend=None, dut=None, **kwargs):
        """
         - This keyword gets device ports status from CLI
        :return: Device ports status dictionary
        """
        if networkElementCliSend is None or dut is None:
            return
        # get the required information from the device CLI
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842 Add CLI support for all ports
        if dut.cli_type.upper() == 'VOSS':
            sleep(10)
            output = networkElementCliSend.send_cmd(
                dut.name, 'show interfaces gigabitEthernet name | no-more', max_wait=10, interval=2)
            # get a list of all the ports from the device
            p = re.compile(r'^\d+\/\d+', re.M)
            match_port = re.findall(p, output[0].return_text)
            # search the port status values in the command output
            p = re.compile(r'(?:up|down)', re.M)
            match_cli_port_status = re.findall(p, output[0].return_text)

            # get a dictionary with ports as the keys and their corresponding speeds as the values
            cli_ports_status = dict(zip(match_port, match_cli_port_status))
        elif dut.cli_type.upper() == 'EXOS':
            sleep(10)
            networkElementCliSend.send_cmd(dut.name, 'disable cli refresh', max_wait=10, interval=2)
            networkElementCliSend.send_cmd(dut.name, 'disable cli paging', max_wait=10, interval=2)
            output = networkElementCliSend.send_cmd(dut.name, 'show ports', max_wait=10, interval=2)
            # get a list of all the ports from the device
            match_port = re.findall(r"\r\n(\d+)\s+", output[0].return_text)
            cli_ports_status={}
            for port in match_port:
                row_text = re.search(fr"\r\n{port}\s.*\r\n", output[0].return_text).group(0)
                cli_ports_status[port] = "up" if re.search(r"\s+A\s+", row_text) else "down"

        self.utils.print_info("****************** Device ports status dictionary: ******************")
        self.utils.print_info(cli_ports_status)
        kwargs['pass_msg'] = f'get_device_port_status() passed. Device ports status dictionary: {cli_ports_status}'
        self.commonValidation.passed(**kwargs)
        return cli_ports_status

    def get_device_ports_speed(self, networkElementCliSend=None, dut=None, **kwargs):
        """
         - This keyword gets device ports speed from CLI
        :return: Device ports speed dictionary
        """
        if networkElementCliSend is None or dut is None:
            return

        match_port = None
        device_ports_speed = None

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842 Add CLI support for all ports
        # get the required information from the device CLI
        if dut.cli_type.upper() == 'VOSS':
            output = networkElementCliSend.send_cmd(dut.name, 'show interfaces gigabitEthernet name | no-more', max_wait=10, interval=2)

            # get a list of all the ports from the device
            p = re.compile(r'^\d+\/\d+', re.M)
            match_port = re.findall(p, output[0].return_text)

            # search the speed values in the command output
            p = re.compile(r'(?:half|full)\s+(\d+)', re.M)
            match_device_ports_speed = re.findall(p, output[0].return_text)

            # get a dictionary with ports as the keys and their corresponding speeds as the values
            device_ports_speed = dict(zip(match_port, match_device_ports_speed))
        elif dut.cli_type.upper() == 'EXOS':
            networkElementCliSend.send_cmd(dut.name, 'disable cli refresh', max_wait=10, interval=2)
            networkElementCliSend.send_cmd(dut.name, 'disable cli paging', max_wait=10, interval=2)
            output = networkElementCliSend.send_cmd(dut.name, 'show ports', max_wait=10, interval=2)

            # get a list of all the ports from the device
            p = re.compile(r'^\d+', re.M)
            match_port = re.findall(p, output[0].return_text)

            # search the speed values in the command output (the link state is needed in the result
            # because the speed is not shown if the port is down)
            p = re.compile(r'([ARNPLDdB]+\s\s\s\s\s\s(?:\d+G?)?)', re.M)
            match_port_link_state_speed = re.findall(p, output[0].return_text)

            # refine the values from the list
            for i in range(len(match_port_link_state_speed)):
                speed = re.search(r'\d+', match_port_link_state_speed[i])
                unit = re.search(r'G', match_port_link_state_speed[i])

                # if the speed value is not present set it as "0"
                if speed is None:
                    speed = "0"
                else:
                    # if a 'G' is found next to the speed value, transform it to Mbps
                    if unit is not None:
                        speed = str(int(speed.group(0)) * 1000)
                    else:
                        speed = speed.group(0)

                # replace the current value in the list with the speed value
                match_port_link_state_speed[i] = speed

            match_device_ports_speed = match_port_link_state_speed

            # get a dictionary with ports as the keys and their corresponding speeds as the values
            device_ports_speed = dict(zip(match_port, match_device_ports_speed))

        self.utils.print_info("****************** Device port list: ******************")
        self.utils.print_info(match_port)

        self.utils.print_info("****************** Device ports speed dictionary: ******************")
        self.utils.print_info(device_ports_speed)
        kwargs['pass_msg'] = f'get_device_ports_speed() passed. Device ports speed dictionary:{device_ports_speed}'
        self.commonValidation.passed(**kwargs)
        return device_ports_speed

    def clear_counters(self, dut, first_port=None, second_port=None, **kwargs):
        """
         - This keyword will clear counters for EXOS and VOSS in CLI
        Args:
         dut: e.g. tb.dut1
         first_port: e.g. self.tb.dut1_tgen_port_a.ifname
         second_port: e.g. self.tb.dut1_tgen_port_b.ifname
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2846
        if dut.cli_type.upper() == "EXOS":
            self.networkElementCliSend.send_cmd(
                dut.name, "clear counters ports all", max_wait=10, interval=2)
        elif dut.cli_type.upper() == "VOSS":
            self.networkElementCliSend.send_cmd(
                dut.name, f"clear-stats port {first_port},{second_port}", max_wait=10, interval=2)
        kwargs['pass_msg'] = 'clear_counters() passed.'
        self.commonValidation.passed(**kwargs)

    def get_received_traffic_list_from_dut(self, dut, first_port, second_port, **kwargs):
        """
        This keyword gets the received traffic from ports visible in CLI
        Args:
         dut: e.g. tb.dut1
         first_port: e.g. self.tb.dut1_tgen_port_a.ifname
         second_port: e.g. self.tb.dut1_tgen_port_b.ifname
        return: received traffic list
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2847
        if dut.cli_type.upper() == "VOSS":
            sleep(10)

            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(
                dut.name, f'show interfaces gigabitEthernet statistics {first_port},{second_port}', max_wait=10,
                interval=2)

            sleep(2)
            self.utils.print_info(output[0].return_text)
            p = re.compile(r'(^\d+\/\d+)\s+(\d+)', re.M)
            match_port = re.findall(p, output[0].return_text)
            self.utils.print_info(f"{match_port}")

            received_traffic_list = []
            received_traffic_list.append(match_port[0][1])
            received_traffic_list.append(match_port[1][1])

            self.utils.print_info(f"received_traffic for port {first_port} is {match_port[0][1]} octets")
            self.utils.print_info(f"received_traffic for port {second_port} is {match_port[1][1]} octets")

        elif dut.cli_type.upper() == "EXOS":
            sleep(10)
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, f'show port {first_port},{second_port} statistics no-refresh',
                                            max_wait=10,
                                            interval=2)
            self.utils.print_info(output[0].return_text)
            p = re.compile(r'(^\d+)\s+(\D+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', re.M)
            match_port = re.findall(p, output[0].return_text)
            self.utils.print_info(f"{match_port}")

            received_traffic_list = []
            received_traffic_list.append(match_port[0][5])
            received_traffic_list.append(match_port[1][5])

            self.utils.print_info(f"received_traffic for port {first_port} is {match_port[0][5]} octets")
            self.utils.print_info(f"received_traffic for port {second_port} is {match_port[1][5]} octets")
        kwargs['pass_msg'] = f'get_received_traffic_list_from_dut() passed. Received traffic list: {received_traffic_list}'
        self.commonValidation.passed(**kwargs)
        return received_traffic_list

    def get_transmitted_traffic_list_from_dut(
            self, dut, first_port, second_port, **kwargs):
        """
         - This keyword gets the transmitted traffic from ports visible in CLI
         Args:
         dut: e.g. tb.dut1
         first_port: e.g. self.tb.dut1_tgen_port_a.ifname
         second_port: e.g. self.tb.dut1_tgen_port_b.ifname
        :return: transmitted traffic list
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2847
        if dut.cli_type.upper() == "VOSS":
            sleep(10)

            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(
                dut.name, f'show interfaces gigabitEthernet statistics {first_port},{second_port}', max_wait=10,
                interval=2)

            sleep(2)
            self.utils.print_info(output[0].return_text)
            p = re.compile(r'(^\d+\/\d+)\s+(\d+)\s+(\d+)', re.M)
            match_port = re.findall(p, output[0].return_text)
            self.utils.print_info(f"{match_port}")

            transmitted_traffic_list = []
            transmitted_traffic_list.append(match_port[0][2])
            transmitted_traffic_list.append(match_port[1][2])

            self.utils.print_info(f"transmitted traffic for port {first_port} is {match_port[0][2]} octets")
            self.utils.print_info(f"transmitted traffic for port {second_port} is {match_port[1][2]} octets")

            self.utils.print_info("list from dut is ", transmitted_traffic_list)

        elif dut.cli_type.upper() == "EXOS":
            sleep(10)
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                 max_wait=10, interval=2)
            output = self.networkElementCliSend.send_cmd(dut.name, f'show port {first_port},{second_port} statistics no-refresh',
                                          max_wait=10, interval=2)
            self.utils.print_info(output[0].return_text)
            p = re.compile(r'(^\d+)\s+(\D+)\s+(\d+)\s+(\d+)', re.M)
            match_port = re.findall(p, output[0].return_text)
            self.utils.print_info(f"{match_port}")

            transmitted_traffic_list = []
            transmitted_traffic_list.append(match_port[0][3])
            transmitted_traffic_list.append(match_port[1][3])

            self.utils.print_info(f"transmitted_traffic_list for port {first_port} is {match_port[0][3]} octets")
            self.utils.print_info(f"transmitted_traffic_list for port {second_port} is {match_port[1][3]} octets")
        kwargs['pass_msg'] = 'get_transmitted_traffic_list_from_dut() passed.'
        self.commonValidation.passed(**kwargs)
        return transmitted_traffic_list

    def close_connection_with_error_handling(self, dut):
        """Method that makes sure the connection to a dut is closed.
        Args:
            dut (dict): the dut, e.g. tb.dut1
        """
        try:
            self.networkElementConnectionManager.close_connection_to_network_element(dut.name)
        except Exception:
            pass

    def verify_path_cost_on_device(self, device, port, expected_path_cost, mode="mstp", retries=10, step=60, **kwargs):
        """Method that verifies the path cost on a specific port of a given device.
        Args:
            device (dict): the device, e.g. tb.dut1
            port (str): the port of the device
            expected_path_cost (int): the expected path cost value
            mode (str, optional): the stp mode. Defaults to "mstp".
            retries (int, optional): the number of retries. Defaults to 10.
            step (int, optional): seconds to sleep between retries. Defaults to 60.
        Returns:
            int: 1 if the function call has succeeded else -1
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2848
        for _ in range(retries):
            try:

                self.close_connection_with_error_handling(device)
                self.networkElementConnectionManager.connect_to_network_element_name(device.name)

                if NetworkElementConstants.OS_AHFASTPATH in device.cli_type.upper():

                    output = self.networkElementCliSend.send_cmd(
                        device.name, f'show spanning-tree mst port detailed 0 {port}', max_wait=10, interval=2)[
                        0].return_text
                    path_cost_match = re.search(r"\r\nPort Path Cost\.+\s+(\d+)", output)
                    external_path_cost_match = re.search(r"\r\nExternal Port Path Cost\.+\s+(\d+)", output)
                    assert path_cost_match or external_path_cost_match

                    for path_cost_match in [path_cost_match, external_path_cost_match]:
                        try:
                            found_path_cost = int(path_cost_match.group(1))
                            self.utils.print_info(f"Found path_cost='{found_path_cost}' for port='{port}'")
                            assert int(expected_path_cost) == found_path_cost, \
                                f"Found path cost for port='{port}' is {found_path_cost}" \
                                f" but expected {expected_path_cost}"
                        except Exception:
                            continue
                        else:
                            kwargs["pass_msg"] = f"Successfully found the path cost correctly set on port='{port}' to {expected_path_cost}"
                            self.commonValidation.passed(**kwargs)
                            return 1
                    else:
                        assert False, "Failed to find the path cost correctly configure for port='{port}'"

                else:

                    if NetworkElementConstants.OS_VOSS in device.cli_type.upper():
                        output = self.networkElementCliSend.send_cmd(
                            device.name, f'show spanning-tree {mode} port config {port}', max_wait=10, interval=2)[
                            0].return_text
                        path_cost_match = re.search(r"\r\nCist Port cost\s+:\s*(\d+)\s*\r\n", output)

                    elif NetworkElementConstants.OS_EXOS in device.cli_type.upper():
                        output = self.networkElementCliSend.send_cmd(
                            device.name, f'show stpd s0 ports {port} detail', max_wait=10, interval=2)[
                            0].return_text
                        path_cost_match = re.search(r"\tPath Cost:\s(\d+)\r\n", output)

                    assert path_cost_match, f"Failed to match get the path cost of port='{port}' from dut {device.name}"
                    found_path_cost = int(path_cost_match.group(1))
                    self.utils.print_info(f"Found path_cost='{found_path_cost}' for port='{port}'")

                    assert int(expected_path_cost) == found_path_cost, \
                        f"Found path cost for port='{port}' is {found_path_cost}" \
                        f" but expected {expected_path_cost}"

                    kwargs["pass_msg"] = f"Successfully found the path cost correctly set on port='{port}' to {expected_path_cost}"
                    self.commonValidation.passed(**kwargs)
                    return 1

            except Exception as exc:
                self.utils.print_info(repr(exc))
                self.utils.wait_till(timeout=step)
            finally:
                self.close_connection_with_error_handling(device)
        else:
            kwargs["fail_msg"] = f"Failed to verify the path cost of port='{port}' on this dut\n{device}"
            self.commonValidation.failed(**kwargs)
            return -1

    def verify_port_removed_from_vlan(self, dut, port, port_type, vlan=None, allowed_vlans="all", **kwargs):
        """Method that verifies if given port is removed from a specific vlan of a switch.
        Currently this method supports only devices with cli_type - exos (standalone and stack) or voss.
        Args:
            dut (dict): the dut, e.g. tb.dut1
            port (str): the port of the switch
            port_type (str): the port type
            vlan (str, optional): the vlan which is not expected to be found (this argument is used only when cli_type is voss). Defaults to None.
            allowed_vlans (str, optional): the allowed vlans (should be used when port_type is "trunk"). Defaults to "all".
        Returns:
            int: 1 if the function call has succeeded else -1
        """
        try:
            self.close_connection_with_error_handling(dut)
            self.networkElementConnectionManager.connect_to_network_element_name(dut.name)

            # TODO: https://jira.extremenetworks.com/browse/AIQ-2849
            if NetworkElementConstants.OS_EXOS in dut.cli_type.upper():
                if port_type == "access":
                    try:
                        output = self.networkElementCliSend.send_cmd(
                            dut.name, f'show vlan ports {port}', expect_error=True, max_wait=10, interval=2)[0].return_text
                    except Exception as exc:
                        self.utils.print_info(f"Successfully verified the {port} port is not member of any VLANs: {repr(exc)}")
                    else:
                        expected_error_message = "Error: The specified ports are not members of any VLANs."
                        assert expected_error_message in output

                elif port_type == "trunk":

                    output = self.networkElementCliSend.send_cmd(
                        dut.name, f'show vlan ports {port}', max_wait=10, interval=2)[0].return_text

                    if allowed_vlans != "all":
                        assert re.search(fr"\r\nVLAN_{allowed_vlans.zfill(4)}\s+{allowed_vlans}\s+", output)
                    else:
                        assert re.search(r"\r\nDefault\s+1\s", output)

            elif NetworkElementConstants.OS_VOSS in dut.cli_type.upper():

                output = self.networkElementCliSend.send_cmd(dut.name, 'show vlan members',
                                              max_wait=10, interval=2)[0].return_text
                assert not re.search(fr"\r\n{vlan}\s+{port}\s+", output)

                if allowed_vlans != "all":
                    assert re.search(fr"\r\n{allowed_vlans}\s+{port}\s+", output)

        except Exception:
            kwargs["fail_msg"] = "Failed to verify that given port is removed from any configured vlan"
            self.commonValidation.failed(**kwargs)
            return -1

        else:
            kwargs["pass_msg"] = "Successfully verified that given port is removed from any configured vlan"
            self.commonValidation.passed(**kwargs)
            return 1

        finally:
            self.close_connection_with_error_handling(dut)

    def get_master_slot(self, onboarded_stack, **kwargs):
        """Method that gets master slot info using "show stacking" command.
        Args:
            onboarded_stack
        Returns:
            int: slot number for master unit
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2850
        output = self.networkElementCliSend.send_cmd(onboarded_stack.name, "show stacking")[0].return_text
        rows = output.split("\r\n")
        for row in rows:
            slot = re.search(r"\s+.*\s+(\d+)\s+", row)
            if not slot:
                continue
            slot = slot.group(1)
            if 'Master' in row:
                kwargs["pass_msg"] = f"Slot: {slot}"
                self.commonValidation.passed(**kwargs)
                return slot
        kwargs["fail_msg"] = "get_master_slot() failed."
        self.commonValidation.failed(**kwargs)

    def set_lacp(self, dut, mlt, key, port, **kwargs):
        """Method that configures lacp.
        Args:
            dut (dict): the dut, e.g. tb.dut1
            mlt: ex. 70
            key: ex. 7
            port: dut1.isl.port_a.ifname
        """
        self.close_connection_with_error_handling(dut)
        self.networkElementConnectionManager.connect_to_network_element_name(dut.name)

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2851
        if dut.cli_type.upper() == "EXOS":
            self.networkElementLacpGenKeywords.lacp_create_lag(dut.name, f"{port}", f"{port}-{port}", '')
        elif dut.cli_type.upper() == "VOSS":
            self.networkElementMltGenKeywords.mlt_create_id(dut.name, mlt)
            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'configure terminal', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, f"interface gigabitEthernet {port}", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "no auto-sense enable", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "exit", max_wait=10, interval=2)
            self.networkElementLacpGenKeywords.lacp_create_lag(dut.name, f"gigabitEthernet {port}", port,
                                                                            key)
            self.networkElementCliSend.send_cmd(dut.name, 'configure terminal', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, f"interface mlt {mlt}", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, f"lacp key {key}", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "lacp enable", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "exit", max_wait=10, interval=2)
            self.networkElementLacpGenKeywords.lacp_enable_global(dut.name)

        self.close_connection_with_error_handling(dut)
        kwargs["pass_msg"] = "set_lacp() passed."
        self.commonValidation.passed(**kwargs)

    def cleanup_lacp(self, dut, mlt, port, **kwargs):
        """Cleanup lacp.
        Args:
            dut (dict): the dut, e.g. tb.dut1
            mlt: ex. 70
            key: ex. 7
            port: dut1.isl.port_a.ifname
        """
        self.close_connection_with_error_handling(dut)
        self.networkElementConnectionManager.connect_to_network_element_name(dut.name)

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2851
        if dut.cli_type.upper() == "EXOS":
            self.networkElementLacpGenKeywords.lacp_delete_lag(dut.name, port, '', '')
        elif dut.cli_type.upper() == "VOSS":
            self.networkElementLacpGenKeywords.lacp_delete_lag(dut.name, f"gigabitEthernet {port}", '',
                                                                             port)
            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, 'configure terminal', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, f"interface gigabitEthernet {port}", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "no lacp enable", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "default lacp key", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "auto-sense enable", max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut.name, "exit", max_wait=10, interval=2)
            self.networkElementMltGenKeywords.mlt_delete_id(dut.name, mlt)

        self.close_connection_with_error_handling(dut)
        kwargs["pass_msg"] = "cleanup_lacp() passed."
        self.commonValidation.passed(**kwargs)

    def get_stacking_details_cli(self, dut, **kwargs):
        """
        This keyword gets stacking details from CLI (Mac add, Slot number and Role -for each unit).
        This keyword is implemented only for EXOS STACK.
        :param dut: The dut object of the device
        :return: a list of tuples
        """
        units_list = []
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2867
        if (dut.cli_type.upper() == "EXOS") and (dut.platform.upper() == "STACK"):
            self.networkElementConnectionManager.connect_to_network_element_name(dut.name)
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging', max_wait=10, interval=2)

            stacking_details_output = self.networkElementCliSend.send_cmd(dut.name, 'show stacking', max_wait=10, interval=2)
            p = re.compile(r"((?:[0-9a-fA-F]:?){12})\s+(\d)\s+[^\s]+\s+([^\s]+)", re.M)
            stacking_details = re.findall(p, stacking_details_output[0].return_text)
            units_list.append(stacking_details)

            kwargs['pass_msg'] = "Stacking details found"
            self.commonValidation.passed(**kwargs)
            return units_list

        kwargs['fail_msg'] = "This method is implemented only for EXOS STACK."
        self.commonValidation.failed(**kwargs)
        return -1

    def get_info_from_stack(self, dut, **kwargs):
        """
        - This keyword gets dut details from CLI(ip, mac address, software version, model, serial, make, iqagent version)
        This keyword is implemented only for EXOS STACK.
        :param dut: the dut object
        :return: a list of tuples
        """
        info_list = []

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845
        if (dut.cli_type.upper() == "EXOS") and (dut.platform.upper() == "STACK"):
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging', max_wait=10, interval=2)
            ip_list_cli = []
            ip_list = []
            ip_output = self.networkElementCliSend.send_cmd(dut.name, 'show iqagent | include Interface', max_wait=10, interval=2)
            p = re.compile(r"(Source\sInterface)\s+(\d+.\d+.\d+.\d+)", re.M)
            ip_dut_list = re.findall(p, ip_output[0].return_text)
            ip_list.append(ip_dut_list)
            for i in range(0, len(ip_list[0])):
                unit_i_ip = ip_list[0][i][1]
                ip_list_cli.append(unit_i_ip)
            info_list.append(ip_list_cli)

            stacking_info_cli = self.get_stacking_details_cli(dut)
            self.utils.print_info(f"Stacking details cli: {stacking_info_cli}")
            stacking_info_cli_list_of_tuples= stacking_info_cli[0]
            sorted_by_second = sorted(stacking_info_cli_list_of_tuples, key=lambda tup: tup[1])
            self.utils.print_info(f"Stacking details cli sorted_by_second: {sorted_by_second}")
            mac_add_list_cli = []
            for i in range(0, len(sorted_by_second)):
                unit_i_mac_address = sorted_by_second[i][0]
                unit_i_mac_address_mapped = unit_i_mac_address.replace(':', '')
                unit_i_mac_address_final_mapped = unit_i_mac_address_mapped.upper()
                mac_add_list_cli.append(unit_i_mac_address_final_mapped)
            info_list.append(mac_add_list_cli)

            soft_version_list_cli = []
            soft_version_list = []
            soft_version_output = self.networkElementCliSend.send_cmd(dut.name, 'show version', max_wait=10, interval=2)
            p = re.compile(r"(Slot-\d)\s+\W.[^\s]+.[^\s]+.[^\s]+.[^\s]+.[^\s]+.[^\s]+\s+.[^\s]+\W([^\s]+)", re.M)
            soft_version_dut_list = re.findall(p, soft_version_output[0].return_text)
            soft_version_list.append(soft_version_dut_list)
            for i in range(0, len(soft_version_list[0])):
                unit_i_soft_version = soft_version_list[0][i][1]
                soft_version_list_cli.append(unit_i_soft_version)
            info_list.append(soft_version_list_cli)

            type_list_cli = []
            type_list = []
            type_output = self.networkElementCliSend.send_cmd(dut.name, 'show slot', max_wait=10, interval=2)
            p = re.compile(r"(Slot-\d)\s{5}([^\s]+)", re.M)
            type_dut_list = re.findall(p, type_output[0].return_text)
            type_list.append(type_dut_list)
            for i in range(0, len(type_list[0])):
                unit_i_type = type_list[0][i][1]
                type_list_cli.append(unit_i_type)
            info_list.append(type_list_cli)

            serial_list_cli = []
            serial_list = []
            serial_output = self.networkElementCliSend.send_cmd(dut.name, 'show version', max_wait=10, interval=2)
            p = re.compile(r"(Slot-\d)\s+\W.[^\s]+.([^\s]+)", re.M)
            serial_number_list = re.findall(p, serial_output[0].return_text)
            serial_list.append(serial_number_list)
            for i in range(0, len(serial_list[0])):
                unit_i_serial_number = serial_list[0][i][1]
                serial_list_cli.append(unit_i_serial_number)
            info_list.append(serial_list_cli)

            make_list_cli = []
            make_list = []
            make_output =  self.networkElementCliSend.send_cmd(dut.name, 'show version | include Image', max_wait=10, interval=2)
            p = re.compile(r"(Image\s+\W)\s+(.*)\sversion", re.M)
            make_dut_list = re.findall(p, make_output[0].return_text)
            make_list.append(make_dut_list)
            for i in range(0, len(make_list[0])):
                unit_i_make = make_list[0][i][1]
                make_list_cli.append(unit_i_make)
            info_list.append(make_list_cli)

            iqagent_version_cli = []
            iqagent_version_list = []
            iqagent_version_output = self.networkElementCliSend.send_cmd(dut.name, 'show iqagent | include Version', max_wait=10,interval=2)
            p = re.compile(r"(Version)\s+([^\s]+)", re.M)
            iqagent_version_dut = re.findall(p, iqagent_version_output[0].return_text)
            iqagent_version_list.append(iqagent_version_dut)
            for i in range(0, len(iqagent_version_list[0])):
                unit_i_iqagent_version = iqagent_version_list[0][i][1]
                iqagent_version_cli.append(unit_i_iqagent_version)
            info_list.append(iqagent_version_cli)

            kwargs['pass_msg'] = "Stacking details found"
            self.commonValidation.passed(**kwargs)
            return info_list

        kwargs['fail_msg'] = "This method is implemented only for EXOS STACK."
        self.commonValidation.failed(**kwargs)
        return -1

    def get_virtual_router(self, dut, **kwargs):
        """
           - This keyword returns the vr used by an EXOS / Switch Engine device
           :param dut: device
           :return match.group(12): the name of VR used by EXOS / Switch Engine device
                                    or -1 if is unable to get virtual router info
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2852
        global vrName
        if dut.cli_type.upper() == "EXOS":
            result = self.networkElementCliSend.send_cmd(dut.name, 'show vlan', max_wait=10, interval=2)
            output = result[0].cmd_obj.return_text
            pattern = rf'(\w+)(\s+)(\d+)(\s+)({dut.ip})(\s+)(\/.*)(\s+)(\w+)(\s+/)(.*)(VR-\w+)'
            match = re.search(pattern, output)

            if match:
                self.utils.print_info(f"Mgmt Vlan Name : {match.group(1)}")
                self.utils.print_info(f"Vlan ID        : {match.group(3)}")
                self.utils.print_info(f"Mgmt IPaddress : {match.group(5)}")
                self.utils.print_info(f"Active ports   : {match.group(9)}")
                self.utils.print_info(f"Total ports    : {match.group(11)}")
                self.utils.print_info(f"Virtual router : {match.group(12)}")

                if int(match.group(9)) > 0:
                    return match.group(12)
                else:
                    self.utils.print_info(f"There is no active port in the mgmt vlan {match.group(1)}")
                    kwargs['fail_msg'] = f"There is no active port in the mgmt vlan {match.group(1)}"
                    self.commonValidation.failed(**kwargs)
                    return -1
            else:
                self.utils.print_info("Pattern not found, unable to get virtual router info!")
                kwargs['fail_msg'] = "Pattern not found, unable to get virtual router info!"
                self.commonValidation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("Device is not an EXOS/Switch Engine device, unable to get virtual router info!")
            kwargs['fail_msg'] = "Device is not an EXOS/Switch Engine device, unable to get virtual router info!"
            self.commonValidation.failed(**kwargs)
            return -1

    def get_device_model_name(self, dut, cli_type, **kwargs):
        """
           - Gets the device model name from CLI for an EXOS/VOSS device
           - Keyword Usage:
            - ``get_device_model_name(dut=dut, cli_type=dut.cli_type)``
           :param dut: device
           :param cli_type: the type of device : EXOS / VOSS
           :return system_type_string: a string with device model
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2853
        if cli_type.lower() == 'exos':
            device_system_output = self.networkElementCliSend.send_cmd(dut.name, 'show system | include System')[0].cmd_obj._return_text
            system_type_regex = '(System Type:[ ]{2,}.{0,})'
            system_type = self.utils.get_regexp_matches(device_system_output, system_type_regex, 1)[0]
            system_type_string = system_type.replace(self.utils.get_regexp_matches(system_type,
                                                                                       '(System Type:[ ]{2,})')[0], '')
            if 'SwitchEngine' in system_type_string:
                system_type_string = 'Switch Engine ' + system_type_string
                system_type_string = system_type_string.replace('-SwitchEngine', '')
                system_type_string = system_type_string.replace('\r', '')
            elif 'EXOS' in system_type_string:
                system_type_string = 'Switch Engine ' + system_type_string
                system_type_string = system_type_string.replace('-EXOS', '')
                system_type_string = system_type_string.replace('\r', '')
            else:
                system_type_string = system_type_string.replace(system_type_string[:4], system_type_string[:4] + '-')
                system_type_string = system_type_string.replace('\r', '')
            self.utils.print_info(f"Model name is:{system_type_string}")
            return system_type_string

        elif cli_type.lower() == 'voss':
            device_system_output = self.networkElementCliSend.send_cmd(dut.name, 'show sys-info | include ModelName')[0].cmd_obj._return_text
            system_type_regex = '(ModelName[ ]{2,}.{0,})'
            system_type = self.utils.get_regexp_matches(device_system_output, system_type_regex, 1)[0]
            system_type_string = system_type.replace(self.utils.get_regexp_matches(system_type,
                                                                                   '(ModelName[ ]{2,}.)')[0], '')
            if 'FabricEngine' in system_type_string:
                system_type_string = 'Fabric Engine' + system_type_string
                system_type_string = system_type_string.replace('-FabricEngine', '')
                system_type_string = system_type_string.replace('\r', '')
            elif 'VOSS' in system_type_string:
                system_type_string = 'Fabric Engine' + system_type_string
                system_type_string = system_type_string.replace('-VOSS', '')
                system_type_string = system_type_string.replace('\r', '')
            else:
                system_type_string = system_type_string.replace(system_type_string[:4], system_type_string[:4] + '-')
                system_type_string = system_type_string.replace('\r', '')
            self.utils.print_info(f"Model name is:{system_type_string}")
            return system_type_string
        else:
            kwargs['fail_msg'] = "Didn't find any switch model"
            self.commonValidation.failed(**kwargs)

    def check_os_versions(self, dut1, dut2, **kwargs):
        """
           - This keyword is used to check if 2 devices have the same os version or not
           - Keyword Usage:
            - ``check_os_versions(dut1=${DEVICE}, dut2=${DEVICE})``
           :param dut1: first device
           :param dut2: second device
           :return "same"/"different": a string that specifies if the devices have the same OS or different OS
                    or -1 if unable to check OS versions
        """
        device_1 = dut1.name
        device_2 = dut2.name
        cli_type_device_1 = dut1.cli_type
        cli_type_device_2 = dut2.cli_type

        # TODO https://jira.extremenetworks.com/browse/AIQ-2855
        if cli_type_device_1.lower() == 'exos' and cli_type_device_2.lower() == 'exos':
            output_1 = self.networkElementCliSend.send_cmd(device_1, 'show version | grep IMG')
            check_image_version_1 = output_1[0].return_text
            image_version_regex = 'IMG:([ ]{1,}.{0,})'
            image_version_1 = self.utils.get_regexp_matches(check_image_version_1, image_version_regex, 1)[0]
            image_version_1_string = image_version_1.replace(self.utils.get_regexp_matches(image_version_1,
                                                                                               '([ ])')[0], '')

            output_2 = self.networkElementCliSend.send_cmd(device_2, 'show version | grep IMG')
            check_image_version_2 = output_2[0].return_text
            image_version_2 = self.utils.get_regexp_matches(check_image_version_2, image_version_regex, 1)[0]
            image_version_2_string = image_version_2.replace(self.utils.get_regexp_matches(image_version_2,
                                                                                               '([ ])')[0], '')
            self.utils.print_info(f"OS version for clone device: {image_version_1_string}")
            self.utils.print_info(f"OS version for replacement device: {image_version_2_string}")

            if image_version_1_string == image_version_2_string:
                self.utils.print_info("OS versions are the same")
                return 'same'
            else:
                self.utils.print_info("OS version are different")
                return 'different'

        elif cli_type_device_1.lower() == 'voss' and cli_type_device_2.lower() == 'voss':
            output_descr_1 = self.networkElementCliSend.send_cmd(device_1, 'show sys-info | include SysDescr')
            check_image_version_1 = output_descr_1[0].return_text
            image_version_regex = '(\\d+[.]\\d+[.]\\d+[.]\\d+)'
            image_version_1_string = self.utils.get_regexp_matches(check_image_version_1, image_version_regex, 1)[0]
            self.utils.print_info(f"OS version for clone device: {image_version_1_string}")

            output_descr_2 = self.networkElementCliSend.send_cmd(device_2, 'show sys-info | include SysDescr')
            check_image_version_2 = output_descr_2[0].return_text
            image_version_2_string = self.utils.get_regexp_matches(check_image_version_2, image_version_regex, 1)[0]
            self.utils.print_info(f"OS version for replacement device: {image_version_2_string}")

            if image_version_1_string == image_version_2_string:
                self.utils.print_info("OS versions are the same")
                return 'same'
            else:
                self.utils.print_info("OS version are different")
                return 'different'
        else:
            kwargs['fail_msg'] = "Unable to check OS version for devices"
            self.commonValidation.failed(**kwargs)
            return -1

    def disable_enable_iqagent_clone_device(self, device, iqagent_option, **kwargs):
        """
                - This keyword is used to enable/disable iq agent for a an EXOS/VOSS device from CLI
                :param device: device selected
                :param iqagent_option: "enable" or "disable" option for iqagent
                :return 1 if sucess or -1 if fails
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2845
        device_1 = device.name
        cli_type_device_1 = device.cli_type
        if iqagent_option == 'disable':
            if cli_type_device_1.lower() == 'exos':
                self.networkElementCliSend.send_cmd(device_1, "disable iqagent", max_wait=10, interval=2,
                                     confirmation_phrases='Do you want to continue?', confirmation_args='y')
                kwargs['pass_msg'] = "IQ agent successfully disabled"
                self.commonValidation.passed(**kwargs)
            elif cli_type_device_1.lower() == 'voss':
                self.networkElementCliSend.send_cmd(device_1, "enable", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(device_1, "configure terminal", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(device_1, "application", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(device_1, "no iqagent enable", max_wait=10, interval=2)
                kwargs['pass_msg'] = "IQ agent successfully disabled"
                self.commonValidation.passed(**kwargs)
            else:
                kwargs['fail_msg'] = "Didn't find any os type"
                self.commonValidation.failed(**kwargs)

        elif iqagent_option == 'enable':
            if cli_type_device_1.lower() == 'exos':
                self.networkElementCliSend.send_cmd(device_1, "enable iqagent", max_wait=10, interval=2)
                kwargs['pass_msg'] = "IQ agent successfully enabled"
                self.commonValidation.passed(**kwargs)
            elif cli_type_device_1.lower() == 'voss':
                self.networkElementCliSend.send_cmd(device_1, "enable", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(device_1, "configure terminal", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(device_1, "application", max_wait=10, interval=2)
                self.networkElementCliSend.send_cmd(device_1, "iqagent enable", max_wait=10, interval=2)
                kwargs['pass_msg'] = "IQ agent successfully enabled"
                self.commonValidation.passed(**kwargs)
            else:
                kwargs['fail_msg'] = "Didn't find any os type"
                self.commonValidation.failed(**kwargs)
        else:
            kwargs['fail_msg'] = "Didn't find option for disable/enable"
            self.commonValidation.failed(**kwargs)

    def check_lacp_dut(self, dut, lacp_list_ports, **kwargs):
        """
        Used for checking lacp on the EXOS switch matches the reference list:
        dut - device to test
        lacp_list_ports = ["port1, "port2", "port3", "port4", ...]
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2856
        if dut.cli_type == 'exos':
            for attempts in range(3):
                self.networkElementConnectionManager.connect_to_network_element_name(dut.name)
                output = self.networkElementCliSend.send_cmd(dut.name, 'show configuration | i sharing',
                                              max_wait=10, interval=2)
                self.networkElementConnectionManager.close_connection_to_network_element(dut.name)
                p = re.compile(r'\d:\d+-\d:\d+|\d:\d+,\d:\d+|\d:\d+-\d+', re.M)
                lacp_list_ports_from_dut = re.findall(p, output[0].return_text)

                for i in range(0, len(lacp_list_ports), 2):
                    if lacp_list_ports[i] + '-' + lacp_list_ports[i+1] in lacp_list_ports_from_dut:
                        lacp_list_ports_from_dut.remove(lacp_list_ports[i] + '-' + lacp_list_ports[i+1])
                    elif lacp_list_ports[i] + '-' + lacp_list_ports[i+1].split(":")[1] in lacp_list_ports_from_dut:
                        lacp_list_ports_from_dut.remove(lacp_list_ports[i] + '-' + lacp_list_ports[i+1].split(":")[1])
                    elif lacp_list_ports[i] + ',' + lacp_list_ports[i+1] in lacp_list_ports_from_dut:
                        lacp_list_ports_from_dut.remove(lacp_list_ports[i] + ',' + lacp_list_ports[i+1])
                    else:
                        kwargs["fail_msg"] = "'check_lacp_dut()' failed. No LACP ports found on CLI"
                        self.commonValidation.failed(**kwargs)
                        return False

                if len(lacp_list_ports_from_dut) == 0:
                    kwargs["pass_msg"] = "Successfully verified number of ports matched."
                    self.commonValidation.passed(**kwargs)
                    return True
                else:
                    kwargs["fail_msg"] = "'check_lacp_dut()' failed. Number of LACP ports do not match CLI"
                    self.commonValidation.failed(**kwargs)
                    return False
        else:
            kwargs["fail_msg"] = f"'check_lacp_dut()' failed. CLI type {dut.cli_type} not supported."
            self.commonValidation.failed(**kwargs)
            return False

    def verify_poe_supported(self, dut, **kwargs):
        """
        Method that verifies if the device has power over ethernet capabilities.
        Currently this method supports only devices with cli_type exos/voss.
        
        :param dut: the dut, e.g. tb.dut1
        :return: 1 if the function call has succeeded else -1
        """
        
        if dut.cli_type.lower() not in ["exos", "voss"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1
        
        check_poe = 1
        if dut.cli_type.lower() == "voss":
            
            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=30, interval=10)
            self.networkElementCliSend.send_cmd(dut.name, 'configure terminal', max_wait=30, interval=10)
            self.utils.print_info("Trying to see if device supoorts POE")
            result = self.networkElementCliSend.send_cmd(dut.name, 'show poe-main-status', max_wait=30, interval=10)[0].cmd_obj._return_text
            self.utils.print_info(f"Result was: {result}")
            
            if "PoE Main Status" in result:
                check_poe = 1
            elif "POE not supported by device" in result:
                kwargs['fail_msg'] = "POE not supported by device"
                self.commonValidation.failed(**kwargs)
                return -1
            
        elif dut.cli_type.lower() == "exos" and not dut.platform == 'Stack':
            
            self.networkElementCliSend.send_cmd(dut.name, 'enable telnet')
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging')
            self.utils.print_info("Trying to see if device supoorts POE")
            
            try:
                result = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power', max_wait=30, interval=10)[0].cmd_obj._return_text
            except Exception:
                kwargs['fail_msg'] = "POE not supported by device"
                self.commonValidation.failed(**kwargs)
                return -1
            
            self.utils.print_info(f"Result was: {result}")
            if 'Inline Power System Information' in result:
                self.utils.print_info("EXOS device supports PoE")
                check_poe = 1
            else:
                kwargs['fail_msg'] = "POE not supported by device"
                self.commonValidation.failed(**kwargs)
                return -1
            
        elif dut.cli_type.lower() == "exos" and dut.platform == 'Stack':
            
            self.networkElementCliSend.send_cmd(dut.name, 'enable telnet')
            self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging')
            
            self.utils.print_info("Trying to see if device supoorts POE")
            try:
                result = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power', max_wait=30, interval=10)[0].cmd_obj._return_text
            except Exception:
                kwargs["fail_msg"] = "Failed! PoE not supported"
                self.commonValidation.fault(**kwargs)
                return -1
            
            self.utils.print_info(f"Result was: {result}")
            if 'Firmware Status' in result:
                self.utils.print_info("EXOS device supports PoE")
                check_poe = 1
            else:
                kwargs['fail_msg'] = "POE not supported by device"
                self.commonValidation.failed(**kwargs)
                return -1
            
        else:
            kwargs['fail_msg'] = "CLI type not supported"
            self.commonValidation.failed(**kwargs)
            return -1
        
        self.commonValidation.passed(**kwargs)
        return check_poe

    def get_cli_poe_details(self, dut, **kwargs):
        """
        Method that returns string with power details from switch CLI.
        Currently this method supports only devices with cli_type exos.
        
        :param dut: the dut, e.g. tb.dut1
        :return: a list with two string elements (the threshold power and the operation power) if the function call has succeeded else -1
        """

        if dut.cli_type.lower() not in ["exos"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1
        
        if dut.cli_type == "exos":
            
            elem = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power', max_wait=30, interval=10)[0].cmd_obj._return_text
            inline_power_info = self.utils.get_regexp_matches(elem,
                            r"(\w+['Inline']\s+\w+['Power]\s+\w+['System']\s+\w+['Information'])",1)
            
            if not inline_power_info:
                kwargs['fail_msg'] = "POE not supported by device"
                self.commonValidation.failed(**kwargs)
                return -1
            
            else:
                self.utils.print_info("EXOS device supports PoE")
                #get PoE values
                var_operational_power = self.utils.get_regexp_matches(elem, r"\w+['Operational']\s+(\d+)", 1)
                
                if not var_operational_power:
                    kwargs['fail_msg'] = "Device POE is not opperational"
                    self.commonValidation.failed(**kwargs)
                    return -1
                
                var_operational_power =  var_operational_power[0]
                var_threshold_power_procents = self.utils.get_regexp_matches(elem, r"\w+['Power']\s+\w+['Usage']\s+\w+['Threshold']\s+.\s+(\d+)", 1)[0]
                self.utils.print_info("Operational Values from CLI is :", var_operational_power)
                self.utils.print_info("Power Threshold value from CLI is :", var_threshold_power_procents)

                # Transform the POE threshold power in watts
                var_threshold_power_watts = int(var_operational_power) * int(var_threshold_power_procents) / 100
                self.utils.print_info("Power Threshold value from CLI is :", var_threshold_power_watts)
                self.utils.print_info("Power Threshold value int from CLI is :", int(var_threshold_power_watts))

                self.commonValidation.passed(**kwargs)
                return [str(int(var_threshold_power_watts)), str(var_operational_power)]

    def get_cli_poe_details_updated(self, dut, **kwargs):
        """
        Method that returns power usage threshold int value from switch CLI.
        Currently this method supports only devices with cli_type exos.
        
        :param dut: the dut, e.g. tb.dut1
        :return: the power usage as int if the function call has succeeded else -1
        """

        if dut.cli_type.lower() not in ["exos"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1
        
        if dut.cli_type.lower() == "exos":
            elem = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power', max_wait=30, interval=10)[0].cmd_obj._return_text
            inline_power_info = self.utils.get_regexp_matches(elem, r"\w+['Power']\s+\w+['Usage']\s+\w+['Threshold']\s+.\s+(\d+)", 1)
            
            if inline_power_info:
                inline_power_info = inline_power_info[0]
                self.utils.print_info("CLI value is ", inline_power_info)

                self.commonValidation.passed(**kwargs)
                return int(inline_power_info)
            
            kwargs["fail_msg"] = "Failed to get power usage threshold value from switch CLI"
            self.commonValidation.failed(**kwargs)
            return -1

    def get_stack_slot_poe(self, dut, **kwargs):
        """
        Method that checks if there is an available stack slot with POE.
        Currently this method supports only devices with cli_type exos.
        
        :param dut: the dut, e.g. tb.dut1
        :return: a list of strings (where each string is a slot of the stack) if the function call has succeeded else -1
        """

        if dut.cli_type.lower() not in ["exos"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1

        if dut.cli_type.lower() == "exos":
            elem = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power', max_wait=30, interval=10)[0].cmd_obj._return_text
            inline_power_slot = self.utils.get_regexp_matches(elem, r"(\d)\s+\w+['Enabled']\s+\w+['Operational']", 1)
            self.utils.print_info(inline_power_slot)

            if type(inline_power_slot) == list:
                self.commonValidation.passed(**kwargs)
                return inline_power_slot

            kwargs['fail_msg'] = "POE not supported by device"
            self.commonValidation.failed(**kwargs)
            return -1

    def get_stack_slot_psu(self, dut, **kwargs):
        """
        Method that shows slot power details from CLI.
        Currently this method supports only devices with cli_type exos.
        
        :param dut: the dut, e.g. tb.dut1
        :return: a list of strings if the function call has succeeded else -1
        """
        
        if dut.cli_type.lower() not in ["exos"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1
        
        if dut.cli_type.lower() == "exos":
            
            power_details = self.networkElementCliSend.send_cmd(dut.name, 'show power detail | grep Power', max_wait=30, interval=10)[0].cmd_obj._return_text
            power_slot = self.utils.get_regexp_matches(
                power_details, r"\w+['Slot'].(\d)\s+\w+['PowerSupply']\s+\d+\s+\w+['information'].\s+\w+\s+.\s+\w+['Powered']\s+\w+['On']\s+\w+['Power']\s+\w+['Usage']\s+.\s+\d+.\d+", 1)
            self.utils.print_info(power_slot)

            if type(power_slot) == list or type(power_slot) == str:
                self.commonValidation.passed(**kwargs)
                return power_slot

            else:
                kwargs['fail_msg'] = "PSU details cannot be collected"
                self.commonValidation.failed(**kwargs)
                return -1

    def get_cli_psu_details(self, dut, **kwargs):
        """
        Method that shows power details for stack or standalone device.
        Currently this method supports only devices with cli_type exos.
        
        :param dut: the dut, e.g. tb.dut1
        :return: a list of strings if the function call has succeeded else -1
        """

        if dut.cli_type.lower() not in ["exos"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1

        if dut.cli_type == "exos":

            if dut.platform == 'Stack':
                all_powers_list = []

                operational_power_details = self.networkElementCliSend.send_cmd(dut.name, 'show power detail | grep Output', max_wait=30, interval=10)[0].cmd_obj._return_text
                operational_power_slot = self.utils.get_regexp_matches(operational_power_details, r"\d+['V]\/(\d+)['W]\s+\w+", 1)
                power_usage_details = self.networkElementCliSend.send_cmd(dut.name, 'show power detail | grep Power', max_wait=30, interval=10)[0].cmd_obj._return_text
                power_usage_slot = self.utils.get_regexp_matches(power_usage_details, r"\w+['Slot'].\d\s+\w+['PowerSupply']\s+\d+\s+\w+['information'].\s+\w+\s+.\s+\w+['Powered']\s+\w+['On']\s+\w+['Power']\s+\w+['Usage']\s+.\s+(\d+.\d+)\s+\w+", 1)
                for operational_power_slot_element in operational_power_slot:
                    all_powers_list.append(operational_power_slot_element)
                for power_per_slot in power_usage_slot:
                    power_per_slot_int = int(float(power_per_slot))
                    all_powers_list.append(str(power_per_slot_int))
                self.utils.print_info(all_powers_list)

                self.commonValidation.passed(**kwargs)
                return all_powers_list

            else:
                powerdetails = self.networkElementCliSend.send_cmd(dut.name, 'show power detail', max_wait=30, interval=10)[0].cmd_obj._return_text
                psu_details = self.utils.get_regexp_matches(powerdetails, r"(\w+['PowerSupply']\s\w\s\w+['information'])", 1)[0]

                if psu_details in powerdetails:
                    total_power_available = self.utils.get_regexp_matches(powerdetails, r"\w+['Output']\s+\d+\s*\S\s\d*.\d*\s+\w+.\s+\d+.\d+\s+\w+\s+\S\d+\w\/(\d+)", 1)[0]
                    total_power_consumed = self.utils.get_regexp_matches(powerdetails, r"\w+['System']\s+\w+['Power']\s+\w+['Usage']\s+.\s+(\d+.\d+)", 1)[0]
                    self.utils.print_info(total_power_available)
                    new_total_power_consumed = int(float(total_power_consumed))
                    self.utils.print_info(new_total_power_consumed)

                    self.commonValidation.passed(**kwargs)
                    return [total_power_available, str(new_total_power_consumed)]

                else:
                    kwargs['fail_msg'] = "Total and Consumed power can't be collected"
                    self.commonValidation.fault(**kwargs)
                    return -1

    def change_threshold_power_from_cli(self, dut, new_threshold_value, **kwargs):
        """
        Method that changes the threshold power value from CLI.
        Currently this method supports only devices with cli_type exos.
        
        :param dut: the dut, e.g. tb.dut1
        :param new_threshold_value: the int value of the new_threshold_value, 0-100
        :return: a list of strings if the function call has succeeded else -1
        """

        if dut.cli_type.lower() not in ["exos"]:
            kwargs["fail_msg"] = "Failed! OS not supported."
            self.commonValidation.fault(**kwargs)
            return -1
        
        if dut.cli_type == "exos":
            
            elem = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power', max_wait=30, interval=10)[0].cmd_obj._return_text
            inline_power_info = self.utils.get_regexp_matches(elem, r"(\w+['Inline']\s+\w+['Power]\s+\w+['System']\s+\w+['Information'])", 1)[0]

            if inline_power_info in elem:
                self.utils.print_info("EXOS device supports PoE")
                #get the Threshold POwer value
                var_operational_power = self.utils.get_regexp_matches(elem, r"\w+['Operational']\s+(\d+)", 1)[0]
                var_threshold_power_procents = self.utils.get_regexp_matches(elem, r"\w+['Power']\s+\w+['Usage']\s+\w+['Threshold']\s+.\s+(\d+)", 1)[0]
                self.utils.print_info(var_operational_power)
                self.utils.print_info(var_threshold_power_procents)
                #change the Threshold Power value from CLI
                threshold_power_changed_procents = self.networkElementCliSend.send_cmd(dut.name, f'configure inline-power usage-threshold {new_threshold_value}', max_wait=30, interval=10)[0].cmd_obj._return_text
                self.utils.print_info(threshold_power_changed_procents)
                # Transform the POE threshold power in watts
                threshold_power_changed_watts = int(var_operational_power) * int(new_threshold_value) / 100

                self.commonValidation.passed(**kwargs)
                return [str(int(threshold_power_changed_watts)), var_operational_power]

            kwargs['fail_msg'] = "POE not supported by device"
            self.commonValidation.failed(**kwargs)
            return -1

    def search_last_command_cli_journal(self, info: str, command, **kwargs):
        """
           - This keyword is used to check if the command presented as last command in "show cli-journal"
           - Keyword Usage:
            - ``search_last_command_cli_journal(info=${INFO}, command=${COMMAND})``

        :param info: CLI output as string
        :param command: CLI command to be found
        :return: 1 if the command was found as last command else fails
        """
        table = []
        for entry in info[4:].split("\n"):
            if entry:
                if entry[0].isdigit():
                    aux = [i for i in entry.split(" ") if i]
                    table.append([' '.join(aux[:2]), aux[2], aux[3], ' '.join(aux[4:])])

        now = datetime.now()
        log_time = (now - timedelta(days=1))
        flag = False
        for row in reversed(table):
            if log_time < datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S.%f') and command in row[-1]:
                self.utils.print_info(row)
                flag = True
                break
            else:
                self.utils.print_info(row)
                flag = False
        if flag:
            kwargs['pass_msg'] = f"'{command}' found as last command in cli journal"
            self.commonValidation.passed(**kwargs)
        else:
            kwargs['fail_msg'] = f"'{command}' didn't find as last command cli journal"
            self.commonValidation.failed(**kwargs)

    def check_pse_restart_in_cli(self, dut, **kwargs):
        """
           - This keyword is used to check if the command "reset inline-power ports" was executed in "show cli-journal"
           - Keyword Usage:
            - ``check_pse_restart_in_cli(dut=${DEVICE})``

        :param dut: device to test
        :return: -1 if fails
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2857 AIQ-2857 - Add Support for CLI journaling
        spawn = self.open_spawn(dut.ip, dut.port, dut.username,
                                dut.password, dut.cli_type)
        if dut.cli_type.upper() in ["VOSS", "AH-FASTPATH"]:
            kwargs['fail_msg'] = f"This keyword (check_pse_restart_in_cli) is not supported for {dut.cli_type} devices"
            self.commonValidation.fault(**kwargs)
            return -1
        elif dut.cli_type.upper() == "EXOS":
            self.send_commands(spawn, "disable cli paging")
            cli_journal = self.send_commands(spawn, "show cli  journal | grep reset")
            self.search_last_command_cli_journal(info=cli_journal, command="reset inline-power ports")
        else:
            kwargs['fail_msg'] = "Fail to find the CLI type"
            self.commonValidation.fault(**kwargs)
            return -1

    def configure_cli_table(self, dut1, dut2, **kwargs):
        """
        - This keyword configures the same cli journal size for both given switches(EXOS) or clears logging history(VOSS) in order to compare the output
        Args:
         dut1 (dict): the dut, e.g. tb.dut1
         dut2 (dict): the dut, e.g. tb.dut2
        :return: -1 if No type OS found
        """
        cli_type_1 = dut1.cli_type
        cli_type_2 = dut2.cli_type
        dut1 = dut1.name
        dut2 = dut2.name

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2857 AIQ-2857 - Add Support for CLI journaling
        if cli_type_1.lower() and cli_type_2.lower() == 'exos':
            self.networkElementCliSend.send_cmd(dut1, 'configure cli journal size 200', max_wait=10, interval=2)
            self.networkElementCliSend.send_cmd(dut2, 'configure cli journal size 200', max_wait=10, interval=2)
            kwargs['pass_msg'] = "configure_cli_table() passed"
            self.commonValidation.passed(**kwargs)
        elif cli_type_1.lower() and cli_type_2.lower() == 'voss':

            self.send_commands(dut1, "configure terminal")
            self.send_commands(dut1, "clear logging")
            self.send_commands(dut2, "configure terminal")
            self.send_commands(dut2, "clear logging")
            kwargs['pass_msg'] = "configure_cli_table() passed"
            self.commonValidation.passed(**kwargs)
        else:
            kwargs['fail_msg'] = "configure_cli_table() failed. No type OS found"
            self.commonValidation.failed(**kwargs)
            return -1

    def check_clone_configuration(self, dut1, dut2, **kwargs):
        """
        - This keyword will verify if the clone configuration was successful by checking if the last commands for both given switches are the same
        Args:
         dut1 (dict): the dut, e.g. tb.dut1
         dut2 (dict): the dut, e.g. tb.dut2
        :return: a pass msg if the commands are the same/a fail msg if the commands are not the same
        """

        cli_type_1 = dut1.cli_type
        cli_type_2 = dut2.cli_type

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2857 AIQ-2857 - Add Support for CLI journaling
        if cli_type_1.lower() and cli_type_2.lower() == 'exos':
            cli_journal_1 = self.send_commands(dut1.name, "show cli journal | include hivemanager")
            commands_device_1 = self.get_cli_commands(cli_journal_1, cli_type=dut1.cli_type)
            self.utils.print_info(commands_device_1)
            cli_journal_2 = self.send_commands(dut2.name, "show cli journal | include hivemanager")
            commands_device_2 = self.get_cli_commands(cli_journal_2, cli_type=dut2.cli_type)
            self.utils.print_info(commands_device_2)
            a = set(commands_device_1)
            b = set(commands_device_2)
            if a == b:
                self.utils.print_info("Commands are the same")
                kwargs['pass_msg'] = "check_clone_configuration() passed"
                self.commonValidation.passed(**kwargs)
            else:
                kwargs['fail_msg'] = "check_clone_configuration() failed. Commands are not the same "
                self.commonValidation.failed(**kwargs)

        elif cli_type_1.lower() and cli_type_2.lower() == 'voss':
            self.send_commands(dut1.name, "terminal more disable")
            cli_journal_1 = self.send_commands(dut1.name,
                                                       'show logging file detail | include "127.0.0.1 hivemanager"')
            commands_device_1 = self.get_cli_commands(cli_journal_1, cli_type=dut1.cli_type)
            self.utils.print_info(commands_device_1)
            self.send_commands(dut1.name, "terminal more disable")
            cli_journal_2 = self.send_commands(dut2.name,
                                                       'show logging file detail | include "127.0.0.1 hivemanager"')
            commands_device_2 = self.get_cli_commands(cli_journal_2, cli_type=dut2.cli_type)
            self.utils.print_info(commands_device_2)
            a = set(commands_device_1)
            b = set(commands_device_2)
            if a == b:
                self.utils.print_info("Commands are the same")
                kwargs['pass_msg'] = "check_clone_configuration() passed."
                self.commonValidation.passed(**kwargs)
            else:
                kwargs['fail_msg'] = "check_clone_configuration() failed. Commands are not the same "
                self.commonValidation.failed(**kwargs)

    def get_cli_commands(self, info: str, cli_type, **kwargs):
        """
        - This keyword will convert last commands from CLI string to a list
        Args:
         info: str : cli output
         cli_type: ex. dut1.cli_type
        Use : get_cli_commands(output, dut1.cli_type)
        :return:  commands table list/ -1 if No type OS found
        """
        table, table_repl = [], []
        for entry in info.split("\n"):
            if entry:
                if entry[0].isdigit():
                    aux = [i for i in entry.split(" ") if i]
                    if cli_type.lower() == 'exos':
                        table.append(' '.join(aux[4:]))
                    elif cli_type.lower() == 'voss':
                        table.append(' '.join(aux[14:]))
        if cli_type.lower() == 'exos':
            for element_table in table:
                table_repl.append(element_table.replace('\r', ' '))
            if 'exit ' in table_repl:
                table_repl.remove('exit ')
            if '' in table_repl:
                table_repl.remove('')
            n = 100
            last_100_commands_table = list(list(islice(reversed(table_repl), 0, n)))
            last_100_commands_table.reverse()
            output = [el.strip() for el in last_100_commands_table]
            kwargs['pass_msg'] = "get_cli_commands() passed."
            self.commonValidation.passed(**kwargs)
            return output
        elif cli_type.lower() == 'voss':
            for element_table in table:
                table_repl.append(element_table.replace('\r', ' '))
            for index in table_repl:
                if 'end ' in table_repl:
                    table_repl.remove('end ')
                if 'logout ' in table_repl:
                    table_repl.remove('logout ')
            output = [el.strip() for el in table_repl]
            kwargs['pass_msg'] = "get_cli_commands() passed."
            self.commonValidation.passed(**kwargs)
            return output
        else:
            kwargs['fail_msg'] = "get_cli_commands() failed. No type OS found "
            self.commonValidation.failed(**kwargs)
            return -1

    def check_ports_existence(self, dut, ports, **kwargs):
        """ Method that verifies if given ports are found on the device.

        Currently this method supports only switches with cli_type - exos.

        Args:
            dut (dict): the dut, e.g. tb.dut1
            ports (str): the ports that will be verified - e.g. '1,3,5,10'

        Returns:
            int: 1 if the function call has succeeded else -1
        """

        supported_devices = ["EXOS"]
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842
        if dut.cli_type.upper() not in supported_devices:
            kwargs["fail_msg"] = f"Chosen device is not currently supported. Supported devices: {supported_devices}"
            self.commonValidation.fault(**kwargs)
            return -1

        if dut.cli_type.upper() == "EXOS":

            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports vlan')[0].cmd_obj._return_text

            ports_not_found = []

            if dut.platform.upper() == 'STACK':

                for slot in range(1, len(dut.serial.split(',')) + 1):
                    for port in ports.split(','):
                        if not re.search(rf"^{slot}:{port}\s+", output):
                            ports_not_found.append(str(slot) + ':' + port)
                        else:
                            self.utils.print_info("Found the port: " + str(slot) + ':' + port)
            else:
                for port in ports.split(','):
                    if not re.search(rf"^{port}\s+", output):
                        ports_not_found.append(port)
                    else:
                        self.utils.print_info("Found the port: " + port)

            if ports_not_found:
                self.utils.print_info('The following ports were not found: ')

                for port_not_found in ports_not_found:
                    self.utils.print_info(port_not_found)

                kwargs["fail_msg"] = f"Did not find these ports on the device: {ports_not_found}"
                self.commonValidation.failed(**kwargs)
                return -1

        kwargs["pass_msg"] = "Successfully found all the ports on the device"
        self.commonValidation.passed(**kwargs)
        return 1

    def get_switch_connected_ports(self, dut):
        """ Method that returns a list of all connected ports on a device.
        :param : dut (dict): the dut, e.g. dut1, node_1
        :return: connected_ports: a list of all connected ports on device if the function call has succeeded else -1
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2858
        if dut.cli_type.lower() == "voss":
            self.utils.print_info("Checking for connected ports on voss switch...")
            output = self.networkElementCliSend.send_cmd(dut.name, 'show lldp neighbor', max_wait=10, interval=2)
            lldp_neighbor_summary_output = output[0].cmd_obj.return_text
            connected_ports = self.utils.get_regexp_matches(lldp_neighbor_summary_output, '((?<=Port: )\\d+/\\d+)', 1)

        elif dut.cli_type.lower() == "exos" and dut.platform.lower() == 'stack':
            self.utils.print_info("Checking for connected ports on exos stack...")
            self.networkElementCliSend.send_cmd(dut.name, 'clear lldp neighbors all', max_wait=10, interval=2)
            self.utils.wait_till(timeout=90, delay=30, silent_failure=True, msg="Waiting for lldp table to "
                                                                                "be repopulated on switch")
            output = self.networkElementCliSend.send_cmd(dut.name, 'show lldp neighbors detail', max_wait=10, interval=2)
            lldp_neighbor_summary_output = output[0].cmd_obj.return_text
            connected_ports = self.utils.get_regexp_matches(lldp_neighbor_summary_output,'((?<=LLDP Port )\\d+:\\d+)', 1)

        elif dut.cli_type.lower() == "exos":
            self.utils.print_info("Checking for connected ports on exos switch...")
            self.networkElementCliSend.send_cmd(dut.name, 'clear lldp neighbors all', max_wait=10, interval=2)
            self.utils.wait_till(timeout=90, delay=30, silent_failure=True, msg="Waiting for lldp table to "
                                                                                "be repopulated on stack")
            output = self.networkElementCliSend.send_cmd(dut.name, 'show lldp neighbors detail', max_wait=10, interval=2)
            lldp_neighbor_summary_output = output[0].cmd_obj.return_text
            connected_ports = self.utils.get_regexp_matches(lldp_neighbor_summary_output, '((?<=LLDP Port )\\d+)', 1)
        return connected_ports

    def get_switch_disconnected_ports(self, dut, connected_ports):
        """ Method that returns a list of all disconnected ports on a device.
        :param: dut (dict): the dut, e.g. dut1, node_1
        :param: connected_ports: list of connected ports detected on dut
        :return: disconnected_ports: a list of all disconnected ports on device if the function call has succeeded else -1
        """

        # TODO: https://jira.extremenetworks.com/browse/AIQ-2842
        if dut.cli_type.lower() == "voss":
            system_type_regex = "(\\d+/\\d+)\\s+\\w+"
            self.networkElementCliSend.send_cmd(dut.name, 'enable', max_wait=30, interval=10)
            self.networkElementCliSend.send_cmd(dut.name, 'configure terminal', max_wait=30, interval=10)
            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports vlan')[0].cmd_obj._return_text
            disconnected_ports = self.utils.get_regexp_matches(output, system_type_regex, 1)
            for connected in connected_ports:
                disconnected_ports.remove(connected)

        if dut.cli_type.lower() == "exos":
            system_type_regex = "(\\d+)\\s+\\w+"
            if dut.platform == 'Stack':
                system_type_regex = "(\\d+:\\d+)"
            output = self.networkElementCliSend.send_cmd(dut.name, 'show ports vlan')[0].cmd_obj._return_text
            disconnected_ports = self.utils.get_regexp_matches(output, system_type_regex, 1)
            for connected in connected_ports:
                if connected in disconnected_ports:
                    disconnected_ports.remove(connected)
        return disconnected_ports

    def get_switch_poe_ports(self, dut):
        """ Method that returns a list of all ports that support POE on a device.
        :param: dut (dict): the dut, e.g. dut1, node_1
        :return: poe_ports: a list of all poe ports on device if the function call has succeeded else -1
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2859
        if dut.cli_type.lower() == "voss":
            self.utils.print_info("Checking for POE ports on voss switch...")
            output = self.networkElementCliSend.send_cmd(dut.name, 'show poe-port-status | include Searching', max_wait=10, interval=2)
            poe_port_capability_output = output[0].cmd_obj.return_text
            poe_ports = self.utils.get_regexp_matches(poe_port_capability_output, r'\n(\d+\/\d+)', 1)

        elif dut.cli_type.lower() == "exos" and dut.platform.lower() == 'stack':
            self.utils.print_info("Checking for POE ports on exos stack...")
            output = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power info ports', max_wait=10, interval=2)
            poe_port_capability_output = output[0].cmd_obj.return_text
            poe_ports = self.utils.get_regexp_matches(poe_port_capability_output, r'\n(\d+:\d+)', 1)

        elif dut.cli_type.lower() == "exos":
            self.utils.print_info("Checking for POE ports on exos switch...")
            output = self.networkElementCliSend.send_cmd(dut.name, 'show inline-power info ports', max_wait=10, interval=2)
            poe_port_capability_output = output[0].cmd_obj.return_text
            poe_ports = self.utils.get_regexp_matches(poe_port_capability_output, r'\n(\d+)', 1)
        return poe_ports

    def expected_commands_in_cli_history(self, expected_commands, dut, dut_time=None, **kwargs):
        """ Method that checks if expected commands are found in CLI history.
        Assumption for VOSS is "clear logging" command was issued on CLI before using this method
        For EXOS, currently there is no equivalent for the clear logging command from VOSS,
        so we need to filter based on current time on device.
        :param: dut (dict): the dut, e.g. dut1, node_1
        :return: 1 if the function call has succeeded else -1
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2857
        if dut.cli_type.lower() == 'voss':
            cli_dut = self.networkElementCliSend.send_cmd(dut.name, "show logging file detail | include SSH:127.0.0.1")
        elif dut.cli_type.lower() == 'exos':
            if dut.platform.lower() == 'stack':
                self.utils.wait_till(timeout=120, delay=60, silent_failure=True, msg="Waiting for commands to "
                                                               "be sent to the stack...")
            cli_dut = self.networkElementCliSend.send_cmd(dut.name, f"show cli journal | begin {dut_time} ")
        output_CLI = self.get_cli_commands(info=cli_dut[0].cmd_obj.return_text, cli_type=dut.cli_type)
        output = [el.strip() for el in output_CLI]
        for i, command in enumerate(expected_commands):
            if command in output:
                if i == len(expected_commands)-1:
                    kwargs['pass_msg'] = f"Found all expected commands in CLI: {expected_commands}"
                    self.commonValidation.passed(**kwargs)
                    return 1
            else:
                kwargs['fail_msg'] = f"Command {command} not found"
                self.commonValidation.failed(**kwargs)
                return -1


    def show_maclocking_on_the_ports_in_cli(self, dut, **kwargs):
        """
         - This keyword will return a list of pairs(port number and mac locking state for each port) for EXOS devices.
        :param: dut: device to be tested
        :return: a list of pairs(port number and mac locking state for each port)
        :return: -1 if error
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2860
        if dut.cli_type.upper() != "EXOS":
            kwargs["fail_msg"] = "Wrong cli_type"
            self.commonValidation.fault(**kwargs)
        self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                            max_wait=10, interval=2)
        output = self.networkElementCliSend.send_cmd(dut.name, 'show mac-locking',
                                                     max_wait=10, interval=2)
        p = re.compile(r'(^\d+)\s+(ena|dis)', re.M)
        match_port_mac_locking_state = re.findall(p, output[0].return_text)
        self.utils.print_info(f"{match_port_mac_locking_state}")
        kwargs["pass_msg"] = "Collected CLI MAC info."
        self.commonValidation.passed(**kwargs)
        return match_port_mac_locking_state

    def get_nw_templ_device_config_forward_delay(self, dut, **kwargs):
        '''
        - Get the forward delay for a device
        :param dut: the dut object
        :return: the forward delay
        '''
        if dut.cli_type.upper() == "EXOS":

            for attempts in range(3):
                sleep(5)
                self.networkElementConnectionManager.connect_to_network_element_name(dut.name)
                self.networkElementCliSend.send_cmd(dut.name, 'disable cli paging',
                                     max_wait=10, interval=2)

                output = self.networkElementCliSend.send_cmd(dut.name, 'show stpd detail',
                                                      max_wait=10,
                                                      interval=2)
                self.networkElementConnectionManager.close_connection_to_network_element(dut.name)
                self.utils.print_info(output[0].return_text)

                p = re.compile(r'(CfgBrForwardDelay:\s+)+(\d+)', re.M)

                match_text = re.findall(p, output[0].return_text)
                self.utils.print_info(f"{match_text}")

                sw_model = []
                sw_model.append(match_text[0][1])

                self.utils.print_info(f"forward delay is {match_text[0][1]} seconds")

                kwargs['pass_msg'] = f"Forw delay for device is: {match_text[0][1]}"
                self.commonValidation.passed(**kwargs)

                return match_text[0][1]

        else:
            kwargs['fail_msg'] = f"get_nw_templ_device_config_forward_delay() failed, {dut.cli_type} not timplemented"
            self.commonValidation.fault(**kwargs)

    def set_nw_templ_device_config_forward_delay(self, dut, forward_delay=15, **kwargs):
        '''
        - Set the forward delay for a given EXOS device
        :param dut: the dut object
        :param forward_delay: the value of the forward delay to be set
        :return: the forward delay after being set
        '''
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2867
        if dut.cli_type.upper() == "EXOS":

            for attempts in range(3):
                sleep(5)
                # once support is added for any of the stories, the code will look like this:
                # self.networkElementConnectionManager.connect_to_network_element_name(dut.name)
                # output = self.networkElementSpanningtreeGenKeywords.spanningtree_set_fwd_delay(dut.name, forward_delay, "0")
                # print(output)
                # output = self.networkElementSpanningtreeGenKeywords.spanningtree_verify_bridge_forward_delay(dut.name,
                #                                                                                     forward_delay, "0")
                # print(output)
                self.networkElementConnectionManager.connect_to_network_element_name(dut.name)
                self.networkElementCliSend.send_cmd(dut.name, f'configure stpd s0 forwarddelay {forward_delay}',
                                     max_wait=10, interval=2)
                output = self.networkElementCliSend.send_cmd(dut.name, 'show stpd detail',
                                              max_wait=10,
                                              interval=2)
                self.networkElementConnectionManager.close_connection_to_network_element(dut.name)
                self.utils.print_info(output[0].return_text)

                p = re.compile(r'(CfgBrForwardDelay:\s+)+(\d+)', re.M)

                match_text = re.findall(p, output[0].return_text)
                self.utils.print_info(f"{match_text}")

                sw_model = []
                sw_model.append(match_text[0][1])

                kwargs['pass_msg'] = f"Forw delay for device is: {match_text[0][1]}"
                self.commonValidation.passed(**kwargs)

                return match_text[0][1]

        else:
            kwargs['fail_msg'] = f"get_nw_templ_device_config_forward_delay() failed, {dut.cli_type} not timplemented"
            self.commonValidation.fault(**kwargs)

    def delete_client_from_ap(self, cli_type, connection, client_mac, **kwargs):
        """
        - This Keyword will configure necessary CLI commands to delete Client from Access Point
        - Keyword Usage:
        -  ``delete_client_from_ap     ${CLI_TYPE}  ${CONNECTION}  ${CLIENT_MAC}``
        :param cli_type: The cli type
        :param connection: The open connection
        :param client_mac: Client Mac Address
        :return:  1 if commands successfully configured and client is getting removed from AP else -1
        """
        # TODO: https://jira.extremenetworks.com/browse/AIQ-2861
        if NetworkElementConstants.OS_AHAP in cli_type.upper():
            self.send(connection, f'clear auth station mac {client_mac}')
            self.send(connection, f'clear auth local-cache mac {client_mac}')
            self.send(connection, f'clear auth roaming-cache mac {client_mac} hive-all')
            self.send(connection, f'clear auth roaming-cache mac {client_mac}')
            show_client_output = self.send(connection, 'show station')
            client_mac_address = ':'.join(client_mac[i:i + 4] for i in range(0,len(client_mac),4))
            if client_mac_address.lower() not in show_client_output:
                kwargs['pass_msg'] = f"Client with Mac {client_mac} Successfully Deleted/Removed from AP "
                self.commonValidation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"Client with MAC {client_mac} still Present in the AP"
                self.commonValidation.failed(**kwargs)
                return -1
        return -1

if __name__ == '__main__':
    from pytest_testconfig import config
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
        -  ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}``
        -  ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60``
        -  ``Open Exos Switch Spawn   ${SPAWN}  ${COMMAND}  ${EXPECTED_OUTPUT}  ${RETRY_DURATION}=60  ${COUNT}=15``
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
                sleep(retry_duration)
            count += 1
        self.utils.print_info("Unable to get the expected output. Please check.")
        return -1