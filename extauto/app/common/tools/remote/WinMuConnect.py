import subprocess
from time import sleep
import xml.etree.ElementTree as ET
import re


def update_wlan_profile(profile, ssid=None, key=None):
    """
    Update the profile xml file dynamically based on ssid, auth type and key
    :param profile: name of the profile file ie xml file
    :param ssid: name of the ssid to update in profile file
    :param key: key to be update
    :return:
    """
    name_index = -1
    ssid_config_index = -1
    msm_index = -1

    file = "C:\\extauto\\common\\tools\\remote\\wlanprofiles\\" + profile
    file_org = "C:\\extauto\\common\\tools\\remote\\wlanprofiles\\ORG_" + profile
    tree = ET.parse(file_org)
    root = tree.getroot()

    # get the sub tag index respect to the root tag
    for x, i in enumerate(root):
        if "name" in i.tag:
            name_index = x
        elif "SSIDConfig" in i.tag:
            ssid_config_index = x
        elif "MSM" in i.tag:
            msm_index = x

    # update the profile name
    root[name_index].text = ssid

    # update the ssid name and its corresponding hex value
    for x in root[ssid_config_index]:
        for subtag in x:
            if "hex" in subtag.tag:
                subtag.text = ssid.encode('utf-8').hex()
            elif "name" in subtag.tag:
                subtag.text = ssid

    # update the ke value
    for x in root[msm_index]:
        for subtag in x:
            if "sharedKey" in subtag.tag:
                for el in subtag:
                    if "keyMaterial" in el.tag:
                        el.text = key

    # write changes to the file
    tree.write(file, default_namespace='xmlns')


class WinMuConnect(object):
    def __init__(self):
        pass

    def _connect_to_network(self, profile):
        """
        Connect the wlan network
        :param profile:
        :return:
        """
        retry_count = 0
        while retry_count < 3:
            cmd = "netsh wlan connect name=" + profile
            out = self.execute_commands(cmd)
            sleep(10)
            print("".join(out))
            if "Connection request was completed successfully." in out:
                print("Check wi-fi connection")
                cmd = 'netsh interface show interface  | findstr Wi-Fi'
                cmd_out = self.execute_commands(cmd)
                print("".join(cmd_out))
                if "Connected" in "".join(cmd_out):
                    return 1
                retry_count += 1
        return -1

    def connect_open_network(self, ssid):
        """
        Connect open ssid
        :param ssid:
        :return:
        """
        # Update the profile file
        update_wlan_profile('Open_Auth.xml', ssid)

        if not self.search_network(ssid):
            return "SSID Not available in scanned list"

        if self.get_network_profile(ssid):
            self.delete_wlan_profile(ssid)

        self.add_wlan_profile('Open_Auth.xml')

        sleep(2)
        return self._connect_to_network(ssid)

    def connect_wpa2_psk_network(self, ssid, key):
        """
        Connect the wpa2 psk network
        :param ssid: name of the ssid to connect
        :param key: password for connection
        :return: status of connection
        """
        # Update the profile file
        update_wlan_profile('WPA2_PSK_AES.xml', ssid, key)

        if not self.search_network(ssid):
            return "SSID Not available in scanned list"

        if self.get_network_profile(ssid):
            self.delete_wlan_profile(ssid)

        self.add_wlan_profile('WPA2_PSK_AES.xml')

        sleep(2)
        return self._connect_to_network(ssid)

    def connect_wpa3_psk_network(self, ssid, key):
        """
        Connect the wpa3 psk network
        :param ssid: name of the ssid to connect
        :param key: password for connection
        :return: status of connection
        """
        # Update the profile file
        update_wlan_profile('WPA3_PSK_AES.xml', ssid, key)

        if not self.search_network(ssid):
            return "SSID Not available in scanned list"

        if self.get_network_profile(ssid):
            self.delete_wlan_profile(ssid)

        self.add_wlan_profile('WPA3_PSK_AES.xml')

        sleep(2)
        return self._connect_to_network(ssid)

    def connect_wpa2_ppsk_network(self, ssid, key):
        """
        Connect the wpa2 ppsk network
        :param ssid: name of the ssid to connect
        :param key: password for connection
        :return: status of connection
        """
        # Update the profile file
        update_wlan_profile('WPA2_PPSK_AES.xml', ssid, key)

        if not self.search_network(ssid):
            return "SSID Not available in scanned list"

        if self.get_network_profile(ssid):
            self.delete_wlan_profile(ssid)

        self.add_wlan_profile('WPA2_PPSK_AES.xml')

        sleep(2)
        return self._connect_to_network(ssid)

    def connect_enterprise_network(self, ssid):
        """
        Assuming that profile is already created for enterprise network with stored user name and password
        :param ssid:
        :return:
        """
        if not self.search_network(ssid):
            return "SSID Not available in scanned list"

        return self._connect_to_network(ssid)

    def disconnect_wifi(self):
        """
        Disconnect to the wlan network
        :return:
        """
        cmd = "netsh wlan disconnect"
        cmd_out = self.execute_commands(cmd)
        print("=========== Disconnection Status ===========")
        print(''.join(cmd_out))
        for out in cmd_out:
            if "Disconnection request was completed successfully for interface" in out:
                return 1
        return -1

    def add_wlan_profile(self, profile_xml):
        """
        Adding wlan profile
        :param profile_xml: Name of the profile xml file to add
        :return:
        """
        cmd = 'netsh wlan add profile filename="C:\\extauto\\common\\tools\\remote\\wlanprofiles\\' + profile_xml + '" interface=Wi-Fi'
        cmd_out = self.execute_commands(cmd)
        print("============= Add wlan Profile =============")
        print("".join(cmd_out))
        for value in cmd_out:
            if "is added on interface Wi-Fi" in value:
                return 1

    def search_network(self, ssid):
        """
        Search the network in available networks
        :param ssid:
        :return:
        """
        cmd = "netsh wlan show networks  | findstr " + ssid

        retry = 0
        while retry < 30:
            cmd_out = self.execute_commands(cmd)
            print("======== Network Available==================")
            print(cmd)
            print("".join(cmd_out))
            if ssid in "".join(cmd_out):
                return 1

            if retry > 3:
                self.refresh_wi_fi_interface()
                retry += 1
            else:
                sleep(10)
                retry += 1

    def refresh_wi_fi_interface(self):
        """
        Enable and disable wi-fi intercae
        :return:
        """
        dis_cmd = 'netsh interface set interface name="Wi-Fi" admin=disabled'
        en_cmd = 'netsh interface set interface name="Wi-Fi" admin=enabled'

        self.execute_commands(dis_cmd)
        sleep(30)
        self.execute_commands(en_cmd)
        sleep(30)
        cmd = 'netsh interface show interface  | findstr Wi-Fi'
        cmd_out = self.execute_commands(cmd)
        print("".join(cmd_out))
        if "Enabled" in "".join(cmd_out):
            return 1

    def get_network_profile(self, profile):
        """
        Get wlan network profile
        :return: 1 if profile exists else none
        """
        cmd = "netsh wlan show profile"
        cmd_out = self.execute_commands(cmd)
        for value in cmd_out:
            if profile in value:
                print(value)
                return 1

    def delete_wlan_profile(self, profile):
        """
        delete network profile
        :param profile:
        :return:
        """
        cmd = "netsh wlan delete profile name=" + profile
        cmd_out = self.execute_commands(cmd)
        for value in cmd_out:
            if "is deleted from interface " in value:
                print("Profile: {} deleted successfully".format(profile))
                return 1

    def get_wi_fi_interface_ip_address(self):
        """
        Get IP Address Assigned to the Wi-Fi Interface
        :return:
        """
        cmd = 'netsh interface ip show addresses "Wi-Fi"'
        cmd_out = self.execute_commands(cmd)
        ip = [value.split(" ")[-1] for value in cmd_out if "IP Address:" in value]
        for value in cmd_out:
            print(value.strip())
        if ip:
            print("Wi-Fi Interface IP:{}".format(ip[0]))
            return ip[0]
        else:
            return -1

    def connectivity_check(self, destination='https://www.facebook.com/'):
        """
        Connectivity check using curl
        :param destination:
        :return:
        """
        cmd = 'curl -I ' + destination
        curl_out = self.execute_commands(cmd)
        for line in curl_out:
            if re.search(r'HTTP/\d+\.\d+ 200', line):
                print(line)
                return 1
            if re.search(r'Failed to connect to', line):
                print(line)
                return -1
            print(line)
        return -1

    def ping_check(self, destination):
        """
        Ping the destination address
        :param destination: destination address ex www.google.com
        :return:
        """
        cmd = 'ping ' + str(destination) + ' -n 3'
        retry = 0
        while retry < 3:
            ping_out = self.execute_commands(cmd)
            for line in ping_out:
                print(line)
                if "Packets: Sent = 3, Received = 3, Lost = 0 (0% loss)" in line:
                    return 1
            retry += 1
        return -1

    @staticmethod
    def execute_commands(cmd):
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
    obj = WinMuConnect()
    output = obj.connect_wpa2_psk_network("PPSK_HS_DEMO3", 'WLsaqgLUJt')
    print(output)
    obj.disconnect_wifi()
