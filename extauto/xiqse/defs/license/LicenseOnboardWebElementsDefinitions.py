

class LicenseOnboardWebElementsDefinitions:

    onboard_title = \
        {
            'DESC': 'Onboard Title',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]/h2[text()="Onboard to ExtremeCloud IQ"]',
            'wait_for': 10
        }

    advanced_link = \
        {
            'DESC': 'Advanced Link',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//a[@id="xiqAdvancedLink"]',
            'wait_for': 10
        }

    hide_advanced_link = \
        {
            'DESC': 'Hide Advanced Link',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//a[@id="xiqAdvancedLink" and text()="Hide Advanced"]',
            'wait_for': 10
        }

    email_field = \
        {
            'DESC': 'Email Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-textbox"]/input[@name="xiq_username"]',
            'wait_for': 10
        }

    password_field = \
        {
            'DESC': 'Password Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-textbox"]/input[@name="xiq_password"]',
            'wait_for': 10
        }

    viq_id_field = \
        {
            'DESC': 'VIQ ID Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="xiq_viqid"]',
            'wait_for': 10
        }

    specify_proxy_checkbox = \
        {
            'DESC': 'Specify Proxy Server Checkbox',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-checkbox"]/input[@name="isProxyServer"]',
            'wait_for': 10
        }

    proxy_server_field = \
        {
            'DESC': 'Proxy Server Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="proxy_server"]',
            'wait_for': 10
        }

    port_id_field = \
        {
            'DESC': 'Port ID Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="port_id"]',
            'wait_for': 10
        }

    proxy_auth_checkbox = \
        {
            'DESC': 'Proxy Authentication Checkbox',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-checkbox"]/input[@name="isProxyAuth"]',
            'wait_for': 10
        }

    proxy_username_field = \
        {
            'DESC': 'Proxy Username Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="proxy_username"]',
            'wait_for': 10
        }

    proxy_password_field = \
        {
            'DESC': 'Proxy Password Field Text Box',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/div[@class="xiq-textbox"]/input[@name="proxy_password"]',
            'wait_for': 10
        }

    serial_label = \
        {
            'DESC': 'Serial Number Label',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@id="xiqAdvancedConfig"]/p[contains(text(), "XIQSE") and contains(text(), "S/N")]',
            'wait_for': 10
        }

    onboard_button = \
        {
            'DESC': 'Onboard Button',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//input[@id="xiqOnboardButton"]',
            'wait_for': 10
        }

    error_label = \
        {
            'DESC': 'Error Label',
            'XPATH': '//div[@id="xiqLicContentDiv" or @id="licenseContentDiv"]//div[@class="xiq-error-block"]',
            'wait_for': 10
        }
