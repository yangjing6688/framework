import re
import time
import socket
import errno
import telnetlib
from ExtremeAutomation.Library.Device.Common.Agents.CliAgent import CliAgent
from ExtremeAutomation.Library.Utils.Constants.Constants import Constants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class TelnetAgent(CliAgent):
    def __init__(self, device):
        super(TelnetAgent, self).__init__(device)
        self.type = self.constants.TYPE_TELNET
        
        slow_time = device.agent_kwargs.get('slow_login', '0')
        if slow_time.isdigit():
            self.slow_login_time = int(slow_time)
        else:
            self.slow_login_time = 0
            self.logger.log_error("Invalid value received for 'slow_login': {}\n"
                                  "Value must be a digit!".format(slow_time))

    def connect(self):
        """Creates a telnet session and attempts to connect with the devices IP (hostname) and port."""
        if not self.connected:
            self.main_session = telnetlib.Telnet()
            port = int(self.device.port) if self.device.port != "" else TelnetConstants.TELNET_PORT
            self.main_session.open(self.device.hostname, port, timeout=5)
            self.connected = True
        return self.main_session

    def login(self):
        """
        This function calls the connect function then attempts to login. It first looks for the
        login prompt. Once the login prompt is found it issues the username and waits for the
        password prompt. Once the password prompt is found it issues the password and waits for the
        main prompt. Once the main prompt is found the function returns True.
        """
        retries = 10
        found_main_prompt = False

        self.debug_print("Using telnet")
        if self.connected and self.logged_in:
            try:
                output = self.send_command("")
                if '*** IDLE TIMEOUT ***' in output:
                    self.connected = False
                    self.logged_in = False
                else:
                    self.debug_print("Already connected and logged in")
                    return True
            except socket.error:
                self.connected = False
                self.logged_in = False
        if not self.connected:
            try:
                self.connect()
                self.logged_in = False
            except socket.error:
                self.disconnect()
                return False
        output = self.wait_no_parse(250, 1)
        time.sleep(self.slow_login_time)
        output += self.wait_no_parse(250, 1)

        found_login_prompt = self.__pre_login_commands(output)

        # Try to find the login prompt.
        # Also check for the main prompt for term server connections.
        if not found_login_prompt:
            for i in range(0, retries):
                if output.strip().endswith(tuple(self.device.login_prompt)):
                    self.write_encode_ln(self.device.username)
                    found_login_prompt = True
                    break
                elif output.strip().endswith(self.device.main_prompt):
                    found_main_prompt = True
                    break
                else:
                    if output.strip().endswith('Press [Ctrl+ d] to go to the Suspend Menu.'):
                        self.write_encode_ln("\r")
                    else:
                        self.write_encode_ln("\n")
                    output += self.wait_no_parse(500, 1)

        # If we found the login prompt try to find the password prompt.
        if found_login_prompt:
            for i in range(0, retries):
                if output.strip().endswith(tuple(self.device.pass_prompt)):
                    adjusted_password = self.cmd_encode(self.device.password)
                    if self.get_enable_default_password_mode():
                        adjusted_password = self.cmd_encode(self.default_password)
                    self.write_encode_ln(adjusted_password)
                    break
                else:
                    output += self.wait_no_parse(250, 1)

        output += self.__post_login_commands(output)

        # Try to find the main prompt.
        if not found_main_prompt:
            for i in range(0, retries):
                if output.strip().endswith(self.device.main_prompt):
                    found_main_prompt = True
                    break
                else:
                    self.write_encode_ln("")
                    output += self.wait_no_parse(250, 1)

        # If we found the main prompt, but not the login prompt treat it as a terminal connection.
        if found_main_prompt:
            self.logged_in = True
        else:
            self.disconnect()
            return False

        if self.logged_in:
            self.__post_main_prompt_commands(output)
            self.debug_print("Telnet connected and logged in")
            self.take_prompt_snapshot(force_snapshot=True)
            return True
        else:
            self.logger.log_info("Telnet failed to login")
            self.disconnect()
            return False

    def logout(self):
        """
        Logs out of the telnet session.
        """
        self.debug_print("Closing telnet")
        if self.main_session is not None:
            self.disconnect()

    def write(self, text):
        """
        Function Args:
        [text] - The text to send to the telnet session.

        Writes the given text to the telnet session. This may fail if the text is no encoded first.
        Call self.cmd_encode on the text or use the write_encode function.
        """
        if self.connected:
            try:
                return self.main_session.write(text.encode('ascii'))
            except socket.error as e:
                if e.errno != errno.EPIPE:
                    raise e
            # Already disconnected.
                else:
                    pass

    def wait_no_parse(self, ms, retries):
        """
        Function Args:
        [ms] - Time in milliseconds to wait between read attempts.
        [retries] - Number of times to retry the read before returning.

        Reads from the telnet session retries <retries> times and appends any new data before
        returning. Each read will delay <ms> milliseconds before attempting another.
        """
        if not self.connected:
            raise EOFError("Telnet session closed.")

        return_string = ""

        for num in range(0, retries + 1):
            return_string += self.main_session.read_very_eager().decode("utf-8")
            time.sleep(ms / 1000.0)
        vt100_escapes = re.compile(r"(\x1b\[|\x9b)[^@-_]*[@-_]|\x1b[@-_]", re.I)
        return_string = vt100_escapes.sub("", return_string)
        return return_string

    def read_until(self, text):
        """
        Function Args:
        [text] - The text that causes the telnet session to stop reading.

        This function will read data until the given <text> is found.
        """
        if not self.connected:
            raise EOFError("Telnet session closed.")
        return self.main_session.read_until(text.encode("ascii")).decode("utf-8")

    def read_until_list_match(self, _list):
        """
        Function Args:
        [_list] - A list of strings that will cause the read to stop.

        This function will read until one of the items in the list matches. It will return all data that was read.
        """
        if not self.connected:
            raise EOFError("Telnet session closed.")

        return_data = self.main_session.expect([i.encode('ascii') for i in _list])

        return return_data[2].decode("utf-8")

    def disconnect(self):
        """
        Closes the connection to the telnet session.
        """
        try:
            super(TelnetAgent, self).disconnect()
        except (EOFError, socket.error):
            # Already disconnected.
            pass

        self.main_session.close()
        self.connected = False

    def __pre_login_commands(self, output):
        if self.device.oper_sys == 'BOSS':
            # This is for login on BOSS, there is no login prompt.
            if "ctrl" in output.lower():
                ctrl_output = output.lower().split("ctrl")
                output_chars_after_ctrl = ctrl_output[1][:3]
                prompt_char = re.sub('[^a-zA-Z]+', '', output_chars_after_ctrl)
                self.write_encode_ln("^" + prompt_char.upper())
                self.wait_no_parse(250, 1)
                self.write_encode_ln('enable')
                output = self.wait_no_parse(250, 1)
                if output.strip().endswith(self.device.main_prompt):
                    return True
                return False
        return False

    def __post_login_commands(self, output):
        if self.device.oper_sys == NetworkElementConstants.OS_VOSS:
            self.write_encode_ln("")
            output += self.wait_no_parse(250, 5)
        else:
            output += self.wait_no_parse(250, 1)

        if self.device.oper_sys in [NetworkElementConstants.OS_VOSS,
                                    NetworkElementConstants.OS_ALPHA,
                                    NetworkElementConstants.OS_SLX,
                                    NetworkElementConstants.OS_ICX,
                                    NetworkElementConstants.OS_MLX,
                                    NetworkElementConstants.OS_VDX]:
            if output.endswith(">"):
                self.write_encode_ln("enable")
                output += self.wait_no_parse(250, 1)

        self.debug_print(output)
        return output

    def __post_main_prompt_commands(self, output):
        if self.device.oper_sys == NetworkElementConstants.OS_EXOS:
            self.debug_print(self.send_command("disable clipaging"))
        elif self.device.oper_sys == NetworkElementConstants.OS_VOSS:
            self.debug_print(self.send_command("terminal more disable"))
        elif self.device.oper_sys == NetworkElementConstants.OS_AHAP:
            self.debug_print(self.send_command("console page 0"))
        elif self.device.oper_sys in [NetworkElementConstants.OS_AHFASTPATH,
                                      NetworkElementConstants.OS_AHXR]:
            self.debug_print(self.send_command("enable"))
            self.debug_print(self.send_command("configure"))
            self.debug_print(self.send_command("do terminal length 0"))
        elif self.device.oper_sys in [NetworkElementConstants.OS_ALPHA,
                                      NetworkElementConstants.OS_BOSS,
                                      NetworkElementConstants.OS_SLX]:
            self.debug_print(self.send_command("terminal length 0"))
        elif self.device.oper_sys in [NetworkElementConstants.OS_ICX,
                                      NetworkElementConstants.OS_MLX]:
            self.device.main_prompt = "#"
            self.send_command("enable")
            output += self.wait_no_parse(250, 1)
            if output.endswith("#"):
                self.logged_in = True
            self.debug_print(self.send_command("skip-page-display"))
        elif self.device.oper_sys in [NetworkElementConstants.OS_VDX]:
            self.debug_print(self.send_command(""))


class TelnetConstants(Constants):
    TELNET_PORT = 23
