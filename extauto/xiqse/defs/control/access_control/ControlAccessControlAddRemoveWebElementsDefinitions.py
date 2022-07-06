

class ControlAccessControlAddRemoveWebElementsDefinitions:

    add_nac_appliance_tb_button = \
        {
            'DESC': 'Add NAC Appliacne Toolbar Button',
            'XPATH': '//span[text()="Add.." and contains(@class, "x-btn-inner x-btn-inner-default-toolbar-small")]',
            
        }

    id_for_ip_field = \
        {
            'DESC': 'Id of IP Address text field in the Add Access Control Engine dialog',
            'XPATH': '//span[@data-ref = "labelTextEl" and text() = "IP Address:"]',
            
        }

    id_for_ip_name_field = \
        {
            'DESC': 'Id of Name text field in the Add Access Control Engine dialog',
            'XPATH': '//span[@data-ref = "labelTextEl" and text() = "Name:"]',
            
        }

    ip_field = \
        {
            'DESC': 'IP Address text field in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="ip"]',
            
        }

    add_checkbox = \
        {
            'DESC': 'Checkbox to add to device in the Add Device dialog',
            'XPATH': '//label[text()="Add Engine to Devices"]',
            
        }

    add_button_dialog = \
        {
            'DESC': 'Add button in the Add Device dialog',
            'XPATH': '//span[text()="Add" and contains(@id, "button")]',
            
        }

    cancel_button_dialog = \
        {
            'DESC': 'Cancel button in the Add Device dialog',
            'XPATH': '//span[text()="Cancel" and contains(@id, "button")]',
            
        }

    save_ok_button = \
        {
            'DESC': 'OK button in Save Successful',
            'XPATH': '//span[@data-ref="btnInnerEl" and text()="OK"]',
            
        }

    save_successful = \
        {
            'DESC': 'Save Successful after adding NAC Engine',
            'XPATH': '//div[@data-ref="textEl" and text()="Save Successful"]',
            
        }

    delete_nac_checkbox = \
        {
            'DESC': 'Checkbox when deleting NAC appliance -  Delete Engine from Devices, if applicable',
            'XPATH': '//*[@id="rmFromConsoleBtn"]',
            
        }