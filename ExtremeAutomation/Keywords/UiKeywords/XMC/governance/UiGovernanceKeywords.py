from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XMC.GovernanceConstants import GovernanceConstants


class UiGovernanceKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGovernanceKeywords, self).__init__()
        self.api_const = self.constants.API_XMC_GOVERNANCE
        self.command_const = GovernanceConstants()

    def add_regime(self, element_name, regime_name, regime_desc, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name
        [regime_name]           - Regime description

        Add a new regime
        """
        args = {"regime_name": regime_name,
                "regime_desc": regime_desc
                }

        return self.execute_keyword(element_name, args, self.command_const.ADD_REGIME, **kwargs)

    def enter_regime_details(self, element_name, regime_name, regime_desc, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name
        [regime_name]           - Regime description

        Enter regime details such as name and description
        """
        args = {"regime_name": regime_name,
                "regime_desc": regime_desc
                }

        return self.execute_keyword(element_name, args, self.command_const.ENTER_REGIME_DETAILS, **kwargs)

    def select_regime(self, element_name, regime_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name

        Select a regime
        """
        args = {"regime_name": regime_name}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_REGIME, **kwargs)

    def run_regime(self, element_name, regime_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name

        Run a regime
        """
        args = {"regime_name": regime_name}

        return self.execute_keyword(element_name, args, self.command_const.RUN_REGIME, **kwargs)

    def edit_regime(self, element_name, regime_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name

        Edit a regime
        """
        args = {"regime_name": regime_name}

        return self.execute_keyword(element_name, args, self.command_const.EDIT_REGIME, **kwargs)

    def delete_regime(self, element_name, regime_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name

        Delete a regime
        """
        args = {"regime_name": regime_name}

        return self.execute_keyword(element_name, args, self.command_const.DELETE_REGIME, **kwargs)

    def select_and_move_single_device(self, element_name, tree_node, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [tree_node]             - Device IP with its naviagation path

        Select a device for running a Regime on it
        """
        args = {"tree_node": tree_node}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_AND_MOVE_SINGLE_DEVICE, **kwargs)

    def verify_regime_exists(self, element_name, regime_name, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify a regime exists or not
        """
        args = {"regime_name": regime_name,
                "flag": flag
                }

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_REGIME_EXISTS, **kwargs)

    def verify_system_regime_is_non_editable(self, element_name, regime_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name

        Verify system regime is non editable
        """
        args = {"regime_name": regime_name}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_SYSTEM_REGIME_IS_NON_EDITABLE,
                                    **kwargs)

    def verify_system_regime_is_non_removable(self, element_name, regime_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [regime_name]           - Regime name

        Verify system regime is non removable
        """
        args = {"regime_name": regime_name}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_SYSTEM_REGIME_IS_NON_REMOVABLE,
                                    **kwargs)
