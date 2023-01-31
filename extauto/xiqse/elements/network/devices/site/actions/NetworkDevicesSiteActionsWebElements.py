from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.devices.site.actions.NetworkDevicesSiteActionsWebElementsDefinitions import NetworkDevicesSiteActionsWebElementsDefinitions


class NetworkDevicesSiteActionsWebElements(NetworkDevicesSiteActionsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_automatically_add_devices_checkbox(self):
        """
        :return: 'Automatically Add Devices' checkbox on the Network> Devices> Site> Actions page
        """
        return self.weh.get_element(self.automatically_add_devices_checkbox)

    def get_add_trap_receiver_checkbox(self):
        """
        :return: 'Add Trap Receiver' checkbox on the Network> Devices> Site> Actions page
        """
        return self.weh.get_element(self.add_trap_receiver_checkbox)

    def get_add_syslog_receiver_checkbox(self):
        """
        :return: 'Add Syslog Receiver' checkbox on the Network> Devices> Site> Actions page
        """
        return self.weh.get_element(self.add_syslog_receiver_checkbox)

    def get_add_to_archive_checkbox(self):
        """
        :return: 'Add to Archive' checkbox on the Network> Devices> Site> Actions page
        """
        return self.weh.get_element(self.add_to_archive_checkbox)
