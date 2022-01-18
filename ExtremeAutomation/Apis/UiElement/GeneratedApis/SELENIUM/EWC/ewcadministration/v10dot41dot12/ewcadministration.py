from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcadministrationBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcadministration(EwcadministrationBase):
    def administration_rename_hostname(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["host_name"], "//input[@type='text' and @name='pcHostName']")
        self.administration_click_save_button(ui_cmd_obj, arg_dict)
        self.administration_hostname_should_exist(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def administration_hostname_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//input[@type='text' and @name='pcHostName']",
                                                            "value", arg_dict["host_name"])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Host name " + str(arg_dict["host_name"]) + " doesn't  exist.")
        else:
            self.logger.log_debug("Host name  " + str(arg_dict["host_name"]) + " EXISTS!")

        return ui_cmd_obj

    def administration_hostname_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//input[@type='text' and @name='pcHostName']",
                                                            "value", arg_dict["host_name"])
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Host name " + str(arg_dict["host_name"]) + " doesn't  exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Host name  " + str(arg_dict["host_name"]) + " still  exist.")

        return ui_cmd_obj

    def administration_rename_domain_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["domain_name"], "//input[@type='text' and @name='pcDomain']")
        self.administration_click_save_button(ui_cmd_obj, arg_dict)
        self.administration_domain_name_should_exist(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def administration_domain_name_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//input[@type='text' and @name='pcDomain']",
                                                            "value", arg_dict["domain_name"])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Domain name " + str(arg_dict["domain_name"]) + " doesn't  exist.")
        else:
            self.logger.log_debug("Domain name  " + str(arg_dict["domain_name"]) + " EXISTS!")

        return ui_cmd_obj

    def administration_domain_name_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//input[@type='text' and @name='pcDomain']",
                                                            "value", arg_dict["domain_name"])
        if not ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Domain name " + str(arg_dict["domain_name"]) + " doesn't  exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Domain name  " + str(arg_dict["domain_name"]) + " still  exist.")

        return ui_cmd_obj

    def administration_add_primary_dns_server_on_host(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["dns_ip"], "//input[@type='text' and @name='dns_ip']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @name='btn_dns_add']")
        self.administration_click_save_button(ui_cmd_obj, arg_dict)
        self.administration_validate_primary_dns_server_ip_on_host(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def administration_delete_primary_dns_server_on_host(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@name='dns_list']/option[@value='" + arg_dict["dns_ip"] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @name='btn_dns_del']")
        self.administration_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def administration_validate_primary_dns_server_ip_on_host(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//select[@name='dns_list']/option[@value='" + arg_dict["dns_ip"] + "']")
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Primary dns server ip: " + str(arg_dict["dns_ip"]) + " doesn't  exist.")
        else:
            self.logger.log_debug("Primary dns server ip:  " + str(arg_dict["dns_ip"]) + " already  exist.")

        return ui_cmd_obj

    def administration_click_save_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='Save']")

        return ui_cmd_obj
