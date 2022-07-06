

class CommonViewWebElementsDefinitions:

    main_application_body = \
        {
            'DESC': 'Main application body',
            'XPATH': '//body[@role="application"]',
            
        }

    load_mask = \
        {
            'DESC': 'Load Mask',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Loading..."]',
            
        }

    div_dropdown_items = \
        {
            'DESC': 'Drop down items for a div type dropdown (div)',
            'XPATH': '//div[contains(@id, "${element_id}") and contains(@id, "-picker-listWrap")]/ul/div',
            
        }

    list_dropdown_items = \
        {
            'DESC': 'Drop down items for a list type dropdown (li)',
            'XPATH': '//div[contains(@id, "${element_id}") and contains(@id, "-picker-listWrap")]/ul/li',
            
        }

    combo_dropdown_items = \
        {
            'DESC': 'Drop down items for a combobox type dropdown (label)',
            'XPATH': '//div[contains(@data-boundview, "${element_id}")]/label',
            
        }

    panel_section_button = \
        {
            'DESC': 'Button that is used to collapse or expand a section in a panel',
            'XPATH': '//div[@class="x-box-target"]//div[text()="${element_id}"]/../../div[contains(@class,"x-tool-after-title")]',
            
        }
