from extauto.common.WebElementHandler import WebElementHandler
from xiq.defs.DashboardDefinitions import DashboardDefinitions


class DashboardElements:
    def __init__(self):
        self.weh = WebElementHandler()
        self.ded = DashboardDefinitions()

    def get_extreme_brand_icon(self):
        return self.weh.get_element(self.ded.extreme_brand_icon)

    def get_total_app_usage(self):
        return self.weh.get_element(self.ded.total_app_usage)

    def get_total_aps_online_count(self):
        return self.weh.get_element(self.ded.total_aps_online_count)

    def get_total_aps_offline_count(self):
        return self.weh.get_element(self.ded.total_aps_offline_count)

    def get_total_apps_count(self):
        return self.weh.get_element(self.ded.total_apps_count)

    def get_total_users_count(self):
        return self.weh.get_element(self.ded.total_users_count)

    def get_total_clients_count(self):
        return self.weh.get_element(self.ded.total_clients_count)

    def get_total_critical_alarms_count(self):
        return self.weh.get_element(self.ded.total_critical_alarms_count)

    def get_total_major_alarms_count(self):
        return self.weh.get_element(self.ded.total_major_alarms_count)

    def get_total_minor_alarms_count(self):
        return self.weh.get_element(self.ded.total_minor_alarms_count)

    def get_total_rogue_aps_count(self):
        return self.weh.get_element(self.ded.total_rogue_aps_count)

    def get_total_rogue_clients_count(self):
        return self.weh.get_element(self.ded.total_rogue_clients_count)

