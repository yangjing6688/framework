class ControlPolicyDomainEnforceWebElementsDefinitions:

    # Enforce Domain
    enforce_domain_data_question = \
        {
            'DESC': 'Enforce confirmation message dialog',
            'XPATH': '//div[contains(text(),"Enforce domain data to")]',
            'wait_for': 5
        }

    enforce_domain_data_yes_button = \
        {
            'DESC': 'Yes button in the Enforce confirmation message dialog',
            'XPATH': '//span[contains(@class,"x-btn-inner-blue-small") and contains(text(),"Yes")]',
            'wait_for': 10
        }

    enforce_domain_data_no_button = \
        {
            'DESC': 'No button in the Enforce confirmation message dialog',
            'XPATH': '//span[contains(@class,"x-btn-inner-default-small") and contains(text(),"No")]',
            'wait_for': 10
        }

    enforce_domain_success_msg = \
        {
            'DESC': 'Enforce Success message in the dialog',
            'XPATH': '//div[contains(@id,"messagebox") and contains(text(),"Domain successfully enforced to device(s).")]',
            'wait_for': 10
        }

    enforce_domain_success_ok_bttn = \
        {
            'DESC': 'Enforce Success message in the dialog',
            'XPATH': '//div/a[2]/span/span/span[contains(@class,"x-btn-inner-blue-small") and contains(text(),"OK")]',
            'wait_for': 10
        }

    enforce_domain_errors_warnings_msg = \
        {
            'DESC': 'Enforce Success message in the dialog',
            'XPATH': '//div[contains(text(),"encountered on the following device(s) during Enforce. Refer to policy event log for additional information.")]',
            'wait_for': 10
        }

    enforce_domain_errors_warnings_ok_bttn = \
        {
            'DESC': 'Enforce Success message in the dialog',
            'XPATH': '//div[contains(@id,"window")]//a[1]//span[contains(@class,"x-btn-inner-blue-small") and contains(text(),"OK")]',
            'wait_for': 10
        }
    # end of Enforce Domain
