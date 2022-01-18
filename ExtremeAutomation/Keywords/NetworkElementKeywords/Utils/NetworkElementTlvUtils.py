from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2LldpPacket import Ethernet2LldpPacket


class NetworkElementTlvUtils(NetworkElementKeywordBaseClass):

    def build_custom_tlv(self, device_name, tlv_name, tlv_type, tlv_length, tlv_message, **kwargs):
        """
        Builds an LLDP TLV based on custom user information.
        """
        self._init_keyword(device_name, **kwargs)

        if tlv_length.startswith("0x"):
            tlv_length = int(tlv_length, base=16)

        tlv_message = tlv_message.replace("0x", "")
        tlv_message = "0x" + ("0" * ((int(tlv_length) * 2) - len(tlv_message))) + tlv_message

        lldp_packet = Ethernet2LldpPacket()

        index = lldp_packet.add_lldp_entry(tlv_type)
        lldp_packet.set_lldp_tlv_length(tlv_length, index)
        lldp_packet.set_lldp_tlv_message(tlv_message, index)

        tlv = lldp_packet.get_lldp_tlv_in_hex_string(index)

        self.value_storage.add_value(device_name, tlv_name, tlv)

        return tlv

    def build_custom_tlv_with_subtype(self, device_name, tlv_name, tlv_type, tlv_length, tlv_subtype, tlv_message,
                                      **kwargs):
        """
        Builds a custom LLDP TLV with additional subtype data from user input.
        """
        self._init_keyword(device_name, **kwargs)

        tlv_message = tlv_message.replace("0x", "")
        tlv_message = ("0x" + ("0" * ((int(tlv_length) * 2) - len(tlv_message + tlv_subtype))) +
                       tlv_subtype + tlv_message)

        tlv = self.build_custom_tlv(device_name, tlv_name, tlv_type, tlv_length, tlv_message, log_keyword=False,
                                    **kwargs)

        return tlv

    def build_custom_tlv_with_oui(self, device_name, tlv_name, tlv_type, tlv_length, tlv_oui, tlv_subtype, tlv_message,
                                  **kwargs):
        """
        Builds a custom LLDP TLV with additional OUI and subtype data from user input.
        """
        self._init_keyword(device_name, **kwargs)

        tlv_message = tlv_message.replace("0x", "")
        tlv_message = ("0x" + ("0" * ((int(tlv_length) * 2) - len(tlv_message + tlv_subtype + tlv_oui))) +
                       tlv_oui + tlv_subtype + tlv_message)

        tlv = self.build_custom_tlv(device_name, tlv_name, tlv_type, tlv_length, tlv_message, log_keyword=False,
                                    **kwargs)

        return tlv

    def find_tlv_by_type(self, tlv_list, tlv_type, tlv_subtype=None, tlv_oui=None):
        """
        Returns a matching TLV, by type, if it exists in the tlv_list.
        """
        if isinstance(tlv_list, list):
            matching_tlvs = list()

            if not tlv_type.startswith("0x"):
                tlv_type = hex(int(tlv_type))
            if tlv_subtype is not None:
                if not tlv_subtype.startswith("0x"):
                    tlv_subtype = hex(int(tlv_subtype))
            if tlv_oui is not None:
                if not tlv_oui.startswith("0x"):
                    tlv_oui = hex(int(tlv_oui))

            # Check each TLVs type, if it matches tlv_type, append it the matching_tlvs list.
            for tlv in tlv_list:
                parse_tlv_type = NetworkElementTlvParse.parse_tlv_type(tlv)

                if parse_tlv_type == tlv_type:
                    matching_tlvs.append(tlv)

            # If len(matching_tlvs) > 1, check the tlv subtype. Append all TLVs with subtype
            # equal to tlv_subtype (if provided)
            if len(matching_tlvs) > 1 and tlv_subtype is not None:
                temp_matching_tlvs = list(matching_tlvs)

                for tlv in matching_tlvs:
                    parse_tlv_type = NetworkElementTlvParse.parse_tlv_type(tlv)
                    if parse_tlv_type == hex(127):
                        parse_tlv_subtype = NetworkElementTlvParse.parse_tlv_subtype(tlv, tlv_level="oui")
                    else:
                        parse_tlv_subtype = NetworkElementTlvParse.parse_tlv_subtype(tlv)

                    if int(parse_tlv_subtype, base=16) != int(tlv_subtype, base=16):
                        temp_matching_tlvs.remove(tlv)

                matching_tlvs = list(temp_matching_tlvs)

            # If len(matching_tlvs) > 1, check the tlv oui. Append all TLVs with oui
            # equal to tlv_oui (if provided)
            if len(matching_tlvs) > 1 and tlv_oui is not None:
                temp_matching_tlvs = list(matching_tlvs)

                for tlv in matching_tlvs:
                    parse_tlv_oui = NetworkElementTlvParse.parse_tlv_oui(tlv)
                    if int(parse_tlv_oui, base=16) != int(tlv_oui, base=16):
                        temp_matching_tlvs.remove(tlv)

                matching_tlvs = list(temp_matching_tlvs)

            if len(matching_tlvs) == 1:
                self.logger.log_info("Found matching TLV: " + matching_tlvs[0])
                return matching_tlvs[0]
            else:
                self.logger.log_info("Unable to find unique TLV, try providing more parameters.")
                return None

        else:
            self.logger.log_info("Did not receive a list of TLVs!")

    @staticmethod
    def tlv_comparator(cap_tlv, tlv_field, exp_value, tlv_level="message"):
        """
        Compares the TLV to an expected value and returns True if matching.
        """
        tlv_parse = NetworkElementTlvParse()
        exp_value = exp_value.lower()

        if tlv_field == "type":
            if not exp_value.startswith("0x"):
                exp_value = hex(int(exp_value))
            cap_type = tlv_parse.parse_tlv_type(cap_tlv)
            return True if cap_type == exp_value else False

        elif tlv_field == "length":
            if not exp_value.startswith("0x"):
                exp_value = hex(int(exp_value))
            cap_length = tlv_parse.parse_tlv_length(cap_tlv)
            return True if cap_length == exp_value else False

        elif tlv_field == "oui":
            if not exp_value.startswith("0x"):
                exp_value = hex(int(exp_value))
            cap_oui = tlv_parse.parse_tlv_oui(cap_tlv)
            return True if cap_oui == exp_value else False

        elif tlv_field == "subtype":
            if not exp_value.startswith("0x"):
                exp_value = hex(int(exp_value))
            cap_subtype = tlv_parse.parse_tlv_subtype(cap_tlv, tlv_level)
            return True if cap_subtype == exp_value else False

        elif tlv_field == "message":
            if not exp_value.startswith("0x"):
                exp_value = exp_value.encode("hex")
            cap_message = tlv_parse.parse_tlv_message(cap_tlv, tlv_level)
            return True if cap_message == exp_value else False


class NetworkElementTlvParse(object):

    @staticmethod
    def parse_tlv_type(tlv):
        """
        Returns the TLV type of the given TLV.
        """
        if isinstance(tlv, str):
            tlv_bits = bin(int(tlv[:2], base=16))

            if tlv_bits == "0b0":
                tlv_bits = "0b00"

            tlv_type = hex(int(tlv_bits[:-1], base=2))
        else:
            raise Exception("parse_tlv requires a single TLV string, received a list.")

        return tlv_type

    @staticmethod
    def parse_tlv_length(tlv):
        """
        Returns the TLV length of the given TLV.
        """
        if isinstance(tlv, str):
            tlv_bits = bin(int(tlv[1:4], base=16))

            if tlv_bits == "0b0":
                tlv_bits = "0b00"

            length = hex(int(tlv_bits[7:], base=2))
        else:
            raise Exception("parse_tlv requires a single TLV string, received a list.")

        return length

    @staticmethod
    def parse_tlv_oui(tlv):
        """
        Returns the TLV OUI of the given TLV.
        """
        if isinstance(tlv, str):
            oui = "0x" + tlv[4:10]
        else:
            raise Exception("parse_tlv requires a single TLV string, received a list.")

        return oui

    @staticmethod
    def parse_tlv_subtype(tlv, tlv_level="subtype"):
        """
        Returns the TLV subtype of the given TLV.
        """
        if isinstance(tlv, str):
            if tlv_level.lower() == "subtype":
                subtype = "0x" + tlv[4:6]
            elif tlv_level.lower() == "oui":
                subtype = "0x" + tlv[10:12]
            else:
                raise Exception("Unknown TLV Level " + tlv_level)
        else:
            raise Exception("parse_tlv requires a single TLV string, received a list.")

        return subtype

    @staticmethod
    def parse_tlv_message(tlv, tlv_level="message"):
        """
        Returns the TLV message of the given TLV.
        """
        if isinstance(tlv, str):
            if tlv_level.lower() == "message":
                message = "0x" + tlv[4:]
            elif tlv_level.lower() == "subtype":
                message = "0x" + tlv[6:]
            elif tlv_level.lower() == "oui":
                message = "0x" + tlv[12:]
            else:
                raise Exception("Unknown TLV Level " + tlv_level)
        else:
            raise Exception("parse_tlv requires a single TLV string, received a list.")

        return message
