
class CloudConfigGroupWebElementDefinition:
    add_ccg_policy = \
        {
            'XPATH': "//*[@data-automation-tag='automation-manage-device-actions-ap-add-to-ccg']"
        }

    add_ccg_policy_button = \
        {
            'XPATH': "//div[@class='ccg-object-wrapper']//span[@data-dojo-attach-point='ipSave']"
        }

    click_select_ccg_policy = \
        {
            'XPATH': "//div[@data-dojo-attach-point='mainContent']//span[@data-dojo-attach-point='ipMark']"
        }

    dropdown_items = \
        {
            'XPATH':  '//ul[@class="item-area"]//li'
        }

    click_ccg_policy_continue = \
        {
            'XPATH': '//button[@data-dojo-attach-point="continueBtn"]'
        }

    ccg_members_arrow = \
        {
            'CSS_SELECTOR': '.arrow'
        }

    ccg_members = \
        {
            'CSS_SELECTOR': '.ccgs'
        }

    ccg_member = \
        {
            'CSS_SELECTOR': '.device-ccg.long'
        }

    ccg_member_all = \
        {
            'CSS_SELECTOR': '.ccgs'
        }

    ccg_add_button = \
        {
            'XPATH': '//*[@class="cloud-config-groups"]//*[@data-tip="Add"]'
        }

    ccg_page_grid_rows = \
        {
            'XPATH': '//div[@class="clearfix device-list"]//div[@data-dojo-attach-point="gridContent"]'
                     '//table[@class="dgrid-row-table"]'
        }

    device_select_check_box_common_object = \
        {
            'CSS_SELECTOR': '.ccg-device-select'
        }

    ccg_select_check_box_common_object = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-0.w30.dgrid-selector'
        }

    ccg_members_hostname = \
        {
            'XPATH': '//div[@class="ui-tags-container"]//span[@class="ui-tag"]'
        }

    edit_ccg_button = \
        {
            'XPATH': '//*[@class="cloud-config-groups"]//span[@class="table-action-icons table-edit"]'
        }

    delete_ccg_button = \
        {
            'XPATH': '//*[@class="cloud-config-groups"]//span[@class="table-action-icons table-remove"]'
        }

    delete_ccg_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]'
        }


    get_ccg_grid_row = \
        {
            'XPATH': '//div[@class="cloud-config-groups"]//div[@data-dojo-attach-point="gridContent"]'
                     '//table[@class="dgrid-row-table"]'
        }

    ccg_row_name = \
        {
            'CSS_SELECTOR': '.field-name'
        }

    get_ccg_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]'
        }

    get_ccg_description = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]'
        }

    get_form_error = \
        {
            'XPATH': '//span[@class="form-error"]'
        }

    get_ccg_description_manage_page = \
        {
            'XPATH': '//div[@class="cloud-config-group ui-small"]//textarea[@data-dojo-attach-point="description"]'
        }

    ccg_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]'
        }

    ccg_cancel_button = \
        {
            'XPATH': '//button[@class="btn btn-small btn-cancel cancelButton"]'
        }

    ccg_select_cancel_button = \
        {
            'XPATH': '//button[@class="btn btn-small btn-cancel"]'
        }

    ccg_continue_button = \
        {
            'XPATH': "//button[@data-dojo-attach-point='continueBtn']"
        }


    get_device_hostname = \
        {
            'CSS_SELECTOR': '.J-ipaddress'
        }

    get_device_serial = \
        {
            'CSS_SELECTOR': '.field-serialNumber'
        }

    remove_device_from_ccg = \
        {
            'CSS_SELECTOR': '.J-tag-close'
        }

    get_device_ccg_hostname = \
        {
            'XPATH': '//div[@class="top-form-side selected-devices"]//span[@class="ui-tag"]'
        }
