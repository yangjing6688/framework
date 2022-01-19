# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.WebElementHandler import *
from xiqse.defs.network.common.configure_device.NetworkCommonConfigureDeviceActionsWebElementsDefinitions import *


class NetworkCommonConfigureDeviceActionsWebElements(NetworkCommonConfigureDeviceActionsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_trap_receiver_cb(self):
        """
        :return: Add Trap Receiver checkbox element
        """
        return self.weh.get_element(self.add_trap_receiver_cb)

    def get_add_syslog_receiver_cb(self):
        """
        :return: Add Syslog Receiver checkbox element
        """
        return self.weh.get_element(self.add_syslog_receiver_cb)

    def get_add_to_archive_cb(self):
        """
        :return: Add to Archive checkbox element
        """
        return self.weh.get_element(self.add_to_archive_cb)

    def get_add_to_map_cb(self):
        """
        :return: Add to Map checkbox element
        """
        return self.weh.get_element(self.add_to_map_cb)

    def get_collection_mode_dropdown(self):
        """
        :return: Collection Mode dropdown element
        """
        return self.weh.get_element(self.collection_mode_dropdown)

    def get_collection_interval_dropdown(self):
        """
        :return: Collection Interval dropdown element
        """
        return self.weh.get_element(self.collection_interval_dropdown)

    def get_map_name_dropdown(self):
        """
        :return: Map Name dropdown element
        """
        return self.weh.get_element(self.map_name_dropdown)
