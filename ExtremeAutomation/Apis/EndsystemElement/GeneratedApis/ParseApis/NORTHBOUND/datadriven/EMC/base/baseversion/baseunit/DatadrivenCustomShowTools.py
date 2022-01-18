from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.datadriven.base.\
    DatadrivenBaseCustomShowTools import DatadrivenBaseCustomShowTools
import json


class DatadrivenCustomShowTools(DatadrivenBaseCustomShowTools):
    def verify_northbound_query(self, output, args, **kwargs):
        expected_json = json.loads(args['expected_json_string'])

        # sort the dictionaries and returns strings
        returned_json = json.dumps(output, sort_keys=True, indent=2)
        expected_json = json.dumps(expected_json, sort_keys=True, indent=2)

        # read the sorted strings back into dictionaries
        returned_json = json.loads(returned_json)
        expected_json = json.loads(expected_json)

        result = self._validate_json_output(output, expected_json, False)

        return result

    def verify_northbound_query_with_regex(self, output, args, **kwargs):
        expected_json = json.loads(args['expected_json_string'])

        # sort the dictionaries and returns strings
        returned_json = json.dumps(output, sort_keys=True, indent=2)
        expected_json = json.dumps(expected_json, sort_keys=True, indent=2)

        # read the sorted strings back into dictionaries
        returned_json = json.loads(returned_json)
        expected_json = json.loads(expected_json)

        result = self._regex_validate_json_output(output, expected_json)

        return result
