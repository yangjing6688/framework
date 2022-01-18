import time
import serial
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent


class SerialAgent(TelnetAgent):
    def __init__(self, device):
        super(SerialAgent, self).__init__(device)
        self.com_port = "COM3"
        self.baud_rate = 9600
        self.byte_size = serial.EIGHTBITS  # Number of bits per byte.
        self.parity = serial.PARITY_NONE   # Set parity check: no parity.
        self.stop_bits = serial.STOPBITS_ONE
        self.type = self.constants.TYPE_SERIAL

    def connect(self):
        """
        Opens the serial connection if no connection exists.
        """
        if not self.connected:
            self.main_session = serial.Serial()
            self.main_session.baudrate = self.baud_rate
            self.main_session.port = self.com_port
            self.main_session.open()
            self.connected = True
        return self.main_session

    def logout(self):
        """
        Logs out of the serial connection then disconnects.
        """
        self.debug_print("Closing serial.")

        if self.main_session is not None:
            self.disconnect()

    def wait_no_parse(self, ms, retries):
        """
        Function Args:
        [ms] - Time in milliseconds to wait between read attempts.
        [retries] - Number of times to retry the read before returning.

        Reads from teh telnet session retries <retries> times and appends any new data before
        returning. Each read will delay <ms> milliseconds before attempting another.
        """
        if self.connected:
            return_string = ""

            for num in range(0, retries + 1):
                return_string += self.main_session.read_all()
                time.sleep(ms / 1000.0)
            return return_string

    def read_until(self, text):
        """
        Function Args:
        [text] - The text that causes the telnet session to stop reading.

        This function will read data until the given <text> is found.
        """
        if self.connected:
            if not text:
                return self.main_session.read_all()
            else:
                return self.main_session.read_until(text)

    def read_until_list_match(self, _list):
        """
        Function Args:
        [_list] - A list of strings that will cause the read to stop.

        This function will read until one of the items in the list matches. It will return all data that was read.
        """
        if self.connected:
            output = ""
            while not any(elem in output for elem in _list):
                output += self.wait_no_parse(10, 10)
            return output

    def flush(self):
        """
        Flushes the serial connection.
        """
        self.write("")
        output = self.read_until("")
        if output != "":
            self.write("")
            self.read_until("")
