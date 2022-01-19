

class LicenseDeploymentWebElementsDefinitions:

    info_label = \
        {
            'DESC': 'Information Label Stating to Select Deployment Model',
            'XPATH': '//div[@id="xiqLicSetupDiv" or @id="licenseContentDiv"]//div[@class="xiq-info-block" and contains(text(), "Select the deployment model")]',
            'wait_for': 10
        }

    onboard_radio = \
        {
            'DESC': 'Radio button for Onboard to ExtremeCloud IQ',
            'XPATH': '//div[@id="xiqLicSetupDiv" or @id="licenseContentDiv"]//form[@class="licenseAgreementForm"]//input[@id="auto"]',
            'wait_for': 10
        }

    airgap_radio = \
        {
            'DESC': 'Radio button for Enter Entitlements for air gapped ExtremeCloud IQ - Site Engine',
            'XPATH': '//div[@id="xiqLicSetupDiv" or @id="licenseContentDiv"]//form[@class="licenseAgreementForm"]//input[@id="airgap"]',
            'wait_for': 10
        }

    next_button = \
        {
            'DESC': 'License Deployment Next Button',
            'XPATH': '//div[@id="xiqLicSetupDiv" or @id="licenseContentDiv"]//form[@class="licenseAgreementForm"]//input[@type="submit"]',
            'wait_for': 10
        }
