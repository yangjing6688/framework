

class AnalyticsConfigurationWebElementsDefinitions:

    configuration_add_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Add Button',
            'XPATH': '//div[contains(@id, "toolbar")]//span[text()="Add..."]/ancestor::a',
            'wait_for': 10
        }

    delete_engine_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Delete Button',
            'XPATH': '//div[contains(@id, "toolbar")]//span[text()="Delete"]/ancestor::a',
            'wait_for': 10
        }

    enforce_engine_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Enforce Button',
            'XPATH': '//div[contains(@id, "toolbar")]//span[text()="Enforce"]/ancestor::a',
            'wait_for': 10
        }

    enforce_all_engine_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Enforce All Button',
            'XPATH': '//div[contains(@id, "toolbar")]//span[text()="Enforce All"]/ancestor::a',
            'wait_for': 10
        }

    poll_engine_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Poll Button',
            'XPATH': '//div[contains(@id, "toolbar")]//span[text()="Poll"]/ancestor::a',
            'wait_for': 10
        }

    restart_collector_engine_button = \
        {
            'DESC': 'Analytics> Configuration Tab> Restart Collector Button',
            'XPATH': '//div[contains(@id, "toolbar")]//span[text()="Restart Collector"]/ancestor::a',
            'wait_for': 10
        }

    panel_refresh_icon = \
        {
            'DESC': 'Refresh Panel Icon',
            'XPATH': '//div[contains(@id, "toolbar")]//span[contains(@class, "fa-refresh")]/ancestor::a',
            'wait_for': 10
        }

    engines_table = \
        {
            'DESC': 'Engines Table',
            'XPATH': '//div[contains(@id, "analyticsEnginesView")]',
            'wait_for': 10
        }

    engine_table_rows = \
        {
            'DESC': 'Engine Table Rows',
            'XPATH': '//div[contains(@role, "listbox")]//div[contains(@class, "analyticsEngine")]//tr',
            'wait_for': 10
        }

    add_application_analytics_engine_dialog = \
        {
            'DESC': 'Add Application Analytics Engine dialog',
            'CSS_SELECTOR':  '.x-window.x-closable[id*=addAnalyticsEngineWindow]',
            'wait_for': 10
        }

    add_application_analytics_engine_dialog_cancel_button = \
        {
            'DESC': 'Cancel button within Add Application Analytics Engine dialog',
            'XPATH': '//div[contains(@id, "addAnalyticsEngineWindow")]//span[contains(text(), "Cancel")]',
            'wait_for': 10
        }

    enforcing_engine_load_mask = \
        {
            'DESC': '"Enforcing Engine..." load mask',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Enforcing Engine..."]',
            'wait_for': 10
        }

    enforcing_engines_load_mask = \
        {
            'DESC': '"Enforcing Engines..." load mask',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Enforcing Engines..."]',
            'wait_for': 10
        }

    polling_engine_load_mask = \
        {
            'DESC': '"Polling Engine..." load mask',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Polling Engine..."]',
            'wait_for': 10
        }

    restarting_collector_load_mask = \
        {
            'DESC': '"Restarting Collector..." load mask',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Restarting Collector..."]',
            'wait_for': 10
        }
