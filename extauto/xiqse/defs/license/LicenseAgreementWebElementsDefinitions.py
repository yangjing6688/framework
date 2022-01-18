

class LicenseAgreementWebElementsDefinitions:

    license_agreement_title = \
        {
            'DESC': 'License Agreement Title',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]/h2[text()="License Agreement"]',
            'wait_for': 10
        }

    license_agreement_text_box = \
        {
            'DESC': 'License Agreement Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]/textarea[@class="licenseAgreementDiv"]',
            'wait_for': 10
        }

    license_accept_checkbox = \
        {
            'DESC': 'Accept License Agreement Checkbox',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-checkbox"]/input',
            'wait_for': 10
        }

    license_next_button = \
        {
            'DESC': 'License Agreement Next Button',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="licenseAgreement"]/input[@name="licenseAccepted"]',
            'wait_for': 10
        }
