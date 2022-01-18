from ExtremeAutomation.Library.Utils.Selenium.SeleniumUtilsBase import SeleniumUtilsBase


class EmcUtils(SeleniumUtilsBase):
    def __init__(self, builder_dict):
        super(EmcUtils, self).__init__(builder_dict)

    def test_utls(self, ui_cmd_obj):
        """
        This is a test function
        """
        self.ext_builder.click(ui_cmd_obj,
                               'tab[text=Policy] => .x-tab-inner-extr-main-tab-panel')
        return ui_cmd_obj

    def click_on_a_cell_on_the_grid(self, ui_cmd_obj, table_css_locator, row_no, col_no):
        """
        click on cell grid
        """
        self.base_builder.webdriver_wait_until(ui_cmd_obj, table_css_locator, 10, 1,
                                               self.base_builder.constants.STRATEGY_CSS_SELECTOR,
                                               self.base_builder.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED)
        locator = table_css_locator + ">tbody>tr:nth-child(" + row_no + ")>td:nth-child(" + col_no + ")"
        cell = self.base_builder.find_element_by_css_selector(ui_cmd_obj, locator)
        self.base_builder.click(ui_cmd_obj, cell)

        return ui_cmd_obj
