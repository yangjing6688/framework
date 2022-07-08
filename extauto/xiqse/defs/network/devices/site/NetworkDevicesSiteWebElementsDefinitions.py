

class NetworkDevicesSiteWebElementsDefinitions:

    discover_tab = \
        {
            'DESC': 'Network> Devices> Site> Discover Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Discover"]',
            
        }

    actions_tab = \
        {
            'DESC': 'Network> Devices> Site> Actions Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Actions"]',
            
        }

    vrf_vlan_tab = \
        {
            'DESC': 'Network> Devices> Site> VRF/VLAN Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="VRF/VLAN"]',
            
        }

    topologies_tab = \
        {
            'DESC': 'Network> Devices> Site> Topologies Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Topologies"]',
            
        }

    services_tab = \
        {
            'DESC': 'Network> Devices> Site> Services Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Services"]',
            
        }

    port_templates_tab = \
        {
            'DESC': 'Network> Devices> Site> Port Templates Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Port Templates"]',
            
        }

    ztp_device_defaults_tab = \
        {
            'DESC': 'Network> Devices> Site> ZTP+ Device Default Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="ZTP+ Device Defaults"]',
            
        }

    endpoint_locations_tab = \
        {
            'DESC': 'Network> Devices> Site> Endpoint Locations Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Endpoint Locations"]',
            
        }

    analytics_tab = \
        {
            'DESC': 'Network> Devices> Site> Analytics Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Analytics"]',
            
        }

    custom_variables_tab = \
        {
            'DESC': 'Network> Devices> Site> Custom Variables Tab',
            'XPATH': '//div[contains(@id, "siteTabPanel")]//span[contains(@class, "x-tab-inner-default") and text()="Custom Variables"]',
            
        }

    discover_button = \
        {
            'DESC': 'Discover button',
            'XPATH': '//span[contains(@class, "x-btn-inner-blue-small") and text()="Discover"]/ancestor::a',
            
        }

    save_button = \
        {
            'DESC': 'Save button',
            'XPATH': '//span[contains(@class, "x-btn-inner-blue-small") and text()="Save"]/ancestor::a',
            
        }

    cancel_button = \
        {
            'DESC': 'Cancel button',
            'XPATH': '//span[contains(@class, "x-btn-inner-default-small") and text()="Cancel"]/ancestor::a',
            
        }

    site_unsaved_changes_dialog = \
        {
            'DESC': 'Site - Unsaved Changes dialog seen when moving away from a site with unsaved changes.',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]',
            
        }

    site_unsaved_changes_yes_button = \
        {
            'DESC': 'Yes button in the Site - Unsaved Changes dialog',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="Yes"]',
            
        }

    site_unsaved_changes_no_button = \
        {
            'DESC': 'No button in the Site - Unsaved Changes dialog',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="No"]',
            
        }

    site_unsaved_changes_cancel_button = \
        {
            'DESC': 'Cancel button in the Site - Unsaved Changes dialog',
            'XPATH': '//div[text()="Site - Unsaved Changes"]/ancestor::div[contains(@class, "x-message-box")]//span[text()="Cancel"]',
            
        }
