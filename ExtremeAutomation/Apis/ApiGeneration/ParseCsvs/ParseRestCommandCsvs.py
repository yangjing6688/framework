from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.RestDataBean import RestDataBean


class ParseRestCommandCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        data_bean = RestDataBean()
        data_bean.feature = feature
        data_bean.uuid = uuid
        data_bean.interface_method = csv_row[0]
        data_bean.operating_system = csv_row[1]
        data_bean.platform = csv_row[2]
        data_bean.version = csv_row[3]
        data_bean.unit = csv_row[4]
        data_bean.request_type = csv_row[5]
        data_bean.uri = csv_row[6]

        if data_bean.uri.startswith("/"):
            if len(data_bean.uri) > 1:
                data_bean.uri = data_bean.uri[1::]

        data_bean.headers = csv_row[7]
        data_bean.ignore_errors = csv_row[8]
        data_bean.add_errors = csv_row[9]

        return data_bean
