import ExtremeAutomation.Library.Net.Packet.PacketClassifier as pc
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.CollectionUtils import CollectionUtils
"""
This class is used to store created packets during a test suite.

It allows the user to store, retrieve, and delete packets.
"""


class PacketDictionary(object):

    packet_dictionary = dict()

    def __init__(self):
        self.logger = Logger()

    def add_packet(self, packet_name, packet):
        """
        Arguments:
        [packet_name] - The string name of a packet.
        [packet] - The packet object to add.

        Adds a packet to the packet_dictionary.
        If a packet already exists in the dictionary it will be overwritten.
        """
        self.packet_dictionary[packet_name] = packet

    def add_collection(self, collection_name, collection):
        """
        Arguments:
        [collection_name] - The name of the packet collection.
        [collection] - A list of packet objects.

        Adds a collection of packets to packet_dictionary.
        If a collection already exists in the dictionary it will be overwritten.
        """
        self.packet_dictionary[collection_name] = collection

    def remove_packet(self, packet_name):
        """
        Arguments:
        [packet_name] - The string name of a packet that should be removed.

        Removes the specified packet from the dictionary.
        """
        try:
            self.packet_dictionary.pop(packet_name)
        except KeyError:
            self.logger.log_info("Packet not found!")
            return False

    def get_packet(self, packet_name):
        """
        Arguments:
        [packet_name] - The string name of the packet to retrieve.

        Retrieves the specified packet from the dictionary.
        """
        try:
            return self.packet_dictionary[packet_name]
        except KeyError:
            if isinstance(packet_name, pc.Ethernet2PacketHeader) or isinstance(packet_name, pc.SapPacketHeader):
                return packet_name
            else:
                self.logger.log_info("Packet not found in dictionary!")
                return False

    def contains_packet(self, packet_name):
        """
        Arguments:
        [packet_name] - The string name of the packet to check the existence of.

        Checks if the packet dictionary contains a packet with name <packet_name>.
        """
        return packet_name in self.packet_dictionary

    def get_collection(self, collection_name):
        """
        Arguments:
        [collection_name] - The string name of the packet collection to retrieve.

        Retrieves a collection of packets from the dictionary.
        """
        try:
            collection = self.packet_dictionary[collection_name]

            if isinstance(collection, list):
                return collection
            else:
                self.logger.log_info("Unable to locate a collection with name " + collection_name +
                                     " verify it was created.")
        except KeyError:
            self.logger.log_info("Unable to locate a collection with name " + collection_name +
                                 " verify it was created.")
            return False

    def __str__(self):
        """Returns the Packet Dictionary as a string."""
        return "contents of packet dictionary:" + CollectionUtils.dict_to_string(self.packet_dictionary)
