from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XMC.WebappConstants import WebappConstants


class UiWdsbiWebappKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiWdsbiWebappKeywords, self).__init__()
        self.api_const = self.constants.API_XMC_WEBAPP
        self.command_const = WebappConstants()

    def open_page(self, element_name, browser, url, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [browser]           - The xbrowser type such as Firefox, Chrome, IE and so on.
        [url]               - The URL the browser should open.

        Open a URL on the specified browser.
        """
        args = {"browser": browser,
                "url": url,
                }

        return self.execute_keyword(element_name, args, self.command_const.OPEN_PAGE, **kwargs)

    def close_page(self, element_name, **kwargs):
        """
        [element_name]      - The UI element(s) the keyword should be run against.

        Close the browser for a given element.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLOSE_PAGE, **kwargs)

    def launch_xmc(self, element_name, browser, url, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [browser]           - The xbrowser type such as Firefox, Chrome, IE and so on.
        [url]               - The URL the browser should open.

        Open a XMC web application on the specified browser.
        """
        args = {"browser": browser,
                "url": url,
                }

        return self.execute_keyword(element_name, args, self.command_const.LAUNCH_XMC, **kwargs)

    def login_to_xmc(self, element_name, username, password, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [username]          - Username
        [password]          - Password

        Login to XMC with valid user credentials
        """
        args = {"username": username,
                "password": password
                }

        return self.execute_keyword(element_name, args, self.command_const.LOGIN_TO_XMC, **kwargs)

    def switch_tab(self, element_name, link_text, partial=None, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [link_text]         - link text
        [partial]           - partial link text

        Wait for a page to load
        """
        args = {"link_text": link_text,
                "partial": partial
                }

        return self.execute_keyword(element_name, args, self.command_const.SWITCH_TAB, **kwargs)

    def select_page(self, element_name, link_text, partial=None, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [link_text]         - link text
        [partial]           - parital link text

        Select a page
        """
        args = {"link_text": link_text,
                "partial": partial
                }

        return self.execute_keyword(element_name, args, self.command_const.SELECT_PAGE, **kwargs)

    def click_on_button(self, element_name, link_text, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [link_text]         - link text

        Click on a push button
        """
        args = {"link_text": link_text
                }

        return self.execute_keyword(element_name, args, self.command_const.CLICK_ON_BUTTON, **kwargs)

    def click_link_text(self, element_name, link_text, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [link_text]         - link text

        Click on a link
        """
        args = {"link_text": link_text
                }

        return self.execute_keyword(element_name, args, self.command_const.CLICK_LINK_TEXT, **kwargs)

    def click_nth_link_text(self, element_name, link_text, x_link_text, partial=None, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [link_text]         - link text
        [x_link_text]       - nth link text
        [partial]           - parital link text

        Click on a nth link if there are multiple links with same name/text
        """
        args = {"link_text": link_text,
                "x_link_text": x_link_text,
                "partial": partial
                }

        return self.execute_keyword(element_name, args, self.command_const.CLICK_NTH_LINK_TEXT, **kwargs)

    def wait_for(self, element_name, seconds, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [seconds]           - seconds

        Wait for x seconds
        """
        args = {"seconds": seconds
                }

        return self.execute_keyword(element_name, args, self.command_const.WAIT_FOR, **kwargs)

    def wait_for_page_to_load(self, element_name, title, timeout=30, **kwargs):
        """
        Keyword Arguments:
        [element_name]  - The UI element(s) the keyword should be run against.
        [username]      - window/page title either in partial or absolute
        [password]      - time to wait

        Switch to a new tab
        """
        args = {"title": title,
                "timeout": timeout
                }

        return self.execute_keyword(element_name, args, self.command_const.WAIT_FOR_PAGE_TO_LOAD, **kwargs)

    def wait_for_loading(self, element_name, timeout=10, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [timeout]           - timeout

        Wait for page loading/rendering
        """
        args = {"timeout": timeout,
                }

        return self.execute_keyword(element_name, args, self.command_const.WAIT_FOR_LOADING, **kwargs)

    def element_exists(self, element_name, by, locator, timeout=10, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [by]                - The UI element locator type (i.e., strategy name)
        [locator]           - The UI element locator
        [timeout]           - timeout

        Check if element exists
        """
        args = {"by": by,
                "locator": locator,
                "timeout": timeout,
                }

        return self.execute_keyword(element_name, args, self.command_const.ELEMENT_EXISTS, **kwargs)

    def accept_dialog_box(self, element_name, accept_button, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [accept_button]     - Accept button(s) such as Yes, OK, Save and so on

        Click on accept button to accept the changes
        """
        args = {"accept_button": accept_button}

        return self.execute_keyword(element_name, args, self.command_const.ACCEPT_DIALOG_BOX, **kwargs)

    def reject_dialog_box(self, element_name, reject_button, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [accept_button]     - Reject button(s) such as No, Cancel, Close and so on

        Click on reject button to reject the changes
        """
        args = {"reject_button": reject_button}

        return self.execute_keyword(element_name, args, self.command_const.REJECT_DIALOG_BOX, **kwargs)

    def invoke_popup_menu(self, element_name, webelement, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [webelement]        - Web element object

        Invoke a popup menu
        """
        args = {"webelement": webelement}

        return self.execute_keyword(element_name, args, self.command_const.INVOKE_POPUP_MENU, **kwargs)

    def select_tree_node_item(self, element_name, treenodes, css_locator, search_order="bottom-up", **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [treenodes]         - Tree node with absolute path delimited by  pipe (|)
        [css_locator]       - CSS locator for the tree node item
        [search_order]      - Search order of Tree node navigation. By default Nodes are searched in
                              bottomup (reverse) order

        Select a treenode item by drilling down a path
        """
        args = {"treenodes": treenodes,
                "css_locator": css_locator,
                "search_order": search_order
                }

        return self.execute_keyword(element_name, args, self.command_const.SELECT_TREE_NODE_ITEM, **kwargs)

    def drag_and_drop_element(self, element_name, webelement, x, y, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [webelement]        - Web element object
        [x]                 - X coordinate
        [y]                 - Y coordinate

        Drag and drop an element
        """
        args = {"webelement": webelement,
                "x": x,
                "y": y
                }

        return self.execute_keyword(element_name, args, self.command_const.DRAG_AND_DROP_ELEMENT, **kwargs)

    def double_click(self, element_name, webelement, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [webelement]        - Web element object

        Double click on element
        """
        args = {"webelement": webelement}

        return self.execute_keyword(element_name, args, self.command_const.DOUBLE_CLICK, **kwargs)

    def click_stale_element(self, element_name, by, locator, timeout=10, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [by]                - The UI element locator type (i.e., strategy name)
        [locator]           - The UI element locator
        [timeout]           - Number of seconds to wait

        Drag and drop an element
        """
        args = {"by": by,
                "locator": locator,
                "timeout": timeout
                }

        return self.execute_keyword(element_name, args, self.command_const.CLICK_STALE_ELEMENT, **kwargs)

    def move_mouse_out_of(self, element_name, by, locator, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [by]                - The UI element locator type (i.e., strategy name)
        [locator]           - The UI element locator

        Move mouse out of an element
        """
        args = {"by": by,
                "locator": locator
                }

        return self.execute_keyword(element_name, args, self.command_const.MOVE_MOUSE_OUT_OF, **kwargs)

    def move_mouse_over_element(self, element_name, webelement, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [element]           - The UI element locator type (i.e., strategy name)

        Move mouse over a web element
        """
        args = {"webelement": webelement}

        return self.execute_keyword(element_name, args, self.command_const.MOVE_MOUSE_OVER_ELEMENT, **kwargs)

    def move_mouse_over_img(self, element_name, by, locator, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [by]                - he UI element locator type (i.e., strategy name)
        [locator]           - The UI element locator

        Move mouse over image to get toolips and so on
        """
        args = {"by": by,
                "locator": locator
                }

        return self.execute_keyword(element_name, args, self.command_const.MOVE_MOUSE_OVER_IMG, **kwargs)

    def invoke_dropdown(self, element_name, by, locator, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [by]                - he UI element locator type (i.e., strategy name)
        [locator]           - The UI element locator

        Invoke a drop down list
        """
        args = {"by": by,
                "locator": locator
                }

        return self.execute_keyword(element_name, args, self.command_const.INVOKE_DROPDOWN, **kwargs)

    def select_boundlist_item(self, element_name, itemname, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [itemname]          - Bound list item name

        Select an item from bound list
        """
        args = {"itemname": itemname}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_BOUNDLIST_ITEM, **kwargs)

    def select_boundlist_item_by_index(self, element_name, index, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [index]             - bound list item index

        Select an item from bound list by its index
        """
        args = {"index": index}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_BOUNDLIST_ITEM_BY_INDEX, **kwargs)

    def select_x_collapsed_panel(self, element_name, css_locator, panel_title, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [locator]           - CSS locator for the UI element

        Open a collapsed x-panel.
        """
        args = {"css_locator": css_locator,
                "panel_title": panel_title
                }

        return self.execute_keyword(element_name, args, self.command_const.SELECT_X_COLLAPSED_PANEL, **kwargs)

    def get_list_item(self, element_name, css_locator, index, **kwargs):
        """
        Keyword Arguments:
        [element_name]         - The UI element(s) the keyword should be run against.
        [css_locator]          - CSS locator of a list element
        [index]                - X item of a list

        Get a list item based on its index
        """
        args = {"css_locator": css_locator,
                "index": index
                }

        return self.execute_keyword(element_name, args, self.command_const.GET_LIST_ITEM, **kwargs)

    def wait_for_message_box(self, element_name, timeout=15, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [timeout]           - Number of seconds to wait

        Wait for a message box to appear
        """
        args = {"timeout": timeout}

        return self.execute_keyword(element_name, args, self.command_const.WAIT_FOR_MESSAGE_BOX, **kwargs)

    def wait_for_dialog_window(self, element_name, windowid, timeout=15, **kwargs):
        """
        Keyword Arguments:
        [element_name]      - The UI element(s) the keyword should be run against.
        [windowid]          - Window ID attribute
        [timeout]           - Number of seconds to wait

        Wait for a dialog window to appear
        """
        args = {"windowid": windowid,
                "timeout": timeout
                }

        return self.execute_keyword(element_name, args, self.command_const.WAIT_FOR_DIALOG_WINDOW, **kwargs)

    def find_a_row_from_grid(self, element_name, grid_table_css_locator, row_content, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element
        [row_content]               - Row content to search for

        Find a row based on serach text from a grid
        """
        args = {"grid_table_css_locator": grid_table_css_locator,
                "row_content": row_content
                }

        return self.execute_keyword(element_name, args, self.command_const.FIND_A_ROW_FROM_GRID, **kwargs)

    def get_a_row_from_grid(self, element_name, grid_table_css_locator, row_no, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element
        [row_no]                    - nth row number

        Get a x row (contents) from a grid
        """
        args = {"grid_table_css_locator": grid_table_css_locator,
                "row_no": row_no
                }

        return self.execute_keyword(element_name, args, self.command_const.GET_A_ROW_FROM_GRID, **kwargs)

    def select_a_row_on_the_grid(self, element_name, grid_table_css_locator, row_no, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element
        [row_no]                    - nth row number

        Select a x row from a grid
        """
        args = {"grid_table_css_locator": grid_table_css_locator,
                "row_no": row_no
                }

        return self.execute_keyword(element_name, args, self.command_const.SELECT_A_ROW_ON_THE_GRID, **kwargs)

    def get_a_column_from_grid(self, element_name, grid_table_css_locator, col_no, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element
        [col_no]                    - nth column number

        Get a x column content from a grid especially from a row
        """
        args = {"grid_table_css_locator": grid_table_css_locator,
                "col_no": col_no
                }

        return self.execute_keyword(element_name, args, self.command_const.GET_A_COLUMN_FROM_GRID, **kwargs)

    def get_a_cell_value_from_grid(self, element_name, grid_table_css_locator, row_no, col_no, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element
        [row_no]                    - nth row number
        [col_no]                    - nth column number

        Get a cell (x, y) value from a grid
        """
        args = {"grid_table_css_locator": grid_table_css_locator,
                "row_no": row_no,
                "col_no": col_no
                }

        return self.execute_keyword(element_name, args, self.command_const.GET_A_CELL_VALUE_FROM_GRID, **kwargs)

    def get_row_count_from_grid(self, element_name, grid_table_css_locator, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element

        Get row(s) count from a grid
        """
        args = {"grid_table_css_locator": grid_table_css_locator}

        return self.execute_keyword(element_name, args, self.command_const.GET_ROW_COUNT_FROM_GRID, **kwargs)

    def click_on_a_cell_on_the_grid(self, element_name, grid_table_css_locator, row_no, col_no, **kwargs):
        """
        Keyword Arguments:
        [element_name]              - The UI element(s) the keyword should be run against.
        [grid_table_css_locator]    - CSS locator of Grid Table element
        [row_no]                    - nth row number
        [col_no]                    - nth column number

        Click on a cell (x, y) value from a grid
        """
        args = {"grid_table_css_locator": grid_table_css_locator,
                "row_no": row_no,
                "col_no": col_no
                }

        return self.execute_keyword(element_name, args, self.command_const.CLICK_ON_A_CELL_ON_THE_GRID, **kwargs)

    def filter_grid_column_values(self, element_name, column_tooltip, **kwargs):
        """
        Keyword Arguments:
        [element_name]          - The UI element(s) the keyword should be run against.
        [column_tooltip]        - Column header tooltip message

        Apply a filter on a column if it's supported
        """
        args = {"column_tooltip": column_tooltip}

        return self.execute_keyword(element_name, args, self.command_const.FILTER_GRID_COLUMN_VALUES, **kwargs)

    def close_tab(self, element_name, **kwargs):
        """
        [element_name]      - The UI element(s) the keyword should be run against.

        Close an open tab
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLOSE_TAB, **kwargs)

    def close_dialog_box(self, element_name, **kwargs):
        """
        [element_name]      - The UI element(s) the keyword should be run against.

        Close dialog box
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLOSE_DIALOG_BOX, **kwargs)

    def browser_full_screen(self, element_name, **kwargs):
        """
        [element_name]      - The UI element(s) the keyword should be run against.

        Full screen of browser (headless browser)
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_FULL_SCREEN, **kwargs)

    def browser_zoom_out(self, element_name, percentage, **kwargs):
        """
        Keyword Arguments:
        [element_name]          - The UI element(s) the keyword should be run against.
        [percentage]            - Column header tooltip message

        Zoom out browser (window) size
        """
        args = {"percentage": percentage}

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_ZOOM_OUT, **kwargs)
