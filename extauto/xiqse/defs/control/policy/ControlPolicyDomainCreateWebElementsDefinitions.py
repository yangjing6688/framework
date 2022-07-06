class ControlPolicyDomainCreateWebElementsDefinitions:

    create_domain_domain_name_field = \
        {
            'DESC': 'Domain Name field in the Create Domain window',
            'XPATH': '//div[contains(@id,"window")]//input[contains(@id,"textfield")]',
            
        }

    create_domain_ok_button = \
        {
            'DESC': 'Ok button in the Create Domain window',
            'XPATH': '//div[contains(@id,"window")]//span[contains(text(),"OK")]',
            
        }

    create_domain_cancel_button = \
        {
            'DESC': 'Cancel button in the Create Domain window',
            'XPATH': '//div[contains(@id,"window")]//span[contains(text(),"Cancel")]',
            
        }

    create_domain_success_msg = \
        {
            'DESC': 'Create Domain Successful message ',
            'XPATH': '//div[contains(text(),"Domain created successfully.")]',
            
        }

    create_domain_success_ok_button = \
        {
            'DESC': 'OK button in the Create Domain Successful dialog',
            'XPATH': '//div[contains(@id,"messagebox")]//span[contains(text(),"OK")]',
            
        }
    create_domain_error_msg = \
        {
            'DESC': 'Create Domain error message ',
            'XPATH': '//div[contains(text(),"Domain name is already in use.")]',
            
        }

    create_domain_error_ok_button = \
        {
            'DESC': 'OK button in the Create Domain error dialog',
            'XPATH': '//div[contains(@id,"messagebox")]//span[contains(text(),"OK")]',
            
        }
