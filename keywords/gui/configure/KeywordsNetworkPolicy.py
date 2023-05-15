# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

# Keyword imports required to run keywords implemented in this file
from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy


class KeywordsNetworkPolicy(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        # Object used to run keywords implemented in this file
        self.network_policy = NetworkPolicy()

    def create_network_policy(self, policy, wireless_profile, cli_type='AH-AP', **kwargs):
        """
        - Create the network policy from CONFIGURE-->NETWORK POLICIES
        - This keyword will create the network policy and wireless network
        - Wireless network includes open, ppsk, psk and enterprise network
        - Example:
        - ``Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}``
        - ``Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}     ${CLI_TYPE}``
        - ${POLICY_NAME} --> Name of the network policy to create
        - ${WIRELESS_NW_PROFILE} --> This is dictionary, include all key value pair to create wireless network
        - For Creating  ${WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot
        - ${CLI_TYPE} --> Device type of the DUT. Default is 'AH-AP'.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsNetworkPolicy.py
        -      Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}
        -      Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}     ${CLI_TYPE}
        -      ${POLICY_NAME} --> Name of the network policy to create
        -      ${WIRELESS_NW_PROFILE} --> This is dictionary, include all key value pair to create wireless network
        -      For Creating  ${WIRELESS_NW_PROFILE} dict refer wireless_network_config.robot
        -      ${CLI_TYPE} --> Device type of the DUT. Default is 'AH-AP'.
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsNetworkPolicy import KeywordsNetworkPolicy
        -      Calling Keyword:
        -         keywords_network_policy = KeywordsNetworkPolicy()
        -         keywords_network_policy.create_network_policy(policy, wireless_profile, cli_type='AH-AP')
        -
        - Keyword Implementations:
        -    GUI

        Supported Modes:
            GUI  - default mode
            XAPI - not implemented

        :param policy: Name of the network policy to create
        :param wireless_profile: (dict) wireless network creation profile parameters
        :param cli_type: Device type of the DUT. Default is 'AH-AP'.
        :return: 1 if network policy creation is success
        """

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("8161d55f-4dca-4ab0-bd73-a01e41d4da42", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to
        # create network policy to any implementations.  We'll return 1 if there is no error raised in
        # any of the implementations.
        return_code = -1

        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.network_policy.create_network_policy(policy, wireless_profile, cli_type, **kwargs)
                else:
                    kwargs['fail_msg'] = f"Keyword: {keyword_name} has not been implemented for XAPI"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if any of the create user group failed
        return return_code