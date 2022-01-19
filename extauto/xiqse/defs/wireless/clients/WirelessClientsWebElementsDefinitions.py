

class WirelessClientsWebElementsDefinitions:

    clients_tab = \
        {
            'DESC': 'Wireless> Clients> Clients Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Clients" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    client_events_tab = \
        {
            'DESC': 'Wireless> Clients> Client Events Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Client Events" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    event_analyzer_tab = \
        {
            'DESC': 'Wireless> Clients> Event Analyzer Tab',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Event Analyzer" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    event_collection_disabled_dialog = \
        {
            'DESC': 'Event Collection Disabled dialog',
            'XPATH': '//div[contains(@id, "messagebox")]//div[contains(text(), "Event Collection is currently disabled")]',
            'wait_for': 10
        }

    event_collection_disabled_dialog_ok_button = \
        {
            'DESC': 'OK Button for the Event Collection Disabled dialog',
            'XPATH': '//div[contains(@id, "messagebox")]//span[text()="OK"]/ancestor::a[@role="button"]',
            'wait_for': 10
        }
