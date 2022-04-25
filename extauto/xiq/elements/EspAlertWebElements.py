from extauto.xiq.defs.EspAlertDefs import *
from extauto.common.WebElementHandler import *


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

    def get_source_parent_device(self):
        return self.weh.get_element(self.source_parent_device)

    def get_source_parent_power_consumption(self):
        return self.weh.get_element(self.source_parent_power_consumption)

    def get_source(self):
        return self.weh.get_element(self.source)

    def get_source_device_down(self):
        return self.weh.get_element(self.source_device_down)

    def get_source_power_consumption_power_consumed(self):
        return self.weh.get_element(self.source_power_consumption_power_consumed)

    def get_threshold_operator_select(self):
        return self.weh.get_element(self.threshold_operator_select)

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

    def get_del_icon_in_row(self,row):
        return self.weh.get_element(self.del_icon_in_row, row)

    def get_del_confirm_ok(self):
        return self.weh.get_element(self.del_confirm_ok)