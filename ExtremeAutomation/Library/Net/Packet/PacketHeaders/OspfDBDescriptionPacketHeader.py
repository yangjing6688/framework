from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import OspfPacketHeader, OspfTlvEntry
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class OspfDBDescriptionPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    OSPF DB Description Packet Header
        # Interface MTU = 16bits
        # Options = 8bits
        # DB Descript = 8bits
        # DD Sequence = 32bits
                http://www.freesoft.org/CIE/RFC/1583/105.htm
                0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |       0       |       0       |    Options    |0|0|0|0|0|I|M|MS
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                     DD sequence number                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                                                               |
       +-                                                             -+
       |                             A                                 |
       +-                 Link State Advertisement                    -+
       |                           Header                              |
       +-                                                             -+
       |                                                               |
       +-                                                             -+
       |                                                               |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

       ...                              |
        # link state age = 16bits
        # link state options = 8bits
        # link state type = 8bits
        # link state id = 32bits
        # advertising router = 32bits
        # sequence number = 32bits
        # checksum = 16bits
        # length = 16bits

       http://www.freesoft.org/CIE/RFC/1583/110.htm
                0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |            LS age             |    Options    |    LS type    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                        Link State ID                          |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                     Advertising Router                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                     LS sequence number                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |         LS checksum           |             length            |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    """

    def __init__(self):
        self.add_dbdescription_header()
        self.tlv_entries = []
        self.HEADER_SIZE_DBDESCRIPTION = 4  # BYTES
        self.links = []
        self.num_links = None
        self.num_lsa = 0
        self.lsa_entries = []
        self.set_lsa_num(0, True)

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start DBDescription Interface MTU methods
    #  interface_mtu is a 16 bit INTEGER example: 1
    def set_dbdescription_interface_mtu(self, interface_mtu, ignore_check=False):
        interface_mtu = self.normalize_value(interface_mtu, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_INTERFACE_MTU, interface_mtu)

    def get_dbdescription_interface_mtu(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_INTERFACE_MTU), PacketConstants.INTEGER)

    def get_dbdescription_interface_mtu_hltapi_cmd(self, dummy_dict):
        interface_mtu = self.get_dbdescription_interface_mtu()
        if isinstance(interface_mtu, int):
            interface_mtu = str(interface_mtu)
        if interface_mtu and 'Not Set' not in interface_mtu:
            dummy_dict[TrafficConfigConstants.TEMP_INTERFACE_MTU_CMD] = interface_mtu
    # end DBDescription Interface MTU methods

    # start DBDescription Options methods
    #  options is a 8 bit INTEGER example: 1
    def set_dbdescription_options(self, options, ignore_check=False):
        options = self.normalize_value(options, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_OPTIONS, options)

    def get_dbdescription_options(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_OPTIONS), PacketConstants.INTEGER)

    def get_dbdescription_options_hltapi_cmd(self, dummy_dict):
        options = self.get_dbdescription_options()
        if isinstance(options, int):
            options = str(options)
        if options and 'Not Set' not in options:
            dummy_dict[TrafficConfigConstants.TEMP_OPTIONS_CMD] = options
    # end DBDescription Options methods

    # start DBDescription DB Descript methods
    #  db_descript is a 8 bit IPV4_ADDRESS example: 1.2.3.4
    def set_dbdescription_db_descript(self, db_descript, ignore_check=False):
        db_descript = self.normalize_value(db_descript, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_DB_DESCRIPT, db_descript)

    def get_dbdescription_db_descript(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_DB_DESCRIPT), PacketConstants.INTEGER)

    def get_dbdescription_db_descript_hltapi_cmd(self, dummy_dict):
        db_descript = self.get_dbdescription_db_descript()
        if db_descript and 'Not Set' not in db_descript:
            dummy_dict[TrafficConfigConstants.TEMP_DB_DESCRIPT_CMD] = db_descript
    # end DBDescription DB Descript methods

    # start DBDescription DD Sequence methods
    #  dd_sequence is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_dbdescription_dd_sequence(self, dd_sequence, ignore_check=False):
        dd_sequence = self.normalize_value(dd_sequence, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_DD_SEQUENCE, dd_sequence)

    def get_dbdescription_dd_sequence(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_DD_SEQUENCE), PacketConstants.INTEGER)

    def get_dbdescription_dd_sequence_hltapi_cmd(self, dummy_dict):
        dd_sequence = self.get_dbdescription_dd_sequence()
        if dd_sequence and 'Not Set' not in dd_sequence:
            dummy_dict[TrafficConfigConstants.TEMP_DD_SEQUENCE_CMD] = dd_sequence
    # end DBDescription DD Sequence methods

    # start DBDescription link state age methods
    #  link_state_age is a 16 bit INTEGER example: 1
    def set_dbdescription_link_state_age(self, link_state_age, ignore_check=False):
        link_state_age = self.normalize_value(link_state_age, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_AGE, link_state_age)

    def get_dbdescription_link_state_age(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_AGE), PacketConstants.INTEGER)

    def get_dbdescription_link_state_age_hltapi_cmd(self, dummy_dict):
        link_state_age = self.get_dbdescription_link_state_age()
        if isinstance(link_state_age, int):
            link_state_age = str(link_state_age)
        if link_state_age and 'Not Set' not in link_state_age:
            dummy_dict[TrafficConfigConstants.TEMP_LINK_STATE_AGE_CMD] = link_state_age
    # end DBDescription link state age methods

    # start DBDescription link state options methods
    #  link_state_options is a 8 bit INTEGER example: 1
    def set_dbdescription_link_state_options(self, link_state_options, ignore_check=False):
        link_state_options = self.normalize_value(link_state_options, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_OPTIONS, link_state_options)

    def get_dbdescription_link_state_options(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_OPTIONS), PacketConstants.INTEGER)

    def get_dbdescription_link_state_options_hltapi_cmd(self, dummy_dict):
        link_state_options = self.get_dbdescription_link_state_options()
        if isinstance(link_state_options, int):
            link_state_options = str(link_state_options)
        if link_state_options and 'Not Set' not in link_state_options:
            dummy_dict[TrafficConfigConstants.TEMP_LINK_STATE_OPTIONS_CMD] = link_state_options
    # end DBDescription link state options methods

    # start DBDescription link state type methods
    #  link_state_type is a 8 bit INTEGER example: 1
    def set_dbdescription_link_state_type(self, link_state_type, ignore_check=False):
        link_state_type = self.normalize_value(link_state_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_TYPE, link_state_type)

    def get_dbdescription_link_state_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_TYPE), PacketConstants.INTEGER)

    def get_dbdescription_link_state_type_string(self):
        try:
            return OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_TYPES[
                self.get_dbdescription_link_state_type()]
        except Exception as e:
            PacketObject.logger.log_info(e)
            return "Unknown"

    def get_dbdescription_link_state_type_hltapi_cmd(self, dummy_dict):
        link_state_type = self.get_dbdescription_link_state_type()
        if isinstance(link_state_type, int):
            link_state_type = str(link_state_type)
        if link_state_type and 'Not Set' not in link_state_type:
            dummy_dict[TrafficConfigConstants.TEMP_LINK_STATE_TYPE_CMD] = link_state_type
    # end DBDescription link state type methods

    # start DBDescription link state id methods
    #  link_state_id is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_dbdescription_link_state_id(self, link_state_id, ignore_check=False):
        link_state_id = self.normalize_value(link_state_id, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_ID, link_state_id)

    def get_dbdescription_link_state_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_ID), PacketConstants.IPV4_ADDRESS)

    def get_dbdescription_link_state_id_hltapi_cmd(self, dummy_dict):
        link_state_id = self.get_dbdescription_link_state_id()
        if link_state_id and 'Not Set' not in link_state_id:
            dummy_dict[TrafficConfigConstants.TEMP_LINK_STATE_ID_CMD] = link_state_id
    # end DBDescription link state id methods

    # start DBDescription advertising router methods
    #  advertising_router is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_dbdescription_advertising_router(self, advertising_router, ignore_check=False):
        advertising_router = self.normalize_value(advertising_router, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_ADVERTISING_ROUTER, advertising_router)

    def get_dbdescription_advertising_router(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_ADVERTISING_ROUTER), PacketConstants.IPV4_ADDRESS)

    def get_dbdescription_advertising_router_hltapi_cmd(self, dummy_dict):
        advertising_router = self.get_dbdescription_advertising_router()
        if advertising_router and 'Not Set' not in advertising_router:
            dummy_dict[TrafficConfigConstants.TEMP_ADVERTISING_ROUTER_CMD] = advertising_router
    # end DBDescription advertising router methods

    # start DBDescription sequence number methods
    #  sequence_number is a 32 bit INTEGER example: 1
    def set_dbdescription_sequence_number(self, sequence_number, ignore_check=False):
        sequence_number = self.normalize_value(sequence_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_SEQUENCE_NUMBER, sequence_number)

    def get_dbdescription_sequence_number(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_SEQUENCE_NUMBER), PacketConstants.INTEGER)

    def get_dbdescription_sequence_number_hltapi_cmd(self, dummy_dict):
        sequence_number = self.get_dbdescription_sequence_number()
        if isinstance(sequence_number, int):
            sequence_number = str(sequence_number)
        if sequence_number and 'Not Set' not in sequence_number:
            dummy_dict[TrafficConfigConstants.TEMP_SEQUENCE_NUMBER_CMD] = sequence_number
    # end DBDescription sequence number methods

    # start DBDescription checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_dbdescription_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_CHECKSUM, checksum)

    def get_dbdescription_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_CHECKSUM), PacketConstants.INTEGER)

    def get_dbdescription_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_dbdescription_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end DBDescription checksum methods

    # start DBDescription length methods
    #  length is a 16 bit INTEGER example: 1
    def set_dbdescription_length(self, length, ignore_check=False):
        length = self.normalize_value(length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
                                  OspfDBDescriptionPacketConstants.DBDESCRIPTION_LENGTH, length)

    def get_dbdescription_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_DBDESCRIPTION,
            OspfDBDescriptionPacketConstants.DBDESCRIPTION_LENGTH), PacketConstants.INTEGER)

    def get_dbdescription_length_hltapi_cmd(self, dummy_dict):
        length = self.get_dbdescription_length()
        if isinstance(length, int):
            length = str(length)
        if length and 'Not Set' not in length:
            dummy_dict[TrafficConfigConstants.TEMP_LENGTH_CMD] = length
    # end DBDescription length methods

    def set_lls_data_block_checksum(self, active_neighbor, ignore_check=False):
        active_neighbor = self.normalize_value(active_neighbor, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfDBDescriptionPacketConstants.LLS_DATA_BLOCK_CHECKSUM, active_neighbor)

    def get_lls_data_block_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
            OspfDBDescriptionPacketConstants.LLS_DATA_BLOCK_CHECKSUM), PacketConstants.INTEGER)

    def set_lls_data_block_lengtgh(self, active_neighbor, ignore_check=False):
        active_neighbor = self.normalize_value(active_neighbor, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfDBDescriptionPacketConstants.LLS_DATA_BLOCK_LENGTH, active_neighbor)

    def get_lls_data_block_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
            OspfDBDescriptionPacketConstants.LLS_DATA_BLOCK_LENGTH), PacketConstants.INTEGER)

    def get_lsa_num(self):
        return self.num_lsa

    def set_lsa_num(self, num_lsas, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(OspfDBDescriptionPacketConstants.LINKSTATEUPDATE_LSA_NUM,
                                                        ignore_check)
        self.num_lsa = NumberUtils.to_integer_value(num_lsas)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  OspfDBDescriptionPacketConstants.LINKSTATEUPDATE_LSA_NUM, num_lsas)

    def add_lsa_entry(self, entry):
        self.set_lsa_num(self.num_lsa + 1)
        self.lsa_entries.append(entry)

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Interface MTU", self.format_int(self.get_dbdescription_interface_mtu(), 4))
        table.add_row_value("Options", self.format_int(self.get_dbdescription_options(), 2))
        table.add_row_value("DB Descript", self.get_dbdescription_db_descript())
        table.add_row_value("DD Sequence", self.get_dbdescription_dd_sequence())
        rt_string = "\n\nDBDESCRIPTION HEADER" + table.to_table_string()
        packet_length = self.get_ospf_packet_length()

        rt_string += "\n\nLINKSTATEUPDATE HEADER" + table.to_table_string()
        index = 0
        for entry in self.lsa_entries:
            index += 1
            assert isinstance(entry, OspfLinkStateLSAEntry)
            rt_string += "\n\n Link State Advertisement header #" + str(index) + "" + entry.to_packet_string()

        options = self.get_dbdescription_options()
        if isinstance(options, str) and "Not" in options:
            pass
        else:
            has_lls_data_block = (options & 0x10) > 0
            if has_lls_data_block:
                table_lls = TableFormatter()
                table_lls.add_row_value("Checksum", self.format_int(self.get_lls_data_block_checksum(), 2))
                table_lls.add_row_value("Length", self.format_int(self.get_lls_data_block_length(), 2))

                rt_string += "\n\nLLS Data Block" + table_lls.to_table_string()
                table_tlv = OspfTlvEntry.to_packet_string(self)
                rt_string += "\nOSPF LLS TLVs " + table_tlv.to_table_string()

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            rt_string += "\n\nAuth Crypt Data:" + self.get_ospf_auth_crypt_data() + "\n\n"

        return rt_string

    def add_dbdescription_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_OSPF_DBDESCRIPTION)

    def build(self):
        self.add_dbdescription_header()
        self.set_ospf_message_type(0x02, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_dbdescription_interface_mtu_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_options_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_db_descript_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_dd_sequence_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_link_state_age_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_link_state_options_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_link_state_type_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_link_state_id_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_advertising_router_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_sequence_number_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_checksum_hltapi_cmd(dummy_dict)
        # self.get_dbdescription_length_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_dbdescription(self, tgen_type, generator_ref, port_string, stream_id,
                                                                 **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_dbdescription(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_dbdescription(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_dbdescription(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kdbdescriptionFieldNumber
        # update this from the ostinato docs.
        #     dbdescriptionField = p.Extensions[dbdescription]
        #     if self.is_field_set(self.get_dbdescription_interface_mtu()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_interface_mtu())
        #     if self.is_field_set(self.get_dbdescription_options()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_options())
        #     if self.is_field_set(self.get_dbdescription_db_descript()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_db_descript())
        #     if self.is_field_set(self.get_dbdescription_dd_sequence()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_dd_sequence())
        #     if self.is_field_set(self.get_dbdescription_link_state_age()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_link_state_age())
        #     if self.is_field_set(self.get_dbdescription_link_state_options()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_link_state_options())
        #     if self.is_field_set(self.get_dbdescription_link_state_type()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_link_state_type())
        #     if self.is_field_set(self.get_dbdescription_link_state_id()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_link_state_id())
        #     if self.is_field_set(self.get_dbdescription_advertising_router()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_advertising_router())
        #     if self.is_field_set(self.get_dbdescription_sequence_number()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_sequence_number())
        #     if self.is_field_set(self.get_dbdescription_checksum()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_checksum())
        #     if self.is_field_set(self.get_dbdescription_length()) :
        #         dbdescriptionField.version = int(self.get_dbdescription_length())

    def config_jets_stream_dbdescription(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "DBDESCRIPTION_HDR"
        pkt_bytes = "0x" + OspfDBDescriptionPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_dbdescription_interface_mtu()) :
        #     pkt_fields["interface_mtu"] = int(self.get_dbdescription_interface_mtu())
        # if self.is_field_set(self.get_dbdescription_options()) :
        #     pkt_fields["options"] = int(self.get_dbdescription_options())
        # if self.is_field_set(self.get_dbdescription_db_descript()) :
        #     pkt_fields["db_descript"] = int(self.get_dbdescription_db_descript())
        # if self.is_field_set(self.get_dbdescription_dd_sequence()) :
        #     pkt_fields["dd_sequence"] = int(self.get_dbdescription_dd_sequence())
        # if self.is_field_set(self.get_dbdescription_link_state_age()) :
        #     pkt_fields["link_state_age"] = int(self.get_dbdescription_link_state_age())
        # if self.is_field_set(self.get_dbdescription_link_state_options()) :
        #     pkt_fields["link_state_options"] = int(self.get_dbdescription_link_state_options())
        # if self.is_field_set(self.get_dbdescription_link_state_type()) :
        #     pkt_fields["link_state_type"] = int(self.get_dbdescription_link_state_type())
        # if self.is_field_set(self.get_dbdescription_link_state_id()) :
        #     pkt_fields["link_state_id"] = int(self.get_dbdescription_link_state_id())
        # if self.is_field_set(self.get_dbdescription_advertising_router()) :
        #     pkt_fields["advertising_router"] = int(self.get_dbdescription_advertising_router())
        # if self.is_field_set(self.get_dbdescription_sequence_number()) :
        #     pkt_fields["sequence_number"] = int(self.get_dbdescription_sequence_number())
        # if self.is_field_set(self.get_dbdescription_checksum()) :
        #     pkt_fields["checksum"] = int(self.get_dbdescription_checksum())
        # if self.is_field_set(self.get_dbdescription_length()) :
        #     pkt_fields["length"] = int(self.get_dbdescription_length())

    def get_ixtclhal_dbdescription_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def parse_bytes(self):
        self.tlv_entries = []
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        interface_mtu = self.get_bits_from_string(16, payload)
        self.set_dbdescription_interface_mtu("0x" + interface_mtu)
        payload = self.remove_bits_from_string(16, payload)
        options = self.get_bits_from_string(8, payload)
        self.set_dbdescription_options("0x" + options)
        options = int(options, 16)
        has_lls_data_block = (options & 0x10) > 0
        payload = self.remove_bits_from_string(8, payload)
        db_descript = self.get_bits_from_string(8, payload)
        self.set_dbdescription_db_descript("0x" + db_descript)
        payload = self.remove_bits_from_string(8, payload)
        dd_sequence = self.get_bits_from_string(32, payload)
        self.set_dbdescription_dd_sequence("0x" + dd_sequence)
        payload = self.remove_bits_from_string(32, payload)

        packet_length = self.get_ospf_packet_length()
        end_length = 0
        if has_lls_data_block:
            end_length = 32
        auth_type = self.get_ospf_auth_type()
        auth_data = self.get_ospf_auth_data()
        if auth_type == 2:
            auth_length = auth_data.replace("0x", "").replace(" ", "")
            auth_length = int(auth_length[0:8], 16)
            end_length += auth_length * 8

        while len(payload) > end_length:
            link_state_age = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_update_link_state_age("0x" + link_state_age)
            payload = self.remove_bits_from_string(16, payload)
            link_state_options = int(self.get_bits_from_string(8, payload), 16)
            # self.set_link_state_update_link_state_options("0x" + link_state_options)
            payload = self.remove_bits_from_string(8, payload)
            link_state_type = int(self.get_bits_from_string(8, payload), 16)
            # self.set_link_state_update_link_state_type("0x" + link_state_type)
            payload = self.remove_bits_from_string(8, payload)
            link_state_id = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_update_link_state_id("0x" + link_state_id)
            payload = self.remove_bits_from_string(32, payload)
            advertising_router = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_update_advertising_router("0x" + advertising_router)
            payload = self.remove_bits_from_string(32, payload)
            sequence_number = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_update_sequence_number("0x" + sequence_number)
            payload = self.remove_bits_from_string(32, payload)
            checksum = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_update_checksum("0x" + checksum)
            payload = self.remove_bits_from_string(16, payload)
            length = int(self.get_bits_from_string(16, payload), 16)
            packet_length -= length
            # self.set_link_state_update_length("0x" + length)
            payload = self.remove_bits_from_string(16, payload)
            entry = OspfLinkStateLSAEntry(self, link_state_age, link_state_options, link_state_type, link_state_id,
                                          advertising_router, sequence_number, checksum, length)
            self.add_lsa_entry(entry)

        payload = OspfPacketHeader.process_auth_entry(payload, self)

        if has_lls_data_block:
            lls_checksum = self.get_bits_from_string(16, payload)
            self.set_lls_data_block_checksum("0x" + lls_checksum)
            payload = self.remove_bits_from_string(16, payload)

            lls_data_length = self.get_bits_from_string(16, payload)
            self.set_lls_data_block_lengtgh("0x" + lls_data_length)
            payload = self.remove_bits_from_string(16, payload)

            payload = OspfTlvEntry.process_tlv(payload, self.tlv_entries, lls_data_length, self)

        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_dbdescription_interface_mtu(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dbdescription_options(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbdescription_db_descript(), PacketConstants.IPV4_ADDRESS, 8)
        ret_string += self.format_byte_string(self.get_dbdescription_dd_sequence(), PacketConstants.IPV4_ADDRESS, 32)

        for entry in self.lsa_entries:
            assert isinstance(entry, OspfLinkStateLSAEntry)
            ret_string += entry.get_header_bytes()

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            ret_string += self.get_bytes_auth_entry(self).replace("0x", "")
        return ret_string

    @staticmethod
    def compare_dbdescription_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, OspfDBDescriptionPacketHeader)
            assert isinstance(actual, OspfDBDescriptionPacketHeader)
            if expected.is_field_set(expected.get_dbdescription_interface_mtu()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_INTERFACE_MTU not in ignore_list:
                name = "DBDESCRIPTION interface mtu : "
                if expected.get_dbdescription_interface_mtu() != actual.get_dbdescription_interface_mtu():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_interface_mtu()) + " != " +
                                                      str(actual.get_dbdescription_interface_mtu()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_interface_mtu()) + " == " +
                                                 str(actual.get_dbdescription_interface_mtu()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_options()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_OPTIONS not in ignore_list:
                name = "DBDESCRIPTION options : "
                if expected.get_dbdescription_options() != actual.get_dbdescription_options():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_options()) + " != " +
                                                      str(actual.get_dbdescription_options()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_options()) + " == " +
                                                 str(actual.get_dbdescription_options()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_db_descript()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_DB_DESCRIPT not in ignore_list:
                name = "DBDESCRIPTION db descript : "
                if expected.get_dbdescription_db_descript() != actual.get_dbdescription_db_descript():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_db_descript()) + " != " +
                                                      str(actual.get_dbdescription_db_descript()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_db_descript()) + " == " +
                                                 str(actual.get_dbdescription_db_descript()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_dd_sequence()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_DD_SEQUENCE not in ignore_list:
                name = "DBDESCRIPTION dd sequence : "
                if expected.get_dbdescription_dd_sequence() != actual.get_dbdescription_dd_sequence():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_dd_sequence()) + " != " +
                                                      str(actual.get_dbdescription_dd_sequence()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_dd_sequence()) + " == " +
                                                 str(actual.get_dbdescription_dd_sequence()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_link_state_age()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_AGE not in ignore_list:
                name = "DBDESCRIPTION link state age : "
                if expected.get_dbdescription_link_state_age() != actual.get_dbdescription_link_state_age():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_link_state_age()) + " != " +
                                                      str(actual.get_dbdescription_link_state_age()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_link_state_age()) + " == " +
                                                 str(actual.get_dbdescription_link_state_age()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_link_state_options()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_OPTIONS not in ignore_list:
                name = "DBDESCRIPTION link state options : "
                if expected.get_dbdescription_link_state_options() != actual.get_dbdescription_link_state_options():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_link_state_options()) + " != " +
                                                      str(actual.get_dbdescription_link_state_options()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_link_state_options()) + " == " +
                                                 str(actual.get_dbdescription_link_state_options()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_link_state_type()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_TYPE not in ignore_list:
                name = "DBDESCRIPTION link state type : "
                if expected.get_dbdescription_link_state_type() != actual.get_dbdescription_link_state_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_link_state_type()) + " != " +
                                                      str(actual.get_dbdescription_link_state_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_link_state_type()) + " == " +
                                                 str(actual.get_dbdescription_link_state_type()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_link_state_id()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_LINK_STATE_ID not in ignore_list:
                name = "DBDESCRIPTION link state id : "
                if expected.get_dbdescription_link_state_id() != actual.get_dbdescription_link_state_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_link_state_id()) + " != " +
                                                      str(actual.get_dbdescription_link_state_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_link_state_id()) + " == " +
                                                 str(actual.get_dbdescription_link_state_id()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_advertising_router()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_ADVERTISING_ROUTER not in ignore_list:
                name = "DBDESCRIPTION advertising router : "
                if expected.get_dbdescription_advertising_router() != actual.get_dbdescription_advertising_router():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_advertising_router()) + " != " +
                                                      str(actual.get_dbdescription_advertising_router()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_advertising_router()) + " == " +
                                                 str(actual.get_dbdescription_advertising_router()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_sequence_number()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_SEQUENCE_NUMBER not in ignore_list:
                name = "DBDESCRIPTION sequence number : "
                if expected.get_dbdescription_sequence_number() != actual.get_dbdescription_sequence_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_sequence_number()) + " != " +
                                                      str(actual.get_dbdescription_sequence_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_sequence_number()) + " == " +
                                                 str(actual.get_dbdescription_sequence_number()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_checksum()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_CHECKSUM not in ignore_list:
                name = "DBDESCRIPTION checksum : "
                if expected.get_dbdescription_checksum() != actual.get_dbdescription_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_checksum()) + " != " +
                                                      str(actual.get_dbdescription_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_checksum()) + " == " +
                                                 str(actual.get_dbdescription_checksum()) + " Pass")

            if expected.is_field_set(expected.get_dbdescription_length()) and \
                    OspfDBDescriptionPacketConstants.DBDESCRIPTION_LENGTH not in ignore_list:
                name = "DBDESCRIPTION length : "
                if expected.get_dbdescription_length() != actual.get_dbdescription_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbdescription_length()) + " != " +
                                                      str(actual.get_dbdescription_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbdescription_length()) + " == " +
                                                 str(actual.get_dbdescription_length()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with DBDescriptionPacketHeader")
        return results


class OspfLinkStateLSAEntry(object):
    """
     LSA header (they all have this):
       0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |            LS age             |     Options   |       1       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                        Link State ID                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                     Advertising Router                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                     LS sequence number                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         LS checksum           |             length            |
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length):
        self.handler = handler
        self.age = age
        self.option = option
        self.pkt_type = pkt_type
        self.pkt_id = pkt_id
        self.advertising_router = advertising_router
        self.sequence_number = sequence_number
        self.checksum = checksum
        self.length = length
        self.type_string = self.get_type_string(pkt_type)

    def get_type_string(self, lsa_type):
        if lsa_type == 0x01:
            return "LSA Type 1 (Router-LSA)"
        elif lsa_type == 0x02:
            return "LSA Type 2 (Network-LSA)"
        elif lsa_type == 0x03:
            return "LSA Type 3 (Summary-LSA IP Network)"
        elif lsa_type == 0x04:
            return "LSA Type 4 (Summary-LSA ASBR)"
        elif lsa_type == 0x05:
            return "LSA Type 5 (AS-External-LSA)"
        elif 0x05 < lsa_type <= 0x0A:
            return "Future Expansion"
        else:
            return "Unknown Type"

    def to_packet_string(self):
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Age", packet.format_int(self.age, 2))
        table_tlv.add_row_value("Options", packet.format_int(self.option, 2))
        table_tlv.add_row_value("Type", self.type_string + " " + packet.format_int(self.pkt_type, 2))
        table_tlv.add_row_value("ID", Ipv4Address(self.pkt_id))
        table_tlv.add_row_value("Advertising Router", Ipv4Address(self.advertising_router))
        table_tlv.add_row_value("Sequence Number", packet.format_int(self.sequence_number, 2))
        table_tlv.add_row_value("Checksum", packet.format_int(self.checksum, 2))
        table_tlv.add_row_value("Length", packet.format_int(self.length, 2))
        return table_tlv.to_table_string()

    def get_header_bytes(self):
        ret_string = ""
        handler = self.handler
        ret_string += handler.format_byte_string(self.age, PacketConstants.INTEGER, 16)
        ret_string += handler.format_byte_string(self.option, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.pkt_type, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.pkt_id, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.advertising_router, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.sequence_number, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.checksum, PacketConstants.INTEGER, 16)
        ret_string += handler.format_byte_string(self.length, PacketConstants.INTEGER, 16)
        return ret_string


class OspfDBDescriptionPacketConstants:
    def __init__(self):
        pass

    DBDESCRIPTION_INTERFACE_MTU = "DBDESCRIPTION_INTERFACE_MTU"
    DBDESCRIPTION_OPTIONS = "DBDESCRIPTION_OPTIONS"
    DBDESCRIPTION_DB_DESCRIPT = "DBDESCRIPTION_DB_DESCRIPT"
    DBDESCRIPTION_DD_SEQUENCE = "DBDESCRIPTION_DD_SEQUENCE"
    DBDESCRIPTION_LINK_STATE_AGE = "DBDESCRIPTION_LINK_STATE_AGE"
    DBDESCRIPTION_LINK_STATE_OPTIONS = "DBDESCRIPTION_LINK_STATE_OPTIONS"

    DBDESCRIPTION_LINK_STATE_TYPE = "DBDESCRIPTION_LINK_STATE_TYPE"
    DBDESCRIPTION_LINK_STATE_TYPE_ROUTER_LINKS = "1"
    DBDESCRIPTION_LINK_STATE_TYPE_NETWORK_LINKS = "2"
    DBDESCRIPTION_LINK_STATE_TYPE_SUMMARY_LINK_IP_NETWORK = "3"
    DBDESCRIPTION_LINK_STATE_TYPE_SUMMARY_LINK_ASBR = "4"
    DBDESCRIPTION_LINK_STATE_TYPE_AS_EXTERNAL_LINK = "5"
    DBDESCRIPTION_LINK_STATE_TYPES = {
        1: "Router links",
        2: "Network links",
        3: "Summary link(IP network)",
        4: "Summary link(ASBR)",
        5: "AS external link",
    }

    DBDESCRIPTION_LINK_STATE_ID = "DBDESCRIPTION_LINK_STATE_ID"
    DBDESCRIPTION_ADVERTISING_ROUTER = "DBDESCRIPTION_ADVERTISING_ROUTER"
    DBDESCRIPTION_SEQUENCE_NUMBER = "DBDESCRIPTION_SEQUENCE_NUMBER"
    DBDESCRIPTION_CHECKSUM = "DBDESCRIPTION_CHECKSUM"
    DBDESCRIPTION_LENGTH = "DBDESCRIPTION_LENGTH"
    LINKSTATEUPDATE_LSA_NUM = "LINKSTATEUPDATE_LSA_NUM"

    LLS_DATA_BLOCK_CHECKSUM = "HELLO_LLS_DATA_BLOCK_CHECKSUM"
    LLS_DATA_BLOCK_LENGTH = "HELLO_LLS_DATA_BLOCK_LENGTH"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
