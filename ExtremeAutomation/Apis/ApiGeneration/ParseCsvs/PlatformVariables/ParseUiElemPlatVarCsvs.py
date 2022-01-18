from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Library.Device.UiElement.Constants.UiElementConstants import UiElementConstants
from ExtremeAutomation.Apis.ApiGeneration.Beans.PlatformVariableBeans.\
    UiElementPlatformVariableDataBean import UiElementPlatformVariableDataBean


class ParseUiElemPlatVarCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature):
        data_bean = UiElementPlatformVariableDataBean()
        data_bean.feature = feature
        data_bean.variable_name = csv_row[0].lower()
        data_bean.application = csv_row[1].upper()
        data_bean.app_version = csv_row[2].lower()
        data_bean.variable_value = csv_row[3].lower()

        if data_bean.app_version.lower() == UiElementConstants.APP_VER_BASE.lower():
            data_bean.is_base = True

        return data_bean
