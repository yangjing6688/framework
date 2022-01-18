"""
Keyword class for all datadriven northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.DatadrivenConstants import \
    DatadrivenConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.DatadrivenConstants import \
    DatadrivenConstants as CommandConstants
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class EndsystemDatadrivenKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemDatadrivenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "datadriven"

    def verify_northbound_query(self, device_name, query_string, expected_json_string, **kwargs):
        """Verifies northbound query."""
        dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_DATADRIVEN,
                                                     self.constants.API_DATADRIVEN, **kwargs)
        arg_dict = {"query_string": query_string,
                    "expected_json_string": expected_json_string}

        command_obj = cmd_api.verify_northbound_query(arg_dict)
        output = command_obj.return_text
        result = parse_api.verify_northbound_query(output, arg_dict)
        total_time = command_obj.end_time - command_obj.start_time
        self.logger.log_info("Northbound query time: " + str(total_time) + " seconds.")
        kw_results = self._determine_result(dev, command_obj, result, True, 'Returned JSON matched expected JSON.',
                                            'Returned JSON did not match expected JSON.')
        return self._keyword_cleanup([kw_results])

    def get_northbound_query(self, device_name, query_string, **kwargs):
        """Returns dictionary representation of JSON returned by NBI query"""
        _, cmd_api, _ = self._init_keyword(device_name, self.constants.API_DATADRIVEN,
                                           self.constants.API_DATADRIVEN, **kwargs)
        arg_dict = {"query_string": query_string}

        command_obj = cmd_api.verify_northbound_query(arg_dict)
        output = StringUtils.format_json_output(command_obj.return_text)
        return output

    def verify_northbound_query_with_regex(self, device_name, query_string, expected_json_string, **kwargs):
        """Verifies northbound query using regex. Values in provided JSON obj should be regex strings"""
        dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_DATADRIVEN,
                                                     self.constants.API_DATADRIVEN, **kwargs)
        arg_dict = {"query_string": query_string,
                    "expected_json_string": expected_json_string}

        command_obj = cmd_api.verify_northbound_query_with_regex(arg_dict)
        output = command_obj.return_text
        result = parse_api.verify_northbound_query_with_regex(output, arg_dict)
        total_time = command_obj.end_time - command_obj.start_time
        self.logger.log_info("Northbound query time: " + str(total_time) + " seconds.")
        kw_results = self._determine_result(dev, command_obj, result, True, 'Returned JSON matched expected JSON.',
                                            'Returned JSON did not match expected JSON.')
        return self._keyword_cleanup([kw_results])
