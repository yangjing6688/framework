from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class IxiaPortConfigIxTclHalApi (IxiaIxTclHalApi):
    def __init__(self, device):
        super(IxiaPortConfigIxTclHalApi, self).__init__(device)

    def set_transmit_mode(self, port_string, mode):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        commands.append("port config -transmitMode " + str(mode))
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)

    def get_transmit_mode(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        self.send_command("port get " + str(port_string))
        return self.strip_return(self.send_command("port cget -transmitMode "))


class IxiaPortConfigIxTclHalConstants(object, metaclass=Singleton):
    # 0 (default) set up hardware to use normal streams
    TRANSMIT_MODE_PORTTXPACKETSTREAMS = "portTxPacketStreams"
    # 1 set up hardware to use packet flows
    TRANSMIT_MODE_PORTTXPACKETFLOWS = "portTxPacketFlows"
    # 4 set up hardware to use the advanced scheduler
    TRANSMIT_MODE_PORTTXMODEADVANCEDSCHEDULER = "portTxModeAdvancedScheduler"
    # 5 set up the hardware to use Bit Error Rate patterns
    TRANSMIT_MODE_PORTTXMODEBERT = "portTxModeBert"
    # 6 set up the hardware to use channelized BERT
    TRANSMIT_MODE_PORTTXMODEBERTCHANNELIZED = "portTxModeBertChannelized"
    # 7 sets up port to echo received packets
    TRANSMIT_MODE_PORTTXMODEECHO = "portTxModeEcho"
    # 8 sets up the port to only transmit DCC packets as a stream
    TRANSMIT_MODE_PORTTXMODEDCCSTREAMS = "portTxModeDccStreams"
    # 9 sets up the port to only transmit DCC packets as advanced streams
    TRANSMIT_MODE_PORTTXMODEDCCAVANCEDSCHEDULER = "portTxModeDccAvancedScheduler"
    # 10 sets up the port to transmit DCC packets as flows and SPE packets as streams
    TRANSMIT_MODE_PORTTXMODEDCCFLOWSSPESTREAMS = "portTxModeDccFlowsSpeStreams"
    # 11 sets up the port to transmit DCC packets as flows and SPE packets as advanced streams
    TRANSMIT_MODE_PORTTXMODEDCCFLOWSSPEADVANCEDSCHEDULER = "portTxModeDccFlowsSpeAdvancedScheduler"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
