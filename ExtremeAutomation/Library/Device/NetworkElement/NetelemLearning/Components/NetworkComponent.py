from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Component import Component


class NetworkComponent(Component):
    def __init__(self):
        super(NetworkComponent, self).__init__()

        self.sku = None
        self.firmware_version = None
        self.bootloader_version = None
        self.memory = None
        self.operating_system = None
        self.ports = []
        self.licenses = []

    def add_port(self, port):
        """
        This function adds the passed port object to the port list.
        """
        # Todo: Might want to do some verification on the port object that is passed in.
        self.ports.append(port)

    def add_license(self, _license):
        """
        This function adds the passed _license to the licenses list.
        """
        # Use _license to avoid shadowing built in "license".
        # Todo: Might want to do some verification on the license object that is passed in.
        self.licenses.append(_license)
