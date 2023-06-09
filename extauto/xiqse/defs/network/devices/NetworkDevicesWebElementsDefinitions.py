

class NetworkDevicesWebElementsDefinitions:

    devices_tab = \
        {
            'DESC': 'Network> Devices> Devices Tab',
            'XPATH': '//div[contains(@id, "networkDeviceView")]//span[text()="Devices" and contains(@class, "x-tab-inner-default")]',
            
        }

    site_tab = \
        {
            'DESC': 'Network> Devices> Site Tab (where Site is the name of the site)',
            'XPATH': '//div[contains(@id, "networkDeviceView")]//span[contains(@class, "x-tab-inner-default") and text()="${element_name}"]',
            
        }

    site_summary_tab = \
        {
            'DESC': 'Network> Devices> Site Summary Tab',
            'XPATH': '//div[contains(@id, "networkDeviceView")]//span[text()="Site Summary" and contains(@class, "x-tab-inner-default")]',
            
        }

    endpoint_locations_tab = \
        {
            'DESC': 'Network> Devices> Endpoint Locations Tab',
            'XPATH': '//div[contains(@id, "networkDeviceView")]//span[text()="Endpoint Locations" and contains(@class, "x-tab-inner-default")]',
            
        }

    flexreports_tab = \
        {
            'DESC': 'Network> Devices> FlexReports Tab',
            'XPATH': '//div[contains(@id, "networkDeviceView")]//span[text()="FlexReports" and contains(@class, "x-tab-inner-default")]',
            
        }
