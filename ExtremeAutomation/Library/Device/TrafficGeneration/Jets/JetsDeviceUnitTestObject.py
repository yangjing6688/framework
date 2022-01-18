from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDevice import JetsDevice
from ExtremeAutomation.Library.Logger.Logger import Logger

#############################################################
# ###  DO NOT USE THIS CLASS!!!!!
# ###  This is used solely to test new features on the Traffic Generating Devices.
# ###
#############################################################


class JetsDeviceUnitTestObject(object):
    def __init__(self):
        self.username = "root"
        self.password = "PASprt86"
        # self.vm = "192.168.56.15"
        # self.dev = "192.168.56.15"
        # self.tx_port = "eth6" # my typical
        # self.rx_port = "eth7" # my typical
        #
        # # my typical vm
        # self.vm = "192.168.11.15"
        # self.dev = "192.168.11.15"
        # self.tx_port = "eth6" # my typical
        # self.rx_port = "eth7" # my typical

        # sandeeps jets vm on 10.148.35.92
        # self.vm = "10.148.35.92"
        # self.dev = "10.148.35.92"

        # jets vm on 10.59.4.249

        # # jets 6.0 centos
        # self.vm = "10.59.4.253"
        # self.dev = "10.59.4.253"
        # self.tx_port = "eth1"  # my typical
        # self.rx_port = "eth4"  # my typical
        # jets 7.6 centos
        self.vm = "10.59.5.61"
        self.dev = "10.59.5.61"
        self.tx_port = "ens161"  # my typical
        self.rx_port = "ens192"  # my typical
        #
        # # hets 6.5 centos
        # self.vm = "10.59.5.50"
        # self.dev = "10.59.5.50"
        # self.tx_port = "eth2"  # my typical
        # self.rx_port = "eth5"  # my typical
        self.ixNetworkIp = ""
        self.vm_port = 22

        self.dev_object = JetsDevice()

    def connect_and_take_ports(self):
        jets_device = self.dev_object
        jets_device.logger.console_level = Logger.DEBUG
        assert isinstance(jets_device, JetsDevice)
        jets_device.set_username(self.username)
        jets_device.set_password(self.password)
        # jets_device.set_view_tag("blah")
        # jets_device.set_jets_directory("/root/")
        try:
            jets_device.connect(self.dev, self.dev_port)
        except AttributeError:
            jets_device.connect(self.dev)
        if jets_device.is_connected() and jets_device.is_initialized():
            port_send = self.tx_port
            port_rec = self.rx_port
            jets_device.take_port_ownership(jets_device.get_host_name(), jets_device.get_username(), port_send)
            jets_device.take_port_ownership(jets_device.get_host_name(), jets_device.get_username(), port_rec)

            # jets_device.clear_capture_filters_and_triggers(port_send)
            # jets_device.clear_capture_filters_and_triggers(port_rec)
            # jets_device.clear_all_streams(port_send)
            # jets_device.clear_all_streams(port_rec)
            return jets_device
        else:
            return False
