class MLInsightscmpAnalyticsDefinitions:

    n360_cmp_analytics_cur = \
        {
            'XPATH': '//*[contains(text(), "Current")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his = \
        {
            'XPATH': '//*[contains(text(), "Historical")]',
            'wait_for': 5
        }

    n360_cmp_analytics_refresh = \
        {
            'XPATH': '//*[@class="ui-icon ui-fresh-icon"]',
            'wait_for': 5
        }

    n360_cmp_analytics_bw_use_ind = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthUsage"]//span[contains(text(), "Enterprise")]',
            'wait_for': 5
        }

    n360_cmp_analytics_bw_use_ind_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthUsage"]//ul[@class="chzn-results qa-chzn-results-optionsindustry"]//li',
            'wait_for': 5
        }

    n360_cmp_analytics_bw_use_org_size = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthUsage"]//span[contains(text(), "1 to 10 APs")]',
            'wait_for': 5
        }

    n360_cmp_analytics_bw_use_org_size_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthUsage"]//ul[@class="chzn-results qa-chzn-results-optionssize"]//li',
            'wait_for': 5
        }

    n360_cmp_analytics_unique_cli_ind = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientDevices"]//span[contains(text(), "Enterprise")]',
            'wait_for': 5
        }

    n360_cmp_analytics_unique_cli_ind_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientDevices"]//ul[@class="chzn-results qa-chzn-results-optionsindustry"]//li',
            'wait_for': 5
        }

    n360_cmp_analytics_unique_cli_org_size = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientDevices"]//span[contains(text(), "1 to 10 APs")]',
            'wait_for': 5
        }

    n360_cmp_analytics_unique_cli_org_size_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientDevices"]//ul[@class="chzn-results qa-chzn-results-optionssize"]//li',
            'wait_for': 5
        }

    n360_cmp_analytics_unique_cli_tech = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientDevices"]//span[contains(text(), "All Clients")]',
            'wait_for': 5
        }

    n360_cmp_analytics_unique_cli_tech_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientDevices"]//ul[@class="chzn-results qa-chzn-results-optionsclientmacprotocols"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_avg_cli_ind = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthClients"]//span[contains(text(), "Enterprise")]',
            'wait_for': 5
        }

    n360_cmp_analytics_avg_cli_ind_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthClients"]//ul[@class="chzn-results qa-chzn-results-optionsindustry"]//li',
            'wait_for': 5
        }

    n360_cmp_analytics_avg_cli_org_size = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthClients"]//span[contains(text(), "1 to 10 APs")]',
            'wait_for': 5
        }

    n360_cmp_analytics_avg_cli_org_size_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthClients"]//ul[@class="chzn-results qa-chzn-results-optionssize"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_avg_cli_radio = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthClients"]//span[contains(text(), "2.4 GHz and 5 GHz")]',
            'wait_for': 5
        }

    n360_cmp_analytics_avg_cli_radio_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthClients]//ul[@class="chzn-results qa-chzn-results-optionsband"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_bw_use_ind = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthHistorical"]//span[contains(text(), "Enterprise")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_bw_use_ind_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthHistorical"]//ul[@class="chzn-results qa-chzn-results-optionsindustry"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_bw_use_org_size = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthHistorical"]//span[contains(text(), "1 to 10 APs")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_bw_use_org_size_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedBandwidthHistorical"]//ul[@class="chzn-results qa-chzn-results-optionssize"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_unique_cli_ind = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientHistorical"]//span[contains(text(), "Enterprise")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_unique_cli_ind_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientHistorical"]//ul[@class="chzn-results qa-chzn-results-optionsindustry"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_unique_cli_org_size = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientHistorical"]//span[contains(text(), "1 to 10 APs")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_unique_cli_org_size_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientHistorical"]//ul[@class="chzn-results qa-chzn-results-optionssize"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_unique_cli_tech = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientHistorical"]//span[contains(text(), "All Clients")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_unique_cli_tech_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_NormalizedCountUniqueClientHistorical"]//ul[@class="chzn-results qa-chzn-results-optionsclientmacprotocols"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_avg_cli_ind = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthHistorical"]//span[contains(text(), "Enterprise")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_avg_cli_ind_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthHistorical"]//ul[@class="chzn-results qa-chzn-results-optionsindustry"]//li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_avg_cli_org_size = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthHistorical"]//span[contains(text(), "1 to 10 APs")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_avg_cli_org_size_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthHistorical"]//ul[@class="chzn-results qa-chzn-results-optionssize"]/li',
            'wait_for': 5
        }

    n360_cmp_analytics_his_avg_cli_radio = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthHistorical"]//span[contains(text(), "2.4 GHz and 5 GHz")]',
            'wait_for': 5
        }

    n360_cmp_analytics_his_avg_cli_radio_option = \
        {
            'XPATH': '//*[@id="ComparativeAnalytics_AverageCountPoorHealthHistorical"]//ul[@class="chzn-results qa-chzn-results-optionsband"]/li',
            'wait_for': 5
        }
