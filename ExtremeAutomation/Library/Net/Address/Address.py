import abc


class Address(object, metaclass=abc.ABCMeta):
    def __init__(self, address, length):
        self.length = length
        self.pkt_bytes = [0] * length
        self.parse_address(address)

    @abc.abstractmethod
    def to_string(self):
        pass

    def to_formated_string(self, string_format, delim):
        ret_string = ""
        for byte in self.pkt_bytes:
            if string_format == 16:
                ret_string = str(hex(byte)).upper()[2:].zfill(2) + delim + ret_string
            elif string_format == 10:
                ret_string = str(byte) + delim + ret_string
        if delim and ret_string.endswith(delim):
            return ret_string[:-1]
        else:
            return ret_string

    def parse_address(self, address):
        if isinstance(address, str) and address.startswith("0x"):
            address = address[2:]
        if isinstance(address, int):
            # treat it as an integer
            hex_string = str(hex(address).replace("L", "")).upper()[2:].zfill(self.length * 2)
            self.parse_address("0x" + hex_string)
        elif "." in address:
            # probably an ip address
            parts = address.split('.')
            index = self.length - 1
            for part in parts:
                self.pkt_bytes[index] = int(part)
                index -= 1
        elif ":" in address or "-" in address:
            # probably a mac address
            parts = address.split(':') if ":" in address else address.split('-')
            index = self.length - 1
            for part in parts:
                self.pkt_bytes[index] = int(part, 16)
                index -= 1
        elif len(address) == self.length * 2 or (len(address) - 2 == self.length * 2 and address.startswith("0x")):
            # probably hex string
            if len(address) - 2 == self.length * 2 and address.startswith("0x"):
                address = address.replace("0x", "")
            parts = Address.split_hex(address).split(" ")
            index = self.length - 1
            for part in parts:
                self.pkt_bytes[index] = int(part, 16)
                index -= 1

    def get_bytes_string(self):
        ret_string = ""
        for byte in self.pkt_bytes:
            ret_string = (hex(byte)[2:].replace("L", "").zfill(2)).upper() + " " + ret_string
        return ret_string.strip()

    @staticmethod
    def split_hex(value):
        return " ".join(value[i:i + 2] for i in range(0, len(value), 2))

    @staticmethod
    def to_long(addr):
        pass

    @staticmethod
    def add_to_address(address, num):
        val = address.to_long(address)
        val += num
        address.parse_address(val)
        return address

    def __str__(self):
        return self.to_string()
