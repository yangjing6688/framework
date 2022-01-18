# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#


class NetworkCommonConfigureDeviceAnnotationsWebElementsDefinitions:

    # Device Annotation Tab Fields
    nickname_field = \
        {
            'DESC': 'Nickname field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="nickname"]',
            'wait_for': 5
        }

    asset_tag_field = \
        {
            'DESC': 'Asset Tag field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="assetTag"]',
            'wait_for': 5
        }

    user_data_1_field = \
        {
            'DESC': 'User Data 1 field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData1"]',
            'wait_for': 5
        }

    user_data_2_field = \
        {
            'DESC': 'User Data 2 field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData2"]',
            'wait_for': 5
        }

    user_data_3_field = \
        {
            'DESC': 'User Data 3 field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData3"]',
            'wait_for': 5
        }

    user_data_4_field = \
        {
            'DESC': 'User Data 4 field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData4"]',
            'wait_for': 5
        }

    note_field = \
        {
            'DESC': 'Notes field on the Device Annotation tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//textarea[@name="note"]',
            'wait_for': 5
        }
