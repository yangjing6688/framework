class EventsWebElementsDefs:

    events_refresh_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="refresh"]',
            'wait_for': 5
        }

    events_download_button = \
        {
            'XPATH': '//*[@data-tip="Download"]',
            'wait_for': 5
        }

    events_content_grid = \
        {
            'XPATH': '//*[@class="dgrid-content ui-widget-content"]//tr',
            'wait_for': 5
        }

    events_pagination = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pagesWrap"]//a[@data-page="1"]',
            'wait_for': 5
        }