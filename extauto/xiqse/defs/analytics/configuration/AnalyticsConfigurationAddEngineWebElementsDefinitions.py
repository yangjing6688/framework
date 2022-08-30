

class AnalyticsConfigurationAddEngineWebElementsDefinitions:

    add_engine_ip_address_field = \
        {
            'DESC': 'Analytics> Configuration Tab> Add Engine Dialog> IP Address field',
            'XPATH': '//input[@name="ip"]',
            
        }

    add_engine_name_field = \
        {
            'DESC': 'Analytics> Configuration Tab> Add Engine Dialog> Name field',
            'XPATH': '//input[@name="name"]',
            
        }

    add_engine_snmp_profile_dropdown = \
        {
            'DESC': 'Analytics> Configuration Tab> Add Engine Dialog> SNMP Profile dropdown field',
            'XPATH': '//input[@name="profileId"]',
            
        }

    add_engine_ok_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Add Engine Dialog> OK Button',
            'XPATH': '//div[contains(@id, "addAnalyticsEngineWindow")]//span[contains(text(), "OK")]/ancestor::a',
            
        }

    add_engine_cancel_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Add Engine Dialog> Cancel Button',
            'XPATH': '//div[contains(@id, "addAnalyticsEngineWindow")]//span[contains(text(), "Cancel")]/ancestor::a',
            
        }
