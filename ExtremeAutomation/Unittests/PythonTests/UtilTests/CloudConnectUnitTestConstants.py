from ExtremeAutomation.Library.Utils.Constants.Constants import Constants


class CloudConnectUnitTestConstants(Constants):
    # configBlock Constants
    config_block_dut = {"configBlock": {
        "poe": {"enabled": False,
                "disconnectedPrecedence": "deny-port",
                "logging": "debug",
                "ports": [
                    {"portName": "1",
                     "enabled": True,
                     "poePortAlias": "1",
                     "detection": "bypass",
                     "operatorLimit": "15400",
                     "priority": "critical"
                     },
                    {"portName": "2",
                     "enabled": True,
                     "poePortAlias": "2",
                     "detection": "bypass",
                     "operatorLimit": "15400",
                     "priority": "critical"
                     },
                    {"portName": "3",
                     "enabled": True,
                     "poePortAlias": "3",
                     "detection": "bypass",
                     "operatorLimit": "15400",
                     "priority": "critical"
                     }]
                },
        "dot1x": {"enabled": False,
                  "logging": "debug",
                  "dot1xConfig": [
                      {"dot1xEnable": True,
                       "dot1xPorts": ["1", "2"]
                       },
                      {"dot1xEnable": False,
                       "dot1xPorts": ["3"]
                       }
                  ]},
        "lacp": {"enabled": True,
                 "logging": "debug",
                 "lags": [
                     {"enabled": True,
                      "lagPort": "1",
                      "lagPorts": ["1", "2"]}
                 ]},
        "lldp": {"enabled": True,
                 "logging": "debug",
                 "tlvMgmtAddress": True,
                 "mgmtAddress": "202.1.1.10",
                 "tlvSystemName": True,
                 "systemName": "chill_test",
                 "tlvLocation": True,
                 "location": "cloud9",
                 "lldpConfig": [
                     {"lldpEnable": True,
                      "lldpPorts": ["1", "2"]},
                     {"lldpEnable": False,
                      "lldpPorts": ["3"]}
                 ]},
        "logins": {
            "loginConfig": [
                {"username": "admin",
                 "password": "",
                 "accessLevel": "SUPER_USER",
                 "isRecoveryAccount": True},
                {"username": "user",
                 "password": "",
                 "accessLevel": "READ_ONLY",
                 "isRecoveryAccount": False}
            ]},
        "macauth": {"enabled": True,
                    "logging": "debug",
                    "macAuthConfig": [
                        {"macAuthEnable": True,
                         "macAuthPorts": ["1", "2", "3"]},
                        {"macAuthEnable": False,
                         "macAuthPorts": []}
                    ]},
        "radiusServers": [
            {"networkAddress": "202.1.1.2",
             "networkPort": 1812,
             "sharedKey": "BeExtreme!",
             "realmType": "management",
             "clientIP": "202.1.1.10",
             "precedence": 1}
        ],
        "ports": [
            {"portName": "1",
             "portAlias": "1",
             "adminStatus": "on",
             "pvid": 1,
             "nodeAlias": True,
             "mvrp": False,
             "admitRules": "admitAll",
             "ingressFiltering": "disabled",
             "linkDuplex": "auto",
             "linkSpeed": "Auto",
             "linkDuplexList": ["auto"],
             "linkSpeedList": ["10", "100", "1G"]},
            {"portName": "2",
             "portAlias": "2",
             "adminStatus": "on",
             "pvid": 1,
             "nodeAlias": True,
             "mvrp": False,
             "admitRules": "admitAll",
             "ingressFiltering": "disabled",
             "linkDuplex": "auto",
             "linkSpeed": "Auto",
             "linkDuplexList": ["auto"],
             "linkSpeedList": ["10", "100", "1G"]},
            {"portName": "3",
             "portAlias": "3",
             "adminStatus": "on",
             "pvid": 1,
             "nodeAlias": True,
             "mvrp": False,
             "admitRules": "admitAll",
             "ingressFiltering": "disabled",
             "linkDuplex": "auto",
             "linkSpeed": "Auto",
             "linkDuplexList": ["auto"],
             "linkSpeedList": ["10", "100", "1G"]}
        ],
        "snmp": {"sysName": "chill_test",
                 "sysLocation": "cloud9",
                 "sysContact": "chill@extremenetworks.com",
                 "snmpV1": {"enabled": True,
                            "logging": "debug",
                            "communities": [
                                {"name": "public",
                                 "accessLevel": "READ_ONLY"}
                            ]},
                 "snmpV2c": {"enabled": True,
                             "logging": "debug",
                             "communities": [
                                 {"name": "publicv2",
                                  "accessLevel": "READ_WRITE"}
                             ]},
                 "snmpV3": {"enabled": False,
                            "logging": "none",
                            "users": [],
                            "notifications": []}
                 },
        "spanningTree": {"enabled": True,
                         "logging": "debug",
                         "version": "mstp",
                         "bridgePriority": 32768,
                         "portLinkType": [
                             {"linkType": "auto",
                              "linkTypePorts": ["1", "2", "3"]},
                             {"linkType": "broadcast",
                              "linkTypePorts": []},
                             {"linkType": "point-to-point",
                              "linkTypePorts": []},
                             {"linkType": "edge",
                              "linkTypePorts": []}],
                         "spanGuard": [
                             {"spanGuardEnabled": False,
                              "spanGuardPorts": ["1", "2", "3"]},
                             {"spanGuardEnabled": True,
                              "spanGuardPorts": []}],
                         "loopProtect": [
                             {"loopProtectEnabled": True,
                              "loopProtectPorts": ["1", "2", "3"]},
                             {"loopProtectEnabled": False,
                              "loopProtectPorts": []}]
                         },
        "syslog": {"enabled": True,
                   "logging": "debug",
                   "syslogConfig": [
                       {"serverNetworkAddress": "202.1.1.2",
                        "serverUdpPort": 162}]
                   },
        "vlans": {"vlanConfig": [
            {"vlanIds": "1",
             "vlanId": 1,
             "name": "Default",
             "dynamic": False,
             "untaggedEgressPorts": ["1", "2", "3"],
             "taggedEgressPorts": [],
             "dynamicUntaggedEgressPorts": [],
             "dynamicTaggedEgressPorts": [],
             "networkAddress": "",
             "networkPrefixLength": 0,
             "networkDefaultGateway": "",
             "dnsServer": "",
             "domainName": "",
             "routing": False,
             "management": False,
             "ntpServer": "",
             "dhcpClient": False,
             "igmp": {"snooping": False,
                      "query": False}
             }
        ]},
        "vxlan": {"enabled": False,
                  "logging": "error"},
        "mgmtAccess": {"telnetConfig": {"telnetEnabled": True},
                       "sshConfig": {"sshEnabled": True},
                       "httpConfig": {"httpEnabled": True},
                       "httpsConfig": {"httpsEnabled": False}}
    }}

    config_block_robot = {"configBlock": {
        "license": {"systemLicense": "4e51-69d1-c7a4-2a95-6fff",
                    "effectiveLevel": "Advanced Edge",
                    "featurePacks": [{"featurePackName": "ServiceProviderEdge",
                                      "featurePackLicense": "4e51-69d1-c7a4-2a95-6eee"}]
                    },
        "poe": {"enabled": False,
                "disconnectedPrecedence": "deny-port",
                "logging": "debug",
                "ports": [
                    {"portName": "1",
                     "enabled": True,
                     "poePortAlias": "1",
                     "detection": "bypass",
                     "operatorLimit": "15400",
                     "priority": "critical"
                     },
                    {"portName": "2",
                     "enabled": True,
                     "poePortAlias": "2",
                     "detection": "bypass",
                     "operatorLimit": "15400",
                     "priority": "critical"
                     },
                    {"portName": "3",
                     "enabled": True,
                     "poePortAlias": "3",
                     "detection": "bypass",
                     "operatorLimit": "15400",
                     "priority": "critical"
                     }]
                },
        "dot1x": {"enabled": False,
                  "logging": "debug",
                  "dot1xConfig": [
                      {"dot1xEnable": True,
                       "dot1xPorts": ["1", "2"]
                       },
                      {"dot1xEnable": False,
                       "dot1xPorts": ["3"]
                       }
                  ]},
        "lacp": {"enabled": True,
                 "logging": "debug",
                 "lags": [
                     {"enabled": True,
                      "lagPort": "1",
                      "lagPorts": ["1", "2"]}
                 ]},
        "lldp": {"enabled": True,
                 "logging": "debug",
                 "tlvMgmtAddress": True,
                 "mgmtAddress": "202.1.1.10",
                 "tlvSystemName": True,
                 "systemName": "chill_test",
                 "tlvLocation": True,
                 "location": "cloud9",
                 "lldpConfig": [
                     {"lldpEnable": True,
                      "lldpPorts": ["1", "2"]},
                     {"lldpEnable": False,
                      "lldpPorts": ["3"]}
                 ]},
        "logins": {
            "loginConfig": [
                {"username": "admin",
                 "password": "",
                 "accessLevel": "SUPER_USER",
                 "isRecoveryAccount": True},
                {"username": "user",
                 "password": "",
                 "accessLevel": "READ_ONLY",
                 "isRecoveryAccount": False}
            ]},
        "macauth": {"enabled": True,
                    "logging": "debug",
                    "macAuthConfig": [
                        {"macAuthEnable": True,
                         "macAuthPorts": ["1", "2", "3"]},
                        {"macAuthEnable": False,
                         "macAuthPorts": []}
                    ]},
        "radiusServers": [
            {"networkAddress": "202.1.1.2",
             "networkPort": 1812,
             "sharedKey": "BeExtreme!",
             "realmType": "management",
             "clientIP": "202.1.1.10",
             "precedence": 1}
        ],
        "ports": [
            {"portName": "1",
             "portAlias": "1",
             "adminStatus": "on",
             "pvid": 1,
             "nodeAlias": True,
             "mvrp": False,
             "admitRules": "admitAll",
             "ingressFiltering": "disabled",
             "linkDuplex": "auto",
             "linkSpeed": "Auto",
             "linkDuplexList": ["auto"],
             "linkSpeedList": ["10", "100", "1G"]},
            {"portName": "2",
             "portAlias": "2",
             "adminStatus": "on",
             "pvid": 1,
             "nodeAlias": True,
             "mvrp": False,
             "admitRules": "admitAll",
             "ingressFiltering": "disabled",
             "linkDuplex": "auto",
             "linkSpeed": "Auto",
             "linkDuplexList": ["auto"],
             "linkSpeedList": ["10", "100", "1G"]},
            {"portName": "3",
             "portAlias": "3",
             "adminStatus": "on",
             "pvid": 1,
             "nodeAlias": True,
             "mvrp": False,
             "admitRules": "admitAll",
             "ingressFiltering": "disabled",
             "linkDuplex": "auto",
             "linkSpeed": "Auto",
             "linkDuplexList": ["auto"],
             "linkSpeedList": ["10", "100", "1G"]}
        ],
        "snmp": {"sysName": "chill_test",
                 "sysLocation": "cloud9",
                 "sysContact": "chill@extremenetworks.com",
                 "snmpV1": {"enabled": True,
                            "logging": "debug",
                            "communities": [
                                {"name": "public",
                                 "accessLevel": "READ_ONLY"}
                            ]},
                 "snmpV2c": {"enabled": True,
                             "logging": "debug",
                             "communities": [
                                 {"name": "publicv2",
                                  "accessLevel": "READ_WRITE"}
                             ]},
                 "snmpV3": {"enabled": False,
                            "logging": "none",
                            "users": [],
                            "notifications": []}
                 },
        "spanningTree": {"enabled": True,
                         "logging": "debug",
                         "version": "mstp",
                         "bridgePriority": 32768,
                         "portLinkType": [
                             {"linkType": "auto",
                              "linkTypePorts": ["1", "2", "3"]},
                             {"linkType": "broadcast",
                              "linkTypePorts": []},
                             {"linkType": "point-to-point",
                              "linkTypePorts": []},
                             {"linkType": "edge",
                              "linkTypePorts": []}],
                         "spanGuard": [
                             {"spanGuardEnabled": False,
                              "spanGuardPorts": ["1", "2", "3"]},
                             {"spanGuardEnabled": True,
                              "spanGuardPorts": []}],
                         "loopProtect": [
                             {"loopProtectEnabled": True,
                              "loopProtectPorts": ["1", "2", "3"]},
                             {"loopProtectEnabled": False,
                              "loopProtectPorts": []}]
                         },
        "syslog": {"enabled": True,
                   "logging": "debug",
                   "syslogConfig": [
                       {"serverNetworkAddress": "202.1.1.2",
                        "serverUdpPort": 162}]
                   },
        "vlans": {"vlanConfig": [
            {"vlanIds": "1",
             "vlanId": 1,
             "name": "Default",
             "dynamic": False,
             "untaggedEgressPorts": ["1", "2", "3"],
             "taggedEgressPorts": [],
             "dynamicUntaggedEgressPorts": [],
             "dynamicTaggedEgressPorts": [],
             "networkAddress": "",
             "networkPrefixLength": 0,
             "networkDefaultGateway": "",
             "dnsServer": "",
             "domainName": "",
             "routing": False,
             "management": False,
             "ntpServer": "",
             "dhcpClient": False,
             "igmp": {"snooping": False,
                      "query": False}
             },
            {"networkAddress": "202.1.1.10",
             "dnsServer": "202.1.1.2",
             "domainName": "extremenetworks.com",
             "ntpServer": "202.1.1.2",
             "dhcpClient": False,
             "role": "OutOfBandMgmt",
             "networkPrefixLength": "24",
             "networkDefaultGateway": "202.1.1.2"
             }
        ]},
        "vxlan": {"enabled": False,
                  "logging": "error"},
        "mgmtAccess": {"telnetConfig": {"telnetEnabled": True},
                       "sshConfig": {"sshEnabled": True},
                       "httpConfig": {"httpEnabled": True},
                       "httpsConfig": {"httpsEnabled": False}}
    }}

    config_block_result = {"configBlock": {
        "logins": {
            "loginConfig": [{
                "username": "admin",
                "accessLevel": "SUPER_USER",
                "password": "",
                "isRecoveryAccount": True},
                {"username": "user",
                 "accessLevel": "READ_ONLY",
                 "password": "",
                 "isRecoveryAccount": False}
            ]},
        "lacp": {
            "logging": "debug",
            "enabled": True,
            "lags": [
                {"lagPorts": ["1", "2"],
                 "enabled": True,
                 "lagPort": "1"}]
        },
        "syslog": {
            "logging": "debug",
            "enabled": True,
            "syslogConfig": [
                {"serverUdpPort": 162,
                 "serverNetworkAddress": "202.1.1.2"}]
        },
        "macauth": {
            "macAuthConfig": [
                {"macAuthPorts": ["1", "2", "3"],
                 "macAuthEnable": True},
                {"macAuthPorts": [],
                 "macAuthEnable": False}],
            "logging": "debug",
            "enabled": True
        },
        "poe": {
            "logging": "debug",
            "enabled": False,
            "ports": [
                {"priority": "critical",
                 "operatorLimit": "15400",
                 "enabled": True,
                 "detection": "bypass",
                 "poePortAlias": "1",
                 "portName": "1"},
                {"priority": "critical",
                 "operatorLimit": "15400",
                 "enabled": True,
                 "detection": "bypass",
                 "poePortAlias": "2",
                 "portName": "2"},
                {"priority": "critical",
                 "operatorLimit": "15400",
                 "enabled": True,
                 "detection": "bypass",
                 "poePortAlias": "3",
                 "portName": "3"}],
            "disconnectedPrecedence": "deny-port"
        },
        "lldp": {
            "tlvLocation": True,
            "systemName": "chill_test",
            "logging": "debug",
            "location": "cloud9",
            "mgmtAddress": "202.1.1.10",
            "tlvMgmtAddress": True,
            "lldpConfig": [
                {"lldpEnable": True,
                 "lldpPorts": ["1", "2"]},
                {"lldpEnable": False,
                 "lldpPorts": ["3"]}],
            "enabled": True,
            "tlvSystemName": True
        },
        "spanningTree": {
            "logging": "debug",
            "enabled": True,
            "bridgePriority": 32768,
            "portLinkType": [
                {"linkType": "auto",
                 "linkTypePorts": ["1", "2", "3"]},
                {"linkType": "broadcast",
                 "linkTypePorts": []},
                {"linkType": "point-to-point",
                 "linkTypePorts": []},
                {"linkType": "edge",
                 "linkTypePorts": []}],
            "version": "mstp",
            "loopProtect": [
                {"loopProtectEnabled": True,
                 "loopProtectPorts": ["1", "2", "3"]},
                {"loopProtectEnabled": False,
                 "loopProtectPorts": []}],
            "spanGuard": [
                {"spanGuardEnabled": False,
                 "spanGuardPorts": ["1", "2", "3"]},
                {"spanGuardEnabled": True,
                 "spanGuardPorts": []}]
        },
        "vlans": {
            "vlanConfig": [
                {"dynamic": False,
                 "igmp":
                     {"query": False,
                      "snooping": False},
                 "management": False,
                 "dynamicUntaggedEgressPorts": [],
                 "vlanIds": "1",
                 "dhcpClient": False,
                 "routing": False,
                 "dynamicTaggedEgressPorts": [],
                 "networkPrefixLength": 0,
                 "vlanId": 1,
                 "untaggedEgressPorts": ["1", "2", "3"],
                 "dnsServer": "",
                 "networkAddress": "",
                 "name": "Default",
                 "domainName": "",
                 "ntpServer": "",
                 "networkDefaultGateway": "",
                 "taggedEgressPorts": []},
                {"dhcpClient": False,
                 "networkAddress": "202.1.1.10",
                 "dnsServer": "202.1.1.2",
                 "domainName": "extremenetworks.com",
                 "role": "OutOfBandMgmt",
                 "ntpServer": "202.1.1.2",
                 "networkDefaultGateway": "202.1.1.2",
                 "networkPrefixLength": "24"}
            ]
        },
        "license": {
            "featurePacks": [
                {"featurePackLicense": "4e51-69d1-c7a4-2a95-6eee",
                 "featurePackName": "ServiceProviderEdge"}],
            "effectiveLevel": "Advanced Edge",
            "systemLicense": "4e51-69d1-c7a4-2a95-6fff"
        },
        "snmp": {
            "sysName": "chill_test",
            "snmpV2c": {
                "communities": [
                    {"accessLevel": "READ_WRITE",
                     "name": "publicv2"}],
                "logging": "debug",
                "enabled": True
            },
            "sysLocation": "cloud9",
            "sysContact": "chill@extremenetworks.com",
            "snmpV1": {
                "communities": [
                    {"accessLevel": "READ_ONLY",
                     "name": "public"}],
                "logging": "debug",
                "enabled": True
            },
            "snmpV3": {
                "logging": "none",
                "enabled": False,
                "users": [],
                "notifications": []
            }
        },
        "dot1x": {
            "logging": "debug",
            "dot1xConfig": [
                {"dot1xPorts": ["1", "2"],
                 "dot1xEnable": True},
                {"dot1xPorts": ["3"],
                 "dot1xEnable": False}
            ],
            "enabled": False
        },
        "mgmtAccess": {
            "httpConfig": {"httpEnabled": True},
            "httpsConfig": {"httpsEnabled": False},
            "sshConfig": {"sshEnabled": True},
            "telnetConfig": {"telnetEnabled": True}
        },
        "ports": [
            {"adminStatus": "on",
             "linkDuplexList": ["auto"],
             "ingressFiltering": "disabled",
             "nodeAlias": True,
             "mvrp": False,
             "portName": "1",
             "linkSpeed": "Auto",
             "admitRules": "admitAll",
             "portAlias": "1",
             "pvid": 1,
             "linkDuplex": "auto",
             "linkSpeedList": ["10", "100", "1G"]},
            {"adminStatus": "on",
             "linkDuplexList": ["auto"],
             "ingressFiltering": "disabled",
             "nodeAlias": True,
             "mvrp": False,
             "portName": "2",
             "linkSpeed": "Auto",
             "admitRules": "admitAll",
             "portAlias": "2",
             "pvid": 1,
             "linkDuplex": "auto",
             "linkSpeedList": ["10", "100", "1G"]},
            {"adminStatus": "on",
             "linkDuplexList": ["auto"],
             "ingressFiltering": "disabled",
             "nodeAlias": True,
             "mvrp": False,
             "portName": "3",
             "linkSpeed": "Auto",
             "admitRules": "admitAll",
             "portAlias": "3",
             "pvid": 1,
             "linkDuplex": "auto",
             "linkSpeedList": ["10", "100", "1G"]}
        ],
        "vxlan": {
            "logging": "error",
            "enabled": False
        },
        "radiusServers": [
            {"networkPort": 1812,
             "realmType": "management",
             "networkAddress": "202.1.1.2",
             "sharedKey": "BeExtreme!",
             "precedence": 1,
             "clientIP": "202.1.1.10"}
        ]
    }}


def merge_config_blocks(orig, new):
    for block in new:
        if block not in orig:
            orig[block] = new[block]
        elif isinstance(new[block], list) and len(new[block]) > 0 and isinstance(new[block][0], dict):
            if block == "vlanConfig":
                merged = {}
                for vlan in orig[block] + new[block]:
                    if "vlanId" in vlan:
                        if vlan["vlanId"] in merged:
                            merged[vlan["vlanId"]].update(vlan)
                        else:
                            merged[vlan["vlanId"]] = vlan
                    else:
                        if vlan["role"] in merged:
                            merged[vlan["role"]].update(vlan)
                        else:
                            merged[vlan["role"]] = vlan
                orig[block] = [val for (_, val) in merged.items()]
                print(orig[block])
            else:
                for new_item, orig_item in zip(new[block], orig[block]):
                    merge_config_blocks(orig_item, new_item)
        elif isinstance(new[block], dict):
            merge_config_blocks(orig[block], new[block])
        else:
            orig[block] = new[block]


original = CloudConnectUnitTestConstants.config_block_dut.copy()
newinal = CloudConnectUnitTestConstants.config_block_robot.copy()
merge_config_blocks(original, newinal)
