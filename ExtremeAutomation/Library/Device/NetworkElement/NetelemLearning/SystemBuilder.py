import abc
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Port import Port
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Unit import Unit
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Stack import Stack
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.System import System
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Chassis import Chassis
# from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.OptionModule import OptionModule
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.DeviceDiscoveryKeywords import \
    DeviceDiscoveryKeywords


class Builder(object):
    def __init__(self, netelem_name):
        self.sys_builder = SystemBuilder(netelem_name)

    def build(self):
        """
        This is the main build method. Users should call this in order to build their system.
        """
        return self.sys_builder.build()


class BaseBuilder(object):
    def __init__(self, netelem_name):
        self.lrn_kw = DeviceDiscoveryKeywords()
        self.netelem_name = netelem_name
        self.device = DeviceCollectionManager().get_device(netelem_name)

    @abc.abstractmethod
    def build(self, *args):
        """
        This function must be overridden by any child classes. It provides the code
        for building whatever kind of object the builder class creates.
        """
        pass


class SystemBuilder(BaseBuilder):
    """
    This class figures out what kind of system is being built then calls the correct build() function.
    """

    def __init__(self, netelem_name):
        super(SystemBuilder, self).__init__(netelem_name)
        self.system = None

        sys_info = self.lrn_kw.get_system_info(self.netelem_name)

        if sys_info is not None:
            self.system = System(**sys_info)

    def build(self):
        """
        This function builds a system. A system can be made up of many components. Including
        stacks, chassis, and units. Once it figures out what type of system it's creating it
        calls the needed build function of the component(s).
        """
        component = None

        if self.lrn_kw.is_stacked(self.netelem_name):
            if self.lrn_kw.is_chassis(self.netelem_name):
                component = StackBuilder(self.netelem_name).build(StackBuilder.TYPE_CHASSIS)
            else:
                component = StackBuilder(self.netelem_name).build(StackBuilder.TYPE_UNIT)
        elif self.lrn_kw.is_chassis(self.netelem_name):
            component = ChassisBuilder(self.netelem_name).build()
        elif self.system is not None:
            component = UnitBuilder(self.netelem_name).build()

        if component is not None:
            self.system.add_component(component)

        return self.system


class StackBuilder(BaseBuilder):
    """
    This class figures out which slots are present in the stack. Then builds each component.
    """

    TYPE_CHASSIS = "chassis"
    TYPE_UNIT = "unit"

    def build(self, _type):
        """
        This function builds a stack. For each slot of the stack it creates either a
        chassis or unit.
        """
        stack = Stack()
        slot_numbers = self.lrn_kw.get_stack_slots(self.netelem_name)

        for slot in slot_numbers:
            if _type == self.TYPE_CHASSIS:
                stack.add_component(ChassisBuilder(self.netelem_name).build(slot))
            elif _type == self.TYPE_UNIT:
                stack.add_component(UnitBuilder(self.netelem_name).build(slot))

        return stack


class ChassisBuilder(BaseBuilder):
    """
    This class figures out which units are present within a chassis. Then builds each unit.
    """

    def build(self, chassis_number=None):
        """
        This function creates a chassis object based on the passed chassis number.
        """
        chassis = Chassis(**self.lrn_kw.get_chassis_info(self.netelem_name, chassis_number))
        slot_numbers = self.lrn_kw.get_chassis_slots(self.netelem_name, chassis_number)

        for slot in slot_numbers:
            chassis.add_component(UnitBuilder(self.netelem_name).build(slot))

        return chassis


class UnitBuilder(BaseBuilder):
    """
    This class builds a unit based on the provided slot number.
    """

    def build(self, slot_number=None):
        """
        This function creates a unit based on the passed slot number.
        """
        unit = Unit(**self.lrn_kw.get_unit_info(self.netelem_name, slot_number))
        unit.ports = PortBuilder(self.netelem_name).build(self.lrn_kw.get_port_info(self.netelem_name, slot_number))

        return unit


class OptionModuleBuilder(BaseBuilder):
    # Issue some command to figure out what ports are present.
    # Then create them.
    # if has_ports:
    #    for port present:
    #        PortBuilder().create_port()
    # Create and return OptionModule object.

    def build(self):
        """
        This function builds an option module object.
        """
        pass


class PortBuilder(BaseBuilder):
    def build(self, port_info_list):
        """
        Thsi function creates a port object for each port in the passed <port_info_list>.
        """
        ports = []

        for port_dict in port_info_list:
            ports.append(Port(**port_dict))

        return ports
