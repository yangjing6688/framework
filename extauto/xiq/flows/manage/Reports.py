from time import sleep
from common.AutoActions import AutoActions
from common.Screen import Screen
from common.Utils import Utils
from xiq.flows.common.Navigator import Navigator
import xiq.flows.common.ToolTipCapture as tool_tip
from xiq.elements.ReportsWebElements import ReportsWebElements


class Reports(ReportsWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def get_default_network_summary_report(self, *email_list):
        """
        - Flow: Manage --> Reports
        - Default summary report will generate the reports with default options
        - Keyword Usage:
         - ``Get Default Network Summary Report  @{EMAIL_LIST}``

        :param email_list: list of the emails to send the reports
        :return: 1
        """
        self.utils.print_info("Navigate to Manage--->Reports")
        self.navigator.navigate_to_manage_reports()

        emails = ",".join(email_list)
        self.utils.print_info("Enter the emails to share with")
        self.auto_actions.send_keys(self.get_share_with_email_text_field(), emails)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on report send button")
        self.auto_actions.click(self.get_generate_report_button())
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)
        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tip_text)
        for text in tool_tip_text:
            if "Your report is generating" in text:
                self.utils.print_info(f"Tool tip text: {text}")
                return 1
        return 1
