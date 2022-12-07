
class ClassificationRuleWebElementDefinition:
    add_classification_rule = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewClassificationRUles"]//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    add_classification_rule_name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='assignName']",
            'wait_for': 5
        }

    add_classification_rule_desc = \
        {
            'XPATH': "//*[@data-dojo-attach-point='assignDesc']",
            'wait_for': 5
        }

    add_classification_option = \
        {
            'XPATH': '//span[@class="table-action-icons table-drop-add"]',
            'wait_for': 5
        }

    get_classification_all_option = \
        {
            'XPATH': '//ul[@class="ui-menu-list"]//li',
            'wait_for': 5
        }

    get_ccg_match_type_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="automation-cloud-config-group-chzn-arrow-down"]',
            'wait_for': 5
        }

    get_ccg_match_type_option = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-cloudconfiggroupscope"] /li',
            'wait_for': 5
        }

    get_ccg_policy_drop_down_item = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul[@class="item-area"]//li',
            'wait_for': 5
        }

    get_ccg_policy_select_option_button = \
        {
            'XPATH': '//div[@class="ccg-rule-config"]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    get_continue_buttons = \
        {
            'XPATH': '//button[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 5
        }

    get_save_rule = \
        {
            'XPATH': '//div[@componentpath="AssignmentRule"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    get_org_loc = \
        {
            'XPATH': '//span[@data-dojo-attach-point="expandoNode"]',
            'wait_for': 5,
            'index': 1
        }

    get_country_locations = \
        {
            'XPATH': '//div[@data-dojo-attach-point="rowNode"]',
            'wait_for': 5,
        }

    get_location_node_icon = \
        {
            'CSS_SELECTOR': '.dijitTreeExpando',
            'wait_for': 5
        }

    select_loc_assign = \
        {
            'XPATH': '//div[@class="location-rule-config"]//button[@data-dojo-attach-point="selectButton"]',
            'wait_for': 5,
        }

    get_ip_object_add = \
        {
            'XPATH': '//div[@class="ip-rule-config"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5,
        }

    get_ip_addr_object_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5,
        }

    get_ip_addr_object_ip = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5,
        }

    get_ip_addr_object_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5,
        }

    get_ip_addr_object_subnet = \
        {
            'XPATH': '//input[@data-dojo-attach-point="subnetIp"]',
            'wait_for': 5,
        }

    get_ip_addr_object_mask = \
        {
            'XPATH': '//input[@data-dojo-attach-point="subnetMask"]',
            'wait_for': 5,
        }

    get_ip_addr_range_from = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ipRange1"]',
            'wait_for': 5,
        }

    get_ip_addr_range_to = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ipRange2"]',
            'wait_for': 5,
        }

    enable_classification_rule_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableClassifications"]',
            'wait_for': 5,
        }

    select_classification_rules = \
        {
            'CSS_SELECTOR': '.sp-rule-select-norm',
            'wait_for': 5
        }

    get_classification_rules = \
        {
            'CSS_SELECTOR': '.field-classifiedEntries',
            'wait_for': 5
        }

    delete_classification_rule_from_ssids = \
        {
            'CSS_SELECTOR': '.sp-rule-delete-norm',
            'wait_for': 5
        }

    select_classification_rule_from_common_obj = \
        {
            'CSS_SELECTOR': '.dgrid-selector',
            'wait_for': 5
        }

    confirmation_dialog_yes_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    get_all_classification_rules = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//*[@role="row"]'
                     '//td[@class="dgrid-cell dgrid-column-0 field-name"]',
            'wait_for': 5,
        }

    view_all_classification_rules = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewClassificationRUles"]//*[@role="row"]',
            'wait_for': 5,
        }

    view_all_page = \
        {
            'XPATH': '//a[contains(text(),"100")]',
            'wait_for': 5,
        }

    get_rule_link_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="linkButton"]',
            'wait_for': 5,
        }

    click_next_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="nextBtn"]',
            'wait_for': 5,
        }

    delete_classification_rule_from_common_obj = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewClassificationRUles"]//*[@data-tip="Delete"]',
            'wait_for': 5,
        }
