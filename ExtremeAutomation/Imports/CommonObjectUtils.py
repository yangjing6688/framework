from robot.libraries.BuiltIn import BuiltIn

class CommonObjectUtils:
    def __init__(self):
        self.builtin = BuiltIn()

    def check_cli_type_and_skip(self, accepted_list, cli_type, skip_msg="Not Executed: This test is not support for device type"):
        """
       - Will check the device (cli_type) against the supported device type (list).
         # Device type:
            - VOSS
            - EXOS
            - WING-AP
            - AH-FASTPATH
            - AH-AP
            - AH-XR
        # Endsystem:
            - MU-WINDOWS
            - MU-MAC
            - MU-LINUX
            - A3
       - Keyword Usage:
        - ``check_cli_type_and_skip  ${accepted_list}  ${CLI_TYPE}``

       :param accepted_list: List of device types that are supported
       :param cli_type: The cli type

       :return: If the device type is found, it will return, otherwise it will skip the test.
       """
        if cli_type not in accepted_list:
            self.builtin.skip(skip_msg)

    def convert_to_generic_device_object(self, new_name, index=1, look_for_device_type=None, set_to_index=1):
        value = None
        generic_device_types = ['ap', 'wing', 'netelem', 'router', 'aerohive_sw']

        if look_for_device_type != None:
            try:
                get_value = self.setExecutionVariable(look_for_device_type,str(index))
                value = self.builtin.get_variable_value(get_value)
            except Exception:
                pass
        else:
            for generic_type in generic_device_types:
                try:
                    get_value = self.setExecutionVariable(generic_type, str(index))
                    value = self.builtin.get_variable_value(get_value)
                    if value:
                        break
                except Exception:
                    pass
        if value:
            try:
                # Try and get the generic capwap URL
                generic_capwap_url = self.builtin.get_variable_value(self.setExecutionVariable("capwap_url",""))
                if value['cli_type'].upper() == 'EXOS' or value['cli_type'].upper() == 'VOSS' or value['cli_type'].upper() == 'AH-FASTPATH':
                    generic_capwap_url = self.builtin.get_variable_value(self.setExecutionVariable("sw_capwap_url",""))
                elif value['cli_type'].upper() == 'WING-AP':
                    generic_capwap_url = self.builtin.get_variable_value(self.setExecutionVariable("wing_capwap_url", ""))
                self.builtin.set_global_variable(self.setExecutionVariable("generic_capwap_url",""), generic_capwap_url)
                generic_capwap_url_check = self.builtin.get_variable_value(self.setExecutionVariable("generic_capwap_url", ""))
                if not generic_capwap_url_check:
                    self.builtin.fail("Can't set the generic_capwap_url OBJECT in the variables.")
            except Exception:
                # Let's not print an error here because the user may just want to create a generic device
                pass

            new_value_key = self.setExecutionVariable(new_name, str(set_to_index))
            self.builtin.set_global_variable(new_value_key, value)
            value = self.builtin.get_variable_value(self.setExecutionVariable(new_name, str(set_to_index)))
            if not value:
                self.builtin.fail("Can't set the generic Device OBJECT in the variables.")
        else:
            print("Can't set the generic Device OBJECT in the variables. The following types were not found in the yaml file: " + ' '.join(generic_device_types))

    def setExecutionVariable(self, value, index):
        if self.executionModePytest():
            execution_value = value + str(index)
        else:
            execution_value = "${" + value + str(index) + "}"
        return execution_value


    def executionModePytest(self):
        running_pytest = False
        try:
            running_pytest = self.builtin.isRunningPytest()
        except Exception:
            pass
        return running_pytest
