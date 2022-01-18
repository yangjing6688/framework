from ExtremeAutomation.Library.Utils.Selenium.SeleniumUtilsConstants import SeleniumUtilsConstants
from ExtremeAutomation.Library.Device.Common.Agents.BaseSeleniumAgent import SeleniumConstants


class SeleniumUtilsBase(object):
    def __init__(self, builder_dict):
        self.logger = builder_dict[SeleniumUtilsConstants.logger]
        self.builder = builder_dict[SeleniumUtilsConstants.builder]
        self.base_builder = builder_dict[SeleniumUtilsConstants.base_builder]
        self.ext_builder = builder_dict[SeleniumUtilsConstants.ext_builder]
        self.constants = SeleniumConstants
