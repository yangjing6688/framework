from extauto.xiq.defs.EspAlertDefs import EspAlertDefs
from extauto.common.WebElementHandler import WebElementHandler


class EspAlertWebElements(EspAlertDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_go_to_policy(self):
        return self.weh.get_element(self.go_to_policy)

    def get_configred_tab_txt(self):
        return self.weh.get_element(self.configred_tab_txt)

    def get_not_configred_tab_txt(self):
        return self.weh.get_element(self.not_configred_tab_txt)

    def get_add_policy(self):
        return self.weh.get_element(self.add_policy)

    def get_policy_type_metric(self):
        return self.weh.get_element(self.policy_type_metric)

    def get_policy_type_event(self):
        return self.weh.get_element(self.policy_type_event)

    def get_trigger_type_immediate(self):
        return self.weh.get_element(self.trigger_type_immediate)

    def get_trigger_type_deferred(self):
        return self.weh.get_element(self.trigger_type_deferred)

    def get_trigger_type_repeated(self):
        return self.weh.get_element(self.trigger_type_repeated)

    def get_source_parent(self):
        return self.weh.get_element(self.source_parent)

    def get_source_parent_dynamic(self,source_parent):
        ele_def_source_parent = \
          {
            'CSS_SELECTOR': '.nui-auto-esp-alert-profile-sp-select-' + source_parent,
            'wait_for': 5
          }
        return self.weh.get_element(ele_def_source_parent)

    def get_source_parent_device(self):
        return self.weh.get_element(self.source_parent_device)

    def get_source_parent_power_consumption(self):
        return self.weh.get_element(self.source_parent_power_consumption)

    def get_source(self):
        return self.weh.get_element(self.source)

    def get_source_dynamic(self,source):
        ele_def_source = \
          {
            'CSS_SELECTOR': '.nui-auto-esp-alert-profile-source-select-' + source,
            'wait_for': 5
          }
        return self.weh.get_element(ele_def_source)

    def get_source_device_down(self):
        return self.weh.get_element(self.source_device_down)

    def get_source_device_up(self):
        return self.weh.get_element(self.source_device_up)

    def get_source_power_consumption_power_consumed(self):
        return self.weh.get_element(self.source_power_consumption_power_consumed)

    def get_threshold_operator_select(self):
        return self.weh.get_element(self.threshold_operator_select)

    def get_threshold_operator_dynamic(self,threshold_operator):
        ele_def_threshold_operator = \
          {
            'CSS_SELECTOR': '.nui-auto-esp-alert-profile-threshold-operator-select-' + threshold_operator,
            'wait_for': 5
          }
        return self.weh.get_element(ele_def_threshold_operator)

    def get_threshold_operator_select_ne(self):
        return self.weh.get_element(self.threshold_operator_select_ne)

    def get_threshold_input(self):
        return self.weh.get_element(self.threshold_input)

    def get_save(self):
        return self.weh.get_element(self.save)

    def get_configured_grid_rows(self):
        return self.weh.get_elements(self.configured_grid_rows, self.weh.get_element(self.configured_grid))

    def get_when_in_rows(self,row):
        return self.weh.get_element(self.configred_grid_when_text, row)

    def get_severity_in_rows(self,row):
        return self.weh.get_element(self.configred_grid_severity_text, row)

    def get_del_icon_in_row(self,row):
        return self.weh.get_element(self.del_icon_in_row, row)

    def get_del_confirm_ok(self):
        return self.weh.get_element(self.del_confirm_ok)

    def get_unconfigured_event(self):
        return self.weh.get_element(self.unconfigured_event)

    def get_unconfigured_metric(self):
        return self.weh.get_element(self.unconfigured_metric)

    def get_unconfigured_search_icon(self):
        return self.weh.get_element(self.unconfigured_search_icon)

    def get_unconfigured_search_input(self):
        return self.weh.get_element(self.unconfigured_search_input)

    def get_unconfigured_grid_rows(self):
        return self.weh.get_elements(self.unconfigured_grid_rows, self.weh.get_element(self.unconfigured_grid))

    def get_desc_in_unconfigured_grid_rows(self,row):
        return self.weh.get_element(self.unconfigured_grid_rows_desc,row)

    def get_add_icon_in_row(self,row):
        return self.weh.get_element(self.add_icon_in_row,row)

    def get_severity_select(self):
        return self.weh.get_element(self.severity_select)

    def get_severity_select_info(self):
        return self.weh.get_element(self.severity_select_info)

    def get_severity_select_warning(self):
        return self.weh.get_element(self.severity_select_warning)

    def get_severity_select_critical(self):
        return self.weh.get_element(self.severity_select_critical)

    def get_profile_description(self):
        return self.weh.get_element(self.profile_description)

    def get_status_slide_toggle(self,row):
        return self.weh.get_element(self.status_slide_toggle,row)

    def get_subscribe_email(self,row):
        return self.weh.get_element(self.subscribe_email,row)

    def get_subscribe_sms(self,row):
        return self.weh.get_element(self.subscribe_sms,row)

    def get_subscribed_text(self,row):
        return self.weh.get_elements(self.subscribed_text,row)

    def get_detail_grid_rows(self):
        return self.weh.get_elements(self.detail_grid_row, self.weh.get_element(self.detail_grid))

    def get_summary_in_row(self,row):
        return self.weh.get_elements(self.summary_in_row, row)