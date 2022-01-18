from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump


class BootpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    BOOTP Packet Header
        # Op Code = 8bits
        # Hardware Type = 8bits
        # Hardward Address = 8bits
        # Hops = 8bits
        # Transaction ID = 32bits
        # Seconds = 16bits
        # Flags = 16bits
        # Client IP Address = 32bits
        # Your Client IP Address = 32bits
        # Next Server IP Address = 32bits
        # Relay Agent IP Address = 32bits
        # Client MAC Address = 128bits
        # Server Host Name = 64bits
        # Boot File Name = 1024bits
        # Magic Cookie = 32bits
    """

    def __init__(self):
        self.add_bootp_header()
        self.bootp_options = []
        self.HEADER_SIZE_BOOTP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Bootp Op Code methods
    #  op_code is a 8 bit INTEGER example: 1
    def set_bootp_op_code(self, op_code, ignore_check=False):
        op_code = self.normalize_value(op_code, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_OP_CODE, op_code)

    def get_bootp_op_code(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_OP_CODE), PacketConstants.INTEGER)

    def get_bootp_op_code_hltapi_cmd(self, dummy_dict):
        op_code = self.get_bootp_op_code()
        if isinstance(op_code, int):
            op_code = str(op_code)
        if op_code and 'Not Set' not in op_code:
            dummy_dict[TrafficConfigConstants.TEMP_OP_CODE_CMD] = op_code
    # end Bootp Op Code methods

    # start Bootp Hardware Type methods
    #  hardware_type is a 8 bit INTEGER example: 1
    def set_bootp_hardware_type(self, hardware_type, ignore_check=False):
        hardware_type = self.normalize_value(hardware_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_HARDWARE_TYPE, hardware_type)

    def get_bootp_hardware_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_HARDWARE_TYPE), PacketConstants.INTEGER)

    def get_bootp_hardware_type_hltapi_cmd(self, dummy_dict):
        hardware_type = self.get_bootp_hardware_type()
        if isinstance(hardware_type, int):
            hardware_type = str(hardware_type)
        if hardware_type and 'Not Set' not in hardware_type:
            dummy_dict[TrafficConfigConstants.TEMP_HARDWARE_TYPE_CMD] = hardware_type
    # end Bootp Hardware Type methods

    # start Bootp Hardward Address methods
    #  hardward_address is a 8 bit INTEGER example: 1
    def set_bootp_hardward_address(self, hardward_address, ignore_check=False):
        hardward_address = self.normalize_value(hardward_address, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_HARDWARD_ADDRESS, hardward_address)

    def get_bootp_hardward_address(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_HARDWARD_ADDRESS),
            PacketConstants.INTEGER)

    def get_bootp_hardward_address_hltapi_cmd(self, dummy_dict):
        hardward_address = self.get_bootp_hardward_address()
        if isinstance(hardward_address, int):
            hardward_address = str(hardward_address)
        if hardward_address and 'Not Set' not in hardward_address:
            dummy_dict[TrafficConfigConstants.TEMP_HARDWARD_ADDRESS_CMD] = hardward_address
    # end Bootp Hardward Address methods

    # start Bootp Hops methods
    #  hops is a 8 bit INTEGER example: 1
    def set_bootp_hops(self, hops, ignore_check=False):
        hops = self.normalize_value(hops, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_HOPS, hops)

    def get_bootp_hops(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_HOPS), PacketConstants.INTEGER)

    def get_bootp_hops_hltapi_cmd(self, dummy_dict):
        hops = self.get_bootp_hops()
        if isinstance(hops, int):
            hops = str(hops)
        if hops and 'Not Set' not in hops:
            dummy_dict[TrafficConfigConstants.TEMP_HOPS_CMD] = hops
    # end Bootp Hops methods

    # start Bootp Transaction ID methods
    #  transaction_id is a 32 bit INTEGER example: 1
    def set_bootp_transaction_id(self, transaction_id, ignore_check=False):
        transaction_id = self.normalize_value(transaction_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_TRANSACTION_ID, transaction_id)

    def get_bootp_transaction_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_TRANSACTION_ID), PacketConstants.INTEGER)

    def get_bootp_transaction_id_hltapi_cmd(self, dummy_dict):
        transaction_id = self.get_bootp_transaction_id()
        if isinstance(transaction_id, int):
            transaction_id = str(transaction_id)
        if transaction_id and 'Not Set' not in transaction_id:
            dummy_dict[TrafficConfigConstants.TEMP_TRANSACTION_ID_CMD] = transaction_id
    # end Bootp Transaction ID methods

    # start Bootp Seconds methods
    #  seconds is a 16 bit INTEGER example: 1
    def set_bootp_seconds(self, seconds, ignore_check=False):
        seconds = self.normalize_value(seconds, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_SECONDS, seconds)

    def get_bootp_seconds(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_SECONDS), PacketConstants.INTEGER)

    def get_bootp_seconds_hltapi_cmd(self, dummy_dict):
        seconds = self.get_bootp_seconds()
        if isinstance(seconds, int):
            seconds = str(seconds)
        if seconds and 'Not Set' not in seconds:
            dummy_dict[TrafficConfigConstants.TEMP_SECONDS_CMD] = seconds
    # end Bootp Seconds methods

    # start Bootp Flags methods
    #  flags is a 16 bit INTEGER example: 1
    def set_bootp_flags(self, flags, ignore_check=False):
        flags = self.normalize_value(flags, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_FLAGS, flags)

    def get_bootp_flags(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_FLAGS), PacketConstants.INTEGER)

    def get_bootp_flags_hltapi_cmd(self, dummy_dict):
        flags = self.get_bootp_flags()
        if isinstance(flags, int):
            flags = str(flags)
        if flags and 'Not Set' not in flags:
            dummy_dict[TrafficConfigConstants.TEMP_FLAGS_CMD] = flags
    # end Bootp Flags methods

    # start Bootp Client IP Address methods
    #  client_ip_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_bootp_client_ip_address(self, client_ip_address, ignore_check=False):
        client_ip_address = self.normalize_value(client_ip_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_CLIENT_IP_ADDRESS, client_ip_address)

    def get_bootp_client_ip_address(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_CLIENT_IP_ADDRESS),
            PacketConstants.IPV4_ADDRESS)

    def get_bootp_client_ip_address_hltapi_cmd(self, dummy_dict):
        client_ip_address = self.get_bootp_client_ip_address()
        if client_ip_address and 'Not Set' not in client_ip_address:
            dummy_dict[TrafficConfigConstants.TEMP_CLIENT_IP_ADDRESS_CMD] = client_ip_address
    # end Bootp Client IP Address methods

    # start Bootp Your Client IP Address methods
    #  your_client_ip_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_bootp_your_client_ip_address(self, your_client_ip_address, ignore_check=False):
        your_client_ip_address = self.normalize_value(your_client_ip_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_YOUR_CLIENT_IP_ADDRESS, your_client_ip_address)

    def get_bootp_your_client_ip_address(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_YOUR_CLIENT_IP_ADDRESS),
            PacketConstants.IPV4_ADDRESS)

    def get_bootp_your_client_ip_address_hltapi_cmd(self, dummy_dict):
        your_client_ip_address = self.get_bootp_your_client_ip_address()
        if your_client_ip_address and 'Not Set' not in your_client_ip_address:
            dummy_dict[TrafficConfigConstants.TEMP_YOUR_CLIENT_IP_ADDRESS_CMD] = your_client_ip_address
    # end Bootp Your Client IP Address methods

    # start Bootp Next Server IP Address methods
    #  next_server_ip_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_bootp_next_server_ip_address(self, next_server_ip_address, ignore_check=False):
        next_server_ip_address = self.normalize_value(next_server_ip_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_NEXT_SERVER_IP_ADDRESS, next_server_ip_address)

    def get_bootp_next_server_ip_address(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_NEXT_SERVER_IP_ADDRESS),
            PacketConstants.IPV4_ADDRESS)

    def get_bootp_next_server_ip_address_hltapi_cmd(self, dummy_dict):
        next_server_ip_address = self.get_bootp_next_server_ip_address()
        if next_server_ip_address and 'Not Set' not in next_server_ip_address:
            dummy_dict[TrafficConfigConstants.TEMP_NEXT_SERVER_IP_ADDRESS_CMD] = next_server_ip_address
    # end Bootp Next Server IP Address methods

    # start Bootp Relay Agent IP Address methods
    #  relay_agent_ip_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_bootp_relay_agent_ip_address(self, relay_agent_ip_address, ignore_check=False):
        relay_agent_ip_address = self.normalize_value(relay_agent_ip_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_RELAY_AGENT_IP_ADDRESS, relay_agent_ip_address)

    def get_bootp_relay_agent_ip_address(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_RELAY_AGENT_IP_ADDRESS),
            PacketConstants.IPV4_ADDRESS)

    def get_bootp_relay_agent_ip_address_hltapi_cmd(self, dummy_dict):
        relay_agent_ip_address = self.get_bootp_relay_agent_ip_address()
        if relay_agent_ip_address and 'Not Set' not in relay_agent_ip_address:
            dummy_dict[TrafficConfigConstants.TEMP_RELAY_AGENT_IP_ADDRESS_CMD] = relay_agent_ip_address
    # end Bootp Relay Agent IP Address methods

    # start Bootp Client MAC Address methods
    #  client_mac_address is a 128 bit HEX_STRING example: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    def set_bootp_client_mac_address(self, client_mac_address, ignore_check=False):
        client_mac_address = self.normalize_value(client_mac_address, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_CLIENT_MAC_ADDRESS, client_mac_address)

    def get_bootp_client_mac_address(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_CLIENT_MAC_ADDRESS),
            PacketConstants.HEX_STRING)

    def get_bootp_client_mac_address_hltapi_cmd(self, dummy_dict):
        client_mac_address = self.get_bootp_client_mac_address()
        if client_mac_address and 'Not Set' not in client_mac_address:
            dummy_dict[TrafficConfigConstants.TEMP_CLIENT_MAC_ADDRESS_CMD] = client_mac_address
    # end Bootp Client MAC Address methods

    # start Bootp Server Host Name methods
    #  server_host_name is a 64 bit HEX_STRING example: FFFFFFFFFFFFFFFF
    def set_bootp_server_host_name(self, server_host_name, ignore_check=False):
        server_host_name = self.normalize_value(server_host_name, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_SERVER_HOST_NAME, server_host_name)

    def get_bootp_server_host_name(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_SERVER_HOST_NAME),
            PacketConstants.HEX_STRING)

    def get_bootp_server_host_name_hltapi_cmd(self, dummy_dict):
        server_host_name = self.get_bootp_server_host_name()
        if server_host_name and 'Not Set' not in server_host_name:
            dummy_dict[TrafficConfigConstants.TEMP_SERVER_HOST_NAME_CMD] = server_host_name
    # end Bootp Server Host Name methods

    # start Bootp Boot File Name methods
    #  boot_file_name is a 1024 bit HEX_STRING example: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    #                                                   FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    #                                                   FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    #                                                   FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    def set_bootp_boot_file_name(self, boot_file_name, ignore_check=False):
        boot_file_name = self.normalize_value(boot_file_name, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_BOOT_FILE_NAME, boot_file_name)

    def get_bootp_boot_file_name(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_BOOT_FILE_NAME),
            PacketConstants.HEX_STRING)

    def get_bootp_boot_file_name_hltapi_cmd(self, dummy_dict):
        boot_file_name = self.get_bootp_boot_file_name()
        if boot_file_name and 'Not Set' not in boot_file_name:
            dummy_dict[TrafficConfigConstants.TEMP_BOOT_FILE_NAME_CMD] = boot_file_name
    # end Bootp Boot File Name methods

    # start Bootp Magic Cookie methods
    #  magic_cookie is a 32 bit HEX_STRING example: FFFFFFFF
    def set_bootp_magic_cookie(self, magic_cookie, ignore_check=False):
        magic_cookie = self.normalize_value(magic_cookie, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BOOTP,
                                  BootpPacketConstants.BOOTP_MAGIC_COOKIE, magic_cookie)

    def get_bootp_magic_cookie(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_BOOTP, BootpPacketConstants.BOOTP_MAGIC_COOKIE),
            PacketConstants.HEX_STRING)

    def get_bootp_magic_cookie_hltapi_cmd(self, dummy_dict):
        magic_cookie = self.get_bootp_magic_cookie()
        if magic_cookie and 'Not Set' not in magic_cookie:
            dummy_dict[TrafficConfigConstants.TEMP_MAGIC_COOKIE_CMD] = magic_cookie
    # end Bootp Magic Cookie methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Op Code", self.format_int(self.get_bootp_op_code(), 1))
        table.add_row_value("Hardware Type", self.format_int(self.get_bootp_hardware_type(), 1))
        table.add_row_value("Hardward Address", self.format_int(self.get_bootp_hardward_address(), 1))
        table.add_row_value("Hops", self.format_int(self.get_bootp_hops(), 1))
        table.add_row_value("Transaction ID", self.format_int(self.get_bootp_transaction_id(), 4))
        table.add_row_value("Seconds", self.format_int(self.get_bootp_seconds(), 2))
        table.add_row_value("Flags", self.format_int(self.get_bootp_flags(), 2))
        table.add_row_value("Client IP Address", self.get_bootp_client_ip_address())
        table.add_row_value("Your Client IP Address", self.get_bootp_your_client_ip_address())
        table.add_row_value("Next Server IP Address", self.get_bootp_next_server_ip_address())
        table.add_row_value("Relay Agent IP Address", self.get_bootp_relay_agent_ip_address())
        table.add_row_value("Client MAC Address", self.get_bootp_client_mac_address())
        table.add_row_value("Server Host Name", self.get_bootp_server_host_name())
        table.add_row_value("Boot File Name", self.get_bootp_boot_file_name())
        table.add_row_value("Magic Cookie", self.get_bootp_magic_cookie())

        ret_string = "\n\nBOOTP HEADER" + table.to_table_string()
        table_tlv = BootpOptions.to_packet_string(self)
        return ret_string + "\n\nBOOTP Options" + table_tlv.to_table_string()

    def add_bootp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_BOOTP)

    def build(self):
        self.add_bootp_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_bootp_op_code_hltapi_cmd(dummy_dict)
        # self.get_bootp_hardware_type_hltapi_cmd(dummy_dict)
        # self.get_bootp_hardward_address_hltapi_cmd(dummy_dict)
        # self.get_bootp_hops_hltapi_cmd(dummy_dict)
        # self.get_bootp_transaction_id_hltapi_cmd(dummy_dict)
        # self.get_bootp_seconds_hltapi_cmd(dummy_dict)
        # self.get_bootp_flags_hltapi_cmd(dummy_dict)
        # self.get_bootp_client_ip_address_hltapi_cmd(dummy_dict)
        # self.get_bootp_your_client_ip_address_hltapi_cmd(dummy_dict)
        # self.get_bootp_next_server_ip_address_hltapi_cmd(dummy_dict)
        # self.get_bootp_relay_agent_ip_address_hltapi_cmd(dummy_dict)
        # self.get_bootp_client_mac_address_hltapi_cmd(dummy_dict)
        # self.get_bootp_server_host_name_hltapi_cmd(dummy_dict)
        # self.get_bootp_boot_file_name_hltapi_cmd(dummy_dict)
        # self.get_bootp_magic_cookie_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_bootp(self, tgen_type, generator_ref, port_string, stream_id,
                                                         **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_bootp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_bootp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_bootp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kbootpFieldNumber
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = BootpPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData
    # update this from the ostinato docs.
        # bootpField = p.Extensions[bootp]
        # if self.is_field_set(self.get_bootp_op_code()) :
        #     bootpField.version = int(self.get_bootp_op_code())
        # if self.is_field_set(self.get_bootp_hardware_type()) :
        #     bootpField.version = int(self.get_bootp_hardware_type())
        # if self.is_field_set(self.get_bootp_hardward_address()) :
        #     bootpField.version = int(self.get_bootp_hardward_address())
        # if self.is_field_set(self.get_bootp_hops()) :
        #     bootpField.version = int(self.get_bootp_hops())
        # if self.is_field_set(self.get_bootp_transaction_id()) :
        #     bootpField.version = int(self.get_bootp_transaction_id())
        # if self.is_field_set(self.get_bootp_seconds()) :
        #     bootpField.version = int(self.get_bootp_seconds())
        # if self.is_field_set(self.get_bootp_flags()) :
        #     bootpField.version = int(self.get_bootp_flags())
        # if self.is_field_set(self.get_bootp_client_ip_address()) :
        #     bootpField.version = int(self.get_bootp_client_ip_address())
        # if self.is_field_set(self.get_bootp_your_client_ip_address()) :
        #     bootpField.version = int(self.get_bootp_your_client_ip_address())
        # if self.is_field_set(self.get_bootp_next_server_ip_address()) :
        #     bootpField.version = int(self.get_bootp_next_server_ip_address())
        # if self.is_field_set(self.get_bootp_relay_agent_ip_address()) :
        #     bootpField.version = int(self.get_bootp_relay_agent_ip_address())
        # if self.is_field_set(self.get_bootp_client_mac_address()) :
        #     bootpField.version = int(self.get_bootp_client_mac_address())
        # if self.is_field_set(self.get_bootp_server_host_name()) :
        #     bootpField.version = int(self.get_bootp_server_host_name())
        # if self.is_field_set(self.get_bootp_boot_file_name()) :
        #     bootpField.version = int(self.get_bootp_boot_file_name())
        # if self.is_field_set(self.get_bootp_magic_cookie()) :
        #     bootpField.version = int(self.get_bootp_magic_cookie())

    def config_jets_stream_bootp(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "BOOTP_HDR"
        pkt_bytes = "0x" + BootpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_bootp_op_code()):
            pkt_fields["op_code"] = int(self.get_bootp_op_code())
        if self.is_field_set(self.get_bootp_hardware_type()):
            pkt_fields["hardware_type"] = int(self.get_bootp_hardware_type())
        if self.is_field_set(self.get_bootp_hardward_address()):
            pkt_fields["hardward_address"] = int(self.get_bootp_hardward_address())
        if self.is_field_set(self.get_bootp_hops()):
            pkt_fields["hops"] = int(self.get_bootp_hops())
        if self.is_field_set(self.get_bootp_transaction_id()):
            pkt_fields["transaction_id"] = int(self.get_bootp_transaction_id())
        if self.is_field_set(self.get_bootp_seconds()):
            pkt_fields["seconds"] = int(self.get_bootp_seconds())
        if self.is_field_set(self.get_bootp_flags()):
            pkt_fields["flags"] = int(self.get_bootp_flags())
        if self.is_field_set(self.get_bootp_client_ip_address()):
            pkt_fields["client_ip_address"] = int(self.get_bootp_client_ip_address())
        if self.is_field_set(self.get_bootp_your_client_ip_address()):
            pkt_fields["your_client_ip_address"] = int(self.get_bootp_your_client_ip_address())
        if self.is_field_set(self.get_bootp_next_server_ip_address()):
            pkt_fields["next_server_ip_address"] = int(self.get_bootp_next_server_ip_address())
        if self.is_field_set(self.get_bootp_relay_agent_ip_address()):
            pkt_fields["relay_agent_ip_address"] = int(self.get_bootp_relay_agent_ip_address())
        if self.is_field_set(self.get_bootp_client_mac_address()):
            pkt_fields["client_mac_address"] = int(self.get_bootp_client_mac_address())
        if self.is_field_set(self.get_bootp_server_host_name()):
            pkt_fields["server_host_name"] = int(self.get_bootp_server_host_name())
        if self.is_field_set(self.get_bootp_boot_file_name()):
            pkt_fields["boot_file_name"] = int(self.get_bootp_boot_file_name())
        if self.is_field_set(self.get_bootp_magic_cookie()):
            pkt_fields["magic_cookie"] = int(self.get_bootp_magic_cookie())

    def get_ixtclhal_bootp_api_commands(self, port_string, streamid):
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
        self.bootp_options = []
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        op_code = self.get_bits_from_string(8, payload)
        self.set_bootp_op_code("0x" + op_code)
        payload = self.remove_bits_from_string(8, payload)
        hardware_type = self.get_bits_from_string(8, payload)
        self.set_bootp_hardware_type("0x" + hardware_type)
        payload = self.remove_bits_from_string(8, payload)
        hardward_address = self.get_bits_from_string(8, payload)
        self.set_bootp_hardward_address("0x" + hardward_address)
        payload = self.remove_bits_from_string(8, payload)
        hops = self.get_bits_from_string(8, payload)
        self.set_bootp_hops("0x" + hops)
        payload = self.remove_bits_from_string(8, payload)
        transaction_id = self.get_bits_from_string(32, payload)
        self.set_bootp_transaction_id("0x" + transaction_id)
        payload = self.remove_bits_from_string(32, payload)
        seconds = self.get_bits_from_string(16, payload)
        self.set_bootp_seconds("0x" + seconds)
        payload = self.remove_bits_from_string(16, payload)
        flags = self.get_bits_from_string(16, payload)
        self.set_bootp_flags("0x" + flags)
        payload = self.remove_bits_from_string(16, payload)
        client_ip_address = self.get_bits_from_string(32, payload)
        self.set_bootp_client_ip_address("0x" + client_ip_address)
        payload = self.remove_bits_from_string(32, payload)
        your_client_ip_address = self.get_bits_from_string(32, payload)
        self.set_bootp_your_client_ip_address("0x" + your_client_ip_address)
        payload = self.remove_bits_from_string(32, payload)
        next_server_ip_address = self.get_bits_from_string(32, payload)
        self.set_bootp_next_server_ip_address("0x" + next_server_ip_address)
        payload = self.remove_bits_from_string(32, payload)
        relay_agent_ip_address = self.get_bits_from_string(32, payload)
        self.set_bootp_relay_agent_ip_address("0x" + relay_agent_ip_address)
        payload = self.remove_bits_from_string(32, payload)
        client_mac_address = self.get_bits_from_string(128, payload)
        self.set_bootp_client_mac_address("0x" + client_mac_address)
        payload = self.remove_bits_from_string(128, payload)
        server_host_name = self.get_bits_from_string(64 * 8, payload)
        self.set_bootp_server_host_name("0x" + server_host_name)
        payload = self.remove_bits_from_string(64 * 8, payload)
        boot_file_name = self.get_bits_from_string(1024, payload)
        self.set_bootp_boot_file_name("0x" + boot_file_name)
        payload = self.remove_bits_from_string(1024, payload)
        magic_cookie = self.get_bits_from_string(32, payload)
        self.set_bootp_magic_cookie("0x" + magic_cookie)
        payload = self.remove_bits_from_string(32, payload)
        self.payload = payload
        # processBootp Options
        self.payload = BootpOptions.process_options(payload, self.bootp_options, 155555, self)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_bootp_op_code(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_bootp_hardware_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_bootp_hardward_address(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_bootp_hops(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_bootp_transaction_id(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_bootp_seconds(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_bootp_flags(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_bootp_client_ip_address(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_bootp_your_client_ip_address(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_bootp_next_server_ip_address(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_bootp_relay_agent_ip_address(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_bootp_client_mac_address(), PacketConstants.HEX_STRING, 128)
        ret_string += self.format_byte_string(self.get_bootp_server_host_name(), PacketConstants.HEX_STRING, 64 * 8)
        ret_string += self.format_byte_string(self.get_bootp_boot_file_name(), PacketConstants.HEX_STRING, 1024)
        ret_string += self.format_byte_string(self.get_bootp_magic_cookie(), PacketConstants.HEX_STRING, 32)

        for entry in self.bootp_options:
            ret_string += self.format_byte_string(entry.pkt_type, PacketConstants.INTEGER, 8)
            if entry.pkt_type < 0x0ff:
                ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 8)
                ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)
        return ret_string

    @staticmethod
    def compare_bootp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, BootpPacketHeader)
            assert isinstance(actual, BootpPacketHeader)
            if (expected.is_field_set(expected.get_bootp_op_code()) and
                    BootpPacketConstants.BOOTP_OP_CODE not in ignore_list):
                name = "BOOTP op code : "
                if expected.get_bootp_op_code() != actual.get_bootp_op_code():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_op_code()) + " != " +
                                                      str(actual.get_bootp_op_code()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_op_code()) + " == " +
                                                 str(actual.get_bootp_op_code()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_hardware_type()) and
                    BootpPacketConstants.BOOTP_HARDWARE_TYPE not in ignore_list):
                name = "BOOTP hardware type : "
                if expected.get_bootp_hardware_type() != actual.get_bootp_hardware_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_hardware_type()) + " != " +
                                                      str(actual.get_bootp_hardware_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_hardware_type()) + " == " +
                                                 str(actual.get_bootp_hardware_type()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_hardward_address()) and
                    BootpPacketConstants.BOOTP_HARDWARD_ADDRESS not in ignore_list):
                name = "BOOTP hardward address : "
                if expected.get_bootp_hardward_address() != actual.get_bootp_hardward_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_hardward_address()) + " != " +
                                                      str(actual.get_bootp_hardward_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_hardward_address()) + " == " +
                                                 str(actual.get_bootp_hardward_address()) + " Pass")

            if expected.is_field_set(expected.get_bootp_hops()) and BootpPacketConstants.BOOTP_HOPS not in ignore_list:
                name = "BOOTP hops : "
                if expected.get_bootp_hops() != actual.get_bootp_hops():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_hops()) + " != " +
                                                      str(actual.get_bootp_hops()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_hops()) + " == " +
                                                 str(actual.get_bootp_hops()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_transaction_id()) and
                    BootpPacketConstants.BOOTP_TRANSACTION_ID not in ignore_list):
                name = "BOOTP transaction id : "
                if expected.get_bootp_transaction_id() != actual.get_bootp_transaction_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_transaction_id()) + " != " +
                                                      str(actual.get_bootp_transaction_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_transaction_id()) + " == " +
                                                 str(actual.get_bootp_transaction_id()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_seconds()) and
                    BootpPacketConstants.BOOTP_SECONDS not in ignore_list):
                name = "BOOTP seconds : "
                if expected.get_bootp_seconds() != actual.get_bootp_seconds():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_seconds()) + " != " +
                                                      str(actual.get_bootp_seconds()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_seconds()) + " == " +
                                                 str(actual.get_bootp_seconds()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_flags()) and
                    BootpPacketConstants.BOOTP_FLAGS not in ignore_list):
                name = "BOOTP flags : "
                if expected.get_bootp_flags() != actual.get_bootp_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_flags()) + " != " +
                                                      str(actual.get_bootp_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_flags()) + " == " +
                                                 str(actual.get_bootp_flags()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_client_ip_address()) and
                    BootpPacketConstants.BOOTP_CLIENT_IP_ADDRESS not in ignore_list):
                name = "BOOTP client ip address : "
                if expected.get_bootp_client_ip_address() != actual.get_bootp_client_ip_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_client_ip_address()) + " != " +
                                                      str(actual.get_bootp_client_ip_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_client_ip_address()) + " == " +
                                                 str(actual.get_bootp_client_ip_address()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_your_client_ip_address()) and
                    BootpPacketConstants.BOOTP_YOUR_CLIENT_IP_ADDRESS not in ignore_list):
                name = "BOOTP your client ip address : "
                if expected.get_bootp_your_client_ip_address() != actual.get_bootp_your_client_ip_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_your_client_ip_address()) + " != " +
                                                      str(actual.get_bootp_your_client_ip_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_your_client_ip_address()) + " == " +
                                                 str(actual.get_bootp_your_client_ip_address()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_next_server_ip_address()) and
                    BootpPacketConstants.BOOTP_NEXT_SERVER_IP_ADDRESS not in ignore_list):
                name = "BOOTP next server ip address : "
                if expected.get_bootp_next_server_ip_address() != actual.get_bootp_next_server_ip_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_next_server_ip_address()) + " != " +
                                                      str(actual.get_bootp_next_server_ip_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_next_server_ip_address()) + " == " +
                                                 str(actual.get_bootp_next_server_ip_address()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_relay_agent_ip_address()) and
                    BootpPacketConstants.BOOTP_RELAY_AGENT_IP_ADDRESS not in ignore_list):
                name = "BOOTP relay agent ip address : "
                if expected.get_bootp_relay_agent_ip_address() != actual.get_bootp_relay_agent_ip_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_relay_agent_ip_address()) + " != " +
                                                      str(actual.get_bootp_relay_agent_ip_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_relay_agent_ip_address()) + " == " +
                                                 str(actual.get_bootp_relay_agent_ip_address()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_client_mac_address()) and
                    BootpPacketConstants.BOOTP_CLIENT_MAC_ADDRESS not in ignore_list):
                name = "BOOTP client mac address : "
                if expected.get_bootp_client_mac_address() != actual.get_bootp_client_mac_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_client_mac_address()) + " != " +
                                                      str(actual.get_bootp_client_mac_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_client_mac_address()) + " == " +
                                                 str(actual.get_bootp_client_mac_address()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_server_host_name()) and
                    BootpPacketConstants.BOOTP_SERVER_HOST_NAME not in ignore_list):
                name = "BOOTP server host name : "
                if expected.get_bootp_server_host_name() != actual.get_bootp_server_host_name():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_server_host_name()) + " != " +
                                                      str(actual.get_bootp_server_host_name()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_server_host_name()) + " == " +
                                                 str(actual.get_bootp_server_host_name()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_boot_file_name()) and
                    BootpPacketConstants.BOOTP_BOOT_FILE_NAME not in ignore_list):
                name = "BOOTP boot file name : "
                if expected.get_bootp_boot_file_name() != actual.get_bootp_boot_file_name():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_boot_file_name()) + " != " +
                                                      str(actual.get_bootp_boot_file_name()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_boot_file_name()) + " == " +
                                                 str(actual.get_bootp_boot_file_name()) + " Pass")

            if (expected.is_field_set(expected.get_bootp_magic_cookie()) and
                    BootpPacketConstants.BOOTP_MAGIC_COOKIE not in ignore_list):
                name = "BOOTP magic cookie : "
                if expected.get_bootp_magic_cookie() != actual.get_bootp_magic_cookie():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bootp_magic_cookie()) + " != " +
                                                      str(actual.get_bootp_magic_cookie()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bootp_magic_cookie()) + " == " +
                                                 str(actual.get_bootp_magic_cookie()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with BootpPacketHeader")
        return results


class BootpPacketConstants:
    def __init__(self):
        pass

    BOOTP_OP_CODE = "BOOTP_OP_CODE"
    BOOTP_HARDWARE_TYPE = "BOOTP_HARDWARE_TYPE"
    BOOTP_HARDWARD_ADDRESS = "BOOTP_HARDWARD_ADDRESS"
    BOOTP_HOPS = "BOOTP_HOPS"
    BOOTP_TRANSACTION_ID = "BOOTP_TRANSACTION_ID"
    BOOTP_SECONDS = "BOOTP_SECONDS"
    BOOTP_FLAGS = "BOOTP_FLAGS"

    BOOTP_CLIENT_IP_ADDRESS = "BOOTP_CLIENT_IP_ADDRESS"
    BOOTP_YOUR_CLIENT_IP_ADDRESS = "BOOTP_YOUR_CLIENT_IP_ADDRESS"
    BOOTP_NEXT_SERVER_IP_ADDRESS = "BOOTP_NEXT_SERVER_IP_ADDRESS"
    BOOTP_RELAY_AGENT_IP_ADDRESS = "BOOTP_RELAY_AGENT_IP_ADDRESS"
    BOOTP_CLIENT_MAC_ADDRESS = "BOOTP_CLIENT_MAC_ADDRESS"
    BOOTP_SERVER_HOST_NAME = "BOOTP_SERVER_HOST_NAME"
    BOOTP_BOOT_FILE_NAME = "BOOTP_BOOT_FILE_NAME"

    BOOTP_MAGIC_COOKIE = "BOOTP_MAGIC_COOKIE"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
###########################################################################
# ###   end BootpPacketHeader
###########################################################################


class BootpOptions(object):
    def __init__(self, pkt_type, length, data):
        self.pkt_type = pkt_type
        # self.type_string = self.get_type_string(type)
        self.length = length
        self.data = data

    # def get_type_string(self, pkt_type):
    #     if pkt_type == 0x01:
    #         return "Area Address(es)"
    #     else:
    #         return "Unknown Type"

    @staticmethod
    def process_options(payload, tlv_entries, pdu_length, hanlder):
        if not isinstance(pdu_length, int):
            pdu_length = int(pdu_length, 16)
        try:
            while pdu_length > 0 and payload.replace("0", "").strip() != "":
                tlv_type = hanlder.get_bits_from_string(8, payload)
                tlv_type = int(tlv_type, 16)
                payload = hanlder.remove_bits_from_string(8, payload)
                if tlv_type < 0x0ff:
                    pdu_length -= 1
                    tlv_length = hanlder.get_bits_from_string(8, payload)
                    tlv_length = int(tlv_length, 16)
                    payload = hanlder.remove_bits_from_string(8, payload)
                    pdu_length -= 1
                    tlv_data = hanlder.get_bits_from_string(tlv_length * 8, payload)
                    payload = hanlder.remove_bits_from_string(tlv_length * 8, payload)
                    pdu_length -= tlv_length
                tlv_entries.append(BootpOptions(tlv_type, tlv_length, tlv_data))
        except Exception as e:
            PacketObject.logger.log_info(e)
        return payload

    @staticmethod
    def to_packet_string(packet):
        table_tlv = TableFormatter()
        for entry in packet.bootp_options:
            # table_tlv.add_row_value("type",  entry.type_string + " " + packet.format_int(entry.type, 1))
            table_tlv.add_row_value("type", packet.format_int(entry.type, 1))
            if entry.type < 0x0ff:
                table_tlv.add_row_value("length", packet.format_int(entry.length, 1))
                table_tlv.add_row_value("data", entry.data)
            else:
                table_tlv.add_row_value("length", "")
                table_tlv.add_row_value("data", "")
        return table_tlv
