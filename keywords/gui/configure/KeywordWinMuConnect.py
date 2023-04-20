# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper

# Keyword imports required to run keywords implemented in this file
from extauto.common.tools.remote.WinMuConnect import WinMuConnect
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class KeywordsWinMuConnect(object, metaclass=Singleton):  # Example line: Change as needed
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
        self.win_mu_connect = WinMuConnect()

    def connectivity_check(self, destination='https://www.facebook.com/', **kwargs):
        """
        - Connectivity check using curl

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsWinMuConnect.py
        -       MU1.Connectivity Check
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsWinMuConnect import KeywordsWinMuConnect
        -      Calling Keyword:
        -         keywords_win_mu_connect = KeywordsWinMuConnect()
        -         keywords_win_mu_connect.connectivity_check(destination='https://www.facebook.com/')
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
        self.keyword_utils.implementations.set_keyword_uuid("2694882f-7a6d-4ede-a4b4-e3783bccd4dc", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to do
        # connectivity check to any implementations.  We'll return 1 if there is no error raised in any of the implementations.
        return_code = ""

        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.win_mu_connect.connectivity_check(destination)
                else:
                    kwargs['fail_msg'] = f"Keyword: {keyword_name} has not been implemented for XAPI"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if connectivity check failed
        return -1 if (return_code == -1) else 1

    def connect_wpa2_ppsk_network(self, ssid, key, retry_count=5, **kwargs):
        """
        - Connect the wpa2 ppsk network
        - This keyword is used with robot remote server
        - start the remote server in windows MU
        - For starting remote server refer "cw_automation/testsuites/xiq/config/remote_server_config.txt"
        - Include below library in test suite robot file
         - ``Library	Remote 	http://${MU1_IP}:${MU1_REMOTE_PORT}   WITH NAME   MU1``

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsWinMuConnect.py
        -       MU1.Connect Wpa2 Ppsk Network   ${SSID}   ${PSK_KEY}
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsWinMuConnect import KeywordsWinMuConnect
        -      Calling Keyword:
        -         keywords_win_mu_connect = KeywordsWinMuConnect()
        -         keywords_win_mu_connect.connect_wpa2_ppsk_network(policy, ssid, key, retry_count=5)
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
        self.keyword_utils.implementations.set_keyword_uuid("0d56f52e-bc84-4747-abac-a5baa463d7b3", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to connect
        # the wpa2 ppsk network to any implementations.  We'll return 1 if there is no error raised in any of the implementations.
        return_code = ""

        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.win_mu_connect.connect_wpa2_ppsk_network(ssid, key, retry_count)
                else:
                    kwargs['fail_msg'] = f"Keyword: {keyword_name} has not been implemented for XAPI"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if connect the wpa2 ppsk network failed
        return -1 if (return_code == -1) else 1
