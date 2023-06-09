

class LicenseCommonWebElementsDefinitions:

    welcome_title = \
        {
            'DESC': 'Welcome Title',
            'XPATH': '//div[@id="xiqLicSetupDiv" or @id="licenseContentDiv"]/h1[text()="Welcome to ExtremeCloud IQ - Site Engine"]',
            
        }

    copyright_label = \
        {
            'DESC': 'Copyright Label',
            'XPATH': '//div[@class="flex-footer-item"]/span[contains(text(), "Copyright")]',
            
        }
