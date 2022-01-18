

class CommonViewWebElementsDefinitions:

    main_application_body = \
        {
            'DESC': 'Main application body',
            'XPATH': '//body[@role="application"]',
            'wait_for': 10
        }

    load_mask = \
        {
            'DESC': 'Load Mask',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Loading..."]',
            'wait_for': 10
        }

    div_dropdown_items = \
        {
            'DESC': 'Drop down items for a div type dropdown (div)',
            'XPATH': '//div[contains(@id, "${element_id}") and contains(@id, "-picker-listWrap")]/ul/div',
            'wait_for': 10
        }

    list_dropdown_items = \
        {
            'DESC': 'Drop down items for a list type dropdown (li)',
            'XPATH': '//div[contains(@id, "${element_id}") and contains(@id, "-picker-listWrap")]/ul/li',
            'wait_for': 10
        }

    combo_dropdown_items = \
        {
            'DESC': 'Drop down items for a combobox type dropdown (label)',
            'XPATH': '//div[contains(@data-boundview, "${element_id}")]/label',
            'wait_for': 10
        }
