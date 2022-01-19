class ReportsWebElementDefs:
    network_summary_tab = \
        {
            'XPATH': '//li/span[contains(text() , "Network Summary")]',
            'wait_for': 10
        }

    pci_dss_tab = \
        {
            'XPATH': '//li/span[contains(text() , "PCI DSS 3.2")]',
            'wait_for': 10
        }

    wips_history_tab = \
        {
            'XPATH': '//li/span[contains(text() , "WIPS History")]',
            'wait_for': 10
        }

    wifi_statistic_summary_tab = \
        {
            'XPATH': '//li/span[contains(text() , "WIFI Statistics Summary")]',
            'wait_for': 10
        }

    name_report_text_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="reportTitle"]',
            'wait_for': 10
        }

    select_widgets_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="newTags"]//a//span[contains(text(), "Access (Default)")]',
            'wait_for': 10
        }

    select_widgets_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-viewtype")]//li',
            'wait_for': 10
        }

    share_with_email_text_field = \
        {
            'XPATH': '//div/textarea[@data-dojo-attach-point="shareEmail"]',
            'wait_for': 10
        }

    generate_report_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="saveButton" and contains(text(),"Generate Report")]',
            'wait_for': 10
        }
