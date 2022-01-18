from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.UiDataBean import UiDataBean


class ParseUiElementCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature):
        data_beans = []

        for version in csv_row[2].split("||"):
            ui_element_data_bean = UiDataBean()
            ui_element_data_bean.feature = feature
            ui_element_data_bean.interface_method = csv_row[0]
            ui_element_data_bean.application = csv_row[1].upper()
            ui_element_data_bean.app_version = version.lower()

            data_beans.append(ui_element_data_bean)
        return data_beans
