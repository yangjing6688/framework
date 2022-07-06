class ReportsWebElementDefs:
    network_summary_tab = \
        {
            'XPATH': '//li/span[contains(text() , "Network Summary")]',
            
        }

    pci_dss_tab = \
        {
            'XPATH': '//li/span[contains(text() , "PCI DSS 3.2")]',
            
        }

    wips_history_tab = \
        {
            'XPATH': '//li/span[contains(text() , "WIPS History")]',
            
        }

    wifi_statistic_summary_tab = \
        {
            'XPATH': '//li/span[contains(text() , "WIFI Statistics Summary")]',
            
        }

    name_report_text_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="reportTitle"]',
            
        }

    select_widgets_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="newTags"]//a//span[contains(text(), "Access (Default)")]',
            
        }

    select_widgets_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-viewtype")]//li',
            
        }

    share_with_email_text_field = \
        {
            'XPATH': '//div/textarea[@data-dojo-attach-point="shareEmail"]',
            
        }

    generate_report_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="saveButton" and contains(text(),"Generate Report")]',
            
        }
