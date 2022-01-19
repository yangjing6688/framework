# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from common.WebElementHandler import *
from xiqse.defs.network.common.NetworkCommonConfigureDeviceWebElementsDefinitions import *


class NetworkCommonConfigureDeviceWebElements(NetworkCommonConfigureDeviceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Tabs
    def get_device_tab(self):
        """
        :return: 'Device' tab in the Configure Device dialog
        """
        return self.weh.get_element(self.device_tab)

    def get_device_annotation_tab(self):
        """
        :return: 'Device Annotation' tab in the Configure Device dialog
        """
        return self.weh.get_element(self.device_annotation_tab)

    def get_vlan_definitions_tab(self):
        """
        :return: 'VLAN Definitions' tab in the Configure Device dialog
        """
        return self.weh.get_element(self.vlan_definitions_tab)

    def get_ports_tab(self):
        """
        :return: 'Ports' tab in the Configure Device dialog
        """
        return self.weh.get_element(self.ports_tab)

    def get_ztp_plus_device_settings_tab(self):
        """
        :return: 'ZTP+ Device Settings' tab in the Configure Device dialog
        """
        return self.weh.get_element(self.ztp_plus_device_settings_tab)

    def get_vendor_profile_tab(self):
        """
        :return: 'Vendor Profile' tab in the Configure Device dialog
        """
        return self.weh.get_element(self.vendor_profile_tab)

    # Action Buttons
    def get_cancel_button(self):
        """
        :return: 'Cancel' button in the Configure Device dialog
        """
        return self.weh.get_element(self.cancel_btn)

    def get_save_button(self):
        """
        :return: 'Save' button in the Configure Device dialog
        """
        return self.weh.get_element(self.save_btn)

    def get_sync_from_site_button(self):
        """
        :return: 'Sync from Site' button in the Configure Device dialog
        """
        return self.weh.get_element(self.sync_from_site_btn)

    def get_enforce_preview_button(self):
        """
        :return: 'Enforce Preview' button in the Configure Device dialog
        """
        return self.weh.get_element(self.enforce_preview_btn)

    def get_reload_device_button(self):
        """
        :return: 'Reload Device' button in the Configure Device dialog
        """
        return self.weh.get_element(self.reload_device_btn)
