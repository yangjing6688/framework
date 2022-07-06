

class LicenseAgreementWebElementsDefinitions:

    license_agreement_title = \
        {
            'DESC': 'License Agreement Title',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]/h2[text()="License Agreement"]',
            
        }

    license_agreement_text_box = \
        {
            'DESC': 'License Agreement Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]/textarea[@class="licenseAgreementDiv"]',
            
        }

    license_accept_checkbox = \
        {
            'DESC': 'Accept License Agreement Checkbox',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-checkbox"]/input',
            
        }

    license_next_button = \
        {
            'DESC': 'License Agreement Next Button',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="licenseAgreement"]/input[@name="licenseAccepted"]',
            
        }
