from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxLoadDevice import IxLoadDevice
from ExtremeAutomation.Library.Logger.Logger import Logger

#############################################################
# ###  DO NOT USE THIS CLASS!!!!!
# ###  This is used solely to test new features on the Traffic Generating Devices.
# ###
#############################################################


class IxiaLoadDeviceUnitTestObject(object):
    def __init__(self):
        self.username = "aaron"
        self.ixNetworkIp = "10.52.2.167"
        self.vm_port = 5680

        # # my old ports on 189
        # self.dev = "10.52.2.189"
        # self.vm = "10.52.2.167"
        # self.tx_port = "1/1"
        # self.rx_port = "1/2"
        #
        # # from corey this is the socket listener
        # self.dev = "10.52.2.189"
        # self.vm = "10.52.2.167"
        # self.tx_port = "11/13"
        # self.rx_port = "11/14"

        # steve mays IxLoad
        self.dev = "10.52.3.48"
        self.vm = "10.59.22.11"
        self.tx_port = "9/13"
        self.rx_port = "9/16"

        self.dev_object = IxLoadDevice()

    def connect_and_take_ports(self):

        traffic_device = self.dev_object  # instantiate an Ixia Device
        traffic_device.logger.console_level = Logger.DEBUG

        # connect to the Ixia_Device
        traffic_device.connect(self.vm, self.vm_port)
        # alternatively inline version
        traffic_device.tgen_debug = True
        return traffic_device
