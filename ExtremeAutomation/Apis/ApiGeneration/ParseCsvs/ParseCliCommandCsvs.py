from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCsvs import ParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.AgentDataBeans.CLI.Command.CliDataBean \
    import CliDataBean


class ParseCliCommandCsvs(ParseCsvs):
    def _create_data_bean(self, csv_row, feature, uuid=None):
        command_data_bean = CliDataBean()
        command_data_bean.uuid = uuid
        command_data_bean.feature = feature
        command_data_bean.interface_method = csv_row[0]
        command_data_bean.operating_system = csv_row[1]
        command_data_bean.platform = csv_row[2]
        command_data_bean.version = csv_row[3]
        command_data_bean.unit = csv_row[4]
        command_data_bean.command = csv_row[5]
        command_data_bean.prompt = csv_row[6]
        command_data_bean.prompt_arguments = csv_row[7]
        command_data_bean.confirmation_phrase = csv_row[8]
        command_data_bean.confirmation_argument = csv_row[9]
        command_data_bean.ignore_errors = csv_row[10]
        command_data_bean.add_errors = csv_row[11]

        return command_data_bean
