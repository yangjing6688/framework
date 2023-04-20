import re
import subprocess
from time import sleep

from ExtremeAutomation.Utilities.deprecated import deprecated


class MacMuConnect(object):
    def __init__(self):
        self.wifi_port = self.get_wi_fi_port()

    def _wi_fi_interface_on(self):
        # Enable wi-fi interface
        cmd1 = f"networksetup -setairportpower  {self.wifi_port}  ON"
        print(f"WI-Fi interface ON command:{cmd1}")
        out = self._execute_commands(cmd1)
        if "is not a Wi-Fi interface" in str(out):
            print("Please check  the Wi-Fi port")
            return False
        return True

    def _connect_to_network(self, ssid, password='', retry_count=5):
        """

        :param ssid:
        :param password:
        :param retry_count:
        :return:
        """
        if not self._wi_fi_interface_on():
            return -1

        retry_count = int(retry_count)
        while retry_count < 10:
            # Wi-Fi Connect command
            sleep(2)
            cmd2 = f"networksetup -setairportnetwork {self.wifi_port}  {ssid}  {password}"
            print(f"Connection command:{cmd2}")
            con_out = self._execute_commands(cmd2)
            print(f"Command Output: {con_out}")

            if "Failed to join" in str(con_out):
                print(f"Failed to join the network:{ssid}")
                retry_count += 1

            elif "not find network" in str(con_out):
                print(f"could not find network:{ssid}")
                retry_count += 1

            elif "Exception" in str(con_out):
                print(f"Failed with exception:{''.join(con_out)}")
                retry_count += 1

            elif "Error" in str(con_out):
                print(f"Failed with error:{' '.join(con_out)}")
                retry_count += 1

            else:
                print("Connection successful.....")
                return 1

        print(f"Not able to connect the network:{ssid}")
        return -1

    def scan_network(self, ssid):
        """
        - Scan the network
        :param ssid:
        :return:
        """
        if not self._wi_fi_interface_on():
            return False

        cmd = f"/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan | grep {ssid}"
        retry = 0
        while retry < 10:
            cmd_out = self._execute_commands(cmd)
            print("======== Network Available==================")
            print(cmd_out)
            if ssid in str(cmd_out):
                return True
            else:
                print(f"Scanning the network {ssid}... sleeping for 2 seconds")
                sleep(2)
                retry += 1

    def get_wi_fi_port(self):
        """
        - Get the Wi-Fi Interface name
        :return:
        """
        cmd = "networksetup -listallhardwareports | grep -i -A 2 Wi-Fi"
        out = self._execute_commands(cmd)
        print(f"Wi-Fi Port:{out}")
        if re.search('en0', str(out)):
            return 'en0'
        else:
            return "en1"

    def delete_wlan_profile(self, profile):
        """
        - Delete network profile
        - Keyword Usage:
         - ``MU1.Delete Wlan Profile   ${WLAN_PROFILE_NAME}``

        :param profile: profile name
        :return: 1 if deleted else None
        """
        cmd = f"networksetup -removepreferredwirelessnetwork {self.wifi_port}   {profile}"
        cmd_out = self._execute_commands(cmd)
        if "Removed" in str(cmd_out):
            print(cmd_out)
            return 1
        print(cmd_out)
        return -1

    def disconnect_wifi(self):
        cmd = f"networksetup -setairportpower  {self.wifi_port}  OFF"
        print(f"Disconnect command:{cmd}")
        return self._execute_commands(cmd)

    def get_wi_fi_interface_ip_address(self):
        """
        - Get IP Address Assigned to the Wi-Fi Interface
        - Keyword Usage:
         - ``MU1.Get Wi Fi Interface Ip Address``

        :return: wlan interface Ip Address
        """
        cmd = f"ifconfig | grep -i -A 3 {self.wifi_port}"
        print(f"Command to get Wi-Fi ip addr:{cmd}")
        cmd_out = self._execute_commands(cmd)
        ip = [value.split(" ")[-1] for value in cmd_out if "inet " in value]
        for value in cmd_out:
            print(value.strip())
        if ip:
            print("Wi-Fi Interface IP:{}".format(ip[0]))
            return ip[0]
        else:
            return -1

    def connect_open_network(self, ssid):
        """
        - Connect MU to open ssid
        - This keyword is used with robot remote server
        - start the remote server in windows MU
        - For starting remote server refer "cw_automation/testsuites/xiq/config/remote_server_config.txt"
        - Include below library in test suite robot file
         - ``Library	Remote 	http://${MU1_IP}:${MU1_REMOTE_PORT}   WITH NAME   MU1``

        - Keyword Usage:
         - ``MU1.Connect Open Network   ${SSID}``

        :param ssid: ssid name
        :return: 1 for connected else -1
        """
        self._wi_fi_interface_on()
        sleep(10)
        if not self.scan_network(ssid):
            print("SSID not available in scanned list.. please check the ssid name..")
            return -1

        return self._connect_to_network(ssid)

    @deprecated('Please use the {connect_wpa2_ppsk_network} keyword keywords/gui/configure/KeywordsMacMuConnect.py. This method can removed after 5/20/2023')
    def connect_wpa2_ppsk_network(self, ssid, key, retry_count=5):
        return self.gui_connect_wpa2_ppsk_network(ssid, key, retry_count)

    def gui_connect_wpa2_ppsk_network(self, ssid, key, retry_count=5):
        """
        - Connect the wpa2 ppsk network
        - This keyword is used with robot remote server
        - start the remote server in windows MU
        - For starting remote server refer "cw_automation/testsuites/xiq/config/remote_server_config.txt"
        - Include below library in test suite robot file
         - ``Library	Remote 	http://${MU1_IP}:${MU1_REMOTE_PORT}   WITH NAME   MU1``

        - Keyword Usage:
         - ``MU1.Connect Wpa2 Ppsk Network   ${SSID}   ${PSK_KEY}``

        :param ssid: name of the ssid to connect
        :param key: password for connection
        :param retry_count: Retry count to connect the ppsk network
        :return: 1 for connected else -1
        """

        self._wi_fi_interface_on()
        sleep(10)
        if not self.scan_network(ssid):
            print("SSID not available in scanned list.. please check the ssid name..")
            return -1

        return self._connect_to_network(ssid, key, retry_count)

    def connect_wpa2_psk_network(self, ssid, key, retry_count=5):
        """
        - Connect the wpa2 psk network
        - This keyword is used with robot remote server
        - start the remote server in windows MU
        - For starting remote server refer "cw_automation/testsuites/xiq/config/remote_server_config.txt"
        - Include below library in test suite robot file
         - ``Library	Remote 	http://${MU1_IP}:${MU1_REMOTE_PORT}   WITH NAME   MU1``

        - Keyword Usage:
         - ``MU1.Connect Wpa2 Psk Network   ${SSID}   ${PSK_KEY}``

        :param ssid: name of the ssid to connect
        :param key: password for connection
        :param retry_count: Retry count to connect the ppsk network
        :return: 1 for connected else -1
        """
        self._wi_fi_interface_on()
        sleep(10)
        if not self.scan_network(ssid):
            print("SSID not available in scanned list.. please check the ssid name..")
            return -1

        return self._connect_to_network(ssid, key, retry_count)

    def connect_enterprise_network(self, ssid):
        """
        - Assuming that profile is already created for the network with stored user name and password
        - This keyword is used with robot remote server
        - start the remote server in windows MU
        - For starting remote server refer "cw_automation/testsuites/xiq/config/remote_server_config.txt"
        - Include below library in test suite robot file
         - ``Library	Remote 	http://${MU1_IP}:${MU1_REMOTE_PORT}   WITH NAME   MU1``

        - Keyword Usage:
         - ``MU1.Connect Enterprise Network   ${SSID}``

        :param ssid: name of the ssid to connect
        :return: 1 for connected else -1
        """
        self._wi_fi_interface_on()
        sleep(10)
        if not self.scan_network(ssid):
            print("SSID not available in scanned list.. please check the ssid name..")
            return -1

        return self._connect_to_network(ssid)

    @deprecated('Please use the {connectivity_check} keyword keywords/gui/configure/KeywordsMacMuConnect.py. This method can removed after 5/20/2023')
    def connectivity_check(self, destination='https://www.facebook.com/'):
        return self.gui_connectivity_check(destination)

    def gui_connectivity_check(self, destination='https://www.facebook.com/'):
        """
        - Connectivity check using curl
        - Keyword Usage:
         - ``MU1.Connectivity Check``

        :param destination: destination url
        :return: 1 if internet access available else -1
        """
        cmd = 'curl -I ' + destination
        curl_out = self._execute_commands(cmd)
        for line in curl_out:
            if re.search(r'HTTP/\d+ 200', line):
                print(line)
                return 1
            if re.search(r'Failed to connect to', line):
                print(line)
                return -1
            print(line)
        return -1

    def verify_internet_connectivity(self):
        """
        - Verify MU machine Internet connectivity with curl and Firefox detect portal
        - Keyword Usage:
        - ``MU1.Verify Internet Connectivity``

        :return: 1 if Internet is available, else -1
        """
        cmd = 'curl http://detectportal.firefox.com/success.txt'
        curl_out = self._execute_commands(cmd)
        if (len(curl_out) == 1) and re.fullmatch('success', curl_out[0]):
            return 1
        else:
            return -1

    def ping_check(self, destination):
        """
        - Ping the destination address
        - Keyword Usage:
         - ``Ping Check   ${DESTINATION}``
         - ``Ping Check  www.google.com``

        :param destination: destination address ex www.google.com
        :return: 1 if ping success else -1
        """
        cmd = 'ping ' + str(destination) + ' -c 3'
        retry = 0
        while retry < 3:
            ping_out = self._execute_commands(cmd)
            for line in ping_out:
                print(line)
                if "Packets: Sent = 3, Received = 3, Lost = 0 (0% loss)" in line:
                    return 1
            retry += 1
        return -1

    def ping_check_in_background(self, destination='www.google.com', count='4'):
        """
        - Ping the destination address
        - Keyword Usage:
         - ``Ping Check in Background   ${DESTINATION}    50``
         - ``Ping Check in Background   www.google.com    5``

        :param destination: destination address ex www.google.com
        :param count: no of pings
        :return: 1 if ping success else -1
        """
        cmd = 'ping ' + str(destination) + ' -c ' + str(count)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, start_new_session=False)

    def kill_native_captive(self):
        """
        :send killall 'Captive Network Assistant'
        """
        cmd1 = "killall -HUP mDNSResponder"
        cmd2 = "killall 'Captive Network Assistant'"
        out1 = self._execute_commands(cmd1)
        out2 = self._execute_commands(cmd2)
        sleep(2)
        out2 = self._execute_commands(cmd2)
        print(f"{out1}\n{out2}")

    @staticmethod
    def _execute_commands(cmd):
        """
        Execute command on windows command line using subprocess module
        :param cmd: command to execute
        :return: cmd_out of the command
        """
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_out = []
        for line in process.stdout:
            cmd_out.append(line.decode().strip())
        return cmd_out


if __name__ == "__main__":
    obj = MacMuConnect()
