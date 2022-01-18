

class NetworkDevicesDevicesUpgradeFirmwareWebElementsDefinitions:

     assign_firmware_images_button = \
        {
            'DESC': 'Assign Firmware Images Button',
            'CSS_SELECTOR': '[data-qtip^="Assign Firmware Images"]',
            'wait_for': 10
        }

     inventory_settings_button = \
        {
            'DESC': 'Inventory Settings Button',
            'CSS_SELECTOR': '[data-qtip^="Inventory Settings"]',
            'wait_for': 10
        }

     upgrade_firmware_start_button = \
         {
            'DESC': 'Upgrade Firmware Start Button',
            'XPATH': '//div[contains(@id, "firmwareDownloadWindow")]//span[text()="Start"]',
            'wait_for': 10
         }

     upgrade_firmware_close_button = \
         {
             'DESC': 'Close Button',
             'XPATH': '//div[contains(@id, "firmwareDownloadWindow")]//span[text()="Close"]',
             'wait_for': 10
         }

     begin_downloading_firmware_yes_button = \
         {
             'DESC': 'Begin Downloading Firmware Yes Button',
             'XPATH': '//div[contains(@id, "messagebox")]//span[text()="Yes"]/ancestor::a',
             'wait_for': 10
         }

     begin_downloading_firmware_no_button = \
         {
             'DESC': 'Begin Downloading Firmware No Button',
             'XPATH': '//div[contains(@id, "messagebox")]//span[text()="No"]/ancestor::a',
             'wait_for': 10
         }

     processed_upgrade_no_failures_text = \
         {
             'DESC': 'Processed 1 of 1 devices with 0 failures Text',
             'XPATH':  '//div[contains(text(), "Processed 1 of 1 devices with 0 failures")]',
             'wait_for': 10
         }