from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcsitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcsites(EwcsitesBase):
    def sites_create_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//input[@onclick='addSite()']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['site_name'], "//input[@type='text' and @id='site_name']")

        # TODO:  Set local radius auth and configure radius server steps were skipped in the old keyword.
        #             Need to be added later.
        self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='apComChkbox']")

        if arg_dict['site_roles']:
            for site_role in str(arg_dict["site_roles"]).split(","):
                self.builder.click(ui_cmd_obj, "//span[.='" + str(site_role).strip() +
                                   "']//input[@type='checkbox' and @name='sitePolChkbox[]']")
        self.sites_click_save_button(ui_cmd_obj, arg_dict)
        self.sites_site_should_exist(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def sites_site_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        site_existence = self.builder.find_element(ui_cmd_obj, "//table[@id='siteListtable']//div[.='" +
                                                   arg_dict['site_name'] + "']")
        if site_existence:
            self.logger.log_debug("Site " + str(arg_dict["site_name"]) + " already exist.")
        else:
            self.logger.log_debug("Site " + str(arg_dict["site_name"]) + " doesn't exist.")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def sites_site_should_not_exist(self, ui_cmd_obj, arg_dict):
        site_existence = self.builder.find_element(ui_cmd_obj, "//table[@id='siteListtable']//div[.='" +
                                                   arg_dict['site_name'] + "']")
        if not site_existence:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Site " + str(arg_dict["site_name"]) + " doesn't  exist.")
        else:
            self.logger.log_debug("Site " + str(arg_dict["site_name"]) + " still exist.")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def sites_add_ap_to_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='AP Assignments']")
        xpath = "//div[@onmouseout='hideGenericTooltip()' and .='" + \
                arg_dict['ap_name'] + "']/../following-sibling::td/input[@type='checkbox']"
        checkbox = self.builder.driver.find_element_by_xpath(xpath)
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, xpath)
        self.sites_click_save_button(ui_cmd_obj, arg_dict)
        self.sites_ap_should_be_enabled_for_site(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def sites_add_default_dns_server_to_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['dns_ip'], "//span[.='Default DNS Server ']//input")
        self.sites_click_save_button(ui_cmd_obj, arg_dict)
        self.sites_validate_default_dns_server_ip_for_site(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def sites_ap_should_be_enabled_for_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='AP Assignments']")
        checkbox = self.builder.driver.find_element_by_xpath("//div[@onmouseout='hideGenericTooltip()' "
                                                             "and .='" + arg_dict['ap_name'] +
                                                             "']/../following-sibling::td/input[@type='checkbox']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.logger.log_debug("AP " + str(arg_dict["ap_name"]) +
                                  " is not enabled on site " + arg_dict['site_name'] + ".")
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_debug("AP " + str(arg_dict["ap_name"]) +
                                  " is enabled on site " + arg_dict['site_name'] + ".")

        return ui_cmd_obj

    def sites_wlan_should_be_enabled_for_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='WLAN Assignments']")
        radio = self.builder.driver.find_element_by_xpath("//td/div[.='" + arg_dict['wlan_name'] +
                                                          "']/../following-sibling::td/input[@name='rfschk1[]']")
        checked = radio.get_attribute("checked")
        if not checked:
            radio = self.builder.driver.find_element_by_xpath("//td/div[.='" + arg_dict['wlan_name'] +
                                                              "']/../following-sibling::td/input[@name='rfschk2[]']")
            checked = radio.get_attribute("checked")
            if not checked:
                self.logger.log_debug("WLAN " + str(arg_dict["wlan_name"]) +
                                      " is not enabled on site " + arg_dict['site_name'] + ".")
                ui_cmd_obj.error_state = True
        if checked:
            self.logger.log_debug("WLAN " + str(arg_dict["wlan_name"]) +
                                  " is enabled on site " + arg_dict['site_name'] + ".")

        return ui_cmd_obj

    def sites_validate_default_dns_server_ip_for_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//span[.='Default DNS Server ']//input",
                                                            "value", arg_dict['dns_ip'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("The displayed default DNS server ip address doesn't match the expected ip " +
                                  arg_dict['dns_ip'] + ".")
        else:
            self.logger.log_debug("The displayed default DNS server ip address matches the expectation.")

        return ui_cmd_obj

    def sites_delete_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @name='deleteSiteButton']")
        alt = self.builder.driver.switch_to_alert()
        alt.accept()
        self.sites_site_should_not_exist(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def sites_click_save_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@id='btnSave']")

        return ui_cmd_obj

    def sites_add_wlan_radios_to_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='WLAN Assignments']")
        if str(arg_dict['radio']).lower() == 'both' or str(arg_dict['radio']).lower() == 'radio1':
            xpath = "//td/div[.='" + arg_dict['wlan_name'] + "']/../following-sibling::td/input[@name='rfschk1[]']"
            checkbox = self.builder.driver.find_element_by_xpath(xpath)
            checked = checkbox.get_attribute("checked")
            if not checked:
                self.builder.click(ui_cmd_obj, xpath)
        if str(arg_dict['radio']).lower() == 'both' or str(arg_dict['radio']).lower() == 'radio2':
            xpath = "//td/div[.='" + arg_dict['wlan_name'] + "']/../following-sibling::td/input[@name='rfschk2[]']"
            checkbox = self.builder.driver.find_element_by_xpath(xpath)
            checked = checkbox.get_attribute("checked")
            if not checked:
                self.builder.click(ui_cmd_obj, xpath)
        self.sites_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def sites_remove_wlan_radios_from_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='WLAN Assignments']")
        if str(arg_dict['radio']).lower() == 'both' or str(arg_dict['radio']).lower() == 'radio1':
            xpath = "//td/div[.='" + arg_dict['wlan_name'] + "']/../following-sibling::td/input[@name='rfschk1[]']"
            checkbox = self.builder.driver.find_element_by_xpath(xpath)
            checked = checkbox.get_attribute("checked")
            if checked:
                self.builder.click(ui_cmd_obj, xpath)
        if str(arg_dict['radio']).lower() == 'both' or str(arg_dict['radio']).lower() == 'radio2':
            xpath = "//td/div[.='" + arg_dict['wlan_name'] + "']/../following-sibling::td/input[@name='rfschk2[]']"
            checkbox = self.builder.driver.find_element_by_xpath(xpath)
            checked = checkbox.get_attribute("checked")
            if checked:
                self.builder.click(ui_cmd_obj, xpath)
        self.sites_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def sites_select_tab_in_site_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='" + arg_dict['tab_name'] + "']")

        return ui_cmd_obj

    def sites_remove_ap_from_site(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Sites']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['site_name'] + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnTabLink') and .='AP Assignments']")
        xpath = "//div[@onmouseout='hideGenericTooltip()' and .='" + \
                arg_dict['ap_name'] + "']/../following-sibling::td/input[@type='checkbox']"
        checkbox = self.builder.driver.find_element_by_xpath(xpath)
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, xpath)
        self.sites_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj
