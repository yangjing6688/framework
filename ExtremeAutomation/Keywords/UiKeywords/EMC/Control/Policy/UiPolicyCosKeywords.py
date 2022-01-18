from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.PolicycosConstants import PolicycosConstants


class UiPolicyCosKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiPolicyCosKeywords, self).__init__()
        self.api_const = self.constants.API_POLICY_COS
        self.cmd = PolicycosConstants()

    def policy_cos_select_cos_node(self, element_name, tree_node, **kwargs):
        """Returns the result of policy_cos_select_cos_node."""
        args = {"tree-node": tree_node}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_SELECT_COS_NODE, **kwargs)

    def policy_click_tree_panel(self, element_name, tree_name, **kwargs):
        """Returns the result of policy_click_tree_panel."""
        args = {"tree_name": tree_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_CLICK_TREE_PANEL, **kwargs)

    def policy_cos_create(self, element_name, cos_name, **kwargs):
        """Returns the result of policy_cos_create."""
        args = {"cos_name": cos_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_CREATE, **kwargs)

    def policy_cos_create_rate_limit(self, element_name, speed, rate, **kwargs):
        """Returns the result of policy_cos_create_rate_limit."""
        args = {"rate": rate,
                "speed": speed}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_CREATE_RATE_LIMIT, **kwargs)

    def policy_cos_set_irl_index(self, element_name, index, **kwargs):
        """Returns the result of policy_cos_set_irl_index."""
        args = {"index": index}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_SET_IRL_INDEX, **kwargs)

    def policy_cos_delete_cos(self, element_name, cos_name, **kwargs):
        """Returns the result of policy_cos_delete_cos."""
        args = {"cos_name": cos_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_DELETE_COS, **kwargs)

    def policy_cos_delete_rate_limit(self, element_name, rate_limit, **kwargs):
        """Returns the result of policy_cos_delete_rate_limit."""
        args = {"rate_limit": rate_limit}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_DELETE_RATE_LIMIT, **kwargs)

    def policy_cos_edit_txq_index(self, element_name, index, **kwargs):
        """Returns the result of policy_cos_edit_txq_index."""
        args = {"index": index}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_EDIT_TXQ_INDEX, **kwargs)

    def policy_cos_edit_tos(self, element_name, tos_value, **kwargs):
        """Returns the result of policy_cos_edit_tos."""
        args = {"tos_value": tos_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_EDIT_TOS, **kwargs)

    def policy_cos_enable_tos(self, element_name, **kwargs):
        """Returns the result of policy_cos_enable_tos."""
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_COS_ENABLE_TOS, **kwargs)

    def policy_cos_edit_tos_hex_value(self, element_name, tos_value, **kwargs):
        """Returns the result of policy_cos_edit_tos_hex_value."""
        args = {"tos_value": tos_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_EDIT_TOS_HEX_VALUE, **kwargs)

    def policy_cos_set_orl_index(self, element_name, index, **kwargs):
        """Returns the result of policy_cos_set_orl_index."""
        args = {"index": index}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_COS_SET_ORL_INDEX, **kwargs)
