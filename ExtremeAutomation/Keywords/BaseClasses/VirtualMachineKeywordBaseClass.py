import time
from ExtremeAutomation.Keywords.BaseClasses.KeywordBaseClass import KeywordBaseClass
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants


class VirtualMachineKeywordBaseClass(KeywordBaseClass):
    def __init__(self):
        super(VirtualMachineKeywordBaseClass, self).__init__()

        self.vm = None
        self.vm_api = None
        self.constants = VirtualConstants()

    def _init_keyword(self, device_name=None, vm_api_const=None, **kwargs):
        device = super(VirtualMachineKeywordBaseClass, self)._init_keyword(device_name=device_name, **kwargs)

        self._parse_kwargs(device, **kwargs)

        if vm_api_const is not None and device_name is not None:
            self.vm_api = device.get_api(vm_api_const)

    def _wait_for(self, max_wait, interval, message, _function, expected_result, *args):
        """
        Arguments:
        [max_wait] - The maximum amount time the function will wait before stopping.
        [interval] - How often the function should be performed.
        [message] - The message to print each iteration.
        [show_func] - The command to send who's output will later be parsed. Ex "self.command_api.showVlanInfo".
                      Do NOT include the parenthesis.
        [parse_func] - The parse function that should be used to parse the output from <show_func>.
                       Ex "self.parse_api.check_vlan_exists". Do NOT include the parenthesis.
        [expected_result] - The result we expect returned by the parser function.
        [*parse_args] - The arguments required by the parsing function, minus the output, that is passed automatically.
                        Any number of arguments can be passed here depending on what is required by the parse
                        function.
        """
        output = _function(*args)
        result = False

        start_time = time.time()
        if output == expected_result:
            self.logger.log_debug("Condition already met.")
            return output

        while output != expected_result:
            if int(time.time() - start_time) > int(max_wait):
                break
            else:
                self.logger.log_info(message + "[Elapsed Time: " + str(int(time.time() - start_time)) + " seconds.]")
                output = _function(*args)

            time.sleep(int(interval))
        if output == expected_result:
            result = True

        return result

    def _parse_kwargs(self, dev, **kwargs):
        super(VirtualMachineKeywordBaseClass, self)._parse_kwargs(dev, **kwargs)
