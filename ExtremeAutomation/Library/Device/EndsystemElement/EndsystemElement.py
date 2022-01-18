from ExtremeAutomation.Library.Utils.EndsystemElementUtils import EndsystemElementUtils
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.Common.Agents.NorthBoundAgent import NorthboundAgent
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants \
    import EndsystemElementConstants


class EndsystemElement(NetworkElement):
    def __init__(self, oper_sys, platform, unit, version):
        """
        init function
        """
        super(EndsystemElement, self).__init__(oper_sys, platform, unit, version)
        self.agent_dict[self.agent_constants.TYPE_NORTHBOUND] = NorthboundAgent
        self.remove_control_chars = False

    def send_command_object(self, cmd_obj, **kwargs):
        """
        This function calls the parent class's send_command_object function. Then if the
        remove_control_chars flag is set all control chars will be removed from the
        output. Otherwise it is returned as received.
        """
        return_val = super(EndsystemElement, self).send_command_object(cmd_obj, **kwargs)

        if self.remove_control_chars:
            return_val.return_text = EndsystemElementUtils.remove_control_characters(return_val.return_text)

        return return_val

    def get_base_attrs(self):
        """
        This function returns the base attributes for an end system. The base attributes
        are used by the API factories as folders when no match can be found.
        """
        base_attrs = [getattr(EndsystemElementConstants, "PLATFORM_" + self.oper_sys + "_BASE"),
                      EndsystemElementConstants.VERSION_BASE,
                      EndsystemElementConstants.UNIT_BASE
                      ]

        return base_attrs
