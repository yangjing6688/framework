class AlarmsWebElementsDefs:
    alarms_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    alarm_grid_row_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-selector',
            'wait_for': 5
        }

    alarms_grid_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 5
        }

    alarm_clear_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//div[@data-tip="Clear"]',
            'wait_for': 5
        }

    alarm_clear_confirm_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    alarm_clear_tool_tip = \
        {
            'XPATH': '//div//span[@data-dojo-attach-point="clearResult"]',
            'wait_for': 5
        }

    critical_alarm_count_status_bar = \
        {
            'XPATH': '//div//a[@data-dojo-attach-point="criticalCount"]',
            'wait_for': 5
        }

    major_alarm_count_status_bar = \
        {
            'XPATH': '//div//a[@data-dojo-attach-point="criticalCount"]',
            'wait_for': 5
        }

    minor_alarm_count_status_bar = \
        {
            'XPATH': '//div//a[@data-dojo-attach-point="criticalCount"]',
            'wait_for': 5
        }

    alarms_grid_refresh_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="refresh"]',
            'wait_for': 5
        }
