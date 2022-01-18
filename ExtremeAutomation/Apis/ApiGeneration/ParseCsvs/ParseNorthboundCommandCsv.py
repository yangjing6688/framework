from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.NorthboundDataBean \
    import NorthboundDataBean


class ParseNorthboundCommandCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        command_data_bean = NorthboundDataBean()
        command_data_bean.uuid = uuid
        command_data_bean.feature = feature
        command_data_bean.interface_method = csv_row[0]
        command_data_bean.operating_system = csv_row[1]
        command_data_bean.platform = csv_row[2]
        command_data_bean.version = csv_row[3]
        command_data_bean.unit = csv_row[4]
        command_data_bean.query = csv_row[5]

        return command_data_bean
