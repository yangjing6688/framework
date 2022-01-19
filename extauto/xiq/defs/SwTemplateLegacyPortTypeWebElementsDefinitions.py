class SwTemplateLegacyPortTypeWebElementDefinitions:
    save_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 1
        }

    name = \
        {
            'XPATH': "//*[@data-dojo-attach-point='portTypeName']",
            'wait_for': 5
        }

    port_type_desc = \
        {
            'XPATH': "//input[@data-dojo-attach-point='portTypeDesc']",
            'wait_for': 5
        }

    status = \
        {
            'XPATH': "//*[@name='services-field-1' and @data-dojo-attach-point='enablePort']",
            'wait_for': 1
        }

    port_type_access = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-access']",
            'wait_for': 1
        }

    port_type_trunk = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-trunk']",
            'wait_for': 1
        }

    port_type_phone = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-phone']",
            'wait_for': 1
        }

    port_type_auto_sense = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port-auto-sense']",
            'wait_for': 1
        }

    transmission_type = \
        {
            'XPATH': "//*[@data-dojo-attach-point='transmissionTypeSection']/div[2]/div/select",
            'wait_for': 1
        }

    transmission_speed = \
        {
            'XPATH': "//*[@data-dojo-attach-point='portSettingsTransCtn']/div[2]/div[2]/div/select",
            'wait_for': 1
        }

    access_vlan_select = \
        {
            'XPATH': "//*[@data-dojo-attach-point='dynamic-AVLAN']/div[1]/div[2]/div/div/span",
            'wait_for': 1
        }

    access_vlan_add = \
        {
            'XPATH': "//*[@data-dojo-attach-point='dynamic-AVLAN']/div[1]/div[2]/div/div/span",
            'wait_for': 1
        }

    access_vlan_name = \
        {
            'XPATH': "//*[@class='switch-template']/*[@data-dojo-attach-point=modalcontainer/div/div[2]/div[2]/input",
            'wait_for': 1
        }

    access_vlan_id = \
        {
            'XPATH': "//*[@class='switch-template']/*[@data-dojo-attach-point=modalcontainer/div/div[3]/div[2]/input",
            'wait_for': 1
        }

    lldp_transmit = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableLldpTransmit']",
            'wait_for': 1
        }

    lldp_receive = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableLldpReceive']",
            'wait_for': 1
        }

    cdp_receive = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableCdpReceive']",
            'wait_for': 1
        }

    client_reporting = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableClientReporting']",
            'wait_for': 1
        }

    stp_status = \
        {
            'XPATH': "//input[@data-dojo-attach-point='stpStatus']",
            'wait_for': 1
        }

    edge_port = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableEdgePort']",
            'wait_for': 1
        }

    bpdu_protection = \
        {
            'XPATH': "//*[@data-dojo-attach-point='bpduProtection']",
            'wait_for': 1
        }

    stp_priority = \
        {
            'XPATH': "//*[@data-dojo-attach-point='stpPriority']",
            'wait_for': 1
        }

    sc_broadcast = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableBroadcastTraffic']",
            'wait_for': 1
        }

    sc_unicast = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableUnknownUnicastTraffic']",
            'wait_for': 1
        }

    sc_multicast = \
        {
            'XPATH': "//*[@data-dojo-attach-point='enableMulticastTraffic']",
            'wait_for': 1
        }

    sc_threshold_option = \
        {
            'XPATH': "//*[@data-dojo-attach-point='stormControlThresholdOption']",
            'wait_for': 1
        }

    sc_rate_limit_type = \
        {
            'XPATH': "//*[@data-dojo-attach-point='rateLimitType']",
            'wait_for': 1
        }

    sc_rate_limit_value = \
        {
            'XPATH': "//*[@data-dojo-attach-point='rateLimitValue']",
            'wait_for': 1
        }

