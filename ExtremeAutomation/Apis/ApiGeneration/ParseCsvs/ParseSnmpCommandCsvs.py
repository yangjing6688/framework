from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.SnmpDataBean import SnmpDataBean


class ParseSnmpCommandCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        command_data_bean = SnmpDataBean()
        command_data_bean.uuid = uuid
        command_data_bean.feature = feature
        command_data_bean.interface_method = csv_row[0]
        command_data_bean.operating_system = csv_row[1]
        command_data_bean.platform = csv_row[2]
        command_data_bean.version = csv_row[3]
        command_data_bean.unit = csv_row[4]
        command_data_bean.command_type = csv_row[5]
        command_data_bean.oid = csv_row[6]
        command_data_bean.data_type = csv_row[7]
        command_data_bean.value = csv_row[8]

        return command_data_bean
