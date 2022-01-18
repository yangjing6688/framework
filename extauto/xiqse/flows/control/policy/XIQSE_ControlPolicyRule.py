from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.control.policy.ControlPolicyWebElements import ControlPolicyWebElements
from xiqse.elements.control.policy.ControlPolicyRuleTreeWebElements import ControlPolicyRuleTreeWebElements
from xiqse.elements.control.policy.ControlPolicyRuleDetailsWebElements import ControlPolicyRuleDetailsWebElements


class XIQSE_ControlPolicyRule(ControlPolicyRuleDetailsWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.policy_elements = ControlPolicyWebElements()
        self.rule_tree_elements = ControlPolicyRuleTreeWebElements()
