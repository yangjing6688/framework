class RouterTemplateWebElementsDefinitions:

    router_settings_tab = \
        {
            'XPATH': "//*[@data-automation-tag='automation-tab-router-settings']",
            'wait_for': 5
        }

    router_settings_slider = \
        {
            'CSS_SELECTOR': '.ui-nav-sider-title',
            'index': 0,
            'wait_for': 5
        }

    network_allocation_tab = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="routerSubmenu"]//li[@data-tab="NetworkAllocation"]',
            
        }

    device_template_tab = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="list1"]//li[contains(text(), "Device Template")]',
            'wait_for': 5
        }

    vpn_service_tab = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="routerSubmenu"]//li[@data-tab="VpnService"]',
            'wait_for': 5
        }

    sd_wan_tab = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="routerSubmenu"]//li[@data-tab="SDWANList"]',
            'wait_for': 5
        }

    router_policy_tab = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="routerSubmenu"]//li[@data-tab="RoutingPolicy"]',
            'wait_for': 5
        }

    router_template_add_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-filter-drop-add',
            'wait_for': 1
        }

    router_template_items_parent = \
        {
            'CSS_SELECTOR': '.ui-menu-list.ui-scroll-menu-list',
            'wait_for': 5
        }

    router_template_items = \
        {
            'CSS_SELECTOR': '.ui-menu-item',
            'wait_for': 5
        }

    router_template_name_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='tplName']",
            'wait_for': 5
        }

    router_template_save_btn_parent = \
        {
            'CSS_SELECTOR': '.bottom',
            'index': 1,
            'wait_for': 5
        }

    router_template_save_btn = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-primary',
            'wait_for': 5
        }

    router_template_save_button = \
        {
            'XPATH': '//fixed-bar[@class="bottom"]//button[@data-dojo-attach-point="saveButton"]',
            'index': 1,
            'wait_for': 5
        }

    router_device_template_grid_rows = {'CSS_SELECTOR': '.dgrid-row', 'wait_for': 5}

    router_new_port_type_name_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='portTypeName']",
            'wait_for': 5
        }

    router_new_port_type_description_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='portTypeDesc']",
            'wait_for': 5
        }

    router_new_port_status_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enablePort']",
            'wait_for': 5
        }

    router_new_port_type_access_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-access']",
            'wait_for': 5
        }

    router_new_port_type_trunk_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-trunk']",
            'wait_for': 5
        }

    router_new_port_type_wan_radio_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-wan']",
            'wait_for': 5
        }

    router_new_port_mac_authentication_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableMAC,auth-mac']",
            'wait_for': 5
        }

    router_new_port_type_enable_ssh_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ssh']",
            'wait_for': 5
        }

    router_new_port_type_enable_telnet_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='telnet']",
            'wait_for': 5
        }

    router_new_port_type_enable_ping_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ping']",
            'wait_for': 5
        }

    router_new_port_type_enable_snmp_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='snmp']",
            'wait_for': 5
        }

    router_template_port_details_grid_rows = \
        {
            'CSS_SELECTOR': '.state-type-access-port',
            
         }

    router_template_add_port_type_link_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add.J-add-widget.portIcon',
            'wait_for': 5
        }

    new_port_type_trunk_allowed_vlan_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='trunkAllowedVlans']",
            'wait_for': 5
        }

    router_new_port_save_btn_parent = \
        {
            'CSS_SELECTOR': '.bottom',
            'wait_for': 5
        }

    router_new_port_save_btn = \
        {
            'CSS_SELECTOR': '.btn.btn-primary',
            'wait_for': 5
        }

    router_new_port_save_button = \
        {
            'XPATH': '//fixed-bar[@class="bottom"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    network_allocation_add_button = \
        {
            'XPATH': '//div[@class="subnet-main-ctn"]//*[@data-dojo-attach-point="actionLeft"]//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    network_allocation_delete_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkAllocationContentArea"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    port_new_vlan_btn_parent = \
        {
            'CSS_SELECTOR': '.dijitPopup Popup',
            'wait_for': 5
        }

    port_new_vlan_btn = \
        {
            'CSS_SELECTOR': '.item-new',
            'wait_for': 5
        }

    port_new_vlan_name_textfield_parent = \
        {
            'CSS_SELECTOR': '.VLANObjectForm',
            'wait_for': 5
        }

    port_new_vlan_name_textfield = \
        {
            'CSS_SELECTOR': '.w200',
            'wait_for': 5
        }

    port_new_vlan_id_textfield_parent = \
        {
            'CSS_SELECTOR': '.VLANObjectForm',
            'wait_for': 5
        }

    port_new_vlan_id_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='defaultVlanId']",
            'wait_for': 5
        }

    port_new_vlan_save_vlan_button_parent = \
        {
            'CSS_SELECTOR': '.btn-area.btn-mir',
            'wait_for': 5
        }

    port_new_vlan_save_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-primary',
            'wait_for': 5
        }

    port_new_vlan_cancel_button_parent = \
        {
            'CSS_SELECTOR': '.btn-area.btn-mir',
            'wait_for': 5
        }

    port_new_vlan_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-cancel',
            'wait_for': 5
        }

    port_new_vlan_select_btn_parent = \
        {
            'CSS_SELECTOR': '.dgrid-row.dgrid-row-odd.ui-state-default',
            'wait_for': 5
        }

    port_new_vlan_select = \
        {
            'XPATH': '//div[@class="dgrid-row dgrid-row-odd ui-state-default"]//div[@data-dojo-attach-point="ipElWrap"]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    port_new_vlan_edit = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipElWrap"]//span[@data-dojo-attach-point="ipEdit"]',
            'index': 3,
            'wait_for': 5
        }

    port_new_vlan_select_btn = \
        {
            'CSS_SELECTOR': '.ui-ip-mark.ui-ip-inactive',
            'wait_for': 5
        }

    port_subnetwork_space_select_btn_parent = \
        {
            'CSS_SELECTOR': '.dgrid-row.dgrid-row-odd.ui-state-default',
            'wait_for': 5
        }

    port_subnetwork_space_select_btn = \
        {
            'CSS_SELECTOR': '.ui-ip-mark.ui-ip-inactive',
            'index': 1,
            'wait_for': 5
        }

    port_subnetwork_select = \
        {
            'XPATH': '//div[contains(@class,"dgrid-row-odd")]//div[contains(@id,"ah/util/form/objects/SubnetObj")]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    port_subnetwork_edit = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipElWrap"]//span[@data-dojo-attach-point="ipEdit"]',
            'index': 4,
            'wait_for': 5
        }

    port_new_vlan_select_new_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//*[@class="ui-ip-list-item"]'
                     '//a[@data-type="vlan-profile"]',
            'wait_for': 5
        }

    port_subnetwork_space_select_new_btn = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//*[@class="ui-ip-list-item"]//a[@data-type="subnetwork"]',
            'wait_for': 5
        }

    port_new_vlan_object_name_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm,messageHolder"]'
                     '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    port_new_vlan_object_vlanid_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm,messageHolder"]'
                     '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    port_new_vlan_object_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="btnArea"]//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    port_new_subnetwork_name_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewNewSubnetwork"]//input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    port_new_subnetwork_description_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewNewSubnetwork"]//textarea[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    network_type_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewNewSubnetwork"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]/a',
            'wait_for': 5,
            'index': 0,
        }

    network_type_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewNewSubnetwork"]'
                     '//ul[@class="chzn-results qa-chzn-results-networktype"]//li',
            'wait_for': 5,
        }

    create_unique_subnetwork_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="rdSubnetTypeUnique"]',
            'wait_for': 5
        }

    replicate_same_subnetwork_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="rdSubnetTypeSame"]',
            'wait_for': 5
        }

    local_ip_address_space_textfield = \
        {
            'XPATH': '//div[@data-dojo-attach-point="viewIPAddressSpace"]//input[@data-dojo-attach-point="locaIPSpace"]',
            'wait_for': 5
        }

    first_ip_as_gateway_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="rdGatewayIpTypeFirst"]',
            'wait_for': 5
        }

    last_ip_as_gateway_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="rdGatewayIpTypeLast"]',
            'wait_for': 5
        }

    enable_dhcp_checkbox= \
        {
            'XPATH': '//div[@data-dojo-attach-point="advancedSettingsContainer"]'
                     '//input[@data-dojo-attach-point="enableDhcp"]',
            'wait_for': 5
        }

    enable_branch_router_as_dhcp_server_radio_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="advancedSettingsContainer"]'
                     '//input[@data-dojo-attach-point="rdDhcpServer"]',
            'wait_for': 5
        }

    lease_time_textfield= \
        {
            'XPATH': '//div[@data-dojo-attach-point="advancedSettingsContainer"]'
                     '//input[@data-dojo-attach-point="leaseTime"]',
            'wait_for': 5
        }

    ntp_server_textfield= \
        {
            'XPATH': '//div[@data-dojo-attach-point="advancedSettingsContainer"]'
                     '//input[@data-dojo-attach-point="ntpServerIp"]',
            'wait_for': 5
        }

    domain_name_textfield= \
        {
            'XPATH': '//div[@data-dojo-attach-point="advancedSettingsContainer"]'
                     '//input[@data-dojo-attach-point="domainName"]',
            'wait_for': 5
        }

    enable_dhcp_relay_radio_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="advancedSettingsContainer"]'
                     '//input[@data-dojo-attach-point="rdDhcpRelayAgent"]',
            'wait_for': 5
        }

    primary_dhcp_server_textfield= \
        {
            'XPATH': '//div[@data-dojo-attach-point="contentDhcpRelayAgent"]'
                     '//input[@data-dojo-attach-point="primaryServer"]',
            'wait_for': 5
        }

    secondary_dhcp_server_textfield= \
        {
            'XPATH': '//div[@data-dojo-attach-point="contentDhcpRelayAgent"]'
                     '//input[@data-dojo-attach-point="secondaryServer"]',
            'wait_for': 5
        }

    dns_service_select_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipElWrap"]//span[@data-dojo-attach-point="ipMark"]',
            'index': 4,
            'wait_for': 5
        }

    dns_service_add_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipElWrap"]//span[@data-dojo-attach-point="ipSave"]',
            'index': 4,
            'wait_for': 5
        }

    dns_service_edit_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipElWrap"]//span[@data-dojo-attach-point="ipEdit"]',
            'index': 4,
            'wait_for': 5
        }

    enable_nat_via_vpn_tunnel_checkbox= \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableNatViaVPN"]',
            'wait_for': 5
        }

    save_subnetwork_button= \
        {
            'XPATH': '//fixed-bar[@class="bottom"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    cancel_subnetwork_button= \
        {
            'XPATH': '//fixed-bar[@class="bottom"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    save_network_allocation_button= \
        {
            'XPATH': '//div[@class="allocation-btn-group"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    router_template_select_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="accesspointListArea"]//span[@data-tip="Select"]',
            'wait_for': 5
        }

    router_template_delete_button= \
        {
            'XPATH': '//div[@data-dojo-attach-point="accesspointListArea"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    default_router_template_select_button = \
        {
            'XPATH': '//div[@class="router-device-template"]//span[@data-tip="Select"]',
            'wait_for': 1
        }

    default_router_template_dialog = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }

    default_router_template_dialog_rsg_rows = \
        {
            'CLASS_NAME': 'dojoxGridRowTable',
            'wait_for': 1
        }

    default_router_template_dialog_cancel_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-cancel',
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 1
        }

    default_router_template_dialog_rsg_row_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector.dijitReset.dijitReset.dijitCheckBox',
            'wait_for': 1
        }

    router_template_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-reusable-grid"]//span[@data-tip="Delete"]',
            'CSS_SELECTOR': '.table-action-icons.table-remove',
            'wait_for': 1
        }

    router_template_delete_confirm_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 1
        }
