from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcapsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcaps(EwcapsBase):
    def aps_rename_ap_name(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='APs']")
        self.builder.click(ui_cmd_obj, "//table[@id='apMainListDT']//td[.='" + arg_dict["current_ap_name"] + "'][1]")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Configure']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["new_ap_name"], "//input[@type='text' and @name='pName']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @name='btnSave']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @onclick='fnCloseSingleApEdit()']")

        return ui_cmd_obj

    def aps_ap_name_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='APs']")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//table[@id='apMainListDT']//td[contains(@class, 'sorting') "
                                                       "and .='" + arg_dict["ap_name"] + "'][1]",
                                                       arg_dict["ap_name"])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("AP name " + str(arg_dict["ap_name"]) + " doesn't  exist.")
        else:
            self.logger.log_debug("AP name  " + str(arg_dict["ap_name"]) + " EXISTS!")

        return ui_cmd_obj

    def aps_ap_name_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='APs']")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//table[@id='apMainListDT']//td[contains(@class, 'sorting') "
                                                       "and .='" + arg_dict["ap_name"] + "'][1]",
                                                       arg_dict["ap_name"])
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("AP name " + str(arg_dict["ap_name"]) + " doesn't  exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("AP name  " + str(arg_dict["ap_name"]) + " still  exist.")

        return ui_cmd_obj

    def aps_edit_ap_environment(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='APs']")
        self.builder.click(ui_cmd_obj, "//table[@id='apMainListDT']//td[.='" + arg_dict["ap_name"] + "'][1]")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Configure']")
        self.builder.click(ui_cmd_obj, "//td//select[@id='pLoc']//option[.='" + arg_dict["ap_environment"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @name='btnSave']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @onclick='fnCloseSingleApEdit()']")

        return ui_cmd_obj

    def aps_ap_environment_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='APs']")
        self.builder.click(ui_cmd_obj, "//table[@id='apMainListDT']//td[.='" + arg_dict["ap_name"] + "'][1]")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Configure']")
        ap_environment = self.builder.find_element(ui_cmd_obj,
                                                   "//td//select[@id='pLoc']//option[.='" +
                                                   arg_dict["ap_environment"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @onclick='fnCloseSingleApEdit()']")
        if ap_environment:
            self.logger.log_debug("Ap Environment " + str(arg_dict["ap_environment"]) + " already exist.")
        else:
            self.logger.log_debug("Ap Environment  " + str(arg_dict["ap_environment"]) + " doesn't exist.")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
