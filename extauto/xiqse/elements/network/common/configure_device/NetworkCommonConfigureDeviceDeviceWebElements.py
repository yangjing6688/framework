# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.common.configure_device.NetworkCommonConfigureDeviceDeviceWebElementsDefinitions import NetworkCommonConfigureDeviceDeviceWebElementsDefinitions


class NetworkCommonConfigureDeviceDeviceWebElements(NetworkCommonConfigureDeviceDeviceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Device Tab Fields
    def get_system_name_field(self):
        """
        :return: 'System Name' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.system_name_field)

    def get_contact_field(self):
        """
        :return: 'Contact' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.contact_field)

    def get_location_field(self):
        """
        :return: 'Location' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.location_field)

    def get_admin_profile_dropdown(self):
        """
        :return: 'Administration Profile' dropdown in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.admin_profile_dropdown)

    def get_replacement_serial_field(self):
        """
        :return: 'Replacement Serial Number' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.replacement_serial_field)

    def get_remove_from_service_checkbox(self):
        """
        :return: 'Remove from Service' checkbox in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.remove_from_service_checkbox)

    def get_use_default_webview_url_checkbox(self):
        """
        :return: 'Use Default WebView URL' checkbox in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.use_default_webview_url_checkbox)

    def get_webview_url_field(self):
        """
        :return: 'WebView URL' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.webview_url_field)

    def get_default_site_dropdown(self):
        """
        :return: 'Default Site' dropdown in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.default_site_dropdown)

    def get_poll_group_dropdown(self):
        """
        :return: 'Poll Group' dropdown in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.poll_group_dropdown)

    def get_poll_type_dropdown(self):
        """
        :return: 'Poll Type' dropdown in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.poll_type_dropdown)

    def get_snmp_timeout_field(self):
        """
        :return: 'SNMP Timeout' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.snmp_timeout_field)

    def get_snmp_retries_field(self):
        """
        :return: 'SNMP Retries' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.snmp_retries_field)

    def get_topology_layer_dropdown(self):
        """
        :return: 'Topology Layer' dropdown in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.topology_layer_dropdown)

    def get_collection_mode_dropdown_trigger(self):
        """
        :return: 'Collection Mode' dropdown trigger arrow in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.collection_mode_dropdown_trigger)

    def get_collection_mode_dropdown(self):
        """
        :return: 'Collection Mode' dropdown in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.collection_mode_dropdown)

    def get_collection_interval_field(self):
        """
        :return: 'Collection Interval' field in the Configure Device dialog (Device tab)
        """
        return self.weh.get_element(self.collection_interval_field)
