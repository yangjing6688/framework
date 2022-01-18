from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqonboardBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqonboard(EciqonboardBase):

    def bypass_onboarding_routine(self, ui_cmd_obj, arg_dict):
        self.onboard_dialog_click_get_started_button(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 2000)
        self.onboard_dialog_click_done_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def onboard_dialog_add_new_policy_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['policy_name'], "//input[@data-dojo-attach-point='policyName']")

        return ui_cmd_obj

    def onboard_dialog_add_serial_number(self, ui_cmd_obj, arg_dict):
        switch_dict = {}
        if arg_dict['device_type'].lower() == 'aerohive' or arg_dict['device_type'].lower() == 'ah':
            switch_dict['device_type'] = "ahImportArea"
        else:
            switch_dict['device_type'] = arg_dict['device_type'].lower() + 'ImportArea'

        self.builder.enter_text(ui_cmd_obj, arg_dict['serial_number'], "//*[@data-dojo-attach-point='" +
                                switch_dict['device_type'] + "' and  @style='']//textarea[@placeholder="
                                                             "'Serial Numbers (separated by a comma)']")

        return ui_cmd_obj

    def onboard_dialog_assign_location_check_device_checkbox(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[contains(@id,'ah/comp/deviceonboarding') "
                                       "and not(contains(@style,'display: none;'))]"
                                       "//*[.='" + arg_dict['serial_number'] + "']/../td/div[@role='CheckBox']")

        return ui_cmd_obj

    def onboard_dialog_assign_location_popup_click_assign_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@componentpath='AHDialog']//button[@data-dojo-attach-point='btnAssign']")

        return ui_cmd_obj

    def onboard_dialog_assign_location_popup_click_cancel_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@componentpath='AHDialog']//button[@data-dojo-attach-point='btnCancel']")

        return ui_cmd_obj

    def onboard_dialog_click_assign_location_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[contains(@id,'ah/comp/deviceonboarding') "
                                       "and not(contains(@style,'display: none;'))]"
                                       "//a[@data-dojo-attach-point='cmdAssignLocation']")

        return ui_cmd_obj

    def onboard_dialog_click_device_type_real_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='realDevice']")

        return ui_cmd_obj

    def onboard_dialog_click_device_type_simulated_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='simDevice']")

        return ui_cmd_obj

    def onboard_dialog_click_done_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='cancelButton' and .='Done']")

        return ui_cmd_obj

    def onboard_dialog_click_finish_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[.='Finish' and not(contains(@style,'display: none;'))]")

        return ui_cmd_obj

    def onboard_dialog_click_get_started_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[.='Get Started!']")

        return ui_cmd_obj

    def onboard_dialog_click_next_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@data-dojo-attach-point='nextButton' and .='Next']")
        self.builder.delay(ui_cmd_obj, 5000)

        return ui_cmd_obj

    def onboard_dialog_click_skip_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@data-dojo-attach-point='skipButton' and .='Skip']")
        self.builder.delay(ui_cmd_obj, 5000)

        return ui_cmd_obj

    def onboard_dialog_select_create_new_network_policy(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-automation-tag='automation-welcome-onboard-new-policy']")

        return ui_cmd_obj

    def onboard_dialog_select_device_type(self, ui_cmd_obj, arg_dict):
        switch_dict = {}
        if arg_dict['device_type'].lower() == 'dell':
            self.builder.click(ui_cmd_obj, "//*[contains(@componentpath,"
                                           "'WelcomeDevices/DellSwitchStep1')]//a[.='Dell']")
            return ui_cmd_obj

        if arg_dict['device_type'].lower() == 'aerohive' or arg_dict['device_type'].lower() == 'ah':
            switch_dict['device_type'] = "ah-import"
        else:
            switch_dict['device_type'] = arg_dict['device_type'].lower() + '-import'

        self.builder.click(ui_cmd_obj, "//*[contains(@componentpath,'WelcomeDevices/DellSwitchStep1')]"
                                       "//*[contains(@class,'" + switch_dict['device_type'] + "')]")

        return ui_cmd_obj

    def onboard_dialog_select_network_policy(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='existingPolicyContainer']"
                                       "//*[@class='ChosenList']/div/a/div/b")
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='existingPolicyContainer']"
                                       "//*[@class='chzn-drop']//*[.='" + arg_dict['network_policy'] + "']")

        return ui_cmd_obj

    def onboard_dialog_select_use_an_existing_network_policy(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@type='radio' and @data-dojo-attach-point='existingPolicy']")

        return ui_cmd_obj

    def onboard_dialog_uncheck_network_policy_type(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='WelcomePolicyCheckboxLabel' and .='" + arg_dict['policy_type'] +
                           "']/../input[@type='checkbox']")

        return ui_cmd_obj
