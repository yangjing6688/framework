from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.device_types.AdminDeviceTypesWebElementsDefinitions import AdminDeviceTypesWebElementsDefinitions


class AdminDeviceTypesWebElements(AdminDeviceTypesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_detection_and_profiling_tab(self):
        """
        :return: Detection and Profiling tab element
        """
        return self.weh.get_element(self.detection_and_profiling_tab)

    def get_mac_oui_vendors_tab(self):
        """
        :return: MAC OUI Vendors tab element
        """
        return self.weh.get_element(self.mac_oui_vendors_tab)
