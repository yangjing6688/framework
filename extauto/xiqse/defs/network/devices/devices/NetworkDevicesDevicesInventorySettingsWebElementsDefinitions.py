

class NetworkDevicesDevicesInventorySettingsWebElementsDefinitions:

    file_transfer_mode_dropdown = \
        {
            'DESC': 'File Transfer Mode Menu',
            'XPATH': '//div[contains(@id, "firmwareSettingsWindow")]//label//span[contains(text(), "File Transfer Mode")]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

    inventory_settings_ok_button = \
        {
            'DESC': 'OK Button on Inventory Settings Dialog',
            'XPATH': '//div[contains(@id, "firmwareSettingsWindow")]//span[text()="OK"]/ancestor::a',
            
        }

    inventory_settings_cancel_button = \
        {
            'DESC': 'Cancel Button on Inventory Settings Dialog',
            'XPATH': '//div[contains(@id, "firmwareSettingsWindow")]//span[text()="Cancel"]/ancestor::a',
            
        }

    device_family_definition_filename_dropdown = \
        {
            'DESC': 'Device Family Definition Filename Menu',
            'XPATH': '//div[contains(@id, "firmwareSettingsWindow")]//label//span[contains(text(), "Device Family Definition Filename")]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

    firmware_download_mib_dropdown = \
        {
            'DESC': 'Device Family Definition MIB Dropdown Menu',
            'XPATH': '//div[contains(@id, "firmwareSettingsWindow")]//label//span[contains(text(), "Firmware Download MIB")]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

    configuration_download_mib_dropdown = \
        {
            'DESC': 'Device Family Definition MIB Dropdown Menu',
            'XPATH': '//div[contains(@id, "firmwareSettingsWindow")]//label//span[contains(text(), "Configuration Download MIB")]/ancestor::div[contains(@id, "combo")]//div[contains(@id, "trigger-picker")]',
            
        }

