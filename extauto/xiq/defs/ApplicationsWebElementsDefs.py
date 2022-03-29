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