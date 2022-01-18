from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.PacketUtils.PacketDictionary import PacketDictionary
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi \
    import TrafficConfigConstants


class StreamConfig(object):
    _pkt_dict = PacketDictionary()
    _valid_units = ["pps", "bps", "kbps", "mbps", "gbps", "percent", "%"]
    _config_constants = TrafficConfigConstants()
    _mac_src_modes = [getattr(TrafficConfigConstants, i) for i in dir(_config_constants)
                      if (i.startswith("MAC_SRC_MODE") and i != "MAC_SRC_MODE_CMD")]
    _mac_dst_modes = [getattr(TrafficConfigConstants, i) for i in dir(_config_constants)
                      if (i.startswith("MAC_DST_MODE") and i != "MAC_DST_MODE_CMD")]
    _ip_src_modes = [getattr(TrafficConfigConstants, i) for i in dir(_config_constants)
                     if (i.startswith("IP_SRC_MODE") and i != "IP_SRC_MODE_CMD")]
    _ip_dst_modes = [getattr(TrafficConfigConstants, i) for i in dir(_config_constants)
                     if (i.startswith("IP_DST_MODE") and i != "IP_DST_MODE_CMD")]

    def __init__(self, traffic_gen_name, port, stream_number):
        self.traffic_gen_name = traffic_gen_name
        self.port = port
        self.index = stream_number
        self.logger = Logger()
        self.mode = None
        self.burst_gap = None
        self.return_id = None
        self.return_to_id_count = None
        self.mac_src_count = None
        self.mac_src_step = None
        self.mac_dst_count = None
        self.mac_dst_step = None
        self.ip_src_count = None
        self.ip_src_mask = None
        self.ip_dst_count = None
        self.ip_dst_mask = None

        # Attributes with setter methods.
        self._count = None
        self._rate = None
        self._unit = None
        self._packet = None
        self._packet_collection = None
        self._mac_src_mask = "00:00:00:00:00:00"
        self._mac_src_mode = self._config_constants.MAC_SRC_MODE_FIXED
        self._mac_dst_mask = "00:00:00:00:00:00"
        self._mac_dst_mode = self._config_constants.MAC_DST_MODE_FIXED
        self._ip_src_mode = self._config_constants.IP_SRC_MODE_FIXED
        self._ip_dst_mode = self._config_constants.IP_DST_MODE_FIXED

    @property
    def count(self):
        """
        The packet count for the stream.
        """
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @property
    def rate(self):
        """
        The transmit rate of the stream.
        """
        if self._rate is not None:
            return int(self._rate)
        return None

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def unit(self):
        """
        The units for the rate of the stream.
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        if unit.lower() in self._valid_units:
            self._unit = unit.lower()
        else:
            self.logger.log_info("Invalid rate provided defaulting to PPS.")
            self.logger.log_info("Valid rates are \"pps/bps/Kbps/Mbps/Gbps/percent/%\".")
            self._unit = "pps"

    @property
    def packet(self):
        """
        The name of the packet used in the stream.
        """
        return self._packet

    @packet.setter
    def packet(self, packet_name):
        if isinstance(packet_name, str):
            packet = self._pkt_dict.get_packet(packet_name)
            if packet is not None:
                self._packet = packet
        elif isinstance(packet_name, AbstractPacket):
            self._packet = packet_name

    @property
    def packet_collection(self):
        """
        The name of the packet collection used in the streams.
        """
        return self._packet_collection

    @packet_collection.setter
    def packet_collection(self, packet_collection_name):
        if isinstance(packet_collection_name, str):
            packet_collection = self._pkt_dict.get_collection(packet_collection_name)
            if isinstance(packet_collection, list):
                self._packet_collection = packet_collection

    @property
    def mac_src_mask(self):
        """
        The mask value for incrementing/decrementing the Source MAC.
        """
        return self._mac_src_mask

    @mac_src_mask.setter
    def mac_src_mask(self, mask):
        mask = mask.replace(" ", "")

        if len(mask) == 12:
            new_mask = []
            for i in range(len(mask)):
                if i != 0 and i != len(mask):
                    if i % 2 == 0:
                        new_mask += ":"
                new_mask += mask[i]
            self._mac_src_mask = "".join(new_mask)
        else:
            self.logger.log_info("Invalid mask provided, defaulting to \"00:00:00:00:00:00\".")
            self._mac_src_mask = "00:00:00:00:00:00"

    @property
    def mac_src_mode(self):
        """
        The incrementing/decrementing mode for the Source MAC.
        """
        return self._mac_src_mode

    @mac_src_mode.setter
    def mac_src_mode(self, mode):
        if mode in self._mac_src_modes:
            self._mac_src_mode = mode
        else:
            self.logger.log_info("Invalid mac source mode provided, defaulting to fixed")
            self._mac_src_mode = self._config_constants.MAC_SRC_MODE_FIXED

    @property
    def mac_dst_mode(self):
        """
        The incrementing/decrementing mode for the Destination MAC.
        """
        return self._mac_dst_mode

    @mac_dst_mode.setter
    def mac_dst_mode(self, mode):
        if mode in self._mac_dst_modes:
            self._mac_dst_mode = mode
        else:
            self.logger.log_info("Invalid mac destination mode provided, defaulting to fixed")
            self._mac_dst_mode = self._config_constants.MAC_DST_MODE_FIXED

    @property
    def mac_dst_mask(self):
        """
        The mask value for incrementing/decrementing the Destination MAC.
        """
        return self._mac_dst_mask

    @mac_dst_mask.setter
    def mac_dst_mask(self, mask):
        mask = mask.replace(" ", "")

        if len(mask) == 12:
            new_mask = []
            for i in range(len(mask)):
                if i != 0 and i != len(mask):
                    if i % 2 == 0:
                        new_mask += ":"
                new_mask += mask[i]
            self._mac_dst_mask = "".join(new_mask)
        else:
            self.logger.log_info("Invalid mask provided, defaulting to \"00:00:00:00:00:00\".")
            self._mac_dst_mask = "00:00:00:00:00:00"

    @property
    def ip_src_mode(self):
        """
        The incrementing/decrementing mode for the Source IP Address.
        """
        return self._ip_src_mode

    @ip_src_mode.setter
    def ip_src_mode(self, mode):
        if mode in self._ip_src_modes:
            self._ip_src_mode = mode
        else:
            self.logger.log_info("Invalid IP source mode provided, defaulting to fixed")
            self._ip_src_mode = self._config_constants.IP_SRC_MODE_FIXED

    @property
    def ip_dst_mode(self):
        """
        The incrementing/decrementing mode for the Destination IP Address.
        """
        return self._ip_dst_mode

    @ip_dst_mode.setter
    def ip_dst_mode(self, mode):
        if mode in self._ip_dst_modes:
            self._ip_dst_mode = mode
        else:
            self.logger.log_info("Invalid IP destination mode provided, defaulting to fixed.")
            self._ip_dst_mode = self._config_constants.IP_DST_MODE_FIXED


s = StreamConfig("", "", "")
