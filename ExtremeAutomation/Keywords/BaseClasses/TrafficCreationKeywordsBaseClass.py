from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.PacketCreation.PacketDefiner import PacketDefiner


class TrafficCreationKeywordsBaseClass(TrafficKeywordBaseClass):
    def __init__(self):
        super(TrafficCreationKeywordsBaseClass, self).__init__()

        self.add_to_dict = True
        self.pkt_def = None

    def _init_keyword(self, packet_name=None, **kwargs):
        super(TrafficCreationKeywordsBaseClass, self)._init_keyword(**kwargs)

        self.pkt_def = PacketDefiner()

        if packet_name is not None:
            self.packet = self.pkt_dict.get_packet(packet_name)

            # If the "packet" returned is actually a list assume it is a packet collection
            # and assign it to self.packet_collection.
            if isinstance(self.packet, list):
                self.pkt_col = self.packet

    def _parse_kwargs(self, dev, **kwargs):
        super(TrafficCreationKeywordsBaseClass, self)._parse_kwargs(kwargs)
        self.add_to_dict = self.get_kwarg_bool(kwargs, "add_to_dict", True)

    def _validate_packet_length(self):
        if self.packet is not None:
            if not self.packet.user_set_length:
                self.packet.auto_set_minimum_length()
        else:
            self.logger.log_info("No packet created, create a packet first.")
