from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import json
import ipaddress


class PolicyData(object):
    @staticmethod
    def set_access_list_data(arg_dict):
        listname = arg_dict["list_name"]
        rulename = arg_dict["rule"]
        matchstr = arg_dict["match_string"]
        actionstr = arg_dict["action_string"]
        matchdata = ""
        matchlist = matchstr.split(" ")
        index = 0
        ipv4start = '"ipv4": {'
        ipv4flag = 0
        tcpstart = '"tcp": {'
        tcpflag = 0
        udpstart = '"udp": {'
        udpflag = 0
        tcporudpstart = '"tcp-or-udp": {'
        tcporudpdeststart = '"destination-port": {'
        tcporudpsourcestart = '"source-port": {'
        tcporudpflag = 0
        for match in matchlist:
            if "app-signature" == match:
                matchdata += ""
            elif "ether" == match:
                ethvalue = matchlist[index + 1]
                if "x" in ethvalue:
                    ethvalue = StringUtils.hex_str_to_int(ethvalue)
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = int(matchlist[index + 3])
                        binval = ""
                        for i in range(16):
                            if i < maskval:
                                binval = binval + "1"
                            else:
                                binval = binval + "0"
                        maskdecimal = int(binval, 2)
                        matchdata += '"eth": {"ethertype": ' + str(ethvalue) + ',"ethertype-mask": ' + \
                                     str(maskdecimal) + '},'
                    else:
                        matchdata += '"eth": {"ethertype": ' + str(ethvalue) + '},'
                else:
                    matchdata += '"eth": {"ethertype": ' + str(ethvalue) + '},'
            elif "icmp6type" == match:
                icmp6typeval = matchlist[index + 1]
                if "-" in icmp6typeval:
                    icmp6typelist = icmp6typeval.split("-")
                    type6 = int(icmp6typelist[0], 16)
                    code6 = int(icmp6typelist[1], 16)
                else:
                    icmp6typelist = icmp6typeval.split(".")
                    type6 = int(icmp6typelist[0])
                    code6 = int(icmp6typelist[1])
                matchdata += '"eth": {"ethertype": 34525},'
                maskval = "16"
                maskbin = ""
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
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
                matchdata += '"icmp": {"code": ' + str(finalcode) + ',"code-mask": ' + str(finalcodemask) + ',"type": '\
                             + str(finaltype) + ',"type-mask": ' + str(finaltypemask) + '},'
            elif "icmptype" == match:
                icmp4typeval = matchlist[index + 1]
                icmp4typelist = icmp4typeval.split(".")
                type4 = int(icmp4typelist[0])
                code4 = int(icmp4typelist[1])
                matchdata += '"eth": {"ethertype": 2048},'
                maskval = "16"
                maskbin = ""
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
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
                matchdata += '"icmp": {"code": ' + str(finalcode) + ',"code-mask": ' + str(finalcodemask) + ',"type": '\
                             + str(finaltype) + ',"type-mask": ' + str(finaltypemask) + '},'
            elif "ipdestsocket" == match:
                ipv4flag = 1
                origport = ""
                socketval = matchlist[index + 1].split(":")[0]
                if ":" in matchlist[index + 1]:
                    origport = matchlist[index + 1].split(":")[1]
                    maskval = "48"
                else:
                    maskval = "32"
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
                origmask = maskval
                if int(maskval) > 32:
                    tcporudpflag = 1
                    maskval = "32"
                    if int(origmask) < 48:
                        # do conversions
                        binport = '{0:16b}'.format(int(origport))
                        bitstochange = 48 - int(origmask)
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
                        tcporudpdeststart += '"lower-port": ' + str(portlowerdec) + ',"upper-port": ' + \
                                             str(portupperdec) + '},'
                        tcporudpstart += tcporudpdeststart
                    else:
                        # no conversion necessary because mask is 48
                        tcporudpdeststart += '"operator": "eq", "port": ' + str(origport) + '},'
                        tcporudpstart += tcporudpdeststart
                socketval += "/" + maskval
                ipv4start += '"destination-ipv4-network": "' + socketval + '",'
            elif "ipproto" == match:
                ipv4flag = 1
                protoval = matchlist[index + 1]
                if "x" in protoval:
                    protoval = StringUtils.hex_str_to_int(protoval)
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
                        protocolmaskbin = ""
                        for i in range(8):
                            if i < int(maskval):
                                protocolmaskbin += "1"
                            else:
                                protocolmaskbin += "0"
                        protocolmask = int(protocolmaskbin, 2)
                        protovalbin = '{0:08b}'.format(int(protoval))
                        resultingbin = ""
                        indexb = 1
                        for char in protovalbin:
                            if indexb <= int(maskval):
                                resultingbin += char
                            else:
                                resultingbin += "0"
                            indexb += 1
                        protoval = int(resultingbin, 2)
                        ipv4start += '"protocol": ' + str(protoval) + ',"protocol-mask": ' + str(protocolmask) + ','
                    else:
                        ipv4start += '"protocol": ' + str(protoval) + ','
                else:
                    ipv4start += '"protocol": ' + str(protoval) + ','
            elif "ipsourcesocket" == match:
                ipv4flag = 1
                origport = ""
                socketval = matchlist[index + 1].split(":")[0]
                if ":" in matchlist[index + 1]:
                    origport = matchlist[index + 1].split(":")[1]
                    maskval = "48"
                else:
                    maskval = "32"
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
                origmask = maskval
                if int(maskval) > 32:
                    tcporudpflag = 1
                    maskval = "32"
                    if int(origmask) < 48:
                        # do conversions
                        binport = '{0:16b}'.format(int(origport))
                        bitstochange = 48 - int(origmask)
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
                        tcporudpsourcestart += '"lower-port": ' + str(portlowerdec) + ',"upper-port": ' + \
                                               str(portupperdec) + '},'
                        tcporudpstart += tcporudpsourcestart
                    else:
                        # no conversion necessary because mask is 48
                        tcporudpsourcestart += '"operator": "eq", "port": ' + str(origport) + '},'
                        tcporudpstart += tcporudpsourcestart
                socketval += "/" + maskval
                ipv4start += '"source-ipv4-network": "' + socketval + '",'
            elif "iptos" == match:
                ipv4flag = 1
                tosval = matchlist[index + 1]
                if "x" in tosval:
                    tosval = StringUtils.hex_str_to_int(tosval)
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
                    else:
                        maskval = "8"
                else:
                    maskval = "8"
                tosvalbin = '{0:08b}'.format(int(tosval))
                tosvalbinaftermask = ""
                for i in range(8):
                    if i < int(maskval):
                        tosvalbinaftermask += tosvalbin[i]
                    else:
                        tosvalbinaftermask += "0"
                maskbin = ""
                indexb = 1
                for i in range(8):
                    if indexb <= int(maskval):
                        maskbin += "1"
                    else:
                        maskbin += "0"
                    indexb += 1
                dscpmask = maskbin[0:6]
                ecnmask = maskbin[6:8]
                dscpmaskdec = int(dscpmask, 2)
                ecnmaskdec = int(ecnmask, 2)
                dscpbin = tosvalbinaftermask[0:6]
                dscpdec = int(dscpbin, 2)
                if int(maskval) <= 6:
                    ipv4start += '"dscp": ' + str(dscpdec) + ',"dscp-mask": ' + str(dscpmaskdec) + ','
                else:
                    ecnbin = tosvalbinaftermask[6:8]
                    ecndec = int(ecnbin, 2)
                    ipv4start += '"dscp": ' + str(dscpdec) + ',"dscp-mask": ' + str(dscpmaskdec) + ',"ecn": ' + \
                                 str(ecndec) + ',"ecn-mask": ' + str(ecnmaskdec) + ','
            elif "ipttl" == match:
                ipv4flag = 1
                ttlval = matchlist[index + 1]
                if "x" in ttlval:
                    ttlval = StringUtils.hex_str_to_int(ttlval)
                maskval = "255"
                calcmask = ""
                if index + 2 < len(matchlist):
                    if matchlist[index + 2] == "mask":
                        maskval = matchlist[index + 3]
                        indexb = 1
                        for i in range(8):
                            if indexb <= int(maskval):
                                calcmask += "1"
                            else:
                                calcmask += "0"
                            indexb += 1
                        maskval = int(calcmask, 2)
                ipv4start += '"ttl": ' + str(ttlval) + ',"ttl-mask": ' + str(maskval) + ','
            elif "tcpdestportip" == match.lower():
                tcpflag = 1
                port = matchlist[index + 1].split(":")[0]
                origport = port
                origmask = "48"
                ip = ""
                if ":" in matchlist[index + 1]:
                    ip = matchlist[index + 1].split(":")[1]
                    maskval = "48"
                    if index + 2 < len(matchlist):
                        if matchlist[index + 2] == "mask":
                            maskval = matchlist[index + 3]
                    origmask = maskval
                if int(origmask) >= 16:
                    tcpstart += '"destination-port": {"operator": "eq", "port": ' + str(origport) + '},'
                    # now for ip address manipulation based on mask
                    if ip != "":
                        ipv4flag = 1
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
                        ipv4start += '"destination-ipv4-network": "' + ipwithmask + '",'
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
                    tcpstart += '"destination-port": {"lower-port": ' + str(portlowerdec) + ',"upper-port": ' + \
                                str(portupperdec) + '},'
            elif "tcpsourceportip" == match.lower():
                tcpflag = 1
                port = matchlist[index + 1].split(":")[0]
                origport = port
                origmask = "48"
                ip = ""
                if ":" in matchlist[index + 1]:
                    ip = matchlist[index + 1].split(":")[1]
                    maskval = "48"
                    if index + 2 < len(matchlist):
                        if matchlist[index + 2] == "mask":
                            maskval = matchlist[index + 3]
                    origmask = maskval
                if int(origmask) >= 16:
                    tcpstart += '"source-port": {"operator": "eq", "port": ' + str(origport) + '},'
                    # now for ip address manipulation based on mask
                    if ip != "":
                        ipv4flag = 1
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
                        ipv4start += '"source-ipv4-network": "' + ipwithmask + '",'
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
                    tcpstart += '"source-port": {"lower-port": ' + str(portlowerdec) + ',"upper-port": ' + \
                                str(portupperdec) + '},'
            elif "udpdestportip" == match.lower():
                udpflag = 1
                port = matchlist[index + 1].split(":")[0]
                origport = port
                origmask = "48"
                ip = ""
                if ":" in matchlist[index + 1]:
                    ip = matchlist[index + 1].split(":")[1]
                    maskval = "48"
                    if index + 2 < len(matchlist):
                        if matchlist[index + 2] == "mask":
                            maskval = matchlist[index + 3]
                    origmask = maskval
                if int(origmask) >= 16:
                    udpstart += '"destination-port": {"operator": "eq", "port": ' + str(origport) + '},'
                    # now for ip address manipulation based on mask
                    if ip != "":
                        ipv4flag = 1
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
                        ipv4start += '"destination-ipv4-network": "' + ipwithmask + '",'
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
                    udpstart += '"destination-port": {"lower-port": ' + str(portlowerdec) + ',"upper-port": ' + \
                                str(portupperdec) + '},'
            elif "udpsourceportip" == match.lower():
                udpflag = 1
                port = matchlist[index + 1].split(":")[0]
                origport = port
                origmask = "48"
                ip = ""
                if ":" in matchlist[index + 1]:
                    ip = matchlist[index + 1].split(":")[1]
                    maskval = "48"
                    if index + 2 < len(matchlist):
                        if matchlist[index + 2] == "mask":
                            maskval = matchlist[index + 3]
                    origmask = maskval
                if int(origmask) >= 16:
                    udpstart += '"source-port": {"operator": "eq", "port": ' + str(origport) + '},'
                    # now for ip address manipulation based on mask
                    if ip != "":
                        ipv4flag = 1
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
                        ipv4start += '"source-ipv4-network": "' + ipwithmask + '",'
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
                    udpstart += '"source-port": {"lower-port": ' + str(portlowerdec) + ',"upper-port": ' + \
                                str(portupperdec) + '},'
            elif "ipfrag" == match:
                ipv4flag = 1
                ipv4start += '"flags": "fragment",'
            index = index + 1
        if ipv4flag == 1:
            ipv4start = ipv4start.rstrip(",")
            ipv4start += '},'
            if tcporudpflag == 1:
                tcporudpstart = tcporudpstart.rstrip(",")
                ipv4start += tcporudpstart + '},'
            matchdata += ipv4start
        if tcpflag == 1:
            tcpstart = tcpstart.rstrip(",")
            tcpstart += '},'
            matchdata += tcpstart
        if udpflag == 1:
            udpstart = udpstart.rstrip(",")
            udpstart += '},'
            matchdata += udpstart
        matchdata = matchdata.rstrip(",")
        actiondata = ""
        actionlist = actionstr.split(" ")
        index = 0
        for action in actionlist:
            if "cos" == action:
                actiondata += '"cos": ' + actionlist[index + 1] + ','
            elif "drop" == action:
                actiondata += '"forwarding": "drop",'
            elif "forward" == action:
                actiondata += '"forwarding": "accept",'
            elif "mirror-destination" == action:
                actiondata += '"mirror-dest": ' + actionlist[index + 1] + ','
            elif "syslog" == action:
                actiondata += '"logging": "log-syslog",'
            elif "trap" == action:
                actiondata += '"trap": "trap-enable",'
            index = index + 1
        actiondata = actiondata.rstrip(",")
        data = """{
                   "ietf-access-control-list:acls": {
                     "acl": [
                       {
                         "aces": {
                           "ace": [
                             {
                               "actions": {
                                 """ + actiondata + """
                               },
                               "matches": {
                                 """ + matchdata + """
                               },
                               "name": \"""" + rulename + """\"
                             }
                           ]
                         },
                         "application": "extr-acl:policy-application",
                         "name": \"""" + listname + """\",
                         "type": "acl:mixed-eth-ipv4-ipv6-acl-type"
                       }]}}"""
        data = json.loads(data)
        return data

    @staticmethod
    def clear_access_list_all_data(arg_dict):
        pass

    @staticmethod
    def clear_access_list_data(arg_dict):
        pass

    @staticmethod
    def clear_access_list_rule_data(arg_dict):
        pass

    @staticmethod
    def show_access_list_rule_name_data(arg_dict):
        pass

    @staticmethod
    def show_access_list_list_name_data(arg_dict):
        pass
