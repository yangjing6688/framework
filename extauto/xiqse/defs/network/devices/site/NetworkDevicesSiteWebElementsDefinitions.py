

class NetworkDevicesSiteWebElementsDefinitions:

    discover_tab = \
        {
            'DESC': 'Network> Devices> Site> Discover Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Discover"]',
            'wait_for': 10
        }

    actions_tab = \
        {
            'DESC': 'Network> Devices> Site> Actions Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Actions"]',
            'wait_for': 10
        }

    vrf_vlan_tab = \
        {
            'DESC': 'Network> Devices> Site> VRF/VLAN Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="VRF/VLAN"]',
            'wait_for': 10
        }

    topologies_tab = \
        {
            'DESC': 'Network> Devices> Site> Topologies Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Topologies"]',
            'wait_for': 10
        }

    services_tab = \
        {
            'DESC': 'Network> Devices> Site> Services Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Services"]',
            'wait_for': 10
        }

    port_templates_tab = \
        {
            'DESC': 'Network> Devices> Site> Port Templates Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Port Templates"]',
            'wait_for': 10
        }

    ztp_device_defaults_tab = \
        {
            'DESC': 'Network> Devices> Site> ZTP+ Device Default Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="ZTP+ Device Defaults"]',
            'wait_for': 10
        }

    endpoint_locations_tab = \
        {
            'DESC': 'Network> Devices> Site> Endpoint Locations Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Endpoint Locations"]',
            'wait_for': 10
        }

    analytics_tab = \
        {
            'DESC': 'Network> Devices> Site> Analytics Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Analytics"]',
            'wait_for': 10
        }

    custom_variables_tab = \
        {
            'DESC': 'Network> Devices> Site> Custom Variables Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Custom Variables"]',
            'wait_for': 10
        }

    discover_button = \
        {
            'DESC': 'Discover button',
            'XPATH': '//span[contains(@class, "x-btn-inner-blue-small") and text()="Discover"]/ancestor::a',
            'wait_for': 10
        }

    save_button = \
        {
            'DESC': 'Save button',
            'XPATH': '//span[contains(@class, "x-btn-inner-blue-small") and text()="Save"]/ancestor::a',
            'wait_for': 10
        }

    cancel_button = \
        {
            'DESC': 'Cancel button',
            'XPATH': '//span[contains(@class, "x-btn-inner-default-small") and text()="Cancel"]/ancestor::a',
            'wait_for': 10
        }

    site_unsaved_changes_dialog = \
        {
            'DESC': 'Site - Unsaved Changes dialog seen when moving away from a site with unsaved changes.',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]',
            'wait_for': 10
        }

    site_unsaved_changes_yes_button = \
        {
            'DESC': 'Yes button in the Site - Unsaved Changes dialog',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="Yes"]',
            'wait_for': 10
        }

    site_unsaved_changes_no_button = \
        {
            'DESC': 'No button in the Site - Unsaved Changes dialog',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="No"]',
            'wait_for': 10
        }

    site_unsaved_changes_cancel_button = \
        {
            'DESC': 'Cancel button in the Site - Unsaved Changes dialog',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="Cancel"]',
            'wait_for': 10
        }
