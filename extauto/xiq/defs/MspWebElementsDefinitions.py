class MspWebElementsDefinitions:

    view_organizations_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-account-menu-org-filter']",
            'wait_for': 15
        }

    view_organization_select = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mspSelectAll']",
            'wait_for': 15
        }

    view_organization_close_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeBtn']",
            'wait_for': 15
        }

    organizations_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]//td/..',
            'wait_for': 15
        }

    organizations_select_check_box = \
        {
            'CSS_SELECTOR': '.org-checkbox',
            'wait_for':    15
        }

    organizations_select_radio_button = \
        {
            'NAME': 'singleOrgRadio',
            'wait_for':    15
        }

    page_size_element = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 2
        }

    next_page_element = \
        {
            'CSS_SELECTOR': '.J-page-next.ui-page-item-next',
            'XPATH': '//*[@data-dojo-attach-point="next-item1"]',
            'index': 1,
            'wait_for': 2
        }

    page_numbers = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pagesWrap"]',
            'index': 1,
            'wait_for': 2
        }

    organization_search_text_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mspOrgSearch"]',
            'wait_for': 15
        }

    organization_search_icon = \
        {
            'XPATH': '//*[@class="search-icon"]',
            'wait_for': 15
        }

    organization_search_result_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mspOrgSearchResult"]//li',
            'wait_for': 15
        }