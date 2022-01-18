from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Apis.ApiGeneration.Beans.PlatformVariableBeans.\
    NetElemPlatformVariableDataBean import NetElemPlatformVariableDataBean


class ParseNetElemPlatVarCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature):
        data_bean = NetElemPlatformVariableDataBean()
        data_bean.feature = feature
        data_bean.variable_name = csv_row[0]
        data_bean.operating_system = csv_row[1]
        data_bean.platform = csv_row[2]
        data_bean.version = csv_row[3]
        data_bean.unit = csv_row[4]
        data_bean.variable_value = csv_row[5]

        if data_bean.platform == NetworkElementConstants.PLATFORM_BASE and \
           data_bean.version == NetworkElementConstants.VERSION_BASE and \
           data_bean.unit == NetworkElementConstants.UNIT_BASE:
            data_bean.is_base = True

        return data_bean
