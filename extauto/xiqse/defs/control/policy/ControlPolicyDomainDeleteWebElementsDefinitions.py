class ControlPolicyDomainDeleteWebElementsDefinitions:

    delete_domain_name_list = \
        {
            'DESC': 'Domain name list in the dropdown menu in the Delete Domain window',
            'XPATH': '//input[@name="policyDomainSelectionCombo"]',
            
        }

    delete_domain_name_template = \
        {
            'DESC': 'Domain name in the dropdown menu in the Delete Domain window',
            'XPATH': '//li[contains(text(),"${d_name}")]',
            'wait_for': 3
        }

    delete_domain_ok = \
        {
            'DESC': 'OK button in the Delete domain window',
            'XPATH': '//div[contains(@id,"window")]//span[contains(text(),"OK")]',
            
        }

    delete_domain_close = \
        {
         'DESC': 'Close button in the Delete domain window',
         'XPATH': '//div[contains(@id,"window")]//span[contains(text(),"Close")]',
        
        }

    delete_domain_yes = \
        {
            'DESC': 'Yes button in the Are You Sure? dialog during Delete Domain process',
            'XPATH': '//div[contains(@id,"messagebox")]//span[contains(text(),"Yes")]',
            
        }

    delete_domain_confirm_ok = \
        {
            'DESC': 'OK button in the Delete domain Successful dialog',
            'XPATH': '//div[contains(@id,"messagebox")]//span[contains(text(),"OK")]',
            
        }