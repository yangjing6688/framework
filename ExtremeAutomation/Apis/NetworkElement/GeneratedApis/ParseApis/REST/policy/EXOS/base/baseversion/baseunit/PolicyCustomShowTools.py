from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.policy.base.PolicyBaseCustomShowTools import \
    PolicyBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import json
import ipaddress


def create_instance(device):
    return PolicyCustomShowTools(device)


class PolicyCustomShowTools(PolicyBaseCustomShowTools):
    def __init__(self, device):
        super(PolicyCustomShowTools, self).__init__(device)

    def check_policy_acl_app_sig(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_policy_acl_ether(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        ether = output['ietf-access-control-list:ace'][0]['matches']['eth']['ethertype']
        if "x" in args["ether"]:
            args["ether"] = StringUtils.hex_str_to_int(args["ether"])
        if args["mask"] and args["mask"] != "16":
            mask = output['ietf-access-control-list:ace'][0]['matches']['eth']['ethertype-mask']
            binval = ""
            for i in range(16):
                if i < int(args["mask"]):
                    binval = binval + "1"
                else:
                    binval = binval + "0"
            maskdec = int(binval, 2)
            result = ether == int(args["ether"]) and mask == maskdec
            return result, {"ret_ether": str(ether),
                            "ret_mask": str(mask)}
        else:
            result = ether == int(args["ether"])
            return result, {"ret_ether": str(ether)}

    def check_policy_acl_icmp6type(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        if "-" in args["icmp6type"]:
            icmp6typelist = args["icmp6type"].split("-")
            type6 = int(icmp6typelist[0], 16)
            code6 = int(icmp6typelist[1], 16)
        else:
            icmp6typelist = args["icmp6type"].split(".")
            type6 = int(icmp6typelist[0])
            code6 = int(icmp6typelist[1])
        maskval = "16"
        maskbin = ""
        if args["mask"]:
            maskval = args["mask"]
        for i in range(16):
            if i < int(maskval):
                maskbin += "1"
            else:
                maskbin += "0"
        indexb = 0
        typemask = maskbin[0:8]
        codemask = maskbin[8:16]
        type6bin = '{0:08b}'.format(type6)
        code6bin = '{0:08b}'.format(code6)
        type6aftermask = ""
        code6aftermask = ""
        for char in type6bin:
            if typemask[indexb] == "1":
                type6aftermask += char
            else:
                type6aftermask += "0"
            indexb += 1
        indexb = 0
        for char in code6bin:
            if codemask[indexb] == "1":
                code6aftermask += char
            else:
                code6aftermask += "0"
            indexb += 1
        finaltype = int(type6aftermask, 2)
        finalcode = int(code6aftermask, 2)
        finaltypemask = int(typemask, 2)
        finalcodemask = int(codemask, 2)
        code = ""
        resttype = ""
        mask = ""
        tmask = ""
        if finalcode != 0:
            code = output['ietf-access-control-list:ace'][0]['matches']['icmp']['code']
            if finalcode != int(code):
                return False, {"ret_code": str(code)}
        if finaltype != 0:
            resttype = output['ietf-access-control-list:ace'][0]['matches']['icmp']['type']
            if finaltype != int(resttype):
                return False, {"ret_resttype": str(resttype)}
        if finalcodemask != 255 and finalcodemask != 0:
            mask = output['ietf-access-control-list:ace'][0]['matches']['icmp']['code-mask']
            if finalcodemask != int(mask):
                return False, {"ret_cmask": str(mask)}
        if finaltypemask != 255:
            tmask = output['ietf-access-control-list:ace'][0]['matches']['icmp']['type-mask']
            if finaltypemask != int(tmask):
                return False, {"ret_tmask": str(tmask)}
        return True, {"ret_code": str(code),
                      "ret_resttype": str(resttype),
                      "ret_cmask": str(mask),
                      "ret_tmask": str(tmask)}

    def check_policy_acl_icmptype(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        icmp4typelist = args["icmptype"].split(".")
        type4 = int(icmp4typelist[0])
        code4 = int(icmp4typelist[1])
        maskval = "16"
        maskbin = ""
        if args["mask"]:
            maskval = args["mask"]
        for i in range(16):
            if i < int(maskval):
                maskbin += "1"
            else:
                maskbin += "0"
        indexb = 0
        typemask = maskbin[0:8]
        codemask = maskbin[8:16]
        type4bin = '{0:08b}'.format(type4)
        code4bin = '{0:08b}'.format(code4)
        type4aftermask = ""
        code4aftermask = ""
        for char in type4bin:
            if typemask[indexb] == "1":
                type4aftermask += char
            else:
                type4aftermask += "0"
            indexb += 1
        indexb = 0
        for char in code4bin:
            if codemask[indexb] == "1":
                code4aftermask += char
            else:
                code4aftermask += "0"
            indexb += 1
        finaltype = int(type4aftermask, 2)
        finalcode = int(code4aftermask, 2)
        finaltypemask = int(typemask, 2)
        finalcodemask = int(codemask, 2)
        code = ""
        resttype = ""
        mask = ""
        tmask = ""
        if finalcode != 0:
            code = output['ietf-access-control-list:ace'][0]['matches']['icmp']['code']
            if finalcode != int(code):
                return False, {"ret_code": str(code)}
        if finaltype != 0:
            resttype = output['ietf-access-control-list:ace'][0]['matches']['icmp']['type']
            if finaltype != int(resttype):
                return False, {"ret_resttype": str(resttype)}
        if finalcodemask != 255 and finalcodemask != 0:
            mask = output['ietf-access-control-list:ace'][0]['matches']['icmp']['code-mask']
            if finalcodemask != int(mask):
                return False, {"ret_cmask": str(mask)}
        if finaltypemask != 255:
            tmask = output['ietf-access-control-list:ace'][0]['matches']['icmp']['type-mask']
            if finaltypemask != int(tmask):
                return False, {"ret_tmask": str(tmask)}
        return True, {"ret_code": str(code),
                      "ret_resttype": str(resttype),
                      "ret_cmask": str(mask),
                      "ret_tmask": str(tmask)}

    def check_policy_acl_ipdestsocket(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        ipdest = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['destination-ipv4-network']
        masktoappend = "32"
        if ":" in args["ipdestsocket"]:
            args["ipdestsocket"] = args["ipdestsocket"].split(":")[0]
        if args["mask"]:
            if int(args["mask"]) < 32:
                masktoappend = args["mask"]
        ipdestcombostr = args["ipdestsocket"] + "/" + masktoappend
        result = ipdestcombostr == ipdest
        return result, {"ret_ipdest": ipdest}

    def check_policy_acl_ipfrag(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        ipfrag = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['flags']
        result = True if ipfrag == "fragment" else False
        return result, {"ret_ipfrag": ipfrag}

    def check_policy_acl_ipproto(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        protocol = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['protocol']
        protocol_mask = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['protocol-mask']
        ipproto = args["ipproto"]
        if "x" in ipproto:
            ipproto = StringUtils.hex_str_to_int(ipproto)
        if args["mask"]:
            givenmask = args["mask"]
        else:
            givenmask = "8"
        binmask = ""
        for i in range(8):
            if i < int(givenmask):
                binmask += "1"
            else:
                binmask += "0"
        finalmask = int(binmask, 2)
        if args["mask"]:
            result = int(ipproto) == protocol and finalmask == protocol_mask
            return result, {"ret_protocol": protocol,
                            "ret_mask": protocol_mask}
        else:
            result = int(ipproto) == protocol
            return result, {"ret_protocol": protocol}

    def check_policy_acl_ipsourcesocket(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        ipsource = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['source-ipv4-network']
        masktoappend = "32"
        if ":" in args["ipsourcesocket"]:
            args["ipsourcesocket"] = args["ipsourcesocket"].split(":")[0]
        if args["mask"]:
            if int(args["mask"]) < 32:
                masktoappend = args["mask"]
        ipsourcecombostr = args["ipsourcesocket"] + "/" + masktoappend
        result = ipsourcecombostr == ipsource
        return result, {"ret_ipsource": ipsource}

    def check_policy_acl_iptos(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        dscp = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['dscp']
        giventos = args["iptos"]
        if "x" in args["iptos"]:
            giventos = StringUtils.hex_str_to_int(args["iptos"])
        if args["mask"]:
            maskval = args["mask"]
        else:
            maskval = "8"
        tosvalbin = '{0:08b}'.format(int(giventos))
        tosvalbinaftermask = ""
        for i in range(8):
            if i < int(maskval):
                tosvalbinaftermask += tosvalbin[i]
            else:
                tosvalbinaftermask += "0"
        dscpbin = tosvalbinaftermask[0:6]
        dscpdec = int(dscpbin, 2)
        ecnbin = tosvalbinaftermask[6:8]
        ecndec = int(ecnbin, 2)
        if ecndec != 0:
            ecn = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['ecn']
            result = True if dscpdec == dscp and ecndec == ecn else False
            return result, {"ret_dscp": dscp, "ret_ecn": ecn}
        else:
            result = True if dscpdec == dscp else False
            return result, {"ret_dscp": dscp}

    def check_policy_acl_ipttl(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        ttl = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['ttl']
        ttl_mask = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['ttl-mask']
        giventtl = args["ttl"]
        if "x" in giventtl:
            giventtl = StringUtils.hex_str_to_int(args["ttl"])
        if args["mask"]:
            givenmask = args["mask"]
        else:
            givenmask = "8"
        maskbin = ""
        for i in range(8):
            if i < int(givenmask):
                maskbin += "1"
            else:
                maskbin += "0"
        maskdec = int(maskbin, 2)
        if args["mask"]:
            result = int(giventtl) == ttl and maskdec == ttl_mask
            return result, {"ret_ipttl": ttl,
                            "ret_mask": ttl_mask}
        else:
            result = True if int(giventtl) == ttl else False
            return result, {"ret_ipttl": ttl}

    def check_policy_acl_tcpdestportip(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        port = args["tcpdestportip"].split(":")[0]
        origport = port
        origmask = "48"
        ip = ""
        if ":" in args["tcpdestportip"]:
            ip = args["tcpdestportip"].split(":")[1]
            maskval = "48"
            if args["mask"]:
                maskval = args["mask"]
            origmask = maskval
        if int(origmask) >= 16:
            portfromoutput = output['ietf-access-control-list:ace'][0]['matches']['tcp']['destination-port']['port']
            # now for ip address manipulation based on mask
            if ip != "":
                if origmask == "48":
                    finalip = ip
                    finalmask = 32
                    ipwithmask = finalip + "/" + str(finalmask)
                else:
                    finalmask = int(origmask) - 16
                    # apply the mask to the ip
                    ipwithmask = ip + "/" + str(finalmask)
                    ipwithmask = ipaddress.ip_interface(ipwithmask)
                    ipwithmask = ipwithmask.network.compressed
                ipmaskfromoutput = output['ietf-access-control-list:ace'][0]['matches']['ipv4'][
                    'destination-ipv4-network']
                if str(portfromoutput) != str(origport) or str(ipmaskfromoutput) != str(ipwithmask):
                    return False, {"ret_port": str(portfromoutput),
                                   "ret_ipmask": str(ipmaskfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput),
                                  "ret_ipmask": str(ipmaskfromoutput)}
            else:
                if str(portfromoutput) != str(origport):
                    return False, {"ret_port": str(portfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput)}
        else:
            # need upper/lower port manipulation
            binport = '{0:16b}'.format(int(origport))
            bitstochange = 16 - int(origmask)
            upperbits = ""
            lowerbits = ""
            newbinport = ""
            for i in range(bitstochange):
                upperbits += "1"
                lowerbits += "0"
            indexb = 16 - bitstochange
            indexc = 1
            for char in binport:
                if indexc <= indexb:
                    newbinport += char
                indexc += 1
            newbinportupper = newbinport + upperbits
            newbinportlower = newbinport + lowerbits
            portupperdec = int(newbinportupper, 2)
            portlowerdec = int(newbinportlower, 2)
            lowerpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['tcp']['destination-port'][
                'lower-port']
            upperpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['tcp']['destination-port'][
                'upper-port']
            if str(lowerpfromoutput) != str(portlowerdec) or str(upperpfromoutput) != str(portupperdec):
                return False, {"ret_lowerport": str(lowerpfromoutput),
                               "ret_upperport": str(upperpfromoutput)}
            else:
                return True, {"ret_lowerport": str(lowerpfromoutput),
                              "ret_upperport": str(upperpfromoutput)}

    def check_policy_acl_tcpsourceportip(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        port = args["tcpsourceportip"].split(":")[0]
        origport = port
        origmask = "48"
        ip = ""
        if ":" in args["tcpsourceportip"]:
            ip = args["tcpsourceportip"].split(":")[1]
            maskval = "48"
            if args["mask"]:
                maskval = args["mask"]
            origmask = maskval
        if int(origmask) >= 16:
            portfromoutput = output['ietf-access-control-list:ace'][0]['matches']['tcp']['source-port']['port']
            # now for ip address manipulation based on mask
            if ip != "":
                if origmask == "48":
                    finalip = ip
                    finalmask = 32
                    ipwithmask = finalip + "/" + str(finalmask)
                else:
                    finalmask = int(origmask) - 16
                    # apply the mask to the ip
                    ipwithmask = ip + "/" + str(finalmask)
                    ipwithmask = ipaddress.ip_interface(ipwithmask)
                    ipwithmask = ipwithmask.network.compressed
                ipmaskfromoutput = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['source-ipv4-network']
                if str(portfromoutput) != str(origport) or str(ipmaskfromoutput) != str(ipwithmask):
                    return False, {"ret_port": str(portfromoutput),
                                   "ret_ipmask": str(ipmaskfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput),
                                  "ret_ipmask": str(ipmaskfromoutput)}
            else:
                if str(portfromoutput) != str(origport):
                    return False, {"ret_port": str(portfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput)}
        else:
            # need upper/lower port manipulation
            binport = '{0:16b}'.format(int(origport))
            bitstochange = 16 - int(origmask)
            upperbits = ""
            lowerbits = ""
            newbinport = ""
            for i in range(bitstochange):
                upperbits += "1"
                lowerbits += "0"
            indexb = 16 - bitstochange
            indexc = 1
            for char in binport:
                if indexc <= indexb:
                    newbinport += char
                indexc += 1
            newbinportupper = newbinport + upperbits
            newbinportlower = newbinport + lowerbits
            portupperdec = int(newbinportupper, 2)
            portlowerdec = int(newbinportlower, 2)
            lowerpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['tcp']['source-port'][
                'lower-port']
            upperpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['tcp']['source-port'][
                'upper-port']
            if str(lowerpfromoutput) != str(portlowerdec) or str(upperpfromoutput) != str(portupperdec):
                return False, {"ret_lowerport": str(lowerpfromoutput),
                               "ret_upperport": str(upperpfromoutput)}
            else:
                return True, {"ret_lowerport": str(lowerpfromoutput),
                              "ret_upperport": str(upperpfromoutput)}

    def check_policy_acl_udpdestportip(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        port = args["udpdestportip"].split(":")[0]
        origport = port
        origmask = "48"
        ip = ""
        if ":" in args["udpdestportip"]:
            ip = args["udpdestportip"].split(":")[1]
            maskval = "48"
            if args["mask"]:
                maskval = args["mask"]
            origmask = maskval
        if int(origmask) >= 16:
            portfromoutput = output['ietf-access-control-list:ace'][0]['matches']['udp']['destination-port']['port']
            # now for ip address manipulation based on mask
            if ip != "":
                if origmask == "48":
                    finalip = ip
                    finalmask = 32
                    ipwithmask = finalip + "/" + str(finalmask)
                else:
                    finalmask = int(origmask) - 16
                    # apply the mask to the ip
                    ipwithmask = ip + "/" + str(finalmask)
                    ipwithmask = ipaddress.ip_interface(ipwithmask)
                    ipwithmask = ipwithmask.network.compressed
                ipmaskfromoutput = output['ietf-access-control-list:ace'][0]['matches']['ipv4'][
                    'destination-ipv4-network']
                if str(portfromoutput) != str(origport) or str(ipmaskfromoutput) != str(ipwithmask):
                    return False, {"ret_port": str(portfromoutput),
                                   "ret_ipmask": str(ipmaskfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput),
                                  "ret_ipmask": str(ipmaskfromoutput)}
            else:
                if str(portfromoutput) != str(origport):
                    return False, {"ret_port": str(portfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput)}
        else:
            # need upper/lower port manipulation
            binport = '{0:16b}'.format(int(origport))
            bitstochange = 16 - int(origmask)
            upperbits = ""
            lowerbits = ""
            newbinport = ""
            for i in range(bitstochange):
                upperbits += "1"
                lowerbits += "0"
            indexb = 16 - bitstochange
            indexc = 1
            for char in binport:
                if indexc <= indexb:
                    newbinport += char
                indexc += 1
            newbinportupper = newbinport + upperbits
            newbinportlower = newbinport + lowerbits
            portupperdec = int(newbinportupper, 2)
            portlowerdec = int(newbinportlower, 2)
            lowerpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['udp']['destination-port'][
                'lower-port']
            upperpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['udp']['destination-port'][
                'upper-port']
            if str(lowerpfromoutput) != str(portlowerdec) or str(upperpfromoutput) != str(portupperdec):
                return False, {"ret_lowerport": str(lowerpfromoutput),
                               "ret_upperport": str(upperpfromoutput)}
            else:
                return True, {"ret_lowerport": str(lowerpfromoutput),
                              "ret_upperport": str(upperpfromoutput)}

    def check_policy_acl_udpsourceportip(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        port = args["udpsourceportip"].split(":")[0]
        origport = port
        origmask = "48"
        ip = ""
        if ":" in args["udpsourceportip"]:
            ip = args["udpsourceportip"].split(":")[1]
            maskval = "48"
            if args["mask"]:
                maskval = args["mask"]
            origmask = maskval
        if int(origmask) >= 16:
            portfromoutput = output['ietf-access-control-list:ace'][0]['matches']['udp']['source-port']['port']
            # now for ip address manipulation based on mask
            if ip != "":
                if origmask == "48":
                    finalip = ip
                    finalmask = 32
                    ipwithmask = finalip + "/" + str(finalmask)
                else:
                    finalmask = int(origmask) - 16
                    # apply the mask to the ip
                    ipwithmask = ip + "/" + str(finalmask)
                    ipwithmask = ipaddress.ip_interface(ipwithmask)
                    ipwithmask = ipwithmask.network.compressed
                ipmaskfromoutput = output['ietf-access-control-list:ace'][0]['matches']['ipv4']['source-ipv4-network']
                if str(portfromoutput) != str(origport) or str(ipmaskfromoutput) != str(ipwithmask):
                    return False, {"ret_port": str(portfromoutput),
                                   "ret_ipmask": str(ipmaskfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput),
                                  "ret_ipmask": str(ipmaskfromoutput)}
            else:
                if str(portfromoutput) != str(origport):
                    return False, {"ret_port": str(portfromoutput)}
                else:
                    return True, {"ret_port": str(portfromoutput)}
        else:
            # need upper/lower port manipulation
            binport = '{0:16b}'.format(int(origport))
            bitstochange = 16 - int(origmask)
            upperbits = ""
            lowerbits = ""
            newbinport = ""
            for i in range(bitstochange):
                upperbits += "1"
                lowerbits += "0"
            indexb = 16 - bitstochange
            indexc = 1
            for char in binport:
                if indexc <= indexb:
                    newbinport += char
                indexc += 1
            newbinportupper = newbinport + upperbits
            newbinportlower = newbinport + lowerbits
            portupperdec = int(newbinportupper, 2)
            portlowerdec = int(newbinportlower, 2)
            lowerpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['udp']['source-port'][
                'lower-port']
            upperpfromoutput = output['ietf-access-control-list:ace'][0]['matches']['udp']['source-port'][
                'upper-port']
            if str(lowerpfromoutput) != str(portlowerdec) or str(upperpfromoutput) != str(portupperdec):
                return False, {"ret_lowerport": str(lowerpfromoutput),
                               "ret_upperport": str(upperpfromoutput)}
            else:
                return True, {"ret_lowerport": str(lowerpfromoutput),
                              "ret_upperport": str(upperpfromoutput)}

    def check_policy_acl_action_cos(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        cos = output['ietf-access-control-list:ace'][0]['actions']['cos']

        result = True if cos == int(args["cos"]) else False
        return result, {"ret_cos": str(cos)}

    def check_policy_acl_action_mirror(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        mirror = output['ietf-access-control-list:ace'][0]['actions']['mirror-dest']

        result = True if mirror == int(args["mirror_index"]) else False
        return result, {"ret_mirror": str(mirror)}

    def check_policy_acl_action_drop(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        forwarding = output['ietf-access-control-list:ace'][0]['actions']['forwarding']

        result = True if forwarding == "drop" else False
        return result, {"ret_drop": forwarding}

    def check_policy_acl_action_forward(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        forwarding = output['ietf-access-control-list:ace'][0]['actions']['forwarding']

        result = True if forwarding == "accept" else False
        return result, {"ret_drop": forwarding}

    def check_policy_acl_action_trap_enabled(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        trap = output['ietf-access-control-list:ace'][0]['actions']['trap']

        result = True if trap == "trap-enable" else False
        return result, {"ret_trap": trap}

    def check_policy_acl_action_syslog_enabled(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        syslog = output['ietf-access-control-list:ace'][0]['actions']['logging']

        result = True if syslog == "log-syslog" else False
        return result, {"ret_syslog": syslog}

    def check_policy_acl_action_all(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        if 'trap' in output['ietf-access-control-list:ace'][0]['actions']:
            trap = output['ietf-access-control-list:ace'][0]['actions']['trap']
        else:
            trap = ""
        if 'logging' in output['ietf-access-control-list:ace'][0]['actions']:
            syslog = output['ietf-access-control-list:ace'][0]['actions']['logging']
        else:
            syslog = ""
        if 'forwarding' in output['ietf-access-control-list:ace'][0]['actions']:
            forwarding = output['ietf-access-control-list:ace'][0]['actions']['forwarding']
        else:
            forwarding = ""
        if 'cos' in output['ietf-access-control-list:ace'][0]['actions']:
            cos = output['ietf-access-control-list:ace'][0]['actions']['cos']
        else:
            cos = 0
        if 'mirror-dest' in output['ietf-access-control-list:ace'][0]['actions']:
            mir = output['ietf-access-control-list:ace'][0]['actions']['mirror-dest']
        else:
            mir = 0
        if args["ts"] is not None:
            givents = args["ts"].lower()
        else:
            givents = ""

        result = True
        if "s" in givents:
            if syslog != "log-syslog":
                result = False
        if "t" in givents:
            if trap != "trap-enable":
                result = False
        if args["vlan"] is not None:
            if args["vlan"].lower() == "drop":
                if forwarding != "drop":
                    result = False
            elif args["vlan"].lower() == "fwrd":
                if forwarding != "accept":
                    result = False
        if args["cos"] is not None:
            if int(args["cos"]) != cos:
                result = False
        if args["mir"] is not None:
            if int(args["mir"]) != mir:
                result = False
        return result, {"ret_trap": trap,
                        "ret_syslog": syslog,
                        "ret_drop": forwarding,
                        "ret_cos": str(cos),
                        "ret_mirror": str(mir)}

    def check_policy_acl_does_not_exist(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        output = json.dumps(output)
        result = "error" in output
        return result, result

    def check_policy_acl_rule_does_not_exist(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        output = json.dumps(output)
        result = "error" in output
        return result, result
