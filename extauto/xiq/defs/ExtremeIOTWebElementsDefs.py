class ExtremeIOTWebElementsDefs:

    extreme_iot_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="additionalSettingsContentArea"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    extreme_iot_edit_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="additionalSettingsContentArea"]//span[@data-tip="Edit"]',
            'wait_for': 5
        }

    extreme_iot_user_profile_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="profileName"]',
            'wait_for': 5
        }

    extreme_iot_policy_group_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="groupName"]',
            'wait_for': 5
        }

    extreme_iot_policy_group_vlan_add = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlanObjContainer"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    extreme_iot_policy_group_vlan_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    extreme_iot_policy_group_vlan_id = \
        {
            'XPATH': '//*[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    extreme_iot_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_enable = \
        {
            'XPATH': '//*[@data-dojo-attach-point="firewallSwitch"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_ip_add = \
        {
            'XPATH': '//*[@data-dojo-attach-point="firewallListContainer"]//span[@data-tip="Add"]',
            'wait_for': 5,
            'index': 2
        }

    extreme_iot_usr_profile_firewall_service_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceIp"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_service_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="categories"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_service_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="firewallChildNode"]//button[@data-dojo-attach-point="saveDialog"]',
        # // * [ @ componentpath = "CreateIpFirewallRule"] // button[ @ data - dojo - attach - point = "saveDialog"]
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_applications = \
        {
            'XPATH': '//*[@data-dojo-attach-point="taber"]//a[contains(text(), "Applications")]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_applications_filter = \
        {
            'XPATH': '//*[@data-dojo-attach-point="applicationsFilter"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_applications_search = \
        {
            'XPATH': '//*[@data-dojo-attach-point="searchAppService"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_applications_select_all = \
        {
            'XPATH': '//*[@data-dojo-attach-point="applicationAll"]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_type_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="firewallFor"]//span[contains(text(), "Outbound Traffic")]',
            'wait_for': 5
        }

    extreme_iot_usr_profile_firewall_type_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="firewallFor"]//ul/li',
            'wait_for': 5
        }

    extreme_iot_user_profile_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    extreme_iot_user_profile_list = \
        {
            'XPATH': '//*[@class="dgrid-content ui-widget-content"]/div',
            'wait_for': 5
        }

    extreme_iot_policy_group_user_profile_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mainContent"]//div[@data-automation-tag="chzn-container-ctn"]//span[contains(text(), "Select One")]',
            'wait_for': 5
        }

    extreme_iot_policy_group_user_profile_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mainContent"]//ul[@class="chzn-results qa-chzn-results-profilelist"]',
            'wait_for': 5
        }

    extreme_iot_policy_group_save = \
        {
            'XPATH': '//*[@data-dojo-attach-point="continueBtn"]',
            'wait_for': 5
        }

    extreme_iot_policy_group_list = \
        {
            'XPATH': '//*[@class="dgrid-content ui-widget-content"]/div[@role="row"]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="actionRight"]//a[contains(text(), "Change ExtremeIoT Status")]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_assign = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-ap-manage-ap"]//a[contains(text(), "Assigned")]',
            'wait_for': 5
        }

    extreme_iot_dev_list = \
        {
            'XPATH': '//*[@class="dgrid-content ui-widget-content"]//div[@role="row"]',
            'wait_for': 5
        }

    extreme_iot_dev_edit = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-list"]//span[@data-tip="Edit"]',
            'wait_for': 5
        }

    extreme_iot_dev_delete = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-list"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    extreme_iot_dev_action_btn = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-actions_normal-btn"]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-defender-setup"]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_policy_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="npName"]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_dev_timezone_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-container-ctn"]//span[contains(text(), "(GMT-11:00) Pacific/Midway")]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_dev_timezone_options = \
        {
            'XPATH': '//*[@class="ChosenList"]//ul[@data-automation-tag="chzn-results-ctn"]/li',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_dev_template_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="templateName"]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_country_dropdown = \
        {
            'XPATH': '//*[@class="ChosenList country-code"]//a/span',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_country_options = \
        {
            'XPATH': '//*[@class="ChosenList country-code"]//ul/li',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_port_type_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portTypeName"]',
            'wait_for': 5
        }

    extreme_iot_dev_change_extremeIOT_status_finish = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createBtn"]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_policy_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="npExistingCtn"]//span',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_policy_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="npExistingCtn"]//ul/li',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_policy_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="npExistingCtn"]/input',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_policy_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="npName"]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_dev_timezone_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-container-ctn"]//span[contains(text(), "(GMT-11:00) Pacific/Midway")]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_dev_timezone_options = \
        {
            'XPATH': '//*[@class="ChosenList"]//ul[@data-automation-tag="chzn-results-ctn"]/li',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_template_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="templateLabel"]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_template_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="templateExistingCtn"]//span',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_template_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="templateExistingCtn"]//ul/li',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_template_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="templateName"]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_country_dropdown = \
        {
            'XPATH': '//*[@class="ChosenList country-code"]//a/span',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_country_options = \
        {
            'XPATH': '//*[@class="ChosenList country-code"]//ul/li',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_port_type_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portTypeExistingCtn"]/input',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_port_type_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portTypeName"]',
            'wait_for': 5
        }

    extreme_iot_dev_extremeIOT_setup_finish = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createBtn"]',
            'wait_for': 5
        }

    extreme_iot_clients_list = \
        {
            'XPATH': '//*[@class="dgrid-content ui-widget-content"]//div[@role="row"]',
            'wait_for': 5
        }

    extreme_iot_title_check = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-container-ctn"]//span[contains(text(), "ExtremeIoT View")]',
            'wait_for': 5
        }

