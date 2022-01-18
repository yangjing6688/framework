import abc
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class PortParserBaseClass(object, metaclass=abc.ABCMeta):
    def __init__(self, portlist):
        self.logger = Logger()
        self.port_block_ports = None
        self.media_type = None
        self.port_speed = None
        self.port_slot = None
        self.port_list = []
        self.speed_10_array = ["ethernet", "10"]
        self.speed_100_array = ["fast ethernet", "100"]
        self.speed_1000_array = ["gigabit ethernet", "1000"]
        self.speed_10000_array = ["ten gigabit ethernet", "10000"]
        self.speed_40000_array = ["forty gigabit ethernet", "40000"]
        self.media_types = {}
        self.port_block_dict = {}
        self.port_flag_dict = {}
        self.port_list = self.normalize_port_value(portlist)
        if portlist in [NetworkElementConstants.VALUE_NOT_PRESENT,
                        "emptyclireturn"]:
            self.port_block_ports = "none"
        else:
            self.port_block_ports = portlist.replace("\\+", ",")
        self.init_port()

    @staticmethod
    @abc.abstractmethod
    def normalize_port_value(portlist):
        """
        Converts the portlist for slot and port differences.
        """
        pass

    @abc.abstractmethod
    def init_port(self):
        """
        Sets the init values for the current port block.
        """
        pass
