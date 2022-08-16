import time
import socket
import paramiko
from ExtremeAutomation.Library.Device.Common.Agents.CliAgent import CliAgent
from netmiko import ConnectHandler, NetMikoTimeoutException  # pip install netmiko
from ExtremeAutomation.Library.Utils.Constants.Constants import Constants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenConstants import TrafficGenConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class SshAgent(CliAgent):
    def __init__(self, device):
        super(SshAgent, self).__init__(device)
        self.type = self.constants.TYPE_SSH

    def connect(self):
        """
        This function is not needed for ssh, since the connection is part of the login.
        """
        pass

    def login(self):
        """
        This function will both create the SSH connection as well as login.
        """
        self.debug_print("Using ssh.")

        try:
            if self.connected and self.logged_in:
                self.debug_print("Already connected and logged in.")
                return True

            adjusted_password = self.cmd_encode(self.device.password)
            if self.get_enable_default_password_mode():
                adjusted_password = self.cmd_encode(self.default_password)

            ssh_args = {"device_type": "cisco_ios",
                        "ip": self.cmd_encode(self.device.hostname),
                        "username": self.cmd_encode(self.device.username),
                        "password": adjusted_password,
                        "port": self.device.port,
                        "timeout": 30,
                        "keepalive": 3,
                        "banner_timeout": 200,
                        "auth_timeout": 200}

            if self.device.oper_sys in [NetworkElementConstants.OS_EOS,
                                        NetworkElementConstants.OS_BOSS,
                                        TrafficGenConstants.JETS_CHASSIS.upper(),
                                        NetworkElementConstants.OS_SLX,
                                        EndsystemElementConstants.OS_WINDOWS,
                                        EndsystemElementConstants.OS_WINDOWS_MU,
                                        EndsystemElementConstants.OS_A3]:
                ssh_args["device_type"] = "terminal_server"
            elif self.device.oper_sys == NetworkElementConstants.OS_EXOS:
                ssh_args["device_type"] = "extreme"
            elif self.device.oper_sys in [NetworkElementConstants.OS_LINUX,
                                          NetworkElementConstants.OS_SNAP_ROUTE]:
                ssh_args["device_type"] = "ovs_linux"
            elif self.device.oper_sys == NetworkElementConstants.OS_VOSS:
                ssh_args["device_type"] = "avaya_vsp"

            try:
                self.logger.log_debug("SSH Connection values:" +
                                      ", ".join("{}: {}".format(key, value) for key, value in ssh_args.items()))
                client = ConnectHandler(**ssh_args)
                connect_using_paramiko = self.get_disable_strict_host_key_checking()
                if connect_using_paramiko:
                    self.logger.log_debug("Disabling SSH key Checking for Remote Device/Host On Server")
                    paramiko_ssh_connection = paramiko.SSHClient()
                    paramiko_ssh_connection.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
                    paramiko_ssh_connection.connect(ssh_args["ip"], port=ssh_args["port"], username=ssh_args["username"], password=ssh_args["password"],
                                                         look_for_keys=False, allow_agent=False)

                if self.device.oper_sys == NetworkElementConstants.OS_VOSS:
                    # client._test_channel_read()  # Re-enable this if read_channel() doesn't work.
                    client.read_channel()
                    client.set_base_prompt()
                    client.send_command("enable", strip_prompt=False, auto_find_prompt=False)
                if self.device.oper_sys == NetworkElementConstants.OS_AHAP:
                    # client._test_channel_read()  # Re-enable this if read_channel() doesn't work.
                    client.read_channel()
                    client.set_base_prompt()
                    client.send_command("console page 0", strip_prompt=False, auto_find_prompt=False)
                if self.device.oper_sys in [NetworkElementConstants.OS_AHFASTPATH,
                                            NetworkElementConstants.OS_AHXR]:
                    # client._test_channel_read()  # Re-enable this if read_channel() doesn't work.
                    client.read_channel()
                    client.send_command("enable", strip_prompt=False, auto_find_prompt=False)
                    client.send_command("configure", strip_prompt=False, auto_find_prompt=False)
                    client.set_base_prompt()
                    client.send_command("do terminal length 0", strip_prompt=False, auto_find_prompt=False)
                self.main_session = client
                self.debug_print("SSH connected.")
                self.connected = True
                self.logged_in = True
            except NetMikoTimeoutException:
                if self.device.oper_sys == NetworkElementConstants.OS_EXOS:
                    self.debug_print("Error when connecting with SSH.")

            if self.device.oper_sys == NetworkElementConstants.OS_BOSS:
                self.write_encode_ln("^Y")
                self.send_command("terminal length 0")
                self.send_command("")

            if self.main_session is not None:
                self.take_prompt_snapshot()
                return True
        except Exception as e:
            self.logger.log_info("Unable to connect via SSH: " + str(e))
            self.connected = False
            self.logged_in = False
            return False

    def logout(self):
        """
        This function will close the SSH connection."
        """
        self.debug_print("Closing ssh connection.")
        if self.main_session is not None:
            self.disconnect()

    def write(self, text):
        """
        Function Args:
        [text] - The text that will be written to the SSH session.

        Writes the given text to the SSH session.

        Note: Call cmd_encode on <text> or this command might fail.
        """
        if self.connected:
            return self.main_session.remote_conn.sendall(text)

    def wait_no_parse(self, ms, retries):
        """
        Function Args:
        [ms] - The amount of time in milliseconds the function should wait between read attempts.
        [retries] - The number of reads this function should attempt.

        This function will attempt to read <retries> times from the SSH session. Between each read it will delay
        <ms> milliseconds.
        """
        if not self.connected:
            raise EOFError("SSH session closed.")

        # check to see if EOF is True, set the connection as closed and return an error
        if type(self.main_session.remote_conn.eof_received) == bool and self.main_session.remote_conn.eof_received:
            self.main_session.remote_conn.close()
            raise EOFError("SSH session got EOF")

        return_string = ""

        for num in range(0, retries + 1):
            if self.main_session.remote_conn.recv_ready():
                return_string += self.main_session.remote_conn.recv(65535).decode("utf-8")
            if self.main_session.remote_conn.recv_stderr_ready():
                return_string += self.main_session.remote_conn.recv_stderr(65535).decode("utf-8")
            time.sleep(ms / 1000.0)
        return return_string

    def read_until(self, text):
        """
        Function Args:
        [text] - The text that causes the SSH session to stop reading.

        This function will read data until the given <text> is found.
        """
        output = ""
        while text not in output:
            output += self.wait_no_parse(10, 10)
        return output

    def read_until_list_match(self, _list):
        """
        Function Args:
        [_list] - A list of strings that will cause the read to stop.

        This function will read until one of the items in the list matches. It will return all data that was read.
        """
        output = ""
        while not any(elem in output for elem in _list):
            output += self.wait_no_parse(10, 10)
        return output

    def disconnect(self):
        """
        Closes the SSH connection.
        """
        try:
            self.main_session.disconnect()
        except (AttributeError, socket.error):
            pass

        try:
            super(SshAgent, self).disconnect()
        except (socket.error, AttributeError):
            # Session is already closed.
            pass

        self.connected = False
        self.logged_in = False


class SshConstants(Constants):
    SSH_PORT = 22
