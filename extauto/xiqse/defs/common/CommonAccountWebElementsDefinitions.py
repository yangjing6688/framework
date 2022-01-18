# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
class CommonAccountWebElementsDefinitions:

    account_menu_button = \
        {
            'DESC': 'Account Menu Button',
            'XPATH': '//span[contains(@class, "fa-user-circle")]/ancestor::a',
            'wait_for': 10
        }

    logout_menu_item = \
        {
            'DESC': 'Logout Menu Item',
            'XPATH': '//div[contains(@class, "x-menu-item")]/a[@class="x-menu-item-link"]/span[text()="Logout"]',
            'wait_for': 10
        }

    xiqse_username_field = \
        {
            'DESC': 'XIQSE username field',
            'XPATH': '//a[contains(@class,"userButton")]//span[contains(@class,"x-btn-inner-top-nav-toolbar-large")]//b',
            'wait_for': 10
        }

    xiqse_authorization_group_field = \
        {
            'DESC': '',
            'XPATH': '//a[contains(@class,"userButton")]//span[@style="font-size:10px"]',
            'wait_for': 10
        }
