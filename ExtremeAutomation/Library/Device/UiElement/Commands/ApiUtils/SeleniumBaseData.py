from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Agents.SeleniumAgent import SeleniumConstants
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.UiApiBuilder import UiApiBuilder


class SeleniumBaseData(object):
    def __init__(self, ui_element):
        self.ui_element = ui_element
        self.builder = UiApiBuilder(self.ui_element)
        self.logger = Logger()
        self.constants = SeleniumConstants()
