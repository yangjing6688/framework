class ApplicationsWebElementsDefs:

    manage_applications = \
        {
            'XPATH': "//*[@data-automation-tag='automation-manage-application-button']",
            'wait for': 5
        }

    manage_add_custom = \
        {
            'XPATH': '//div[@data-automation-tag="automation-application-services-app-list"]'
                 '//span[@class="table-action-buttons table-action-icons table-addCustom"]',
            'wait_for': 3
        }

    manage_add_custom_name_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="txtAppNameNode"]',
            'wait_for': 3
        }

    manage_add_custom_add_app = \
        {
            'XPATH': '//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 3
        }

    manage_add_custom_group_name_textfield = \
        {
            'XPATH': '//input[@data-dojo-attach-point="txtGroupNameNode"]',
            'wait_for': 3
        }

    manage_add_custom_group_name_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 3
        }

    manage_add_custom_app_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveNode"]',
            'wait_for': 3
        }

    manage_add_custom_tooltip_text = \
        {
            'XPATH': '//*[@class="ui-tipbox-title"]',
            'index': 1,
            'wait_for': 5
        }

    manage_add_custom_app_search = \
        {
            'XPATH': '//div[@data-automation-tag="automation-app-services-seach-container"]',
            'wait_for': 3
        }

    manage_add_custom_search_text = \
        {
            'XPATH': '//input[@data-dojo-attach-point="txtFilterNode"]',
            'wait_for': 3
        }

    manage_apps_cell = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-0 w30 dgrid-selector"]',
            'wait_for': 3
        }

    manage_add_custom_edit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-application-services-app-list"]'
                     '//span[@class="table-action-icons table-edit"]',
            'wait_for': 3
        }

    manage_add_custom_delete = \
        {
            'XPATH': '//div[@data-automation-tag="automation-application-services-app-list"]'
                     '//span[@class="table-action-icons table-remove"]',
            'wait_for': 3
        }

    manage_add_custom_delete_confirm = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 3

        }

    application_dialogbox_close_button = \
        {
            'XPATH': '//div[contains(@class,"manage-applications-pop-up")]//div[@data-dojo-attach-point="titleBar"]//span[@data-dojo-attach-point="closeButtonNode"]',
        }

    application_dialogbox_close_tab = \
        {
            'XPATH': '//div[@class="manage-applications-pop-up hmOverride dijitDialog dijitDialogHover dijitHover"]//div[@data-dojo-attach-point="titleBar"]//span[@data-dojo-attach-point="closeButtonNode"]',
            'wait_for': 5
        }