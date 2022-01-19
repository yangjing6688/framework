# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#


class NetworkCommonConfigureDeviceWebElementsDefinitions:

    # Tabs
    device_tab = \
        {
            'DESC': 'Device Tab in the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Device"]',
            'wait_for': 10
        }

    device_annotation_tab = \
        {
            'DESC': 'Device Annotation Tab in the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Device Annotation"]',
            'wait_for': 10
        }

    vlan_definitions_tab = \
        {
            'DESC': 'VLAN Definitions Tab in the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="VLAN Definitions"]',
            'wait_for': 10
        }

    ports_tab = \
        {
            'DESC': 'Ports Tab in the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Ports"]',
            'wait_for': 10
        }

    ztp_plus_device_settings_tab = \
        {
            'DESC': 'ZTP+ Device Settings Tab in the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="ZTP+ Device Settings"]',
            'wait_for': 10
        }

    vendor_profile_tab = \
        {
            'DESC': 'Vendor Profile Tab in the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Vendor Profile"]',
            'wait_for': 10
        }

    # Action Buttons
    cancel_btn = \
        {
            'DESC': 'Cancel Button for the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Cancel"]/ancestor::a',
            'wait_for': 5
        }

    save_btn = \
        {
            'DESC': 'Save Button for the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Save"]/ancestor::a',
            'wait_for': 5
        }

    sync_from_site_btn = \
        {
            'DESC': 'Sync from Site Button for the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Sync from Site"]/ancestor::a',
            'wait_for': 5
        }

    enforce_preview_btn = \
        {
            'DESC': 'Enforce Preview Button for the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Enforce Preview..."]/ancestor::a',
            'wait_for': 5
        }

    reload_device_btn = \
        {
            'DESC': 'Reload Device Button for the Configure Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Reload Device"]/ancestor::a',
            'wait_for': 5
        }
