

class AlarmsEventsAlarmsWebElementsDefinitions:

    search_open_button = \
        {
            'DESC': 'Button to open the Search field',
            'XPATH': '//div[contains(@id, "alarmGrid")]//span[contains(@class, "x-form-search-trigger")]/ancestor::a',
            
        }

    search_text_field = \
        {
            'DESC': 'Search Text Field',
            'XPATH': '//div[contains(@id, "alarmGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "inputWrap")]/input',
            
        }

    search_trigger_button = \
        {
            'DESC': 'Button to trigger the search',
            'XPATH': '//div[contains(@id, "alarmGrid")]//div[contains(@id, "trigger-search")]',
            
        }

    search_clear_button = \
        {
            'DESC': 'Button to clear the search',
            'XPATH': '//div[contains(@id, "alarmGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "trigger-clear")]',
            
        }

    alarms_table = \
        {
            'DESC': 'Alarms Table',
            'XPATH': '//div[contains(@id, "alarmGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            
        }

    alarms_table_rows = \
        {
            'DESC': 'Alarms Table Rows',
            'XPATH': '//div[contains(@id, "alarmGrid")]//table[contains(@id, "gridview")]//tr',
            
        }
