

class AnalyticsApplicationFlowsWebElementsDefinitions:

    search_open_button = \
        {
            'DESC': 'Button to open the Search field',
            'XPATH': '//div[contains(@id, "textfield")]//div[contains(@class, "x-form-search-trigger")]',
            
        }

    search_text_field = \
        {
            'DESC': 'Search Text Field',
            'XPATH': ' //div[contains(@id, "textfield")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "inputWrap")]/input',
            
        }

    search_trigger_button = \
        {
            'DESC': 'Button to trigger the search',
            'XPATH': '//div[contains(@id, "textfield")]//div[contains(@id, "trigger-search")]',
            
        }

    search_clear_button = \
        {
            'DESC': 'Button to clear the search',
            'XPATH': '//div[contains(@id, "textfield")]//div[contains(@id, "trigger-clear")]',
            
        }

    application_flows_table = \
        {
            'DESC': 'Application Flows Table',
            'XPATH': '//div[contains(@id, "flowGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            
        }

    application_flows_table_rows = \
        {
            'DESC': 'Application Flows Table Rows',
            'XPATH': '//div[contains(@id, "flowGrid")]//table[contains(@id, "gridview")]//tr',
            
        }

