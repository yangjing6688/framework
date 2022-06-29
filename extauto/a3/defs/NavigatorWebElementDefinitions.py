class NavigatorWebElementDefinitions:

    configuration_tab = \
        {
            'XPATH': '//*[@data-automation-tag="top_configuration"]',
            'wait_for': 2
        }

    tools_tab = \
        {
            'XPATH': '//*[@href="#/tools"]',
            'wait_for': 2
        }

    auditing_tab = \
        {
            'XPATH': '//*[@data-automation-tag="top_auditing"]',
            'wait_for': 5
        }

    clients_tab = \
        {
            'XPATH': '//*[@data-automation-tag="top_nodes"]',
            'wait_for': 5
        }

    system_config_tab = \
        {
            'XPATH': '//*[@id="pf-sidebar-links"]/ul/a[6]/span',
            'wait_for': 2
        }

    policies_tab = \
        {
            'XPATH': '//span[contains(text(), "Policies and Access Control")]',
            'wait_for': 2
        }

