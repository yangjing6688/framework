from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants \
    import EndsystemElementConstants
from ExtremeAutomation.Apis.ApiGeneration.Beans.PlatformVariableBeans.\
    EndSysPlatformVariableDataBean import EndSysPlatformVariableDataBean


class ParseEndSysPlatVarCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature):
        data_bean = EndSysPlatformVariableDataBean()
        data_bean.feature = feature
        data_bean.variable_name = csv_row[0]
        data_bean.operating_system = csv_row[1]
        data_bean.platform = csv_row[2]
        data_bean.version = csv_row[3]
        data_bean.unit = csv_row[4]
        data_bean.variable_value = csv_row[5]  # todo (jhall) - Literal eval values here?

        if data_bean.platform == EndsystemElementConstants.PLATFORM_BASE and \
           data_bean.version == EndsystemElementConstants.VERSION_BASE and \
           data_bean.unit == EndsystemElementConstants.UNIT_BASE:
            data_bean.is_base = True

        return data_bean
