from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.RadioProfileWebElements import RadioProfileWebElements

from extauto.common.WebElementHandler import WebElementHandler
from extauto.common.CloudDriver import CloudDriver


class RadioProfile (RadioProfileWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.radprof_web_elements = RadioProfileWebElements()
        self.web = WebElementHandler()
        self.common_validation = CommonValidation()
        # self.driver = extauto.common.CloudDriver.cloud_driver

    def add_radio_profile(self, radio_profile_name):
        """
        - Flow: Configure --> Common Objects --> Policy --> Radio Profile
        - This keyword is to Add a Radio profile from the radio grid
        - Keyword Usage:
        - ``Add Radio Profile  ${RADIO_PROFILE_NAME}``

        :param radio_profile_name: Name of the Radio profile
        :return: 1 if Radio profile named successfully else -1
        """
        self.utils.print_info("Navigating to Common Objects ---> Radio Profiles")
        self.navigator.navigate_to_radio_profile()
        sleep(3)

        self.utils.print_info("Click on Add radio profile button")
        self.auto_actions.click_reference(self.radprof_web_elements.get_add_radio_profile_button)
        sleep(2)

        self.utils.print_info("Add radio profile name")
        self.auto_actions.send_keys(self.radprof_web_elements.get_radio_profile_name(), radio_profile_name)
        sleep(3)
        return 1

    def choose_radio_profile_radio_mode(self, radio_mode=None):
        """
        - This keyword is to configure radio mode in the radio profile
        - Keyword Usage:
        - ``Choose Radio Profile Radio Mode ${RADIO_MODE}``

        :param radio_mode: Select the radio mode ("b/g" or "g/n" or  "ax (2.4GHz)" or "a" or "a/n" or "ac" or
                                                                                                    "ax (5GHz)")
        :return: 1 if Chosen Radio Mode Successfully else -1
        """
        self.utils.print_info("Clicking on radio modes dropdown")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_radio_mode_dropdown)

        self.utils.print_info("Selecting the radio mode")
        self.auto_actions.select_drop_down_options(self.radprof_web_elements.
                                                   get_radio_profile_radio_mode_dropdown_opts(), radio_mode)
        self.screen.save_screen_shot()
        sleep(3)
        return 1

    def config_radio_profile_max_transmit_power(self, max_transmit_power):
        """
        - This keyword is to configure the maximum transmit power in radio profile
        - Keyword Usage:
        - ``Config Radio Profile Max Transmit Power ${MAX_TRANSMIT_POWER}``

        :param max_transmit_power: Configure maximum transmit power
        :return: 1 if success else -1
        """
        self.utils.print_info("Selecting maximum transmit power")
        self.auto_actions.send_keys(self.radprof_web_elements.get_radio_profile_max_tx_power(), max_transmit_power)
        sleep(3)
        return 1

    def config_radio_profile_tx_power_floor(self, tx_power_floor):
        """
        - This keyword is to configure the transmission power floor in radio profile
        - Keyword Usage:
        - ``Config Radio Profile Tx Power Floor ${TX_PWR_FLOOR}``

        :param tx_power_floor: Configure transmission power floor
        :return: 1 if success else -1
        """
        self.utils.print_info("Selecting Transmission Power Floor")
        self.auto_actions.send_keys(self.radprof_web_elements.get_radio_profile_tx_power_floor(), tx_power_floor)
        sleep(3)
        return 1

    def config_radio_profile_tx_power_max_drop(self, tx_power_max_drop):
        """
        - This keyword is to configure the transmission power max drop in radio profile
        - Keyword Usage:
        - ``Config Transmission Power Max Drop ${TX_PWR_MAX_DROP}``

        :param tx_power_max_drop: Configure transmission power max drop in the radio profile
        :return: 1 if success else -1
        """
        self.utils.print_info("Selecting Transmission Power Max Drop")
        self.auto_actions.send_keys(self.radprof_web_elements.get_radio_profile_tx_power_max_drop(), tx_power_max_drop)
        sleep(3)
        return 1

    def config_radio_profile_max_no_of_clients(self, max_no_of_clients):
        """
        - This keyword is to configure max no of clients in the radio profile
        - Keyword Usage:
        - ``Config Radio Profile Max No Of Clients ${MAX_CLIENTS}``

        :param max_no_of_clients: Configure maximum number of clients in the radio profile
        :return: 1 if success else -1
        """
        self.utils.print_info("Selecting Maximum No of Clients")
        self.auto_actions.send_keys(self.radprof_web_elements.get_radio_profile_max_no_of_clients(), max_no_of_clients)
        sleep(5)
        self.utils.print_info("Scrolling the page down")
        self.auto_actions.scroll_down()
        sleep(3)
        return 1

    def config_radio_profile_bg_scan_interval(self, bg_scan_interval):
        """
        - This Keyword is to configure the Background Scan Interval and its parameters
        - Keyword Usage:
        - ``Config Radio Profile BG Scan Interval ${BG_SCAN_INTERVAL}``

        :param bg_scan_interval: Enable/Disable Background Scan, Background Scan Interval
        :return: 1 if success else -1
        """
        self.utils.print_info("Configuring Background Scan Interval")
        self.auto_actions.send_keys(self.radprof_web_elements.get_radio_profile_background_scan_interval(),
                                    bg_scan_interval)
        sleep(3)
        return 1

    def config_radio_profile_bg_scan_interval_unit(self, bg_scan_interval_unit=None):
        """
        - This Keyword is to configure the Background Scan Interval Unit
        - Keyword Usage:
        - ``Config BG Scan Int Unit ${BG_SCAN_INT_UNIT}``

        :param bg_scan_interval_unit: Background Scan Interval Unit
        :return: 1 if success else -1
        """
        self.utils.print_info("Clicking on the drop-down options of BG Scan Interval Unit")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_bg_scan_interval_unit_dropdown),
        self.utils.print_info("Selecting Background Scan Interval Unit")
        self.auto_actions.select_drop_down_options(self.radprof_web_elements.
                                                   get_radio_profile_bg_scan_interval_unit_dropdown_opts(), bg_scan_interval_unit)
        sleep(3)
        return 1

    def config_radio_profile_skip_bg_scan_when_clients_connected(self, skip_bg_scan_clients_connected):
        """
        - This Keyword is to Skip the Background Scan when clients are connected
        - Keyword Usage:
        - ``Skip BG Scan When Clients Connected ${CLIENTS_CONNECTED}``

        :param skip_bg_scan_clients_connected: Skip background scan when clients are connected
        :return: 1 if success else -1
        """
        self.utils.print_info("Skipping Background Scan when Clients are Connected")
        self.auto_actions.click_reference(self.radprof_web_elements.
                                          get_radio_profile_skip_bg_scan_clients_connected_checkbox)
        sleep(3)
        return 1

    def config_radio_profile_skip_bg_scan_clients_pwr_save_mode(self, skip_bg_scan_pwr_save):
        """
        - This Keyword is to Skip the Background Scan when clients are in power save mode
        - Keyword Usage:
        - ``Skip BG Scan When Clients are in Power Save Mode ${CLIENTS_PWR_SAVE_MODE}``

        :param skip_bg_scan_pwr_save:Skip background scan when clients are in Power Save Mode
        :return: 1 if success else -1
        """
        self.utils.print_info("Skipping Background Scan when Clients Connected are in Power Save Mode")
        self.auto_actions.click_reference(self.radprof_web_elements.
                                          get_radio_profile_skip_bg_scan_clients_power_save_mode_checkbox)
        sleep(3)
        return 1

    def config_radio_profile_skip_bg_scan_nw_voice_priority(self, skip_bg_scan_nw_voice_priority):
        """
        - This Keyword is to Skip the Background Scan when clients has Network Voice Priority
        - Keyword Usage:
        - ``Skip BG Scan When Clients has network voice priority ${CLIENTS_NW_VOICE_PRIORITY}``

        :param skip_bg_scan_nw_voice_priority: Skip background scan when clients has network voice priority
        :return: 1 if success else -1
        """
        self.utils.print_info("Skipping Background Scan when N/w Traffic Voice Priority detected")
        self.auto_actions.click_reference(self.radprof_web_elements.
                                          get_radio_profile_skip_bg_scan_nw_voice_priority_checkbox)

        self.utils.print_info("Scrolling the page down...")
        self.auto_actions.scroll_down()
        sleep(5)
        return 1

    def config_radio_profile_radio_channel(self, channel_selection=None):
        """
        - This keyword is to configure channel in the radio profile
        - Keyword Usage:
        - ``Choose Radio Profile Channel ${CHANNEL}``

        :param channel_selection: Select any channel ("1-14" or "36-165")
        :return: 1 if channel is chosen Successfully else -1
        """
        self.utils.print_info("Scrolling the page down...")
        self.auto_actions.scroll_down()

        self.utils.print_info("Clicking on Channels list drop-down")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_channel_list_dropdown)
        sleep(3)
        self.screen.save_screen_shot()

        self.utils.print_info("Selecting channel from the drop-down")
        self.auto_actions.select_drop_down_options(self.radprof_web_elements.
                                                   get_radio_profile_channel_list_dropdown_opts(), channel_selection)
        self.screen.save_screen_shot()
        return 1

    def choose_radio_profile_channel_width(self, channel_width=None):
        """
        - This keyword is to configure channel width in the radio profile
        - Keyword Usage:
        - ``Choose Radio Profile Channel Width ${CHANNEL_WIDTH} ``

        :param channel_width : Select any channel width("20MHz" or "40MHz" or "80MHz")
        :return: 1 if channel_width is chosen Successfully else -1
        """
        self.utils.print_info("Clicking on channel-width drop-down")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_channel_width_dropdown)
        sleep(3)
        self.screen.save_screen_shot()

        self.utils.print_info("Selecting channel-width from the drop-down")
        self.auto_actions.select_drop_down_options(self.radprof_web_elements.
                                                   get_radio_profile_channel_width_dropdown_opts(), channel_width)
        self.screen.save_screen_shot()
        sleep(3)
        return 1

    def enable_exclude_channels_btn(self, exclude_channels_btn):
        """
        - This keyword is to Enable Exclude Channels option in the radio profile
        - Keyword Usage:
        - ``Enable Exclude Channels Button ${EXCLUDE_CHANNELS_BUTTON} ``

        :param exclude_channels_btn : Enable Exclude Channels option
        :return: 1 if channels are chosen for exclusion Successfully else -1
        """
        self.utils.print_info("Enabling Exclude Channels option")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_enable_exclude_channels_button)
        self.screen.save_screen_shot()

        self.utils.print_info("Checking for the channels available for exclusion")
        self.auto_actions.screen(self.radprof_web_elements.get_radio_profile_channels_avail_for_exclusion())
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Selecting the channels for exclusion")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_select_channels_for_exclusion)
        self.screen.save_screen_shot()

        self.utils.print_info("Scrolling the page down...")
        self.auto_actions.scroll_down()
        sleep(3)
        return 1

    def disable_exclude_channels_btn(self, disable_exclude_channels_opt):
        """
        - This keyword is to Disable Exclude Channels option in the radio profile
        - Keyword Usage:
        - ``Disable Exclude Channels Button ${EXCLUDE_CHANNELS_BUTTON} ``

        :param disable_exclude_channels_opt:
        :return: 1 if exclude channels button is disabled successfully else -1
        """
        self.utils.print_info("Disabling the Exclude Channels option")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_enable_exclude_channels_button)
        self.screen.save_screen_shot()
        sleep(2)
        return 1

    def conf_transmission_power_auto(self, tx_power_auto):
        """
        - This Keyword is to Configure the Transmission Power as "Auto" in the Radio Profile
        - Keyword Usage:
         ``Conf Transmission Power Auto ${TX_POWER_AUTO}``

        :param tx_power_auto: Transmission Power Auto
        :return: 1 if success else -1
        """
        self.utils.print_info("Configuring tx power Auto")
        self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_transmission_power_auto)
        sleep(2)
        self.screen.save_screen_shot()
        return 1

    def conf_transmission_power_manual(self, tx_power_manual=None):
        """
        - This Keyword is to Configure the Transmission Power as "Manual" in the Radio Profile
        - Keyword Usage:
         ``Conf Transmission Power Auto ${TX_POWER_MANUAL}``

        :param tx_power_manual:
        :return: 1 if success else -1
        """
        self.utils.print_info("Configuring tx power Manual")
        radio_mode = self.auto_actions.select_drop_down_options(self.radprof_web_elements.
                                                                get_radio_profile_radio_mode_dropdown_opts())
        if radio_mode == "b/g" or "g/n" or "ax (2.4GHz)":
            self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_tx_power_slider_24GHz)
        if radio_mode == "a" or "a/n" or "ac" or "ax (5GHZ)":
            self.auto_actions.click_reference(self.radprof_web_elements.get_radio_profile_tx_power_slider_5GHz)
        return 1

    def enable_dfs_button(self, enable_dfs_btn):
        """
        - This Keyword is to Enable the DFS button
        - Keyword Usage:
         -``Enable DFS Btn ${DFS_BTN}``

        :param enable_dfs_btn: enable dfs button
        :return: 1 if DFS button is enabled else -1
        """
        self.utils.print_info("Enabling the DFS option")
        self.auto_actions.enable_radio_button(self.radprof_web_elements.get_radio_profile_enable_dfs_button())
        return 1

    def disable_dfs_button(self, disable_dfs_btn):
        """
        - This Keyword is to Disable the DFS button
        - Keyword Usage:
         -``Disable DFS Btn ${DFS_BTN}``

        :param disable_dfs_btn: disable dfs button
        :return: 1 if success else -1
        """
        self.utils.print_info("Disabling the DFS option")
        self.auto_actions.disable_radio_button(self.radprof_web_elements.get_radio_profile_enable_dfs_button())
        return 1

    def save_radio_profile(self, save_radio_profile, **kwargs):
        """
        - This Keyword is to Save the Radio Profile
        - Keyword Usage:
         -``Save Radio Profile ${RADIO_PROFILE_NAME}``

        :param save_radio_profile: Save the Radio Profile
        :return: 1 if radio profile was saved successfully else -1
        """
        self.utils.print_info("saving the radio profile")
        self.auto_actions.click_reference(self.radprof_web_elements.get_save_radio_profile)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        sleep(5)

        tool_tip_text = tool_tip.tool_tip_text

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Radio profile was saved successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Radio profile was saved successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "save_radio_profile() failed. Unable to save Radio profile"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def cancel_radio_profile(self, cancel_radio_profile):
        """
        - This Keyword is to Cancel the Radio Profile
        - Keyword Usage:
         -``Cancel Radio Profile ${RADIO_PROFILE_NAME}``
        :param cancel_radio_profile: Cancel the radio profile
        :return: 1 if radio profile was cancelled else -1
        """
        self.utils.print_info("cancelling radio profile")
        self.auto_actions.click_reference(self.radprof_web_elements.get_cancel_radio_profile)
        sleep(2)

    def verify_radio_profile_channel_width_and_channels(self, channels, mode='included', channel_width='default', **kwargs):
        """
        - This keyword validates the channels to be exclusive, inclusive, by default and not by default
        - Keyword Usage:
            @channels    7 12 4 5
        - ``check_radio_profile_channel_width_and_channels  $channels  mode=included  channel_width=80``

        :param channels: list of valid channels
        :param mode: channel is either enabled, disabled, included, excluded channel
        :param channel_width: channel width
        :return: 1  else - 1
        """
        sleep(5)
        element = None

        if channel_width in ['80', '160', '40', '20']:
            if channel_width == '80':
                element = self.radprof_web_elements.get_radio_profile_Mega_80_Hert()
            elif channel_width == '160':
                element = self.radprof_web_elements.get_radio_profile_Mega_160_Hert()
            elif channel_width == '40':
                element = self.radprof_web_elements.get_radio_profile_Mega_40_Hert()
            elif channel_width == '20':
                element = self.radprof_web_elements.get_radio_profile_Mega_20_Hert()

            enabled_text = element.get_attribute("class")
            self.utils.print_info(" Attribute Text: " + str(enabled_text))

            if enabled_text.find("disabled") != -1:
                kwargs['fail_msg'] = f"verify_radio_profile_channel_width_and_channels() failed." \
                                     f"Channel with is not by default {channel_width}"
                self.common_validation.fault(**kwargs)
                return -1

        for channel in channels:
            self.utils.print_info("Verify the channel " + str(channel))
            locator = self.radprof_web_elements.get_radio_profile_channel_width(str(channel))
            element = self.web.get_element(locator)

            if element == None:
                kwargs['fail_msg'] = f"verify_radio_profile_channel_width_and_channels() failed." \
                                     f" Button does not exist {channel}"
                self.common_validation.fault(**kwargs)
                return -1

            enabled_text = element.get_attribute("class")
            self.utils.print_info(" Attribute Text: " + str(enabled_text))

            if mode == 'enabled':
                if enabled_text.find("enabled") == -1:
                    kwargs['fail_msg'] = f"verify_radio_profile_channel_width_and_channels() failed." \
                                         f"channel is not by default {channel}"
                    self.common_validation.failed(**kwargs)
                    return -1
            elif mode == 'disabled':
                if enabled_text.find("disabled") == -1:
                    kwargs['fail_msg'] = f"verify_radio_profile_channel_width_and_channels() failed." \
                                         f"channel is by default {channel}"
                    self.common_validation.failed(**kwargs)
                    return -1
            elif mode == 'included':
                if enabled_text.find("included") == -1:
                    kwargs['fail_msg'] = f"verify_radio_profile_channel_width_and_channels() failed." \
                                         f"channel is not included: {channel}"
                    self.common_validation.failed(**kwargs)
                    return -1
            elif mode == 'excluded':
                if enabled_text.find("excluded") == -1:
                    kwargs['fail_msg'] = f"verify_radio_profile_channel_width_and_channels() failed." \
                                         f"channel is not excluded: {channel}"
                    self.common_validation.failed(**kwargs)
                    return -1
        kwargs['pass_msg'] = "Verified radio profile channel width and channels"
        self.common_validation.passed(**kwargs)
        return 1

    def select_radio_profile_excluded_channels(self, channels, **kwargs):
        """
        - This Keyword selects the valid channels to be exclusive
        - Keyword Usage:
            @channels   7 12 4 5
        -``select_excluded_channels  $channels   ``

        :param channels: list of valid channels
        :return: 1  else -1
        """

        for channel in channels:
            self.utils.print_info(" Verify the channel if exists " + str(channel))
            locator = self.radprof_web_elements.get_radio_profile_channel_width(str(channel))
            self.utils.print_info(" LOCATOR  " + str(locator))
            element = self.web.get_element(locator)

            if element is None:
                kwargs['fail_msg'] = f"select_radio_profile_excluded_channels() failed. Channel does not exist {channel}"
                self.common_validation.fault(**kwargs)
                return -1

            try:
                element.click()
                self.utils.print_info("select the channel to be exclusive " + str(channel))
            except:
                kwargs['fail_msg'] = f"select_radio_profile_excluded_channels() failed. " \
                                     f"Not able to select the channel to be exclusive {str(channel)}"
                self.common_validation.failed(**kwargs)
                return -1

        kwargs['pass_msg'] = "Selected the valid channels to be exclusive"
        self.common_validation.passed(**kwargs)
        return 1

    def get_radio_profile_details(self, **kwargs):
        """
        - This keyword will retrieve the all fields in the device configuration interface WiFi2 page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> interface settings --> WiFi2
        - Keyword Usage:
        - ``get_device_configuration_interface_WiFi2_details  ''

        """

        sleep(5)
        self.utils.print_info("Retrieve the device configuration interface wireless Wiffi2")

        try:
            radio_profile_info = dict()
            radio_profile_info["radio_profile_name"] = self.get_radio_profile_name().get_attribute("value")
            radio_profile_info["description"] = self.get_radio_profile_description().get_attribute("value")
            radio_profile_info["supported_radio_modes"] = self.get_radio_profile_radio_mode_dropdown().text
            radio_profile_info["radio_profile_maximum_transmit_power"] = self.get_radio_profile_max_tx_power().get_attribute("value")
            radio_profile_info["radio_profile_transmit_power_floor"] = self.get_radio_profile_tx_power_floor().get_attribute("value")
            radio_profile_info["transmission_power_max_drop"] = self.get_radio_profile_tx_power_max_drop().get_attribute("value")
            radio_profile_info["maximum_number_of_clients"] = self.get_radio_profile_max_no_of_clients().get_attribute("value")
            radio_profile_info["background_scan_interval"] = self.get_radio_profile_background_scan_interval().get_attribute("value")
            radio_profile_info["channel_auto_or_manual"] = self.get_radio_profile_channel_list_dropdown().text
            radio_profile_info["channel_model"] = self.get_radio_profile_channel_model().text
            radio_profile_info["region"] = self.get_radio_profile_region().text
            radio_profile_info["background_scran_every"] = self.get_radio_profile_background_scan_interval().get_attribute("value")

            if self.get_radio_profile_deny_connection_requests_checkbox().is_selected():
                radio_profile_info["deny_connection_requests"] = 'ON'
            else:
                radio_profile_info["deny_connection_requests"] = 'OFF'

            if self.get_radio_profile_deny_connection_requests_802_11b_checkbox().is_selected():
                radio_profile_info["802_11b"] = 'ON'
            else:
                radio_profile_info["802_11b"] = 'OFF'

            if self.get_radio_profile_deny_connection_requests_802_11abg_checkbox().is_selected():
                radio_profile_info["802_11abg"] = 'ON'
            else:
                radio_profile_info["802_11abg"] = 'OFF'

            if self.get_radio_profile_skip_bg_scan_clients_connected_checkbox().is_selected():
                radio_profile_info["clients_connected"] = 'ON'
            else:
                radio_profile_info["clients_connected"] = 'OFF'

            if self.get_radio_profile_skip_bg_scan_clients_power_save_mode_checkbox().is_selected():
                radio_profile_info["clients_power_save_mode"] = 'ON'
            else:
                radio_profile_info["clients_power_save_mode"] = 'OFF'

            if self.get_radio_profile_skip_bg_scan_clients_connected_checkbox().is_selected():
                radio_profile_info["clients_are_connected"] = 'ON'
            else:
                radio_profile_info["clients_are_connected"] = 'OFF'

            if self.get_radio_profile_skip_bg_scan_clients_power_save_mode_checkbox().is_selected():
                radio_profile_info["clients_power_save_mode"] = 'ON'
            else:
                radio_profile_info["clients_power_save_mode"] = 'OFF'

            if self.get_radio_profile_skip_bg_scan_nw_voice_priority_checkbox().is_selected():
                radio_profile_info["network_voice_priority"] = 'ON'
            else:
                radio_profile_info["network_voice_priority"] = 'OFF'

            if self.get_radio_profile_transmission_power_manual().is_selected():
                radio_profile_info["transmission_power"] = 'Manual'
            else:
                radio_profile_info["transmission_power"] = 'Auto'

            if self.get_radio_profile_limit_channel_selection_button().is_selected():
                radio_profile_info["limit_channel_selection"] = 'ON'
            else:
                radio_profile_info["limit_channel_selection"] = 'OFF'

            if self.get_enable_client_transmission_power_control_802_11h_button().is_selected():
                radio_profile_info["transmission_power_control"] = 'ON'
            else:
                radio_profile_info["transmission_power_control"] = 'OFF'

            if self.get_enable_client_transmission_power_control_802_11h_button().is_selected():
                radio_profile_info["transmission_power_control"] = 'ON'
            else:
                radio_profile_info["transmission_power_control"] = 'OFF'

            if self.get_radio_profile_enable_background_scan_button().is_selected():
                radio_profile_info["background_scan"] = 'ON'
            else:
                radio_profile_info["background_scan"] = 'OFF'
        except:
            kwargs['fail_msg'] = "get_radio_profile_details() failed. Fail to retrieve one of the fields"
            self.common_validation.fault(**kwargs)
            return -1

        return radio_profile_info

    def verify_uni_group_channels(self, channels, group_channel, mode='excluded', radio_modes='5GHz',
                                            channel_width='20MHZ', **kwargs):
        """
        - This keyword verifies a excluded channels group of Uni for the 80 Mhz, 40 Mhz and 20 MHz
        - Keyword Usage:
        - ``verify_uni_group_exclusded_channels  [5,12,5,6]  group_channel=uni-1   mode=excluded  ''

        :param  channels: list of channels in Uni group
        :param  group_channel: either uni-1, uni-2, uni-3, uni-4, uni-5, uni-6, uni-7, uni-8
        :param  mode: excluded or included, disabled, enabled
        :param  radio_modes: either 5GHz or 6GHz
        :param  channel_width: either 20, 40, 80 MHz
        """

        self.utils.print_info("Group Channel Not able to click " + str(group_channel))
        try:
            if radio_modes.lower() in ['5ghz', '6ghz'] and channel_width.lower() in ['20mhz']:
                self.get_radio_profile_Mega_20_Hert().click()

            elif radio_modes.lower() in ['5ghz', '6ghz'] and channel_width.lower() in ['40mhz']:
                self.get_radio_profile_Mega_40_Hert().click()

            elif radio_modes.lower() in ['5ghz', '6ghz'] and channel_width.lower() in ['80mhz']:
                self.get_radio_profile_Mega_80_Hert().click()

            if group_channel.lower() == 'uni-1':
                self.get_channel_width_exclusions_uni_1().click()
            elif group_channel.lower() == 'uni-3':
                self.get_channel_width_exclusions_uni_3().click()
            elif group_channel.lower() == 'uni-5':
                self.get_channel_width_exclusions_unii_5().click()
            elif group_channel.lower() == 'uni-6':
                self.get_channel_width_exclusions_unii_6().click()
            elif group_channel.lower() == 'uni-7':
                self.get_channel_width_exclusions_unii_7().click()
            elif group_channel.lower() == 'uni-8':
                self.get_channel_width_exclusions_unii_8().click()

        except:
            kwargs['fail_msg'] = f"verify_uni_group_channels() failed. Not able to click {str(group_channel)}"
            self.common_validation.fault(**kwargs)
            return -1

        return self.verify_radio_profile_channel_width_and_channels(channels, mode=mode)

    def delete_radio_profile(self, profile_name='default', **kwargs):
        """
        - This keyword deletes a radio profile in radio profile table
        - Keyword Usage:
        - ``delete_radio_profile   profile_name=abc_20MHz``

        :param  profile_name: radio profile name
        :return: 1
        """

        radio_profile_table_header = self.get_radio_profile_table_header()
        page_size_100_link = self.get_radio_profile_page_size_100_link()

        if page_size_100_link:
            self.utils.print_info(" Click on page size 100 ")
            self.auto_actions.click(page_size_100_link)
            sleep(5)

        cells = self.get_radio_profile_table_cells()
        if not cells:
            kwargs['fail_msg'] = "delete_radio_profile() failed. Radio Profile table is empty"
            self.common_validation.fault(**kwargs)
            return -1

        row = self._search_radio_profile_in_table(len(radio_profile_table_header), cells, profile_name)
        if not row:
            kwargs['fail_msg'] = f"delete_radio_profile() failed. " \
                                 f"Not able to find the radio profile in table {profile_name}"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(" Select a radio profile ")
        self.auto_actions.click(row)

        self.auto_actions.scroll_up()
        self.utils.print_info(" Click on delete button ")
        self.auto_actions.click_reference(self.get_radio_profile_delete_button)

        sleep(3)
        diag_yes_button = self.get_radio_profile_dialog_yes_button()
        if diag_yes_button:
            self.utils.print_info(" Click on Yes button ")
            self.auto_actions.click_reference(self.get_radio_profile_dialog_yes_button)

        sleep(3)
        cells = self.get_radio_profile_table_cells()
        row = self._search_radio_profile_in_table(len(radio_profile_table_header), cells, profile_name)
        if row:
            kwargs['fail_msg'] = f"delete_radio_profile() failed. Not able to delete the radio profile {profile_name}"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Deleted a radio profile in radio profile table"
        self.common_validation.passed(**kwargs)
        return 1

    def _search_radio_profile_in_table(self, no_columns_per_row, cells, radio_profile):

        """
        - This private function searches a radio profile in the radio profile table
        :param  no_columns_per_row: number column headers of the radio profile tables
        :param  cells: all columns
        :param  radio_profile: profile name
        :return: row or -1
        """
        row_text = []
        cnt = 0
        found = False
        check_box = None

        self.utils.print_info("Search for the value " + str(radio_profile))
        for cell in cells:
            row_text.append(cell.text)
            cnt = cnt + 1

            if cnt == 1:
                check_box = cell

            if cnt == no_columns_per_row:
                if radio_profile in str(row_text):
                    found = True
                    self.utils.print_info("Able to locate the radio in the radio profile table " + str(row_text))
                    return check_box
                else:
                    found = False
                    self.utils.print_info(str(row_text))

                row_text = []
                cnt = 0
                check_box = None

        if not found:
            self.utils.print_info("Not able to find the profile in table ")
            return -1
        return 1

    def enable_DFS_selection(self):
        """
        - This keyword will enable DFS channel selection.
        - Keyword Usage:
        - ``enable_DFS_selection''
        """
        self.utils.print_info("Enable Dynamic Frequency Selection on radio profile")
        self.auto_actions.click_reference(self.get_enable_DFS_selection)
        self.utils.print_info("able to enable DFS selection")