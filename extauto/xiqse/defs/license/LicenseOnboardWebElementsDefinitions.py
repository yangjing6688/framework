

class LicenseOnboardWebElementsDefinitions:

    onboard_title = \
        {
            'DESC': 'Onboard Title',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]/h2[text()="Onboard to ExtremeCloud IQ"]',
            
        }

    advanced_link = \
        {
            'DESC': 'Advanced Link',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//a[@id="xiqAdvancedLink"]',
            
        }

    hide_advanced_link = \
        {
            'DESC': 'Hide Advanced Link',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//a[@id="xiqAdvancedLink" and text()="Hide Advanced"]',
            
        }

    email_field = \
        {
            'DESC': 'Email Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-textbox"]/input[@name="xiq_username"]',
            
        }

    password_field = \
        {
            'DESC': 'Password Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-textbox"]/input[@name="xiq_password"]',
            
        }

    viq_id_field = \
        {
            'DESC': 'VIQ ID Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="xiq_viqid"]',
            
        }

    specify_proxy_checkbox = \
        {
            'DESC': 'Specify Proxy Server Checkbox',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-checkbox"]/input[@name="isProxyServer"]',
            
        }

    proxy_server_field = \
        {
            'DESC': 'Proxy Server Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="proxy_server"]',
            
        }

    port_id_field = \
        {
            'DESC': 'Port ID Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="port_id"]',
            
        }

    proxy_auth_checkbox = \
        {
            'DESC': 'Proxy Authentication Checkbox',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-checkbox"]/input[@name="isProxyAuth"]',
            
        }

    proxy_username_field = \
        {
            'DESC': 'Proxy Username Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="proxy_username"]',
            
        }

    proxy_password_field = \
        {
            'DESC': 'Proxy Password Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="proxy_password"]',
            
        }

    serial_label = \
        {
            'DESC': 'Serial Number Label',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/p[contains(text(), "XIQSE") and contains(text(), "S/N")]',
            
        }

    onboard_button = \
        {
            'DESC': 'Onboard Button',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//input[@id="xiqOnboardButton"]',
            
        }

    error_label = \
        {
            'DESC': 'Error Label',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-error-block"]',
            
        }
