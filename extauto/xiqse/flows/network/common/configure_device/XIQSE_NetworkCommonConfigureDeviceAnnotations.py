# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.common.configure_device.NetworkCommonConfigureDeviceAnnotationsWebElements import NetworkCommonConfigureDeviceAnnotationsWebElements
from xiqse.flows.network.common.XIQSE_NetworkCommonConfigureDevice import XIQSE_NetworkCommonConfigureDevice


class XIQSE_NetworkCommonConfigureDeviceAnnotations(NetworkCommonConfigureDeviceAnnotationsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.cfg_dev = XIQSE_NetworkCommonConfigureDevice()

    # DEVICE ANNOTATIONS TAB
    def xiqse_configure_device_dialog_set_nickname(self, the_value):
        """
        - This keyword sets the Nickname field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set Nickname  NICKNAME``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_nickname_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Nickname field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the Nickname field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_asset_tag(self, the_value):
        """
        - This keyword sets the Asset Tag field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set Asset Tag  ASSET_TAG``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_asset_tag_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Asset Tag field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the Asset Tag field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_user_data_1(self, the_value):
        """
        - This keyword sets the User Data 1 field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set User Data 1  USER_DATA``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_user_data_1_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the User Data 1 field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the User Data 1 field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_user_data_2(self, the_value):
        """
        - This keyword sets the User Data 2 field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set User Data 2  USER_DATA``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_user_data_2_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the User Data 2 field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the User Data 2 field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_user_data_3(self, the_value):
        """
        - This keyword sets the User Data 3 field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set User Data 3  USER_DATA``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_user_data_3_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the User Data 3 field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the User Data 3 field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_user_data_4(self, the_value):
        """
        - This keyword sets the User Data 4 field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set User Data 4  USER_DATA``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_user_data_4_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the User Data 4 field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the User Data 4 field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_note(self, the_value):
        """
        - This keyword sets the Note field in the Configure Device dialog (Device Annotation tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Dialog Set Note  NOTE``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_note_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Note field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to find the Note field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_set_annotation_tab_values(self, nickname=None, asset_tag=None, ud1=None, ud2=None,
                                                         ud3=None, ud4=None, note=None):
        """
        - This keyword sets the fields on the Device Annotation tab in the Configure Device dialog.
        - It assumes the dialog is already open.
        - Keyword Usage:
         - ``XIQSE Configure Device Set Annotation Tab Values    nickname=MY_NICKNAME  note=MY NOTE``

        :param nickname:   Value to enter into the Nickname field
        :param asset_tag:  Value to enter into the Asset Tag field
        :param ud1:        Value to enter into the User Data 1 field
        :param ud2:        Value to enter into the User Data 2 field
        :param ud3:        Value to enter into the User Data 3 field
        :param ud4:        Value to enter into the User Data 4 field
        :param note:       Value to enter into the Note field
        :return: 1 if action is successful, else -1
        """
        ret_val = 1

        if self.cfg_dev.xiqse_configure_device_dialog_select_tab("Device Annotation") == 1:
            if nickname:
                nn_result = self.xiqse_configure_device_dialog_set_nickname(nickname)
                if nn_result == -1:
                    ret_val = -1
            if asset_tag:
                at_result = self.xiqse_configure_device_dialog_set_asset_tag(asset_tag)
                if at_result == -1:
                    ret_val = -1
            if ud1:
                ud_result = self.xiqse_configure_device_dialog_set_user_data_1(ud1)
                if ud_result == -1:
                    ret_val = -1
            if ud2:
                ud_result = self.xiqse_configure_device_dialog_set_user_data_2(ud2)
                if ud_result == -1:
                    ret_val = -1
            if ud3:
                ud_result = self.xiqse_configure_device_dialog_set_user_data_3(ud3)
                if ud_result == -1:
                    ret_val = -1
            if ud4:
                ud_result = self.xiqse_configure_device_dialog_set_user_data_4(ud4)
                if ud_result == -1:
                    ret_val = -1
            if note:
                note_result = self.xiqse_configure_device_dialog_set_note(note)
                if note_result == -1:
                    ret_val = -1
        else:
            ret_val = -1

        return ret_val
