from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.BaseUiApiBuilder import BaseUiApiBuilder
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.UiApiBuilder import UiApiBuilder
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.ExtjsUiApiBuilder import ExtjsUiApiBuilder
from ExtremeAutomation.Library.Utils.Selenium.EMC.EmcUtils import EmcUtils
from ExtremeAutomation.Library.Utils.Selenium.GIM.GimUtils import GimUtils
from ExtremeAutomation.Library.Utils.Selenium.SeleniumUtilsConstants import SeleniumUtilsConstants


class UiBaseApi(BaseApi):
    def __init__(self, device):
        super(UiBaseApi, self).__init__()
        self.logger = Logger()
        self.ui_element = None
        self.builder = UiApiBuilder(device)
        self.ext_builder = ExtjsUiApiBuilder(device)
        self.base_builder = BaseUiApiBuilder(device)
        builder_dict = {SeleniumUtilsConstants.logger: self.logger,
                        SeleniumUtilsConstants.base_builder: self.base_builder,
                        SeleniumUtilsConstants.builder: self.builder,
                        SeleniumUtilsConstants.ext_builder: self.ext_builder}
        self.emc_helpers = EmcUtils(builder_dict)
        self.gim_helpers = GimUtils(builder_dict)
