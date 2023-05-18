class CommunicationsWebElementDefs:
    comm_page_text = \
        {
            'XPATH': '//div[@id="container" and @class="communications"]//h1',
            'XPATH': '//h1//span[@class="s1"]//b[contains(text(), "NOTIFICATIONS")]',
        }

    communications_notification_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-notifications"]',
            
        }

    communications_preview_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-previews"]',
            
        }

    communications_new_updates_nav = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-newUpdates"]',
            
        }

    new_in_extreme_page_text = \
        {
            'XPATH': '//div[@id="container" and @class="communications"]//h1',
            
        }

    notification_page_text = \
        {
            'XPATH': '//span[@class="s1"]//b[contains(text(), "NOTI")]',
            'wait_for': 5
        }

    preview_page_text = \
        {
            'XPATH': '//div[@id="container" and @class="communications"]//h1[contains(text(), "PRE")]',
            'wait_for': 5
        }

    iframe_url = \
        {
            'XPATH': '//div[@class="communications"]',
            'index': 0,
            
        }

    iframe_url_href = \
        {
            'TAG_NAME': 'iframe',
            'index': 0,
            'wait_for': 5
        }