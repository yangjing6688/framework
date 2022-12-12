
class ClassificationRuleWebElementDefinition:
    add_classification_rule = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewClassificationRUles"]//span[@class="table-action-icons table-add"]'
        }

    add_classification_rule_name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='assignName']"
        }

    add_classification_rule_desc = \
        {
            'XPATH': "//*[@data-dojo-attach-point='assignDesc']"
        }

    add_classification_option = \
        {
            'XPATH': '//span[@class="table-action-icons table-drop-add"]'
        }

    get_classification_all_option = \
        {
            'XPATH': '//ul[@class="ui-menu-list"]//li'
        }

    get_ccg_match_type_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="automation-cloud-config-group-chzn-arrow-down"]'
        }

    get_ccg_match_type_option = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-cloudconfiggroupscope"] /li'
        }

    get_ccg_policy_drop_down_item = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul[@class="item-area"]//li'
        }

    get_ccg_policy_select_option_button = \
        {
            'XPATH': '//div[@class="ccg-rule-config"]//span[@data-dojo-attach-point="ipMark"]'
        }

    get_continue_buttons = \
        {
            'XPATH': '//button[@data-dojo-attach-point="continueBtn"]'
        }

    get_save_rule = \
        {
            'XPATH': '//div[@componentpath="AssignmentRule"]//button[@data-dojo-attach-point="saveButton"]'
        }

    get_org_loc = \
        {
            'XPATH': '//span[@data-dojo-attach-point="expandoNode"]',
            'index': 1
        }

    get_country_locations = \
        {
            'XPATH': '//div[@data-dojo-attach-point="rowNode"]'
        }

    get_location_node_icon = \
        {
            'CSS_SELECTOR': '.dijitTreeExpando'
        }

    select_loc_assign = \
        {
            'XPATH': '//div[@class="location-rule-config"]//button[@data-dojo-attach-point="selectButton"]'
        }

    get_ip_object_add = \
        {
            'XPATH': '//div[@class="ip-rule-config"]//span[@data-dojo-attach-point="ipSave"]'
        }

    get_ip_addr_object_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]'
        }

    get_ip_addr_object_ip = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ipAddress"]'
        }

    get_ip_addr_object_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]'
        }

    get_ip_addr_object_subnet = \
        {
            'XPATH': '//input[@data-dojo-attach-point="subnetIp"]'
        }

    get_ip_addr_object_mask = \
        {
            'XPATH': '//input[@data-dojo-attach-point="subnetMask"]'
        }

    get_ip_addr_range_from = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ipRange1"]'
        }

    get_ip_addr_range_to = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ipRange2"]'
        }

    enable_classification_rule_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableClassifications"]'
        }

    select_classification_rules = \
        {
            'CSS_SELECTOR': '.sp-rule-select-norm'
        }

    get_classification_rules = \
        {
            'CSS_SELECTOR': '.field-classifiedEntries'
        }

    delete_classification_rule_from_ssids = \
        {
            'CSS_SELECTOR': '.sp-rule-delete-norm'
        }

    select_classification_rule_from_common_obj = \
        {
            'CSS_SELECTOR': '.dgrid-selector'
        }

    confirmation_dialog_yes_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]'
        }

    get_all_classification_rules = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//*[@role="row"]'
                     '//td[@class="dgrid-cell dgrid-column-0 field-name"]'
        }

    view_all_classification_rules = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewClassificationRUles"]//*[@role="row"]'
        }

    view_all_page = \
        {
            'XPATH': '//a[contains(text(),"100")]'
        }

    get_rule_link_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="linkButton"]'
        }

    click_next_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="nextBtn"]'
        }

    delete_classification_rule_from_common_obj = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewClassificationRUles"]//*[@data-tip="Delete"]'
        }
