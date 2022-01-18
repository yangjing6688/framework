from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDevice import OstinatoDevice
# from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingElement import TrafficGeneratingElement
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import DroneProxy

#############################################################
####  DO NOT USE THIS CLASS!!!!!
####  This is used solely to test new features on the Traffic Generating Devices.
####
#############################################################

class OstinatoDeviceUnitTestObject(object):

    """
    init function
    """
    def __init__(self, base_class_init=False):
        self.username = "aaron"
        self.vm = "127.0.0.1"
        # self.dev = "10.52.153.101"
        # self.dev = "10.52.186.120"

        # my typical vm
        self.dev = "10.59.4.245" # my typical
        # self.tx_port = "eth1"
        # self.rx_port = "eth2"
        self.tx_port = "lo" # my typical
        self.rx_port = "lo" # my typical

        # my typical vm
        self.dev = "10.59.4.253" # my typical
        # self.tx_port = "eth1"
        # self.rx_port = "eth2"
        self.tx_port = "eth1" # my typical
        self.rx_port = "eth1" # my typical

        # 4602node2_3 DUT
        # self.dev = "10.52.15.98"
        # self.dev_port = "9126"
        # self.tx_port = "enp0s8"
        # self.rx_port = "lo"

        # cori's vm
        # self.dev = "10.52.15.14"
        # self.dev_port = "49086"
        # self.tx_port = "enp0s8"
        # self.rx_port = "enp0s9"

        # dev = "10.52.10.62"
        # if base_class_init:
        #     self.dev_object = TrafficGeneratingElement("OSTINATO").traffic_device
        # else:
        self.dev_object = OstinatoDevice()


    def connect_and_take_ports(self):
        ostinatoDevice = self.dev_object
        assert isinstance(ostinatoDevice, OstinatoDevice)
        try:
            ostinatoDevice.connect(self.dev, self.dev_port)
        except AttributeError:
            ostinatoDevice.connect(self.dev)
        if ostinatoDevice.is_connected() and ostinatoDevice.is_initialized():
            port_send = self.tx_port
            port_rec = self.rx_port
            drone = ostinatoDevice.connection
            assert isinstance(drone, DroneProxy)

            port_send = self.tx_port
            port_rec  = self.rx_port
            ostinatoDevice.clear_capture_filters_and_triggers(port_send)
            ostinatoDevice.clear_capture_filters_and_triggers(port_rec)
            ostinatoDevice.clear_all_streams(port_send)
            ostinatoDevice.clear_all_streams(port_rec)
            return ostinatoDevice
        else:
            return False
