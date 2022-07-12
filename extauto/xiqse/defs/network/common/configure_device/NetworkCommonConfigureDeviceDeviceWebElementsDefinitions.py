# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#


class NetworkCommonConfigureDeviceDeviceWebElementsDefinitions:

    # Device Tab Fields
    system_name_field = \
        {
            'DESC': 'System Name field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="sysName"]',
            'wait_for': 5
        }

    contact_field = \
        {
            'DESC': 'Contact field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="sysContact"]',
            'wait_for': 5
        }

    location_field = \
        {
            'DESC': 'Location field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="sysLocation"]',
            'wait_for': 5
        }

    admin_profile_dropdown = \
        {
            'DESC': 'Administration Profile dropdown on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="profileName"]',
            
        }

    replacement_serial_field = \
        {
            'DESC': 'Replacement Serial Number field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="replacementSerialNumber"]',
            'wait_for': 5
        }

    remove_from_service_checkbox = \
        {
            'DESC': 'Remove From Service check box on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="outOfService"]',
            
        }

    use_default_webview_url_checkbox = \
        {
            'DESC': 'Use Default WebView URL check box on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="defaultWebViewUrl"]',
            
        }

    webview_url_field = \
        {
            'DESC': 'WebView URL field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="deviceWebViewUrl"]',
            'wait_for': 5
        }

    default_site_dropdown = \
        {
            'DESC': 'Default Site dropdown on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="defaultSiteId"]',
            
        }

    poll_group_dropdown = \
        {
            'DESC': 'Poll Group dropdown on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="pollGroup"]',
            
        }

    poll_type_dropdown = \
        {
            'DESC': 'Poll Type dropdown on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="pollType"]',
            
        }

    snmp_timeout_field = \
        {
            'DESC': 'SNMP Timeout field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="snmpTimeout"]',
            'wait_for': 5
        }

    snmp_retries_field = \
        {
            'DESC': 'SNMP Retries field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="snmpRetry"]',
            'wait_for': 5
        }

    topology_layer_dropdown = \
        {
            'DESC': 'Topology Layer dropdown on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="topologyRole"]',
            
        }

    collection_mode_dropdown_trigger = \
        {
            'DESC': 'Collection Mode dropdown trigger arrow on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="collectionMode"]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

    collection_mode_dropdown = \
        {
            'DESC': 'Collection Mode dropdown on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="collectionMode"]',
            
        }

    collection_interval_field = \
        {
            'DESC': 'Collection Interval field on the Device tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceUserDataPanel")]//input[@name="collectionInterval"]',
            'wait_for': 5
        }
