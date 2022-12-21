from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.access_control.ControlAccessControlTreeWebElements import ControlAccessControlTreeWebElements
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class XIQSE_AccessControlTree(ControlAccessControlTreeWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.ac_tree_els = ControlAccessControlTreeWebElements()
        self.screen = Screen()

    def xiqse_control_select_engines_tree_node(self, treenode):
        """
        - This keyword selects the specified tree node on the Control> Access Control Tab
        - Keyword Usage
        - ``XIQSE Control Select Engines Tree Node   ${TREENODE}``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.ac_tree_els.get_engines_tree_node(treenode)
        if the_node:
            # Will need to add a slight delay here to make sure data is properly displayed in panel
            sleep(5)
            self.utils.print_info(f"Selecting {treenode} Tree Node...")
            self.auto_actions.click(the_node)
            sleep(5)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to select {treenode} tree node")
            self.screen.save_screen_shot()
        return ret_val
