

class AdminDeviceTypesWebElementsDefinitions:

    detection_and_profiling_tab = \
        {
            'DESC': 'Detection and Profiling Tab on the Administration> Device Types page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Detection and Profiling" and contains(@class, "x-tab-inner")]',
            'wait_for': 10
        }

    mac_oui_vendors_tab = \
        {
            'DESC': 'MAC OUI Vendors Tab on the Administration> Device Types page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="MAC OUI Vendors" and contains(@class, "x-tab-inner")]',
            'wait_for': 10
        }
