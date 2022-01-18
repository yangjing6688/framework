import abc
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Logger.Logger import Logger


class NetworkEmulatingDevice(object, metaclass=abc.ABCMeta):
    def __init__(self):
        self.logger = Logger()
        self.connection = None

    @abc.abstractmethod
    def connect_network_generator(self, host, ixnetwork_ip, port=5678):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def init_network_generator_device(self):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def take_network_generator_port_ownership(self, host, user, port_string, reset=False):
        return self.logger.log_unimplemented_method()


class NetworkEmulatingDeviceConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
