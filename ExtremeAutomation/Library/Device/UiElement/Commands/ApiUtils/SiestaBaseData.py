from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.SiestaApiUtils import SiestaApiUtils


class SiestaBaseData(object):
    def __init__(self, ui_element):
        self.ui_element = ui_element
        self.builder = SiestaApiUtils(self.ui_element)
        self.logger = Logger()
