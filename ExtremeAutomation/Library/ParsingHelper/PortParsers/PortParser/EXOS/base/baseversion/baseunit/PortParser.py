from ExtremeAutomation.Library.ParsingHelper.InspectionConstants import InspectionConstants
from ExtremeAutomation.Library.ParsingHelper.PortParsers.PortParserBaseClass import PortParserBaseClass


class PortParser(PortParserBaseClass):
    def sort_ports(self):
        """
        Sorts the current port_list into numerical order.
        """
        self.port_list = sorted(self.port_list)

    def normalize_port_value(self, portlist):
        """
        Converts the portlist for slot:port differences.
        """
        if portlist.lower() == "none":
            return portlist
        if portlist == "-":
            return "none"
        if ":" not in portlist and "," not in portlist:
            portlist = "1:" + portlist
            portlist = self.strip_and_store_flags(portlist.replace(".", ""))
        else:
            normalizedgroup = ""
            splitslot = portlist.split(",")
            for s in splitslot:
                slot = "1:"
                splitport = s.split(",")
                for p in splitport:
                    if ":" in p:
                        slot = p.split(":")[0] + ":"
                    else:
                        p = slot + p.strip()
                    p += ","
                    normalizedgroup += p
            portlist = normalizedgroup[0:-1]
            portlist = self.strip_and_store_flags(portlist.replace(".", ""))
        return portlist

    def init_port(self):
        """
        Sets the init values for the current port block.
        """
        if "none" not in self.port_block_ports.lower() and \
                "invalid" not in self.port_block_ports.lower() and \
                "any" not in self.port_block_ports.lower():
            self.expand_master_port_list(self.port_block_ports)
        else:
            self.port_slot = self.port_block_ports
            self.media_type = self.port_block_ports
            self.port_speed = self.port_block_ports
            self.port_list = []

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
        portslot = "1"
        portrange = ""
        newportlist = port.replace("[^\\d.:,-]", "")
        if "emptyCliReturn" in port or "notpresent" in port.lower():
            return port
        else:
            portlist = port.split(",")
            for portrange in portlist:
                portrangelist = portrange.strip().split(":")
                portslot = "1"  # Default to 1 to support non-stacked units
                if len(portrangelist) == 2:
                    portslot = portrangelist[0]  # If the port uses the stacked format, populate slot and port
                    portrange = portrangelist[1]
                elif len(portrangelist) == 1:
                    # If the port uses the non-stacked format, populate port (keep default slot of 1)
                    portrange = portrangelist[0]
                else:
                    return "malformed port (" + port + ")"
            portslotflags = portslot.replace("[0-9]", "")
            portslot = portslot.replace("\\D+", "")
            portrange += portslotflags
            ilist = []
            if "-" in portrange:
                i = int(portrange.split("-")[0].replace("[^\\d.]", ""))
                endrange = int(portrange.split("-")[1].replace("[^\\d.]", ""))
                ilist += range(i, endrange)
            else:
                cleanportrange = portrange.replace("[^\\d.]", "")
                ilist.append(cleanportrange)
            for i in ilist:
                p = str(i)
                flagvector = []
                if "*" in portrange:
                    flagvector.append("*")
                if "!" in portrange:
                    flagvector.append("!")
                if "m" in portrange:
                    flagvector.append("m")
                if "a" in portrange:
                    flagvector.append("a")
                if "U" in portrange:
                    flagvector.append("U")
                if "V" in portrange:
                    flagvector.append("V")
                if "e" in portrange:
                    flagvector.append("e")
                if "s" in portrange:
                    flagvector.append("s")
                if "L" in portrange:
                    flagvector.append("L")
                if "u" in portrange:
                    flagvector.append("u")
                if "g" in portrange:
                    flagvector.append("g")
                if "H" in portrange:
                    flagvector.append("H")
                if "x" in portrange:
                    flagvector.append("x")
                if "G" in portrange:
                    flagvector.append("G")
                if "b" in portrange:
                    flagvector.append("b")
                if "t" in portrange:
                    flagvector.append("t")
                self.port_flag_dict[portslot + ":" + p] = flagvector
        return newportlist

    @staticmethod
    def strip_exos_flags(port):
        """
        Remove all EXOS specific flags from the port string.
        """
        if "emptyCliReturn" in port or "notpresent" in port.lower():
            return port
        else:
            port = port.replace("\\*", "")
            port = port.replace("!", "")
            port = port.replace("m", "")
            port = port.replace("a", "")
            port = port.replace("U", "")
            port = port.replace("V", "")
            port = port.replace("e", "")
            port = port.replace("s", "")
            port = port.replace("L", "")
            port = port.replace("u", "")
            port = port.replace("g", "")
            port = port.replace("H", "")
            port = port.replace("x", "")
            port = port.replace("G", "")
            port = port.replace("b", "")
            port = port.replace("t", "")
        return port

    def group_ports_by_slot(self, portlist):
        """
        Sorts the ports into group based on the device slot.
        """
        expandedportlist = ""
        for port in portlist.split(","):
            if "-" in port:
                if ":" in port:
                    splitport = port.split(":")
                    slot = splitport[0]
                    ports = ""
                    if port.count(":") == 2:
                        port_range = splitport[1].split("-")[0] + "-" + splitport[2]
                        ilist = self.expand_num_range(port_range)
                    else:
                        ilist = self.expand_num_range(splitport[1])
                    for i in ilist:
                        ports += slot + ":" + str(i) + ","
                    port = ports[0:-1]
                else:
                    slot = "1"
                    ports = ""
                    ilist = self.expand_num_range(port)
                    for i in ilist:
                        ports += slot + ":" + str(i) + ","
                    port = ports[0:-1]
            expandedportlist += port + ","
        portlist = expandedportlist[0:-1]
        portlist = portlist.split(",")
        return portlist

    def expand_master_port_list_simple(self, masterportlist):
        """
        Expands the portlist to the full individual ports list, no ranges.
        """
        ilist = []
        portlist = masterportlist.split(",")
        for port in portlist:
            port = port.strip().split(":")[1]
            if "-" in port:
                ilist = self.expand_num_range(port)
            else:
                ilist.append(port)
        self.port_block_ports = ", ".join(map(str, ilist))

    def expand_master_port_list(self, masterportlist):
        """
        Expands the portlist to the full individual ports list, no ranges.
        """
        portvec = []
        portblocks = masterportlist.split(",")
        for portblock in portblocks:
            # media = ""  # EXOS doesn"t seem to display media types
            portdict = self.expand_port_list(portblock)
            for portslot in portdict.keys():
                if "SLOT" + str(portslot) not in self.port_block_dict:
                    self.port_block_dict["SLOT" + str(portslot)] = portdict[portslot]
                else:
                    for elem in portdict[portslot]:
                        if elem not in self.port_block_dict["SLOT" + str(portslot)]:
                            self.port_block_dict["SLOT" + str(portslot)].append(elem)
            slots = self.port_block_dict.keys()
            for slot in slots:
                portlist = self.port_block_dict[slot]
                for port in portlist:
                    current_port = slot.replace("SLOT", "") + ":" + port
                    if current_port not in portvec:
                        portvec.append(current_port)
        self.port_list = sorted(portvec)

    def expand_port_list(self, portlist):
        """
        Expands the portlist to the full individual ports list, no ranges.
        """
        portdict = {}
        if portlist != "None":
            portarray = self.group_ports_by_slot(portlist)
            for portentry in portarray:
                portentry = portentry.replace(".", ":")
                if ":" not in portentry:
                    portentry = "1:" + portentry
                splitport = portentry.split(":")
                slot = splitport[0]
                port = splitport[1]
                if slot in portdict.keys():
                    slotvector = [port]
                    slotarray = portdict[slot]
                    for slotentry in slotarray:
                        slotvector.append(slotentry)
                    portdict[slot] = sorted(slotvector)
                else:
                    portdict[slot] = [port]
        return portdict

    def collapse_port_list(self):
        """
        Collapses the portlist, combining ports on the same slot.
        """
        curr_portblock = ""

        slots = sorted(self.port_block_dict.keys())
        if slots:
            for slot in slots:
                ilist = []
                curr_port_range = []
                portlist = self.port_block_dict[slot]

                for port in portlist:
                    if port:
                        try:
                            p = int(port)
                            ilist.append(p)
                        except ValueError:
                            pass
                ilist.sort(key=lambda x: int(x))
                previousval = 0
                for currentval in ilist:
                    if previousval != 0:
                        if currentval == previousval + 1:
                            curr_port_range.append(currentval)
                        else:
                            if len(curr_port_range) != 0:
                                if len(curr_port_range) == 1:
                                    curr_portblock += (slot.replace("SLOT", "") + ":" +
                                                       str(curr_port_range[0]) + ",")
                                else:
                                    curr_portblock += (slot.replace("SLOT", "") + ":" +
                                                       str(curr_port_range[0]) + "-" +
                                                       str(curr_port_range[len(curr_port_range) - 1]) + ",")
                                curr_port_range = [currentval]
                            else:
                                curr_port_range.append(currentval)
                    else:
                        curr_port_range.append(currentval)
                    previousval = currentval
                if len(curr_port_range) != 0:
                    if len(curr_port_range) == 1:
                        curr_portblock += slot.replace("SLOT", "") + ":" + str(curr_port_range[0])
                    else:
                        curr_portblock += (slot.replace("SLOT", "") + ":" + str(curr_port_range[0]) +
                                           "-" + str(curr_port_range[len(curr_port_range) - 1]))
                curr_portblock += ","
            curr_portblock = curr_portblock[:-1]
        else:
            if "none" in self.port_block_ports:
                curr_portblock = "None"
            else:
                curr_portblock = "Invalid"
        return curr_portblock

    def is_port_on_list(self, portlist):
        """
        Returns True if the given port(s) are in the current port_list.
        """
        if isinstance(portlist, str):
            portlist = PortParser(portlist)
        filterpass = True
        incominglist = portlist.port_list
        thislist = self.port_list
        # For now this supports one slot...I believe the format is 1:1
        for iport in incominglist:
            match = False
            for tport in thislist:
                if tport == iport:
                    match = True
                    break
            if not match:
                filterpass = False
                break
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
        subtractblocks = portlist.port_block_dict
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
        mportport = ""
        yportport = ""
        if operand != InspectionConstants.FOUNDIN and operand != InspectionConstants.NOTFOUNDIN:
            myports = pblock.get_port_list()
            yourports = pblock.port_list
            for mport in myports:
                mportcomponents = mport.split("\\.")
                mportslot = mportcomponents[2]
                for yport in yourports:
                    yportcomponents = yport.split("\\.")
                    yportslot = yportcomponents[2]
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
                        raise ValueError("EosPortParser.compare_ports(pBlock, operand: Invalid "
                                         "operand (" + operand + ")")
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

    def to_string(self):
        """
        Returns the current port_block_ports as a string.
        """
        # But really it does nothing and just returns the port block as is...
        return self.port_block_ports

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
