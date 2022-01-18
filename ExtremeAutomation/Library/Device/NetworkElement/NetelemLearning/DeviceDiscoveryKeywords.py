from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import \
    NetworkElementConstants as Constants


class DeviceDiscoveryKeywords(NetworkElementKeywordBaseClass):
    def _initialize_keyword(self, device_name=None):
        return self._init_keyword(device_name, Constants.API_DUT_LEARNING, self.constants.API_DUT_LEARNING,
                                  log_keyword=False)

    def is_stacked(self, netelem_name):
        """
        This function checks if the given device is stacked.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_stacking_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.is_stacked(cmd_obj.return_text)
        return ret_val

    def is_chassis(self, netelem_name):
        """
        This function checks if the given device is a chassis.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_chassis_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.is_chassis(cmd_obj.return_text)
        return ret_val

    def get_unit_info(self, netelem_name, slot_number):
        """
        This function gathers all needed information from a given slot on a device.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_unit_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.gather_unit_info(cmd_obj.return_text, slot_number)
        return ret_val

    def get_chassis_slots(self, netelem_name, chassis_number=None):
        """
        This function returns the slot number for each slot present on the system.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_chassis_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.get_chassis_slot_numbers(cmd_obj.return_text, chassis_number)
        return ret_val

    def get_stack_slots(self, netelem_name):
        """
        This function gets the slot number for each slot present in a stack.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_stack_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.get_stack_slot_numbers(cmd_obj.return_text)
        return ret_val

    def get_system_info(self, netelem_name):
        """
        This function returns all information about a given device.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_system_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.gather_system_info(cmd_obj.return_text)
        return ret_val

    def get_chassis_info(self, netelem_name, chassis_number):
        """
        This function returns all information about a given chassis.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)
        cmd_obj = dev.send_command_object(cmd_api.show_chassis_info(None))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.gather_chassis_info(cmd_obj.return_text, chassis_number)
        return ret_val

    def get_port_info(self, netelem_name, slot_number):
        """
        This function returns all port info for a give slot on a device.
        """
        dev, cmd_api, parse_api = self._initialize_keyword(netelem_name)

        if dev.oper_sys == self.constants.OS_EOS:
            slot_number = slot_number if slot_number is not None else "1"

        args = {"slot_number": slot_number if slot_number is not None else ""}
        cmd_obj = dev.send_command_object(cmd_api.show_port_info(args))

        if cmd_obj.not_supported:
            return None
        ret_val, get_val = parse_api.gather_port_info(cmd_obj.return_text)
        return ret_val
