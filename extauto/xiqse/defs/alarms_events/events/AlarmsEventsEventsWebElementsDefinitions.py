

class AlarmsEventsEventsWebElementsDefinitions:

    time_range_dropdown = \
        {
            'DESC': 'Time Range Dropdown',
            'XPATH': '//input[@name="timeSpanSelector"]',
            'wait_for': 10
        }

    type_dropdown = \
        {
            'DESC': 'Type Dropdown',
            'XPATH': '//span[text()="Type:"]/ancestor::div[contains(@id, "multicombobox")]//input',
            'wait_for': 10
        }

    search_open_button = \
        {
            'DESC': 'Button to open the Search field',
            'XPATH': '//div[contains(@id, "eventLogGrid")]//span[contains(@class, "x-form-search-trigger")]/ancestor::a',
            'wait_for': 10
        }

    search_text_field = \
        {
            'DESC': 'Search Text Field',
            'XPATH': '//div[contains(@id, "eventLogGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "inputWrap")]/input',
            'wait_for': 10
        }

    search_trigger_button = \
        {
            'DESC': 'Button to trigger the search',
            'XPATH': '//div[contains(@id, "eventLogGrid")]//div[contains(@id, "trigger-search")]',
            'wait_for': 10
        }

    search_clear_button = \
        {
            'DESC': 'Button to clear the search',
            'XPATH': '//div[contains(@id, "eventLogGrid")]//div[contains(@id, "trigger-search")]/preceding-sibling::div[contains(@id, "trigger-clear")]',
            'wait_for': 10
        }

    events_table = \
        {
            'DESC': 'Events Table',
            'XPATH': '//div[contains(@id, "eventLogGrid") and @data-ref="body"]//div[@class="x-grid-item-container"]',
            'wait_for': 10
        }

    events_table_rows = \
        {
            'DESC': 'Events Table Rows',
            'XPATH': '//div[contains(@id, "eventLogGrid")]//table[contains(@id, "gridview")]//tr',
            'wait_for': 10
        }
