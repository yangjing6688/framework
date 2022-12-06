
class CloudConfigGroupWebElementDefinition:
    add_ccg_policy = \
        {
            'XPATH': "//*[@data-automation-tag='automation-manage-device-actions-ap-add-to-ccg']",
            'wait_for': 5
        }

    add_ccg_policy_button = \
        {
            'XPATH': "//div[@class='ccg-object-wrapper']//span[@data-dojo-attach-point='ipSave']",
            'wait_for': 5
        }

    click_select_ccg_policy = \
        {
            'XPATH': "//div[@data-dojo-attach-point='mainContent']//span[@data-dojo-attach-point='ipMark']",
            'wait_for': 5
        }

    dropdown_items = \
        {
            'XPATH':  '//ul[@class="item-area"]//li',
            'wait_for': 5
        }

    click_ccg_policy_continue = \
        {
            'XPATH': '//button[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 5
        }

    ccg_members_arrow = \
        {
            'CSS_SELECTOR': '.arrow',
            'wait_for': 5
        }

    ccg_members = \
        {
            'CSS_SELECTOR': '.ccgs',
            'wait_for': 2
        }

    ccg_member = \
        {
            'CSS_SELECTOR': '.device-ccg.long',
            'wait_for': 2
        }

    ccg_member_all = \
        {
            'CSS_SELECTOR': '.ccgs',
            'wait_for': 2
        }

    ccg_add_button = \
        {
            'XPATH': '//*[@class="cloud-config-groups"]//*[@data-tip="Add"]',
            'wait_for': 5
        }

    ccg_page_grid_rows = \
        {
            'XPATH': '//div[@class="clearfix device-list"]//div[@data-dojo-attach-point="gridContent"]'
                     '//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    device_select_check_box_common_object = \
        {
            'CSS_SELECTOR': '.ccg-device-select',
            'wait_for':    2
        }

    ccg_select_check_box_common_object = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector',
            'wait_for': 2
        }

    ccg_members_hostname = \
        {
            'XPATH': '//div[@class="ui-tags-container"]//span[@class="ui-tag"]',
            'wait_for': 2
        }

    edit_ccg_button = \
        {
            'XPATH': '//*[@class="cloud-config-groups"]//span[@class="table-action-icons table-edit"]',
            'wait_for': 10
        }

    delete_ccg_button = \
        {
            'XPATH': '//*[@class="cloud-config-groups"]//span[@class="table-action-icons table-remove"]',
            'wait_for': 2
        }

    delete_ccg_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 2
        }


    get_ccg_grid_row = \
        {
            'XPATH': '//div[@class="cloud-config-groups"]//div[@data-dojo-attach-point="gridContent"]'
                     '//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    ccg_row_name = \
        {
            'CSS_SELECTOR': '.field-name',
            'wait_for': 2
        }

    get_ccg_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    get_ccg_description = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    get_form_error = \
        {
            'XPATH': '//span[@class="form-error"]',
            'wait_for': 5
        }

    get_ccg_description_manage_page = \
        {
            'XPATH': '//div[@class="cloud-config-group ui-small"]//textarea[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    ccg_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    ccg_cancel_button = \
        {
            'XPATH': '//button[@class="btn btn-small btn-cancel cancelButton"]',
            'wait_for': 5
        }

    ccg_select_cancel_button = \
        {
            'XPATH': '//button[@class="btn btn-small btn-cancel"]',
            'wait_for': 5
        }

    ccg_continue_button = \
        {
            'XPATH': "//button[@data-dojo-attach-point='continueBtn']",
            'wait_for': 5
        }


    get_device_hostname = \
        {
            'CSS_SELECTOR': '.J-ipaddress',
            'wait_for': 5
        }

    get_device_serial = \
        {
            'CSS_SELECTOR': '.field-serialNumber',
            'wait_for': 5
        }

    remove_device_from_ccg = \
        {
            'CSS_SELECTOR': '.J-tag-close',
            'wait_for': 2
        }

    get_device_ccg_hostname = \
        {
            'XPATH': '//div[@class="top-form-side selected-devices"]//span[@class="ui-tag"]',
            'wait_for': 5
        }
