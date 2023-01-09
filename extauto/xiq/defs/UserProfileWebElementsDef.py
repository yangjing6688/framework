class UserProfileWebElementsDef:
    # had to update this to use index 1
    user_profile_add = \
        {
            'XPATH': '//span[@class="table-action-icons table-add"]',
            'index': 1,
            'wait_for': 5
        }

    user_profile_name = \
        {
            'XPATH': '//*[@data-automation-tag="automation-user-profile-mgmt-name"]',
            'wait_for': 5
        }

    user_profile_vlan_add = \
        {
            'XPATH': '//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    user_profile_vlan_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    user_profile_vlan_id = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    user_profile_vlan_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    user_profile_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    user_profile_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="additionalSettingsContentArea"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
         }

    user_profile_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    user_profile_delete = \
        {
            'XPATH': '//span[@class="table-action-icons table-remove"]',
            'index': 1,
            'wait_for': 5
        }

    vlan_profile_delete = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnDel"]',
            'wait_for': 5
        }

    user_profile_confirm_delete_no = \
        {
            'XPATH': '//button[@data-dojo-attach-point="noBtn"]',
            'wait_for': 5
        }

    user_profile_confirm_delete_yes = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    user_profile_view_all_pages = \
        {
            'XPATH': '//div[@data-dojo-attach-point="additionalSettingsContentArea"]//a[@data-size="100"]',
            'wait_for': 3
        }

    user_profile_row_cell_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 5
        }

    user_profile_vlan_edit_btn = \
        {
            'XPATH': '//*[@data-automation-tag="automation-undefined-new-vlan-edit-btn"]',
            'wait_for': 3
        }

    user_profile_vlan_apply_vlans_to_device_chkbx = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlanRuleButton"]',
            'wait_for': 3
        }

    user_profile_vlan_apply_vlans_to_device_add = \
        {
            'XPATH': '//*[@data-dojo-attach-point="classificationCtn"]//*[@class="table-action-icons table-add"]',
            'wait_for': 3
        }

    user_profile_vlan_apply_vlans_to_device_vlanid_txtbx = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlanId"]',
            'wait_for': 3
        }

    user_profile_vlan_apply_vlans_to_device_add_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addToVlan"]',
            'wait_for': 3
        }

    user_profile_vlan_rows = \
        {
            'CSS_SELECTOR': '.dojoxGridRow',
            'wait_for': 5
        }

    user_profile_vlan_row_cell_select_rule_href = \
        {
            'CSS_SELECTOR': '.sp-rule-select-norm',
            'wait_for': 5
        }

    user_profile_vlan_row_cell_add_rule_href = \
        {
            'CSS_SELECTOR': '.sp-rule-add-norm',
            'wait_for': 5
        }

    user_profile_vlan_row_rule_rows = \
        {
            'XPATH': '//*[@class="dgrid-cell dgrid-column-0 field-name"]',
            'wait_for': 5
        }

    user_profile_vlan_row_rule_link_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="linkButton"]',
            'wait_for': 3
        }

    user_profile_vlan_row_rule_cancel_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="containerNode"]//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 3
        }

    user_profile_assignment_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="assignName"]',
            'wait_for': 3
        }

    user_profile_assignment_description = \
        {
            'XPATH': '//*[@data-dojo-attach-point="assignDesc"]',
            'wait_for': 3
        }

    user_profile_assignment_add_assignment_rule = \
        {
            'XPATH': '//*[@data-dojo-attach-point="Menu"]',
            'wait_for': 3
        }

    user_profile_assignment_add_user_group = \
        {
            'XPATH': '//*[@data-automation-tag="automation-undefined-user-group"]',
            'wait_for': 3
        }

    user_profile_assignment_add_client_os_type = \
        {
            'XPATH': '//*[@data-automation-tag="automation-undefined-client-os-type"]',
            'wait_for': 3
        }

    user_profile_assignment_add_user_group_rows = \
        {
            'XPATH': '//*[@data-dojo-attach-point="listArea"]/li/label/span',
            'wait_for': 5
        }

    user_profile_assignment_add_client_os_type_rows = \
        {
            'CSS_SELECTOR': '.dojoxGridRow',
            'wait_for': 5
        }

    user_profile_assignment_add_client_os_type_checked_row = \
        {
            'CSS_SELECTOR': '.dojoxGridCell',
            'wait_for': 5
        }

    user_profile_assignment_add_asssignment_rule_select_btn = \
        {
            'XPATH': '//*[@class="ui-dialog-bottom clearfix"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    user_profile_assignment_save_btn = \
        {
            'XPATH': '//*[@class="btn-area btn-mir"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    apply_different_user_profile_to_various_clients_chkbx = \
        {
            'XPATH': '//*[@data-dojo-attach-point="profileCheckbox"]',
            'wait_for': 3
        }

    apply_different_user_profile_add_user_profile = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userprofileListArea"]//*[@class="table-action-icons table-add"]',
            'wait_for': 3
        }

    different_user_profile_add_user_profile_vlan_addbtn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="vlanObjContainer"]//*[@data-dojo-attach-point="ipSave"]',
            'wait_for': 3
        }

    different_user_profile_add_user_profile_save_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buttonEl"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    different_user_profile_vlan_rows = \
        {
            'CSS_SELECTOR': '.dgrid-row',
            'wait_for': 5
        }

    different_user_profile_vlan_rule_optbox = \
        {
            'CSS_SELECTOR': '.dojoxGridCell',
            'index': 0,
            'wait_for': 5
        }
