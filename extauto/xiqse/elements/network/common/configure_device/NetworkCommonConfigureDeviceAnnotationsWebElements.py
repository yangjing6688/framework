# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.common.configure_device.NetworkCommonConfigureDeviceAnnotationsWebElementsDefinitions import NetworkCommonConfigureDeviceAnnotationsWebElementsDefinitions


class NetworkCommonConfigureDeviceAnnotationsWebElements(NetworkCommonConfigureDeviceAnnotationsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Device Annotation Tab Fields
    def get_nickname_field(self):
        """
        :return: 'Nickname' field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.nickname_field)

    def get_asset_tag_field(self):
        """
        :return: 'Asset Tag' field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.asset_tag_field)

    def get_user_data_1_field(self):
        """
        :return: 'User Data 1' field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.user_data_1_field)

    def get_user_data_2_field(self):
        """
        :return: 'User Data 2 field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.user_data_2_field)

    def get_user_data_3_field(self):
        """
        :return: 'User Data 3' field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.user_data_3_field)

    def get_user_data_4_field(self):
        """
        :return: 'User Data 4' field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.user_data_4_field)

    def get_note_field(self):
        """
        :return: 'Note' field in the Configure Device dialog (Device Annotation tab)
        """
        return self.weh.get_element(self.note_field)
