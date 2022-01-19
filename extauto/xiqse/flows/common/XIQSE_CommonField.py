# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.Utils import Utils


class XIQSE_CommonField:
    def __init__(self):
        self.utils = Utils()

    def xiqse_is_field_disabled(self, field_element):
        """
        - This keyword tests if the field is disabled.
        - It assumes the view is already open.
        - Keyword Usage
            - ``XIQSE is Field Disabled  field``
        :param field_element: field
        :return: True if disabled else None
        """
        if field_element:
            field_disabled = field_element.get_attribute("aria-disabled")
            self.utils.print_debug(f"Field Disabled Value: '{field_disabled}")
            if field_disabled == 'true':
                return True

    def xiqse_is_field_readonly(self, field_element):
        """
        - This keyword tests if the field is read only.
        - It assumes the view is already open.
        - Keyword Usage
            - ``XIQSE is Field Readonly  field``
        :param field_element: field
        :return: True if readonly else None
        """
        if field_element:
            field_readonly = field_element.get_attribute("aria-readonly")
            self.utils.print_debug(f"Field Read Only Value: '{field_readonly}")
            if field_readonly == 'true':
                return True
