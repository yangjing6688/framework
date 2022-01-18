

class NetworkDevicesSiteActionsWebElementsDefinitions:

    automatically_add_devices_checkbox = \
        {
            'DESC': 'Automatically Add Devices Checkbox',
            'XPATH': '//input[@name="addToNetSight"]',
            'wait_for': 10
        }

    add_trap_receiver_checkbox = \
        {
            'DESC': 'Add Trap Receiver Checkbox',
            'XPATH': '//input[@name="addTrapServer"]',
            'wait_for': 10
        }

    add_syslog_receiver_checkbox = \
        {
            'DESC': 'Add syslog Receiver Checkbox',
            'XPATH': '//input[@name="addSyslogServer"]',
            'wait_for': 10
        }

    add_to_archive_checkbox = \
        {
            'DESC': 'Add to Archive Checkbox',
            'XPATH': '//input[@name="addToSiteArchive"]',
            'wait_for': 10
        }
