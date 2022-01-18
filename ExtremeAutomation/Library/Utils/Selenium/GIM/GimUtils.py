from ExtremeAutomation.Library.Utils.Selenium.SeleniumUtilsBase import SeleniumUtilsBase


class GimUtils(SeleniumUtilsBase):
    def __init__(self, builder_dict):
        super(GimUtils, self).__init__(builder_dict)

    def gim_spinner_loading(self, ui_cmd_obj):
        """
        validate gim page ready
        """
        self.base_builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                               strategy=self.constants.STRATEGY_CSS_SELECTOR,
                                               condition=self.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def gim_select_row_from_table(self, ui_cmd_obj, select_text):
        """
        Select row from gim table
        """
        row_count = self.builder.get_length_of_find_elements("//div[@class ='x-grid-item-container']/table",
                                                             strategy=self.constants.STRATEGY_ELEMENTS_XPATH)

        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element("//div[@class ='x-grid-item-container']/table[" +
                                                str(index) + "]/tbody/tr/td[1]", strategy=self.constants.STRATEGY_XPATH)
            return_text = web_obj.text
            self.logger.log_info("ot_name: " + str(index) + "::" + return_text)
            if return_text == select_text:
                self.base_builder.click(ui_cmd_obj, web_obj)
                break
        return ui_cmd_obj
