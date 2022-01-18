from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDevice import SpirentDevice
from ExtremeAutomation.Library.Logger.Logger import Logger

#############################################################
# ###  DO NOT USE THIS CLASS!!!!!
# ###  This is used solely to test new features on the Traffic Generating Devices.
# ###
#############################################################


class SpirentDeviceUnitTestObject(object):
    def __init__(self):
        self.username = "aaron"
        self.dev = "10.69.11.5"
        self.vm = "127.0.0.1"
        self.vm_port = 5679
        self.tx_port = "2/1"
        self.rx_port = "2/2"
        self.dev_object = SpirentDevice()
        self.logger = Logger()

    def connect_and_take_ports(self):
        traffic_device = self.dev_object  # instantiate an Ixia Device
        assert isinstance(traffic_device, SpirentDevice)
        traffic_device.logger.console_level = Logger.DEBUG

        # connect to the Ixia_Device
        traffic_device.connect(self.vm, self.vm_port)
        # alternatively inline version
        traffic_device.tgen_debug = True
        ixia_ver = traffic_device.get_version().replace(" ", "")
        self.logger.log_info(ixia_ver)
        # traffic_device.tgen_debug = True
        if traffic_device.is_connected() and traffic_device.is_initialized():
            traffic_device.take_port_ownership(self.dev, self.username, [self.tx_port, self.rx_port], True)
            # traffic_device.take_port_ownership(self.dev, self.username, self.tx_port, True)
            # traffic_device.take_port_ownership(self.dev, self.username, self.rx_port, True)

            # traffic_device.tgen_debug = False

            self.logger.log_info("clear the statics of ports " + self.tx_port + " and " + self.rx_port + "\n")
            traffic_device.clear_statistics_and_filters(self.tx_port)
            traffic_device.clear_statistics_and_filters(self.rx_port)
            return traffic_device
        else:
            return False
