from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class ApiUtils(object):
    @staticmethod
    def exos_instance(sid):
        """Removes mst id if using the default instance."""
        if sid == "0":
            return ""
        return sid

    @staticmethod
    def exos_stp_mode(mode):
        """Returns the proper stp-mode for EXOS."""
        if mode in ["stp", "stpcompatible", "dot1d"]:
            stpmode = "dot1d"
        elif mode in ["rstp", "dot1w"]:
            stpmode = "dot1w"
        elif mode in ["mstp"]:
            stpmode = "mstp"
        else:
            stpmode = mode
        return stpmode

    @staticmethod
    def eos_stp_mode(mode):
        """Returns the proper stp-mode for EOS."""
        if mode in ["stp", "stpcompatible", "dot1d"]:
            stpmode = "stpcompatible"
        elif mode in ["rstp", "dot1w"]:
            stpmode = "rstp"
        elif mode in ["mstp"]:
            stpmode = "mstp"
        else:
            stpmode = mode
        return stpmode

    @staticmethod
    def voss_stp_mode(mode):
        """Returns the proper stp-mode for VOSS."""
        if mode in ["stp", "stpcompatible", "dot1d"]:
            stpmode = "stp-compatible"
        elif mode in ["rstp", "dot1w"]:
            stpmode = "rstp"
        elif mode in ["mstp"]:
            stpmode = "mstp"
        else:
            stpmode = mode
        return stpmode

    @staticmethod
    def state_on_off(state):
        """Returns a state of on||off."""
        if state in ["on", "enable", "true"]:
            new_state = "on"
        elif state in ["off", "disable", "false"]:
            new_state = "off"
        else:
            new_state = state
        return new_state

    @staticmethod
    def state_enable_disable(state):
        """Returns a state of enaable||disable."""
        if state in ["on", "enable", "true"]:
            new_state = "enable"
        elif state in ["off", "disable", "false"]:
            new_state = "disable"
        else:
            new_state = state
        return new_state

    @staticmethod
    def state_true_false(state):
        """Returns a state of true||false."""
        if state in ["on", "enable", "true"]:
            new_state = "true"
        elif state in ["off", "disable", "false"]:
            new_state = "false"
        else:
            new_state = state
        return new_state

    @staticmethod
    def state_no_empty(state):
        """Returns a state of 'empty string'||no."""
        if state in ["on", "enable", "true"]:
            new_state = ""
        elif state in ["off", "disable", "false"]:
            new_state = "no"
        else:
            new_state = state
        return new_state

    @staticmethod
    def exos_prio_mode(mode):
        """Returns the proper priority mode for EXOS."""
        if mode in ["8021t", "dot1t"]:
            exos_mode = "dot1t"
        elif mode in ["8021d", "dot1d"]:
            exos_mode = "dot1d"
        else:
            exos_mode = mode
        return exos_mode

    @staticmethod
    def eos_prio_mode(mode):
        """Returns the proper priority mode for EOS."""
        if mode in ["8021t", "dot1t"]:
            exos_mode = "8021t"
        elif mode in ["8021d", "dot1d"]:
            exos_mode = "8021d"
        else:
            exos_mode = mode
        return exos_mode

    @staticmethod
    def exos_upm_profile(lines):
        """Returns the UPM profile lines as a '||' separated command string."""
        cmd_string = "||".join(lines) if isinstance(lines, list) else lines

        return cmd_string + "||."

    @staticmethod
    def exos_ma_mode(mode):
        """Returns the proper multi-auth mode for EXOS."""
        if mode.lower() in ["optional", "auth-opt"]:
            return "optional"
        elif mode.lower() in ["required", "auth-reqd"]:
            return "required"
        else:
            return mode

    @staticmethod
    def eos_ma_mode(mode):
        """Returns the proper multi-auth mode for EOS."""
        if mode.lower() in ["optional", "auth-opt"]:
            return "auth-opt"
        elif mode.lower() in ["required", "auth-reqd"]:
            return "auth-reqd"
        else:
            return mode

    @staticmethod
    def exos_ma_agent(agent_type):
        """Returns the proper multi-auth agent for EXOS."""
        if agent_type.lower() in ["pwa", "web", "web-based"]:
            return "web-based"
        else:
            return agent_type

    @staticmethod
    def eos_ma_agent(agent_type):
        """Returns the proper multi-auth agent for EOS."""
        if agent_type.lower() in ["pwa", "web", "web-based"]:
            return "pwa"
        else:
            return agent_type

    @staticmethod
    def policy_vlan_append(append):
        """Adds or removes the 'append' option from the command string."""
        if append is not None:
            if isinstance(append, bool):
                if append:
                    append = "append"
                else:
                    append = ""
            else:
                if append.lower() in ["yes", "true", "append"]:
                    append = "append"
                else:
                    append = ""
        else:
            append = ""
        return append

    @staticmethod
    def policy_gen_rule(mask, port_string, storage_type, vlan, forward, drop, cos,
                        tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile):
        """Returns the generated policy rule as a command string."""
        rule_data = []

        # Check each optional argument, append entries that are set.
        if mask is not None:
            rule_data.append("mask")
            rule_data.append(mask)

        if port_string is not None:
            rule_data.append("port-string")
            rule_data.append(port_string)

        if storage_type is not None:
            rule_data.append("storage-type")
            rule_data.append(storage_type)

        # Only one of vlan, forward, and drop can be set on a rule at a time.
        if vlan is not None:
            rule_data.append("vlan")
            rule_data.append(vlan)
        elif forward is not None:
            if StringUtils.string_to_boolean(forward, default=False):
                rule_data.append("forward")
        elif drop is not None:
            if StringUtils.string_to_boolean(drop, default=False):
                rule_data.append("drop")

        if cos is not None:
            rule_data.append("cos")
            rule_data.append(cos)

        if tci_overwrite is not None:
            rule_data.append("tci-overwrite")
            rule_data.append(tci_overwrite)

        if mirror_destination is not None:
            rule_data.append("mirror-destination")
            rule_data.append(mirror_destination)

        if syslog is not None:
            rule_data.append("syslog")
            rule_data.append(syslog)

        if trap is not None:
            rule_data.append("trap")
            rule_data.append(trap)

        if disable_port is not None:
            rule_data.append("disable-port")
            rule_data.append(disable_port)

        if quarantine_profile is not None:
            rule_data.append("quarantine-profile")
            rule_data.append(quarantine_profile)

        return " ".join(rule_data)

    @staticmethod
    def policy_gen_rule_del(mask, port_string):
        """Returns the command string for deleting the policy rule."""
        rule_data = []

        # Check each optional argument, append entries that are set.
        if mask is not None:
            rule_data.append("mask")
            rule_data.append(mask)

        if port_string is not None:
            rule_data.append("port-string")
            rule_data.append(port_string)

        return " ".join(rule_data)

    @staticmethod
    def policy_gen_icmp6(icmp6_type, icmp6_code):
        """Returns the ICMPv6 type.code string."""
        if "0x" in icmp6_type and "0x" in icmp6_code:
            rule_args = icmp6_type + "-" + icmp6_code
        else:
            rule_args = icmp6_type + "." + icmp6_code
        return rule_args

    @staticmethod
    def policy_gen_icmp(icmp_type, icmp_code):
        """Returns the ICMP type.code string."""
        if "0x" in icmp_type and "0x" in icmp_code:
            rule_args = icmp_type + "-" + icmp_code
        else:
            rule_args = icmp_type + "." + icmp_code
        return rule_args

    @staticmethod
    def policy_gen_ip6dest(ipv6_addr, l4_port):
        """Returns the combined IPv6 Addresss and L4 port, if present."""
        rule_args = ipv6_addr if l4_port is None else ipv6_addr + "-" + l4_port
        return rule_args

    @staticmethod
    def policy_gen_ipaddr(ip_addr, l4_port):
        """Returns the combined IPv4 Addresss and L4 port, if present."""
        rule_args = ip_addr if l4_port is None else ip_addr + ":" + l4_port
        return rule_args

    @staticmethod
    def policy_gen_tcpip(ip_addr, tcp_port):
        """Returns the combined L4 port and IP Address, if present"""
        if ip_addr is None:
            rule_args = tcp_port
        elif ":" in ip_addr:
            rule_args = tcp_port + "-" + ip_addr
        else:
            rule_args = tcp_port + ":" + ip_addr
        return rule_args

    @staticmethod
    def eos_fdb_portlist(port):
        """Returns a joined portlist if a list() was provided."""
        port_eos = ";".join(port) if isinstance(port, list) else port
        return port_eos

    @staticmethod
    def exos_fdb_portlist(port):
        """Returns a joined portlist if a list() was provided."""
        port_exos = ",".join(port) if isinstance(port, list) else port
        return port_exos

    @staticmethod
    def exos_qos_profile(qos_profile):
        """Returns the EXOS style QOS profile name, if only a digit is provided."""
        ret_profile = "qp" + qos_profile if qos_profile.isdigit() else qos_profile
        return ret_profile

    @staticmethod
    def exos_ipsec_trap(snmp_trap):
        """Returns the 'snmp-trap' command option if not None."""
        return "snmp-trap" if snmp_trap else ""

    @staticmethod
    def exos_ipsec_duration(duration, snmp_trap, block):
        """Returns the command string for EXOS duration."""
        if "permanently" or "duration" in duration:
            dur_str = duration
        else:
            if duration is None:
                if snmp_trap or block:
                    dur_str = "permanently"
                else:
                    dur_str = ""
            else:
                if duration.isdigit():
                    dur_str = "duration " + str(duration)
                else:
                    dur_str = "permanently"
        return dur_str
