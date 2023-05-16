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
        Create the network policy from CONFIGURE-->NETWORK POLICIES
        This keyword will create the network policy and wireless network
        Wireless network includes open, ppsk, psk and enterprise network
        Example:
        Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}     ${CLI_TYPE}
        ${POLICY_NAME} --> Name of the network policy to create
        ${CLI_TYPE} --> Device type of the DUT. Default is 'AH-AP'.

        Each of the remaining parameters as dictionaries are exemplified in turn under below sections

        Example of valid network profile:
        &{WIRELESS_NW_PROFILE}=    ssid_name=SSID_01         network_type=standard    ssid_profile=&{SSID_PROFILE}   auth_profile=&{AUTH_PROFILE}
        ssid_name --> The name of the SSID to be created
        network_type --> Describes the type of network. Values can be "standard" or left unspecified
        ssid_profile --> This is a dictionary used to specify the SSID profile parameters
        auth_profile --> This is a dictionary used to specify the authentication profile parameters

        Example of a valid SSID profile:
        &{SSID_PROFILE}=            WIFI0=Disable       WIFI1=Enable
        WIFI0 --> Specify to enable or disable the WIFI0 interface
        WIFI1 --> Specify to enable or disable the WIFI1 interface

        Example of a valid authentication profile:
        &{AUTH_PROFILE}     auth_type=Open    cwp_profile=&{CWP_Profile}
        auth_type --> Specify the type of authentication. Valid values are: open, psk, ppsk, enhanced or enterprise
        cwp_profile --> This is a dictionary used to specify the CWP profile

        Example of a valid CWP profile:
        &{CWP_Profile}      enable_cwp=Enable   cloud_captive_web_portal=Enable  social_login=Enable   request_pin=Disable   open_cwp_config=&{OPEN_CWP_CONFIG}
        enable_cwp --> Specify to enable or disable CWP
        cloud_captive_web_portal --> Specify to enable or disable Cloud Captive Web Portal
        social_login --> Specify to enable or disable social login
        request_pin --> Specify to enable or disable request pin
        open_cwp_config --> This is a dictionary used to specify the Open CWP Configuration settings

        Example of a valid Open CWP Configuration:
        &{OPEN_CWP_CONFIG}=     social_cwp_config=&{SOCIAL_CWP_CONFIG}    cloud_cwp_name=cloudcwpsocialfacebook
        social_cwp_config --> This is a dictionary used to specify the Social CWP Configuration settings
        cloud_cwp_name --> Specify the Cloud CWP name

        Example of a valid Social CWP Configuration:
        &{SOCIAL_CWP_CONFIG}=    social_login_type=Facebook   restrict_access=default    auth_cache_duration=2
        social_login_type --> Specify the social login type. Values can be one of Facebook, Google, Linkedin
        restrict_access --> Specify the restrict access to domains. Values can be default or arbitrary
        auth_cache_duration --> Specify the authentication cache duration. Values can be "default" or arbitrary

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsNetworkPolicy.py
        -      Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}
        -      Create Network Policy   ${POLICY_NAME}   ${WIRELESS_NW_PROFILE}     ${CLI_TYPE}
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

        # Return an error if create network policy failed
        return return_code