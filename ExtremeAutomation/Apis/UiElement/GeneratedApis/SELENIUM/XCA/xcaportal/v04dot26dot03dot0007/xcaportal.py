from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcaportalBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Xcaportal(XcaportalBase):
    def click_add_to_create_new_portal(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.onCreate()']")

        return ui_cmd_obj

    def click_portal_name_to_open_portal_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['portal_name']) + "']")

        return ui_cmd_obj

    def set_portal_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['portal_name'], "//input[@id='portal_name']")
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-hidden='false']")

        return ui_cmd_obj

    def select_guest_portal(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@name='guestPortal']/option[.='" +
                           str(arg_dict['guest_portal']) + "']")

        return ui_cmd_obj

    def select_authenticated_portal(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@name='authenticatedPortal']/option[.='" +
                           str(arg_dict['authenticated_portal']) + "']")

        return ui_cmd_obj

    def click_portal_configurations_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/strong[.='PORTAL CONFIGURATIONS']")

        return ui_cmd_obj

    def click_network_settings_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/strong[.='NETWORK SETTINGS']")

        return ui_cmd_obj

    def click_administration_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//md-tab-item[@role='tab']/strong[.='ADMINISTRATION']")

        return ui_cmd_obj

    def config_portal_network_settings(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@id='useMobileCP']", "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict["toggle_use_mobile_captive_portal"]) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//*[@id='useMobileCP']")
        ui_cmd_obj.error_state = False
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@id='displayWelcomePage']", "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict["toggle_display_welcome_page"]) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//*[@id='displayWelcomePage']")
        ui_cmd_obj.error_state = False
        if arg_dict['test_image_url']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['test_image_url'], "//*[@id='networkConfigTestImageUrl']")
        if arg_dict['redirection']:
            self.builder.click(ui_cmd_obj,
                               "//select[@ng-model='defaultPortalConfig.network_config.redirection']/option[.='" +
                               str(arg_dict['redirection']) + "']")
        if arg_dict['destination']:
            self.builder.enter_text(ui_cmd_obj, arg_dict['destination'], "//*[@id='networkConfigTestURL']")
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-hidden='false']")

        return ui_cmd_obj

    def delete_existing_portal(self, ui_cmd_obj, arg_dict):
        self.click_portal_name_to_open_portal_settings(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canDelete' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='deletePortalConfig(this, curPortalConfig.name)']")

        return ui_cmd_obj

    def save_portal_config_and_back_to_portal_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='setBack()']")

        return ui_cmd_obj

    def verify_portal_exists(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, '//*[contains(@class, "ui-grid-cell") and normalize-space(.)="' +
                                  arg_dict['portal_name'] + '"]/div')
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Portal " + str(arg_dict["portal_name"]) + " doesn't exist.")
        else:
            self.logger.log_debug("Portal " + str(arg_dict["portal_name"]) + " exist.")

        return ui_cmd_obj

    def verify_portal_does_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, '//*[contains(@class, "ui-grid-cell") and normalize-space(.)="' +
                                  arg_dict['portal_name'] + '"]/div')
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Portal " + str(arg_dict["portal_name"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Portal " + str(arg_dict["portal_name"]) + "still exist.")

        return ui_cmd_obj
