from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwccosBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewccos(EwccosBase):
    def cos_create_cos_profile(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @onclick='addCos()']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["cos_name"], "//input[@type='text' and @name='cos_name']")
        if arg_dict["priority_override"] == "enable":
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='wlanMarkingCheck']")
        if arg_dict['priority'] != "disable":
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosUpCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='cosUpSel']/option[.='" + str(arg_dict['priority']) + "']")
        if arg_dict['irl'] != "disable":
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='ingressCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='ingress']/option[.='" + str(arg_dict['irl']) + "']")
        if arg_dict['orl'] != "disable":
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='egressCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='egress']/option[.='" + str(arg_dict['orl']) + "']")
        if arg_dict['txq'] != "disable":
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosTxqCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='cosTxqSel']/option[.='" + str(arg_dict['txq']) + "']")
        if arg_dict['tos'] != "disable":
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosTosCheck']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['tos'], "//input[@type='text' and @id='tosDscpInput']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['tos_mask'], "//input[@type='text' and @id='tosMaskInput']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_profile_priority_override_from_wlan(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='wlanMarkingCheck']")
        checked = checkbox.get_attribute("checked")
        if (arg_dict["priority_override"] == "enable" and not checked) or \
                (arg_dict["priority_override"] == "disable" and checked):
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='wlanMarkingCheck']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_profile_priority(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='cosUpCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["priority"] == "disable" and checked:
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosUpCheck']")
        elif arg_dict["priority"] != "disable":
            if not checked:
                self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosUpCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='cosUpSel']/option[.='" + str(arg_dict['priority']) + "']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_profile_tos(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='cosTosCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["tos"] == "disable" and checked:
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosTosCheck']")
        elif arg_dict["tos"] != "disable":
            if not checked:
                self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosTosCheck']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['tos'], "//input[@type='text' and @id='tosDscpInput']")
            if arg_dict['tos_mask']:
                self.builder.enter_text(ui_cmd_obj, arg_dict['tos_mask'],
                                        "//input[@type='text' and @id='tosMaskInput']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_profile_irl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='ingressCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["irl_name"] == "disable" and checked:
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='ingressCheck']")
        elif arg_dict["irl_name"] != "disable":
            if not checked:
                self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='ingressCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='ingress']/option[.='" + str(arg_dict['irl_name']) + "']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_profile_orl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='egressCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["orl_name"] == "disable" and checked:
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='egressCheck']")
        elif arg_dict["orl_name"] != "disable":
            if not checked:
                self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='egressCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='egress']/option[.='" + str(arg_dict['orl_name']) + "']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_profile_txq(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='cosTxqCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["txq"] == "disable" and checked:
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosTxqCheck']")
        elif arg_dict["txq"] != "disable":
            if not checked:
                self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='cosTxqCheck']")
            self.builder.click(ui_cmd_obj, "//select[@id='cosTxqSel']/option[.='" + str(arg_dict['txq']) + "']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_delete_cos_profile(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['cos_profile'] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @id='deleteCosButton']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_create_cos_irl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @id='newIngressBtn']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["irl_name"], "//input[@type='text' and @id='profile_nameadd']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["rate"], "//input[@type='text' and @id='rateadd']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Add']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_irl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @id='editIngressBtn']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["irl_name"], "//input[@type='text' and @id='profile_nameadd']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["rate"], "//input[@type='text' and @id='rateadd']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Save']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_create_cos_orl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @id='newEgressBtn']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["orl_name"], "//input[@type='text' and @id='profile_nameadd']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["rate"], "//input[@type='text' and @id='rateadd']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Add']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_edit_cos_orl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @id='editEgressBtn']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["orl_name"], "//input[@type='text' and @id='profile_nameadd']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["rate"], "//input[@type='text' and @id='rateadd']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Save']")
        self.cos_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def cos_profile_priority_override_should_be_enabled(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='wlanMarkingCheck']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.logger.log_debug("Priority override is enabled in profile")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Priority override is disabled in profile")

        return ui_cmd_obj

    def cos_verify_cos_profile_priority(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='cosUpCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["priority"] == "disable" and checked:
            ui_cmd_obj.error_state = True
        elif arg_dict["priority"] != "disable":
            if not checked:
                ui_cmd_obj.error_state = True
        option = self.builder.driver.find_element_by_xpath("//select[@id='cosUpSel']/option[.='" +
                                                           str(arg_dict['priority']) + "']")
        selected = option.get_attribute("selected")
        if selected and not ui_cmd_obj.error_state:
            self.logger.log_debug("Priority status is correct in profile.")
        elif ui_cmd_obj.error_state:
            self.logger.log_debug("Priority status is incorrect in profile.")

        return ui_cmd_obj

    def cos_verify_cos_profile_tos(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='cosTosCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["tos"] == "disable" and checked:
            self.logger.log_debug("Tos status isn't correct in profile")
            ui_cmd_obj.error_state = True

            return ui_cmd_obj
        elif arg_dict["tos"] != "disable":
            if not checked:
                self.logger.log_debug("Tos status isn't correct in profile")
                ui_cmd_obj.error_state = True

                return ui_cmd_obj
            self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                                "//input[@type='text' and @id='tosDscpInput']",
                                                                "value", arg_dict["tos"])
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Tos status isn't correct in profile")

                return ui_cmd_obj
            if not arg_dict['tos_mask']:
                self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                                    "//input[@type='text' and @id='tosDscpInput']",
                                                                    "value", arg_dict["tos_mask"])
                if ui_cmd_obj.error_state:
                    self.logger.log_debug("Tos status isn't correct in profile")

        return ui_cmd_obj

    def cos_verify_cos_profile_irl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='ingressCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["irl_name"] == "disable" and checked:
            ui_cmd_obj.error_state = True
        elif arg_dict["irl_name"] != "disable":
            if not checked:
                ui_cmd_obj.error_state = True

                return ui_cmd_obj
            # Selected option doesn't have @selected attribute. So the following verification will always pass.
            self.builder.find_element(ui_cmd_obj, "//select[@id='ingress']/option[.='" +
                                      str(arg_dict['irl_name']) + "']")
        if not ui_cmd_obj.error_state:
            self.logger.log_debug("Irl status is correct in profile")

        return ui_cmd_obj

    def cos_verify_cos_profile_orl(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='egressCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["orl_name"] == "disable" and checked:
            ui_cmd_obj.error_state = True
        elif arg_dict["orl_name"] != "disable":
            if not checked:
                ui_cmd_obj.error_state = True

                return ui_cmd_obj
            # Selected option doesn't have @selected attribute. So the following verification will always pass.
            self.builder.find_element(ui_cmd_obj, "//select[@id='ingress']/option[.='" +
                                      str(arg_dict['orl_name']) + "']")
        if not ui_cmd_obj.error_state:
            self.logger.log_debug("Orl status is correct in profile")

        return ui_cmd_obj

    def cos_verify_cos_profile_txq(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict["cos_profile"] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @id='cosTxqCheck']")
        checked = checkbox.get_attribute("checked")
        if arg_dict["txq"] == "disable" and checked:
            ui_cmd_obj.error_state = True
        elif arg_dict["txq"] != "disable":
            if not checked:
                ui_cmd_obj.error_state = True
        option = self.builder.driver.find_element_by_xpath("//select[@id='cosTxqSel']/option[.='" +
                                                           str(arg_dict['txq']) + "']")
        selected = option.get_attribute("selected")
        if selected and not ui_cmd_obj.error_state:
            self.logger.log_debug("Txq status is correct in profile.")
        elif ui_cmd_obj.error_state:
            self.logger.log_debug("Txq status is incorrect in profile.")

        return ui_cmd_obj

    def cos_click_save_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@type='submit' and @id='btnSave']")

        return ui_cmd_obj
