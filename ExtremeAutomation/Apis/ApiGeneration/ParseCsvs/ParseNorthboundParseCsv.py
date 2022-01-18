from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.NorthboundDataBean \
    import NorthboundDataBean


class ParseNorthboundParseCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        parse_data_bean = NorthboundDataBean()
        parse_data_bean.uuid = uuid
        parse_data_bean.feature = feature
        parse_data_bean.interface_method = csv_row[0]
        parse_data_bean.operating_system = csv_row[1]
        parse_data_bean.platform = csv_row[2]
        parse_data_bean.version = csv_row[3]
        parse_data_bean.unit = csv_row[4]
        parse_data_bean.query = csv_row[5]

        parse_data_bean.file_name = feature.capitalize() + "CustomShowTools.py"
        parse_data_bean.base_file_name = feature.capitalize() + "BaseCustomShowTools.py"

        return parse_data_bean
