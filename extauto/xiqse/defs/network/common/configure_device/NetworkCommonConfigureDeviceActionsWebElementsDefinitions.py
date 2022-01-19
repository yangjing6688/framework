# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#


class NetworkCommonConfigureDeviceActionsWebElementsDefinitions:

    # Add Device Actions Tab Fields
    add_trap_receiver_cb = \
        {
            'DESC': 'Add Trap Receiver checkbox in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="addTrapServer"]',
            'wait_for': 5
        }

    add_syslog_receiver_cb = \
        {
            'DESC': 'Add Syslog Receiver checkbox in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="addSyslogServer"]',
            'wait_for': 5
        }

    add_to_archive_cb = \
        {
            'DESC': 'Add to Archive checkbox in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="addToSiteArchive"]',
            'wait_for': 5
        }

    add_to_map_cb = \
        {
            'DESC': 'Add to Map checkbox in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="addToSiteMap"]',
            'wait_for': 5
        }

    collection_mode_dropdown = \
        {
            'DESC': 'Collection Mode dropdown menu in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="addCollectionMode"]',
            'wait_for': 5
        }

    collection_interval_dropdown = \
        {
            'DESC': 'Collection Interval dropdown menu in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="addCollectionInterval"]',
            'wait_for': 5
        }

    map_name_dropdown = \
        {
            'DESC': 'Map Name dropdown menu in Configure Device > Add Device Actions panel',
            'XPATH': '//input[@name="mapId"]',
            'wait_for': 5
        }
