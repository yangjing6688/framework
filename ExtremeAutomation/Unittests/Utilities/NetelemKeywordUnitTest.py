from ExtremeAutomation.Unittests.Utilities.KeywordUnitTest import KeywordUnitTest
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject import SnmpCommandObject


class CliKeywordUnitTest(KeywordUnitTest):
    def __init__(self, csv_path, kw_path, agent):
        super(CliKeywordUnitTest, self).__init__(csv_path, kw_path, agent)
        self.con_method = self.CON_METHOD_CLI

    def create_method_dict(self, feature, csv_row):
        method_dict = {"feature": feature.lower(),
                       "function_name": csv_row[0].lower(),
                       "os": csv_row[1].upper(),
                       "platform": csv_row[2],
                       "version": csv_row[3],
                       "unit": csv_row[4],
                       "command": csv_row[5]}

        command_args = " ".join([csv_row[5], csv_row[7], csv_row[9]])
        method_dict["command_args"] = self._get_args_from_command(command_args)

        return_command = self._generate_return_command(method_dict["command"], method_dict["command_args"])
        method_dict["return_command"] = return_command if return_command else "N/A"

        return method_dict


class RestKeywordUnitTest(KeywordUnitTest):
    def __init__(self, csv_path, kw_path, agent):
        super(RestKeywordUnitTest, self).__init__(csv_path, kw_path, agent)
        self.con_method = self.CON_METHOD_REST

    def create_method_dict(self, feature, csv_row):
        method_dict = {"feature": feature.lower(),
                       "function_name": csv_row[0],
                       "os": csv_row[1].upper(),
                       "platform": csv_row[2],
                       "version": csv_row[3],
                       "unit": csv_row[4],
                       "command": csv_row[5] + " " + (csv_row[6] if csv_row[6] == "/" else csv_row[6][1::])
                       }

        method_dict["command_args"] = self._get_args_from_command(method_dict["command"])
        method_dict["return_command"] = self._generate_return_command(method_dict["command"],
                                                                      method_dict["command_args"])
        return method_dict

    def generate_test(self, feature, keyword_name, method_dict):
        def generated_test(_self):
            result = RestCommandObject()
            feature = method_dict["feature"]
            dev_name = self._get_device_name(method_dict)
            args = method_dict["command_args"]
            api_method = method_dict["function_name"]

            args_built = False

            while not args_built:
                try:
                    # result = self.net_elem_kw.execute_keyword(dev_name, args, api_method, command_api_const=feature)[0]
                    args_built = True
                except KeyError as e:
                    args[str(e).strip("'")] = "test_val_" + str(e).strip("'")
                except ValueError as e:
                    if "int" in str(e):
                        for arg in args:
                            if args[arg] == str(e).split()[-1].strip("'"):
                                args[arg] = 10
                                break
            _self.assertEqual(result.command, method_dict["return_command"])
        return generated_test


class SnmpKeywordUnitTest(KeywordUnitTest):
    def __init__(self, csv_path, kw_path, agent):
        super(SnmpKeywordUnitTest, self).__init__(csv_path, kw_path, agent)
        self.con_method = self.CON_METHOD_SNMP

    def create_method_dict(self, feature, csv_row):
        method_dict = {"feature": feature.lower(),
                       "function_name": csv_row[0],
                       "os": csv_row[1].upper(),
                       "platform": csv_row[2],
                       "version": csv_row[3],
                       "unit": csv_row[4],
                       "command": csv_row[5],
                       "return_command": "snmp" + csv_row[5] + " " + csv_row[6],
                       "command_args": self._get_args_from_command(csv_row[6])}

        method_dict["return_command"] = ("snmp" + method_dict["command"] + " " +
                                         self._generate_return_command(csv_row[6], method_dict["command_args"]))

        return method_dict

    def generate_test(self, feature, keyword_name, method_dict):
        def generated_test(_self):
            result = SnmpCommandObject()
            feature = method_dict["feature"]
            dev_name = self._get_device_name(method_dict)
            args = method_dict["command_args"]
            api_method = method_dict["function_name"]

            args_built = False
            current_arg = ""

            while not args_built:
                try:
                    # result = self.net_elem_kw.execute_keyword(dev_name, args, api_method, command_api_const=feature)[0]
                    args_built = True
                except KeyError as e:
                    if str(e).strip("'") == current_arg:
                        _self.assertTrue(False, "Unable to generate args.")
                    current_arg = str(e).strip("'")
                    args[current_arg] = "test_val_" + str(e).strip("'")
            _self.assertEqual(result.command, method_dict["return_command"])
        return generated_test
