class ControlPolicyDomainOpenWebElementsDefinitions:

    d_name = \
        {
            'DESC': 'Domain name list in the dropdown menu in the Delete Domain window',
            'XPATH': '//input[@name="policyDomainSelectionCombo"]',
            
        }

    domain_els_active_template = \
        {
            'DESC': 'Device node in the left tree view',
            'XPATH': '// div[contains(@class,"x-menu")] // span[contains(text(), "${d_name}")]',
            'wait_for': 3
        }
