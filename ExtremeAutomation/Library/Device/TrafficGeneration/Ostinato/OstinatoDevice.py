import socket
import binascii
# import ostinato  # pip install python-ostinato
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb, DroneProxy
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.protocol_pb2 import \
    StreamControl, StreamCore, PortIdList, StreamIdList, Stream
from ExtremeAutomation.Library.Device.Common.Agents.IxiaConnectionTelnetAgent import IxiaConnectionTelnetAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceCaptureHelper import \
    OstinatoDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceStatisticHelper import \
    OstinatoDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceTrafficHelper import \
    OstinatoDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoArpHelper import OstinatoArpHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDevice import TrafficGeneratingDevice
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Utils.Time import current_milli_time
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Apis.OstinatoStreamConfigApi import \
    OstinatoStreamConfigConstants
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
# from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump

"""
Ostinato install

apt-get install Xvfb
apt-get install ostinato
pip install python-ostinato
sudo apt-get install python-pip

xvfb-run drone &

this needs to be version .6 or better.
apt-cache policy ostinato

create and add:
/etc/apt/sources.list.d/ostinato.list
deb http://download.opensuse.org/repositories/home:/pstavirs:/ostinato/xUbuntu_14.04/ /
deb http://download.opensuse.org/repositories/home:/pstavirs:/branches:/home:/pstavirs:/ostinato/xUbuntu_17.04/ /


wget http://download.opensuse.org/repositories/home:pstavirs:ostinato/xUbuntu_14.04/Release.key
wget http://download.opensuse.org/repositories/home:/pstavirs:/branches:/home:/pstavirs:/ostinato/xUbuntu_17.04/
                                                                                                        Release.key
sudo apt-key add - < Release.key

sudo apt-get update

sudo apt-get upgrade ostinato

if that doesn't work, check the ostinato.list again and run
sudo apt-get dist-upgrade
sudo apt-get clean
sudo apt-get autoclean
sudo apt-get purge

# starting the ostinato drone proxy
sudo drone &

"""


class OstinatoDevice(TrafficGeneratingDevice, OstinatoDeviceCaptureHelper, OstinatoDeviceStatisticHelper,
                     OstinatoDeviceTrafficHelper, OstinatoArpHelper):
    tgen_debug = True

    def __init__(self):
        super(OstinatoDevice, self).__init__()
        # ostinato.__log__.setLevel(logging.ERROR)
        OstinatoDeviceCaptureHelper.__init__(self, self)
        OstinatoDeviceStatisticHelper.__init__(self, self)
        OstinatoDeviceTrafficHelper.__init__(self, self)
        self.drone = None
        self.capture_buffer = OstinatoCaptureBuffer(self)

    def connect(self, host, port=7878):
        if self.connection is None:
            self.set_host_name(host)
            host_name = host  # self.get_host_name() # '10.52.153.101'
            self.connection = DroneProxy(host_name, int(port))  # port_number

        try:
            self.connection.connect()
            self.init_connection()
        except socket.error:
            self.initialized = False

    def init_connection(self):
        if self.initialized:
            return
        self.initialized = True

    def disconnect(self):
        if self.connection is None:
            self.initialized = False
            return
        else:
            try:
                self.connection.disconnect()
            except:
                pass
            self.connection = None
            self.initialized = False

    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        # return self.logger.log_unimplemented_method()
        pass

    def set_host_name(self, hostname):
        self.hostname = hostname

    def set_port(self, port):
        self.port = port

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def get_port_duplex(self, port_string):
        return self.logger.log_unimplemented_method()

    def set_port_duplex(self, port_string, duplex, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_speed(self, port_string):
        return self.logger.log_unimplemented_method()

    def set_port_speed(self, port_string, speed, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def set_port_autonegotiation(self, port_string, bool, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def has_link(self, port_string):
        """
        LinkStateUnknown = 0;
        LinkStateDown = 1;
        LinkStateUp = 2;
        """
        try:
            # assert isinstance(self.connection, DroneProxy)
            port_string = self.ostinato_port_number_to_port(port_string)
            reply = self.connection.getStats(port_string)
            return reply.port_stats[0].state.link_state == 2
        except:
            return False

    def reset_port(self, host, port_string):
        return self.logger.log_unimplemented_method()

    def __get_stream_cfg_class(self, port_string, stream_id):
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        if isinstance(stream_id, StreamIdList):
            sids.stream_id.add().id = stream_id.stream_id[0].id
        else:
            sids.stream_id.add().id = stream_id
        scfgs = drone.getStreamConfig(sids)
        return scfgs
        # stream = scfgs.stream[0]
        #
        # streams = drone.getStreamIdList(port_string.port_id[0])
        # stream_cfg = None
        # for stream in streams.stream_id:
        #     if stream.id == stream_id:
        #         stream_cfg = drone.getStreamConfig(streams)
        #         break
        # return stream_cfg

    def __get_stream_class(self, port_string, stream_id):
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        if isinstance(stream_id, StreamIdList):
            sids.stream_id.add().id = stream_id.stream_id[0].id
        else:
            sids.stream_id.add().id = stream_id
        scfgs = drone.getStreamConfig(sids)
        stream = scfgs.stream[0]
        return stream

    # internal
    def __get_protocol_class(self, port_string, stream_id, extention_id):
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        sids.stream_id.add().id = stream_id
        scfgs = drone.getStreamConfig(sids)
        stream = scfgs.stream[0]
        for protocol in stream.protocol:
            if protocol.protocol_id.id == extention_id:
                p = protocol
                break
        return p

# port_stats {
#   port_id {
#     id: 1
#   }
#   state {
#     link_state: LinkStateUp
#     is_transmit_on: false
#     is_capture_on: true
#   }
#   rx_pkts: 241
#   rx_bytes: 31571
#   rx_pps: 0
#   rx_bps: 0
#   tx_pkts: 0
#   tx_bytes: 0
#   tx_pps: 0
#   tx_bps: 0
#   rx_drops: 0
#   rx_errors: 0
#   rx_fifo_errors: 0
#   rx_frame_errors: 0
# }

    def is_port_transmitting(self, port_string):
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        reply = self.connection.getStats(port_string)
        return reply.port_stats[0].state.is_transmit_on

    def is_port_capturing(self, port_string):
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        reply = self.connection.getStats(port_string)
        return reply.port_stats[0].state.is_capture_on

    def start_traffic(self, port_string, options=None):
        self.logger.log_debug("start_traffic(" + port_string + ")")
        if options is None:
            options = {}
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        self.connection.startTransmit(port_string)

    def stop_traffic(self, port_string, options=None):
        self.logger.log_debug("stop_traffic(" + port_string + ")")
        if options is None:
            options = {}
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        self.connection.stopTransmit(port_string)

    def start_capture(self, port_string, options=None):
        self.logger.log_debug("start_capture(" + port_string + ")")
        self.capture_buffer.start_capture_buffer(port_string)
        if options is None:
            options = {}
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        self.connection.startCapture(port_string)
        # print("REMOVE AFTER DEBUG")
        # print(self.is_port_transmitting(port_string))

    def stop_capture(self, port_string, options=None):
        self.logger.log_debug("stop_capture(" + port_string + ")")
        if options is None:
            options = {}
        # assert isinstance(self.connection, DroneProxy)
        org_ps = port_string
        port_string = self.ostinato_port_number_to_port(port_string)
        # print("REMOVE AFTER DEBUG")
        # print(self.is_port_transmitting(port_string))
        self.connection.stopCapture(port_string)
        self.capture_buffer.stop_capture_buffer(org_ps)

    def clear_capture_buffer(self, port_string, options=None):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        if options is None:
            options = {}
        self.clear_statistics(port_string)
        self.capture_buffer.clear_capture_buffer(port_string)

    def set_capture_mode(self, port_string, mode, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture(self, port_handle, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame(self, port_handle, frame_num, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_statistic(self, port_handle, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic(self, port_handle, stream_id, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def clear_statistics(self, port_string, options=None):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        if options is None:
            options = {}
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        drone.clearStats(port_string)

    def set_stream_transmit_mode(self, port_string, stream_id, mode):
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        stream = stream_cfg.stream[0]
        assert isinstance(stream, Stream)
        control = stream.control
        assert isinstance(control, StreamControl)
        if mode == OstinatoStreamConfigConstants.DMA_MODE_ADVANCE:
            control.next = ost_pb.StreamControl.e_nw_goto_next
        elif mode == OstinatoStreamConfigConstants.DMA_MODE_STOPSTREAM:
            control.next = ost_pb.StreamControl.e_nw_stop
        elif mode == OstinatoStreamConfigConstants.DMA_MODE_GOTOFIRST:
            control.next = ost_pb.StreamControl.e_nw_goto_id
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        drone.modifyStream(stream_cfg)

    def get_stream_transmit_action(self, port_string, stream_id):
        #
        # port_string = self.ostinato_port_number_to_port(port_string)
        # streams = drone.getStreamIdList(port_string.port_id[0])
        # stream = streams.stream_id[stream_num-1]
        # return self.get_stream_from_stream_id(port_string, stream.id)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        try:
            stream = stream_cfg.stream[0]
        except:
            # something is up with the get... try again.
            drone = self.connection
            # assert isinstance(drone, DroneProxy)
            original_port = port_string
            port_string = self.ostinato_port_number_to_port(port_string)
            streams = drone.getStreamIdList(port_string.port_id[0])
            stream = streams.stream_id[stream_id -1]
            stream_cfg = self.__get_stream_cfg_class(port_string, stream.id)
            stream = stream_cfg.stream[0]
        assert isinstance(stream, Stream)
        control = stream.control
        assert isinstance(control, StreamControl)
        return control.next

    def get_stream_transmit_action_string(self, port_string, stream_id):
        val = self.get_stream_transmit_action(port_string, stream_id)
        if val == ost_pb.StreamControl.e_nw_goto_next:
            return "Next/Advance"
        elif val == ost_pb.StreamControl.e_nw_stop:
            return "Stop Stream"
        elif val == ost_pb.StreamControl.e_nw_goto_id:
            return "Goto First"
        else:
            return "Unknown (" + str(val) + ")"

    def get_stream_transmit_mode(self, port_string, stream_id):
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        try:
            stream = stream_cfg.stream[0]
        except:
            # something is up with the get... try again.
            drone = self.connection
            # assert isinstance(drone, DroneProxy)
            original_port = port_string
            port_string = self.ostinato_port_number_to_port(port_string)
            streams = drone.getStreamIdList(port_string.port_id[0])
            stream = streams.stream_id[stream_id - 1]
            stream_cfg = self.__get_stream_cfg_class(port_string, stream.id)
            stream = stream_cfg.stream[0]
        assert isinstance(stream, Stream)
        control = stream.control
        assert isinstance(control, StreamControl)
        return control.mode
        # stream_control.mode = s.control.e_sm_continuous
        # stream_control.unit = s.control.e_su_bursts

    def get_stream_transmit_mode_string(self, port_string, stream_id):
        val = self.get_stream_transmit_mode(port_string, stream_id)
        if val == ost_pb.StreamControl.e_sm_continuous:
            return "Continuous"
        elif val == ost_pb.StreamControl.e_sm_fixed:
            return "Fixed"
        else:
            return "Unknown (" + str(val) + ")"

    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        if options is None:
            options = {}
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        stream_num = stream_id
        opt_dict = options
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        sids.stream_id.add().id = stream_num
        if clear_all_streams:
            if clear_all_streams != "Nothing":
                self.clear_all_streams(port_string)
        else:
            drone.deleteStream(sids)

        if TrafficConfigConstants.MODE_CMD not in options:
            drone.addStream(sids)
        elif options[TrafficConfigConstants.MODE_CMD] == TrafficConfigConstants.MODE_CREATE:
            drone.addStream(sids)
        elif options[TrafficConfigConstants.MODE_CMD] == TrafficConfigConstants.MODE_MODIFY:
            pass  # drone.addStream(sids)
        else:
            drone.addStream(sids)

        sids = drone.getStreamIdList(port_string.port_id[0])
        sids.stream_id.sort(key=lambda b: b.id)

        stream_cfg = drone.getStreamConfig(sids)
        stream_cfg.port_id.CopyFrom(port_string.port_id[0])
        stream_cfg.stream.sort(key=lambda b: b.stream_id.id)

        if TrafficConfigConstants.MODE_CMD not in options:
            s = stream_cfg.stream.add()
            s.stream_id.id = sids.stream_id[-1].id
            s.core.ordinal = s.stream_id.id
        elif options[TrafficConfigConstants.MODE_CMD] == TrafficConfigConstants.MODE_CREATE:
            s = stream_cfg.stream.add()
            s.stream_id.id = sids.stream_id[-1].id
            s.core.ordinal = s.stream_id.id
        elif options[TrafficConfigConstants.MODE_CMD] == TrafficConfigConstants.MODE_MODIFY:
            for s in stream_cfg.stream:
                if s.stream_id.id == stream_num:
                    break
        else:
            s = stream_cfg.stream.add()
            s.stream_id.id = sids.stream_id[-1].id
            s.core.ordinal = s.stream_id.id

        s.core.is_enabled = True
        self.logger.log_debug(s)
        packet.config_thirdparty_traffic_generator_stream(EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO, drone,
                                                          port_string, s, options=opt_dict)
        if packet.is_field_set(packet.get_payload()):
            p = s.protocol.add()
            p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
            payloadData = packet.get_payload().replace(" ", "")
            payloadData = binascii.a2b_hex(payloadData)
            p.Extensions[hexDump].content = payloadData
        stream_control = s.control
        assert isinstance(stream_control, StreamControl)
        stream_core = s.core
        assert isinstance(stream_core, StreamCore)
        new_mode = None
        if TrafficConfigConstants.TRANSMIT_MODE_CMD in opt_dict:
            # opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST
            # s.control.mode
            # e_nw_goto_id = {int} 2
            # e_nw_goto_next = {int} 1
            # e_nw_stop = {int} 0
            # next = {int} 1

            # mode = {int} 0
            # e_sm_continuous = {int} 1
            # e_sm_print(= {int} 0)
            self.logger.log_debug("setting " + TrafficConfigConstants.TRANSMIT_MODE_CMD + " to " +
                                  str(opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD]))

            if TrafficConfigConstants.TRANSMIT_MODE_CMD in options:
                mode = options[TrafficConfigConstants.TRANSMIT_MODE_CMD]
                if mode == TrafficConfigConstants.TRANSMIT_MODE_NEXT or \
                        mode == TrafficConfigConstants.TRANSMIT_MODE_END or \
                        mode == TrafficConfigConstants.TRANSMIT_MODE_RETURN_TO_ID:
                    new_mode = mode
                    options[TrafficConfigConstants.TRANSMIT_MODE_CMD] = \
                        TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST

            port_id_list = drone.getPortIdList()
            port_config_list = drone.getPortConfig(port_id_list)
            if opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] == \
                    TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST:
                for port in port_config_list.port:
                    if port.port_id == port_string.port_id[0]:
                        port.transmit_mode = ost_pb.kInterleavedTransmit
                stream_control.mode = s.control.e_sm_continuous
                stream_control.unit = s.control.e_su_bursts
            elif opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] == \
                    TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS:
                for port in port_config_list.port:
                    if port.port_id == port_string.port_id[0]:
                        port.transmit_mode = ost_pb.kInterleavedTransmit
                stream_control.mode = s.control.e_sm_continuous
                stream_control.unit = s.control.e_su_packets
            elif opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] == \
                    TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST:
                for port in port_config_list.port:
                    if port.port_id == port_string.port_id[0]:
                        port.transmit_mode = ost_pb.kSequentialTransmit
                stream_control.mode = s.control.e_sm_fixed
                stream_control.unit = s.control.e_su_packets
            else:
                for port in port_config_list.port:
                    if port.port_id == port_string.port_id[0]:
                        port.transmit_mode = ost_pb.kSequentialTransmit
                stream_control.mode = s.control.e_sm_fixed
                stream_control.unit = s.control.e_su_packets
            drone.modifyPort(port_config_list)

        if TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD in opt_dict:
            self.logger.log_debug("setting " + TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD + " to " +
                                  str(opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD]))
            stream_control.num_packets = NumberUtils.to_integer_value(
                opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD])

        # s.core.ordinal = 0x2
        if TrafficConfigConstants.FRAME_SIZE_CMD in opt_dict:
            stream_core.frame_len = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD])
            self.logger.log_debug("setting " + TrafficConfigConstants.FRAME_SIZE_CMD + " to " +
                                  str(opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD]))
        elif packet and packet.get_length() > 64:
            stream_core.frame_len = NumberUtils.to_integer_value(packet.get_length())
            self.logger.log_debug("setting " + TrafficConfigConstants.FRAME_SIZE_CMD + " to " +
                                  str(packet.get_length()))

        if TrafficConfigConstants.NUMBER_OF_PACKETS_TX_CMD in opt_dict:
            stream_control.num_packets = NumberUtils.to_integer_value(
                opt_dict[TrafficConfigConstants.NUMBER_OF_PACKETS_TX_CMD])
        elif TrafficConfigConstants.RATE_PPS_CMD in opt_dict:
            stream_control.packets_per_sec = NumberUtils.to_integer_value(
                opt_dict[TrafficConfigConstants.RATE_PPS_CMD])
            self.logger.log_debug("setting rate pps to " +
                                  str(opt_dict[TrafficConfigConstants.RATE_PPS_CMD]))
            if TrafficConfigConstants.PKTS_PER_BURST_CMD in opt_dict:
                stream_control.num_packets = NumberUtils.to_integer_value(
                    opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD])
                self.logger.log_debug("setting number of packets to " +
                                      str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            else:
                stream_control.num_packets = NumberUtils.to_integer_value(
                    opt_dict[TrafficConfigConstants.RATE_PPS_CMD])
                self.logger.log_debug("setting number of packets to " +
                                      str(opt_dict[TrafficConfigConstants.RATE_PPS_CMD]))
        elif TrafficConfigConstants.PKTS_PER_BURST_CMD in opt_dict:
            # print("OSTINATO")
            # print( NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.RATE_PPS_CMD]))
            # print(NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            stream_control.packets_per_burst = NumberUtils.to_integer_value(
                opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD])
            self.logger.log_debug("setting " + TrafficConfigConstants.PKTS_PER_BURST_CMD + " to " +
                                  str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            stream_control.num_packets = NumberUtils.to_integer_value(
                opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD])
            self.logger.log_debug("setting number of packets to " +
                                  str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            # e_nw_goto_id = {int} 2
            # e_nw_goto_next = {int} 1
            # e_nw_stop = {int} 0
            # e_sm_continuous = {int} 1
            # e_sm_fixed = {int} 0
            # e_su_bursts = {int} 1
            # e_su_packets = {int} 0
            self.logger.log_debug("setting " + TrafficConfigConstants.PKTS_PER_BURST_CMD + " to " +
                                  str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
        if TrafficConfigConstants.NAME_CMD in opt_dict:
            s.core.name = opt_dict[TrafficConfigConstants.NAME_CMD]
        else:
            s.core.name = packet.get_name()

    # opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 100
    # opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = \
    #     TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST # constant value

    # num_bursts = {int} 1
    # num_packets = {int} 1
    # packets_per_burst = {int} 10
    # packets_per_sec = {int} 1

    # e_su_bursts = {int} 1
    # e_su_packets = {int} 0
    # unit = {int} 0

        drone.modifyStream(stream_cfg)

        if new_mode:
            if new_mode == TrafficConfigConstants.TRANSMIT_MODE_NEXT:
                self.set_stream_transmit_mode(port_string, stream_id, OstinatoStreamConfigConstants.DMA_MODE_ADVANCE)
            elif new_mode == TrafficConfigConstants.TRANSMIT_MODE_END:
                self.set_stream_transmit_mode(port_string, stream_id, OstinatoStreamConfigConstants.DMA_MODE_STOPSTREAM)
            elif new_mode == TrafficConfigConstants.TRANSMIT_MODE_RETURN_TO_ID:
                self.set_stream_transmit_mode(port_string, stream_id, OstinatoStreamConfigConstants.DMA_MODE_GOTOFIRST)

        if packet.is_field_set(packet.get_source_mac_mode()):
            self.configure_stream_mac_src_options(port_string, stream_num,
                                                        packet.get_source_mac(),
                                                        packet.get_source_mac_mode(),
                                                        packet.get_source_mac_count(),
                                                        packet.get_source_mac_mask(),
                                                        packet.get_source_mac_seed())

        if packet.is_field_set(packet.get_destination_mac_mode()):
            self.configure_stream_mac_dst_options(port_string, stream_num,
                                                        packet.get_destination_mac(),
                                                        packet.get_destination_mac_mode(),
                                                        packet.get_destination_mac_count(),
                                                        packet.get_destination_mac_mask(),
                                                        packet.get_destination_mac_seed())
        if isinstance(packet, IpV4PacketHeader):
            if packet.is_field_set(packet.get_source_ip_mode()):
                self.configure_stream_ip_src_options(port_string, stream_num,
                                                        packet.get_source_ip(),
                                                        packet.get_source_ip_mode(),
                                                        packet.get_source_ip_count(),
                                                        packet.get_source_ip_mask())

            if packet.is_field_set(packet.get_destination_ip_mode()):
                self.configure_stream_ip_dst_options(port_string, stream_num,
                                                        packet.get_destination_ip(),
                                                        packet.get_destination_ip_mode(),
                                                        packet.get_destination_ip_count(),
                                                        packet.get_destination_ip_mask())

        if isinstance(packet, IpV6PacketHeader):
            if packet.is_field_set(packet.get_ipv6_source_address_mode()):
                self.configure_stream_ipv6_src_options(port_string, stream_num,
                                                        packet.get_ipv6_source_address(),
                                                        packet.get_ipv6_source_address_mode(),
                                                        packet.get_ipv6_source_address_count(),
                                                        packet.get_ipv6_source_address_mask())

            if packet.is_field_set(packet.get_ipv6_destination_address_mode()):
                self.configure_stream_ipv6_dst_options(port_string, stream_num,
                                                        packet.get_ipv6_destination_address(),
                                                        packet.get_ipv6_destination_address_mode(),
                                                        packet.get_ipv6_destination_address_count(),
                                                        packet.get_ipv6_destination_address_mask())

    def clear_stream(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        drone.deleteStream(stream_id)

    def clear_all_streams(self, port_string, options=None):
        if options is None:
            options = {}
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        try:
            sid_list = drone.getStreamIdList(port_string.port_id[0])
            drone.deleteStream(sid_list)

            # change port back to non-continuous
            # https://groups.google.com/forum/#!searchin/ostinato/
            #   https$3A$2F$2Fgithub.com$2Fpstavirs$2Fostinato$2Fissues$2F179%7Csort:relevance/ostinato/
            #   _2iROawPVGk/Rg_1uYIqCQAJ
            port_id_list = drone.getPortIdList()
            port_config_list = drone.getPortConfig(port_id_list)
            for port in port_config_list.port:
                if port.port_id == port_string.port_id[0]:
                    port.transmit_mode = ost_pb.kSequentialTransmit
                    break
            drone.modifyPort(port_config_list)

            # https://github.com/pstavirs/ostinato/issues/179
            stream_cfg = ost_pb.StreamConfigList()
            stream_cfg.port_id.id = port_string.port_id[0].id
            drone.modifyStream(stream_cfg)
        except:
            print(str(port_string) + " isn't a valid port")

    def stream_exists(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream(self, port_string, stream_num):
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        original_port = port_string
        port_string = self.ostinato_port_number_to_port(port_string)
        streams = drone.getStreamIdList(port_string.port_id[0])
        stream = streams.stream_id[stream_num - 1]
        return self.get_stream_from_stream_id(port_string, stream.id)

    def set_stream_enabled(self,port_string, stream_id, enable):
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        stream = stream_cfg.stream[0]
        stream.core.is_enabled = enable
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        drone.modifyStream(stream_cfg)

    def get_stream_from_stream_id(self, port_string, stream_id):
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        original_port = port_string
        port_string = self.ostinato_port_number_to_port(port_string)
        streams = drone.getStreamIdList(port_string.port_id[0])
        for stream in streams.stream_id:
            if stream.id == stream_id:
                stream_cfgs = drone.getStreamConfig(streams)
                ret_string = ""
                ret_string += "port=" + str(original_port) + " " + str(port_string) + ";"
                ret_string += "ID=" + str(stream_id) + ";"
                ret_string += "name=" + str(stream) + ";"
                for stream_cfg in stream_cfgs.stream:
                    if stream_cfg.stream_id.id == stream_id:
                        ret_string += "" + str(stream_cfg).replace("\n", " ").replace("\r", " ").replace("  ", " ")
                        # needs to get port state and stream cont/etc...
                        ret_string += self.is_stream_continuous(original_port, stream_id, True)
                        return ret_string.replace("\n", " ").replace("\r", " ").replace("  ", " ")

    def get_port_transmit_mode(self, port_string):
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        original_port = port_string
        port_string = self.ostinato_port_number_to_port(port_string)
        port_id_list = drone.getPortIdList()
        port_config_list = drone.getPortConfig(port_id_list)
        for port in port_config_list.port:
            if port.port_id == port_string.port_id[0]:
                return port.transmit_mode

    def get_port_transmit_mode_string(self, port_string):
        val = self.get_port_transmit_mode(port_string)
        if val == ost_pb.kInterleavedTransmit:
            return "Interleaved"
        elif val == ost_pb.kSequentialTransmit:
            return "Sequential"
        else:
            return "Unknown (" + str(val) + ")"

    def get_all_stream(self, port_string):
        count = self.get_stream_count(port_string)
        index = 1
        streams = []
        while int(index) <= int(count):
            streams.append(self.get_stream(port_string, index))
            index += 1
        return streams

    def get_stream_count(self, port_string, options=None):
        if options is None:
            options = {}
        drone = self.connection
        # assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sid_list = drone.getStreamIdList(port_string.port_id[0])
        return len(sid_list.stream_id)

    def clear_statistics_and_filters(self, port_string, options=None):
        if options is None:
            options = {}
        self.clear_statistics(port_string, options)
        self.capture_buffer.clear_capture_buffer(port_string)
        # ostinato doesn't have filters or triggers
        # self.clear_capture_filters_and_triggers(port_string)

    def ostinato_port_number_to_port(self, port_number):
        og_port_number = port_number
        try:
            port_number = self.ostinato_port_name_to_port_number(port_number)
            port = ost_pb.PortIdList()
            port.port_id.add().id = port_number
            return port
        except:
            self.logger.log_error("Invalid Ostinato port: " + str(og_port_number))
            # log error

    def ostinato_port_name_to_port_number(self, port_name):
        drone = self.connection
        if isinstance(port_name, PortIdList):
            return port_name.port_id[0].id
        if str(port_name).isdigit():
            return port_name
        port_id_list = drone.getPortIdList()
        port_config_list = drone.getPortConfig(port_id_list)
        for port in port_config_list.port:
            if port.name == port_name:
                return port.port_id.id

    def list_port_list(self):
        drone = self.connection
        port_id_list = drone.getPortIdList()
        port_config_list = drone.getPortConfig(port_id_list)
        self.logger.log_debug('Port List')
        self.logger.log_debug('---------')
        for port in port_config_list.port:
            self.logger.log_debug('%d.%s (%s)' % (port.port_id.id, port.name, port.description))

    def clear_capture_filters_and_triggers(self, port_string):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        pass
        # return self.logger.log_unimplemented_method()

    def register_agents(self):
        super(OstinatoDevice, self).register_agents()
        self.register_agent(TrafficGenerationConstants.TELNET, IxiaConnectionTelnetAgent(self))

    def register_apis(self):
        super(OstinatoDevice, self).register_apis()
        self.logger.log_debug("registering Ostinato Agents")
        # self.register_api(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API, SpirentTrafficTagConfigApi(self))


class OstinatoCaptureBuffer(object):
    def __init__(self, dev):
        self.dev = dev
        self.buffer = {}
        self.bufferStartStamp = {}
        self.bufferStopStamp = {}

    def start_capture_buffer(self, port_string):
        self.clear_capture_buffer(port_string)
        self.bufferStartStamp[port_string] = current_milli_time()

    def stop_capture_buffer(self, port_string):
        self.bufferStopStamp[port_string] = current_milli_time()
        self.buffer[port_string] = self.dev.get_all_captured_frames(port_string)

    def get_stored_capture_buffer(self, port_string):
        return self.buffer[port_string]

    def clear_capture_buffer(self, port_string):
        self.buffer[port_string] = None
        self.bufferStartStamp[port_string] = -1
        self.bufferStopStamp[port_string] = -1

    def clear_all_capture_buffer(self, port_string):
        self.buffer = {}
        self.bufferStartStamp = {}
        self.bufferStopStamp = {}

    def is_capture_buffer_filled(self, port_string):
        return port_string in self.buffer and self.buffer[port_string] is not None


class OstinatoDeviceConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device

    ARP_DST_HW_ADDR_CMD = "arp_dst_hw_addr"

    IPV6_DST_MODE_CMD = "ipv6_dst_mode"
    # Constant values for IPV6_DST_MODE_CMD
    IPV6_DST_MODE_FIXED_INCREMENT = "fixed increment"
    IPV6_DST_MODE_DECREMENT_LIST_RANDOM = "decrement list random"
    IPV6_DST_MODE_INCR_HOST_DECR_HOST = "incr_host decr_host"
    IPV6_DST_MODE_INCR_NETWORK = "incr_network"
    IPV6_DST_MODE_DECR_NETWORK = "decr_network"
    IPV6_DST_MODE_INCR_INTF_ID = "incr_intf_id"
    IPV6_DST_MODE_DECR_INTF_ID = "decr_intf_id"
    IPV6_DST_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    IPV6_DST_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    IPV6_DST_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"
    IPV6_DST_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    IPV6_DST_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    IPV6_DST_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    IPV6_DST_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    IPV6_DST_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    IPV6_DST_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    IPV6_DST_MODE_DECR_MCAST_GROUP = "decr_mcast_group"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

# protocol fields
# kArpFieldNumber = {int} 300
# kDot2LlcFieldNumber = {int} 206
# kDot2SnapFieldNumber = {int} 207
# kDot3FieldNumber = {int} 201
# kEth2FieldNumber = {int} 200
# kHexDumpFieldNumber = {int} 104
# kIcmpFieldNumber = {int} 402
# kIgmpFieldNumber = {int} 403
# kIp4FieldNumber = {int} 301
# kIp4over4FieldNumber = {int} 305
# kIp4over6FieldNumber = {int} 304
# kIp6FieldNumber = {int} 302
# kIp6over4FieldNumber = {int} 303
# kIp6over6FieldNumber = {int} 306
# kLlcFieldNumber = {int} 202
# kMacFieldNumber = {int} 100
# kMldFieldNumber = {int} 404
# kPayloadFieldNumber = {int} 101
# kSampleFieldNumber = {int} 102
# kSnapFieldNumber = {int} 203
# kSvlanFieldNumber = {int} 204
# kTcpFieldNumber = {int} 400
# kTextProtocolFieldNumber = {int} 500
# kUdpFieldNumber = {int} 401
# kUserScriptFieldNumber = {int} 103
# kVlanFieldNumber = {int} 205
# kVlanStackFieldNumber = {int} 208
