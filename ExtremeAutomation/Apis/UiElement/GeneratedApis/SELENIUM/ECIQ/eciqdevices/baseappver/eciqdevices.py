from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqdevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqdevices(EciqdevicesBase):
    def devices_check_device_checkbox(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[.='" + arg_dict['serial_number'] + "']/../td/div/a[.='" +
                                  arg_dict['host_name'] + "']/../../../td/input[@type='checkbox' and "
                                                          "@aria-checked='true']")
        if "false" in str(arg_dict['status']).lower() and ui_cmd_obj.error_state is False:
            self.builder.click(ui_cmd_obj, "//*[.='" + arg_dict['serial_number'] + "']/../td/div/a[.='" +
                               arg_dict['host_name'] + "']/../../../td/input[@type='checkbox']")
        if "true" in str(arg_dict['status']).lower() and ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[.='" + arg_dict['serial_number'] + "']/../td/div/a[.='" +
                               arg_dict['host_name'] + "']/../../../td/input[@type='checkbox']")
        if "false" in str(arg_dict['status']).lower() and ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def devices_clear_device_search(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-automation-tag='automation-manage-device-list']"
                                       "//*[@data-dojo-attach-point='clearSearchField']")

        return ui_cmd_obj

    def devices_click_add_and_select_advanced_onboarding(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[.='Add']")
        self.builder.click(ui_cmd_obj, "//span[.='Add']//../ul/li/a[.='Advanced Onboarding']")

        return ui_cmd_obj

    def devices_click_refresh(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='ui-icon ui-fresh-icon' and @data-dojo-attach-point='refresh']")
        self.builder.delay(ui_cmd_obj, 5000)

        return ui_cmd_obj

    def devices_delete_device(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[.='" + arg_dict['serial_number'] + "']/../td/div/a[.='" +
                           arg_dict['host_name'] + "']/../../../td/div/span/span[contains(@class,'dashboard-icon')]")
        self.builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//*[@data-automation-tag='automation-manage-device-list']"
                                       "//*[@data-tip='Delete']")
        self.builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='yesBtn']")
        self.builder.delay(ui_cmd_obj, 5000)

        return ui_cmd_obj

    def devices_monitor_dialog_click_close(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='ah-close-icon' and @data-dojo-attach-point='closeDialog']")

        return ui_cmd_obj

    def devices_monitor_dialog_click_refresh(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='entity-page-actions']/*[@data-dojo-attach-point='pageRefresh']")

        return ui_cmd_obj

    def devices_monitor_dialog_select_port(self, ui_cmd_obj, arg_dict):
        switch_dict = {}
        if arg_dict['device_type'].lower() == 'aerohive':
            switch_dict['device_type'] = "AerohiveSwitch"
        if arg_dict['device_type'].lower() == 'exos':
            switch_dict['device_type'] = "ExosSwitch"
        if arg_dict['device_type'].lower() == 'voss':
            switch_dict['device_type'] = 'VossSwitch'

        self.builder.click(ui_cmd_obj,
                           "//*[@componentpath='Application/DevicesController/DeviceList/DeviceEntitySwitch/" +
                           switch_dict['device_type'] + "']//span[contains(@class,'port-desc') and .=' " +
                           arg_dict['port_name'] + "']/../div")

        return ui_cmd_obj

    def devices_select_device_by_hostname_and_ip(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until_element_exists(ui_cmd_obj, "//*[.='" + arg_dict['mgmt_ip'] +
                                                         "']/../td/div/a[.='" + arg_dict['host_name'] + "']",
                                                         int(arg_dict['timeout']), int(arg_dict['retry']))
        self.builder.click(ui_cmd_obj, "//*[.='" + arg_dict['mgmt_ip'] + "']/../td/div/a[.='" + arg_dict['host_name'] +
                           "']")

        return ui_cmd_obj

    def devices_select_device_by_hostname_and_serial_number(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until_element_exists(ui_cmd_obj, "//*[.='" + arg_dict['serial_number'] +
                                                         "']/../td/div/a[.='" + arg_dict['host_name'] + "']",
                                                         int(arg_dict['timeout']), int(arg_dict['retry']))
        self.builder.click(ui_cmd_obj, "//*[.='" + arg_dict['serial_number'] + "']/../td/div/a[.='" +
                           arg_dict['host_name'] + "']")

        return ui_cmd_obj

    def devices_select_device_count_per_page(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element(ui_cmd_obj, "//*[@data-dojo-attach-point='gridCurrentResults']")
        current_grid_total = int(ui_cmd_obj.return_text)
        self.builder.get_text_from_element(ui_cmd_obj, "//*[@data-dojo-attach-point='gridTotalResults']")
        grid_total = int(ui_cmd_obj.return_text)
        if current_grid_total is not grid_total:
            self.builder.click(ui_cmd_obj, "//a[contains(@class,'J-page-size ui-page-size') and @data-size='" +
                               arg_dict['device_count'] + "']")

        return ui_cmd_obj

    def devices_verify_device_firmware(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='softwareVersion' and contains(text(),'" +
                                  arg_dict['firmware_version'] + "')]")

        return ui_cmd_obj

    def devices_verify_device_ip(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='ipAddress' and contains(text(),'" +
                                  arg_dict['mgmt_ip'] + "')]")

        return ui_cmd_obj

    def devices_verify_device_iq_agent_version(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='hiveAgent' and contains(text(),'" +
                                  arg_dict['iq_agent_version'] + "')]")

        return ui_cmd_obj

    def devices_verify_device_mac(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='macAddress' and contains(text(),'" +
                                  arg_dict['mac_addr'].upper() + "')]")

        return ui_cmd_obj

    def devices_verify_device_model(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='productType' and contains(text(),'" +
                                  arg_dict['model'] + "')]")

        return ui_cmd_obj

    def devices_verify_device_serial_number(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='serviceTag' and contains(text(),'" +
                                  arg_dict['serial_number'].upper() + "')]")

        return ui_cmd_obj

    def devices_verify_device_vendor(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@componentpath,'DeviceEntitySwitch/SwitchPortsPanel')]"
                                  "//*[@data-dojo-attach-point='make' and contains(text(),'" +
                                  arg_dict['vendor'] + "')]")

        return ui_cmd_obj

    def devices_verify_port_lacp_status(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['lacp_status'].lower() + "')]/../span[contains(text(),'LACP Status')]")

        return ui_cmd_obj

    def devices_verify_port_mode(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['port_mode'].capitalize() + "')]/../span[contains(text(),'Port Mode')]")

        return ui_cmd_obj

    def devices_verify_port_name(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['port_name'] + "')]/../span[contains(text(),'Port Name')]")

        return ui_cmd_obj

    def devices_verify_port_power_used(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['power_used'] + " mW')]/../span[contains(text(),'Power Used')]")

        return ui_cmd_obj

    def devices_verify_port_speed(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['port_speed'] + "')]/../span[contains(text(),'Port Speed')]")

        return ui_cmd_obj

    def devices_verify_port_status(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['port_status'].upper() + "')]/../span[contains(text(),'Port Status')]")

        return ui_cmd_obj

    def devices_verify_port_traffic_rx(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['traffic_rx'] + " PKTs')]/../span[contains(text(),'Traffic Received (Rx)')]")

        return ui_cmd_obj

    def devices_verify_port_traffic_tx(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['traffic_tx'] +
                                  " PKTs')]/../span[contains(text(),'Traffic Transmitted (Tx)')]")

        return ui_cmd_obj

    def devices_verify_port_type(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['port_type'].upper() + "')]/../span[contains(text(),'Type')]")

        return ui_cmd_obj

    def devices_verify_port_vlan(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[@class='portdetails-table']/li/span[contains(text(),'" +
                                  arg_dict['port_vlan'] + "')]/../span[contains(text(),'VLAN')]")

        return ui_cmd_obj

    def devices_verify_serial_number_does_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['serial_number'],
                                "//*[@data-automation-tag='automation-manage-device-list']"
                                "//*[@data-dojo-attach-point='deviceSearchInput']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.click(ui_cmd_obj, "//*[@data-automation-tag='automation-manage-device-list']"
                                       "//*[@data-dojo-attach-point='searchBtn']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.find_element(ui_cmd_obj, "//*[@data-automation-tag='automation-manage-device-list']"
                                              "//*[contains(text(),'No records found.')]")

        return ui_cmd_obj

    def devices_verify_serial_number_exists(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['serial_number'],
                                "//*[@data-automation-tag='automation-manage-device-list']"
                                "//*[@data-dojo-attach-point='deviceSearchInput']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.click(ui_cmd_obj, "//*[@data-automation-tag='automation-manage-device-list']"
                                       "//*[@data-dojo-attach-point='searchBtn']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.find_element(ui_cmd_obj, "//*[@data-automation-tag='automation-manage-device-list']"
                                              "//span[.='" + arg_dict['serial_number'] + "']")

        return ui_cmd_obj
