# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper

# Keyword imports required to run keywords implemented in this file
from extauto.common.tools.remote.MacMuConnect import MacMuConnect
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class KeywordsMacMuConnect(object, metaclass=Singleton):  # Example line: Change as needed
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if not hasattr(self, 'initialized'):
            return
        self.initialized = True

        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        # Object used to run keywords implemented in this file
        self.mac_mu_connect = MacMuConnect()

    def connectivity_check(self, destination='https://www.facebook.com/', **kwargs):
        """
        Connectivity check using curl

        This keyword uses curl to check the connectivity of the network of the Mobile Unit (MU).
        The method checks to see if the MU can connect to the specified destination internet address by only fetching headers.
        If the curl command's result contains a successful status then the connection is considered good.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsMacMuConnect.py
        -       MU1.Connectivity Check
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsMacMuConnect import KeywordsMacMuConnect
        -      Calling Keyword:
        -         keywords_mac_mu_connect = KeywordsMacMuConnect()
        -         keywords_mac_mu_connect.connectivity_check(destination='https://www.facebook.com/')
        -
        - Keyword Implementations:
        -    GUI

        Supported Modes:
            GUI  - default mode
            XAPI - not implemented

        :param destination: destination url
        :return: 1 if internet access available else -1
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("6597f13f-9386-4bbd-9bc0-d5e4331b9e0a", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to do
        # connectivity check to any implementations.  We'll return 1 if there is no error raised in any of the implementations.
        return_code = -1

        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.mac_mu_connect.connectivity_check(destination)
                else:
                    kwargs['fail_msg'] = f"Keyword: {keyword_name} has not been implemented for XAPI"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if connectivity check failed
        return return_code

    def connect_wpa2_ppsk_network(self, ssid, key, retry_count=5, **kwargs):
        """
        Connect the wpa2 ppsk network

        This keyword instructs the Mobile Unit (MU) to connect to wpa2 ppsk network.
        The method checks for the MU's interface to be in available state, waits for the network to be reachable by the MU,
        then attempts to connect the MU successfully to the network for the specified amount of retries.
        If the MU's connection is made without any issues then the connection is considered good.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsMacMuConnect.py
        -       MU1.Connect Wpa2 Ppsk Network   ${SSID}   ${PSK_KEY}
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsMacMuConnect import KeywordsMacMuConnect
        -      Calling Keyword:
        -         keywords_mac_mu_connect = KeywordsMacMuConnect()
        -         keywords_mac_mu_connect.connect_wpa2_ppsk_network(policy, ssid, key, retry_count=5)
        -
        - Keyword Implementations:
        -    GUI

        Supported Modes:
            GUI  - default mode
            XAPI - not implemented

        :param ssid: name of the ssid to connect
        :param key: password for connection
        :param retry_count: Retry count to connect the ppsk network
        :return: 1 for connected else -1
        """

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("8161d55f-4dca-4ab0-bd73-a01e41d4da42", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to connect
        # the wpa2 ppsk network to any implementations.  We'll return 1 if there is no error raised in any of the implementations.
        return_code = -1

        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.mac_mu_connect.connect_wpa2_ppsk_network(ssid, key, retry_count)
                else:
                    kwargs['fail_msg'] = f"Keyword: {keyword_name} has not been implemented for XAPI"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if connect the wpa2 ppsk network failed
        return return_code
