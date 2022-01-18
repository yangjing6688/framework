"""
This class outlines all the constants for the webapp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(WebappConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class WebappConstants(ApiConstants):
    def __init__(self):
        super(WebappConstants, self).__init__()
        self.ACCEPT_DIALOG_BOX = {"constant": "accept_dialog_box",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.accept_dialog_box}
        self.BROWSER_FULL_SCREEN = {"constant": "browser_full_screen",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.browser_full_screen}
        self.BROWSER_ZOOM_OUT = {"constant": "browser_zoom_out",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.browser_zoom_out}
        self.CLICK_LINK_TEXT = {"constant": "click_link_text",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.click_link_text}
        self.CLICK_NTH_LINK_TEXT = {"constant": "click_nth_link_text",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.click_nth_link_text}
        self.CLICK_ON_A_CELL_ON_THE_GRID = {"constant": "click_on_a_cell_on_the_grid",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.click_on_a_cell_on_the_grid}
        self.CLICK_ON_BUTTON = {"constant": "click_on_button",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.click_on_button}
        self.CLICK_STALE_ELEMENT = {"constant": "click_stale_element",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.click_stale_element}
        self.CLOSE_DIALOG_BOX = {"constant": "close_dialog_box",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.close_dialog_box}
        self.CLOSE_PAGE = {"constant": "close_page",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.close_page}
        self.CLOSE_TAB = {"constant": "close_tab",
                          "tags": ["COMMAND_SELENIUM"],
                          "link": self.link.close_tab}
        self.DOUBLE_CLICK = {"constant": "double_click",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.double_click}
        self.DRAG_AND_DROP_ELEMENT = {"constant": "drag_and_drop_element",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.drag_and_drop_element}
        self.ELEMENT_EXISTS = {"constant": "element_exists",
                               "tags": ["COMMAND_SELENIUM"],
                               "link": self.link.element_exists}
        self.FILTER_GRID_COLUMN_VALUES = {"constant": "filter_grid_column_values",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.filter_grid_column_values}
        self.FIND_A_ROW_FROM_GRID = {"constant": "find_a_row_from_grid",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.find_a_row_from_grid}
        self.GET_A_CELL_VALUE_FROM_GRID = {"constant": "get_a_cell_value_from_grid",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.get_a_cell_value_from_grid}
        self.GET_A_COLUMN_FROM_GRID = {"constant": "get_a_column_from_grid",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.get_a_column_from_grid}
        self.GET_A_ROW_FROM_GRID = {"constant": "get_a_row_from_grid",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.get_a_row_from_grid}
        self.GET_LIST_ITEM = {"constant": "get_list_item",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.get_list_item}
        self.GET_ROW_COUNT_FROM_GRID = {"constant": "get_row_count_from_grid",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.get_row_count_from_grid}
        self.INVOKE_DROPDOWN = {"constant": "invoke_dropdown",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.invoke_dropdown}
        self.INVOKE_POPUP_MENU = {"constant": "invoke_popup_menu",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.invoke_popup_menu}
        self.LAUNCH_XMC = {"constant": "launch_xmc",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.launch_xmc}
        self.LOGIN_TO_XMC = {"constant": "login_to_xmc",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.login_to_xmc}
        self.MOVE_MOUSE_OUT_OF = {"constant": "move_mouse_out_of",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.move_mouse_out_of}
        self.MOVE_MOUSE_OVER_ELEMENT = {"constant": "move_mouse_over_element",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.move_mouse_over_element}
        self.MOVE_MOUSE_OVER_IMG = {"constant": "move_mouse_over_img",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.move_mouse_over_img}
        self.OPEN_PAGE = {"constant": "open_page",
                          "tags": ["COMMAND_SELENIUM"],
                          "link": self.link.open_page}
        self.REJECT_DIALOG_BOX = {"constant": "reject_dialog_box",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.reject_dialog_box}
        self.SELECT_A_ROW_ON_THE_GRID = {"constant": "select_a_row_on_the_grid",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.select_a_row_on_the_grid}
        self.SELECT_BOUNDLIST_ITEM = {"constant": "select_boundlist_item",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.select_boundlist_item}
        self.SELECT_BOUNDLIST_ITEM_BY_INDEX = {"constant": "select_boundlist_item_by_index",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.select_boundlist_item_by_index}
        self.SELECT_PAGE = {"constant": "select_page",
                            "tags": ["COMMAND_SELENIUM"],
                            "link": self.link.select_page}
        self.SELECT_TREE_NODE_ITEM = {"constant": "select_tree_node_item",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.select_tree_node_item}
        self.SELECT_X_COLLAPSED_PANEL = {"constant": "select_x_collapsed_panel",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.select_x_collapsed_panel}
        self.SWITCH_TAB = {"constant": "switch_tab",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.switch_tab}
        self.WAIT_FOR = {"constant": "wait_for",
                         "tags": ["COMMAND_SELENIUM"],
                         "link": self.link.wait_for}
        self.WAIT_FOR_DIALOG_WINDOW = {"constant": "wait_for_dialog_window",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.wait_for_dialog_window}
        self.WAIT_FOR_LOADING = {"constant": "wait_for_loading",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.wait_for_loading}
        self.WAIT_FOR_MESSAGE_BOX = {"constant": "wait_for_message_box",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.wait_for_message_box}
        self.WAIT_FOR_PAGE_TO_LOAD = {"constant": "wait_for_page_to_load",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.wait_for_page_to_load}
