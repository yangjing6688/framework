

class ControlAccessControlPanelWebElementsDefinitions:

    nac_status_ok = \
        {
            'DESC': 'Get ID for NAC Status in the right panel',
            'XPATH': '//div[contains(@id, "nacApplianceDetailsPanel")]//div[(@data-ref="innerCt") and contains(text(),"Status: OK")]',
            
        }

    nac_status = \
        {
            'DESC': 'Get ID for NAC Status in the right panel',
            'XPATH': '//div[contains(@id, "nacApplianceDetailsPanel")]//div[(@data-ref="innerCt") and starts-with(text(),"Status:")]',
            
        }

    nac_unlicensed_text = \
        {
            'DESC': 'Xpath for unlicensed virtaul appliance in the right panel',
            'XPATH': '//div[contains(@id, "box")]/b[contains(text(), "Unlicensed Virtual Appliance")]',
            
        }

    nac_validlicensed_text = \
        {
            'DESC': 'Xpath for Valid Virtaul Appliance License in the right panel',
            'XPATH': '//div[contains(@id, "box") and contains(text(), "Valid Virtual Appliance License")]',
            
        }

    row_grid_by_ip = \
        {
            'DESC': 'Selecting a row from the right panel',
            'XPATH': '//td[@data-qtip="' + "${element_name}" + '" and contains(@class, "x-grid-cell-first")]',
            
        }
