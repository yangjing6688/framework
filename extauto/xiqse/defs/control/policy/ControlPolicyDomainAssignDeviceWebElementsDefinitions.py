class ControlPolicyDomainAssignDeviceWebElementsDefinitions:

    # Assign Device(s) to Domain window
    assign_all_devices_node = \
        {
            'DESC': 'expand/collapse icon for the "All Devices" node in the Assign Device(s) to Domain window',
            'XPATH': '//span[contains(@class, "x-tree-node-text") and contains(text(),"All Devices")]/../div[contains(@class, "x-tree-expander")]',
            
        }

    device_els_active_template = \
        {
            'DESC': 'Device node in the left tree view',
            'XPATH': '//div[contains(@id, "deviceSelectionTree")]//span[contains(text(), "${ip}")]',
            'wait_for': 2
        }

    assign_add_button = \
        {
            'DESC': 'Add button in the Assign Device(s) to Domain window',
            'XPATH': '//span[contains(text(), "►")]',
            
        }

    assign_cancel_button = \
        {
            'DESC': 'Cancel button in the Assign Device(s) to Domain window',
            'XPATH': '//div[contains(@id,"window")]//span[contains(text(),"Cancel")]',
            
        }

    assign_ok_button = \
        {
            'DESC': 'OK button in the Assign Device(s) to Domain window',
            'XPATH': '//div[@xiqse-auto-id="policyAssignDevicesOkButton"] |'
                     '//div[contains(@id, "window")]//span[text()="OK"]/ancestor::a',
            
        }
    # end of Assign Device(s) to Domain window
