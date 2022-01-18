import mock
import inspect
import time
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.Common.Agents.SshAgent import SshAgent
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDevice import JetsDevice, JetsStreamObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDevice import SpirentDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDevice import OstinatoDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import DroneProxy
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class TrafficGenerationTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.logger = Logger()
        cls.logger.log_info("START-Loading Devices and Device Information")
        cls.jets_dev = JetsDevice()
        setattr(cls, "jets_vm", "1.2.3.4")
        setattr(cls, "jets_vm_port", 22)

        # cls.ostinato_dev = OstinatoDevice()
        # setattr(cls, "ostinato_vm", "1.2.3.4")
        # setattr(cls, "ostinato_vm_port", 7878)

        cls.ixia_dev = IxiaDevice()
        setattr(cls, "ixia_vm", "1.2.3.4")
        setattr(cls, "ixia_vm_port", 5678)

        cls.spirent_dev = SpirentDevice()
        setattr(cls, "spirent_vm", "1.2.3.4")
        setattr(cls, "spirent_vm_port", 5679)
        cls.logger.log_info("END-Loading Devices and Device Information\n")

    # +-------------+
    # | Connect Tests |
    # +-------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(SshAgent, "login")
    @mock.patch.object(JetsDevice, "send_command")
    def test_connect_jets(self, mock_dev, mock_login, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        mock_login.return_value = ""
        mock_connect.return_value = ""
        mock_dev.return_value = ""
        self.logger.log_info("Connect called")
        traffic_device.connect(self.jets_vm, self.jets_vm_port)
        self.__test_connected(traffic_device)
        self.__test_teardown(self.jets_dev)

    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(SshAgent, "login")
    @mock.patch.object(JetsDevice, "send_command")
    def test_connect_jets_view_tag(self, mock_dev, mock_login, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        mock_login.return_value = ""
        mock_connect.return_value = ""
        mock_dev.return_value = ""
        self.logger.log_info("Connect called")
        traffic_device.set_view_tag("vtag")
        traffic_device.connect(self.jets_vm, self.jets_vm_port)
        self.__test_connected(traffic_device)
        self.__test_teardown(self.jets_dev)

    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(SshAgent, "login")
    @mock.patch.object(JetsDevice, "send_command")
    def test_connect_jets_root_directory(self, mock_dev, mock_login, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        mock_login.return_value = ""
        mock_connect.return_value = ""
        mock_dev.return_value = ""
        self.logger.log_info("Connect called")
        traffic_device.set_jets_directory("/tmp/ddd/")
        traffic_device.connect(self.jets_vm, self.jets_vm_port)
        self.__test_connected(traffic_device)
        self.__test_teardown(self.jets_dev)

    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(SshAgent, "login")
    @mock.patch.object(JetsDevice, "send_command")
    def test_connect_jets_view_tag_and_root_directory(self, mock_dev, mock_login, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        mock_login.return_value = ""
        mock_connect.return_value = ""
        mock_dev.return_value = ""
        self.logger.log_info("Connect called")
        traffic_device.set_view_tag("vtag")
        traffic_device.set_jets_directory("/tmp/ddd/")
        traffic_device.connect(self.jets_vm, self.jets_vm_port)
        self.__test_connected(traffic_device)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch.object(OstinatoDevice, "send_command")
    # def test_connect_ostinato(self, mock_dev, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     mock_connect.return_value = ""
    #     mock_dev.return_value = ""
    #     self.logger.log_info("Connect called")
    #     traffic_device.connect(self.ostinato_vm, self.ostinato_vm_port)
    #     # self.logger.log_info("assert connect call")
    #     # mock_connect.assert_called_with()
    #     self.__test_connected(traffic_device)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_connect_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        self.logger.log_info("Connect called")
        traffic_device.connect(self.ixia_vm, self.ixia_vm_port)
        self.logger.log_info("assert connect call")
        mock_connect.assert_called_with()
        self.__test_connected(traffic_device)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_connect_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.spirent_dev)
        assert isinstance(traffic_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        self.logger.log_info("Connect called")
        traffic_device.connect(self.spirent_vm, self.spirent_vm_port)
        self.logger.log_info("assert connect call")
        mock_connect.assert_called_with()
        self.__test_connected(traffic_device)
        self.__test_teardown(self.spirent_dev)

    def __test_connected(self, traffic_device):
        self.logger.log_info("assert is_connected")
        self.assertTrue(traffic_device.is_connected())
        self.logger.log_info("assert is_initialized")
        self.assertTrue(traffic_device.is_initialized())

    # +------------------+
    # | Disconnect Tests |
    # +------------------+
    @mock.patch.object(SshAgent, "disconnect")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_disconnect_jets(self, mock_ssh, mock_disconnect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        traffic_device.connection = mock_ssh
        self.logger.log_info("disconnect called")
        traffic_device.disconnect()
        self.__test_disconnected(traffic_device)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "disconnect")
    # @mock.patch("ostinato.core.DroneProxy")
    # def test_disconnect_ostinato(self, mock_drone_proxy, mock_disconnect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     traffic_device.connection = mock_drone_proxy
    #     self.logger.log_info("disconnect called")
    #     traffic_device.disconnect()
    #     self.__test_disconnected(traffic_device)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "disconnect")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent")
    def test_disconnect_ixia(self, mock_telnet, mock_disconnect):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        traffic_device.connection = mock_telnet
        self.logger.log_info("disconnect called")
        traffic_device.disconnect()
        self.__test_disconnected(traffic_device)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "disconnect")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent")
    def test_disconnect_spirent(self, mock_telnet, mock_disconnect):
        traffic_device = self.__test_setup(self.spirent_dev)
        assert isinstance(traffic_device, SpirentDevice)
        traffic_device.connection = mock_telnet
        self.logger.log_info("disconnect called")
        traffic_device.disconnect()
        self.__test_disconnected(traffic_device)
        self.__test_teardown(self.spirent_dev)

    def __test_disconnected(self, traffic_device):
        self.logger.log_info("assert is_connected")
        self.assertFalse(traffic_device.is_connected())
        self.logger.log_info("assert is_initialized")
        self.assertFalse(traffic_device.is_initialized())

    # +---------------------+
    # | Start Traffic Tests |
    # +---------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_start_traffic_jets(self, mock_ssh, mock_send_command, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        traffic_device.connection = mock_ssh
        port = "eth1"
        traffic_device._streams = {port: {"1": "1"}}
        stream_object = JetsStreamObject("st"
                                         "ream_name", "eth1", "1", "1", "length",
                                         "packet_mode", "num_packets", "rate_pps",
                                         "rate_burst")
        traffic_device._stream_objects = {"1": stream_object}
        self.logger.log_info("Start Traffic called")
        traffic_device.start_traffic(port)
        self.logger.log_info("Check State")
        self.assertEqual(stream_object.state, "Run")
        # self.__test_start_traffic(traffic_device, port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_start_traffic_ostinato(self, mock_dev, mock_proxy, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     traffic_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     port = "eth1"
    #     self.logger.log_info("Start Traffic called")
    #     traffic_device.start_traffic(port)
    #     # self.__test_start_traffic(traffic_device, port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_start_traffic_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Start Traffic called")
        traffic_device.start_traffic(port)
        # self.__test_start_traffic(traffic_device, port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_start_traffic_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.spirent_dev)
        assert isinstance(traffic_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Start Traffic called")
        traffic_device.start_traffic(port)
        # self.__test_start_traffic(traffic_device, port)
        self.__test_teardown(self.spirent_dev)

    def __test_start_traffic(self, traffic_device, port):
        self.logger.log_info("assert is_port_transmitting")
        self.assertTrue(traffic_device.is_port_transmitting(port))

    # +---------------------+
    # | Stop Traffic Tests |
    # +---------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_stop_traffic_jets(self, mock_ssh, mock_send_command, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        traffic_device.connection = mock_ssh
        port = "eth1"
        traffic_device._streams = {port: {"1": "1"}}
        stream_object = JetsStreamObject("st"
                                         "ream_name", "eth1", "1", "1", "length",
                                         "packet_mode", "num_packets", "rate_pps",
                                         "rate_burst")
        traffic_device._stream_objects = {"1": stream_object}
        self.logger.log_info("Stop Traffic called")
        traffic_device.stop_traffic(port)
        self.logger.log_info("Check State")
        self.assertEqual(stream_object.state, "Stop")
        # self.__test_stop_traffic(traffic_device, port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_stop_traffic_ostinato(self, mock_dev, mock_proxy, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     traffic_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     port = "eth1"
    #     self.logger.log_info("Stop Traffic called")
    #     traffic_device.stop_traffic(port)
    #     # self.__test_stop_traffic(traffic_device, port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_stop_traffic_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Stop Traffic called")
        traffic_device.stop_traffic(port)
        self.__test_stop_traffic(traffic_device, port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_stop_traffic_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.spirent_dev)
        assert isinstance(traffic_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Stop Traffic called")
        traffic_device.stop_traffic(port)
        self.__test_stop_traffic(traffic_device, port)
        self.__test_teardown(self.spirent_dev)

    def __test_stop_traffic(self, traffic_device, port):
        self.logger.log_info("assert is_port_transmitting")
        self.assertFalse(traffic_device.is_port_transmitting(port))

    # +------------------------------+
    # | Start Traffic And Wait Tests |
    # +------------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_start_traffic_and_wait_jets(self, mock_ssh, mock_send_command, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        traffic_device.connection = mock_ssh
        port = "eth1"
        traffic_device._streams = {port: {"1": "1"}}
        stream_object = JetsStreamObject("st"
                                         "ream_name", "eth1", "1", "1", "length",
                                         "packet_mode", "num_packets", "rate_pps",
                                         "rate_burst")
        traffic_device._stream_objects = {"1": stream_object}
        self.logger.log_info("Start Traffic And Wait called")
        traffic_device.start_traffic_and_wait(port, 0)
        self.logger.log_info("Check State")
        self.assertEqual(stream_object.state, "Run")
        # self.__test_start_traffic(traffic_device, port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch.object(OstinatoDevice, "get_stream_count")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_start_traffic_and_wait_ostinato(self, mock_dev, mock_proxy, mock_stream_count, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     traffic_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stream_count.return_value = "1"
    #     port = "eth1"
    #     self.logger.log_info("Start Traffic And Wait called")
    #     traffic_device.start_traffic_and_wait(port, 0)
    #     # self.__test_start_traffic(traffic_device, port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "get_stream_count")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_start_traffic_and_wait_ixia(self, mock_dev, mock_stream_count, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_stream_count.return_value = "1"
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Start Traffic And Wait called")
        traffic_device.start_traffic_and_wait(port, 0)
        # self.__test_start_traffic(traffic_device, port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "get_stream_count")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_start_traffic_and_wait_spirent(self, mock_dev, mock_stream_count, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.spirent_dev)
        assert isinstance(traffic_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_stream_count.return_value = "1"
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Start Traffic And Wait called")
        traffic_device.start_traffic_and_wait(port, 0)
        # self.__test_start_traffic(traffic_device, port)
        self.__test_teardown(self.spirent_dev)

    # +---------------------+
    # | Start Capture Tests |
    # +---------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_start_capture_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        port = "eth2"
        self.logger.log_info("Start Capture called")
        capture_device.start_capture(port)
        # self.__test_start_capture(capture_device, port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_start_capture_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value.port_stats[0].state.is_capture_on = False
    #     port = "eth1"
    #     self.logger.log_info("Start Capture called")
    #     capture_device.start_capture(port)
    #     # self.__test_start_capture(capture_device, port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_start_capture_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Start Capture called")
        capture_device.start_capture(port)
        # self.__test_start_capture(capture_device, port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_start_capture_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Start Capture called")
        capture_device.start_capture(port)
        # self.__test_start_capture(capture_device, port)
        self.__test_teardown(self.spirent_dev)

    def __test_start_capture(self, traffic_device, port):
        self.logger.log_info("assert is_port_capturing")
        self.assertTrue(traffic_device.is_port_capturing(port))

    # +---------------------+
    # | Stop Capture Tests |
    # +---------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch.object(OstinatoDevice, "get_all_captured_frames")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_stop_capture_jets(self, mock_ssh, mock_buffer, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        mock_buffer.return_value = []
        capture_device.connection = mock_ssh
        port = "eth2"
        self.logger.log_info("Stop Capture called")
        capture_device.stop_capture(port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "get_all_captured_frames")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_stop_capture_ostinato(self, mock_dev, mock_buffer, mock_proxy, mock_connect):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_buffer.return_value = []
    #     port = "eth1"
    #     self.logger.log_info("Stop Capture called")
    #     capture_device.stop_capture(port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "get_all_captured_frames")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_stop_capture_ixia(self, mock_dev, mock_buffer, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_buffer.return_value = []
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Stop Capture called")
        capture_device.stop_capture(port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "get_all_captured_frames")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_stop_capture_spirent(self, mock_dev, mock_buffer, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_buffer.return_value = []
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Stop Capture called")
        capture_device.stop_capture(port)
        self.__test_teardown(self.spirent_dev)

    # +---------------------+
    # | Has Link Tests |
    # +---------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_has_link_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        port = "eth2"
        self.logger.log_info("Has Link called")
        self.logger.log_info("answer:" + str(capture_device.has_link(port)))
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_has_link_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value.port_stats[0].state.link_state = 2
    #     port = "eth1"
    #     self.logger.log_info("Has Link called")
    #     answer = str(capture_device.has_link(port))
    #     self.assertTrue(StringUtils.string_to_boolean(answer))
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_has_link_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}} " \
                                "{port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} " \
                                "{rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0} " \
                                "{late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        port = "1.2.3"
        self.logger.log_info("Has Link called - Linked")
        answer = str(capture_device.has_link(port))
        self.assertTrue(StringUtils.string_to_boolean(answer))
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}} " \
                                "{port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} " \
                                "{rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0} " \
                                "{late_collisions 0} {link 0} {portCpuMemory 256}}} {status 1}"
        self.logger.log_info("Has Link called - No Linked")
        answer = str(capture_device.has_link(port))
        self.assertFalse(StringUtils.string_to_boolean(answer))
        self.__test_teardown(self.ixia_dev)

    # @mock.patch.object(TelnetAgent, "connect")
    # @mock.patch.object(TelnetAgent, "wait_no_parse")
    # @mock.patch.object(SpirentDevice, "send_command")
    # def test_has_link_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
    #     capture_device = self.__test_setup(self.spirent_dev)
    #     assert isinstance(capture_device, SpirentDevice)
    #     mock_connect.return_value = ""
    #     mock_wait_no_parse.return_value = ""
    #     mock_dev.return_value = "{$port__2_3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}"
    #     " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} {rx_collisions 0}"
    #     " {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0} {late_collisions 0} {link 1} "
    #     " {portCpuMemory 256}}} {status 1}"
    #     port = "1.2.3"
    #     self.logger.log_info("Has Link called - Linked")
    #     answer = str(capture_device.has_link(port))
    #     self.assertTrue(StringUtils.string_to_boolean(answer))
    #     mock_dev.return_value = "{$port__2_3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}"
    #     " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} {rx_collisions 0} "
    #     "{total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0} {late_collisions 0} {link 0} "
    #     "{portCpuMemory 256}}} {status 1}"
    #     self.logger.log_info("Has Link called - No Linked")
    #     answer = str(capture_device.has_link(port))
    #     self.assertFalse(StringUtils.string_to_boolean(answer))
    #     self.__test_teardown(self.spirent_dev)

    # +---------------------+
    # | Wait For Has Link Tests |
    # +---------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_wait_for_has_link_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        port = "eth2"
        self.logger.log_info("Wait For Has Link called")
        capture_device.wait_for_has_link(port, "1000")
        self.logger.log_info("Wait For Has Link called timeout")
        mock_send_command.return_value = ""
        start_time = time.time()
        time_out = 2
        capture_device.wait_for_has_link(port, time_out * 1000)
        elapsed_time = int(round(time.time() - start_time))
        self.assertEqual(elapsed_time, time_out)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "has_link")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_wait_for_has_link_ostinato(self, mock_dev, mock_link, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value.port_stats[0].state.is_capture_on = False
    #     mock_link.return_value = True
    #     port = "eth1"
    #     self.logger.log_info("Wait For Has Link called")
    #     capture_device.wait_for_has_link(port, "1000")
    #     self.logger.log_info("Wait For Has Link called timeout")
    #     mock_link.return_value = False
    #     start_time = time.time()
    #     time_out = 2
    #     capture_device.wait_for_has_link(port, time_out * 1000)
    #     elapsed_time = int(round(time.time() - start_time))
    #     self.assertEqual(elapsed_time, time_out)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_wait_for_has_link_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}} " \
                                "{port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} " \
                                "{rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0}" \
                                " {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        port = "1.2.3"
        self.logger.log_info("Wait For Has Link called")
        capture_device.wait_for_has_link(port, "1000")
        self.logger.log_info("Wait For Has Link called timeout")
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}" \
                                " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00}" \
                                " {rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0}" \
                                " {late_collisions 0} {link 0} {portCpuMemory 256}}} {status 1}"
        start_time = time.time()
        time_out = 2
        capture_device.wait_for_has_link(port, time_out * 1000)
        elapsed_time = int(round(time.time() - start_time))
        self.assertEqual(elapsed_time, time_out)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "has_link")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_wait_for_has_link_spirent(self, mock_dev, mock_link, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_link.return_value = True
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}" \
                                " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00}" \
                                " {rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0}" \
                                " {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        port = "1.2.3"
        self.logger.log_info("Wait For Has Link called")
        capture_device.wait_for_has_link(port, "1000")
        self.logger.log_info("Wait For Has Link called timeout")
        mock_link.return_value = False
        start_time = time.time()
        time_out = 2
        capture_device.wait_for_has_link(port, time_out * 1000)
        elapsed_time = int(round(time.time() - start_time))
        self.assertEqual(elapsed_time, time_out)
        self.__test_teardown(self.spirent_dev)

    # +---------------------------+
    # | Take Port Ownership Tests |
    # +---------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_take_port_ownership_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        traffic_device = self.__test_setup(self.jets_dev)
        assert isinstance(traffic_device, JetsDevice)
        mock_port.return_value = "2"
        traffic_device.connection = mock_ssh
        mock_send_command.return_value = ""
        port = "eth2"
        self.logger.log_info("Take Ports Ownership called - one port")
        traffic_device.take_port_ownership(self.jets_vm, "name", port)
        port = ["eth2", "eth4", "eth5"]
        self.logger.log_info("Take Ports Ownership called - three ports")
        traffic_device.take_port_ownership(self.jets_vm, "name", port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch.object(OstinatoDevice, "send_command")
    # def test_take_port_ownership_ostinato(self, mock_dev, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     mock_connect.return_value = ""
    #     mock_dev.return_value = ""
    #     port = "eth2"
    #     self.logger.log_info("Take Ports Ownership called - one port")
    #     traffic_device.take_port_ownership(self.jets_vm, "name", port)
    #     port = ["eth2", "eth4", "eth5"]
    #     self.logger.log_info("Take Ports Ownership called - three ports")
    #     traffic_device.take_port_ownership(self.jets_vm, "name", port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_take_port_ownership_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Take Ports Ownership called - one port")
        traffic_device.take_port_ownership(self.jets_vm, "name", port)
        port = ["1.2.3", "1.3.4", "1.3.3"]
        self.logger.log_info("Take Ports Ownership called - three ports")
        traffic_device.take_port_ownership(self.jets_vm, "name", port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_take_port_ownership_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        traffic_device = self.__test_setup(self.spirent_dev)
        assert isinstance(traffic_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Loaded"
        port = "1.2.3"
        self.logger.log_info("Take Ports Ownership called - one port")
        traffic_device.take_port_ownership(self.jets_vm, "name", port)
        port = ["1.2.3", "1.3.4", "1.3.3"]
        self.logger.log_info("Take Ports Ownership called - three ports")
        traffic_device.take_port_ownership(self.jets_vm, "name", port)
        self.__test_teardown(self.spirent_dev)

    # +----------------------------+
    # | Clear Capture Buffer Tests |
    # +----------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "get_circuit_name_from_interface_name")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_clear_capture_buffer_jets(self, mock_ssh, mock_send_command,
                                       mock_circuitname_command,  mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        mock_circuitname_command.return_value = "i2"
        port = "eth2"
        self.logger.log_info("Clear Capture Buffer called")
        capture_device.clear_capture_buffer(port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_clear_capture_buffer_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value = ""
    #     port = "eth1"
    #     self.logger.log_info("Clear Capture Buffer called")
    #     capture_device.clear_capture_buffer(port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_clear_capture_buffer_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Checking link states on ports ...\nLinks on all ports are up."
        port = "1.2.3"
        self.logger.log_info("Clear Capture Buffer called")
        capture_device.clear_capture_buffer(port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_clear_capture_buffer_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "Checking link states on ports ...\nLinks on all ports are up."
        port = "1.2.3"
        self.logger.log_info("Clear Capture Buffer called")
        capture_device.clear_capture_buffer(port)
        self.__test_teardown(self.spirent_dev)

    # +----------------------------+
    # | Clear All Streams Tests |
    # +----------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_clear_all_streams_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        port = "eth2"
        self.logger.log_info("Clear All Streams called")
        capture_device.clear_all_streams(port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_clear_all_streams_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value = ""
    #     port = "eth1"
    #     self.logger.log_info("Clear All Streams called")
    #     capture_device.clear_all_streams(port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_clear_all_streams_ixia(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear All Streams called")
        capture_device.clear_all_streams(port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_clear_all_streams_spirent(self, mock_dev, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear All Streams called")
        capture_device.clear_all_streams(port)
        self.__test_teardown(self.spirent_dev)

    # +------------------------------------------+
    # | Clear Capture Filters And Triggers Tests |
    # +------------------------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_clear_capture_filters_and_triggers_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        port = "eth2"
        self.logger.log_info("Clear Capture Filters And Triggers called")
        capture_device.clear_capture_filters_and_triggers(port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_clear_capture_filters_and_triggers_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value = ""
    #     port = "eth1"
    #     self.logger.log_info("Clear Capture Filters And Triggers called")
    #     capture_device.clear_capture_filters_and_triggers(port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "clear_output_buffer")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_clear_capture_filters_and_triggers_ixia(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear Capture Filters And Triggers called")
        capture_device.clear_capture_filters_and_triggers(port)
        self.__test_teardown(self.ixia_dev)

    # @mock.patch.object(TelnetAgent, "connect")
    # @mock.patch.object(TelnetAgent, "wait_no_parse")
    # @mock.patch.object(SpirentDevice, "clear_output_buffer")
    # @mock.patch.object(SpirentDevice, "send_command")
    # def test_clear_capture_filters_and_triggers_spirent(self, mock_dev, mock_clear_buff, mock_wait_no_parse,
    # mock_connect):
    #     capture_device = self.__test_setup(self.spirent_dev)
    #     assert isinstance(capture_device, SpirentDevice)
    #     mock_connect.return_value = ""
    #     mock_wait_no_parse.return_value = ""
    #     mock_clear_buff.return_value = ""
    #     mock_dev.return_value = "{status 1}"
    #     port = "1.2.3"
    #     self.logger.log_info("Clear Capture Filters And Triggers called")
    #     capture_device.clear_capture_filters_and_triggers(port)
    #     self.__test_teardown(self.spirent_dev)

    # +------------------------------------------+
    # | Clear Statistics Tests |
    # +------------------------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "get_circuit_name_from_interface_name")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_clear_statistics_jets(self, mock_ssh, mock_send_command,
                                   mock_circuitname_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        mock_circuitname_command.return_value = "i2"
        port = "eth2"
        self.logger.log_info("Clear Statistics called")
        capture_device.clear_statistics(port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_clear_statistics_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value = ""
    #     port = "eth1"
    #     self.logger.log_info("Clear Statistics called")
    #     capture_device.clear_statistics(port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "clear_output_buffer")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_clear_statistics_ixia(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear Statistics called")
        capture_device.clear_statistics(port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "clear_output_buffer")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_clear_statistics_spirent(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear Statistics called")
        capture_device.clear_statistics(port)
        self.__test_teardown(self.spirent_dev)

    # +------------------------------------------+
    # | Clear Statistics And Filters Tests |
    # +------------------------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "get_circuit_name_from_interface_name")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_clear_statistics_and_filters_jets(self, mock_ssh, mock_send_command,
                                               mock_circuitname_command, mock_port, connect_command):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        mock_circuitname_command.return_value = "i2"
        port = "eth2"
        self.logger.log_info("Clear Statistics And Filters called")
        capture_device.clear_statistics_and_filters(port)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_clear_statistics_and_filters_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value = ""
    #     port = "eth1"
    #     self.logger.log_info("Clear Statistics And Filters called")
    #     capture_device.clear_statistics_and_filters(port)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "clear_output_buffer")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_clear_statistics_and_filters_ixia(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear Statistics And Filters called")
        capture_device.clear_statistics_and_filters(port)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "clear_output_buffer")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_clear_statistics_and_filters_spirent(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        self.logger.log_info("Clear Statistics And Filters called")
        capture_device.clear_statistics_and_filters(port)
        self.__test_teardown(self.spirent_dev)

    # +------------------------------------------+
    # | Clear Stream Tests |
    # +------------------------------------------+
    @mock.patch.object(SshAgent, "connect")
    @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    @mock.patch.object(JetsDevice, "send_command")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    def test_clear_stream_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
        capture_device = self.__test_setup(self.jets_dev)
        assert isinstance(capture_device, JetsDevice)
        mock_port.return_value = "2"
        capture_device.connection = mock_ssh
        mock_send_command.return_value = "yes"
        port = "eth2"
        stream = 1
        self.logger.log_info("Clear Statistics And Filters called")
        capture_device.clear_stream(port, stream)
        self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "callRpcMethod")
    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "ostinato_port_number_to_port")
    # def test_clear_stream_ostinato(self, mock_dev, mock_proxy, mock_connect, mock_stats):
    #     capture_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(capture_device, OstinatoDevice)
    #     capture_device.connection = mock_proxy
    #     mock_dev.return_value = "1"
    #     mock_stats.return_value = ""
    #     port = "eth1"
    #     stream = 1
    #     self.logger.log_info("Clear Statistics And Filters called")
    #     capture_device.clear_stream(port, stream)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "clear_output_buffer")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_clear_stream_ixia(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        stream = 1
        self.logger.log_info("Clear Statistics And Filters called")
        capture_device.clear_stream(port, stream)
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "connect")
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "clear_output_buffer")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_clear_stream_spirent(self, mock_dev, mock_clear_buff, mock_wait_no_parse, mock_connect):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_connect.return_value = ""
        mock_wait_no_parse.return_value = ""
        mock_clear_buff.return_value = ""
        mock_dev.return_value = "{status 1}"
        port = "1.2.3"
        stream = 1
        self.logger.log_info("Clear Statistics And Filters called")
        capture_device.clear_stream(port, stream)
        self.__test_teardown(self.spirent_dev)

    # +------------------------------------------+
    # | Get Port Capture Tests                   |
    # +------------------------------------------+

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_get_port_capture_ixia(self, mock_dev, mock_wait_no_parse):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "N/A"
        port = "1.2.3"
        self.logger.log_info("Get Port Capture called")
        capture_device.get_port_capture(port, "format")
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_get_port_capture_spirent(self, mock_dev, mock_wait_no_parse):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "N/A"
        port = "1.2.3"
        self.logger.log_info("Get Port Capture called")
        capture_device.get_port_capture(port, "format")
        self.__test_teardown(self.spirent_dev)

    # +------------------------------------------+
    # | Get Port Capture Frame Tests             |
    # +------------------------------------------+

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_get_port_capture_frame_ixia(self, mock_dev, mock_wait_no_parse):
        capture_device = self.__test_setup(self.ixia_dev)
        assert isinstance(capture_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "N/A"
        port = "1.2.3"
        self.logger.log_info("Get Port Capture Frame called")
        capture_device.get_port_capture_frame(port, 1, "format")
        self.__test_teardown(self.ixia_dev)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(SpirentDevice, "send_command")
    def test_get_port_capture_frame_spirent(self, mock_dev, mock_wait_no_parse):
        capture_device = self.__test_setup(self.spirent_dev)
        assert isinstance(capture_device, SpirentDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "N/A"
        port = "1.2.3"
        self.logger.log_info("Get Port Capture Frame called")
        capture_device.get_port_capture_frame(port, 1, "format")
        self.__test_teardown(self.spirent_dev)

    # +-------------------------------+
    # | Get Port Duplex Tests         |
    # +-------------------------------+

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_get_port_duplex_ixia(self, mock_dev, mock_wait_no_parse):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}" \
                                " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00}" \
                                " {rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 1000}" \
                                " {fcs_errors 0} {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        port = "1.2.3"
        self.logger.log_info("Get Port Duplex called")
        duplex = traffic_device.get_port_duplex(port)
        self.assertEqual(duplex, "full")
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}" \
                                " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00}" \
                                " {rx_collisions 0} {total_collisions 0} {duplex half} {intf_speed 1000}" \
                                " {fcs_errors 0} {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        duplex = traffic_device.get_port_duplex(port)
        self.assertEqual(duplex, "half")
        self.__test_teardown(self.ixia_dev)

    # +-------------------------------+
    # | Get Port Speed Tests         |
    # +-------------------------------+

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_get_port_speed_ixia(self, mock_dev, mock_wait_no_parse):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}" \
                                " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00}" \
                                " {rx_collisions 0} {total_collisions 0} {duplex full} {intf_speed 1000}" \
                                " {fcs_errors 0} {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        port = "1.2.3"
        self.logger.log_info("Get Port Speed called")
        duplex = traffic_device.get_port_speed(port)
        self.assertEqual(duplex, "1000")
        mock_dev.return_value = "{1/2/3 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}" \
                                " {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00}" \
                                " {rx_collisions 0} {total_collisions 0} {duplex half} {intf_speed 10}" \
                                " {fcs_errors 0} {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}"
        duplex = traffic_device.get_port_speed(port)
        self.assertEqual(duplex, "10")
        self.__test_teardown(self.ixia_dev)

    # +-------------------------------+
    # | Get Port Statistics Tests     |
    # +-------------------------------+

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_get_port_statistic_ixia(self, mock_dev, mock_wait_no_parse):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        # mock_dev.return_value = "{1/2/3 {{aggregate {{rx {{uds2_count {Stat userDefinedStat2 not supported}}"
        # " {qos2_rate 0} {pkt_byte_count {Stat bytesReceived not supported}} {qos0_count 0} {vlan_pkts_rate "
        # "{Stat vlanTaggedFramesRx not supported}} {sequence_errors_count {Stat sequenceErrors not supported}}"
        # " {qos4_count 0} {crc_errors_count 0} {qos7_rate 0} {uds1_count {Stat userDefinedStat1 not supported}}"
        # " {raw_pkt_count 0} {data_int_errors_count {Stat dataIntegrityErrors not supported}} {uds2_rate {Stat "
        # "userDefinedStat2 not supported}} {qos4_rate 0} {vlan_pkts_count {Stat vlanTaggedFramesRx not supported}} "
        # "{data_int_errors_rate {Stat dataIntegrityErrors not supported}} {raw_pkt_rate 0} {pkt_bit_count {Stat "
        # "bitsReceived not supported}} {qos3_count 0} {qos1_rate 0} {fragments_count 0} {collisions_count 0} "
        # "{qos7_count 0} {sequence_frames_count {Stat sequenceFrames not supported}} {sequence_errors_rate {Stat "
        # "sequenceErrors not supported}} {collisions_rate 0} {fragments_rate 0} {data_int_frames_rate {Stat "
        # "dataIntegrityFrames not supported}} {qos6_rate 0} {qos2_count 0} {pkt_count 0} {dribble_errors_count 0}"
        # " {uds1_rate {Stat userDefinedStat1 not supported}} {qos3_rate 0} {qos6_count 0} {data_int_frames_count"
        # " {Stat dataIntegrityFrames not supported}} {dribble_errors_rate 0} {qos0_rate 0} {crc_errors_rate 0} "
        # "{oversize_count 0} {pkt_bit_rate {Stat bitsReceived not supported}} {sequence_frames_rate {Stat "
        # "sequenceFrames not supported}} {pkt_rate 0} {undersize_rate 0} {qos1_count 0} {pkt_byte_rate {Stat "
        # "bytesReceived not supported}} {protocol_pkt_count 0} {qos5_count 0} {undersize_count 0} {oversize_rate 0} "
        # "{qos5_rate 0} {protocol_pkt_rate {Stat protocolServerRx not supported}}}} {tx {{raw_pkt_count 0} "
        # "{pkt_byte_count 0} {total_pkt_rate 0} {pkt_bit_count 0} {pkt_bit_rate 0} {pkt_rate 0} {pkt_count 0} "
        # "{total_pkt_bytes 0} {total_pkts_bytes 0} {elapsed_time 0.00} {pkt_byte_rate 0} {protocol_pkt_rate "
        # "{Stat protocolServerTx not supported}} {total_pkts 0} {raw_pkt_rate 0} {protocol_pkt_count 0}}}}} "
        # "{elapsed_time {Stat transmitDuration not supported}}}} {seconds 1549470299} {clicks 718319134} {status 1}"
        mock_dev.return_value = "0"
        port = "1.2.3"
        self.logger.log_info("Get Port Statistic called")
        duplex = traffic_device.get_port_statistic(port, 'rx', "qos0_count")
        self.assertEqual(duplex, "0")
        self.__test_teardown(self.ixia_dev)

    # +--------------------------------------+
    # | Get Port Stream Statistics Tests     |
    # +--------------------------------------+

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_get_port_stream_statistic_ixia(self, mock_dev, mock_wait_no_parse):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        # mock_dev.return_value = "{1/2/3 {{aggregate {{rx {{uds2_count {Stat userDefinedStat2 not supported}} "
        # "{qos2_rate 0} {pkt_byte_count {Stat bytesReceived not supported}} {qos0_count 0} {vlan_pkts_rate "
        # "{Stat vlanTaggedFramesRx not supported}} {sequence_errors_count {Stat sequenceErrors not supported}} "
        # "{qos4_count 0} {crc_errors_count 0} {qos7_rate 0} {uds1_count {Stat userDefinedStat1 not supported}} "
        # "{raw_pkt_count 0} {data_int_errors_count {Stat dataIntegrityErrors not supported}} {uds2_rate {Stat "
        # "userDefinedStat2 not supported}} {qos4_rate 0} {vlan_pkts_count {Stat vlanTaggedFramesRx not supported}} "
        # "{data_int_errors_rate {Stat dataIntegrityErrors not supported}} {raw_pkt_rate 0} {pkt_bit_count {Stat "
        # "bitsReceived not supported}} {qos3_count 0} {qos1_rate 0} {fragments_count 0} {collisions_count 0} "
        # "{qos7_count 0} {sequence_frames_count {Stat sequenceFrames not supported}} {sequence_errors_rate "
        # "{Stat sequenceErrors not supported}} {collisions_rate 0} {fragments_rate 0} {data_int_frames_rate {Stat "
        # "dataIntegrityFrames not supported}} {qos6_rate 0} {qos2_count 0} {pkt_count 0} {dribble_errors_count 0} "
        # "{uds1_rate {Stat userDefinedStat1 not supported}} {qos3_rate 0} {qos6_count 0} {data_int_frames_count "
        # "{Stat dataIntegrityFrames not supported}} {dribble_errors_rate 0} {qos0_rate 0} {crc_errors_rate 0} "
        # "{oversize_count 0} {pkt_bit_rate {Stat bitsReceived not supported}} {sequence_frames_rate {Stat "
        # "sequenceFrames not supported}} {pkt_rate 0} {undersize_rate 0} {qos1_count 0} {pkt_byte_rate {Stat "
        # "bytesReceived not supported}} {protocol_pkt_count 0} {qos5_count 0} {undersize_count 0} {oversize_rate 0} "
        # "{qos5_rate 0} {protocol_pkt_rate {Stat protocolServerRx not supported}}}} {tx {{raw_pkt_count 0} "
        # "{pkt_byte_count 0} {total_pkt_rate 0} {pkt_bit_count 0} {pkt_bit_rate 0} {pkt_rate 0} {pkt_count 0} "
        # "{total_pkt_bytes 0} {total_pkts_bytes 0} {elapsed_time 0.00} {pkt_byte_rate 0} {protocol_pkt_rate "
        # "{Stat protocolServerTx not supported}} {total_pkts 0} {raw_pkt_rate 0} {protocol_pkt_count 0}}}}} "
        # "{elapsed_time {Stat transmitDuration not supported}}}} {seconds 1549470299} {clicks 718319134} {status 1}"
        mock_dev.return_value = "0"
        port = "1.2.3"
        stream = 1
        self.logger.log_info("Get Port Stream Statistic called")
        duplex = traffic_device.get_port_stream_statistic(port, stream, "rx", "line_rate_percentage")
        self.assertEqual(duplex, "0")
        self.__test_teardown(self.ixia_dev)

    # +--------------------------------------+
    # | Get Is Port Transmitting Tests     |
    # +--------------------------------------+

    # @mock.patch.object(SshAgent, "connect")
    # @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    # @mock.patch.object(JetsDevice, "send_command")
    # @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    # def test_is_port_transmitting_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
    #     traffic_device = self.__test_setup(self.jets_dev)
    #     assert isinstance(traffic_device, JetsDevice)
    #     mock_port.return_value = "2"
    #     traffic_device.connection = mock_ssh
    #     mock_send_command.return_value = ""
    #     port = "eth2"
    #     self.logger.log_info("Is Port Transmitting called")
    #     duplex = traffic_device.is_port_transmitting(port)
    #     self.assertEqual(duplex, False)
    #     mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 0}"
    #     duplex = traffic_device.is_port_transmitting(port)
    #     self.assertEqual(duplex, True)
    #     self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "send_command")
    # def test_is_port_transmitting_ostinato(self, mock_dev, mock_drone_proxy, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     mock_connect.return_value = ""
    #     mock_dev.return_value = ""
    #     traffic_device.connection = mock_drone_proxy
    #     # port = "eth2"
    #     self.logger.log_info("Is Port Transmitting called")
    #     # duplex = traffic_device.is_port_transmitting(port)
    #     # self.assertEqual(duplex, False)
    #     # mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 0}"
    #     # duplex = traffic_device.is_port_transmitting(port)
    #     # self.assertEqual(duplex, True)
    #     self.__test_teardown(self.ostinato_dev)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(IxiaDevice, "send_command")
    def test_is_port_transmitting_ixia(self, mock_dev, mock_wait_no_parse):
        traffic_device = self.__test_setup(self.ixia_dev)
        assert isinstance(traffic_device, IxiaDevice)
        mock_wait_no_parse.return_value = ""
        mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 1}"
        port = "1.2.3"
        self.logger.log_info("Is Port Transmitting called")
        duplex = traffic_device.is_port_transmitting(port)
        self.assertEqual(duplex, False)
        mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 0}"
        duplex = traffic_device.is_port_transmitting(port)
        self.assertEqual(duplex, True)
        self.__test_teardown(self.ixia_dev)

    # +--------------------------------------+
    # | Get Is Port Capturing Tests     |
    # +--------------------------------------+

    # @mock.patch.object(SshAgent, "connect")
    # @mock.patch.object(JetsDevice, "get_port_index_from_group_string")
    # @mock.patch.object(JetsDevice, "send_command")
    # @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent")
    # def test_is_port_transmitting_jets(self, mock_ssh, mock_send_command, mock_port, mock_connect):
    #     traffic_device = self.__test_setup(self.jets_dev)
    #     assert isinstance(traffic_device, JetsDevice)
    #     mock_port.return_value = "2"
    #     traffic_device.connection = mock_ssh
    #     mock_send_command.return_value = ""
    #     port = "eth2"
    #     self.logger.log_info("Is Port Capturing called")
    #     duplex = traffic_device.is_port_capturing(port)
    #     self.assertEqual(duplex, False)
    #     mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 0}"
    #     duplex = traffic_device.is_port_capturing(port)
    #     self.assertEqual(duplex, True)
    #     self.__test_teardown(self.jets_dev)

    # @mock.patch.object(DroneProxy, "connect")
    # @mock.patch("ostinato.core.DroneProxy")
    # @mock.patch.object(OstinatoDevice, "send_command")
    # def test_is_port_capturing_ostinato(self, mock_dev, mock_drone_proxy, mock_connect):
    #     traffic_device = self.__test_setup(self.ostinato_dev)
    #     assert isinstance(traffic_device, OstinatoDevice)
    #     mock_connect.return_value = ""
    #     mock_dev.return_value = ""
    #     traffic_device.connection = mock_drone_proxy
    #     # port = "eth2"
    #     self.logger.log_info("Is Port Capturing called")
    #     # duplex = traffic_device.is_port_capturing(port)
    #     # self.assertEqual(duplex, False)
    #     # mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 0}"
    #     # duplex = traffic_device.is_port_capturing(port)
    #     # self.assertEqual(duplex, True)
    #     self.__test_teardown(self.ostinato_dev)

    # @mock.patch.object(TelnetAgent, "wait_no_parse")
    # @mock.patch.object(IxiaDevice, "send_command")
    # def test_is_port_capturing_ixia(self, mock_dev, mock_wait_no_parse):
    #     traffic_device = self.__test_setup(self.ixia_dev)
    #     assert isinstance(traffic_device, IxiaDevice)
    #     mock_wait_no_parse.return_value = ""
    #     mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 1}"
    #     port = "1.2.3"
    #     self.logger.log_info("Is Port Capturing called")
    #     duplex = traffic_device.is_port_capturing(port)
    #     self.assertEqual(duplex, False)
    #     mock_dev.return_value = "{clicks 2038344610} {seconds 1549308411} {status 1} {stopped 0}"
    #     duplex = traffic_device.is_port_capturing(port)
    #     self.assertEqual(duplex, True)
    #     self.__test_teardown(self.ixia_dev)

    # ##################################################################################################################
    #   Non-test helper functions.   ###################################################################################
    # ##################################################################################################################
    @staticmethod
    def __test_setup(device):
        TrafficGenerationTests.logger.log_info(("+---"*10) + "+")
        TrafficGenerationTests.logger.log_info("START="+TrafficGenerationTests.func_name())
        previous_frame = inspect.currentframe().f_back
        arg_vales = inspect.getargvalues(previous_frame)
        names = arg_vales.args
        values = arg_vales.locals
        index = 1
        while index < len(names):
            TrafficGenerationTests.logger.log_info(names[index] + "=" + str(values[names[index]]))
            index += 1
        return device

    @staticmethod
    def __test_teardown(device):
        TrafficGenerationTests.logger.log_info("END="+TrafficGenerationTests.func_name())
        return device

    @staticmethod
    def func_name():
        import traceback
        stack = traceback.extract_stack()
        filename, codeline, funcName, text = stack[-3]
        return funcName


if __name__ == '__main__':
    RobotUnitTest.main()
