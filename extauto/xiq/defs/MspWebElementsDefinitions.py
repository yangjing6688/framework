class MspWebElementsDefinitions:

    view_organizations_button = \
        {
            'XPATH': "//*[@class='msp-multi-org-display expanded']",
            'wait_for': 5
        }

    view_organization_select = \
        {
            'XPATH': "//*[@data-dojo-attach-point='mspSelectAll']",
            'wait_for': 5
        }

    view_organization_close_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='closeBtn']",
            'wait_for': 5
        }

    organizations_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]//td/..',

        }

    organizations_select_check_box = \
        {
            'CSS_SELECTOR': '.org-checkbox',
            'wait_for':    2
        }