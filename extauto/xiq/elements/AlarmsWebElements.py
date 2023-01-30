from extauto.xiq.defs.AlarmsWebElementsDefs import AlarmsWebElementsDefs
from extauto.common.WebElementHandler import WebElementHandler


class AlarmsWebElements(AlarmsWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_alarms_grid_rows(self):
        return self.weh.get_elements(self.alarms_grid_rows)

    def get_alarms_grid_row_cells(self, row):
        return self.weh.get_elements(self.alarms_grid_row_cells, row)

    def get_alarm_grid_row_check_box(self, row):
        return self.weh.get_element(self.alarm_grid_row_check_box, row)

    def get_alarm_clear_button(self):
        return self.weh.get_element(self.alarm_clear_button)

    def get_alarm_clear_confirm_yes_button(self):
        return self.weh.get_element(self.alarm_clear_confirm_yes_button)

    def get_alarm_clear_tool_tip(self):
        return self.weh.get_element(self.alarm_clear_tool_tip)

    def get_critical_alarm_count_status_bar(self):
        return self.weh.get_element(self.critical_alarm_count_status_bar)

    def get_major_alarm_count_status_bar(self):
        return self.weh.get_element(self.major_alarm_count_status_bar)

    def get_minor_alarm_count_status_bar(self):
        return self.weh.get_element(self.minor_alarm_count_status_bar)

    def get_alarms_grid_refresh_button(self):
        return self.weh.get_element(self.alarms_grid_refresh_button)

    def get_alarms_grid_legacy_alarm_button(self):
        return self.weh.get_element(self.alarms_grid_legacy_alarm_button)
