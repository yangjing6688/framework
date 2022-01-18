from ExtremeAutomation.Library.ParsingHelper.InspectionConstants import InspectionConstants
from ExtremeAutomation.Library.ParsingHelper.PortParsers.PortParserBaseClass import PortParserBaseClass


class PortParser(PortParserBaseClass):
    def sort_ports(self):
        """
        Sorts the current port_list into numerical order.
        """
        self.port_list = sorted(self.port_list)

    @staticmethod
    def normalize_port_value(portlist):
        """
        Converts the portlist for slot:port differences.
        """
        if "." not in portlist:
            if "-" not in portlist:
                portlist = "ge.1." + portlist
            else:
                portrange = portlist.split("-")
                portlist = "ge.1." + portrange[0] + portrange[1]
        portlist = portlist.replace(",[]*([A-za-z])", ";$1")
        return portlist

    def init_port(self):
        """
        Sets the init values for the current port block.
        """
        self.media_types["eth"] = self.speed_10_array
        self.media_types["fe"] = self.speed_100_array
        self.media_types["ge"] = self.speed_1000_array
        self.media_types["host"] = self.speed_10_array
        if "none" not in self.port_block_ports \
                and "invalid" not in self.port_block_ports \
                and "any" not in self.port_block_ports:
            self.expand_master_port_list(self.port_block_ports)
        else:
            self.port_slot = self.port_block_ports
            self.media_type = self.port_block_ports
            self.port_speed = self.port_block_ports
            self.port_list = []
        self.sort_ports()

    def get_port_flags(self, port):
        """
        Returns the flags for the given port.
        """
        flaglist = ""
        v = self.port_flag_dict[port]
        if v is not None:
            for flag in v:
                flaglist += flag
        return flaglist

    def strip_and_store_flags(self, port):
        """
        Removes the flags from the port string and stores them in the port_flag_dict.
        """
        new_port_list = port.replace("[^\\d.:,-]", "")
        if "emptyCliReturn" in port or "notpresent" in port.lower():
            return port
        else:
            portlist = port.split(",")
            for portrange in portlist:
                portrange = portrange.split(":")[1]
                i_list = []
                if "-" in portlist:
                    i = int(portrange.split("-")[0].replace("[^\\d.]", ""))
                    endrange = int(portrange.split("-")[1].replace("[^\\d.]", ""))
                    while i < endrange:
                        i_list.append(i)
                        i += 1
                else:
                    cleanportrange = portrange.replace("[^\\d.]", "")
                    i_list.append(cleanportrange)
                for p in i_list:
                    p = str(p)
                    flaglist = list()
                    flaglist.append("notSupported")
                    self.port_flag_dict[p] = flaglist
            return new_port_list

    def expand_master_port_list(self, masterportlist):
        """
        Expands the portlist to the full individual ports list, no ranges.
        """
        portvec = []
        portdict = {}
        portblocks = masterportlist.split(";")
        for portblock in portblocks:
            media = portblock.split(".")[0]
            ex = self.expand_port_list(portblock)
            if portdict.keys().__len__() == 0:
                portdict = ex
            else:
                for key in ex.keys():
                    if key in portdict.keys():
                        current_list = portdict[key]
                        for elem in ex[key]:
                            current_list.append(elem)
                        portdict[key] = current_list
                    else:
                        portdict[key] = ex[key]
            for portslot in portdict.keys():
                self.port_block_dict[media + "SLOT" + str(portslot)] = portdict[portslot]
            slots = self.port_block_dict.keys()
            for slot in slots:
                portlist = self.port_block_dict[slot]
                for port in portlist:
                    portvec.append(port)
        self.port_list = list(set(portvec))

    def expand_port_list(self, portlist):
        """
        Expands the portlist to the full individual ports list, no ranges.
        """
        portdict = {}
        if portlist != "None":
            mediatype = portlist.split(".")[0] + "."
            mediaarray = portlist.split(mediatype)
            for media in mediaarray:
                try:
                    if len(media) == 0:
                        continue
                    slotsnports = media.split(".")
                    slotstringlist = slotsnports[0].split(",")
                    portstringlist = slotsnports[1].split(",")
                    slots = []
                    ports = []
                    for slotstr in slotstringlist:
                        if "*" in slotstr:
                            slots.append(-1)
                        else:
                            slotstr = self.expand_num_range(slotstr)
                            slots.extend(slotstr)
                    for portstr in portstringlist:
                        if "*" in portstr:
                            ports.append(-1)
                        else:
                            portstr = self.expand_num_range(portstr)
                            ports.extend(portstr)
                    for slot in slots:
                        if slot == -1:
                            sslot = "*"
                        else:
                            sslot = str(slot)
                        mediaslotportlist = []
                        if slot in portdict.keys():
                            slotnportalreadyinhash = portdict[str(slots[slot])]
                            for snp in slotnportalreadyinhash:
                                mediaslotportlist.append(snp)
                        for port in ports:
                            if port == -1:
                                sport = "*"
                            else:
                                sport = str(port)
                            mediaslotportlist.append(mediatype + str(sslot) + "." + str(sport))
                        portdict[sslot] = mediaslotportlist
                except IndexError:
                    pass
        return portdict

    def collapse_port_list(self):
        """
        Collapses the portlist, combining ports on the same slot.
        """
        ilist = []
        prefixlist = []
        currentportassembly = ""
        slots = sorted(self.port_block_dict.keys())
        if len(slots) > 0:
            for slot in slots:
                currentportrange = []
                portlist = self.port_block_dict[slot]
                porttype = portlist[0].split(".")[0]
                portslot = portlist[0].split(".")[1]
                prefixlist.append(porttype + "." + portslot + ".")
                self.logger.log_info(portlist)
                for port in portlist:
                    p = int(port.split(".")[2])
                    ilist.append(p)
                previousval = 0
                for currentval in ilist:
                    if previousval != 0:
                        if currentval == previousval + 1:
                            currentportrange.append(currentval)
                        else:
                            if len(currentportrange) != 0:
                                if len(currentportrange) == 1:
                                    currentportassembly += (str(porttype) + "." + str(portslot) + "." +
                                                            str(currentportrange[0]) + ",")
                                else:
                                    currentportassembly += (str(porttype) + "." + str(portslot) + "." +
                                                            str(currentportrange[0]) + "-" +
                                                            str(currentportrange[len(currentportrange) - 1]) + ",")
                                currentportrange = list()
                                currentportrange.append(currentval)
                            else:
                                currentportrange.append(currentval)
                    else:
                        currentportrange.append(currentval)
                    previousval = currentval
                if len(currentportrange) != 0:
                    if len(currentportrange) == 1:
                        currentportassembly += str(porttype) + "." + str(portslot) + "." + str(currentportrange[0])
                    else:
                        currentportassembly += (str(porttype) + "." + str(portslot) + "." + str(currentportrange[0]) +
                                                "-" + str(currentportrange[len(currentportrange) - 1]))
                currentportassembly += ";"
            for pv in prefixlist:
                currentportassembly = currentportassembly.replace("," + pv.replace("\\.", "\\\\."), ",")
            currentportassembly = currentportassembly[:-1]
        else:
            if "none" in self.port_block_ports:
                currentportassembly = "None"
            else:
                currentportassembly = "Invalid"
        return currentportassembly

    def is_port_on_list(self, portlist):
        """
        Returns True if the given port(s) are in the current port_list.
        """
        if isinstance(portlist, str):
            portlist = PortParser(portlist)
        filterpass = False
        outofrange = False
        incominglist = portlist.port_list
        thislist = self.port_list
        for incomingport in incominglist:
            currentmatch = False
            for thisport in thislist:
                mediamatch = False
                slotmatch = False
                portmatch = False
                iport = incomingport.split(".")
                tport = thisport.split(".")
                if iport[0] == tport[0] or iport[0] == "*" or tport[0] == "*":
                    mediamatch = True
                if iport[1] == tport[1] or iport[1] == "*" or tport[1] == "*":
                    slotmatch = True
                if iport[2] == tport[2] or iport[2] == "*" or tport[2] == "*":
                    portmatch = True
                if mediamatch is True and slotmatch is True and portmatch is True:
                    currentmatch = True
            if currentmatch is True:
                filterpass = True
            else:
                outofrange = True
        if outofrange is True:
            filterpass = False
        return filterpass

    def add(self, portlist):
        """
        Adds the given port(s) to the current port_list.
        """
        addblocks = portlist.get_port_blocks()
        slots = addblocks.keys()
        for slot in slots:
            comparekey = slot
            if comparekey in self.port_block_dict:
                combovec = []
                vecone = self.port_block_dict[comparekey]
                vectwo = addblocks[comparekey]
                for p in vecone:
                    combovec.append(p)
                for p in vectwo:
                    combovec.append(p)
                self.port_block_dict[slot] = combovec
            else:
                self.port_block_dict[slot] = addblocks[comparekey]
        updatevec = []
        slots = self.port_block_dict.keys()
        for slot in slots:
            for p in self.port_block_dict[slot]:
                updatevec.append(p)
        self.port_list = updatevec

    def subtract(self, portlist):
        """
        Removes the given port(s) from the current port_list.
        """
        subtractblocks = portlist.get_port_blocks()
        slots = subtractblocks.keys()
        for slot in slots:
            comparekey = slot
            if comparekey in self.port_block_dict:
                subtractedvec = []
                subtractstring = ""
                vecone = self.port_block_dict[comparekey]
                vectwo = subtractblocks[comparekey]
                for sp in vectwo:
                    subtractstring += sp + " "
                for p in vecone:
                    match = False
                    for subp in subtractstring.split(" "):
                        if p == subp:
                            match = True
                    if match is False:
                        subtractedvec.append(p)
                if len(subtractedvec) != 0:
                    del self.port_block_dict[slot]
                    if len(subtractedvec) == 1 and subtractedvec[0] == "":
                        del self.port_block_dict[slot]
                    else:
                        self.port_block_dict[slot] = subtractedvec
        updatevec = []
        slots = self.port_block_dict.keys()
        for slot in slots:
            for p in self.port_block_dict[slot]:
                updatevec.append(p)
        self.port_list = updatevec

    def compare_ports(self, pblock, operand):
        """
        Compare port lists using the specified operand type.
        """
        isoperandtrue = False
        mismatchdetected = False
        if operand != InspectionConstants.FOUNDIN and operand != InspectionConstants.NOTFOUNDIN:
            myports = self.port_list
            yourports = pblock.get_port_list()
            for mport in myports:
                mportcomponents = mport.split("\\.")
                mportslot = mportcomponents[1]
                mportport = mportcomponents[2]
                for yport in yourports:
                    yportcomponents = yport.split("\\.")
                    yportslot = yportcomponents[1]
                    yportport = yportcomponents[2]
                    if operand == InspectionConstants.EQUALTO:
                        isyslotequal = False
                        isyportequal = False
                        if yportslot == "*" or mportslot == "*":
                            isyslotequal = True
                        if yportport == "*" or mportport == "*":
                            isyportequal = True
                        if (yportslot != "*" and mportslot != "*") and yportslot == mportslot:
                            isyslotequal = True
                        if (yportport != "*" and mportport != "*") and yportport == mportport:
                            isyportequal = True
                        if isyslotequal and isyportequal:
                            mismatchdetected = False
                        else:
                            mismatchdetected = True
                    elif operand == InspectionConstants.NOTEQUALTO:
                        isyslotequal = False
                        isyportequal = False
                        if yportslot == "*" or mportslot == "*":
                            isyslotequal = True
                        if yportport == "*" or mportport == "*":
                            isyportequal = True
                        if (yportslot != "*" and mportslot != "*") and yportslot == mportslot:
                            isyslotequal = True
                        if (yportport != "*" and mportport != "*") and yportport == mportport:
                            isyportequal = True
                        if isyslotequal and isyportequal:
                            mismatchdetected = True
                        else:
                            mismatchdetected = False
                    elif operand == InspectionConstants.LESSTHAN:
                        isyslotlt = False
                        isyportlt = False
                        if yportslot == "*" or mportslot == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand LESSTHAN")
                        elif yportport == "*" or mportport == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand LESSTHAN")
                        else:
                            yportslotint = int(yportslot)
                            yportportint = int(yportport)
                            mportslotint = int(mportslot)
                            mportportint = int(mportport)
                            if yportslotint <= mportslotint:
                                isyslotlt = True
                            if yportportint < mportportint:
                                isyportlt = True
                        if not isyslotlt:
                            mismatchdetected = True
                        if isyslotlt:
                            if not isyportlt:
                                mismatchdetected = True
                    elif operand == InspectionConstants.GREATERTHAN:
                        isyslotgt = False
                        isyportgt = False
                        if yportslot == "*" or mportslot == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand GREATERTHAN")
                        elif yportport == "*" or mportport == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand GREATERTHAN")
                        else:
                            yportslotint = int(yportslot)
                            yportportint = int(yportport)
                            mportslotint = int(mportslot)
                            mportportint = int(mportport)
                            if yportslotint >= mportslotint:
                                isyslotgt = True
                            if yportportint > mportportint:
                                isyportgt = True
                        if not isyslotgt:
                            mismatchdetected = True
                        if isyslotgt:
                            if not isyportgt:
                                mismatchdetected = True
                    elif operand == InspectionConstants.LESSTHANOREQUALTO:
                        isyslotlte = False
                        isyportlte = False
                        if yportslot == "*" or mportslot == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand "
                                                  "LESSTHANOREQUALTO")
                        elif yportport == "*" or mportport == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand "
                                                  "LESSTHANOREQUALTO")
                        else:
                            yportslotint = int(yportslot)
                            yportportint = int(yportport)
                            mportslotint = int(mportslot)
                            mportportint = int(mportport)
                            if yportslotint <= mportslotint:
                                isyslotlte = True
                            if yportportint <= mportportint:
                                isyportlte = True
                        if not isyslotlte:
                            mismatchdetected = True
                        if isyslotlte:
                            if not isyportlte:
                                mismatchdetected = True
                    elif operand == InspectionConstants.GREATERTHANOREQUALTO:
                        isyslotgte = False
                        isyportgte = False
                        if yportslot == "*" or mportslot == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand "
                                                  "GREATERTHANOREQUALTO")
                        elif yportport == "*" or mportport == "*":
                            self.logger.log_trace("EosPortParser: Wildcards not supported with operand "
                                                  "GREATERTHANOREQUALTO")
                        else:
                            yportslotint = int(yportslot)
                            yportportint = int(yportport)
                            mportslotint = int(mportslot)
                            mportportint = int(mportport)
                            if yportslotint >= mportslotint:
                                isyslotgte = True
                            if yportportint >= mportportint:
                                isyportgte = True
                        if not isyslotgte:
                            mismatchdetected = True
                        if isyslotgte:
                            if not isyportgte:
                                mismatchdetected = True
                    else:
                        raise ValueError("EosPortParser.compare_ports(pBlock, operand: Invalid operand (" +
                                         operand + ")")
                    if mismatchdetected:
                        break
                if mismatchdetected:
                    break
        else:
            if operand == InspectionConstants.FOUNDIN:
                if self.is_port_on_list(pblock):
                    isoperandtrue = True
                else:
                    mismatchdetected = True
            elif operand == InspectionConstants.NOTFOUNDIN:
                if self.is_port_on_list(pblock):
                    isoperandtrue = False
                    mismatchdetected = True
            else:
                raise ValueError("EosPortParser.compare_ports(pBlock, operand: Invalid operand (" + operand + ")")
        if not mismatchdetected:
            isoperandtrue = True
        return isoperandtrue

    def print_port_list(self):
        """
        Logs the current port_list.
        """
        for port in self.port_list:
            self.logger.log_info(port)

    @staticmethod
    def expand_num_range(rng):
        """
        Expands a port index range into its individual ports.
        """
        r = []
        for i in rng.split(","):
            if "-" not in i:
                r.append(int(i))
            else:
                l, h = map(int, i.split("-"))
                r += range(l, h + 1)
        return r
