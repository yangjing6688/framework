from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.ParsingHelper.InspectionConstants import InspectionConstants
from ExtremeAutomation.Library.ParsingHelper.PortParsers.PortParserFactory import PortParserFactory


class InspectionToolkit(object):
    """
    The Inspection Toolkit class is a bundle of cli output parsing and value comparison tools
    that are specific to the NetworkElement object provided as a constructor argument. It currently
    contains the following tools:
        Generating custom parsing objects
        ---------------------------------------------------
        self.get_port_parser_obj('ge.1.1-10,12')

        Comparisons between different data types
        ----------------------------------------------------
        self.compare_port_values(cli_return, 'ge.1.5', InspectionToolkitConstants.FOUNDIN)
    """

    def __init__(self, device):
        self.device = device
        self.logger = Logger()
        self.port_parser_factory = PortParserFactory()
        self.constants = InspectionConstants()

    def get_port_parser_obj(self, ports):
        """
        Gets the correct Port Parser API for the device.

        :param ports: A string representing a port or block of ports (ge.1.1, ge.1.1-10, 1:1, 1:1-10, etc)
        :return: A PortParser object initialized with the provided port list
        """
        return self.port_parser_factory.get_api(self.device, api_args=ports)

    def compare_port_values(self, port_str, req_port, operand):
        """
        Function Args:
        [port_str] - This is a string or ports. It can contain multiple ports including ranges.
        [req_port] - This must be a single port. This is the port to check against the port_str using
                     the given operand.
        [operand] - The operand to use when comparing the port_str and req_port. Supported operands are
                    EQUALTO, NOTEQUALTO, CONTAINS, FOUNDIN, NOTCONTAIN, and NOTFOUNDIN.

        This function checks the req_port against the port list using the provided operator.
        """
        port = self.get_port_parser_obj(port_str)
        req_port = self.get_port_parser_obj(req_port)

        oper_dict = {self.constants.EQUALTO: port.collapse_port_list() == req_port.collapse_port_list(),
                     self.constants.NOTEQUALTO: port.collapse_port_list() != req_port.collapse_port_list(),
                     self.constants.CONTAINS: port.is_port_on_list(req_port),
                     self.constants.FOUNDIN: port.is_port_on_list(req_port),
                     self.constants.NOTCONTAIN: not port.is_port_on_list(req_port),
                     self.constants.NOTFOUNDIN: not port.is_port_on_list(req_port)}

        if operand in oper_dict:
            return oper_dict[operand]
        self.logger.log_debug('InspectionToolkit: operand (' + operand + ') is not valid for Port inspection')
