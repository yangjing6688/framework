# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

# Keyword imports required to run keywords implemented in this file
from extauto.common.tools.remote.MacMuConnect import MacMuConnect


class KeywordsMacMuConnect(object, metaclass=Singleton):
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
        self.mac_mu_connect = MacMuConnect()

    def connectivity_check(self, destination='https://www.facebook.com/', **kwargs):
        """
        Connectivity check using curl

        This keyword uses curl to check the connectivity of the network of the Mobile Unit (MU).
        The method checks to see if the MU can connect to the specified destination internet address by only fetching headers.
        If the curl command's result contains a successful status then the connection is considered good.
        This keyword runs on a remote device (Mobile Unit). To connect to the MU use a keyword like:
        Library Remote http://${mu1.ip}:${mu1.port} WITH NAME mu1

        Then refer to the named device when running the keyword. For example:
        ${RESULT}=   MU1.Connectivity Check

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsMacMuConnect.py
        -      MU1.Connectivity Check
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsMacMuConnect import KeywordsMacMuConnect
        -      Calling Keyword:
        -         keywords_mac_mu_connect = KeywordsMacMuConnect()
        -         keywords_mac_mu_connect.connectivity_check(destination='https://www.facebook.com/')
        -
        - Keyword Implementations:
        -   This does not access a WebApplication and therefore does not have a GUI or XAPI implementation
        :param destination: destination url
        :return: 1 if internet access available else -1
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("6597f13f-9386-4bbd-9bc0-d5e4331b9e0a", keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to
        # do connectivity check to any implementations.  We'll return 1 if there is no error raised in
        # any of the implementations.
        return_code = -1

        try:
            self.keyword_utils.timing.start(keyword_name, 'GUI')
            return_code = self.mac_mu_connect.connectivity_check(destination)
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
        This keyword runs on a remote device (Mobile Unit). To connect to the MU use a keyword like:
        Library Remote http://${mu1.ip}:${mu1.port} WITH NAME mu1

        Then refer to the named device when running the keyword. For example:
        ${RESULT}=   MU1.Connect Wpa2 Ppsk Network   SSID_01   Passw0rd

         Keyword Usage:
           Robot:
              Library  keywords/gui/configure/KeywordsMacMuConnect.py
              MU1.Connect Wpa2 Ppsk Network   ${SSID}   ${PSK_KEY}
           Pytest:
              Imports:
                 from keywords.gui.configure.KeywordsMacMuConnect import KeywordsMacMuConnect
              Calling Keyword:
                 keywords_mac_mu_connect = KeywordsMacMuConnect()
                 keywords_mac_mu_connect.connect_wpa2_ppsk_network(ssid, key, retry_count=5)

         Keyword Implementations:
           This does not access a WebApplication and therefore does not have a GUI or XAPI implementation

        :param ssid: name of the ssid to connect
        :param key: password for connection
        :param retry_count: Retry count to connect the ppsk network
        :return: 1 for connected else -1
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("8161d55f-4dca-4ab0-bd73-a01e41d4da42", keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to
        # connect the wpa2 ppsk network to any implementations.  We'll return 1 if there is no error raised in
        # any of the implementations.
        return_code = -1

        try:
            self.keyword_utils.timing.start(keyword_name, 'GUI')
            return_code = self.mac_mu_connect.connect_wpa2_ppsk_network(ssid, key, retry_count)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if connect the wpa2 ppsk network failed
        return return_code