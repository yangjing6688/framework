class IPFirewallPoliciesDefinitions:

    ip_firewall_policy_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-sider-list-ipFirewallPolicies"]',
            'wait_for': 5
        }

    ip_firewall_policy_add = \
        {
            'XPATH': '//*[@class="table-action-buttons table-action-icons table-add"]',
            'wait_for': 5
        }

    ip_firewall_policy_edit = \
        {
            'XPATH': '//*[@class="table-action-icons table-edit"]',
            'wait_for': 5
        }

    ip_firewall_policy_clone = \
        {
            'XPATH': '//*[@class="table-action-icons table-clone"]',
            'wait_for': 5
        }

    ip_firewall_policy_delete = \
        {
            'XPATH': '//*[@class="table-action-icons table-remove"]',
            'wait_for': 5
        }

    ip_firewall_policy_row = \
        {
            'XPATH': '//*[@data-dojo-attach-point="gridContent"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_desc = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_add_button = \
        {
            'XPATH': '//div//span[contains(@class, "table-action-buttons table-action-icons table-add") and contains(text(), "Add")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_edit_button = \
        {
            'XPATH': '//div//span[contains(@class, "table-action-icons table-edit") and contains(@data-tip(), "Edit")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_delete_button = \
        {
            'XPATH': '//div//span[contains(@class, "table-action-icons table-remove") and contains(@data-tip(), "Delete")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service = \
        {
            'XPATH': '//*[@class="ip-textselect"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_source_ip_input = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_2"]//input[@data-dojo-attach-point="ipEl"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_source_ip_select = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_2"]//input[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_source_ip_sel_lst = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_2"]//div[@class="ui-ip ui-ip-list"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_source_ip_add = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_2"]//input[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_source_ip_add_lst = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_2"]//ul[@data-dojo-attach-point="ipTypeList"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_source_ip_edit = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_2"]//input[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_dest_ip_input = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipEl"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_dest_ip_select = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_dest_ip_sel_lst = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_3"]//div[@class="ui-ip ui-ip-list"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_dest_ip_add = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_dest_ip_add_lst = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_3"]//ul[@data-dojo-attach-point="ipTypeList"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_dest_ip_edit = \
        {
            'XPATH': '//*[@id="ah/util/form/objects/IPObject_3"]//input[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_action = \
        {
            'XPATH': '//*[@class="chzn-single"]//span[contains(text(), "Permit")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_action_lst = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-action"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_logging = \
        {
            'XPATH': '//*[@class="chzn-single"]//span[contains(text(), "Off")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_logging_lst = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-logging-permit"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_select = \
        {
            'XPATH': '//*[@class="hmng-icon-select"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_net_searchbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="categoriesFilter"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_net_cat_list = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="categories"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_net_search_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="searchNetService"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_app_type = \
        {
            'XPATH': '//*[@class="chzn-single"]//span[contains(text(), "Application Name")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_net_app_lst = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-appsearchtype"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_app_searchbox = \
        {
            'XPATH': '//*[data-dojo-attach-point="applicationsFilter"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_app_search_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="searchAppService"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_sel_app_app_lst = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="applications"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add = \
        {
            'XPATH': '//*[@class="hmng-icon-add"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_desc = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_idle_timeout = \
        {
            'XPATH': '//*[@data-dojo-attach-point="idleTimeout"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_ip_protocol = \
        {
            'XPATH': '//*[@class="chzn-single"]//span[contains(text(), "TCP (6)")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_ip_proto_lst = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-ipprotocol"]//li',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_port = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portNumber"]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_alg_type = \
        {
            'XPATH': '//*[@class="chzn-single"]//span[contains(text(), "None")]',
            'wait_for': 5
        }

    ip_firewall_policy_add_service_add_alg_type_lst = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-algtype"]//li',
            'wait_for': 5
        }
