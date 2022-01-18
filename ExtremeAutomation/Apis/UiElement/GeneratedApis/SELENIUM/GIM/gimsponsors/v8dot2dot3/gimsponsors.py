from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimsponsorsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimsponsors(GimsponsorsBase):
    def gim_sponsor_details_add(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Sponsor']")
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @name='sponsorApproval']")
        if arg_dict['sponsor_type'] == "pre_defined":
            self.builder.click(ui_cmd_obj, "//input[@name='sponsorTypeRadio']"
                                           "/following::label[text()='Predefined Sponsor']")
            self.builder.click(ui_cmd_obj, "//div[text()='Predefined Sponsor Email:']/following::input[1]")
            self.builder.enter_text(ui_cmd_obj, arg_dict['pre_def_email'],
                                    "//div[text()='Predefined Sponsor Email:']"
                                    "/following::input[1]")
            self.builder.click(ui_cmd_obj, "//div[text()='Predefined Sponsor Email:']/following::a[1]")
            self.builder.click(ui_cmd_obj, "#addEditOnboardingTemplateDialog [role='presentation'] td "
                                           "div.x-grid-cell-inner", self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//div[text()='Predefined Sponsor Email:']/following::a[2]")
            self.builder.click(ui_cmd_obj, "//div[text()='Predefined Sponsor Email:']/following::input[1]")
            self.builder.enter_text(ui_cmd_obj, arg_dict['pre_def_email'],
                                    "//div[text()='Predefined Sponsor Email:']"
                                    "/following::input[1]")
            self.builder.click(ui_cmd_obj, "//div[text()='Predefined Sponsor Email:']/following::a[1]")
            self.builder.click(ui_cmd_obj, "//span[text()='Sponsor Email Field:']")
            self.builder.delay(ui_cmd_obj, 5)
            if arg_dict['option'] == "1":
                self.builder.click(ui_cmd_obj, "//div/ul/li[1]")
            if arg_dict['option'] == "2":
                self.builder.click(ui_cmd_obj, "//div/ul/li[2]")

        if arg_dict['sponsor_type'] == "fixed":
            self.builder.click(ui_cmd_obj, "//input[@name='sponsorTypeRadio']"
                                           "/following::label[text()='Fixed Sponsor']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['fixed_fn'], "//input[@name='fixedSponsorFN']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['fixed_ln'], "//input[@name='fixedSponsorLN']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['fixed_email'], "//input[@name='fixedSponsorEmail']")

        if arg_dict['sponsor_type'] == "ldap":
            self.builder.click(ui_cmd_obj, "//input[@name='sponsorTypeRadio']/following::label[starts-with(text(), "
                                           "'Configured Sponsor LDAP')]")
            self.builder.enter_text(ui_cmd_obj, arg_dict['ldap_grp'], "//input[@name='sponsorAD']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['sync_dur'], "//input[@name='sponsorCacheSyncDuration']")

        if arg_dict['ot_action'] == "save":
            self.builder.click(ui_cmd_obj,
                               "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/div/div/div/a[1]")
            self.builder.delay(ui_cmd_obj, 2000)
            self.is_ldap_pop_up_exists(ui_cmd_obj)
        if arg_dict['ot_action'] == "cancel":
            self.builder.click(ui_cmd_obj,
                               "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/div/div/div/a[2]")

        return ui_cmd_obj

    def is_ldap_pop_up_exists(self, ui_cmd_obj):
        web_obj = self.base_builder.find_element_by_css_selector(ui_cmd_obj, "[role='alertdialog'] div "
                                                                             "[hidefocus='on']:nth-of-type(1)")
        if self.base_builder.is_element_displayed(ui_cmd_obj, web_obj):
            self.logger.log_info("element exists")
            self.base_builder.click(ui_cmd_obj, web_obj)
            self.spinner_loading(ui_cmd_obj)
        else:
            self.logger.log_info("element not exists")

        return ui_cmd_obj
