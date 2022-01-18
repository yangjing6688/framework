from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.cos.base.CosBaseCustomShowTools import \
    CosBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return CosCustomShowTools(device)


class CosCustomShowTools(CosBaseCustomShowTools):
    def __init__(self, device):
        super(CosCustomShowTools, self).__init__(device)

    def check_cos_state(self, output, args, **kwargs):
        output = output.lower()
        state = self.pw.get_value_by_offset(output, "class-of-service", 3)

        result = True if state == "enabled" else False
        return result, {"ret_cos_state": state}

    def check_port_group_exists(self, output, args, **kwargs):
        output = output.lower()
        group_list = args["group"].split(".")
        output = output.replace("port group name", "pgn")
        groups = self.pw.get_value_by_offset(output, "port group", 2).split(" ")
        types = self.pw.get_value_by_offset(output, "port type", 2).split(" ")

        for i in range(len(groups)):
            if groups[i].replace(":", "") == group_list[0] and types[i].replace(":", "") == group_list[1]:
                return True, {"ret_groups": str(groups),
                              "ret_types": str(types)}
        return False, {"ret_groups": str(groups),
                       "ret_types": str(types)}

    def check_cos_reference(self, output, args, **kwargs):
        output = output.lower()
        output = output.splitlines()

        references = list()

        for index, line in enumerate(output):
            if index > 2 and line != "":
                references.append(line[12:])

        value = None
        for entry in references:
            dev_reference = self.pw.get_value_by_offset(entry, "", 0)
            if dev_reference == args["reference"]:
                value = self.pw.get_value_by_offset(entry, "", 2)
                if value == args["rate_limiter"] or value == args["queue"]:
                    return True, {"ret_reference": value}
        return False, {"ret_reference": value}

    def check_cos_port_resource(self, output, args, **kwargs):
        configured = args.get("configured", True)
        output = output.lower()

        if "no entries found" in output:
            return False, None

        output = output.splitlines()

        resources = list()

        if args["unit"] in ["percentage", "percent", "%"]:
            args["unit"] = "perc"

        for index, line in enumerate(output):
            if index > 3 and line[12:] != "":
                resources.append(line[12:])

        dev_unit = None
        dev_rate = None
        for entry in resources:
            dev_resource = self.pw.get_value_by_offset(entry, "", 0)
            if dev_resource == args["cos_index"]:
                dev_unit = self.pw.get_value_by_offset(entry, "", 2)
                dev_rate = self.pw.get_value_by_offset(entry, "", 3)
                if dev_unit == args["unit"] and dev_rate == args["rate"]:
                    result = False
                    if configured:
                        result = True
                    return result, {"ret_unit": dev_unit,
                                    "ret_rate": dev_rate}

        result = True
        if configured:
            result = False
        return result, {"ret_unit": dev_unit,
                        "ret_rate": dev_rate}

    def check_cos_settings(self, output, args, **kwargs):
        output = output.lower()
        output = output.splitlines()

        result = False
        indexes = list()

        for i, line in enumerate(output):
            if line.find("-----") != -1:
                i += 1
                while len(output[i]) > 55:
                    indexes.append(output[i])
                    i += 1
                else:
                    break

        ret_dict = {"priority": None,
                    "tos": None,
                    "txq": None,
                    "irl": None,
                    "orl": None,
                    "drop_prec": None,
                    "flood_ctrl": None}
        for entry in indexes:
            dev_index = self.pw.get_value_by_offset(entry, "", 0)

            if dev_index == args["cos_index"]:
                ret_dict["priority"] = self.pw.get_value_by_offset(entry, "", 1)
                ret_dict["tos"] = self.pw.get_value_by_offset(entry, "", 2)
                ret_dict["txq"] = self.pw.get_value_by_offset(entry, "", 3)
                ret_dict["irl"] = self.pw.get_value_by_offset(entry, "", 4)
                ret_dict["orl"] = self.pw.get_value_by_offset(entry, "", 5)
                ret_dict["drop_prec"] = self.pw.get_value_by_offset(entry, "", 6)
                ret_dict["flood_ctrl"] = self.pw.get_value_by_offset(entry, "", 7)

                result = True
                if args.get("priority", None) is not None and result:
                    if ret_dict["priority"] != args["priority"]:
                        result = False
                if args.get("tos", None) is not None and result:
                    if ret_dict["tos"] != args["tos"]:
                        result = False
                if args.get("txq", None) is not None and result:
                    if ret_dict["txq"] != args["txq"]:
                        result = False
                if args.get("irl", None) is not None and result:
                    if ret_dict["irl"] != args["irl"]:
                        result = False
                if args.get("orl", None) is not None and result:
                    if ret_dict["orl"] != args["orl"]:
                        result = False
                if args.get("drop_prec", None) is not None and result:
                    if ret_dict["drop_prec"] != args["drop_prec"]:
                        result = False
                if args.get("flood_ctrl", None) is not None and result:
                    if ret_dict["flood_ctrl"] != args["flood_ctrl"]:
                        result = False
            if result:
                return True, ret_dict
        return result, ret_dict

    def check_port_group_ports(self, output, args, **kwargs):
        ports = self.pw.get_value_by_offset(output, "Assigned Ports", 2)
        ports = ports[1::]  # Remove leading ":".

        result = self.it.compare_port_values(ports, args["port"], self.inspect_constants.CONTAINS)

        return result, {"ret_ports": str(ports)}

    def check_txq_weights(self, output, args, **kwargs):
        weights = args["weights"].split(",")
        queues = self.__get_queue_list(output)

        try:
            for index, weight in enumerate(weights):
                if queues[index] == "llq":
                    if not weight == queues[index] and not weight == "0":
                        return False, {"ret_weights": str(queues)}
                elif not weight == queues[index]:
                    return False, {"ret_weights": str(queues)}
            return True, {"ret_weights": str(queues)}
        except IndexError:
            return False, {"ret_weights": str(queues)}

    def verify_port_priority(self, output, args, **kwargs):
        """
        The following function returns True if the priority value found in the output is equal to the priority
        argument provided.
        """
        priority_output = self.pw.get_value_by_offset(output, "is set to", 4)

        result = True if priority_output == args["priority"] else False
        return result, {"ret_priority": priority_output}

    @staticmethod
    def __get_queue_list(output):
        output = output.lower()
        output = output.replace("(slices/queue)", "").replace("[ ", "[")
        output = output.splitlines()

        queues = list()

        for i in range(len(output)):
            if output[i].find("slices/queue") != -1:
                tmp_queues = ""
                while output[i].find("percentage/queue") == -1:
                    tmp_queues += (output[i])
                    i += 1
                else:
                    j = 0
                    while tmp_queues.find("[" + str(j) + "]") != -1:
                        index = tmp_queues.find("[" + str(j) + "]")
                        if j < 9:
                            queues.append(tmp_queues[index + 5:index + 8].replace(" ", ""))
                        else:
                            queues.append(tmp_queues[index + 5:index + 9].replace(" ", ""))
                        j += 1
                    break
        return queues
