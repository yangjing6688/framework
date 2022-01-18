from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Logger.Logger import Logger


class EndsystemCloudConnectConfigKeywords(object, metaclass=Singleton):
    def __init__(self):
        self.logger = Logger()
        self.config_blocks = DeviceValueStorage.storageDictionary

########################################################################################################################
#   Configuration Keywords   ###########################################################################################
########################################################################################################################
    def configure_client_management_ipv4_address(self, vlan, serial, ip_address="0.0.0.0", netmask="0.0.0.0",
                                                 gateway="0.0.0.0", dns="0.0.0.0", domain=None, ntp=None):
        """
        Keyword Arguments:
        vlan            - The vlan to be used for Management. oob or ID.
        serial          - The serial number of the device state list being cleared.
        ip_address      - The IPv4 Address to assign the OutOfBandMgmt port. (Optional)
        netmask         - The network mask for the IPv4 address. (Optional)
        gateway         - The default gateway address. (Optional)
        dns             - The DNS address. (Optional)
        domain          - The default domain for the OutOfBandMgmt port. (Optional)
        ntp             - The NTP server IP address. (Optional)
        """
        self.initialize_config_serial(serial)
        prefix = StringUtils.prefix_len(netmask) if netmask is not None else "0"
        dhcp = True if ip_address == "0.0.0.0" else False

        if not dhcp:
            if str(vlan).lower() == "oob":
                self.config_blocks[serial]["oob_mgmt"] = {
                    "networkAddress": ip_address,
                    "dnsServer": dns,
                    "domainName": domain,
                    "dhcpClient": dhcp,
                    "role": "OutOfBandMgmt",
                    "networkPrefixLength": prefix,
                    "networkDefaultGateway": gateway
                }
                if ntp is not None:
                    self.config_blocks[serial]["oob_mgmt"]["ntpServer"] = ntp
                self.logger.log_info("Out of Band Management port configured with IP address: " + str(ip_address))
            else:
                vlan = int(vlan)
                if 1 <= vlan < 4095:
                    if "vlans" not in self.config_blocks[serial]:
                        self.configure_client_vlan_create(serial, vlan)
                    self.config_blocks[serial]["vlans"][vlan]["dnsServer"] = dns
                    self.config_blocks[serial]["vlans"][vlan]["management"] = True
                    self.config_blocks[serial]["vlans"][vlan]["networkAddress"] = ip_address
                    self.config_blocks[serial]["vlans"][vlan]["dhcpClient"] = dhcp
                    self.config_blocks[serial]["vlans"][vlan]["networkPrefixLength"] = prefix
                    self.config_blocks[serial]["vlans"][vlan]["networkDefaultGateway"] = gateway
                    if ntp is not None:
                        self.config_blocks[serial]["vlans"][vlan]["ntpServer"] = ntp
                else:
                    self.logger.log_info("Invalid VLAN ID: " + str(vlan) + " Must be in range 1-4094")
        else:
            if str(vlan).lower() == "oob":
                self.config_blocks[serial]["oob_mgmt"] = {
                    "dhcpClient": dhcp,
                    "role": "OutOfBandMgmt",
                }
                self.logger.log_info("Out of Band Management port configured with DHCP.")
            else:
                vlan = int(vlan)
                if 1 <= vlan < 4095:
                    if "vlans" not in self.config_blocks[serial]:
                        self.configure_client_vlan_create(serial, vlan)
                    elif vlan not in self.config_blocks[serial]["vlans"]:
                        self.configure_client_vlan_create(serial, vlan)
                    self.config_blocks[serial]["vlans"][vlan]["management"] = True
                    self.config_blocks[serial]["vlans"][vlan]["dhcpClient"] = dhcp
                else:
                    self.logger.log_info("Invalid VLAN ID: " + str(vlan) + " Must be in range 1-4094")

    def configure_client_port_enabled(self, serial, ports):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        ports           - The port(s) configuration being modified.
        """
        self.initialize_config_serial(serial)
        if "-" in ports:
            ports = map(str, StringUtils.range_to_list(ports))
        for port in ListUtils.convert_to_list(ports):
            port = StringUtils.normalize_exos_ports(port)
            port_dict = {"adminStatus": "on",
                         "linkSpeed": "Auto",
                         "pvid": 1,
                         "nodeAlias": False,
                         "linkDuplex": "auto",
                         "portName": port}
            if "ports" in self.config_blocks[serial]:
                if port not in self.config_blocks[serial]["ports"]:
                    self.config_blocks[serial]["ports"][port] = port_dict
                    self.logger.log_info("Created portConfig entry for port " + port + " with adminStatus \"on\".")
                else:
                    self.config_blocks[serial]["ports"][port]["adminStatus"] = "on"
                    self.logger.log_info("Modified portConfig entry for port " + port + " with adminStatus \"on\".")
            else:
                self.config_blocks[serial]["ports"] = {port: port_dict}
                self.logger.log_info("Created portConfig entry for port " + port + " with adminStatus \"on\".")

    def configure_client_port_disabled(self, serial, ports):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        ports           - The port(s) configuration being modified.
        """
        self.initialize_config_serial(serial)
        for port in ListUtils.convert_to_list(ports):
            port = StringUtils.normalize_exos_ports(port)
            port_dict = {"adminStatus": "off",
                         "linkSpeed": "Auto",
                         "pvid": 1,
                         "nodeAlias": False,
                         "linkDuplex": "auto",
                         "portName": port}
            if "ports" in self.config_blocks[serial]:
                if port not in self.config_blocks[serial]["ports"]:
                    self.config_blocks[serial]["ports"][port] = port_dict
                    self.logger.log_info("Created portConfig entry for port " + port + " with adminStatus \"off\".")
                else:
                    self.config_blocks[serial]["ports"][port]["adminStatus"] = "off"
                    self.logger.log_info("Modified portConfig entry for port " + port + " with adminStatus \"off\".")
            else:
                self.config_blocks[serial]["ports"] = {port: port_dict}
                self.logger.log_info("Created portConfig entry for port " + port + " with adminStatus \"off\".")

    def configure_client_vlan_create(self, serial, vlans):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        vlans           - The vlan('s) configuration being modified.
        """
        self.initialize_config_serial(serial)
        for vlan in ListUtils.convert_to_list(vlans):
            vlan = vlan if isinstance(vlan, int) else int(vlan)
            vlan_dict = {"dnsServer": None,
                         "management": False,
                         "networkAddress": None,
                         "networkPrefixLength": None,
                         "networkDefaultGateway": None,
                         "name": "Default" if vlan == 1 else StringUtils.exos_vlan_string(str(vlan)),
                         "domainName": None,
                         "dynamic": False,
                         "ntpServer": None,
                         "dynamicUntaggedEgressPorts": [],
                         "vlanIds": str(vlan),
                         "vlanId": vlan,
                         "untaggedEgressPorts": [],
                         "dhcpClient": False,
                         "role": "VLAN",
                         "routing": False,
                         "dynamicTaggedEgressPorts": [],
                         "taggedEgressPorts": [],
                         "igmp": {"query": True, "snooping": True}}

            if "vlans" in self.config_blocks[serial]:
                if vlan not in self.config_blocks[serial]["vlans"]:
                    self.config_blocks[serial]["vlans"][vlan] = vlan_dict
                    self.logger.log_info("Created vlanConfig entry for VLAN " + str(vlan) + ".")
                else:
                    self.logger.log_info("VLAN entry already exists in vlanConfig!")
            else:
                self.config_blocks[serial]["vlans"] = {vlan: vlan_dict}
                self.logger.log_info("Created vlanConfig entry for VLAN " + str(vlan) + ".")

    def configure_client_vlan_add_ports_untagged(self, serial, vlan, ports):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        vlan            - The vlan('s) configuration being modified.
        ports           - The port(s) to add to the VLAN's untagged egress list.
        """
        self.initialize_config_serial(serial)
        vlan = vlan if isinstance(vlan, int) else int(vlan)
        if "-" in ports:
            ports = map(str, StringUtils.range_to_list(ports))

        if "vlans" in self.config_blocks[serial]:
            if vlan not in self.config_blocks[serial]["vlans"]:
                self.configure_client_vlan_create(serial, vlan)
        else:
            self.configure_client_vlan_create(serial, vlan)
        self._add_untagged_ports(serial, vlan, ports)

    def configure_client_vlan_remove_ports_untagged(self, serial, vlan, ports):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        vlan            - The vlan('s) configuration being modified.
        ports           - The port(s) to add to the VLAN's untagged egress list.
        """
        self.initialize_config_serial(serial)
        vlan = vlan if isinstance(vlan, int) else int(vlan)
        if "vlans" in self.config_blocks[serial]:
            if vlan in self.config_blocks[serial]["vlans"]:
                for port in ListUtils.convert_to_list(ports):
                    port = StringUtils.normalize_exos_ports(port)
                    if str(port) not in self.config_blocks[serial]["vlans"][vlan]["untaggedEgressPorts"]:
                        self.logger.log_info(
                            "Port " + str(port) + " is not in VLAN " + str(vlan) + "'s Untagged Egress list.")
                    else:
                        self.config_blocks[serial]["vlans"][vlan]["untaggedEgressPorts"].remove(str(port))
                        self.logger.log_info(
                            "Port " + str(port) + " removed from Untagged Egress for VLAN " + str(vlan) + ".")
            else:
                self.logger.log_error("VLAN " + str(vlan) + " does not exist in vlanConfig.")
        else:
            self.logger.log_error("VLAN " + str(vlan) + " does not exist in vlanConfig.")

    def configure_client_vlan_add_ports_tagged(self, serial, vlan, ports):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        vlan            - The vlan('s) configuration being modified.
        ports           - The port(s) to add to the VLAN's tagged egress list.
        """
        self.initialize_config_serial(serial)
        vlan = vlan if isinstance(vlan, int) else int(vlan)
        if "-" in ports:
            ports = map(str, StringUtils.range_to_list(ports))

        if "vlans" in self.config_blocks[serial]:
            if vlan not in self.config_blocks[serial]["vlans"]:
                self.configure_client_vlan_create(serial, vlan)
        else:
            self.configure_client_vlan_create(serial, vlan)
        self._add_tagged_ports(serial, vlan, ports)

    def configure_client_vlan_remove_ports_tagged(self, serial, vlan, ports):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        vlan            - The vlan('s) configuration being modified.
        ports           - The port(s) to add to the VLAN's tagged egress list.
        """
        self.initialize_config_serial(serial)
        vlan = vlan if isinstance(vlan, int) else int(vlan)
        if "vlans" in self.config_blocks[serial]:
            if vlan in self.config_blocks[serial]["vlans"]:
                for port in ListUtils.convert_to_list(ports):
                    port = StringUtils.normalize_exos_ports(port)
                    if str(port) not in self.config_blocks[serial]["vlans"][vlan]["taggedEgressPorts"]:
                        self.logger.log_info(
                            "Port " + str(port) + " is not in VLAN " + str(vlan) + "'s Tagged Egress list.")
                    else:
                        self.config_blocks[serial]["vlans"][vlan]["taggedEgressPorts"].remove(str(port))
                        self.logger.log_info(
                            "Port " + str(port) + " removed from Tagged Egress for VLAN " + str(vlan) + ".")
            else:
                self.logger.log_error("VLAN " + str(vlan) + " does not exist in vlanConfig.")
        else:
            self.logger.log_error("VLAN " + str(vlan) + " does not exist in vlanConfig.")

    def configure_client_port_pvid(self, serial, ports, pvid):
        """
        Keyword Arguments:
        serial - The serial number of the device configuration to modify.
        ports  - The port(s) configuration being modified.
        pvid   - The PVID value to set on the port(s).
        """
        self.initialize_config_serial(serial)
        for port in ListUtils.convert_to_list(ports):
            port = StringUtils.normalize_exos_ports(port)
            if "ports" not in self.config_blocks[serial]:
                self.logger.log_info("Port entry does not exist, creating in Disabled state.")
                self.configure_client_port_disabled(serial, port)
            elif port not in self.config_blocks[serial]["ports"]:
                self.logger.log_info("Port entry does not exist, creating in Disabled state.")
                self.configure_client_port_disabled(serial, port)

            self.config_blocks[serial]["ports"][port]["pvid"] = int(pvid)
            self.logger.log_info("Modified portConfig entry for port " + port + " with PVID " + str(pvid) + ".")

    def configure_client_radius_server(self, serial, ip_address, port, key, client_ip=None, realm="any", precedence=1):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        ip_address      - The IP Address of the RADIUS server.
        port            - The RADIUS network port.
        key             - The shared key for the RADIUS server.
        client_ip       - The IP Address of the Switch.
        realm           - The port group to source RADIUS packets. (network = Front-Panel, management = OOB)
        precedence      - The precedence order of the RADIUS server. ( 1 or 2, primary/secondary)
        """
        self.initialize_config_serial(serial)
        radius_dict = {"networkAddress": StringUtils.normalize_value(ip_address, PacketConstants.IPV4_ADDRESS),
                       "networkPort": int(port),
                       "sharedKey": key,
                       "realmType": realm,
                       "precedence": int(precedence)}
        if client_ip is not None:
            radius_dict["clientIP"] = StringUtils.normalize_value(client_ip, PacketConstants.IPV4_ADDRESS)
        if "radius" in self.config_blocks[serial]:
            self.config_blocks[serial]["radius"].append(radius_dict)
        else:
            self.config_blocks[serial]["radius"] = [radius_dict]
        self.logger.log_info("Added RADIUS config for server: " + str(ip_address))

    def configure_client_macauth(self, serial, global_enable, logging="info", enable_ports=None, disable_ports=None):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        global_enable   - The global state for MAC Authentication. (True or False)
        logging         - The logging level for MAC Authentication.
                          (emergency | alert | critical | error | warning | notice | info | debug | none)
        enable_ports    - The list of ports to enable for MAC Authentication.
        disable_ports   - The list of ports to disable for MAC Authentication.
        """
        self.initialize_config_serial(serial)
        log_types = ["emergency", "alert", "critical", "error", "warning", "notice", "info", "debug", "none"]
        if logging.lower() in log_types:
            logging = logging.lower()
        else:
            raise ValueError("Invalid MACauth logging level. Must be one of the following: " + str(log_types))

        macauth_dict = {"enabled": False if not global_enable else True,
                        "logging": logging,
                        "macAuthConfig": []
                        }
        if enable_ports is not None:
            macauth_dict["macAuthConfig"].append({"macAuthEnable": True,
                                                  "macAuthPorts": ListUtils.convert_to_list(enable_ports)})
        if disable_ports is not None:
            macauth_dict["macAuthConfig"].append({"macAuthEnable": False,
                                                  "macAuthPorts": ListUtils.convert_to_list(disable_ports)})

        self.config_blocks[serial]["macauth"] = macauth_dict
        self.logger.log_info("Added MACauth configBlock with \'enabled\':" + str(global_enable))

    def configure_client_license(self, serial, system_license, effective_level):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        system_license  - The License string for the system or "" if no license install necessary.
        effective_level - The logging level for MAC Authentication.
                          (l2_edge | edge | advanced | advanced_edge | core | advanced_core | trial)
        """
        self.initialize_config_serial(serial)
        levels = ["l2_edge", "edge", "advanced", "advanced_edge", "core", "advanced_core", "trial"]

        if effective_level.lower() in levels:
            license_dict = {"system_license": system_license,
                            "effective_level": effective_level.lower()}
        else:
            raise ValueError("Invalid effective license level: " + effective_level.lower())

        if "license" in self.config_blocks[serial]:
            self.config_blocks[serial]["license"].update(license_dict)
        else:
            self.config_blocks[serial]["license"] = license_dict

    def configure_client_feature_pack(self, serial, feature_name, feature_license):
        """
        Keyword Arguments:
        serial          - The serial number of the device configuration to modify.
        feature_name    - The name of the Feature Pack.
        feature_license - The license of the Feature Pack.
        """
        self.initialize_config_serial(serial)
        features = ["mpls", "flowvsr", "serviceprovideredge", "ssh", "directattach", "networktiming", "3rdpartyoptics",
                    "avb", "openflowsdn", "trill", "quad 10g uplink", "dual 10g uplink"]

        if feature_name.lower() in features:
            license_dict = {"feature_name": feature_name.lower(),
                            "feature_license": feature_license}
        else:
            raise ValueError("Invalid effective feature name: " + feature_name.lower())

        if "feature_packs" in self.config_blocks[serial]:
            self.config_blocks[serial]["feature_packs"].append(license_dict)
        else:
            self.config_blocks[serial]["feature_packs"] = [license_dict]

    def configure_client_add_login(self, serial, username, password, level="READ_ONLY", recovery=False):
        """
        Keyword Arguments:
        serial   - The serial number of the device configuration to modify.
        username - The username for the new login.
        password - The password for the new login.
        level    - The access level for the new login.
        recovery - The 'isRecoveryAccount' flag. (True or False).
        """
        self.initialize_config_serial(serial)
        valid_levels = ["READ_ONLY", "READ_WRITE", "SUPER_USER"]
        if level.upper() in valid_levels:
            level = level.upper()

            login_dict = {"username": username,
                          "password": password,
                          "accessLevel": level,
                          "isRecoveryAccount": True if recovery else False}

            if "logins" in self.config_blocks[serial]:
                for i, user in enumerate(self.config_blocks[serial]["logins"]):
                    if user["username"] == username:
                        self.config_blocks[serial]["logins"].pop(i)
                        self.logger.log_info("Login entry for username: " + username + " already exists! Overwriting.")
                self.config_blocks[serial]["logins"].append(login_dict)
            else:
                self.config_blocks[serial]["logins"] = [login_dict]
            self.logger.log_info("Login entry for username: " + username + " has been added.")

        else:
            self.logger.log_error("User access level \"" + level.upper() + "\" is not in valid accessLevels:\n" +
                                  str(valid_levels))
            raise FailureException

    def configure_client_remove_login(self, serial, username):
        """
        Keyword Arguments:
        serial   - The serial number of the device configuration to modify.
        username - The username for the new login.
        """
        self.initialize_config_serial(serial)
        found = False
        if "logins" in self.config_blocks[serial]:
            for i, user in enumerate(self.config_blocks[serial]["logins"]):
                if user["username"] == username:
                    found = True
                    self.config_blocks[serial]["logins"].pop(i)
                    self.logger.log_info("Login entry for username: " + username + " has been removed.")
        if not found:
            self.logger.log_info("Login entry for username: " + username + " was not found, ignoring.")

########################################################################################################################
#   Helper Functions   #################################################################################################
########################################################################################################################
    def build_config_response(self, serial):
        """
        Combines the Configuration Blocks in config_blocks into a single dictionary
        for the CcConfigResponse.
        """
        reply_dict = {"configBlock": {}}
        if serial in self.config_blocks:
            if "vlans" in self.config_blocks[serial] or "oob_mgmt" in self.config_blocks[serial]:
                reply_dict["configBlock"]["vlans"] = self._build_vlan_config(serial)
            if "ports" in self.config_blocks[serial]:
                reply_dict["configBlock"]["ports"] = self._build_port_config(serial)
            if "radius" in self.config_blocks[serial]:
                reply_dict["configBlock"]["radiusServers"] = self._build_radius_config(serial)
            if "macauth" in self.config_blocks[serial]:
                reply_dict["configBlock"]["macAuth"] = self.config_blocks[serial]["macauth"]
            if "license" in self.config_blocks[serial]:
                reply_dict["configBlock"]["license"] = self._build_license_config(serial)
            if "logins" in self.config_blocks[serial]:
                reply_dict["configBlock"]["logins"] = self._build_login_config(serial)
        else:
            self.config_blocks[serial] = {}

        return reply_dict

    def _build_port_config(self, serial):
        """
        Builds the "ports" list for the configBlock dictionary using all the key values in the self.config_blocks
        "ports" dictionary for the device's serial number.
        """
        port_list = list(self.config_blocks[serial]["ports"].values())
        return port_list

    def _build_vlan_config(self, serial):
        """
        Builds the "vlans" list for the configBlock dictionary using all the key values in the self.config_blocks
        "vlans" dictionary for the device's serial number.
        """
        vlan_dict = dict()
        if "vlans" in self.config_blocks[serial]:
            vlan_dict["vlanConfig"] = list(self.config_blocks[serial]["vlans"].values())
            if "oob_mgmt" in self.config_blocks[serial]:
                vlan_dict["vlanConfig"].append(self.config_blocks[serial]["oob_mgmt"])
        elif "oob_mgmt" in self.config_blocks[serial]:
            vlan_dict["vlanConfig"] = [self.config_blocks[serial]["oob_mgmt"]]
        return vlan_dict

    def _build_radius_config(self, serial):
        """
        Builds the "radiusServer" list for the configBlock dictionary using all the key values in the self.config_blocks
        "radius" dictionary for the device's serial number.
        """
        return self.config_blocks[serial]["radius"]

    def _build_license_config(self, serial):
        """
        Builds the "license" block for the configBlock dictionary using all the key values in the self.config_blocks
        "license" and "feature_pack" dictionaries for the device's serial number.
        """
        license_dict = self.config_blocks[serial]["license"]
        if "feature_packs" in self.config_blocks[serial]:
            license_dict["featurePacks"] = self.config_blocks[serial]["feature_packs"]
        return license_dict

    def _add_untagged_ports(self, serial, vlan, ports):
        for port in ListUtils.convert_to_list(ports):
            port = StringUtils.normalize_exos_ports(port)
            if str(port) not in self.config_blocks[serial]["vlans"][vlan]["untaggedEgressPorts"]:
                self.config_blocks[serial]["vlans"][vlan]["untaggedEgressPorts"].append(str(port))
                self.logger.log_info(
                    "Port " + str(port) + " added to Untagged Egress for VLAN " + str(vlan) + ".")
            else:
                self.config_blocks[serial]["vlans"][vlan]["untaggedEgressPorts"].append(str(port))
                self.logger.log_info(
                    "Port " + str(port) + " added to Untagged Egress for VLAN " + str(vlan) + ".")

    def _add_tagged_ports(self, serial, vlan, ports):
        for port in ListUtils.convert_to_list(ports):
            port = StringUtils.normalize_exos_ports(port)
            if str(port) not in self.config_blocks[serial]["vlans"][vlan]["taggedEgressPorts"]:
                self.config_blocks[serial]["vlans"][vlan]["taggedEgressPorts"].append(str(port))
                self.logger.log_info(
                    "Port " + str(port) + " added to Tagged Egress for VLAN " + str(vlan) + ".")
            else:
                self.config_blocks[serial]["vlans"][vlan]["taggedEgressPorts"].append(str(port))
                self.logger.log_info(
                    "Port " + str(port) + " added to Tagged Egress for VLAN " + str(vlan) + ".")

    def _build_login_config(self, serial):
        """
        Builds the "ports" list for the configBlock dictionary using all the key values in the self.config_blocks
        "ports" dictionary for the device's serial number.
        """
        login_list = self.config_blocks[serial]["logins"]
        return {"loginConfig": login_list}

    def initialize_config_serial(self, serial):
        """
        Reserved for later use, if necessary.
        """
        if serial not in self.config_blocks:
            self.config_blocks[serial] = {}
