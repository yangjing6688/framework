import re
import time
import pexpect
from extauto.common.Cli import Cli
from extauto.common.Utils import Utils

class Mu:
    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()

    def associate_mu(self, mu_spawn, interface, ssid_name, ip_address="default", retries=3):
        """

        :param mu_spawn:
        :param interface:
        :param ssid_name:
        :param ip_address:
        :param retries:
        :return:
        """
        retry_count = 1
        while retry_count <= retries:
            self.utils.print_info("Associating MU - Loop : ", retry_count)
            self.cli.send(mu_spawn, "rm -rf /tmp.txt")
            time.sleep(10)
            self.cli.send(mu_spawn, "pkill dhclient")
            self.cli.send(mu_spawn, "pkill wpa_supplicant")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + interface + " down")
            self.cli.send(mu_spawn, " ifconfig " + interface + " up ")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + interface)
            self.cli.send(mu_spawn, "iwconfig " + interface)
            time.sleep(10)
            self.cli.send(mu_spawn, " iwconfig " + interface + " essid " + ssid_name)
            # self.cli.send(mu_spawn, " ifconfig " + interface + " up ")
            time.sleep(2)

        self.cli.send(mu_spawn, " iw dev " + interface + " connect " + ssid_name)
        time.sleep(2)

        self.cli.send(mu_spawn, "iwconfig " + interface)

        if ip_address == "default":
            self.cli.send(mu_spawn, " dhclient " + interface + " -v -r ")
            time.sleep(10)
            output = self.cli.send(mu_spawn, " iwconfig " + interface)
            if "Link Quality" in output:
                output = self.cli.send(mu_spawn, " dhclient " + interface + " -v ")
                time.sleep(5)
                if "bound to " in output:
                    self.cli.send(mu_spawn, "ifconfig " + interface)
                    self.utils.print_info("MU got IP Address")
                    return 1
            retry_count += 1
        else:
            return 1

        self.utils.print_info("Unable to associate MU to AP")
        return 0

    def associate_mu_to_ethport(self, mu_spawn, wlan_port, eth_port, ip_address="default", retries=3):
        """

        :param mu_spawn:
        :param interface:
        :param ssid_name:
        :param ip_address:
        :param retries:
        :return:
        """
        retry_count = 1
        while retry_count <= retries:
            self.utils.print_info("Associating MU - Loop : ", retry_count)
            self.cli.send(mu_spawn, "rm -rf /tmp.txt")
            time.sleep(10)
            self.cli.send(mu_spawn, "pkill dhclient")
            self.cli.send(mu_spawn, "pkill wpa_supplicant")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + wlan_port + " down")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + eth_port + " down")
            self.cli.send(mu_spawn, " ifconfig " + eth_port + " up ")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + eth_port)
            time.sleep(5)

            self.cli.send(mu_spawn, "iwconfig " + eth_port)

            if ip_address == "default":
                self.cli.send(mu_spawn, " dhclient " + eth_port + " -v -r ")
                time.sleep(10)
                self.cli.send(mu_spawn, " dhclient " + eth_port + " -v ")
                time.sleep(10)
                self.utils.print_info("Got DHCP Address")
                self.utils.print_info("Checking the Internet reachability...")
                if self.cli.ping_from_spawn(mu_spawn, "google.com"):
                    self.cli.send(mu_spawn, "ifconfig " + eth_port + " down")
                    return 1
                retry_count += 1
        self.cli.send(mu_spawn, "ifconfig " + eth_port + " down")
        self.utils.print_info("Unable to associate MU to AP")
        return 0

    def get_testip_mu1(self, wlan_port, eth_port, ip_address="default", retries=3):
        """

        :param mu_spawn:
        :param interface:
        :param ssid_name:
        :param ip_address:
        :param retries:
        :return:
        """

        ip = self.utils.get_config_value("MU1_IP")
        port = self.utils.get_config_value("MU1_PORT")
        username = self.utils.get_config_value("MU1_USERNAME")
        password = self.utils.get_config_value("MU1_PASSWORD")
        platform = self.utils.get_config_value("MU1_PLATFORM")
        interface = self.utils.get_config_value("MU1_INTERFACE")

        self.utils.print_info("MU IP         : ", ip)
        self.utils.print_info("MU Port       : ", port)
        self.utils.print_info("MU Username   : ", username)
        self.utils.print_info("MU Password   : ", password)
        self.utils.print_info("MU Platform   : ", platform)
        self.utils.print_info("MU Interface  : ", interface)

        mu_spawn = self.cli.open_spawn(ip, port, username, password, platform)

        expect_str = "CTRL-EVENT-CONNECTED"

        retry_count = 1
        while retry_count <= retries:
            self.utils.print_info("Associating MU - Loop : ", retry_count)
            self.cli.send(mu_spawn, "rm -rf /tmp.txt")
            time.sleep(10)
            self.cli.send(mu_spawn, "pkill dhclient")
            self.cli.send(mu_spawn, "pkill wpa_supplicant")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + wlan_port + " down")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + eth_port + " down")
            self.cli.send(mu_spawn, " ifconfig " + eth_port + " up ")
            time.sleep(2)
            self.cli.send(mu_spawn, "ifconfig " + eth_port)
            time.sleep(5)

            self.cli.send(mu_spawn, "iwconfig " + eth_port)

            if ip_address == "default":
                self.cli.send(mu_spawn, " dhclient " + eth_port + " -v -r ")
                time.sleep(10)
                self.cli.send(mu_spawn, " dhclient " + eth_port + " -v ")
                time.sleep(10)
                self.utils.print_info("Got DHCP Address")
                self.utils.print_info("Checking the Internet reachability...")
                if self.cli.ping_from_spawn(mu_spawn, "google.com"):
                    output = self.cli.send(mu_spawn, "ifconfig " + eth_port + " | grep --color=NO \"inet addr\"")
                    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', output)
                    try:
                        return ip[0]
                    except IndexError:
                        self.utils.print_info("Error : Unable to find the IP")
                        return -1
                self.cli.send(mu_spawn, "ifconfig " + eth_port + " down")
                retry_count += 1
        self.cli.send(mu_spawn, "ifconfig " + eth_port + " down")
        self.utils.print_info("Unable to associate MU to AP")
        return 0

    def get_mu_test_ip(self, mu_spawn, interface):
        output = self.cli.send(mu_spawn, "ifconfig " + interface + " | grep --color=NO \"inet addr\"")
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', output)
        try:
            return ip[0]
        except IndexError:
            self.utils.print_info("Error : Unable to find the IP")
            return -1

    def mu_reboot(self, mu_ip, mu_port, mu_username, mu_password, mu_platform):
        spawn = self.cli.open_spawn(mu_ip, mu_port, mu_username, mu_password, mu_platform)
        output = self.reload_mu(spawn)
        return output

    def connect_mu5_to_open_network(self, ssid, ip_address="default"):
        """
        - This keyword used to connect MU5 to open network
        - Keyword Usage:
         - ``Connect MU5 To Open Network    ${SSID_NAME}``

        :param ssid: ssid name
        :return: cli ping from spawn.
        """
        ip = self.utils.get_config_value("MU5_IP")
        port = self.utils.get_config_value("MU5_PORT")
        username = self.utils.get_config_value("MU5_USERNAME")
        password = self.utils.get_config_value("MU5_PASSWORD")
        platform = self.utils.get_config_value("MU5_PLATFORM")
        interface = self.utils.get_config_value("MU5_INTERFACE")

        self.utils.print_info("MU IP         : ", ip)
        self.utils.print_info("MU Port       : ", port)
        self.utils.print_info("MU Username   : ", username)
        self.utils.print_info("MU Password   : ", password)
        self.utils.print_info("MU Platform   : ", platform)
        self.utils.print_info("MU Interface  : ", interface)

        mu_spawn = self.cli.open_spawn(ip, port, username, password, platform)

        self.cli.send(mu_spawn, "rm -rf /var/lib/dhcp/dhclient.leases")
        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        time.sleep(2)

        retries = 3
        retry_count = 1
        connect_flag = -1
        while retry_count <= retries:

            self.cli.send(mu_spawn, "ifconfig")
            time.sleep(1)
            self.cli.send(mu_spawn, "iwconfig")
            time.sleep(1)

            self.cli.send(mu_spawn, "ifconfig " + interface + " down")
            time.sleep(1)

            self.cli.send(mu_spawn, "ifconfig " + interface + " down")
            time.sleep(1)

            self.cli.send(mu_spawn, "iwconfig " + interface + " essid " + ssid)
            time.sleep(2)

            self.cli.send(mu_spawn, "iwconfig " + interface + " essid " + ssid)
            time.sleep(2)

            self.cli.send(mu_spawn, "ifconfig")
            time.sleep(1)
            self.cli.send(mu_spawn, "iwconfig")
            time.sleep(2)

            self.cli.send(mu_spawn, "ifconfig " + interface + " up")
            time.sleep(5)

            self.cli.send(mu_spawn, "ifconfig")

            retry_count += 1

            if "Access Point: Not-Associated" in self.cli.send(mu_spawn, "iwconfig"):
                time.sleep(5)
            else:
                connect_flag = 1
                break

        """
        time.sleep(1)
        count = 1
        connect_flag = -1
        while count <= 5:
            if "Access Point: Not-Associated" in self.cli.send(mu_spawn, "iwconfig"):
                time.sleep(5)
            else:
                connect_flag = 1
                break
            count += 1
        time.sleep(2)
        """
        time.sleep(5)

        dhcp_command = "dhclient " + str(interface) + " -v"
        dhcp_release_command = "dhclient " + str(interface) + " -r -v"

        if connect_flag == 1:
            if ip_address == "default":
                self.utils.print_info("Requesting DHCP IP Address...")
                self.cli.send(mu_spawn, dhcp_release_command)
                time.sleep(5)
                output = self.cli.send(mu_spawn, dhcp_command)
                if 'bound to' not in output:
                    self.cli.send(mu_spawn, dhcp_command)
                    self.cli.send(mu_spawn, "ifconfig " + str(interface))
                    self.cli.send(mu_spawn, "iwconfig " + str(interface))

        self.utils.print_info("Got DHCP Address")
        self.utils.print_info("Checking the Internet reachability...")
        return self.cli.ping_from_spawn(mu_spawn, "google.com")

    def connect_mu1_to_wep_network(self, ssid, key_type, key, key_index, ip_address="default"):
        ip = self.utils.get_config_value("MU1_IP")
        port = self.utils.get_config_value("MU1_PORT")
        username = self.utils.get_config_value("MU1_USERNAME")
        password = self.utils.get_config_value("MU1_PASSWORD")
        platform = self.utils.get_config_value("MU1_PLATFORM")
        interface = self.utils.get_config_value("MU1_INTERFACE")

        self.utils.print_info("MU IP         : ", ip)
        self.utils.print_info("MU Port       : ", port)
        self.utils.print_info("MU Username   : ", username)
        self.utils.print_info("MU Password   : ", password)
        self.utils.print_info("MU Platform   : ", platform)
        self.utils.print_info("MU Interface  : ", interface)

        mu_spawn = self.cli.open_spawn(ip, port, username, password, platform)

        expect_str = "CTRL-EVENT-CONNECTED"

        self.cli.send(mu_spawn, "rm -rf /tmp.txt")

        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        time.sleep(2)

        if key_type == "hex" or key_type == "HEX":
            key = "0x" + key

        self.cli.send(mu_spawn, "echo \"network={\" > wep.conf")
        self.cli.send(mu_spawn, "echo \' ssid=\"" + ssid + "\"\' >> wep.conf")
        self.cli.send(mu_spawn, "echo \" key_mgmt=NONE\" >> wep.conf")
        self.cli.send(mu_spawn, "echo \' wep_key0=\"" + key + "\"\' >> wep.conf")
        self.cli.send(mu_spawn, "echo \" wep_tx_keyidx=" + key_index + "\" >> wep.conf")
        self.cli.send(mu_spawn, "echo \"}\" >> wep.conf")

        file_name = "wep.conf"
        time.sleep(2)

        self.cli.send(mu_spawn, " wpa_supplicant -i " + interface + " -c " + file_name + " -B -f " + "/tmp.txt")
        time.sleep(10)

        count = 1
        connect_flag = 0
        while count < 10:
            if expect_str in self.cli.send(mu_spawn, " cat /tmp.txt | grep -i CTRL-EVENT-CONNECTED"):
                self.utils.print_info("MU Associated to SSID")
                self.cli.send(mu_spawn, "ifconfig " + interface)
                self.cli.send(mu_spawn, "iwconfig " + interface)
                connect_flag = 1
                break
            else:
                self.utils.print_info("retrying...")
                time.sleep(5)
            count += 1

        dhcp_command = "dhclient " + str(interface) + " -v"
        dhcp_release_command = "dhclient " + str(interface) + " -r -v"

        if connect_flag == 1:
            if ip_address == "default":
                self.utils.print_info("Requesting DHCP IP Address...")
                self.cli.send(mu_spawn, dhcp_release_command)
                time.sleep(5)
                output = self.cli.send(mu_spawn, dhcp_command)
                if 'bound to' not in output:
                    self.cli.send(mu_spawn, dhcp_command)
                    self.cli.send(mu_spawn, "ifconfig " + str(interface))
                    self.cli.send(mu_spawn, "iwconfig " + str(interface))
                    return mu_spawn

    def connect_mu1_to_psk_network(self, ssid, psk, ip_address="default"):
        ip = self.utils.get_config_value("MU1_IP")
        port = self.utils.get_config_value("MU1_PORT")
        username = self.utils.get_config_value("MU1_USERNAME")
        password = self.utils.get_config_value("MU1_PASSWORD")
        platform = self.utils.get_config_value("MU1_PLATFORM")
        interface = self.utils.get_config_value("MU1_INTERFACE")

        self.utils.print_info("MU IP         : ", ip)
        self.utils.print_info("MU Port       : ", port)
        self.utils.print_info("MU Username   : ", username)
        self.utils.print_info("MU Password   : ", password)
        self.utils.print_info("MU Platform   : ", platform)
        self.utils.print_info("MU Interface  : ", interface)

        mu_spawn = self.cli.open_spawn(ip, port, username, password, platform)

        expect_str = "CTRL-EVENT-CONNECTED"

        self.cli.send(mu_spawn, "rm -rf /tmp.txt")

        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        time.sleep(2)

        self.cli.send(mu_spawn, "echo \"network={\" > psk.conf")
        self.cli.send(mu_spawn, "echo \' ssid=\"" + ssid + "\"\' >> psk.conf")
        self.cli.send(mu_spawn, "echo \" proto=RSN\" >> psk.conf")
        self.cli.send(mu_spawn, "echo \" key_mgmt=WPA-PSK\" >> psk.conf")
        self.cli.send(mu_spawn, "echo \" pairwise=CCMP TKIP\" >> psk.conf")
        self.cli.send(mu_spawn, "echo \" group=CCMP TKIP\" >> psk.conf")
        self.cli.send(mu_spawn, "echo \' psk=\"" + psk + "\"\' >> psk.conf")
        self.cli.send(mu_spawn, "echo \"}\" >> psk.conf")

        file_name = "psk.conf"
        time.sleep(2)

        self.cli.send(mu_spawn, " wpa_supplicant -i " + interface + " -c " + file_name + " -B -f " + "/tmp.txt")
        time.sleep(10)

        count = 1
        connect_flag = 0
        while count < 10:
            if expect_str in self.cli.send(mu_spawn, " cat /tmp.txt | grep -i CTRL-EVENT-CONNECTED"):
                self.utils.print_info("MU Associated to SSID")
                self.cli.send(mu_spawn, "ifconfig " + interface)
                self.cli.send(mu_spawn, "iwconfig " + interface)
                connect_flag = 1
                break
            else:
                self.utils.print_info("retrying...")
                time.sleep(5)
            count += 1

        dhcp_command = "dhclient " + str(interface) + " -v"
        dhcp_release_command = "dhclient " + str(interface) + " -r -v"

        if connect_flag == 1:
            if ip_address == "default":
                self.utils.print_info("Requesting DHCP IP Address...")
                self.cli.send(mu_spawn, dhcp_release_command)
                time.sleep(5)
                output = self.cli.send(mu_spawn, dhcp_command)
                if 'bound to' not in output:
                    self.cli.send(mu_spawn, dhcp_command)
                    self.cli.send(mu_spawn, "ifconfig " + str(interface))
                    self.cli.send(mu_spawn, "iwconfig " + str(interface))

    def start_wpa_supplicant(self, mu_spawn, _interface, encryption_type, key_type="ascii", ip_address="default"):
        """

        :param mu_spawn:
        :param _interface:
        :param encryption_type:
        :param key_type:
        :param ip_address:
        :return:
        """
        interface = str(_interface)
        self.utils.print_info("MU Interface         : ", interface)
        self.utils.print_info("SSID Encryption Type : ", encryption_type)
        self.utils.print_info("IP Address           : ", ip_address)

        expect_str = "CTRL-EVENT-CONNECTED"

        self.cli.send(mu_spawn, "rm -rf /tmp.txt")
        time.sleep(5)

        self.cli.send(mu_spawn, "pkill dhclient")
        self.cli.send(mu_spawn, "pkill dhclient")
        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        self.cli.send(mu_spawn, "pkill wpa_supplicant")
        time.sleep(5)

        self.cli.send(mu_spawn, "ifconfig " + interface + " down")
        time.sleep(5)

        self.cli.send(mu_spawn, "ifconfig " + interface + " down")
        time.sleep(5)

        self.cli.send(mu_spawn, "ifconfig " + interface)
        self.cli.send(mu_spawn, "iwconfig " + interface)

        file_name = -1
        if encryption_type == "WEP-64":
            file_name = "wep_64.conf"
            if key_type == "hex":
                file_name = "wep_64_hex.conf"

        if encryption_type == "WEP-128":
            file_name = "wep_128.conf"
            if key_type == "hex":
                file_name = "wep_128_hex.conf"

        if encryption_type == "TKIP-CCMP":
            file_name = "tkip_ccmp.conf"
            if key_type == "hex":
                file_name = "tkip_ccmp_hex.conf"

        if encryption_type == "WPA2-CCMP":
            file_name = "wpa2_ccmp.conf"
            if key_type == "hex":
                file_name = "wpa2_ccmp_hex.conf"

        if encryption_type == "WPA2-CCMP-IdentiFi":
            file_name = "wpa2_ccmp_identifi.conf"
            if key_type == "hex":
                file_name = "wpa2_ccmp_hex.conf"

        if encryption_type == "WPA2-DOT1X":
            file_name = "eap_dot1x_peap.conf"
            if key_type == "hex":
                file_name = "eap_dot1x_peap_hex.conf"

        time.sleep(10)

        dhcp_command = "dhclient " + str(interface) + " -v"
        dhcp_release_command = "dhclient " + str(interface) + " -r -v"

        if file_name != -1:
            self.cli.send(mu_spawn, " wpa_supplicant -i " + interface + " -c " + file_name + " -B -f " + "/tmp.txt")
            time.sleep(10)

            count = 1
            connect_flag = 0
            while count < 10:
                if expect_str in self.cli.send(mu_spawn, " cat /tmp.txt | grep -i CTRL-EVENT-CONNECTED"):
                    self.utils.print_info("MU Associated to SSID")
                    self.cli.send(mu_spawn, "ifconfig " + interface)
                    self.cli.send(mu_spawn, "iwconfig " + interface)
                    connect_flag = 1
                    break
                else:
                    self.utils.print_info("retrying...")
                    time.sleep(5)
                count += 1

            if connect_flag == 1:
                if ip_address == "default" or ip_address == "default":
                    self.utils.print_info("Requesting DHCP IP Address...")
                    self.cli.send(mu_spawn, dhcp_release_command)
                    time.sleep(5)
                    self.utils.print_info("***************************************************************************")
                    output = self.cli.send(mu_spawn, dhcp_command)
                    self.utils.print_info("***************************************************************************")
                    if 'bound to' not in output:
                        self.cli.send(mu_spawn, dhcp_command)
                        self.cli.send(mu_spawn, "ifconfig " + str(interface))
                        self.cli.send(mu_spawn, "iwconfig " + str(interface))
            return 1

    def reload_mu(self, spawn):
        """

        :param spawn:
        :return:
        """
        self.utils.print_info("Rebooting MU...")
        spawn.sendline('reboot -f')
        spawn.read_nonblocking(size=5000)

        i = spawn.expect(["The system is going down for reboot NOW", pexpect.TIMEOUT], timeout=90)
        if i == 0:
            self.utils.print_info("Host is rebooting")
        if i == 1:
            self.utils.print_info("Host is not rebooting.. Please check")

        self.utils.print_info("Before : ", spawn.before)
        self.utils.print_info("After  : ", spawn.after)
        return 1

    def mu_interface_down(self, mu_spawn, interface):
        """
        - This keyword used to bring down MU interface
        - Keyword Usage:
         - ``MU Interface Down      ${MU5_SPAWN}      ${MU5_INTERFACE}``

        :param mu_spawn: MU5 spawn
        :param interface: MU5 interface
        :return:
        """
        self.utils.print_info("Bring down MU interface")
        time.sleep(10)
        self.cli.send(mu_spawn, "ifconfig " + str(interface) + " down")
        time.sleep(2)
