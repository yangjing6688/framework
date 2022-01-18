from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: packet_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class PacketStatsApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(PacketStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_stats
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[PacketStatsConstants.CHUNK_SIZE_CMD] = "dummyValue1" # static value
        dummyDict[PacketStatsConstants.DIRNAME_CMD] = "dummyValue2" # static value
        dummyDict[PacketStatsConstants.ENABLE_ETHERNET_TYPE_CMD] = "dummyValue3" # static value
        dummyDict[PacketStatsConstants.ENABLE_FRAMESIZE_CMD] = "dummyValue4" # static value
        dummyDict[PacketStatsConstants.ENABLE_PATTERN_CMD] = "dummyValue5" # static value
        dummyDict[PacketStatsConstants.ETHERNET_TYPE_CMD] = "dummyValue6" # static value
        dummyDict[PacketStatsConstants.FILENAME_CMD] = "dummyValue7" # static value
        dummyDict[PacketStatsConstants.FORMAT_CMD] = PacketStatsConstants.FORMAT_VAR # constant value
        dummyDict[PacketStatsConstants.FRAME_ID_END_CMD] = "dummyValue9" # static value
        dummyDict[PacketStatsConstants.FRAME_ID_START_CMD] = "dummyValue10" # static value
        dummyDict[PacketStatsConstants.FRAMESIZE_CMD] = "dummyValue11" # static value
        dummyDict[PacketStatsConstants.PACKET_TYPE_CMD] = PacketStatsConstants.PACKET_TYPE_DATA # constant value
        dummyDict[PacketStatsConstants.PATTERN_CMD] = "dummyValue13" # static value
        dummyDict[PacketStatsConstants.PATTERN_OFFSET_CMD] = "dummyValue14" # static value
        dummyDict[PacketStatsConstants.PORT_HANDLE_CMD] = "dummyValue15" # static value
        dummyDict[PacketStatsConstants.STOP_CMD] = "dummyValue16" # static value

        api = device.getApi(PacketStatsConstants.PACKET_STATS_API)
        api.packet_stats(dummyDict)
    """
    def packet_stats(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::packet_stats", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_stats_chunk_size(self, size):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_dirname(self, path):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_enable_ethernet_type(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_enable_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_enable_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_ethernet_type(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_filename(self, file):
        """
        This is the method the command: packet_stats option filename
        Description:Supported with IxTclHal. Used in-conjunction with the format parameter. Specifies the name to save the captured packets.(DEFAULT = ixia-datetime-port_handle.format). Example: ixia-2305062301-104.enc. Dependencies: Mandatory, when format is specified as cap/enc/txt???.
        Constants Available: FILENAME_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        file --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.FILENAME_CMD : file})

    def packet_stats_format(self, type):
        """
        This is the method the command: packet_stats option format
        Description:Specifies how the data is returned.
            Valid options are:
            txt: IxTclHal: Returns the data in a text (.txt) file specified by parameter -filename. Aggregate stats keys are also returned. Example: Frames 1 to 2 of 2 Frame,Time Stamp,DA,SA,Type/Length,Data,Frame Length,Status 1 00:00:24.474262360 00 00 DE BB 00 02 00 DE 01 07 03 00 08 00 45 00 00 2C 00 00 00 00 40 FF 5E D0 0C 01 01 01 0D 01 01 01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 00 48 F0 61 42 5B 3D FF EA 62 Bad Packet 0x0002 2 00:00:24.474305640 00 00 DE BB 00 02 00 DE 01 07 03 00 08 00 45 00 00 2D 00 00 00 00 40 FF 5E CF 0C 01 01 01 0D 01 01 01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 00 00 48 F0 69 B6 18 71 D4 B2 63 Bad Packet 0x0002 IxTclNetwork: The text file format is not supported. Aggregate stats keys are returned.
            cap: IxTclHal (default): Returns the data in a .cap file specified by parameter -filename. Aggregate stats keys are also returned. IxTclNetwork (default): Returns the data in .cap files (for both data and control captured packets) in the folder specified by the -dirname parameter. Aggregate stats keys are also returned.
            enc: IxTclHal: Returns the data in binary format for use with NAI's Sniffer program. The file is specified by parameter -filename. Aggregate stats keys are also returned. IxTclNetwork: The enc format is not supported. Aggregate stats keys are returned.
            none: IxTclHal: Do not export capture buffer. Aggregate stats keys are returned. IxTclNetwork: Do not export capture buffer. Aggregate stats keys are returned.
            var: IxTclHal: Returns a keyed list (aggregate and frame stats). Can be used only if the capture buffer contains a number of frames less or equal than 20 frames. If the capture buffer contains more than 20 frames, the first 20 frames from the capture are returned and a warning will be displayed. IxTclNetwork: Returns a keyed list (aggregate and frame stats). Returns the frames that are between frame_id_start and frame_id_end. If the frame_id_start and frame_id_end are not given only the first 20 frames will be returned.
            csv: IxTclHal: Not supported, an error will be returned. IxTclNetwork: A csv file will be returned with the captured frames in the folder specified by the -dirname parameter. The keys data_file and control_file will be returned. These keys contain the names of the files csv files created. Output example: Field Id,Field Display Name,Field Value Packet 0 Display Stack Name: Frame::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Frame is marked$0"",Frame is marked,False ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Arrival Time$1"",Arrival Time,""Feb 28, 2013 14:41:10.817357000"" ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Time delta from previous packet$2"",Time delta from previous packet,0.000000000 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Time since reference or first frame$3"",Time since reference or first frame,0.000000000 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Frame Number$4"",Frame Number,1 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Frame length on the wire$5"",Frame length on the wire,38 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Frame length stored into the capture file$6"",Frame length stored into the capture file,38 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Frame$0""/field:""root$0/Frame$0/Protocols in frame$7"",Protocols in frame,eth:ip:data Display Stack Name: Ethernet ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Ethernet$1""/field:""root$0/Ethernet$1/Destination$0"",Destination,00:00:00:00:00:00 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Ethernet$1""/field:""root$0/Ethernet$1/Source$1"",Source,00:00:00:00:00:00 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Ethernet$1""/field:""root$0/Ethernet$1/Source or Destination Address$2"",Source or Destination Address,00:00:00:00:00:00 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Ethernet$1""/field:""root$0/Ethernet$1/Source or Destination Address$3"",Source or Destination Address,00:00:00:00:00:00 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Ethernet$1""/field:""root$0/Ethernet$1/Type$4"",Type,2048 ::ixNet::OBJ-/vport:2/capture/currentPacket/stack:""Ethernet$1""/field:""root$0/Ethernet$1/Trailer$5"",Trailer,1EB741F2
        Constants Available: FORMAT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        type --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.FORMAT_CMD : type})

    def packet_stats_frame_id_end(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_frame_id_start(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_framesize(self, size):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_packet_type(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_pattern(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_pattern_offset(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_port_handle(self, port):
        """
        This is the method the command: packet_stats option port_handle
        Description:Supported with IxTclHal and IxTclNetwork. Associate the command performed by action to the port handle listed
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.PORT_HANDLE_CMD : port})

    def packet_stats_stop(self, opt):
        """
        This is the method the command: packet_stats option stop
        Description:Supported with IxTclHal and IxTclNetwork. Stop capture when collecting statistics and downloading capture buffer.
        Constants Available: STOP_CMD
        Supported:IxNetwork [M] , IxOS/IxNetwork-FT [M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.STOP_CMD : opt})


"""
    This is the Constants class for the command: packet_stats
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class PacketStatsConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    PACKET_STATS_API = "PACKET_STATS_API"

    ACTION_CMD = "action"
    ACTION_FILTERED = "filtered"

    CHUNK_SIZE_CMD = "chunk_size"

    DIRNAME_CMD = "dirname"

    ENABLE_ETHERNET_TYPE_CMD = "enable_ethernet_type"

    ENABLE_FRAMESIZE_CMD = "enable_framesize"

    ENABLE_PATTERN_CMD = "enable_pattern"

    ETHERNET_TYPE_CMD = "ethernet_type"

    FILENAME_CMD = "filename"

    FORMAT_CMD = "format"
    # Constant values for FORMAT_CMD
    FORMAT_VAR = "var"
    FORMAT_ENC = "enc"
    FORMAT_TXT = "txt"
    FORMAT_CAP = "cap"
    FORMAT_CSV = "csv"
    FORMAT_PCAP = "pcap"
    FORMAT_NONE = "none"

    FRAME_ID_END_CMD = "frame_id_end"

    FRAME_ID_START_CMD = "frame_id_start"

    FRAMESIZE_CMD = "framesize"

    PACKET_TYPE_CMD = "packet_type"
    # Constant values for PACKET_TYPE_CMD
    PACKET_TYPE_DATA = "data"
    PACKET_TYPE_CONTROL = "control"
    PACKET_TYPE_BOTH = "both"

    PATTERN_CMD = "pattern"

    PATTERN_OFFSET_CMD = "pattern_offset"

    PORT_HANDLE_CMD = "port_handle"

    STOP_CMD = "stop"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -chunk_size
    -dirname
    -enable_ethernet_type
    -enable_framesize
    -enable_pattern
    -ethernet_type
    -filename
    -format
    -frame_id_end
    -frame_id_start
    -framesize
    -packet_type
    -pattern
    -pattern_offset
    -port_handle
    -stop
If you want to update this file, look in the CSV
"""
