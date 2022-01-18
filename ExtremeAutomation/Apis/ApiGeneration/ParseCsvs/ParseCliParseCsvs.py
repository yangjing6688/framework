from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.CLI.Parse.CliParseDataBean \
    import CliParseDataBean


class ParseCliParseCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        parse_api_data_bean = CliParseDataBean()
        parse_api_data_bean.uuid = uuid
        parse_api_data_bean.feature = feature
        parse_api_data_bean.interface_method = csv_row[0]
        parse_api_data_bean.operating_system = csv_row[1]
        parse_api_data_bean.platform = csv_row[2]
        parse_api_data_bean.version = csv_row[3]
        parse_api_data_bean.unit = csv_row[4]

        return parse_api_data_bean
