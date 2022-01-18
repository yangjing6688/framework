from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.RestDataBean import RestDataBean
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.SnmpDataBean import SnmpDataBean
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.CLI.Command.CliDataBean \
    import CliDataBean


class ParseCommandCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        if csv_row[-1] == GenerationConstants.AGENT_TYPE_CLI:
            data_bean = CliDataBean()
            data_bean.uuid = uuid
            data_bean.feature = feature
            data_bean.interface_method = csv_row[0]
            data_bean.operating_system = csv_row[1]
            data_bean.platform = csv_row[2]
            data_bean.version = csv_row[3]
            data_bean.unit = csv_row[4]
            data_bean.command = csv_row[5]
            data_bean.prompt = csv_row[6]
            data_bean.prompt_arguments = csv_row[7]
            data_bean.confirmation_phrase = csv_row[8]
            data_bean.confirmation_argument = csv_row[9]
            data_bean.ignore_errors = csv_row[10]
            data_bean.add_errors = csv_row[11]

        elif csv_row[-1] == GenerationConstants.AGENT_TYPE_REST:
            data_bean = RestDataBean()
            data_bean.feature = feature
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

        elif csv_row[-1] == GenerationConstants.AGENT_TYPE_SNMP:
            data_bean = SnmpDataBean()
            data_bean.feature = feature
            data_bean.interface_method = csv_row[0]
            data_bean.operating_system = csv_row[1]
            data_bean.platform = csv_row[2]
            data_bean.version = csv_row[3]
            data_bean.unit = csv_row[4]
            data_bean.command_type = csv_row[5]
            data_bean.oid = csv_row[6]
            data_bean.data_type = csv_row[7]
            data_bean.value = csv_row[8]

        else:
            raise TypeError("Wrong agent type for ParseCommandCsvs: {0} in {1}.{2}".
                            format(csv_row[-1], feature, csv_row[0]))

        return data_bean
