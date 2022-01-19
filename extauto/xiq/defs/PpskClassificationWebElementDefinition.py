
class PpskClassificationWebElementDefinition:
    get_network_dropdown = \
        {
            'XPATH': '//div[contains(@class,"ppsk-group")]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    get_all_network_from_dropdown = \
        {
            'XPATH': '//div[contains(@class,"ppsk-group")]//li[contains(@class,"active-result")]',
            'wait_for': 5
        }

    get_ppsk_classification_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]//*[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    get_ppsk_classification_user_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]//*[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    get_ppsk_classification_user_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]'
                     '//ul[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    add_user_button = \
        {
            'XPATH': '//*[contains(@class, "J-add-user")]',
            'wait_for': 5
        }

    select_classification_rule_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]//a[contains(@class, "J-select-rule")]',
            'wait_for': 5
        }

    classification_all_rule = \
        {
            'XPATH': '//div[@componentpath="PPSKGroup/SelectAssignRuleCopy"]//*[@class="dgrid-row-table"]'
                     '//*[contains(@class, "field-name")]',
            'wait_for': 5
        }

    link_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="linkButton"]',
            'wait_for': 5
        }

    save_button = \
        {
            'XPATH': '//span[@class="J-save-group btn btn-primary-2 btn-small"]',
            'wait_for': 5
        }

    edit_button = \
        {
            'CSS_SELECTOR': '.J-edit-group',
            'wait_for': 2
        }

    user_select_classification_rule_button = \
        {
            'CSS_SELECTOR': '.J-select-rule',
            'wait_for': 2
        }

    ppsk_classification_users_row = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]//div[contains(@class, "dgrid-content")]'
                     '//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    user_assigned_classification_rule = \
        {
            'CSS_SELECTOR': '.field-classAssign',
            'wait_for': 2
        }

    select_all_ppsk_users = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]//div[contains(@class,"dgrid-autoheight")]'
                     '//input[@type="checkbox"]',
            'wait_for': 5
        }

    delete_ppsk_user = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ppskGroupSetting"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    yes_confirmation_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }
