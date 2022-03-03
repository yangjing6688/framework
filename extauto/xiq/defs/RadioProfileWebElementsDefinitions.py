class RadioProfileWebElementsDefinitions:
    radio_profile_add_radio_profile = \
        {
            'XPATH': '//span[@data-automation-tag="automation-radio-mgmt-add-btn"]',
            'wait_for': 1
        }
    radio_profile_name_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="radioProfileName"]',
            'wait_for': 5
        }
    radio_profile_description = \
        {
            'XPATH': '//*[@data-dojo-attach-point="radioProfileDesc"]',
            'wait_for': 5
        }
    radio_profile_radio_mode_dropdown = \
        {
            'XPATH': '//div[@class="grid_16 clearfix mt50"]//a[@class ="chzn-single"]',
            'index': 0,
            'wait_for': 5
        }

    radio_profile_radio_mode_dropdown_opts = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-radiomodecombo"]/li',
            'wait_for': 5
         }

    radio_profile_maximum_transmit_power = \
        {
            'XPATH': '//*[@data-dojo-attach-point="maxTransmitPower"]',
            'wait_for': 5
        }
    radio_profile_transmit_power_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPowerFloor"]',
            'wait_for': 5
        }
    radio_profile_transmit_power_max_drop = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPowerMaxDrop"]',
            'wait_for': 5
        }
    radio_profile_maximum_number_of_clients = \
        {
            'XPATH': '//*[@data-dojo-attach-point="maxClients"]',
            'wait_for': 5
        }
    radio_profile_deny_connection_requests_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="toggle-deny"]',
            'wait_for': 5
        }
    radio_profile_deny_connection_requests_option_802_11b = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deny802-11b"]',
            'wait_for': 5
        }
    radio_profile_deny_connection_requests_option_802_11abg = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deny802-11abg"]',
            'wait_for': 5
        }
    radio_profile_enable_background_scan_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableBackgroundScan"]',
            'wait_for': 5
        }
    radio_profile_background_scan_interval = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bgScanInterval"]',
            'wait_for': 5
        }
    radio_profile_bg_scan_interval_unit_dropdown = \
        {
            'XPATH': '//div[@id="ah_util_Chosen_30_chzn"]//a[@class="chzn-single"]',
            'index': 1,
            'wait_for': 2
        }

    radio_profile_bg_scan_interval_unit_dropdown_opts = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-bgscanintervalunit"]//li',
            'wait_for': 2
        }

    radio_profile_skip_bg_scan_clients_connected = \
        {
            'XPATH': '//*[@data-dojo-attach-point="neighborhoodCheckBox"]',
            'wait_for': 5
        }
    radio_profile_skip_bg_scan_clients_power_save_mode = \
        {
            'XPATH': '//*[@data-dojo-attach-point="skipScanWhenClientsInPowerSaveMode"]',
            'wait_for': 5
        }
    radio_profile_skip_bg_scan_nw_voice_priority = \
        {
            'XPATH': '//*[@data-dojo-attach-point="skipScanWhenProcessVoiceTraffic"]',
            'wait_for': 5
        }

    radio_profile_channel_selection = \
        {
            'XPATH': '//div[@data-dojo-attach-point="axChannel"]',
            'wait_for': 5
         }
    radio_profile_channel_list_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="axChannel"]//a[@class="chzn-single"]',
            'wait_for': 2
        }

    radio_profile_channel_list_dropdown_opts = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-channelaxghz"]//li',
            'wait_for': 2
        }

    radio_profile_channel_width_dropdown = \
        {
            'XPATH': '//div[@id="ah_util_Chosen_32_chzn"]//a[@class="chzn-single"]',
            'index': 3,
            'wait_for': 5
        }

    radio_profile_channel_width_dropdown_opts = \
        {
            'XPATH': '//*[@data-automation-tag="chzn-drop-ctn"]//ul[@class="chzn-results qa-chzn-results-channelwidth"]',
            'wait_for': 5
        }

    radio_profile_enable_exclude_channels_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableAxChannelSelection"]',
            'wait_for': 5
        }

    radio_profile_channels_avail_for_exclusion = \
        {
            'XPATH': '//*[@data-dojo-attach-point="exclude2gCtn"]//div[@class="channel-list-ctn"]',
            'wait_for': 5
        }
    radio_profile_select_channels_for_exclusion = \
        {
            'XPATH': '//*[@data-dojo-attach-point="channelSelect"]//input[@class="channelBox click-trigger"]',
            'wait_for': 5
        }

    radio_profile_transmission_power = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPower2G"]',
            'wait_for': 5
        }
    radio_profile_transmission_power_Auto = \
        {
            'XPATH': '//div[@data-dojo-attach-point="transmissionPower2G"]//label[@class="radio fn-inline-block"]',
            'index': 0,
            'wait_for': 5
        }
    radio_profile_transmission_power_Manual = \
        {
            'XPATH': '//ul[@class="radio-list"]//*[@data-dojo-attach-point="powerType2GHz-manual"]',
            'wait_for': 5
        }

    wifi1_transmission_power_slider_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPower5GBar_20"]'
                     '//div[@data-dojo-attach-event="press:_onHandleClick"]',
            'wait_for': 5
        }

    wifi0_transmission_power_slider_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="transmissionPower2GBar_20"]'
                     '//div[@data-dojo-attach-event="press:_onHandleClick"]',
            'wait_for': 5
        }
    radio_profile_enable_DFS_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableDynamicFrequencySelection"]',
            'wait_for': 5
        }
    save_radio_profile = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }
    cancel_radio_profile = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    radio_profile_channel_width = \
        {
            'XPATH': '//div[@data-automation-tag="radio-profile-channel-picker-channel-',
            'wait_for': 5
        }

    radio_profile_Mega_80_Hert = \
        {
            'XPATH': '//div[@data-automation-prefix="radio-profile-channel-picker-header-80mhz"]',
            'wait_for': 5
        }

    radio_profile_Mega_160_Hert = \
        {
            'XPATH': '//div[@data-automation-prefix="radio-profile-channel-picker-header-160mhz"]',
            'wait_for': 5
        }

    radio_profile_Mega_40_Hert = \
        {
            'XPATH': '//div[@data-automation-prefix="radio-profile-channel-picker-header-40mhz"]',
            'wait_for': 5
        }

    radio_profile_Mega_20_Hert = \
        {
            'XPATH': '//div[@data-automation-prefix="radio-profile-channel-picker-header-20mhz"]',
            'wait_for': 5
        }

    radio_profile_limit_channel_selection = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableLimitChannelSelection"]',
            'wait_for': 5
        }

    enable_client_transmission_power_control_802_11h_button = \
        {
            'XPATH': '//input[@data-automation-tag="radio-profile-enable-client-power-control"]',
            'wait_for': 5
        }

    radio_profile_channel_model = \
        {
            'XPATH': '//div[@data-dojo-attach-point="csCtn"]/div[2]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    radio_profile_region = \
        {
            'XPATH': '//div[@data-dojo-attach-point="csCtn"]/div[1]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    channel_width_exclusions_uni_1 = \
        {
            'XPATH': '//div[@data-channel-num="unii-1"]',
            'wait_for': 5
        }

    channel_width_exclusions_uni_2 = \
        {
            'XPATH': '//div[@data-channel-num="unii-2"]',
            'wait_for': 5
        }

    channel_width_exclusions_uni_3 = \
        {
            'XPATH': '//div[@data-channel-num="unii-3"]',
            'wait_for': 5
        }

    channel_width_exclusions_unii_2_extended = \
        {
            'XPATH': '//div[@data-channel-num="unii-2-extended"]',
            'wait_for': 5
        }

    channel_width_exclusions_unii_5 = \
        {
            'XPATH': '//div[@data-channel-num="unii-5"]',
            'wait_for': 5
        }

    channel_width_exclusions_unii_6 = \
        {
            'XPATH': '//div[@data-channel-num="unii-6"]',
            'wait_for': 5
        }

    channel_width_exclusions_unii_7 = \
        {
            'XPATH': '//div[@data-channel-num="unii-7"]',
            'wait_for': 5
        }

    channel_width_exclusions_unii_8 = \
        {
            'XPATH': '//div[@data-channel-num="unii-8"]',
            'wait_for': 5
        }

