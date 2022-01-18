from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants


class Checksum(object):
    MAX_16_BIT_WORD = 0x10000

    def __init__(self):
        pass

    @staticmethod
    def calculate_udp_checksum(packet, pkt_bytes, offset):
        pseudo = ""
        if "4" in packet.get_name():
            sip = packet.format_byte_string(packet.get_source_ip(), PacketConstants.IPV4_ADDRESS, 32)
            dip = packet.format_byte_string(packet.get_destination_ip(), PacketConstants.IPV4_ADDRESS, 32)
            protocol = packet.format_byte_string(packet.get_ip_protocol(), PacketConstants.INTEGER, 8)
            length = packet.get_udp_length()
            length = packet.format_byte_string(length, PacketConstants.INTEGER, 16)
            pseudo = sip + dip + "00" + protocol + length
        pkt_bytes = (pseudo + pkt_bytes[(offset * 2):]).replace(" ", "")
        pkt_bytes = pkt_bytes[:-8]
        header_sum = Checksum.calculate_headersum(pkt_bytes)
        return header_sum

    @staticmethod
    def calculate_tcp_checksum(packet, pkt_bytes, offset):
        pseudo = ""
        if "4" in packet.get_name():
            sip = packet.format_byte_string(packet.get_source_ip(), PacketConstants.IPV4_ADDRESS, 32)
            dip = packet.format_byte_string(packet.get_destination_ip(), PacketConstants.IPV4_ADDRESS, 32)
            protocol = packet.format_byte_string(packet.get_ip_protocol(), PacketConstants.INTEGER, 8)
            all_bytes = pkt_bytes
            length = (len(all_bytes) // 2 - offset) - 4
            length = packet.format_byte_string(length, PacketConstants.INTEGER, 16)
            pseudo = sip + dip + "00" + protocol + length
        pkt_bytes = (pseudo + pkt_bytes[(offset * 2):]).replace(" ", "")
        pkt_bytes = pkt_bytes[:-8]
        header_sum = Checksum.calculate_headersum(pkt_bytes)
        return header_sum

    @staticmethod
    def calculate_ip_checksum(pkt_bytes, offset, end_offset):
        pkt_bytes = pkt_bytes[(offset * 2):]
        pkt_bytes = pkt_bytes[:end_offset * 2]
        headerSum = Checksum.calculate_headersum(pkt_bytes)
        return headerSum

    @staticmethod
    def calculate_icmp_checksum(packet, pkt_bytes, offset, end_offset):
        pseudo = ""
        if "4" in packet.get_name():  # ipv4 pseudo header
            sip = packet.format_byte_string(packet.get_source_ip(), PacketConstants.IPV4_ADDRESS, 32)
            dip = packet.format_byte_string(packet.get_destination_ip(), PacketConstants.IPV4_ADDRESS, 32)
            protocol = packet.format_byte_string(packet.get_ip_protocol(), PacketConstants.INTEGER, 8)
            all_bytes = pkt_bytes
            length = (len(all_bytes) // 2 - offset) - 4
            length = packet.format_byte_string(length, PacketConstants.INTEGER, 16)
            pseudo = sip + dip + "00" + protocol + length
        elif "6" in packet.get_name():  # ipv6 pseudo header
            sip = packet.format_byte_string(packet.get_ipv6_source_address(), PacketConstants.IPV6_ADDRESS, 128)
            dip = packet.format_byte_string(packet.get_ipv6_destination_address(), PacketConstants.IPV6_ADDRESS, 128)
            payload_length = packet.format_byte_string(packet.get_ipv6_payload_length(), PacketConstants.INTEGER, 8)
            # extention headers
            pseudo = sip + dip + "00" + payload_length
        pkt_bytes = (pseudo + pkt_bytes[(offset * 2):]).replace(" ", "")
        pkt_bytes = pkt_bytes[:-8]
        header_sum = Checksum.calculate_headersum(pkt_bytes)
        return header_sum

    @staticmethod
    def calculate_headersum(pkt_bytes):
        """
        Make sure the checksum is zero'd out.
        """
        headerSum = 0
        while len(pkt_bytes) % 4 != 0:
            pkt_bytes += "0"
        while len(pkt_bytes) > 0:
            chunk = pkt_bytes[0:4]
            pkt_bytes = pkt_bytes[4:]
            headerSum += int(chunk, 16)
        headerSum = (headerSum & 0x0FFFF) + ((headerSum & 0x0FFFF0000) >> 16)
        return headerSum

    @staticmethod
    def calculate_complement(decimalValue):
        pkt_sum = int(decimalValue // Checksum.MAX_16_BIT_WORD) + int(decimalValue % Checksum.MAX_16_BIT_WORD)
        if pkt_sum >= Checksum.MAX_16_BIT_WORD:
            complement = ~(1 + pkt_sum) & 0xFFFF
        else:
            complement = ~(0 + pkt_sum) & 0xFFFF
        return complement
