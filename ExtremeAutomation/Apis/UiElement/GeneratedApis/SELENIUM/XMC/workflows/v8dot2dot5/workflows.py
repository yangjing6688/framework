# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XMC.webapp.baseappver.webapp \
    import Webapp as WorkflowsBase


class Workflows(WorkflowsBase):
    def expand_workflow_tree_panel_size(self, ui_cmd_obj, arg_dict):
        weblement = self.builder.driver.find_element_by_css_selector("div[id$='splitter']:nth-child(4)")
        self._drag_and_drop_element(ui_cmd_obj, weblement, int(arg_dict["x"]), int(arg_dict["y"]))

        return ui_cmd_obj

    def expand_workflow_activity_panel_size(self, ui_cmd_obj, arg_dict):
        weblement = self.builder.driver.find_element_by_css_selector("div[id$='splitter']:nth-child(1)")
        self._drag_and_drop_element(ui_cmd_obj, weblement, int(arg_dict["x"]), int(arg_dict["y"]))

        return ui_cmd_obj

    def collapse_all_user_workflow_items(self, ui_cmd_obj, arg_dict):
        weblement = self.builder.driver.find_element_by_css_selector("div[id^='workflowTree']>div>div.x-grid-item-"
                                                                     "container>table:nth-child(1)")
        self._double_click(ui_cmd_obj, weblement)

        return ui_cmd_obj

    def select_workflows_tab(self, ui_cmd_obj, arg_dict):
        if arg_dict["tab_name"].lower() == 'user':
            webelement = self.builder.find_element(ui_cmd_obj, "div.x-panel>div[id^='workflowTree']:nth-child(2)",
                                                   self.builder.constants.STRATEGY_CSS_SELECTOR)
        else:
            webelement = self.builder.find_element(ui_cmd_obj, "div.x-box-target>div[id^='workflowSystemTree']"
                                                               ":nth-child(2)",
                                                   self.builder.constants.STRATEGY_CSS_SELECTOR)

        webelement.click()

        return ui_cmd_obj

    def refresh_workflows(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "a[data-qtip='Reloads the tree']",
                                  self.builder.constants.STRATEGY_CSS_SELECTOR).click()
        # self.builder.driver.find_element_by_css_selector("a[data-qtip='Reloads the tree']").click()
        self._wait_for_loading(ui_cmd_obj, 10)

        return ui_cmd_obj

    def select_a_system_workflow(self, ui_cmd_obj, arg_dict):
        self._select_tree_node_item(ui_cmd_obj, arg_dict["workflow_name"],
                                    "div[id^='workflowSystemTree']>div>div.x-grid-item-container>table")

        return ui_cmd_obj

    def select_a_user_workflow(self, ui_cmd_obj, arg_dict):
        self._select_tree_node_item(ui_cmd_obj, arg_dict["workflow_name"],
                                    "div[id^='workflowTree']>div>div.x-grid-item-container>table")

        return ui_cmd_obj

    def invoke_context_menu_for_user_workflow(self, ui_cmd_obj, arg_dict):
        webelement = self._select_tree_node_item(ui_cmd_obj, arg_dict["treenodes"], "div[id^='workflowTree']>div>"
                                                                                    "div.x-grid-item-container>table")
        try:
            self._invoke_popup_menu_for_webelement(ui_cmd_obj, webelement)
        except Exception:
            leafnode = None
            # Split tree nodes
            items = arg_dict["treenodes"].split("|")
            # Get tree view items
            tvnodes = self.builder.driver.find_elements_by_css_selector("div[id^='workflowTree']>div>div.x-grid-item-"
                                                                        "container>table")
            count = len(tvnodes) + 1
            # Work around for handling duplicate leaf nodes
            tvnodes.reverse()
            # Select the leaf node
            for node in tvnodes:
                count -= 1
                if node.text == items[len(items) - 1]:
                    leafnode = self.builder.driver.find_element_by_css_selector(
                        "div[id^='workflowTree']>div>div.x-grid-item-container>table:nth-child(" + str(count) + ")")

            self._invoke_popup_menu_for_webelement(ui_cmd_obj, leafnode)

        return ui_cmd_obj

    def invoke_context_menu_for_system_workflow(self, ui_cmd_obj, arg_dict):
        webelement = self._select_tree_node_item(ui_cmd_obj, arg_dict["treenodes"], "div[id^='workflowSystemTree']>"
                                                                                    "div>div.x-grid-item-container>"
                                                                                    "table")
        try:
            self._invoke_popup_menu_for_webelement(ui_cmd_obj, webelement)
        except Exception:
            leafnode = None
            # Split tree nodes
            items = arg_dict["treenodes"].split("|")
            # Get tree view items
            tvnodes = self.builder.driver.find_elements_by_css_selector("div[id^='workflowSystemTree']>div>div."
                                                                        "x-grid-item-container>table")
            count = len(tvnodes) + 1
            # Work around for handling duplicate leaf nodes
            tvnodes.reverse()
            # Select the leaf node
            for node in tvnodes:
                count -= 1
                if node.text == items[len(items) - 1]:
                    leafnode = self.builder.driver.find_element_by_css_selector(
                        "div[id^='workflowSystemTree']>div>div.x-grid-item-container>table:nth-child(" + str(count) +
                        ")")

            self._invoke_popup_menu_for_webelement(ui_cmd_obj, leafnode)

        return ui_cmd_obj

    def select_humburger_menu_item(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector("div[id^='workflowTreePanel']>div>div>div>"
                                                         "a:nth-child(1)").click()
        self.builder.driver.find_element_by_link_text(arg_dict["menu_item"]).click()

        return ui_cmd_obj

    def create_workflow(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_name("name").send_keys(arg_dict["wflow_name"])
        self.builder.driver.find_element_by_css_selector("div.x-vbox-form-item>div>div>div>textarea[name="
                                                         "'description']").send_keys(
            arg_dict["wflow_description"])

        return ui_cmd_obj

    def create_workgroup(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_name("name").send_keys(arg_dict["wgroup_name"])
        self.builder.driver.find_element_by_css_selector(
            "div.x-vbox-form-item>div>div>div>textarea[name='description']").send_keys(
            arg_dict["wgroup_description"])

        return ui_cmd_obj

    def rename_workflow(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_name("name").clear()
        self.builder.driver.find_element_by_name("name").send_keys(arg_dict["wflow_name"])

        return ui_cmd_obj

    def rename_workgroup(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_name("name").clear()
        self.builder.driver.find_element_by_name("name").send_keys(arg_dict["wgroup_name"])

        return ui_cmd_obj

    def save_workflow_as(self, ui_cmd_obj, arg_dict):
        # Enter a workflow name and path.
        self.builder.driver.find_element_by_name("name").send_keys(arg_dict["wflow_name"])
        if arg_dict["wgroup_path"] is not None:
            self.builder.driver.find_element_by_name("path").send_keys(arg_dict["wgroup_path"])
        # Accept
        self._click_on_button(ui_cmd_obj, "OK")
        # Clear acknowledgement
        self._wait_for(ui_cmd_obj, 1)
        self._click_on_button(ui_cmd_obj, "OK")

        return ui_cmd_obj

    def run_workflow(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Run Workflow']").click()
        # Select a device

        return ui_cmd_obj

    def select_a_device(self, ui_cmd_obj, arg_dict):
        # Expand a All Devices node
        self.builder.driver.find_element_by_css_selector("div[id^='deviceSelectionTree']>div>div>div>div."
                                                         "x-grid-item-container>table:nth-child(2)>tbody>tr>td>div>"
                                                         "div.x-tree-expander").click()
        self._move_mouse_out_of(ui_cmd_obj, "CSS", "div[id^='deviceSelectionTree']")
        # Select a device from tree view
        self._select_tree_node_item(ui_cmd_obj, arg_dict["tree_node"], "div[id^='deviceSelectionTree']>div>div>div>"
                                                                       "div.x-grid-item-container>table")
        # Move selected device into Test Devices
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Move selected from tree to list']").click()

        return ui_cmd_obj

    def import_workflow(self, ui_cmd_obj, arg_dict):
        if self._element_exists(ui_cmd_obj, "CSS", "div[id^='multiFileWorkflowFieldPanel']>div[id^='gridview']"):
            self._wait_for(ui_cmd_obj, 3)
            self.builder.driver.find_element_by_css_selector("div[id$='filebutton']>div>span+input").click()
            self._open_file(ui_cmd_obj, arg_dict["file_name"])
        # Accept
        self._click_on_button(ui_cmd_obj, "Import")
        # Close Import Workflow dialog box
        self._click_on_button(ui_cmd_obj, "Close")
        self._wait_for(ui_cmd_obj, 2)

        return ui_cmd_obj

    def toggle_mini_map(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Toggle Mini Map']").click()
        self._wait_for(ui_cmd_obj, 2)

        return ui_cmd_obj

    def add_activity(self, ui_cmd_obj, arg_dict):
        welement = None
        if arg_dict["name"].lower() == "script":
            welement = self.builder.driver.find_element_by_css_selector("img[title='Script Activity']")
        elif arg_dict["name"].lower() == "shell":
            welement = self.builder.driver.find_element_by_css_selector("img[title='Shell Activity']")
        elif arg_dict["name"].lower() == "http":
            welement = self.builder.driver.find_element_by_css_selector("img[title='HTTP Activity']")
        elif arg_dict["name"].lower() == "mail":
            welement = self.builder.driver.find_element_by_css_selector("img[title='Mail Activity']")
        elif arg_dict["name"].lower() == "cli":
            welement = self.builder.driver.find_element_by_css_selector("img[title='CLI Activity']")
        elif arg_dict["name"].lower() == "activity group":
            welement = self.builder.driver.find_element_by_css_selector("img[title='Activity Group']")
        elif arg_dict["name"].lower() == "inclusive parallel":
            welement = self.builder.driver.find_element_by_css_selector("img[title^='Inclusive Parallel']")
        elif arg_dict["name"].lower() == "parallel":
            welement = self.builder.driver.find_element_by_css_selector("img[title^='Parallel - "
                                                                        "No Gateway conditions']")
        elif arg_dict["name"].lower() == "boundary timer":
            welement = self.builder.driver.find_element_by_css_selector("img[title='Boundary Timer']")
        elif arg_dict["name"].lower() == "signal":
            welement = self.builder.driver.find_element_by_css_selector("img[title='Signal']")
        elif arg_dict["name"].lower() == "end":
            welement = self.builder.driver.find_element_by_css_selector("img[title='End Event']")

        self._drag_and_drop_element(ui_cmd_obj, welement, arg_dict["x"], arg_dict["y"])

        return ui_cmd_obj

    def delete_activity(self, ui_cmd_obj, arg_dict):
        self._focus_activity(ui_cmd_obj, arg_dict["name"])
        self.builder.driver.find_element_by_css_selector("span[title='Delete']").click()

        return ui_cmd_obj

    def save_workflow(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Save Workflow']").click()
        # Clear Success message
        if self._element_exists(ui_cmd_obj, "CSS", "div.x-window.x-message-box"):
            self._click_on_button(ui_cmd_obj, "OK")

        return ui_cmd_obj

    def collapse_workflows_tree_panel(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector(".x-layout-split-left").click()
        self._wait_for(ui_cmd_obj, 3)

        return ui_cmd_obj

    def collapse_workflow_Details_panel(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector(".x-layout-split-right").click()
        self._wait_for(ui_cmd_obj, 3)

        return ui_cmd_obj

    def expand_workflows_tree_panel(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector(".x-tool-expand-right").click()
        self._wait_for(ui_cmd_obj, 3)

        return ui_cmd_obj

    def expand_workflow_details_panel(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector(".x-tool-expand-left").click()
        self._wait_for(ui_cmd_obj, 3)

        return ui_cmd_obj

    def verify_system_workflow_version(self, ui_cmd_obj, arg_dict):
        act_wflow_version = self._get_workflow_version(ui_cmd_obj)
        # Verify device IP is found on the grid
        if arg_dict["exp_version"] == act_wflow_version:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: " + arg_dict["exp_version"])
            self.logger.log_info("ACTUAL RESULT: " + act_wflow_version)

        return ui_cmd_obj

    def verify_workflow_control_tooltips(self, ui_cmd_obj, arg_dict):
        act_tooltips = self._get_tooltips(ui_cmd_obj, arg_dict["control_name"])
        # Verify device IP is found on the grid
        if arg_dict["exp_tooltips"] == act_tooltips:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: " + arg_dict["exp_tooltips"])
            self.logger.log_info("ACTUAL RESULT: " + act_tooltips)

        return ui_cmd_obj

    def verify_user_workflows_item_exists(self, ui_cmd_obj, arg_dict):
        obj1 = self._select_a_user_workflow(ui_cmd_obj, arg_dict["workflow_item"])
        # Verify if user workflow item exists
        if arg_dict["flag"].lower() == "true":
            if obj1 is not None:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: " + arg_dict["workflow_item"])
            self.logger.log_info("ACTUAL RESULT: None")
        else:
            if obj1 is None:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: None")
            self.logger.log_info("ACTUAL RESULT: " + arg_dict["workflow_item"])

        return ui_cmd_obj

    def verify_system_workflows_item_exists(self, ui_cmd_obj, arg_dict):
        obj1 = self._select_a_system_workflow(ui_cmd_obj, arg_dict["workflow_item"])
        # Verify if system workflow item exists
        if arg_dict["flag"].lower() == "true":
            if obj1 is not None:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: " + arg_dict["workflow_item"])
            self.logger.log_info("ACTUAL RESULT: None")
        else:
            if obj1 is None:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: None")
            self.logger.log_info("ACTUAL RESULT: " + arg_dict["workflow_item"])

        return ui_cmd_obj

    def verify_system_workflows_are_read_only(self, ui_cmd_obj, arg_dict):
        flag = "false"
        self._focus_activity(ui_cmd_obj, arg_dict["activity_name"])
        presence = self._element_exists(ui_cmd_obj, "CSS", "span[title='Delete']")
        if presence == 1:
            flag = "true"
        # Verify system workflows are read-only
        if flag == "false":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: false")
        self.logger.log_info("ACTUAL RESULT: " + flag)

        return ui_cmd_obj

    def verify_workflow_mini_map_exists(self, ui_cmd_obj, arg_dict):
        flag = "false"
        presence = self._element_exists(ui_cmd_obj, "CSS", "div.outlineContainer")
        if presence == 1:
            flag = "true"
        # Verify if mini map exists
        if arg_dict["flag"].lower() == "true":
            if flag == "true":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        else:
            if flag == "false":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + arg_dict["flag"])
        self.logger.log_info("ACTUAL RESULT: " + flag)

        return ui_cmd_obj

    def verify_workflow_tree_panel_exists(self, ui_cmd_obj, arg_dict):
        flag = "false"
        presence = self._element_exists(ui_cmd_obj, "CSS", "a[data-qtip='Reloads the tree']", 5)
        if presence == 1:
            flag = "true"
        # Verify if workflow tree panel exists
        if arg_dict["flag"].lower() == "true":
            if flag == "true":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        else:
            if flag == "false":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + arg_dict["flag"])
        self.logger.log_info("ACTUAL RESULT: " + flag)

        return ui_cmd_obj

    def verify_workflow_details_panel_exists(self, ui_cmd_obj, arg_dict):
        flag = "false"
        presence = self._element_exists(ui_cmd_obj, "NAME", "description", 5)
        if presence == 1:
            flag = "true"
        # Verify if workflow details exists
        if arg_dict["flag"].lower() == "true":
            if flag == "true":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        else:
            if flag == "false":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + arg_dict["flag"])
        self.logger.log_info("ACTUAL RESULT: " + flag)

        return ui_cmd_obj

    def verify_workflow_changes_exist(self, ui_cmd_obj, arg_dict):
        flag = "false"
        presence = self._element_exists(ui_cmd_obj, "XPATH",
                                        "//div[contains(@style, 'display')]//div[contains(text(), '" +
                                        arg_dict["activity_name"] + "')]")
        if presence == 1:
            flag = "true"
        # Verify changes exist
        if arg_dict["flag"].lower() == "true":
            if flag == "true":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        else:
            if flag == "false":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + arg_dict["flag"])
        self.logger.log_info("ACTUAL RESULT: " + flag)

        return ui_cmd_obj

    def verify_workflow_diagram_zoom_in(self, ui_cmd_obj, arg_dict):
        # Get Actual workflow diagram size (height)
        actual_size = self._get_workflow_diagram_height()
        # Zoom in the diagram
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Zoom In']").click()
        self._wait_for(ui_cmd_obj, 2)
        # Get current size after zoom in
        current_size = self._get_workflow_diagram_height()
        # Verify both the sizes
        if current_size > actual_size:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + str(current_size))
        self.logger.log_info("ACTUAL RESULT: " + str(actual_size))

        return ui_cmd_obj

    def verify_workflow_diagram_zoom_out(self, ui_cmd_obj, arg_dict):
        # Get Actual workflow diagram size (height)
        actual_size = self._get_workflow_diagram_height()
        # Zoom out the diagram
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Zoom Out']").click()
        self._wait_for(ui_cmd_obj, 2)
        # Get current size after zoom out
        current_size = self._get_workflow_diagram_height()
        # Verify both the sizes
        if current_size < actual_size:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + str(current_size))
        self.logger.log_info("ACTUAL RESULT: " + str(actual_size))

        return ui_cmd_obj

    def verify_workflow_validation_message(self, ui_cmd_obj, arg_dict):
        # Click on Verify Workflow button
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Verify Workflow']").click()
        self._wait_for_dialog_window(ui_cmd_obj, "messagebox", 5)
        # Get message
        act_message = self.builder.driver.find_element_by_css_selector("div.x-component.x-window-text.x-box-item").text
        self._click_on_button(ui_cmd_obj, "OK")
        # Verify message
        if act_message == arg_dict["message"]:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: " + arg_dict["message"])
        self.logger.log_info("ACTUAL RESULT: " + act_message)

        return ui_cmd_obj

    def _get_tooltips(self, ui_cmd_obj, control_name):
        tooltips = None
        flag = 0
        for x in ['Activity', 'Timer', 'Signal', 'Event', 'Parallel']:
            if x in control_name:
                if x == 'Parallel':
                    locator = "img[title^='" + control_name + "']"
                else:
                    locator = "img[title='" + control_name + "']"
                self._move_mouse_over_img(ui_cmd_obj, "CSS", locator)
                tooltips = self.builder.driver.find_element_by_css_selector(locator).get_attribute("Title")
                flag = 1
                break
        if flag == 0:
            locator = "a[data-qtip='" + control_name + "']"
            self._move_mouse_over_img(ui_cmd_obj, "CSS", locator)
            tooltips = self.builder.driver.find_element_by_css_selector(locator).get_attribute("data-qtip")

        return tooltips

    def _get_workflow_version(self, ui_cmd_obj):
        ver = self.builder.driver.find_element_by_css_selector("div.x-anchor-form-item:nth-child(4)>div>div").text

        return ver

    def _get_workflow_diagram_height(self):
        """Get workflow diagram height"""
        weblement = self.builder.driver.find_element_by_css_selector("div.myDiagramDiv>svg>g")
        # Get Size of the diagram
        rect_size = weblement.size

        return rect_size['height']

    def _focus_activity(self, ui_cmd_obj, name):
        """Select an activity from diagram"""
        activities = self.builder.driver.find_elements_by_tag_name("foreignObject")
        for activity in activities:
            text = activity.text
            if name in text:
                self._move_mouse_over_element(ui_cmd_obj, activity)
                break

    def _select_a_user_workflow(self, ui_cmd_obj, workflow_item):
        cmd_object = self._select_tree_node_item(ui_cmd_obj, workflow_item,
                                                 "div[id^='workflowTree']>div>div.x-grid-item-container>table")
        return cmd_object

    def _select_a_system_workflow(self, ui_cmd_obj, workflow_item):
        cmd_object = self._select_tree_node_item(ui_cmd_obj, workflow_item,
                                                 "div[id^='workflowSystemTree']>div>div.x-grid-item-container>table")
        return cmd_object
