from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils


class IxiaCaptureIxTclHalApi(IxiaIxTclHalApi):
    """
    init function
    """

    def __init__(self, device):
        super(IxiaCaptureIxTclHalApi, self).__init__(device)

    def get_captured_frame_count(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("capture get " + str(port_string))
        frame_string = dev.send_command("capture cget -nPackets")
        return self.strip_return(frame_string)

    def get_captured_frame_status(self, port_string, frame_num):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("captureBuffer get " + str(port_string) + " " + str(frame_num) + " " + str(frame_num))
        dev.send_command("captureBuffer getframe 1")
        frame_string = dev.send_command("captureBuffer cget -status")
        return self.strip_return(frame_string)

    def get_captured_frame(self, port_string, frame_num):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("captureBuffer get " + str(port_string) + " " + str(frame_num) + " " + str(frame_num))
        dev.send_command("captureBuffer getframe 1")
        frame_string = dev.send_command("captureBuffer cget -frame")
        return self.strip_return(frame_string)

    def get_captured_packet(self, port_string, frame_num):
        return PacketClassifier.classify_packet_bytes(self.get_captured_frame(port_string, frame_num))

    def get_captured_frames(self, port_string, first_frame, last_frame):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("captureBuffer get " + str(port_string) + " " + str(first_frame) + " " + str(last_frame))
        frame_count = last_frame - first_frame
        return_frames = []
        for index in range(0, frame_count):
            dev.send_command("captureBuffer getframe " + str(index + 1))
            frame_string = self.strip_return(dev.send_command("captureBuffer cget -frame"))
            return_frames.append(frame_string)
            index += 1
        return return_frames

    def get_captured_packets(self, port_string, first_frame, last_frame):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("captureBuffer get " + str(port_string) + " " + str(first_frame) + " " + str(last_frame))
        frame_count = last_frame - first_frame
        return_frames = []
        for index in range(0, frame_count):
            dev.send_command("captureBuffer getframe " + str(index + 1))
            frame_string = dev.send_command("captureBuffer cget -frame")
            return_frames.append(PacketClassifier.classify_packet_bytes(self.strip_return(frame_string)))
            index += 1
        return return_frames
